{{ config(materialized='table') }}

with region as 
(
    select * from {{ source('dwh', 'region') }}
)

select * from region