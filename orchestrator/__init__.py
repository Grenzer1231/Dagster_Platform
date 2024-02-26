import os
from dagster import Definitions, AssetSelection, define_asset_job
from dagster_dbt import DbtCliResource

from .assets import sling_assets, ml_assets, ML, SLING
from .assets.dbt_user_assets.dbt_user_assets import curator_dbt_assets
from .assets.dbt_user_assets.constants import dbt_project_dir
from .resources.sling_resources import sling_resource
from .schedules import schedules

all_assets = [
    curator_dbt_assets,
    *sling_assets,
    *ml_assets,
]

ml_assets_job = define_asset_job(name="ml_assets_job", selection=AssetSelection.groups(ML))
sling_assets_job = define_asset_job(name="sling_assets_job", selection=AssetSelection.groups(SLING))

defs = Definitions(
    assets=all_assets,
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
        "sling": sling_resource
    },
    jobs=[ml_assets_job, sling_assets_job]
)