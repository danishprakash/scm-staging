# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr


class CreateKeyOption(BaseModel):
    """
    CreateKeyOption options when creating a key
    """

    key: StrictStr = Field(..., description="An armored SSH key to add")
    read_only: Optional[StrictBool] = Field(
        None, description="Describe if the key has only read access or read/write"
    )
    title: StrictStr = Field(..., description="Title of the key to add")
    __properties = ["key", "read_only", "title"]

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
    def from_json(cls, json_str: str) -> CreateKeyOption:
        """Create an instance of CreateKeyOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateKeyOption:
        """Create an instance of CreateKeyOption from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateKeyOption.parse_obj(obj)

        _obj = CreateKeyOption.parse_obj(
            {
                "key": obj.get("key"),
                "read_only": obj.get("read_only"),
                "title": obj.get("title"),
            }
        )
        return _obj