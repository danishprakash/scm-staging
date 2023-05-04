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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr


class Milestone(BaseModel):
    """
    Milestone milestone is a collection of issues on one repository
    """

    closed_at: Optional[datetime] = None
    closed_issues: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = None
    due_on: Optional[datetime] = None
    id: Optional[StrictInt] = None
    open_issues: Optional[StrictInt] = None
    state: Optional[StrictStr] = Field(None, description="StateType issue state type")
    title: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    __properties = [
        "closed_at",
        "closed_issues",
        "created_at",
        "description",
        "due_on",
        "id",
        "open_issues",
        "state",
        "title",
        "updated_at",
    ]

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
    def from_json(cls, json_str: str) -> Milestone:
        """Create an instance of Milestone from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Milestone:
        """Create an instance of Milestone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Milestone.parse_obj(obj)

        _obj = Milestone.parse_obj(
            {
                "closed_at": obj.get("closed_at"),
                "closed_issues": obj.get("closed_issues"),
                "created_at": obj.get("created_at"),
                "description": obj.get("description"),
                "due_on": obj.get("due_on"),
                "id": obj.get("id"),
                "open_issues": obj.get("open_issues"),
                "state": obj.get("state"),
                "title": obj.get("title"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
