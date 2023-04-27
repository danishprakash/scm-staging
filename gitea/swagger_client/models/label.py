# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class Label(BaseModel):
    """
    Label a label to an issue or a pr
    """

    color: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    exclusive: Optional[StrictBool] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties = ["color", "description", "exclusive", "id", "name", "url"]

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
    def from_json(cls, json_str: str) -> Label:
        """Create an instance of Label from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Label:
        """Create an instance of Label from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Label.parse_obj(obj)

        _obj = Label.parse_obj(
            {
                "color": obj.get("color"),
                "description": obj.get("description"),
                "exclusive": obj.get("exclusive"),
                "id": obj.get("id"),
                "name": obj.get("name"),
                "url": obj.get("url"),
            }
        )
        return _obj
