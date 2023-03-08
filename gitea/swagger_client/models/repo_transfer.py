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


from typing import List, Optional
from pydantic import BaseModel, conlist
from swagger_client.models.team import Team
from swagger_client.models.user import User


class RepoTransfer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    doer: Optional[User] = None
    recipient: Optional[User] = None
    teams: Optional[conlist(Team)] = None
    __properties = ["doer", "recipient", "teams"]

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
    def from_json(cls, json_str: str) -> RepoTransfer:
        """Create an instance of RepoTransfer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of doer
        if self.doer:
            _dict["doer"] = self.doer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict["recipient"] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item in self.teams:
                if _item:
                    _items.append(_item.to_dict())
            _dict["teams"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RepoTransfer:
        """Create an instance of RepoTransfer from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RepoTransfer.parse_obj(obj)

        _obj = RepoTransfer.parse_obj(
            {
                "doer": User.from_dict(obj.get("doer"))
                if obj.get("doer") is not None
                else None,
                "recipient": User.from_dict(obj.get("recipient"))
                if obj.get("recipient") is not None
                else None,
                "teams": [Team.from_dict(_item) for _item in obj.get("teams")]
                if obj.get("teams") is not None
                else None,
            }
        )
        return _obj
