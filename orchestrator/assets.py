from dagster import AssetExecutionContext
from dagster import AssetSpec
from dagster_dbt import DbtCliResource, dbt_assets
from dagster_embedded_elt.sling import (
    SlingMode,
    SlingResource,
    SlingSourceConnection,
    SlingTargetConnection,
    build_sling_asset,
)  

from .constants import dbt_manifest_path

# Sling Resources

source = SlingSourceConnection(
    type="postgres",
    host="localhost",
    port="5432",
    database="dbo",
    user="postgres",
    password="postgres",
)

target = SlingTargetConnection(
    type="snowflake",
    host="",
    user="",
    database="",
    password="",
    role="",
)

sling = SlingResource(source_connection=source, target_connection=target)

asset_def = build_sling_asset(
    asset_spec=AssetSpec("my_asset_name"),
    source_stream="public.my_table",
    target_object="marts.my_table",
    mode=SlingMode.INCREMENTAL,
    primary_key="id",
)

# DBT Models
@dbt_assets(manifest=dbt_manifest_path)
def curator_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()