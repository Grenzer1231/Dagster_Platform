{{ config(materialized='table') }}

with customers as 
(
    select * from {{ source('dwh', 'customer') }}
)

select * from customers