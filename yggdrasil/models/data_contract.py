"""Data Contract Model.

This Data Contract Model is based on the Open Data Contract Standard.
"""

from pydantic import Field

from yggdrasil.models.fundamentals import Fundamentals
from yggdrasil.models.object import Object


class DataContract(Fundamentals):
    """Defines the base data contract model."""

    schema: list[Object] = Field(
        description="A list of elements within the schema to be cataloged.",
        json_schema_extra={"ux_label": "Schema", "required": "Yes"},
    )
