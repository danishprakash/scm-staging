import asyncio
import tempfile
from git.remote import Remote
from py_gitea_opensuse_org import (
    CreatePullRequestOption,
    RepositoryApi,
)
from git.repo import Repo

from scm_staging.webhook import AppConfig


async def create_pr_to_pool(pkg_name: str, user: str, repo_api: RepositoryApi) -> None:
    await repo_api.create_fork(owner="pool", repo=pkg_name)

    with tempfile.TemporaryDirectory() as tmp_dir:
        repo = Repo.clone_from(
            url=f"gitea@gitea.opensuse.org:{user}/{pkg_name}.git", to_path=tmp_dir
        )
        remote = Remote.create(
            repo=repo, name="rpm", url=f"https://gitea.opensuse.org/rpm/{pkg_name}"
        )
        remote.fetch()

        rpm_factory = repo.commit("rpm/factory")

        repo.git.reset("--hard", rpm_factory.hexsha)
        origin = repo.remote("origin")
        origin.push(force=True)

    await repo_api.repo_create_pull_request(
        "pool",
        pkg_name,
        CreatePullRequestOption(
            base="factory", head=f"{user}:factory", title="Sync package with rpm/"
        ),
    )


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "package_name",
        nargs=1,
        type=str,
        help="The name of the package for which a PR will be created",
    )

    args = parser.parse_args()

    conf = AppConfig.from_env()
    repo_api = RepositoryApi(api_client=conf._api_client)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            create_pr_to_pool(args.package_name[0], conf.bot_user, repo_api)
        )
    finally:
        loop.run_until_complete(conf.osc.teardown())