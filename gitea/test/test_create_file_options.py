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
from swagger_client.models.create_file_options import CreateFileOptions  # noqa: E501
from swagger_client.rest import ApiException


class TestCreateFileOptions(unittest.TestCase):
    """CreateFileOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateFileOptions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateFileOptions`
        """
        model = swagger_client.models.create_file_options.CreateFileOptions()  # noqa: E501
        if include_optional :
            return CreateFileOptions(
                author = swagger_client.models.identity.Identity(
                    email = '', 
                    name = '', ), 
                branch = '', 
                committer = swagger_client.models.identity.Identity(
                    email = '', 
                    name = '', ), 
                content = '', 
                dates = swagger_client.models.commit_date_options.CommitDateOptions(
                    author = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    committer = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                message = '', 
                new_branch = '', 
                signoff = True
            )
        else :
            return CreateFileOptions(
                content = '',
        )
        """

    def testCreateFileOptions(self):
        """Test CreateFileOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()