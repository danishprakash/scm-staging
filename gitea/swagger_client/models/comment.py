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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr
from swagger_client.models.user import User


class Comment(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    issue_url: Optional[StrictStr] = None
    original_author: Optional[StrictStr] = None
    original_author_id: Optional[StrictInt] = None
    pull_request_url: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
    __properties = [
        "body",
        "created_at",
        "html_url",
        "id",
        "issue_url",
        "original_author",
        "original_author_id",
        "pull_request_url",
        "updated_at",
        "user",
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
    def from_json(cls, json_str: str) -> Comment:
        """Create an instance of Comment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict["user"] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Comment:
        """Create an instance of Comment from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Comment.parse_obj(obj)

        _obj = Comment.parse_obj(
            {
                "body": obj.get("body"),
                "created_at": obj.get("created_at"),
                "html_url": obj.get("html_url"),
                "id": obj.get("id"),
                "issue_url": obj.get("issue_url"),
                "original_author": obj.get("original_author"),
                "original_author_id": obj.get("original_author_id"),
                "pull_request_url": obj.get("pull_request_url"),
                "updated_at": obj.get("updated_at"),
                "user": User.from_dict(obj.get("user"))
                if obj.get("user") is not None
                else None,
            }
        )
        return _obj
