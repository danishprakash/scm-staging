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
from pydantic import BaseModel, Field, StrictInt, StrictStr


class CreatePullReviewComment(BaseModel):
    """
    CreatePullReviewComment represent a review comment for creation api
    """

    body: Optional[StrictStr] = None
    new_position: Optional[StrictInt] = Field(
        None, description="if comment to new file line or 0"
    )
    old_position: Optional[StrictInt] = Field(
        None, description="if comment to old file line or 0"
    )
    path: Optional[StrictStr] = Field(None, description="the tree path")
    __properties = ["body", "new_position", "old_position", "path"]

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
    def from_json(cls, json_str: str) -> CreatePullReviewComment:
        """Create an instance of CreatePullReviewComment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreatePullReviewComment:
        """Create an instance of CreatePullReviewComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreatePullReviewComment.parse_obj(obj)

        _obj = CreatePullReviewComment.parse_obj(
            {
                "body": obj.get("body"),
                "new_position": obj.get("new_position"),
                "old_position": obj.get("old_position"),
                "path": obj.get("path"),
            }
        )
        return _obj
