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
from swagger_client.models.team import Team  # noqa: E501
from swagger_client.rest import ApiException


class TestTeam(unittest.TestCase):
    """Team unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Team
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Team`
        """
        model = swagger_client.models.team.Team()  # noqa: E501
        if include_optional :
            return Team(
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
                units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}
            )
        else :
            return Team(
        )
        """

    def testTeam(self):
        """Test Team"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
