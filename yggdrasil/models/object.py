"""Data Contract Schema Object."""

from pydantic import Field

from yggdrasil.models.common_schema import CommonSchema
from yggdrasil.models.object_properties import ObjectProperties


class Object(CommonSchema):
    """Defines the schema of a Data Contract Schema Object."""

    dataGranularityDescription: str | None = Field(
        default=None,
        description='Granular level of the data in the object. Example would be "Aggregation by country."',
        json_schema_extra={"ux_label": "Data Granularity", "required": "Yes"},
        examples=["Aggregation by country.", "No Aggregation."],
    )
    properties: list[ObjectProperties] | None = Field(
        default=[],
        description="List of properties within the object.",
        json_schema_extra={"ux_label": "Properties", "required": "No"},
    )
