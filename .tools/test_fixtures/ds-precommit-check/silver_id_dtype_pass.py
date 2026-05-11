from __future__ import annotations
# Fixture: PASS — build_* function that calls coerce_silver_ids before return.
import pandas as pd

def coerce_silver_ids(df, cols=None):  # stub — real one from _orion_api_silver_lib
    return df

def build_accounts(snapshot_date) -> pd.DataFrame:
    df = pd.DataFrame({'account_id': [1, 2, 3], 'household_id': [10, 20, 30]})
    df['snapshot_date'] = snapshot_date
    df = coerce_silver_ids(df)
    return df[['account_id', 'household_id', 'snapshot_date']]
