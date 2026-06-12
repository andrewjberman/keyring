from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd

def read(key):
    return None



def load_transactions(keys):
    """POSITIVE: completion-order append -> concat -> order-sensitive dedup, no total-order
    sort. Mirrors A_01 (73ec87a84^) / A_04 (9a89926fd^) pre-fix. MUST FIRE."""
    dfs = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(read, k): k for k in keys}
        for fut in as_completed(futures):
            dfs.append(fut.result())
    df = pd.concat(dfs, ignore_index=True)
    df = df.drop_duplicates(subset=['transaction_id'], keep='last')
    return df
