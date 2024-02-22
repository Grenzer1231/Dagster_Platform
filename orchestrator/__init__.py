import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets import curator_dbt_assets, sling_assets
from .assets.constants import dbt_project_dir
from .resources.sling_resources import sling_resource
from .schedules import schedules

all_assets = [
    curator_dbt_assets,
    *sling_assets,
]

defs = Definitions(
    assets=all_assets,
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
        "sling": sling_resource
    },
)