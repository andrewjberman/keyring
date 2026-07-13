"""gate-2 (3.0.0_SA_CVO~B) -- does round-8.2's R1 freshness assertion CLOSE the F1 fail-open?

Tests DS's ACTUAL in-progress guard (aor_resolution.py load_resolution R1, uncommitted
working-tree @ HEAD 127e7dc0f) -- not a model of it. Hermetic: stubbed S3, real lib,
no prod touch, no gold run.

THE CLAIM UNDER TEST (DS's comment, verbatim): "The assertion asks 'was this resolution
built FOR THE RUN I AM IN?'"

It does not ask that. It asks "was this resolution built for THIS RUN'S SOURCE PARTITION?"
Those are the same question only when a source partition is used by at most ONE run. The
pin is `aws s3 ls .../accounts_v2/ | tail -1` (dispatch:1296) -- the latest PARTITION, not
the run. So every run that shares a partition shares a pin:
  * a same-day recovery run (nightly full 02:05Z, then --chain incremental at 09:00Z),
  * a weekend/holiday when the feed does not advance -- DS's own comment concedes this
    ("the data legitimately does not advance"),
  * any re-run before the next partition lands.  LIVE RIGHT NOW: latest partition is
    2026-07-12, today is 2026-07-13 -- so every run today pins to the same 2026-07-12.

On those runs the guard's two sides agree with each other while the resolver never ran in
this chain. DS cites that self-agreement as the feature that avoids false raises; it is
also exactly what makes it blind.

ARM 3 is the state CHAIN_INCREMENTAL puts us in BY CONSTRUCTION (measured: refreshes
accounts_v2 at step 7, runs 5 AoR consumers, carries NO resolver).
"""
from __future__ import annotations

import os
import sys
from io import BytesIO

import pandas as pd

sys.path.insert(0, r'C:\Users\AndrewBerman\Desktop\ajb_workspace\data\inf\scripts\gold\lib')

PIN = '2026-07-12'          # the LIVE pin: latest accounts_v2 partition (today is 2026-07-13)
PRIOR_PARTITION = '2026-07-11'

# The guard reads the pin from the environment, exactly as the dispatch exports it.
os.environ['INF_AOR_ASOF'] = PIN

from aor_resolution import RESOLUTION_KEY, load_resolution  # noqa: E402

SERVICING = 'peter_lee'        # what a switch-OFF run MUST serve (DELTA-0)
FOLDED = 'noel_soderblom'      # what an ON-run resolution carries for a mover


def _frame(as_of: str, advisor_key: str) -> pd.DataFrame:
    """A shape-valid resolution stamped with `as_of`, carrying `advisor_key` for the mover."""
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
    def __init__(self, frame):
        self.frame = frame

    def get_object(self, Bucket, Key):
        if self.frame is None or Key != RESOLUTION_KEY:
            raise FileNotFoundError(f'NoSuchKey: s3://{Bucket}/{Key}')
        buf = BytesIO()
        self.frame.to_parquet(buf, index=False, engine='pyarrow')
        buf.seek(0)
        return {'Body': BytesIO(buf.read())}


ARMS = [
    ('A1  artifact ABSENT                    (pre-GO; the state F1 assumed)',
     None, True,
     'resolver never ran; nothing at the key'),

    ('A2  STALE, source ADVANCED             (rollback across a partition boundary)',
     _frame(PRIOR_PARTITION, FOLDED), True,
     "artifact stamped 2026-07-11, run pinned 2026-07-12 -> pins DIFFER"),

    ('A3  STALE, SAME source partition       (same-day recovery run / frozen feed)',
     _frame(PIN, FOLDED), True,
     "artifact stamped 2026-07-12 by an EARLIER run; this run pinned 2026-07-12 -> pins AGREE"),

    ('A4  FRESH, written by THIS run         (control -- must NOT raise)',
     _frame(PIN, FOLDED), False,
     'the resolver ran in this chain and wrote this'),
]

print('=' * 104)
print('R1 FRESHNESS ASSERTION -- run-identity vs source-identity   [real lib, uncommitted working-tree]')
print(f'INF_AOR_ASOF = {PIN}   (live: latest accounts_v2 partition; today is 2026-07-13)')
print('  RAISED   = fail-CLOSED (chain aborts, yesterday\'s gold stays served)')
print('  RETURNED = FAIL-OPEN   (consumers silently attribute off a resolution THIS run did not build)')
print('=' * 104)

got_by_arm = {}
for name, frame, must_raise, why in ARMS:
    try:
        res = load_resolution(StubS3(frame), 'opal-data-inf')
        got, served = 'RETURNED', str(res.loc[res['account_id'] == 1, 'advisor_key'].iloc[0])
    except Exception as e:
        got, served = 'RAISED', '-'
        _ = e
    ok = (got == 'RAISED') == must_raise
    tag = 'ok' if ok else ('*** FAIL-OPEN ***' if got == 'RETURNED' else '*** PLACEBO-ABORT ***')
    got_by_arm[name[:2]] = got
    print(f'\n{name}')
    print(f'      {why}')
    print(f'      safe={"RAISE" if must_raise else "RETURN"}  ->  got={got:<9} {tag}'
          + (f'   served advisor_key={served}' if served != '-' else ''))

print('\n' + '=' * 104)
print('DETERMINATION')
print('=' * 104)
a2, a3, a4 = got_by_arm['A2'], got_by_arm['A3'], got_by_arm['A4']
print(f'  A2 (source ADVANCED)      -> {a2}    R1 CLOSES the partition-boundary rollback. Real progress.')
print(f'  A3 (SAME source partition)-> {a3}    <-- the fail-open R1 was built to close SURVIVES.')
print(f'  A4 (fresh, control)       -> {a4}    <-- non-placebo: the guard can still pass.')
print()
if a2 == 'RAISED' and a3 == 'RETURNED' and a4 == 'RETURNED':
    print('  >> THE INSTRUMENT DISCRIMINATES (A2 and A3 diverge; A4 proves it is not a stuck RAISE).')
    print()
    print('  A3 is not a corner case. It is the SHIPPING behavior of --chain incremental / --chain gold-*,')
    print('  which carry AoR consumers and NO resolver, and of ANY re-run before the next partition lands.')
    print('  In A3 the served advisor_key is the FOLDED one while the switch is OFF: the rollback')
    print('  did not roll back, and the detector (INF_D_11) that would have caught it is dropped by the')
    print('  SAME conditional (dispatch:354).')
    print()
    print('  ROOT: `as_of` stamps the SOURCE PARTITION, never the RUN. The event LEDGER already got this')
    print('  right -- a NEW {run-ts} key EVERY run, "uncollapsible by construction". The RESOLUTION is a')
    print('  FIXED key stamped with a value that repeats. The guard inherited the weaker identity.')
    print()
    print('  GATE-2 POSITION: R1 is NECESSARY, NOT SUFFICIENT. Stamp the resolution with a RUN identity')
    print('  (the run-ts the ledger already mints) and assert THAT. Then A3 goes RED and the assertion')
    print('  finally asks the question its own docstring claims it asks.')
    sys.exit(1)
print('  >> DID NOT DISCRIMINATE -- instrument untrustworthy; do not quote it.')
sys.exit(2)
