"""Data Contract Schema Data Model"""

from typing import Any

from pydantic import Field

from yggdrasil.models.object import CommonSchema


class ObjectProperties(CommonSchema):
    """Defines the schema of a Data Contract Schema Properties."""

    primaryKey: bool = Field(
        default=False,
        description="Boolean value specifying whether the field is primary or not. Default is false.",
        json_schema_extra={"ux_label": "Primary Key", "required": "No"},
    )
    primaryKeyPosition: int | None = Field(
        default=None,
        description="If field is a primary key, the position of the primary key element. Starts from 1. Example of account_id, name being primary key columns, account_id has primaryKeyPosition 1 and name primaryKeyPosition 2. Default to -1.",
        json_schema_extra={"ux_label": "Primary Key Position", "required": "No"},
    )
    logicalType: str | None = Field(
        default=None,
        description="The logical field datatype. One of string, date, timestamp, time, number, integer, object, array or boolean.",
        json_schema_extra={"ux_label": "Logical Type", "required": "No"},
    )
    logicalTypeOptions: dict[str, Any] | None = Field(
        default=None,
        description="Additional optional metadata to describe the logical type. See Logical Type Options for more details about supported options for each logicalType.",
        json_schema_extra={
            "ux_label": "Logical Type Options",
            "required": "No",
            "authoritativeDefinitions": "https://bitol-io.github.io/open-data-contract-standard/latest/schema/#logical-type-options",
        },
    )
    physicalType: str | None = Field(
        default=None,
        description="The physical element data type in the data source. For example, VARCHAR(2), DOUBLE, INT.",
        json_schema_extra={"ux_label": "Physical Type", "required": "No"},
    )
    description: str | None = Field(
        default=None,
        description="Description of the element.",
        json_schema_extra={"ux_label": "Description", "required": "No"},
    )
    required: bool = Field(
        default=False,
        description="Indicates if the element may contain Null values; possible values are true and false. Default is false.",
        json_schema_extra={"ux_label": "Required", "required": "No"},
    )
    unique: bool = Field(
        default=False,
        description="Indicates if the element contains unique values; possible values are true and false. Default is false.",
        json_schema_extra={"ux_label": "Unique", "required": "No"},
    )
    partitioned: bool = Field(
        default=False,
        description="Indicates if the element is partitioned; possible values are true and false. Default is false.",
        json_schema_extra={"ux_label": "Partitioned", "required": "No"},
    )
    partitionKeyPosition: int | None = Field(
        default=None,
        description="If element is used for partitioning, the position of the partition element. Starts from 1. Example of country, year being partition columns, country has partitionKeyPosition 1 and year partitionKeyPosition 2. Default to -1.",
        json_schema_extra={"ux_label": "Partition Key Position", "required": "No"},
    )
    classification: str | None = Field(
        default=None,
        description="The classification of the element. One of confidential, business, financial, healthcare, government, public, or other.",
        json_schema_extra={"ux_label": "Classification", "required": "No"},
    )
    authoritativeDefinitions: str | None = Field(
        default=None,
        description="List of links to sources that provide more detail on element logic or values; model_templates would be URL to a git repo, documentation, a data catalog or another tool.",
        json_schema_extra={"ux_label": "Authoritative Definition", "required": "No"},
    )
    encryptedName: str | None = Field(
        default=None,
        description="The encrypted name of the element.",
        json_schema_extra={"ux_label": "Encrypted Name", "required": "No"},
    )
    transformSourceObjects: list[str] | None = Field(
        default=None,
        description="List of objects in the data source used in the transformation.",
        json_schema_extra={"ux_label": "Transform Source Objects", "required": "No"},
    )
    transformLogic: str | None = Field(
        default=None,
        description="Logic used in the column transformation.",
        json_schema_extra={"ux_label": "Transform Logic", "required": "No"},
    )
    transformDescription: str | None = Field(
        default=None,
        description="Description of the transformation.",
        json_schema_extra={"ux_label": "Transform Description", "required": "No"},
    )
    examples: list[str] | None = Field(
        default=None,
        description="List of model_templates of the transformation.",
        json_schema_extra={"ux_label": "Example Values", "required": "No"},
    )
    criticalDataElement: bool = Field(
        default=False,
        description="True or false indicator; If element is considered a critical data element (CDE) then true else false.",
        json_schema_extra={"ux_label": "Critical Data Element", "required": "No"},
    )
    items: list[str] | None = Field(
        default=None,
        description="List of items in an array (only applicable when logicalType: array)",
        json_schema_extra={"ux_label": "Items", "required": "No"},
    )
