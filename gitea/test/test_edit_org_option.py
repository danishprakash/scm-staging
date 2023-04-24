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
from swagger_client.models.edit_org_option import EditOrgOption  # noqa: E501
from swagger_client.rest import ApiException


class TestEditOrgOption(unittest.TestCase):
    """EditOrgOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EditOrgOption
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EditOrgOption`
        """
        model = swagger_client.models.edit_org_option.EditOrgOption()  # noqa: E501
        if include_optional :
            return EditOrgOption(
                description = '', 
                full_name = '', 
                location = '', 
                repo_admin_change_team_access = True, 
                visibility = 'public', 
                website = ''
            )
        else :
            return EditOrgOption(
        )
        """

    def testEditOrgOption(self):
        """Test EditOrgOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()