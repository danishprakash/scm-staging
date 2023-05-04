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
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator


class MergePullRequestOption(BaseModel):
    """
    MergePullRequestForm form for merging Pull Request
    """

    do: StrictStr = Field(..., alias="Do")
    merge_commit_id: Optional[StrictStr] = Field(None, alias="MergeCommitID")
    merge_message_field: Optional[StrictStr] = Field(None, alias="MergeMessageField")
    merge_title_field: Optional[StrictStr] = Field(None, alias="MergeTitleField")
    delete_branch_after_merge: Optional[StrictBool] = None
    force_merge: Optional[StrictBool] = None
    head_commit_id: Optional[StrictStr] = None
    merge_when_checks_succeed: Optional[StrictBool] = None
    __properties = [
        "Do",
        "MergeCommitID",
        "MergeMessageField",
        "MergeTitleField",
        "delete_branch_after_merge",
        "force_merge",
        "head_commit_id",
        "merge_when_checks_succeed",
    ]

    @validator("do")
    def do_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (
            "merge",
            "rebase",
            "rebase-merge",
            "squash",
            "manually-merged",
        ):
            raise ValueError(
                "must be one of enum values ('merge', 'rebase', 'rebase-merge', 'squash', 'manually-merged')"
            )
        return value

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
    def from_json(cls, json_str: str) -> MergePullRequestOption:
        """Create an instance of MergePullRequestOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MergePullRequestOption:
        """Create an instance of MergePullRequestOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MergePullRequestOption.parse_obj(obj)

        _obj = MergePullRequestOption.parse_obj(
            {
                "do": obj.get("Do"),
                "merge_commit_id": obj.get("MergeCommitID"),
                "merge_message_field": obj.get("MergeMessageField"),
                "merge_title_field": obj.get("MergeTitleField"),
                "delete_branch_after_merge": obj.get("delete_branch_after_merge"),
                "force_merge": obj.get("force_merge"),
                "head_commit_id": obj.get("head_commit_id"),
                "merge_when_checks_succeed": obj.get("merge_when_checks_succeed"),
            }
        )
        return _obj
