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
from pydantic import BaseModel, Field, StrictBool, StrictStr


class MarkdownOption(BaseModel):
    """
    MarkdownOption markdown options
    """

    context: Optional[StrictStr] = Field(
        None, alias="Context", description="Context to render  in: body"
    )
    mode: Optional[StrictStr] = Field(
        None, alias="Mode", description="Mode to render  in: body"
    )
    text: Optional[StrictStr] = Field(
        None, alias="Text", description="Text markdown to render  in: body"
    )
    wiki: Optional[StrictBool] = Field(
        None, alias="Wiki", description="Is it a wiki page ?  in: body"
    )
    __properties = ["Context", "Mode", "Text", "Wiki"]

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
    def from_json(cls, json_str: str) -> MarkdownOption:
        """Create an instance of MarkdownOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MarkdownOption:
        """Create an instance of MarkdownOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MarkdownOption.parse_obj(obj)

        _obj = MarkdownOption.parse_obj(
            {
                "context": obj.get("Context"),
                "mode": obj.get("Mode"),
                "text": obj.get("Text"),
                "wiki": obj.get("Wiki"),
            }
        )
        return _obj
