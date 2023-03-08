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
from pydantic import BaseModel, Field, StrictBool, StrictStr


class UserSettingsOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    description: Optional[StrictStr] = None
    diff_view_style: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    hide_activity: Optional[StrictBool] = None
    hide_email: Optional[StrictBool] = Field(None, description="Privacy")
    language: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    theme: Optional[StrictStr] = None
    website: Optional[StrictStr] = None
    __properties = [
        "description",
        "diff_view_style",
        "full_name",
        "hide_activity",
        "hide_email",
        "language",
        "location",
        "theme",
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
    def from_json(cls, json_str: str) -> UserSettingsOptions:
        """Create an instance of UserSettingsOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserSettingsOptions:
        """Create an instance of UserSettingsOptions from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UserSettingsOptions.parse_obj(obj)

        _obj = UserSettingsOptions.parse_obj(
            {
                "description": obj.get("description"),
                "diff_view_style": obj.get("diff_view_style"),
                "full_name": obj.get("full_name"),
                "hide_activity": obj.get("hide_activity"),
                "hide_email": obj.get("hide_email"),
                "language": obj.get("language"),
                "location": obj.get("location"),
                "theme": obj.get("theme"),
                "website": obj.get("website"),
            }
        )
        return _obj
