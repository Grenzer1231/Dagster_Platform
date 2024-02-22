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
    user="postgres",
    password="postgres",
)

source = SlingSourceConnection(
    type="snowflake",
    host=EnvVar("SNOWFLAKE_HOST"),
    user=EnvVar("SNOWFLAKE_USER"),
    database="SNOWFLAKE_SAMPLE_DATA",
    password=EnvVar("SNOWFLAKE_PASSWORD"),
    role=EnvVar("SNOWFLAKE_ROLE"),
)

sling_resource = SlingResource(source_connection=source, target_connection=target)