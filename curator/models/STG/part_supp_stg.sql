{{ config(materialized='table') }}

with part_supp as 
(
    select * from {{ source('dwh', 'partsupp') }}
)

select * from part_supp