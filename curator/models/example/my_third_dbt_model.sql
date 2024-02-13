{{ config(materialized='table') }}

with source_data as (

    select 2 as id

)

select *
from source_data
