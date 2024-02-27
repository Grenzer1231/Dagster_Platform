{{ config(materialized='table') }}

with region as 
(
    select 
        R_NAME
        ,R_REGIONKEY
    from {{ ref('region_stg') }}
),

nation as 
(
    select 
        N_NAME
        ,N_NATIONKEY
        ,N_REGIONKEY
    from {{ ref('nation_stg') }}
),

merged as 
(
    select 
        nation.N_NATIONKEY as COUNTRY_ID
        ,region.R_NAME as REGION
        ,nation.N_NAME as COUNTRY
    from nation 
    left join region on nation.N_REGIONKEY = region.R_REGIONKEY
),

final as 
(
    select * from merged
)

select * from final
