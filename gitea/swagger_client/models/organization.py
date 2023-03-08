# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.18.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class Organization(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    avatar_url: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    location: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    repo_admin_change_team_access: Optional[StrictBool] = None
    username: Optional[StrictStr] = Field(None, description="deprecated")
    visibility: Optional[StrictStr] = None
    website: Optional[StrictStr] = None
    __properties = [
        "avatar_url",
        "description",
        "full_name",
        "id",
        "location",
        "name",
        "repo_admin_change_team_access",
        "username",
        "visibility",
        "website",
    ]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Organization:
        """Create an instance of Organization from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Organization:
        """Create an instance of Organization from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Organization.parse_obj(obj)

        _obj = Organization.parse_obj(
            {
                "avatar_url": obj.get("avatar_url"),
                "description": obj.get("description"),
                "full_name": obj.get("full_name"),
                "id": obj.get("id"),
                "location": obj.get("location"),
                "name": obj.get("name"),
                "repo_admin_change_team_access": obj.get(
                    "repo_admin_change_team_access"
                ),
                "username": obj.get("username"),
                "visibility": obj.get("visibility"),
                "website": obj.get("website"),
            }
        )
        return _obj
