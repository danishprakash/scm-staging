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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr


class GenerateRepoOption(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    avatar: Optional[StrictBool] = Field(
        None, description="include avatar of the template repo"
    )
    default_branch: Optional[StrictStr] = Field(
        None, description="Default branch of the new repository"
    )
    description: Optional[StrictStr] = Field(
        None, description="Description of the repository to create"
    )
    git_content: Optional[StrictBool] = Field(
        None, description="include git content of default branch in template repo"
    )
    git_hooks: Optional[StrictBool] = Field(
        None, description="include git hooks in template repo"
    )
    labels: Optional[StrictBool] = Field(
        None, description="include labels in template repo"
    )
    name: StrictStr = Field(..., description="Name of the repository to create")
    owner: StrictStr = Field(
        ..., description="The organization or person who will own the new repository"
    )
    private: Optional[StrictBool] = Field(
        None, description="Whether the repository is private"
    )
    topics: Optional[StrictBool] = Field(
        None, description="include topics in template repo"
    )
    webhooks: Optional[StrictBool] = Field(
        None, description="include webhooks in template repo"
    )
    __properties = [
        "avatar",
        "default_branch",
        "description",
        "git_content",
        "git_hooks",
        "labels",
        "name",
        "owner",
        "private",
        "topics",
        "webhooks",
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
    def from_json(cls, json_str: str) -> GenerateRepoOption:
        """Create an instance of GenerateRepoOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GenerateRepoOption:
        """Create an instance of GenerateRepoOption from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GenerateRepoOption.parse_obj(obj)

        _obj = GenerateRepoOption.parse_obj(
            {
                "avatar": obj.get("avatar"),
                "default_branch": obj.get("default_branch"),
                "description": obj.get("description"),
                "git_content": obj.get("git_content"),
                "git_hooks": obj.get("git_hooks"),
                "labels": obj.get("labels"),
                "name": obj.get("name"),
                "owner": obj.get("owner"),
                "private": obj.get("private"),
                "topics": obj.get("topics"),
                "webhooks": obj.get("webhooks"),
            }
        )
        return _obj
