import polars as pl
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import adfuller

from dagster import asset, multi_asset, AssetOut

@asset
def load_data_from_postgres():
    uri = "postgresql://postgres:postgres@localhost:5432/dwh"
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

@asset
def adfuller_test(load_data_from_postgres):
    quantity = load_data_from_postgres.select("orders")
    return adfuller(quantity)

@multi_asset(
        outs={
            "training_data": AssetOut(),
            "test_data": AssetOut()
        }
)
def training_test_data(load_data_from_postgres):

    # Convert to pandas dataframe 

    orders_df = load_data_from_postgres.to_pandas()
    orders_df.index = orders_df['ship_date']
    


    del orders_df['ship_date']
    train_end = datetime(1996,12,31)
    test_end = datetime(1998, 1,1)

    train_data = orders_df[:train_end]['orders']
    test_data = orders_df[train_end + timedelta(days=1):test_end]['orders']

    return train_data, test_data

@asset
def ar_model(training_data):
    model = AutoReg(training_data, lags=1)
    model_fit = model.fit()

    return model_fit

@asset
def ar_model_test_mse(test_data, ar_model):
    predictions = ar_model.predict(start=test_data.index[0], end=test_data.index[-1])
    residuals = test_data - predictions
    mse = np.sqrt(np.mean(residuals**2))

    return mse