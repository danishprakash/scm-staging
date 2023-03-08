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
from swagger_client.models.branch_protection import BranchProtection  # noqa: E501
from swagger_client.rest import ApiException


class TestBranchProtection(unittest.TestCase):
    """BranchProtection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BranchProtection
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `BranchProtection`
        """
        model = swagger_client.models.branch_protection.BranchProtection()  # noqa: E501
        if include_optional :
            return BranchProtection(
                approvals_whitelist_teams = [
                    ''
                    ], 
                approvals_whitelist_username = [
                    ''
                    ], 
                block_on_official_review_requests = True, 
                block_on_outdated_branch = True, 
                block_on_rejected_reviews = True, 
                branch_name = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                dismiss_stale_approvals = True, 
                enable_approvals_whitelist = True, 
                enable_merge_whitelist = True, 
                enable_push = True, 
                enable_push_whitelist = True, 
                enable_status_check = True, 
                merge_whitelist_teams = [
                    ''
                    ], 
                merge_whitelist_usernames = [
                    ''
                    ], 
                protected_file_patterns = '', 
                push_whitelist_deploy_keys = True, 
                push_whitelist_teams = [
                    ''
                    ], 
                push_whitelist_usernames = [
                    ''
                    ], 
                require_signed_commits = True, 
                required_approvals = 56, 
                status_check_contexts = [
                    ''
                    ], 
                unprotected_file_patterns = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return BranchProtection(
        )
        """

    def testBranchProtection(self):
        """Test BranchProtection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
