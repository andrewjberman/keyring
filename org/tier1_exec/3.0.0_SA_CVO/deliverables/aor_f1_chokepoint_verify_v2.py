"""!!! RETRACTED 2026-07-13 -- THIS DRIVER'S "7/7 SOUND" VERDICT IS WITHDRAWN. DO NOT CITE IT. !!!

RETRACTION (3.0.0_SA_CVO, the author). This instrument is a CONFIRMATION INSTRUMENT and it
GREENED THE DEFECT IT WAS WRITTEN TO CATCH. Kept in the tree ONLY as the worked example --
running it is fine; trusting its verdict is not.

WHY IT IS INVALID. Its stale arm (ARM 2 / 'stale artifact') uses an as_of TEN DAYS OLD --
stale AND DIFFERENT. An as_of-keyed guard catches that BY CONSTRUCTION, so this driver was
structurally incapable of failing the very fix its author recommended.

AND IT IS WORSE THAN A MISS. The GREEN arm below --
    WEEKEND: pin=Fri, stamp=Fri (legit non-advance) -> RETURNED [OK]
-- IS the fail-open state (CVO~B's A3). The author constructed the exploit, watched it pass,
and certified it as proof the guard "does not false-raise." The guard cannot distinguish:
    (a) resolver RAN, source didn't advance  -> stamp=Fri, pin=Fri   [legitimately fresh]
    (b) resolver SKIPPED, leftover artifact  -> stamp=Fri, pin=Fri   [FROZEN -- the defect]
Identical output. The "no-false-raise" control and the hole are THE SAME STATE.

ROOT. The pin (orion-gold-dispatch.sh:1296, `s3 ls | tail -1`) identifies the SOURCE PARTITION,
never the RUN -- every run sharing a partition shares a pin. And as_of is only HALF the
artifact's identity: resolution == f(accounts_v2 partition, AOR_FOLD_ACTIVE), and `fold_mode`
is neither stamped (RESOLUTION_COLS :58-59) nor asserted. A3 is a MODE mismatch, not a vintage one.

THE LESSON, which is the whole point of keeping this file: BOTH-DIRECTIONS IS NOT ENOUGH.
Proving an instrument can go RED and can go GREEN says nothing if the GREEN is reachable FROM
THE FAILING STATE. The arms must be reachable from DIFFERENT TRUTHS, not merely produce
different outputs. This driver passed its own both-directions bar and was still a placebo.

Superseded by CVO~B's gate-2 fixture (c0dfeaec6). Full: CVO_CANNOT_GO_GREEN_register_and_gate_20260713.md
(the register this driver was meant to exemplify -- and violated 20 minutes after it was written).

---- original docstring below, preserved unaltered ----

CVO verify-v2 -- exercises DS's in-flight R1/R1b chokepoint fix in aor_resolution.py.

v1 (aor_f1_rollback_falsifier.py) proved the DEFECT: a stale resolution was accepted as fresh.
v2 proves the FIX, and -- per the cannot-go-GREEN register -- proves it can still go GREEN.

A freshness assertion that RAISES on everything is not a fix, it is a condemnation instrument.
So the RED arms (does it now catch the defect?) and the GREEN arms (does it still pass a healthy
run?) are asserted SEPARATELY. The weekend/holiday arm is the one that would have been broken by
a wall-clock tolerance -- CTO ruled exact-match-against-the-run's-pin precisely to dodge it.

Hermetic: stubbed s3, no prod touch. Run against the WORKING TREE (DS's fix is uncommitted).
"""
from __future__ import annotations

import os
import sys
from io import BytesIO

import pandas as pd

sys.path.insert(0, 'data/inf/scripts/gold/lib')
import aor_resolution as A  # noqa: E402


def frame(as_of, drop_as_of=False, mixed=None):
    d = {'account_id': [1001, 1002, 1003],
         'advisor_key': ['adv_alpha', 'adv_beta', 'adv_gamma'],
         'advisor_of_record': ['Alpha', 'Beta', 'Gamma']}
    if not drop_as_of:
        d['as_of'] = mixed if mixed else [as_of] * 3
    return pd.DataFrame(d)


class StubS3:
    def __init__(self, payload):
        self.payload = payload

    def get_object(self, Bucket, Key):  # noqa: N803
        if self.payload is None:
            raise Exception(f'NoSuchKey: s3://{Bucket}/{Key}')
        buf = BytesIO()
        self.payload.to_parquet(buf, index=False, engine='pyarrow', compression='snappy')
        buf.seek(0)
        return {'Body': BytesIO(buf.getvalue())}


def arm(name, pin, payload, expect):
    if pin is None:
        os.environ.pop('INF_AOR_ASOF', None)
    else:
        os.environ['INF_AOR_ASOF'] = pin
    try:
        A.load_resolution(StubS3(payload), 'opal-data-inf')
        got = 'RETURNED'
    except Exception:
        got = 'RAISED'
    ok = 'OK' if got == expect else '*** REGRESSION ***'
    print(f'  {name:<44} pin={str(pin):<12} -> {got:<8} (want {expect:<8}) [{ok}]')
    return got == expect


TODAY = '2026-07-13'
STALE = '2026-07-03'
FRI = '2026-07-10'          # a Friday: the weekend/holiday non-advance case

print('DS R1/R1b chokepoint fix -- verify v2 (working tree, uncommitted)\n')

print('RED arms -- the assertion must CATCH the defect:')
red = [
    arm('stale artifact (the post-GO rollback)', TODAY, frame(STALE), 'RAISED'),
    arm('artifact absent (resolver never ran)', TODAY, None, 'RAISED'),
    arm('as_of column MISSING (unverifiable)', TODAY, frame(None, drop_as_of=True), 'RAISED'),
    arm('MIXED as_of (partial rebuild)', TODAY, frame(None, mixed=[TODAY, STALE, TODAY]), 'RAISED'),
    arm('pin UNSET (R1b: no fabrication)', None, frame(TODAY), 'RAISED'),
]

print('\nGREEN arms -- the assertion must NOT false-raise on a healthy run:')
green = [
    arm('fresh artifact, pin == stamp', TODAY, frame(TODAY), 'RETURNED'),
    arm('WEEKEND: pin=Fri, stamp=Fri (no advance)', FRI, frame(FRI), 'RETURNED'),
]

print('\n' + '=' * 84)
print(f'RED   (catches the defect):     {sum(red)}/{len(red)}')
print(f'GREEN (no false-raise):         {sum(green)}/{len(green)}')
print('=' * 84)

if all(red) and all(green):
    print('\nVERDICT: the fix is SOUND and DISCRIMINATING.')
    print('  - It now RAISES on the exact state v1 proved it silently accepted (stale artifact).')
    print('  - It still RETURNS on a healthy run, INCLUDING a legitimately non-advancing weekend')
    print('    as-of -- the case a wall-clock tolerance would have false-raised on every Saturday.')
    print('  Both directions demonstrated => not a confirmation instrument, not a condemnation one.')
elif all(red) and not all(green):
    print('\nVERDICT: *** CONDEMNATION INSTRUMENT *** -- it catches the defect but false-raises on a')
    print('  healthy run. This would abort the nightly. DO NOT SHIP.')
else:
    print('\nVERDICT: *** THE FIX DOES NOT CLOSE THE DEFECT *** -- a RED arm did not raise.')
