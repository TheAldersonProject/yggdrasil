"""Data Contract Schema Data Model"""

from typing import Any

from pydantic import ConfigDict, Field

from yggdrasil.models.quality import Quality
from yggdrasil.models.references import References
from yggdrasil.models.specialized_implementation import CommonBaseModel, Description


class CommonSchema(CommonBaseModel):
    """Defines the schema of the Data Contract Schema.

    This data model contains common fields that are shared across schemas: Object and Property.
    """

    __version__ = "0.1.0"

    model_config = ConfigDict(use_enum_values=True)
    id: str | None = Field(
        default=None,
        title="ID",
        description="A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See References for more details.",
        json_schema_extra={
            "ux_label": "ID",
            "required": "Yes",
            "authoritativeDefinitions": "https://bitol-io.github.io/open-data-contract-standard/latest/references/",
        },
    )
    name: str = Field(
        description="Name of the element.",
        title="Name",
    )
    physicalName: str | None = Field(
        default=None,
        title="Physical Name",
        description="Physical name.",
    )
    physicalType: str | None = Field(
        default=None,
        description="The physical element data type in the data source. For objects: table, view, topic, file. For properties: VARCHAR(2), DOUBLE, INT, etc.",
        json_schema_extra={"ux_label": "Physical Type", "required": "No"},
    )
    description: Description | str = Field(
        description="Description of the element.",
        json_schema_extra={"ux_label": "Description", "required": "Yes"},
    )
    businessName: str | None = Field(
        default=None,
        description="The business name of the element.",
        json_schema_extra={"ux_label": "Business Name", "required": "No"},
    )
    authoritativeDefinitions: list[str] | None = Field(
        default=None,
        description="List of links to sources that provide more details on the element; model_templates would be a link to privacy statement, terms and conditions, license agreements, data catalog, or another tool.",
        json_schema_extra={"ux_label": "Authoritative Definitions", "required": "No"},
    )
    quality: list[Quality] | None = Field(
        default=None,
        description="Quality tag with all the relevant information for rule setup and execution.",
        json_schema_extra={"ux_label": "Quality", "required": "No"},
    )
    tags: list[str] | None = Field(
        default=None,
        description="A list of tags that may be assigned to the elements (object or property); the tags keyword may appear at any level. Tags may be used to better categorize an element. For example, finance, sensitive, employee_record.",
        json_schema_extra={"ux_label": "Tags", "required": "No"},
    )
    customProperties: list[dict[str, Any]] | None = Field(
        default=None,
        description="Additional properties required for rule execution. Follows the same structure as any custom properties block.",
        json_schema_extra={"ux_label": "Custom Properties", "required": "No"},
    )
    relationships: list[References] | None = Field(
        default=None,
        description="Array of relationship definitions.",
        json_schema_extra={"ux_label": "Relationships", "required": "No"},
    )
