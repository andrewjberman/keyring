"""Gate-1 round-8.2 falsifier -- CTO~B, 2026-07-13.

TWO candidate findings. Each arm carries a POSITIVE CONTROL, because a control that
cannot fail is not a control, and an arm that passes for the wrong reason is worthless.

  A. attach_advisor_key floors advisor_key on the absent set but NOT rep_bucket.
     A_01:200-202 and C_07:277-279 comments claim the floor protects against the
     rep_bucket-drop silent row loss (INF_09:193). Does it?

  B. load_resolution's three identity assertions use .dropna().unique() -- a COLUMN
     aggregate answering a ROW question. Does ONE correctly-stamped row vouch for N
     NULL-stamped rows that are then returned to every consumer?
"""
from __future__ import annotations

import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join('data', 'inf', 'scripts', 'gold', 'lib'))
import aor_resolution as ar  # noqa: E402

FAIL = []


def check(name, cond, detail=''):
    print(f'  [{"PASS" if cond else "FAIL"}] {name}' + (f'  -- {detail}' if detail else ''))
    if not cond:
        FAIL.append(name)


# ---------------------------------------------------------------- ARM A
print('\nARM A -- does the absent-floor cover rep_bucket, the field that SILENTLY drops the row?')

resolution = pd.DataFrame({
    'account_id': [1, 2],
    'advisor_key': ['joe_brandenburg', 'peter_lee'],
    'rep_bucket': ['individual', 'individual'],
})
# account 3 is ABSENT from the resolution -- the case the floor exists for.
frame = pd.DataFrame({'account_id': [1, 2, 3], 'nna': [10.0, 20.0, 30.0]})

out, n_att = ar.attach_advisor_key(frame.copy(), resolution, absent='unknown')
row3 = out[out['account_id'] == 3].iloc[0]

# POSITIVE CONTROL: the PRESENT accounts must inherit a real bucket. If this fails the
# harness is broken and arm A proves nothing.
present_ok = (out[out['account_id'] == 1]['rep_bucket'].iloc[0] == 'individual')
check('POSITIVE CONTROL: a present account inherits rep_bucket', present_ok,
      'if this fails, the arm below measures nothing')

check('absent row: advisor_key IS floored (the VISIBLE field)',
      row3['advisor_key'] == 'unknown', f"advisor_key={row3['advisor_key']!r}")

rb_floored = pd.notna(row3['rep_bucket'])
check('absent row: rep_bucket IS floored (the SILENT field)', rb_floored,
      f"rep_bucket={row3['rep_bucket']!r}  <-- if NA, INF_09:193 DROPS this row")

# The consequence, exercised on the real filter INF_09:193 uses.
indiv = out[out['rep_bucket'] == 'individual']
survived = 3 in set(indiv['account_id'])
check('absent row SURVIVES the INF_09:193 rep_bucket filter', survived,
      f"individual-bucket NNA sum = {indiv['nna'].sum()} of {out['nna'].sum()} "
      f"-- {out['nna'].sum() - indiv['nna'].sum()} silently vanishes")


# ---------------------------------------------------------------- ARM B
print('\nARM B -- does the chokepoint assert the ROW, or only the COLUMN?')

good = ar.fold_mode()
os.environ['INF_AOR_SRC_ETAG'] = 'etag-abc'
digest, code = 'etag-abc', ar.code_digest()

# ONE correctly-stamped row + 3 NULL-stamped rows carrying attribution.
poisoned = pd.DataFrame({
    'account_id': [1, 2, 3, 4],
    'advisor_key': ['joe_brandenburg'] * 4,
    'rep_bucket': ['individual'] * 4,
    'fold_mode': [good, None, None, None],
    'source_digest': [digest, None, None, None],
    'code_digest': [code, None, None, None],
})
clean = poisoned.copy()
clean[['fold_mode', 'source_digest', 'code_digest']] = [good, digest, code]

ar._RESOLUTION_CACHE.clear()
orig = ar._read_parquet
try:
    # POSITIVE CONTROL: a fully-stamped frame must PASS. If it raises, the arm below
    # cannot distinguish "the guard caught the poison" from "the harness is broken"
    # -- both sides equally broken, comparing garbage against itself.
    ar._read_parquet = lambda s3, b, k: clean.copy()
    try:
        ar.load_resolution(s3=object(), bucket='b')
        check('POSITIVE CONTROL: a fully-stamped resolution PASSES', True)
    except Exception as e:  # noqa: BLE001
        check('POSITIVE CONTROL: a fully-stamped resolution PASSES', False, f'{type(e).__name__}: {e}')

    ar._RESOLUTION_CACHE.clear()
    ar._read_parquet = lambda s3, b, k: poisoned.copy()
    try:
        res = ar.load_resolution(s3=object(), bucket='b')
        n_null = int(res['fold_mode'].isna().sum())
        check('poisoned resolution (1 stamped / 3 NULL) is REFUSED', False,
              f'RETURNED {len(res)} rows, {n_null} of them UNSTAMPED and carrying attribution')
    except RuntimeError:
        check('poisoned resolution (1 stamped / 3 NULL) is REFUSED', True)
finally:
    ar._read_parquet = orig
    ar._RESOLUTION_CACHE.clear()

print('\n' + '=' * 70)
print(f'FAILING ARMS: {len(FAIL)}')
for f in FAIL:
    print(f'  - {f}')
sys.exit(1 if FAIL else 0)
