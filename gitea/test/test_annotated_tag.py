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
from swagger_client.models.annotated_tag import AnnotatedTag  # noqa: E501
from swagger_client.rest import ApiException


class TestAnnotatedTag(unittest.TestCase):
    """AnnotatedTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnnotatedTag
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AnnotatedTag`
        """
        model = swagger_client.models.annotated_tag.AnnotatedTag()  # noqa: E501
        if include_optional :
            return AnnotatedTag(
                message = '', 
                object = swagger_client.models.annotated_tag_object.AnnotatedTagObject(
                    sha = '', 
                    type = '', 
                    url = '', ), 
                sha = '', 
                tag = '', 
                tagger = swagger_client.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                    date = '', 
                    email = '', 
                    name = '', ), 
                url = '', 
                verification = swagger_client.models.payload_commit_verification.PayloadCommitVerification(
                    payload = '', 
                    reason = '', 
                    signature = '', 
                    signer = swagger_client.models.payload_user.PayloadUser(
                        email = '', 
                        name = '', 
                        username = '', ), 
                    verified = True, )
            )
        else :
            return AnnotatedTag(
        )
        """

    def testAnnotatedTag(self):
        """Test AnnotatedTag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()