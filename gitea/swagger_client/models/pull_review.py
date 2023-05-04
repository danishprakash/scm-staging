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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from swagger_client.models.team import Team
from swagger_client.models.user import User


class PullReview(BaseModel):
    """
    PullReview represents a pull request review
    """

    body: Optional[StrictStr] = None
    comments_count: Optional[StrictInt] = None
    commit_id: Optional[StrictStr] = None
    dismissed: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    official: Optional[StrictBool] = None
    pull_request_url: Optional[StrictStr] = None
    stale: Optional[StrictBool] = None
    state: Optional[StrictStr] = Field(
        None, description="ReviewStateType review state type"
    )
    submitted_at: Optional[datetime] = None
    team: Optional[Team] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
    __properties = [
        "body",
        "comments_count",
        "commit_id",
        "dismissed",
        "html_url",
        "id",
        "official",
        "pull_request_url",
        "stale",
        "state",
        "submitted_at",
        "team",
        "updated_at",
        "user",
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
    def from_json(cls, json_str: str) -> PullReview:
        """Create an instance of PullReview from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict["team"] = self.team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict["user"] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PullReview:
        """Create an instance of PullReview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PullReview.parse_obj(obj)

        _obj = PullReview.parse_obj(
            {
                "body": obj.get("body"),
                "comments_count": obj.get("comments_count"),
                "commit_id": obj.get("commit_id"),
                "dismissed": obj.get("dismissed"),
                "html_url": obj.get("html_url"),
                "id": obj.get("id"),
                "official": obj.get("official"),
                "pull_request_url": obj.get("pull_request_url"),
                "stale": obj.get("stale"),
                "state": obj.get("state"),
                "submitted_at": obj.get("submitted_at"),
                "team": Team.from_dict(obj.get("team"))
                if obj.get("team") is not None
                else None,
                "updated_at": obj.get("updated_at"),
                "user": User.from_dict(obj.get("user"))
                if obj.get("user") is not None
                else None,
            }
        )
        return _obj
