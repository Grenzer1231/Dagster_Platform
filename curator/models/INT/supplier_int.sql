
with supplier as 
(
    select 
        S_SUPPKEY as SUPP_ID
        ,S_NAME as SUPP_NAME
        ,S_ADDRESS as SUPP_ADDRESS
        ,S_NATIONKEY as SUPP_COUNTRY
        ,S_ACCTBAL as SUPP_ACCOUNTBAL
    from {{ref('supplier_stg')}}
)

select * from supplier