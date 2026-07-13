"""GATE-2 (3.0.0_SA_CVO~B) -- F2: THE ABSENT-ACCOUNT PATH. RE-WRITTEN AT HEAD, AND HERE IS WHY.

>> THIS ARM USED TO ENCODE THE DEFECT, AND IT WOULD HAVE DEFENDED IT. <<

The previous version's load-bearing line was:

    out, n_att = attach_advisor_key(dim, res)   # EXACTLY A_00:236 -- `absent` defaults to None
    ...
    if nan_key: RED

It asserted the OLD contract -- that `absent` DEFAULTS, so an absent account lands a NaN advisor_key
(and a NaN rep_bucket, which is what silently drops the row). That default WAS the F2 hazard, and
DS's F2-B(a) fix DELETED it: `absent` is now REQUIRED and KEYWORD-ONLY. So at HEAD this arm did not
go RED and did not go GREEN -- **it raised TypeError.**

    CLAUDE.md: "A TEST THAT ASSERTS THE DEFECT WILL DEFEND IT. When a fix makes a test fail, ask
    FIRST whether the TEST was encoding the bug."

It was. And the trap was live: the "obvious" repair is to re-add a default so my own test passes --
which would have RESTORED THE HAZARD to green my instrument. Rewritten to assert the CONTRACT.

WHAT F2 WAS. INF_A_00 is a FULL-ATTACH consumer. An account present in A_00's frame but ABSENT from
the resolution got `advisor_key = <NA>` **and `rep_bucket = <NA>`**, no raise, only a log WARN. The
severity was never "a null advisor": `INF_09:193` filters `rep_bucket == 'individual'` BEFORE the
per-advisor groupby, so the row is **silently DROPPED** -- the account VANISHES from per-advisor NNA
and the served number quietly gets smaller with nothing to tie the loss to.

WHAT IS AT HEAD NOW (source-confirmed, INF_A_00 @ HEAD):
    :274  dim, _n_att = attach_advisor_key(dim, _res, absent='unknown')   <- the FLOOR (belt+braces)
    :283  _n_absent   = <count of A_00 accounts not in the resolution>
    :302  if _n_absent: raise RuntimeError(...)                           <- the GATE (fails CLOSED)

THE THREE ARMS, AND A2 IS THE ONE THAT MATTERS:

  A1  THE DANGEROUS DEFAULT IS STRUCTURALLY GONE. Calling attach_advisor_key without `absent` must be
      a TypeError. Not "defaulted safely" -- NOT SETTABLE. A call site cannot forget an argument that
      does not exist.

  A2  THE FLOOR ALONE WOULD NOT HAVE SAVED THE ROW -- SO THE RAISE IS LOAD-BEARING, NOT DECORATIVE.
      With absent='unknown', an absent account gets advisor_key='unknown' (the field a human SEES) but
      rep_bucket STAYS NULL (the field that silently drops the row at INF_09:193). attach_advisor_key
      has NO absent-branch for rep_bucket at all (:749-756 -- look; there is none).
      >> A BACKSTOP THAT PROTECTS THE OBSERVABLE AND NOT THE UNOBSERVABLE IS A BACKSTOP FOR THE
      >> READER, NOT FOR THE DATA. The floor closes the NULL and not the LOSS.
      This arm exists so that if anyone ever "simplifies" A_00 by keeping the floor and dropping the
      raise -- which will LOOK completely safe, because the served advisor_key is visibly non-null --
      the row still silently vanishes from per-advisor NNA, and THIS ARM SAYS SO.

  A3  THE GATE FIRES, AND IT DOES NOT OVER-CONDEMN.
      _n_absent > 0  -> RAISE   (an absent account can never reach a served artifact)
      _n_absent == 0 -> RETURN  (a healthy run is NOT condemned -- the non-placebo control)
      A fail-closed guard that also fires on the healthy case is the disease it was sent to cure.

Hermetic: real lib functions, A_00's real predicate. No S3, no prod touch, no gold run.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold' / 'lib'))

import aor_resolution as ar  # noqa: E402

FAILS: list[str] = []


def check(name: str, ok: bool, detail: str = '') -> None:
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f'\n      {detail}' if detail else ''))
    if not ok:
        FAILS.append(name)


def resolution() -> pd.DataFrame:
    """The canonical resolution: accounts 1 and 2. Account 99 is NOT in it -- the ABSENT case."""
    return pd.DataFrame({'account_id': [1, 2], 'advisor_key': ['peter_lee', 'joe_brandenburg'],
                         'rep_bucket': ['individual', 'individual'], 'is_mover': [False, False]})


def a00_frame(include_absent: bool) -> pd.DataFrame:
    ids = [1, 2] + ([99] if include_absent else [])
    return pd.DataFrame({'account_id': ids, 'advisor_key': [pd.NA] * len(ids),
                         'rep_bucket': [pd.NA] * len(ids)})


def n_absent(dim: pd.DataFrame, res: pd.DataFrame) -> int:
    """INF_A_00:280-283 -- the predicate the RAISE at :302 is gated on."""
    aid = pd.to_numeric(dim['account_id'], errors='coerce')
    res_ids = {int(a) for a in pd.to_numeric(res['account_id'], errors='coerce').dropna()}
    return int((~aid.dropna().astype('int64').isin(res_ids)).sum())


print('=' * 100)
print('F2 ARM @ HEAD -- the absent-account path: the FLOOR, and why the RAISE is LOAD-BEARING')
print('=' * 100)

# ---- A1: the dangerous default is structurally gone ---------------------------------------------
try:
    ar.attach_advisor_key(a00_frame(True), resolution())      # no `absent=` -- must be IMPOSSIBLE
    check('A1 the dangerous default is GONE (calling without `absent` is impossible)', False,
          'IT RETURNED. The knob is settable again -- the F2-B(a) fix has REGRESSED.')
except TypeError as e:
    check('A1 the dangerous default is GONE (calling without `absent` is impossible)', True,
          f'TypeError: {e}')

# ---- A2: the floor protects the OBSERVABLE field, NOT the one that silently drops the row --------
dim, _ = ar.attach_advisor_key(a00_frame(True), resolution(), absent='unknown')
row = dim[pd.to_numeric(dim['account_id'], errors='coerce') == 99].iloc[0]
ak, rb = row['advisor_key'], row['rep_bucket']

check('A2 the FLOOR sets the OBSERVABLE field (advisor_key -> "unknown", visibly non-null)',
      ak == 'unknown', f'advisor_key = {ak!r}')
check('A2 ...and LEAVES THE SILENT FIELD NULL (rep_bucket has NO absent-branch)',
      pd.isna(rb), f'rep_bucket = {rb!r}')

# ASSERT THE THING, NOT A PROXY FOR IT. My first cut wrote `survives = (rb == 'individual')` on the
# SCALAR -- which yields pd.NA, not False, and blew up on `not NA` ("boolean value of NA is ambiguous").
# That was a scalar STANDING IN for what INF_09:193 actually does, which is a SERIES MASK -- and the
# two do not behave the same on a null (a mask coerces NA -> False and DROPS the row; the scalar
# refuses to answer). So: run the REAL filter and read what SURVIVES it.
served = dim[dim['rep_bucket'] == 'individual']              # INF_09:193, verbatim in behaviour
ids_served = set(pd.to_numeric(served['account_id'], errors='coerce').dropna().astype(int))
check('A2 >> SO THE ROW STILL VANISHES AT INF_09:193 -- the floor closes the NULL, not the LOSS.\n'
      '      THIS is why INF_A_00:302 must RAISE. A floor alone is a backstop for the READER. <<',
      99 not in ids_served,
      f'survivors of the rep_bucket filter: {sorted(ids_served)}  -- account 99 is GONE, and it is '
      f'gone SILENTLY: it carries a visibly-populated advisor_key={ak!r} the whole way to the drop.')

# ---- A3: the gate fires, and it does not over-condemn --------------------------------------------
n_bad = n_absent(a00_frame(True), resolution())
n_ok = n_absent(a00_frame(False), resolution())
check('A3 GATE FIRES: an absent account is detected -> INF_A_00:302 RAISES '
      "(chain aborts; yesterday's gold stays served)", n_bad > 0, f'_n_absent = {n_bad} -> raise')
check('A3 NON-PLACEBO CONTROL: a HEALTHY run is NOT condemned -> RETURNS', n_ok == 0,
      f'_n_absent = {n_ok} -> no raise. (A fail-closed guard that also fires on the healthy case '
      'is the disease it was sent to cure.)')

# =================================================================================================
# A4 -- THE CORRECTION. I RENDERED "F2 IS CLOSED AT HEAD" FROM **ONE** CALL SITE.
#
# A1-A3 above exercise INF_A_00, which RAISES at :302. From that I concluded F2 was closed. It is
# not: there are THREE full-attach call sites, and I checked one. **COUNT AT THE UNIT AT WHICH THE
# VERDICT IS RENDERED -- and the unit here is the CALL SITE, not the class.** A guarded script cannot
# vouch for an unguarded sibling any more than a safe script can hide an unsafe write.
#
# Caught by 1.0.0_SA_CTO~B's gate-1 (independently exercised: 30.0 of 60.0 NNA silently vanishes),
# then re-grounded here by my own source census. His finding stands; this arm now encodes it, so a
# future reader cannot repeat my generalisation.
#
# CONTROLS ON THE CENSUS ITSELF (a census that cannot score a KNOWN case correctly is worthless):
#   PROVEN-GUARDED   : INF_A_00 -- I read the raise at :302. The census MUST score it GUARDED.
#   PROVEN-UNGUARDED : INF_A_01 -- no absent-count, no raise. The census MUST score it UNGUARDED.
# If either control misfires, the census is broken and reports NO verdict on the third.
# =================================================================================================
import re  # noqa: E402
import subprocess  # noqa: E402

CONSUMERS = {
    'INF_A_00': ('data/inf/scripts/gold/INF_A_00.accounts_dimension.py', 'GUARDED'),    # control
    'INF_A_01': ('data/inf/scripts/gold/INF_A_01.advisor_assignments.py', 'UNGUARDED'),  # control
    'INF_C_07': ('data/inf/scripts/gold/INF_C_07.advisor_attribution.py', None),         # the subject
}


def guard_state(path: str) -> str:
    """Does this consumer RAISE on accounts absent from the resolution, or floor-and-continue?

    Grounded on FUNCTION, not mention: the script must both COUNT the absent set and RAISE on it.
    A floor alone is not a guard (A2 above proves the floored row still vanishes at INF_09:193)."""
    src = subprocess.run(['git', 'show', f'HEAD:{path}'], capture_output=True, text=True).stdout
    if not src.strip():
        raise RuntimeError(f'INSTRUMENT BROKEN: empty source for {path}. Refusing to score it.')
    lines = src.splitlines()
    at = next((i for i, ln in enumerate(lines) if 'attach_advisor_key(' in ln
               and 'def ' not in ln), None)
    if at is None:
        raise RuntimeError(f'INSTRUMENT BROKEN: no attach_advisor_key call site in {path}.')
    window = '\n'.join(lines[at:at + 45])          # from the attach to the end of its block
    counts_absent = bool(re.search(r'_n_absent\s*=', window))
    raises_on_it = bool(re.search(r'if\s+_n_absent\s*:', window) and 'raise' in window)
    return 'GUARDED' if (counts_absent and raises_on_it) else 'UNGUARDED'


print('\n' + '-' * 100)
print('A4  PER-CALL-SITE GUARD CENSUS -- the three FULL-ATTACH consumers (denominator: 3)')
print('-' * 100)
states, census_sound = {}, True
for name, (path, expected) in CONSUMERS.items():
    got = guard_state(path)
    states[name] = got
    ctrl = ''
    if expected:
        ok = (got == expected)
        census_sound &= ok
        ctrl = f'   [CONTROL: expected {expected} -> {"PASS" if ok else "CENSUS BROKEN"}]'
    mark = 'raises on absent -> fails CLOSED' if got == 'GUARDED' else \
           'FLOORS AND CONTINUES -> the row is served, then silently DROPPED'
    print(f'  {name:<10} {got:<10} {mark}{ctrl}')

if not census_sound:
    print('\nCENSUS BROKEN -- a control misfired. NO VERDICT on any consumer.')
    sys.exit(2)

unguarded = [n for n, s in states.items() if s == 'UNGUARDED']
check('A4 the guard census is SOUND (both controls scored correctly)', True,
      f'{len(unguarded)} of {len(CONSUMERS)} full-attach call sites are UNGUARDED: {unguarded}')

# ---- A5: the CONSEQUENCE at an unguarded call site (quantified, on the real filter) --------------
frame = pd.DataFrame({'account_id': [1, 2, 99], 'advisor_key': [pd.NA] * 3,
                      'rep_bucket': [pd.NA] * 3, 'nna': [30.0, 30.0, 30.0]})
frame, _ = ar.attach_advisor_key(frame, resolution(), absent='unknown')   # A_01:203 / C_07:280
served_nna = frame[frame['rep_bucket'] == 'individual']['nna'].sum()      # INF_09:193
total_nna = frame['nna'].sum()
check('A5 CONSEQUENCE at an UNGUARDED call site: the absent account is floored to a visibly-populated\n'
      "      advisor_key='unknown', carries rep_bucket=<NA>, and is then SILENTLY DROPPED at INF_09:193",
      served_nna < total_nna,
      f'NNA in the frame: ${total_nna:,.1f}   NNA surviving the rep_bucket filter: ${served_nna:,.1f}'
      f'   -> ${total_nna - served_nna:,.1f} VANISHES with no alarm.\n      '
      'The comments at A_01/C_07 claim the floor protects against exactly this. IT DOES NOT.')

print('\n' + '=' * 100)
if FAILS:
    print(f'F2 ARM: {len(FAILS)} FAILURE(S) -- {FAILS}')
    sys.exit(1)
print('F2 ARM @ HEAD -- SPLIT VERDICT. THIS IS NOT A GREEN.')
print('  CLOSED at INF_A_00 (:302 raises -- fails closed, does not over-condemn).')
print(f'  OPEN at {unguarded} -- they FLOOR AND CONTINUE. The floor closes the NULL and')
print('  not the LOSS: a visibly-populated advisor_key rides all the way to a SILENT drop.')
print('  >> A backstop that protects the OBSERVABLE and not the UNOBSERVABLE is a backstop for the')
print('  >> READER, not for the DATA. <<')
print('\n  I originally rendered "F2 CLOSED at HEAD" off INF_A_00 ALONE. That was a census of one.')
print('  Caught by CTO~B gate-1, re-grounded here. The unit is the CALL SITE.')
sys.exit(1)
