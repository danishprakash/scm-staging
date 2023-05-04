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
from pydantic import BaseModel, StrictBool, StrictStr
from swagger_client.models.payload_user import PayloadUser


class PayloadCommitVerification(BaseModel):
    """
    PayloadCommitVerification represents the GPG verification of a commit
    """

    payload: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    signature: Optional[StrictStr] = None
    signer: Optional[PayloadUser] = None
    verified: Optional[StrictBool] = None
    __properties = ["payload", "reason", "signature", "signer", "verified"]

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
    def from_json(cls, json_str: str) -> PayloadCommitVerification:
        """Create an instance of PayloadCommitVerification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of signer
        if self.signer:
            _dict["signer"] = self.signer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PayloadCommitVerification:
        """Create an instance of PayloadCommitVerification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PayloadCommitVerification.parse_obj(obj)

        _obj = PayloadCommitVerification.parse_obj(
            {
                "payload": obj.get("payload"),
                "reason": obj.get("reason"),
                "signature": obj.get("signature"),
                "signer": PayloadUser.from_dict(obj.get("signer"))
                if obj.get("signer") is not None
                else None,
                "verified": obj.get("verified"),
            }
        )
        return _obj
