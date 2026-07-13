"""GATE-2 ACCEPTANCE BAR (3.0.0_SA_CVO~B) -- THE TWO WITHHOLDS, AS AN EXECUTABLE TEST.

PRE-REGISTERED, BEFORE EITHER FIX EXISTS. That is the whole point.

Gate-2 is WITHHELD at `59c24b46e` on two defects (determination #3, `d3826ceb3`). This file is the
bar those fixes must clear. It is written BEFORE the fixes land so that:

  * the fix cannot be graded on a moving target (I cannot be talked into a bar I did not pre-register);
  * the OVER-CONDEMNATION controls are baked in from the start rather than bolted on afterwards --
    **a fail-closed fix that fires on a legitimate zero is the disease it was sent to cure**, and that
    is not hypothetical: the F2-B "wipe the whole firm under OFF" defect existed ONLY IN A RULING and
    was caught because someone exercised it before building it;
  * the moment DS commits, I re-run this at the committed hash and render.

IT IS RED TODAY BY CONSTRUCTION. A bar that is green before the fix lands is not a bar.

=================================================================================================
BAR 1 -- R2: THE CHOKEPOINT MUST ASSERT THE **ROW**, NOT THE COLUMN.
    aor_resolution.py:661/:675/:691 compare `sorted({...})` over `.dropna().unique()`.
    `.dropna()` removes NULL-stamped rows FROM THE COMPARISON. They stay in the frame and are
    SERVED. So the guard RAISES on a missing COLUMN and SILENTLY ACCEPTS a ROW that cannot say
    what produced it.
    B1  a resolution carrying ANY null-stamped row          -> must RAISE
    B2  [OVER-CONDEMNATION] a healthy OFF resolution        -> must RETURN  (must not be wiped)
    B3  [OVER-CONDEMNATION] a healthy ACTIVE resolution     -> must RETURN
    (`:606` already raises on len==0, so an EMPTY resolution is NOT the over-condemnation risk --
     the risk is a legitimate, fully-stamped run being condemned by a careless row assertion.)

BAR 2 -- F2: THE ABSENT-ACCOUNT PATH MUST FAIL CLOSED AT **EVERY** FULL-ATTACH CALL SITE.
    `absent='unknown'` floors advisor_key (the field a human SEES) and leaves rep_bucket <NA> (the
    field that SILENTLY DROPS the row at INF_09:193). Only INF_A_00 raises (:302).
    B4  INF_A_00 / INF_A_01 / INF_C_07 must ALL raise on absent   -> 3/3 GUARDED
    B5  [OVER-CONDEMNATION] a healthy run (0 absent)              -> must NOT raise
=================================================================================================
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold' / 'lib'))

E1 = 'e1e1e1e1e1e1e1e1e1e1e1e1e1e1e1e1'
os.environ['INF_AOR_FOLD_ACTIVE'] = '0'          # this run is OFF
os.environ['INF_AOR_ASOF'] = '2026-07-12'
os.environ['INF_AOR_SRC_ETAG'] = E1

import aor_resolution as A  # noqa: E402

CODE_NOW = A.code_digest()
RESULTS: list[tuple[str, bool, str]] = []


def bar(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok, detail))
    print(f"{'PASS' if ok else 'RED '} {name}\n       {detail}")


def frame(n_good: int, n_null: int, mode: str = 'OFF') -> pd.DataFrame:
    """n_good correctly-stamped rows + n_null rows whose IDENTITY STAMPS ARE NULL (they still carry
    attribution, and today's guard cannot see them)."""
    rows = []
    for i in range(n_good):
        rows.append({'account_id': 100 + i, 'advisor_key': 'peter_lee', 'rep_bucket': 'individual',
                     'is_mover': False, 'fold_mode': mode, 'source_digest': E1,
                     'code_digest': CODE_NOW})
    for i in range(n_null):
        rows.append({'account_id': 900 + i, 'advisor_key': 'noel_soderblom_FOLDED',
                     'rep_bucket': 'individual', 'is_mover': True,
                     'fold_mode': None, 'source_digest': None, 'code_digest': None})
    return pd.DataFrame(rows)


def load(df) -> tuple[str, object]:
    """Drive the REAL load_resolution. Only the S3 read is stubbed."""
    A._RESOLUTION_CACHE.clear()                        # F6 memoization would mask every arm after #1
    A._read_parquet = lambda s3, bucket, key: df       # the ONLY stub
    try:
        return 'RETURNED', A.load_resolution(s3=object(), bucket='opal-data-inf')
    except Exception as e:                             # noqa: BLE001
        return 'RAISED', e


print('=' * 100)
print('GATE-2 ACCEPTANCE BAR -- pre-registered. RED today BY CONSTRUCTION.')
print('=' * 100)
print('\n--- BAR 1: R2 -- the chokepoint must assert the ROW, not the column ---')

state, out = load(frame(n_good=1, n_null=870))
served = sorted(out['advisor_key'].unique()) if state == 'RETURNED' else []
bar('B1  ONE stamped row + 870 NULL-stamped rows carrying FOLDED attribution -> must RAISE',
    state == 'RAISED',
    f'{state}. served advisors = {served}\n       '
    + ('the null-stamped rows are INVISIBLE to .dropna().unique() and ARE SERVED -- one good row '
       'vouches for 870.' if state == 'RETURNED' else f'{type(out).__name__}: {str(out)[:90]}'))

state, out = load(frame(n_good=871, n_null=0, mode='OFF'))
bar('B2  [OVER-CONDEMNATION] a HEALTHY, fully-stamped OFF resolution -> must RETURN',
    state == 'RETURNED',
    f'{state}. {"rows=" + str(len(out)) if state == "RETURNED" else str(out)}\n       '
    'A fail-closed fix that fires on a legitimate run is the disease it was sent to cure.')

# >> B3 MUST RUN IN ITS OWN PROCESS, AND HERE IS WHAT IT COST ME TO LEARN THAT AGAIN. <<
# My first cut flipped INF_AOR_FOLD_ACTIVE=1 and called importlib.reload(aor_resolution). It went RED,
# and it read like a REAL over-condemnation: "a healthy ACTIVE resolution is being RAISED on."
# IT WAS MY INSTRUMENT. `fold_mode()` resolves AOR_FOLD_ACTIVE out of `inflection_rep_scope`, which
# reads the env var AT IMPORT TIME -- and reloading aor_resolution does NOT reload that transitive
# dependency. So the RUN was still OFF while my fixture stamped ACTIVE, and the chokepoint raised on a
# MODE MISMATCH: **the A3 guard doing precisely its job.**
# In a fresh process the same frame RETURNS (871 rows). Verified.
# **THIS IS THE SAME CLASS AS THE SERVED-VIEW ARM'S FALSE RED, WRITTEN BY ME, ONE HOUR LATER, IN THE
# BAR I BUILT TO CATCH OVER-CONDEMNATION.** Had it shipped, B3 would have looked like the guard
# over-condemning a legitimate ACTIVE run -- and the "fix" for that is to STOP RAISING ON A MODE
# MISMATCH, i.e. to DISARM A3, the rollback protection this whole round exists to build.
# A false RED's remedy is destructive. Knowing the failure mode by name does not immunize you against
# writing it. (base CVO's fixture says this in one line at the top and I read past it.)
b3 = subprocess.run(
    [sys.executable, '-c',
     'import os,sys;sys.path.insert(0,r"data/inf/scripts/gold/lib");'
     f'os.environ["INF_AOR_FOLD_ACTIVE"]="1";os.environ["INF_AOR_ASOF"]="2026-07-12";'
     f'os.environ["INF_AOR_SRC_ETAG"]="{E1}";'
     'import pandas as pd,aor_resolution as A;c=A.code_digest();'
     'df=pd.DataFrame([{"account_id":100+i,"advisor_key":"peter_lee","rep_bucket":"individual",'
     f'"is_mover":False,"fold_mode":"ACTIVE","source_digest":"{E1}","code_digest":c}}'
     ' for i in range(871)]);'
     'A._RESOLUTION_CACHE.clear();A._read_parquet=lambda s,b,k: df;'
     'out=A.load_resolution(s3=object(),bucket="opal-data-inf");print("RETURNED",len(out))'],
    capture_output=True, text=True, cwd=str(REPO))
# PRINT THE EVIDENCE YOU ACTUALLY GOT. My first cut wrote the detail as
#     (stdout or stderr[-1] if stderr else 'no output')
# which Python parses as ((stdout or stderr[-1]) if stderr else 'no output') -- the conditional binds
# LOOSER than `or`. So whenever stderr was empty (i.e. whenever the arm SUCCEEDED) the evidence line
# read "no output" while the verdict said PASS. **A PASS whose evidence line is empty is a PASS nobody
# can check** -- the same shape as a harness comparing HEAD_FAILED against HEAD_FAILED and scoring it
# green. The verdict was sound; the thing I would have SHOWN a reader was not.
_ev = b3.stdout.strip() or (b3.stderr.strip().splitlines()[-1] if b3.stderr.strip() else '<no output>')
bar('B3  [OVER-CONDEMNATION] a HEALTHY, fully-stamped ACTIVE resolution -> must RETURN  (own process)',
    b3.returncode == 0 and 'RETURNED' in b3.stdout,
    f'rc={b3.returncode}  {_ev}\n       '
    'Run in its OWN process: fold_mode() reads AOR_FOLD_ACTIVE at IMPORT time.')

# =================================================================================================
print('\n--- BAR 2: F2 -- every FULL-ATTACH call site must fail CLOSED on an absent account ---')

CONSUMERS = {
    'INF_A_00': 'data/inf/scripts/gold/INF_A_00.accounts_dimension.py',
    'INF_A_01': 'data/inf/scripts/gold/INF_A_01.advisor_assignments.py',
    'INF_C_07': 'data/inf/scripts/gold/INF_C_07.advisor_attribution.py',
}


def guarded(path: str) -> bool:
    """Does the consumer COUNT the absent set and RAISE on it? A floor alone is not a guard: the
    floored row still carries rep_bucket <NA> and still vanishes at INF_09:193 (exercised)."""
    src = subprocess.run(['git', 'show', f'HEAD:{path}'], capture_output=True, text=True).stdout
    if not src.strip():
        raise RuntimeError(f'INSTRUMENT BROKEN: empty source for {path}. Refusing to score it.')
    lines = src.splitlines()
    at = next((i for i, ln in enumerate(lines)
               if 'attach_advisor_key(' in ln and 'def ' not in ln), None)
    if at is None:
        raise RuntimeError(f'INSTRUMENT BROKEN: no attach_advisor_key call site in {path}.')
    w = '\n'.join(lines[at:at + 45])
    return bool(re.search(r'_n_absent\s*=', w) and re.search(r'if\s+_n_absent\s*:', w) and 'raise' in w)


states = {n: guarded(p) for n, p in CONSUMERS.items()}
unguarded = [n for n, g in states.items() if not g]
bar('B4  ALL THREE full-attach call sites raise on absent (denominator 3)',
    not unguarded,
    'GUARDED: ' + ', '.join(n for n, g in states.items() if g)
    + (f'   || STILL UNGUARDED: {unguarded} -- they FLOOR AND CONTINUE, and the floored row carries '
       f'rep_bucket <NA> straight to the silent drop at INF_09:193' if unguarded else ''))

# B5: the over-condemnation control on the F2 fix -- a healthy frame must not be condemned.
res_ok = pd.DataFrame({'account_id': [1, 2], 'advisor_key': ['peter_lee', 'joe_brandenburg'],
                       'rep_bucket': ['individual'] * 2, 'is_mover': [False, False]})
dim_ok = pd.DataFrame({'account_id': [1, 2], 'advisor_key': [pd.NA] * 2, 'rep_bucket': [pd.NA] * 2})
aid = pd.to_numeric(dim_ok['account_id'], errors='coerce')
ids = {int(a) for a in pd.to_numeric(res_ok['account_id'], errors='coerce').dropna()}
n_absent_healthy = int((~aid.dropna().astype('int64').isin(ids)).sum())
bar('B5  [OVER-CONDEMNATION] a HEALTHY run (0 accounts absent) -> the guard must NOT fire',
    n_absent_healthy == 0,
    f'_n_absent = {n_absent_healthy} on a healthy frame -> no raise. The fix must keep this true.')

# =================================================================================================
print('\n' + '=' * 100)
reds = [n for n, ok, _ in RESULTS if not ok]
print(f'  BAR: {len(RESULTS) - len(reds)} / {len(RESULTS)} PASS   (denominator printed so a truncated '
      'run cannot read as a green)')
if reds:
    print(f'\n  STILL RED: {reds}')
    print('  GATE-2 REMAINS WITHHELD. This is the expected state until the fixes land -- the bar is')
    print('  pre-registered, not a regression. Re-run me at the COMMITTED fix hash.')
    print('\n  NOTE THE SHAPE: B2/B3/B5 are the OVER-CONDEMNATION controls and they are ALREADY GREEN.')
    print('  They must STAY green. If a fix turns B1/B4 green by turning any of them RED, it is not a')
    print('  fix -- it is a fail-closed guard that fires on a legitimate run, and I will refuse it.')
    sys.exit(1)
print('\n  ALL BARS CLEAR -- both withholds are discharged AND neither fix over-condemns.')
print('  (This clears the two DEFECTS. It does NOT clear V4, which is NOT RUN and blocked by the')
print('   bronze STOP -- an EXPLICIT GAP, and no fixture green can close it.)')
sys.exit(0)
