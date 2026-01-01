"""Data Contract Relationships Schema Data Model"""

from typing import Any

from pydantic import Field

from yggdrasil.models.specialized_implementation import CommonBaseModel


class References(CommonBaseModel):
    """Defines the schema of a Data Contract Relationship."""

    type: str = Field(
        description="Type of relationship (defaults to foreignKey)",
        json_schema_extra={"ux_label": "Type", "required": "Yes"},
    )
    to: str | None = Field(
        description="Target property reference using schema.property notation",
        json_schema_extra={"ux_label": "To", "required": "No"},
    )
    from_: str | None = Field(
        default=None,
        description="Source property reference using schema.property notation",
        json_schema_extra={"ux_label": "From", "required": "No", "reference": "Context-dependent"},
    )
    customProperties: list[dict[str, Any]] | None = Field(
        default=None,
        description="Additional metadata about the relationship",
        json_schema_extra={"ux_label": "Custom Properties", "required": "No"},
    )
