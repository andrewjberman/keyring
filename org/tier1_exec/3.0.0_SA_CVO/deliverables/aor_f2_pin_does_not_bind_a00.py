"""GATE-2 (3.0.0_SA_CVO~B) -- F2: THE RUN-LEVEL PIN DOES NOT BIND THE LARGEST CONSUMER.

CONFIRMED-BY-EXERCISE @ c16b0c73b (DS's committed round-8.2 hash).

THE FINDING. `INF_A_00.accounts_dimension` has **ZERO** references to `INF_AOR_ASOF` (measured).
It selects its accounts_v2 partition with its OWN loader -- `load_accounts_v2_latest_healthy()` /
`_list_accounts_v2_partitions()` (:119-135) -- doing its OWN walk-back to the "latest HEALTHY"
partition, entirely independently of the partition the resolver pinned.

WHY THAT DEFEATS A PROTECTION WE DELIBERATELY BUILT. The entire purpose of the INF_AOR_ASOF pin
(6d5188391) was, verbatim: "so all 10 fold producers derive off ONE accounts_v2 partition --
prevents a mid-chain silver re-emit splitting NNA(P') from AUA(P)." The pin does not bind A_00.
So the split it exists to prevent is still open at the biggest consumer -- and CHAIN_INCREMENTAL
REFRESHES accounts_v2 mid-chain (INF_API_SILVER_ACCOUNTS_V2, step 7), which is exactly the
re-emit that creates the skew.

SEVERITY IS NOT "A NULL ADVISOR". rep_bucket goes <NA> too, and downstream filters on
rep_bucket == 'individual' (INF_09:186 filters before grouping by advisor_key), so the row is
SILENTLY DROPPED from per-advisor NNA. The failure is UNDER-COUNTED AGGREGATES, not a visible null.

THE CLASS IS F1's, EXACTLY: two independent paths to "which partition", and NOTHING ASSERTS THEY
AGREE. The remedy is the key we already built -- A_00 asserts the digest of the partition IT read
against INF_AOR_SRC_ETAG (source_etag_pin()); divergence RAISES. The pin, the ETag and the pin
function all already exist; this is wiring an existing key into the one consumer that bypassed it.
(Merely making A_00 honor INF_AOR_ASOF is NOT sufficient: it makes the two paths usually agree
without ever ASSERTING that they do -- the exact posture that produced F1. Assert, don't hope.)

Hermetic: real lib, A_00's exact call. No prod touch, no gold run.
"""
from __future__ import annotations

import sys

import pandas as pd

sys.path.insert(0, r'C:\Users\AndrewBerman\Desktop\ajb_workspace\data\inf\scripts\gold\lib')

from aor_resolution import attach_advisor_key  # noqa: E402

# A_00 loaded a LATER partition (its own pin-blind walk-back): it carries account 4.
dim = pd.DataFrame({'account_id': [1, 2, 3, 4], 'rep_id': ['11', '12', '11', '12']})

# The resolver pinned an EARLIER partition: account 4 does not exist in the resolution.
res = pd.DataFrame({
    'account_id': [1, 2, 3],
    'advisor_key': ['noel_soderblom', 'peter_lee', 'patrick_scanlan'],
    'rep_bucket': ['individual'] * 3,
})

out, n_att = attach_advisor_key(dim, res)   # EXACTLY A_00:236 -- `absent` defaults to None

print('=' * 92)
print('F2 -- accounts_dimension rows the resolver never saw, at c16b0c73b')
print('=' * 92)
print(out[['account_id', 'advisor_key', 'rep_bucket']].to_string(index=False))

nan_key = int(out['advisor_key'].isna().sum())
nan_bucket = int(out['rep_bucket'].isna().sum())
print(f'\n  attached                       : {n_att} of {len(dim)}')
print(f'  SERVED rows, NaN advisor_key   : {nan_key}')
print(f'  SERVED rows, NaN rep_bucket    : {nan_bucket}')
print('\n' + '=' * 92)
if nan_key:
    print('VERDICT: RED -- F2 IS LIVE.')
    print('  The account the resolver never saw SERVES with a NULL advisor. It does NOT raise;')
    print('  A_00 emits a log WARN ("advisor_key left unset ... Investigate the as-of pin").')
    print('  A WARN IN A LOG IS NOT A GATE.')
    print('  And rep_bucket is NULL too -> a rep_bucket==\'individual\' filter DROPS the row ->')
    print('  per-advisor NNA silently UNDER-COUNTS. Silent row loss, not a visible null.')
    sys.exit(1)
print('VERDICT: GREEN -- every row inherited a resolution. F2 closed.')
sys.exit(0)
