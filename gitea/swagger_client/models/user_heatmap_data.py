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
from pydantic import BaseModel, Field, StrictInt


class UserHeatmapData(BaseModel):
    """
    UserHeatmapData represents the data needed to create a heatmap
    """

    contributions: Optional[StrictInt] = None
    timestamp: Optional[StrictInt] = Field(
        None, description="TimeStamp defines a timestamp"
    )
    __properties = ["contributions", "timestamp"]

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
    def from_json(cls, json_str: str) -> UserHeatmapData:
        """Create an instance of UserHeatmapData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserHeatmapData:
        """Create an instance of UserHeatmapData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserHeatmapData.parse_obj(obj)

        _obj = UserHeatmapData.parse_obj(
            {
                "contributions": obj.get("contributions"),
                "timestamp": obj.get("timestamp"),
            }
        )
        return _obj
