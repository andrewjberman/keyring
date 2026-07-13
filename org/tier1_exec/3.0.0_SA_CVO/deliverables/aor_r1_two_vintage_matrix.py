"""gate-2: what did R1 actually BUY? Same 5 arms, run against BOTH vintages.

  pre-fix  = ee2780818 (shape-only load_resolution; no freshness assertion)
  post-fix = working-tree @127e7dc0f (DS's in-progress R1 exact-match on as_of)

Answers base CVO's point 1 ("run BOTH -- an arm that only ever sees the post-fix code
cannot demonstrate it would have caught the pre-fix defect") and tests his point 3
("a SAME-DAY recovery run passes -- pin unchanged, artifact current"), which treats a
pin-match as proof the artifact is correct.

usage: python two_vintage_matrix.py <lib_dir> <label>
"""
from __future__ import annotations

import os
import sys
from io import BytesIO

import pandas as pd

lib_dir, label = sys.argv[1], sys.argv[2]
sys.path.insert(0, lib_dir)

PIN = '2026-07-12'            # live: latest accounts_v2 partition (today = 2026-07-13)
PRIOR = '2026-07-11'
os.environ['INF_AOR_ASOF'] = PIN

from aor_resolution import RESOLUTION_KEY, load_resolution  # noqa: E402

SERVICING = 'peter_lee'        # what a switch-OFF run MUST serve (DELTA-0)
FOLDED = 'noel_soderblom'      # what an ON-run resolution carries for a mover


def _frame(as_of, advisor_key):
    return pd.DataFrame({
        'account_id': [1, 2, 3],
        'advisor_key': [advisor_key, 'peter_lee', 'patrick_scanlan'],
        'rep_bucket': ['individual'] * 3,
        'servicing_advisor_key': [SERVICING] * 3,
        'advisor_of_record_raw': ['Noel', '', ''],
        'explicit_aor': [True, False, False],
        'is_mover': [True, False, False],
        'as_of': [as_of] * 3,
    })


class StubS3:
    def __init__(self, f):
        self.f = f

    def get_object(self, Bucket, Key):
        if self.f is None or Key != RESOLUTION_KEY:
            raise FileNotFoundError('NoSuchKey')
        b = BytesIO()
        self.f.to_parquet(b, index=False, engine='pyarrow')
        b.seek(0)
        return {'Body': BytesIO(b.read())}


ARMS = [
    ('A1  absent', None, True),
    ('A2  stale, source ADVANCED (cross-day)', _frame(PRIOR, FOLDED), True),
    ('A3  stale, SAME partition (same-day recovery / weekend)', _frame(PIN, FOLDED), True),
    ('A3R ROLLBACK: switch now OFF, artifact FOLDED from last ON run, SAME pin', _frame(PIN, FOLDED), True),
    ('A4  fresh, written by THIS run (control)', _frame(PIN, FOLDED), False),
]

print(f'--- {label} ---')
for name, frame, must_raise in ARMS:
    try:
        res = load_resolution(StubS3(frame), 'opal-data-inf')
        got = 'RETURNED'
        served = str(res.loc[res['account_id'] == 1, 'advisor_key'].iloc[0])
    except Exception:
        got, served = 'RAISED', '-'
    ok = (got == 'RAISED') == must_raise
    tag = 'ok' if ok else ('FAIL-OPEN' if got == 'RETURNED' else 'PLACEBO')
    extra = ''
    if name.startswith('A3R') and got == 'RETURNED':
        extra = f'  served={served} but switch=OFF demands {SERVICING}  <== ROLLBACK RE-SERVED THE FOLD'
    print(f'  {name:<62} {got:<9} {tag}{extra}')
