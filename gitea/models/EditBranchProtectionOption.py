from typing import *

from pydantic import BaseModel, Field


class EditBranchProtectionOption(BaseModel):
    """
    None model
        EditBranchProtectionOption options for editing a branch protection

    """

    approvals_whitelist_teams: Optional[List[str]] = Field(
        alias="approvals_whitelist_teams", default=None
    )

    approvals_whitelist_username: Optional[List[str]] = Field(
        alias="approvals_whitelist_username", default=None
    )

    block_on_official_review_requests: Optional[bool] = Field(
        alias="block_on_official_review_requests", default=None
    )

    block_on_outdated_branch: Optional[bool] = Field(
        alias="block_on_outdated_branch", default=None
    )

    block_on_rejected_reviews: Optional[bool] = Field(
        alias="block_on_rejected_reviews", default=None
    )

    dismiss_stale_approvals: Optional[bool] = Field(
        alias="dismiss_stale_approvals", default=None
    )

    enable_approvals_whitelist: Optional[bool] = Field(
        alias="enable_approvals_whitelist", default=None
    )

    enable_merge_whitelist: Optional[bool] = Field(
        alias="enable_merge_whitelist", default=None
    )

    enable_push: Optional[bool] = Field(alias="enable_push", default=None)

    enable_push_whitelist: Optional[bool] = Field(
        alias="enable_push_whitelist", default=None
    )

    enable_status_check: Optional[bool] = Field(
        alias="enable_status_check", default=None
    )

    merge_whitelist_teams: Optional[List[str]] = Field(
        alias="merge_whitelist_teams", default=None
    )

    merge_whitelist_usernames: Optional[List[str]] = Field(
        alias="merge_whitelist_usernames", default=None
    )

    protected_file_patterns: Optional[str] = Field(
        alias="protected_file_patterns", default=None
    )

    push_whitelist_deploy_keys: Optional[bool] = Field(
        alias="push_whitelist_deploy_keys", default=None
    )

    push_whitelist_teams: Optional[List[str]] = Field(
        alias="push_whitelist_teams", default=None
    )

    push_whitelist_usernames: Optional[List[str]] = Field(
        alias="push_whitelist_usernames", default=None
    )

    require_signed_commits: Optional[bool] = Field(
        alias="require_signed_commits", default=None
    )

    required_approvals: Optional[int] = Field(alias="required_approvals", default=None)

    status_check_contexts: Optional[List[str]] = Field(
        alias="status_check_contexts", default=None
    )

    unprotected_file_patterns: Optional[str] = Field(
        alias="unprotected_file_patterns", default=None
    )
