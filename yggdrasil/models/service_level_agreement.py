"""Data Contract Service-level Agreement Data Model"""

from typing import Literal

from pydantic import Field

from yggdrasil.models.specialized_implementation import CommonBaseModel


class ServiceLevelAgreement(CommonBaseModel):
    """Defines the schema of a Data Contract Service-level Agreement."""

    id: str = Field(
        coerce_numbers_to_str=True,
        description="A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See References for more details",
        json_schema_extra={
            "ux_label": "ID",
            "required": "No",
            "authoritativeDefinitions": "https://bitol-io.github.io/open-data-contract-standard/latest/references/",
        },
    )
    property: str = Field(
        description="Specific property in SLA, check the Data QoS periodic table. May requires units.",
        json_schema_extra={
            "ux_label": "Property",
            "required": "Yes",
            "authoritativeDefinitions": "https://medium.com/data-mesh-learning/what-is-data-qos-and-why-is-it-critical-c524b81e3cc1",
        },
    )
    value: str = Field(
        coerce_numbers_to_str=True,
        description="Agreement value. The label will change based on the property itself.",
        json_schema_extra={"ux_label": "Value", "required": "Yes"},
    )
    valueExt: str | None = Field(
        default=None,
        description="Extended agreement value. The label will change based on the property itself.",
        json_schema_extra={"ux_label": "Extended value", "required": "No"},
    )
    unit: str | None = Field(
        default=None,
        description="d, day, days for days; y, yr, years for years, etc. Units use the ISO standard.",
        json_schema_extra={"ux_label": "Unit", "required": "No"},
    )
    element: str | None = Field(
        default=None,
        description="Element(s) to check on. Multiple elements should be extremely rare and, if so, separated by commas.",
        json_schema_extra={"ux_label": "Element(s)", "required": "No"},
    )
    driver: Literal["regulatory", "analytics", "operational"] | None = Field(
        default=None,
        description="Describes the importance of the SLA from the list of: regulatory, analytics, or operational.",
        json_schema_extra={"ux_label": "Driver", "required": "No"},
    )
    description: str = Field(
        description="Description of the SLA for humans.",
        json_schema_extra={"ux_label": "Description", "required": "Yes"},
    )
    scheduler: str | None = Field(
        default=None,
        description="Name of the scheduler, can be cron or any tool your organization supports.",
        json_schema_extra={"ux_label": "Scheduler", "required": "No"},
    )
    schedule: str | None = Field(
        default=None,
        description="Configuration information for the scheduling tool, for cron a possible value is 0 20 * * *.",
        json_schema_extra={"ux_label": "Scheduler Configuration", "required": "No"},
    )
