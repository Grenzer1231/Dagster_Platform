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

target = SlingTargetConnection(
    type="postgres",
    host="postgres",
    port="5432",
    database="dwh",
    user="postgres",
    password="postgres",
)

source = SlingSourceConnection(
    type="snowflake",
    host="tb53604.southeast-asia.azure.snowflakecomputing.com",
    user="mdinglasan1231",
    database="SNOWFLAKE_SAMPLE_DATA",
    password="Grenzer12",
    role="ACCOUNTADMIN",
)

asset_def = build_sling_asset(
    asset_spec=AssetSpec("my_asset_name"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER",
    target_object="dbo.CUSTOMER",
    mode=SlingMode.INCREMENTAL,
    primary_key="C_CUSTKEY",
)

sling_resource = SlingResource(source_connection=source, target_connection=target)

# DBT Models
@dbt_assets(manifest=dbt_manifest_path)
def curator_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()