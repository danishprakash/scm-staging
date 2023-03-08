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
from swagger_client.models.hook import Hook  # noqa: E501
from swagger_client.rest import ApiException


class TestHook(unittest.TestCase):
    """Hook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Hook
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Hook`
        """
        model = swagger_client.models.hook.Hook()  # noqa: E501
        if include_optional :
            return Hook(
                active = True, 
                config = {
                    'key' : ''
                    }, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                events = [
                    ''
                    ], 
                id = 56, 
                type = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Hook(
        )
        """

    def testHook(self):
        """Test Hook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
