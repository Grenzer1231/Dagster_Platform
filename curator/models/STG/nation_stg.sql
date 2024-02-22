{{ config(materialized='table') }}

with nation as 
(
    select * from {{ source('dwh', 'nation') }}
)

select * from nation