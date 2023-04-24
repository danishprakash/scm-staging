# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import swagger_client
from swagger_client.models.migrate_repo_options import MigrateRepoOptions  # noqa: E501
from swagger_client.rest import ApiException


class TestMigrateRepoOptions(unittest.TestCase):
    """MigrateRepoOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MigrateRepoOptions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MigrateRepoOptions`
        """
        model = swagger_client.models.migrate_repo_options.MigrateRepoOptions()  # noqa: E501
        if include_optional :
            return MigrateRepoOptions(
                auth_password = '', 
                auth_token = '', 
                auth_username = '', 
                clone_addr = '', 
                description = '', 
                issues = True, 
                labels = True, 
                lfs = True, 
                lfs_endpoint = '', 
                milestones = True, 
                mirror = True, 
                mirror_interval = '', 
                private = True, 
                pull_requests = True, 
                releases = True, 
                repo_name = '', 
                repo_owner = '', 
                service = 'git', 
                uid = 56, 
                wiki = True
            )
        else :
            return MigrateRepoOptions(
                clone_addr = '',
                repo_name = '',
        )
        """

    def testMigrateRepoOptions(self):
        """Test MigrateRepoOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()