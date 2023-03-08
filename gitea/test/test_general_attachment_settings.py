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
from swagger_client.models.general_attachment_settings import (
    GeneralAttachmentSettings,
)  # noqa: E501
from swagger_client.rest import ApiException


class TestGeneralAttachmentSettings(unittest.TestCase):
    """GeneralAttachmentSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GeneralAttachmentSettings
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GeneralAttachmentSettings`
        """
        model = swagger_client.models.general_attachment_settings.GeneralAttachmentSettings()  # noqa: E501
        if include_optional :
            return GeneralAttachmentSettings(
                allowed_types = '', 
                enabled = True, 
                max_files = 56, 
                max_size = 56
            )
        else :
            return GeneralAttachmentSettings(
        )
        """

    def testGeneralAttachmentSettings(self):
        """Test GeneralAttachmentSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
