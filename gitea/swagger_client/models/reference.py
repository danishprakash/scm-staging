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
from pydantic import BaseModel, StrictStr
from swagger_client.models.git_object import GitObject


class Reference(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    object: Optional[GitObject] = None
    ref: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties = ["object", "ref", "url"]

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
    def from_json(cls, json_str: str) -> Reference:
        """Create an instance of Reference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict["object"] = self.object.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Reference:
        """Create an instance of Reference from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Reference.parse_obj(obj)

        _obj = Reference.parse_obj(
            {
                "object": GitObject.from_dict(obj.get("object"))
                if obj.get("object") is not None
                else None,
                "ref": obj.get("ref"),
                "url": obj.get("url"),
            }
        )
        return _obj
