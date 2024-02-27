with lineitem as 
(
    select 
        L_ORDERKEY as ORDER_ID
        ,L_PARTKEY as PART_ID
        ,L_SUPPKEY as SUPP_ID
        ,L_LINENUMBER as LINE_NUMBER
        ,L_QUANTITY as QUANTITY
        ,L_EXTENDEDPRICE as EXTENDED_PRICE
        ,L_DISCOUNT as DISCOUNT
        ,L_TAX as TAX
        ,L_RETURNFLAG as RETURN_FLAG
        ,L_LINESTATUS as LINE_STATUS
        ,L_SHIPDATE as SHIP_DATE
        ,L_COMMITDATE as COMMIT_DATE
        ,L_RECEIPTDATE as RECEIPT_DATE
        ,L_SHIPINSTRUCT as SHIP_INSTRUCT
        ,L_SHIPMODE as SHIP_MODE
    from {{ref('lineitem_stg')}}

)

select * from lineitem