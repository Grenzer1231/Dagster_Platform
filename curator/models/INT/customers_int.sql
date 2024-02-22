{{ config(materialized='table') }}

with customer as 
(
    select 
        C_CUSTKEY as CUSTOMER_ID
        ,C_NATIONKEY as COUNTRY_ID
        ,C_ACCTBAL as ACCOUNT_BAL
        ,C_MKTSEGMENT as MARKET_SEG
    from {{ ref('customers_stg') }}
),

country as 
(
    select
        COUNTRY_ID
        ,REGION
        ,COUNTRY
    from {{ ref('countries_int') }}
),

merged as 
(
    select 
        customer.CUSTOMER_ID
        ,country.COUNTRY
        ,country.REGION
        ,customer.ACCOUNT_BAL
        ,customer.MARKET_SEG
    from customer
    left join country on customer.COUNTRY_ID = country.COUNTRY_ID
),

final as 
(
    select * from merged
)

select * from final