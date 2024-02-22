{{ config(materialized='table') }}

with parts as 
(
    select * from {{ source('dwh', 'part') }}
)

select * from parts