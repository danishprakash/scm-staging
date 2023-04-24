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
from pydantic import BaseModel, Field, StrictStr


class CreateBranchRepoOption(BaseModel):
    """
    CreateBranchRepoOption options when creating a branch in a repository
    """

    new_branch_name: StrictStr = Field(..., description="Name of the branch to create")
    old_branch_name: Optional[StrictStr] = Field(
        None, description="Name of the old branch to create from"
    )
    __properties = ["new_branch_name", "old_branch_name"]

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
    def from_json(cls, json_str: str) -> CreateBranchRepoOption:
        """Create an instance of CreateBranchRepoOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateBranchRepoOption:
        """Create an instance of CreateBranchRepoOption from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateBranchRepoOption.parse_obj(obj)

        _obj = CreateBranchRepoOption.parse_obj(
            {
                "new_branch_name": obj.get("new_branch_name"),
                "old_branch_name": obj.get("old_branch_name"),
            }
        )
        return _obj