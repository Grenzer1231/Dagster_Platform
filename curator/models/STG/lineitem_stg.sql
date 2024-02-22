{{ config(materialized='table') }}

with lineitem as 
(
    select * from {{ source('dwh', 'lineitem') }}
)

select * from lineitem