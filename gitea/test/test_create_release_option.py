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
from swagger_client.models.create_release_option import (
    CreateReleaseOption,
)  # noqa: E501
from swagger_client.rest import ApiException


class TestCreateReleaseOption(unittest.TestCase):
    """CreateReleaseOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateReleaseOption
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateReleaseOption`
        """
        model = swagger_client.models.create_release_option.CreateReleaseOption()  # noqa: E501
        if include_optional :
            return CreateReleaseOption(
                body = '', 
                draft = True, 
                name = '', 
                prerelease = True, 
                tag_name = '', 
                target_commitish = ''
            )
        else :
            return CreateReleaseOption(
                tag_name = '',
        )
        """

    def testCreateReleaseOption(self):
        """Test CreateReleaseOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
