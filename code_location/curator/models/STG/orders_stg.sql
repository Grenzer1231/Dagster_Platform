{{ config(materialized='table') }}

with orders as 
(
    select * from {{ source('dwh', 'orders') }}
)

select * from orders