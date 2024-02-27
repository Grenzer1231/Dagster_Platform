{{ config(materialized='table') }}

with supplier as 
(
    select * from {{ source('dwh', 'supplier') }}
)

select * from supplier