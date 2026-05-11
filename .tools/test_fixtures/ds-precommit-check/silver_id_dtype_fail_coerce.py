from __future__ import annotations
# Fixture: FAIL — build_* function that returns DataFrame without calling coerce_silver_ids.
import pandas as pd

def build_accounts(snapshot_date) -> pd.DataFrame:
    df = pd.DataFrame({'account_id': [1, 2, 3], 'household_id': [10, 20, 30]})
    df['snapshot_date'] = snapshot_date
    return df[['account_id', 'household_id', 'snapshot_date']]
