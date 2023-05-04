# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictStr


class Email(BaseModel):
    """
    Email an email address belonging to a user
    """

    email: Optional[StrictStr] = None
    primary: Optional[StrictBool] = None
    verified: Optional[StrictBool] = None
    __properties = ["email", "primary", "verified"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Email:
        """Create an instance of Email from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Email:
        """Create an instance of Email from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Email.parse_obj(obj)

        _obj = Email.parse_obj(
            {
                "email": obj.get("email"),
                "primary": obj.get("primary"),
                "verified": obj.get("verified"),
            }
        )
        return _obj
