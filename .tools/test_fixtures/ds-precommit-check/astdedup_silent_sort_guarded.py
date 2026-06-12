from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd

def read(key):
    return None



def load_transactions(keys):
    """NEGATIVE (sort-guarded): a total-order .sort_values(...) chained immediately before
    .drop_duplicates() makes the survivor deterministic despite the completion-order append.
    Mirrors A_01 post-fix (73ec87a84). MUST STAY SILENT."""
    dfs = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(read, k): k for k in keys}
        for fut in as_completed(futures):
            dfs.append(fut.result())
    df = pd.concat(dfs, ignore_index=True)
    df = (df.sort_values(['transaction_id', '_file_date', '_intra_pos'])
          .drop_duplicates(subset=['transaction_id'], keep='last'))
    return df
