from dagster import AssetExecutionContext, AssetKey
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslator, DagsterDbtTranslatorSettings
from .constants import dbt_manifest_path
from typing import Any, Mapping, Optional

class CustomDagsterDbtTranslator(DagsterDbtTranslator): 
    def get_group_name(
            self, dbt_resource_props: Mapping[str, Any]
    ) -> Optional[str]:
        return "dbt_assets"
    
dagster_dbt_translator = CustomDagsterDbtTranslator(
    settings=DagsterDbtTranslatorSettings(enable_asset_checks=True)
)

@dbt_assets(manifest=dbt_manifest_path, dagster_dbt_translator=dagster_dbt_translator)
def curator_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()