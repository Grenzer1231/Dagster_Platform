from dagster import  load_assets_from_package_module
from . import sling, ml 

ML = "machine_learning_and_analytics"
SLING = "sling"

sling_assets = load_assets_from_package_module(package_module=sling, group_name=SLING)
ml_assets = load_assets_from_package_module(package_module=ml, group_name=ML)