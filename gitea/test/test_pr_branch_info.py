# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.18.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import swagger_client
from swagger_client.models.pr_branch_info import PRBranchInfo  # noqa: E501
from swagger_client.rest import ApiException


class TestPRBranchInfo(unittest.TestCase):
    """PRBranchInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PRBranchInfo
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PRBranchInfo`
        """
        model = swagger_client.models.pr_branch_info.PRBranchInfo()  # noqa: E501
        if include_optional :
            return PRBranchInfo(
                label = '', 
                ref = '', 
                repo = swagger_client.models.repository.Repository(
                    allow_merge_commits = True, 
                    allow_rebase = True, 
                    allow_rebase_explicit = True, 
                    allow_rebase_update = True, 
                    allow_squash_merge = True, 
                    archived = True, 
                    avatar_url = '', 
                    clone_url = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    default_branch = '', 
                    default_delete_branch_after_merge = True, 
                    default_merge_style = '', 
                    description = '', 
                    empty = True, 
                    external_tracker = swagger_client.models.external_tracker.ExternalTracker(
                        external_tracker_format = '', 
                        external_tracker_regexp_pattern = '', 
                        external_tracker_style = '', 
                        external_tracker_url = '', ), 
                    external_wiki = swagger_client.models.external_wiki.ExternalWiki(
                        external_wiki_url = '', ), 
                    fork = True, 
                    forks_count = 56, 
                    full_name = '', 
                    has_issues = True, 
                    has_projects = True, 
                    has_pull_requests = True, 
                    has_wiki = True, 
                    html_url = '', 
                    id = 56, 
                    ignore_whitespace_conflicts = True, 
                    internal = True, 
                    internal_tracker = swagger_client.models.internal_tracker.InternalTracker(
                        allow_only_contributors_to_track_time = True, 
                        enable_issue_dependencies = True, 
                        enable_time_tracker = True, ), 
                    language = '', 
                    languages_url = '', 
                    mirror = True, 
                    mirror_interval = '', 
                    mirror_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    open_issues_count = 56, 
                    open_pr_counter = 56, 
                    original_url = '', 
                    owner = swagger_client.models.user.User(
                        active = True, 
                        avatar_url = '', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        email = '', 
                        followers_count = 56, 
                        following_count = 56, 
                        full_name = '', 
                        id = 56, 
                        is_admin = True, 
                        language = '', 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        location = '', 
                        login = '', 
                        login_name = 'empty', 
                        prohibit_login = True, 
                        restricted = True, 
                        starred_repos_count = 56, 
                        visibility = '', 
                        website = '', ), 
                    parent = swagger_client.models.repository.Repository(
                        allow_merge_commits = True, 
                        allow_rebase = True, 
                        allow_rebase_explicit = True, 
                        allow_rebase_update = True, 
                        allow_squash_merge = True, 
                        archived = True, 
                        avatar_url = '', 
                        clone_url = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        default_branch = '', 
                        default_delete_branch_after_merge = True, 
                        default_merge_style = '', 
                        description = '', 
                        empty = True, 
                        fork = True, 
                        forks_count = 56, 
                        full_name = '', 
                        has_issues = True, 
                        has_projects = True, 
                        has_pull_requests = True, 
                        has_wiki = True, 
                        html_url = '', 
                        id = 56, 
                        ignore_whitespace_conflicts = True, 
                        internal = True, 
                        language = '', 
                        languages_url = '', 
                        mirror = True, 
                        mirror_interval = '', 
                        mirror_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        open_issues_count = 56, 
                        open_pr_counter = 56, 
                        original_url = '', 
                        permissions = swagger_client.models.permission.Permission(
                            admin = True, 
                            pull = True, 
                            push = True, ), 
                        private = True, 
                        release_counter = 56, 
                        repo_transfer = swagger_client.models.repo_transfer.RepoTransfer(
                            doer = swagger_client.models.user.User(
                                active = True, 
                                avatar_url = '', 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                description = '', 
                                email = '', 
                                followers_count = 56, 
                                following_count = 56, 
                                full_name = '', 
                                id = 56, 
                                is_admin = True, 
                                language = '', 
                                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                location = '', 
                                login = '', 
                                login_name = 'empty', 
                                prohibit_login = True, 
                                restricted = True, 
                                starred_repos_count = 56, 
                                visibility = '', 
                                website = '', ), 
                            recipient = , 
                            teams = [
                                swagger_client.models.team.Team(
                                    can_create_org_repo = True, 
                                    description = '', 
                                    id = 56, 
                                    includes_all_repositories = True, 
                                    name = '', 
                                    organization = swagger_client.models.organization.Organization(
                                        avatar_url = '', 
                                        description = '', 
                                        full_name = '', 
                                        id = 56, 
                                        location = '', 
                                        name = '', 
                                        repo_admin_change_team_access = True, 
                                        username = '', 
                                        visibility = '', 
                                        website = '', ), 
                                    permission = 'none', 
                                    units = [repo.code, repo.issues, repo.ext_issues, repo.wiki, repo.pulls, repo.releases, repo.projects, repo.ext_wiki], 
                                    units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}, )
                                ], ), 
                        size = 56, 
                        ssh_url = '', 
                        stars_count = 56, 
                        template = True, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        watchers_count = 56, 
                        website = '', ), 
                    permissions = swagger_client.models.permission.Permission(
                        admin = True, 
                        pull = True, 
                        push = True, ), 
                    private = True, 
                    release_counter = 56, 
                    repo_transfer = swagger_client.models.repo_transfer.RepoTransfer(), 
                    size = 56, 
                    ssh_url = '', 
                    stars_count = 56, 
                    template = True, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    watchers_count = 56, 
                    website = '', ), 
                repo_id = 56, 
                sha = ''
            )
        else :
            return PRBranchInfo(
        )
        """

    def testPRBranchInfo(self):
        """Test PRBranchInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
