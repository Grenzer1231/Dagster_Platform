from dagster_embedded_elt.sling import (
    SlingResource,
    SlingSourceConnection,
    SlingTargetConnection,
) 
from dagster import EnvVar

target = SlingTargetConnection(
    type="postgres",
    host="postgres",
    port="5432",
    database="dwh",
    user=EnvVar("POSTGRES_USER"),
    password=EnvVar("POSTGRES_PASSWORD"),
)

source = SlingSourceConnection(
    type="snowflake",
    host=EnvVar("SOURCE_HOST"),
    user=EnvVar("SOURCE_USER"),
    database="SNOWFLAKE_SAMPLE_DATA",
    password=EnvVar("SOURCE_PASSWORD"),
    role=EnvVar("SOURCE_ROLE"),
)

sling_resource = SlingResource(source_connection=source, target_connection=target)