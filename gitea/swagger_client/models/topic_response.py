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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr


class TopicResponse(BaseModel):
    """
    TopicResponse for returning topics
    """

    created: Optional[datetime] = None
    id: Optional[StrictInt] = None
    repo_count: Optional[StrictInt] = None
    topic_name: Optional[StrictStr] = None
    updated: Optional[datetime] = None
    __properties = ["created", "id", "repo_count", "topic_name", "updated"]

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
    def from_json(cls, json_str: str) -> TopicResponse:
        """Create an instance of TopicResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TopicResponse:
        """Create an instance of TopicResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TopicResponse.parse_obj(obj)

        _obj = TopicResponse.parse_obj(
            {
                "created": obj.get("created"),
                "id": obj.get("id"),
                "repo_count": obj.get("repo_count"),
                "topic_name": obj.get("topic_name"),
                "updated": obj.get("updated"),
            }
        )
        return _obj
