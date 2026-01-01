"""Data Contract Description Data Model"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class DataContractStatus(Enum):
    """
    Represents the status of a data contract.

    This enumeration defines the possible statuses that a data contract
    can have in a system. It is designed to standardize the representation
    of contract states throughout the application. The statuses include:

    - ACTIVE: The data contract is currently active and in use.
    - INACTIVE: The data contract is inactive but still exists in the system.
    - DEPRECATED: The data contract is considered outdated and no longer recommended for use.
    - DRAFT: The data contract is in a preliminary state and is not finalized.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DEPRECATED = "DEPRECATED"
    DRAFT = "DRAFT"


class CommonBaseModel(BaseModel):
    """Defines the base schema for all specialized schemas."""

    model_config = ConfigDict(use_enum_values=True)


class Description(CommonBaseModel):
    """Defines the schema of a Data Contract Description."""

    purpose: str = Field(
        description="Intended purpose for the provided data.",
        json_schema_extra={"ux_label": "Purpose", "required": "No"},
    )
    limitations: str | None = Field(
        default=None,
        description="Technical, compliance, and legal limitations for data use.",
        json_schema_extra={"ux_label": "Limitations", "required": "No"},
    )
    usage: str | None = Field(
        default=None,
        description="Recommended usage of the data.",
        json_schema_extra={"ux_label": "Limitations", "required": "No"},
    )
    authoritativeDefinitions: list[str] | None = Field(
        default=None,
        description="List of links to sources that provide more details on the dataset; model_templates would be a link to privacy statement, terms and conditions, license agreements, data catalog, or another tool.",
        json_schema_extra={"ux_label": "Authoritative Definitions", "required": "No"},
    )
    customProperties: list[dict[str, Any]] | None = Field(
        default=None,
        description="Custom properties that are not part of the standard.",
        json_schema_extra={"ux_label": "Custom Properties", "required": "No"},
    )
