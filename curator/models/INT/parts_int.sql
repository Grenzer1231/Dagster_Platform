{{ config(materialized='table') }}

with parts as 
(
    select
        P_PARTKEY as PART_ID
        ,P_NAME as PART_NAME
        ,P_MFGR as PART_MANUFACTURER
        ,P_BRAND as PART_BRAND
        ,P_TYPE as PART_TYPE
        ,P_SIZE as PART_SIZE
        ,P_CONTAINER as PART_CONTAINER
        ,P_RETAILPRICE as PART_RETAILPRICE
    from {{ ref('parts_stg') }}
)

select * from parts