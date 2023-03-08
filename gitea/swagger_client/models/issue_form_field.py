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


from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictStr


class IssueFormField(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    attributes: Optional[Dict[str, Dict[str, Any]]] = None
    id: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    validations: Optional[Dict[str, Dict[str, Any]]] = None
    __properties = ["attributes", "id", "type", "validations"]

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
    def from_json(cls, json_str: str) -> IssueFormField:
        """Create an instance of IssueFormField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssueFormField:
        """Create an instance of IssueFormField from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IssueFormField.parse_obj(obj)

        _obj = IssueFormField.parse_obj(
            {
                "attributes": obj.get("attributes"),
                "id": obj.get("id"),
                "type": obj.get("type"),
                "validations": obj.get("validations"),
            }
        )
        return _obj
