from dagster import AssetExecutionContext
from dagster import AssetSpec
from dagster import EnvVar

from dagster_embedded_elt.sling import (
    SlingMode,
    SlingResource,
    SlingSourceConnection,
    SlingTargetConnection,
    build_sling_asset,
) 



customer_asset_def = build_sling_asset(
    asset_spec=AssetSpec("customers"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER",
    target_object="dbo.CUSTOMER",
    mode=SlingMode.INCREMENTAL,
    primary_key="C_CUSTKEY",
)

lineitem_asset_def = build_sling_asset(
    asset_spec=AssetSpec("line_item"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM",
    target_object="dbo.LINEITEM",
    mode=SlingMode.FULL_REFRESH,
)

part_asset_def = build_sling_asset(
    asset_spec=AssetSpec("parts"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PART",
    target_object="dbo.PART",
    mode=SlingMode.INCREMENTAL,
    primary_key="P_PARTKEY",
)

partsupp_asset_def = build_sling_asset(
    asset_spec=AssetSpec("part_supplier"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PARTSUPP",
    target_object="dbo.PARTSUPP",
    mode=SlingMode.FULL_REFRESH,
    
)

supplier_asset_def = build_sling_asset(
    asset_spec=AssetSpec("supplier"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER",
    target_object="dbo.SUPPLIER",
    mode=SlingMode.INCREMENTAL,
    primary_key="S_SUPPKEY",
)

region_asset_def = build_sling_asset(
    asset_spec=AssetSpec("region"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.REGION",
    target_object="dbo.REGION",
    mode=SlingMode.INCREMENTAL,
    primary_key="R_REGIONKEY",
)

nation_asset_def = build_sling_asset(
    asset_spec=AssetSpec("nation"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION",
    target_object="dbo.NATION",
    mode=SlingMode.INCREMENTAL,
    primary_key="N_NATIONKEY",
)

orders_asset_def = build_sling_asset(
    asset_spec=AssetSpec("orders"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS",
    target_object="dbo.ORDERS",
    mode=SlingMode.INCREMENTAL,
    primary_key="O_ORDERKEY",
)

