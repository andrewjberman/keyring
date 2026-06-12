from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd

def read(key):
    return None



def load_gains(keys, accts):
    """NEGATIVE (unrelated dedup): the only drop_duplicates is on an UNRELATED lookup
    dimension (accts), not on the pd.concat(dfs) frame the completion-order build feeds.
    Mirrors the C_02 load_tax_status_split / load_holdings_counts shape that the earlier
    same-function-conjunction predicate false-flagged. MUST STAY SILENT."""
    acct_lookup = accts[['account_id', 'tax_status']].drop_duplicates('account_id')
    dfs = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(read, k): k for k in keys}
        for fut in as_completed(futures):
            dfs.append(fut.result())
    gains = pd.concat(dfs, ignore_index=True)
    return gains.merge(acct_lookup, on='account_id', how='left')
