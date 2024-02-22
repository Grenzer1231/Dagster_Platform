from dagster import AssetExecutionContext, AssetKey, load_assets_from_package_module
from dagster_dbt import DbtCliResource, dbt_assets
from .constants import dbt_manifest_path

from . import sling, ml

ML = "machine_learning"
SLING = "sling"

sling_assets = load_assets_from_package_module(package_module=sling, group_name=SLING)

ml_assets = load_assets_from_package_module(package_module=ml, group_name=ML)

@dbt_assets(manifest=dbt_manifest_path)
def curator_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()