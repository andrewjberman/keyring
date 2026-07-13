"""CVO gate-2 instrument: does the AoR SSOT chokepoint distinguish a STALE resolution
from a FRESH one?

F1 (gate-findings brief :53) asserts that under the documented switch-only rollback
(INF_AOR_FOLD_ACTIVE=0) the resolver drops from the chain -> "the artifact isn't
produced -> consumers RAISE -> the nightly aborts."

That reasoning holds only when the artifact is ABSENT. But RESOLUTION_KEY is
overwrite-latest (aor_resolution.py:10,52,432) and the rollback is "flip only"
(brief :29) -- nothing deletes it. So POST-GO the artifact is PRESENT and STALE.

This exercises load_resolution() -- the ONE function every consumer inherits through --
against all three states, via a stubbed s3. No prod touch.
"""
from __future__ import annotations

import sys
from io import BytesIO

import pandas as pd

sys.path.insert(0, 'data/inf/scripts/gold/lib')
import aor_resolution as A  # noqa: E402


def _resolution_frame(as_of: str) -> pd.DataFrame:
    """A structurally VALID canonical resolution -- passes every check load_resolution makes."""
    return pd.DataFrame({
        'account_id': [1001, 1002, 1003],
        'advisor_key': ['adv_alpha', 'adv_beta', 'adv_gamma'],
        'advisor_of_record': ['Alpha', 'Beta', 'Gamma'],
        'as_of': [as_of] * 3,
    })


class StubS3:
    """Stands in for boto3 s3. `payload=None` => the key does not exist (404)."""

    def __init__(self, payload: pd.DataFrame | None):
        self.payload = payload

    def get_object(self, Bucket, Key):  # noqa: N803 (boto3 kwarg casing)
        if self.payload is None:
            raise Exception(f'NoSuchKey: s3://{Bucket}/{Key}')
        buf = BytesIO()
        self.payload.to_parquet(buf, index=False, engine='pyarrow', compression='snappy')
        buf.seek(0)
        return {'Body': BytesIO(buf.getvalue())}


def arm(name: str, s3, expect_raise: bool):
    try:
        res = A.load_resolution(s3, 'opal-data-inf')
    except Exception as e:
        got = 'RAISED'
        detail = f'{type(e).__name__}'
        as_of = None
    else:
        got = 'RETURNED'
        detail = f'{len(res)} rows'
        as_of = str(res['as_of'].max())

    want = 'RAISED' if expect_raise else 'RETURNED'
    verdict = 'as-predicted' if got == want else '*** UNEXPECTED ***'
    print(f'  {name:<34} -> {got:<9} ({detail}){"  as_of=" + as_of if as_of else ""}   [{verdict}]')
    return got


TODAY = str(pd.Timestamp.now(tz='UTC').date())
STALE = str(pd.Timestamp.now(tz='UTC').date() - pd.Timedelta(days=10))

print(f'load_resolution() chokepoint -- aor_resolution.py:232  (today={TODAY})\n')
print('ARM 1  artifact ABSENT           (the state F1 assumes: resolver never ran)')
a1 = arm('switch OFF, no artifact', StubS3(None), expect_raise=True)

print('\nARM 2  artifact STALE-BUT-PRESENT (the ACTUAL post-GO rollback state)')
a2 = arm(f'switch OFF, as_of={STALE}', StubS3(_resolution_frame(STALE)), expect_raise=True)

print('\nARM 3  artifact FRESH             (control: the happy path)')
a3 = arm(f'switch ON,  as_of={TODAY}', StubS3(_resolution_frame(TODAY)), expect_raise=False)

print('\n' + '=' * 78)
print(f'ARM 1 (absent)  : {a1}   <- the firebreak F1 relies on')
print(f'ARM 2 (stale)   : {a2}   <- the post-GO rollback')
print(f'ARM 3 (fresh)   : {a3}   <- control')
print('=' * 78)
if a2 == 'RETURNED':
    print('\nFINDING CONFIRMED (exercised): the SSOT chokepoint CANNOT distinguish a stale')
    print('resolution from a fresh one. A post-GO switch-OFF rollback does NOT abort the')
    print('nightly -- it silently serves attribution off a FROZEN resolution.')
    print('load_resolution() never reads the as_of column it returns (RESOLUTION_COLS :59).')
    print('=> F1 is right that the rollback is broken, and wrong about HOW: it fails OPEN,')
    print('   not closed. The loud abort F1 predicts is unreachable once the key exists.')
else:
    print('\nFINDING REFUTED: the chokepoint rejects a stale resolution. F1 stands as written.')
