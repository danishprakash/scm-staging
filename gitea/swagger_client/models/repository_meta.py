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
from pydantic import BaseModel, StrictInt, StrictStr


class RepositoryMeta(BaseModel):
    """
    RepositoryMeta basic repository information
    """

    full_name: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    __properties = ["full_name", "id", "name", "owner"]

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
    def from_json(cls, json_str: str) -> RepositoryMeta:
        """Create an instance of RepositoryMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RepositoryMeta:
        """Create an instance of RepositoryMeta from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RepositoryMeta.parse_obj(obj)

        _obj = RepositoryMeta.parse_obj(
            {
                "full_name": obj.get("full_name"),
                "id": obj.get("id"),
                "name": obj.get("name"),
                "owner": obj.get("owner"),
            }
        )
        return _obj
