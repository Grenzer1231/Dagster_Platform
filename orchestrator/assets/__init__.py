from dagster import AssetExecutionContext, AssetKey, load_assets_from_package_module
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslator, DagsterDbtTranslatorSettings
from .constants import dbt_manifest_path
from typing import Any, Mapping, Optional

from . import sling, ml

ML = "machine_learning"
SLING = "sling"


class CustomDagsterDbtTranslator(DagsterDbtTranslator): 
    def get_group_name(
            self, dbt_resource_props: Mapping[str, Any]
    ) -> Optional[str]:
        return "dbt_assets"
    
dagster_dbt_translator = CustomDagsterDbtTranslator(
    settings=DagsterDbtTranslatorSettings(enable_asset_checks=True)
)

@dbt_assets(manifest=dbt_manifest_path, dagster_dbt_translator=CustomDagsterDbtTranslator(),)
def curator_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

sling_assets = load_assets_from_package_module(package_module=sling, group_name=SLING)
ml_assets = load_assets_from_package_module(package_module=ml, group_name=ML)