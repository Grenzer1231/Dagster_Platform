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
    target_object="source.CUSTOMER",
    mode=SlingMode.INCREMENTAL,
    primary_key="C_CUSTKEY",
)

lineitem_asset_def = build_sling_asset(
    asset_spec=AssetSpec("line_item"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM",
    target_object="source.LINEITEM",
    mode=SlingMode.FULL_REFRESH,
)

part_asset_def = build_sling_asset(
    asset_spec=AssetSpec("parts"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PART",
    target_object="source.PART",
    mode=SlingMode.INCREMENTAL,
    primary_key="P_PARTKEY",
)

partsupp_asset_def = build_sling_asset(
    asset_spec=AssetSpec("part_supplier"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PARTSUPP",
    target_object="source.PARTSUPP",
    mode=SlingMode.FULL_REFRESH,
    
)

supplier_asset_def = build_sling_asset(
    asset_spec=AssetSpec("supplier"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER",
    target_object="source.SUPPLIER",
    mode=SlingMode.INCREMENTAL,
    primary_key="S_SUPPKEY",
)

region_asset_def = build_sling_asset(
    asset_spec=AssetSpec("region"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.REGION",
    target_object="source.REGION",
    mode=SlingMode.INCREMENTAL,
    primary_key="R_REGIONKEY",
)

nation_asset_def = build_sling_asset(
    asset_spec=AssetSpec("nation"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION",
    target_object="source.NATION",
    mode=SlingMode.INCREMENTAL,
    primary_key="N_NATIONKEY",
)

orders_asset_def = build_sling_asset(
    asset_spec=AssetSpec("orders"),
    source_stream="SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS",
    target_object="source.ORDERS",
    mode=SlingMode.INCREMENTAL,
    primary_key="O_ORDERKEY",
)

