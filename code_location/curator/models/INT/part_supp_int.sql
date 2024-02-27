with part_supp as 
(
    select 
        PS_PARTKEY as PART_ID
        ,PS_SUPPKEY as SUPP_ID
        ,PS_AVAILQTY as AVAIL_QTY
        ,PS_SUPPLYCOST as SUPP_COST
    from {{ref('part_supp_stg')}}
)

select * from part_supp