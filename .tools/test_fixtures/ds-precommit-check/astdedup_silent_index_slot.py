from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd

def read(key):
    return None



def load_transactions(keys):
    """NEGATIVE (CLASS-I): index-slot assembly is deterministic regardless of thread
    completion order, even though it keeps drop_duplicates(keep='last'). Mirrors A_04
    post-fix (9a89926fd). MUST STAY SILENT."""
    keys = sorted(keys)
    dfs = [None] * len(keys)
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(read, key): i for i, key in enumerate(keys)}
        for fut in as_completed(futures):
            dfs[futures[fut]] = fut.result()
    df = pd.concat(dfs, ignore_index=True)
    df = df.drop_duplicates(subset=['transaction_id'], keep='last')
    return df
