import polars as pl
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import adfuller
from sklearn.model_selection import train_test_split
from sklearn import linear_model

from dagster import asset, multi_asset, AssetOut, AssetKey, AssetExecutionContext, Output
from dagster_dbt import get_asset_key_for_model

from ..dbt_user_assets import dbt_user_assets



@asset(
        deps=get_asset_key_for_model([dbt_user_assets.curator_dbt_assets], "lineitem"),
        output_required=False,
    )
def load_data_from_postgres(context: AssetExecutionContext):
    uri = "postgresql://postgres:postgres@postgres:5432/dwh"
    query = """
        SELECT 
            sum(quantity) as orders, 
            ship_date 
        FROM dbo.lineitem 
        where ship_date between '1993-01-01' and '1997-12-31' 
        group by ship_date

"""
    df = pl.LazyFrame(pl.read_database_uri(query=query, uri=uri)).collect()


    return df