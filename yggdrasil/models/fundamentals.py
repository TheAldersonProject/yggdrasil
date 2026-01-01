"""Fundamentals Data Contract Model.

This Data Contract Model is based on the Open Data Contract Standard.
"""

from typing import Literal

from pydantic import Field

from yggdrasil.models.service_level_agreement import ServiceLevelAgreement
from yggdrasil.models.specialized_implementation import (
    CommonBaseModel,
    DataContractStatus,
    Description,
)


class Fundamentals(CommonBaseModel):
    """Defines the base data contract model."""

    apiVersion: Literal["3.1.0"] = Field(
        default="3.1.0",
        title="Standard version",
        description="Version of the standard used to build data contract.",
        validate_default=True,
        pattern="^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$",
        coerce_numbers_to_str=True,
        json_schema_extra={
            "uxLabel": "Standard Version",
            "odcsRequired": True,
            "enforceDefault": True,
        },
    )
    kind: Literal["DataContract"] = Field(
        description="The kind of file this is.",
        default="DataContract",
        title="Kind",
        json_schema_extra={
            "uxLabel": "Kind",
            "odcsRequired": True,
            "enforceDefault": True,
        },
    )
    id: str = Field(
        title="ID",
        validate_default=True,
        description="A unique identifier used to reduce the risk of dataset name collisions, such as a UUID.",
        json_schema_extra={"uxLabel": "ID", "odcsRequired": True, "unique": True},
    )
    name: str = Field(
        description="Name of the data contract.",
        json_schema_extra={"uxLabel": "Name", "odcsRequired": False},
    )
    version: str = Field(
        description="Current version of the data contract.",
        json_schema_extra={"uxLabel": "Version", "odcsRequired": True},
    )
    status: DataContractStatus = Field(
        description="Current status of the data contract. Examples are: proposed, draft, active, deprecated, retired.",
        default=DataContractStatus.DRAFT,
        json_schema_extra={"uxLabel": "Status", "odcsRequired": True},
    )
    tenant: str = Field(
        description="Indicates the property the data is primarily associated with. Value is case insensitive.",
        title="Tenant",
        json_schema_extra={"uxLabel": "Tenant", "odcsRequired": True},
    )
    tags: list[str] | None = Field(
        default=None,
        description="A list of tags that may be assigned to the elements (object or property); the tags keyword may appear at any level. Tags may be used to better categorize an element. For example, finance, sensitive, employee_record.",
        title="Tags",
        json_schema_extra={"uxLabel": "Tags", "odcsRequired": False},
    )
    domain: str = Field(
        description="Name of the logical data domain.",
        json_schema_extra={"uxLabel": "Domain", "odcsRequired": False},
    )
    authoritativeDefinitions: list[str] | None = Field(
        description="List of links to sources that provide more details on the data contract.",
        json_schema_extra={"uxLabel": "Authoritative Definitions", "odcsRequired": False},
    )
    dataProduct: str = Field(
        description="Name of the data product.",
        json_schema_extra={"uxLabel": "Data Product", "odcsRequired": False},
    )
    description: Description | str | None = Field(
        default=None,
        description="Description of the data contract.",
        json_schema_extra={"uxLabel": "Description", "odcsRequired": False},
    )
    slaProperties: list[ServiceLevelAgreement] | None = Field(
        default=None,
        description="A list of key/value pairs for SLA specific properties. There is no limit on the type of properties.",
        json_schema_extra={"uxLabel": "SLA", "odcsRequired": False},
    )
