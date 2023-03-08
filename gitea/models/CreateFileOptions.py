from typing import *

from pydantic import BaseModel, Field

from .CommitDateOptions import CommitDateOptions
from .Identity import Identity


class CreateFileOptions(BaseModel):
    """
        None model
            CreateFileOptions options for creating files
    Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

    """

    author: Optional[Identity] = Field(alias="author", default=None)

    branch: Optional[str] = Field(alias="branch", default=None)

    committer: Optional[Identity] = Field(alias="committer", default=None)

    content: str = Field(alias="content")

    dates: Optional[CommitDateOptions] = Field(alias="dates", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    new_branch: Optional[str] = Field(alias="new_branch", default=None)

    signoff: Optional[bool] = Field(alias="signoff", default=None)
