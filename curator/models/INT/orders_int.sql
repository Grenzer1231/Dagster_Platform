with orders as 
(
    select 
        O_ORDERKEY as ORDER_ID
        ,O_CUSTKEY as CUSTOMER_ID
        ,O_ORDERSTATUS as ORDER_STATUS
        ,O_TOTALPRICE as TOTAL_PRICE
        ,O_ORDERDATE as ORDER_DATE
        ,O_ORDERPRIORITY as ORDER_PRIORITY
        ,O_CLERK as O_CLERK
        ,O_SHIPPRIORITY as SHIP_PRIORITY
    from {{ref('orders_stg')}}
)

select * from orders