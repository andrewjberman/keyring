from __future__ import annotations
# Fixture: FAIL — build_* with .astype(str) on an *_id column (regression pattern).
import pandas as pd

def coerce_silver_ids(df, cols=None):  # stub
    return df

def build_accounts(snapshot_date) -> pd.DataFrame:
    df = pd.DataFrame({'account_id': ['1', '2', '3']})
    df['account_id'] = df['account_id'].astype(str).str.strip()
    df['snapshot_date'] = snapshot_date
    df = coerce_silver_ids(df)
    return df
