from typing import *

from pydantic import BaseModel, Field


class EditOrgOption(BaseModel):
    """
    None model
        EditOrgOption options for editing an organization

    """

    description: Optional[str] = Field(alias="description", default=None)

    full_name: Optional[str] = Field(alias="full_name", default=None)

    location: Optional[str] = Field(alias="location", default=None)

    repo_admin_change_team_access: Optional[bool] = Field(
        alias="repo_admin_change_team_access", default=None
    )

    visibility: Optional[str] = Field(alias="visibility", default=None)

    website: Optional[str] = Field(alias="website", default=None)
