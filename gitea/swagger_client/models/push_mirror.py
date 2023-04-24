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
from pydantic import BaseModel, StrictBool, StrictStr


class PushMirror(BaseModel):
    """
    PushMirror represents information of a push mirror
    """

    created: Optional[StrictStr] = None
    interval: Optional[StrictStr] = None
    last_error: Optional[StrictStr] = None
    last_update: Optional[StrictStr] = None
    remote_address: Optional[StrictStr] = None
    remote_name: Optional[StrictStr] = None
    repo_name: Optional[StrictStr] = None
    sync_on_commit: Optional[StrictBool] = None
    __properties = [
        "created",
        "interval",
        "last_error",
        "last_update",
        "remote_address",
        "remote_name",
        "repo_name",
        "sync_on_commit",
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
    def from_json(cls, json_str: str) -> PushMirror:
        """Create an instance of PushMirror from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PushMirror:
        """Create an instance of PushMirror from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PushMirror.parse_obj(obj)

        _obj = PushMirror.parse_obj(
            {
                "created": obj.get("created"),
                "interval": obj.get("interval"),
                "last_error": obj.get("last_error"),
                "last_update": obj.get("last_update"),
                "remote_address": obj.get("remote_address"),
                "remote_name": obj.get("remote_name"),
                "repo_name": obj.get("repo_name"),
                "sync_on_commit": obj.get("sync_on_commit"),
            }
        )
        return _obj