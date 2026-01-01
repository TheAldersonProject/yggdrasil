"""Data Contract Quality Data Model"""

from typing import Any, Literal

from pydantic import Field

from yggdrasil.models.specialized_implementation import CommonBaseModel, Description


class Quality(CommonBaseModel):
    """Defines the schema of a Data Contract Quality."""

    id: str | None = Field(
        default=None,
        description="A unique identifier for the element used to create stable, refactor-safe references. Recommended for elements that will be referenced. See References for more details.",
        json_schema_extra={
            "ux_label": "ID",
            "required": "Yes",
            "authoritativeDefinitions": "https://bitol-io.github.io/open-data-contract-standard/latest/references/",
        },
    )
    name: str = Field(
        description="A short name for the rule.",
        json_schema_extra={"ux_label": "Name", "required": "Yes"},
    )
    description: Description | str = Field(
        description="Describe the quality check to be completed.",
        json_schema_extra={"ux_label": "Description", "required": "Yes"},
    )
    type: Literal["library", "text", "sql", "custom"] = Field(
        description="Type of DQ rule. Valid values are library (default), text, sql, and custom.",
        json_schema_extra={"ux_label": "Type", "required": "Yes"},
    )
    metric: str = Field(
        description="Required for library: the name of the metric to be calculated and compared.",
        json_schema_extra={
            "ux_label": "Metric Name",
            "required": "Yes",
            "authoritativeDefinitions": "https://bitol-io.github.io/open-data-contract-standard/latest/data-quality/#library",
        },
    )
    arguments: list[dict[str, Any]] | None = Field(
        default={},
        description="Additional arguments for the metric, if needed.",
        json_schema_extra={"ux_label": "Arguments", "required": "No"},
    )
    unit: str | None = Field(
        default=None,
        description="Unit of measurement for the metric.",
        json_schema_extra={"ux_label": "Unit", "required": "No"},
    )
    query: str | None = Field(
        default=None,
        description="Required for sql DQ rules: the SQL query to be executed. Note that it should match the target SQL engine/database, no transalation service are provided here.",
        json_schema_extra={"ux_label": "SQL Query", "required": "No"},
    )
    engine: str | None = Field(
        default=None,
        description="Required for custom DQ rule: name of the third-party engine being used. Any value is authorized here but common values are soda, greatExpectations, montecarlo, etc.",
        json_schema_extra={"ux_label": "Third-party DQ Engine", "required": "No"},
    )
    implementation: str | None = Field(
        default=None,
        description="A text (non-parsed) block of code required for the third-party DQ engine to run.",
        json_schema_extra={"ux_label": "Third-party Implementation", "required": "No"},
    )
    dimension: str | None = Field(
        default=None,
        description="The key performance indicator (KPI) or dimension for data quality. Valid values are listed after the table.",
        json_schema_extra={"ux_label": "Dimension", "required": "No"},
    )
    method: str | None = Field(
        default=None,
        description="Values are open and include reconciliation, such as 'accuracy', 'completeness', 'consistency', 'uniqueness', 'validity', 'timeliness', 'reconciliation', etc.",
        json_schema_extra={"ux_label": "Method", "required": "No"},
    )
    severity: str | None = Field(
        default=None,
        description="The severity of the DQ rule.",
        json_schema_extra={"ux_label": "Severity", "required": "No"},
    )
    customProperties: list[dict[str, Any]] | None = Field(
        default=None,
        title="Custom Properties",
        description="Additional properties required for rule execution. Follows the same structure as any custom properties block.",
        # json_schema_extra={"ux_label": "Custom Properties", "required": "No"},
    )
    tags: list[str] | None = Field(
        default=None,
        description="Tags. Follows the same structure as any tags property.",
        json_schema_extra={"ux_label": "Tags", "required": "No"},
    )
    authoritativeDefinitions: list[str] | None = Field(
        default=None,
        description="Authoritative definitions indicate the link to external definition. Follows the same structure as any authoritative definitions block.",
        json_schema_extra={"ux_label": "Authoritative Definitions", "required": "No"},
    )
    scheduler: str | None = Field(
        default=None,
        description="Name of the scheduler, can be cron or any tool your organization support.",
        json_schema_extra={"ux_label": "Scheduler", "required": "No"},
    )
    schedule: str | None = Field(
        default=None,
        description="Configuration information for the scheduling tool, for cron a possible value is 0 20 * * *.",
        json_schema_extra={"ux_label": "Scheduler Configuration", "required": "No"},
    )
