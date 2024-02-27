
with supplier as 
(
    select 
        S_SUPPKEY as SUPP_ID
        ,S_NAME as SUPP_NAME
        ,S_ADDRESS as SUPP_ADDRESS
        ,S_NATIONKEY as COUNTRY_ID
        ,S_ACCTBAL as SUPP_ACCOUNTBAL
    from {{ref('supplier_stg')}}
),

country as 
(
    select 
        COUNTRY_ID
        ,REGION
        ,COUNTRY
    from {{ref('countries_int')}}
),

merged as 
(
    select 
        s.SUPP_ID
        ,s.SUPP_NAME
        ,s.SUPP_ADDRESS
        ,c.COUNTRY
        ,c.REGION
        ,s.SUPP_ACCOUNTBAL
    from supplier s
    left join country c on s.COUNTRY_ID = c.COUNTRY_ID
)

select * from merged