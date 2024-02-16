import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets import curator_dbt_assets, sling_resource, asset_def
from .constants import dbt_project_dir
from .schedules import schedules

defs = Definitions(
    assets=[curator_dbt_assets, asset_def],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
        "sling": sling_resource
    },
)