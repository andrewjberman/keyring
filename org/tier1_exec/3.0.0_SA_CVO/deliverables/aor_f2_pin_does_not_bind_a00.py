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
# =================================================================================================
# A2 -- REWRITTEN AT 59d70b95e. **MY PREVIOUS A2 ASSERTED THE DEFECT AND A GOOD FIX BROKE IT.**
#
# It read:   check('...LEAVES THE SILENT FIELD NULL', pd.isna(rb))
# i.e. it DEMANDED that rep_bucket stay <NA> -- which is precisely the thing that silently drops the
# row from per-advisor NNA. The fix floors it to an explicit 'unresolved', and my arm went
# **FAIL: rep_bucket = 'unresolved'**. The tempting "repair" was to revert the code.
#     A TEST THAT ASSERTS THE DEFECT WILL DEFEND IT.
# Third time today, in my own battery, and CTO~B warned me about this exact class ONE MESSAGE before
# it happened (his own gate-1 arm A had the mirror-image error: it demanded the absent row SURVIVE
# into per-advisor NNA -- which demands FABRICATED attribution, the phantom sin in reverse).
#
# >> WRITE THE ASSERTION FROM THE PROPERTY YOU WANT, NEVER FROM THE SHAPE OF THE DEFECT. <<
#
# THE PROPERTY (and it is NOT "the row must survive", and NOT "rep_bucket must be null"):
#     AN ABSENT ACCOUNT'S LOSS MUST NEVER BE SILENT. It must be EXCLUDED BY DECISION and DISCLOSED.
# Grounded on the real consumer, INF_09.generate_partner_analytics.py @ 59d70b95e:
#     :188  firm_nna = window['net_nna'].sum()                      <- NOT rep_bucket-filtered
#     :193  indiv    = window[window['rep_bucket'] == 'individual'] <- per-advisor IS filtered
# So a row with rep_bucket='unresolved' is EXCLUDED from per-advisor and REMAINS in the firm total
# => sum(advisors) < firm_total, and the residual is VISIBLE and RECONCILABLE. That is the disclosure.
# =================================================================================================
dim, _ = ar.attach_advisor_key(a00_frame(True), resolution(), absent='unknown')
row = dim[pd.to_numeric(dim['account_id'], errors='coerce') == 99].iloc[0]
ak, rb = row['advisor_key'], row['rep_bucket']

check('A2.P1 the exclusion is a DECISION, not an artifact: rep_bucket is floored to an EXPLICIT named '
      'bucket, never left <NA> (a null exclusion is dtype-dependent and unpinned)',
      (not pd.isna(rb)) and rb == ar.UNRESOLVED_REP_BUCKET,
      f'rep_bucket = {rb!r}   advisor_key = {ak!r}')

# ASSERT THE THING, NOT A PROXY FOR IT: INF_09:193 is a SERIES MASK, and a mask coerces NA -> False.
# A scalar `rb == 'individual'` yields pd.NA and cannot answer. Run the REAL filter.
indiv = dim[dim['rep_bucket'] == 'individual']                 # INF_09:193, verbatim in behaviour
attributed = set(pd.to_numeric(indiv['account_id'], errors='coerce').dropna().astype(int))
check('A2.P2 NO FABRICATED ATTRIBUTION: the unattributable row is NOT rolled into any named advisor '
      "(it must never be served as somebody's NNA)",
      99 not in attributed,
      f'per-advisor rollup contains: {sorted(attributed)}  -- 99 correctly EXCLUDED. '
      '(CTO~B\'s gate-1 arm demanded the OPPOSITE and DS refused it. He was right.)')

# P3 -- the disclosure. firm total is UNFILTERED (INF_09:188), so the row stays in it.
dim['nna'] = 30.0
firm_total = float(dim['nna'].sum())                            # INF_09:188 -- no rep_bucket filter
per_advisor = float(dim[dim['rep_bucket'] == 'individual']['nna'].sum())   # INF_09:193
residual = firm_total - per_advisor
check('A2.P3 THE LOSS IS DISCLOSED, not silently absorbed: the row REMAINS in the firm total, so '
      'sum(advisors) < firm_total and the residual is VISIBLE and RECONCILABLE',
      residual > 0,
      f'firm total {firm_total:.1f}  |  sum over per-advisor {per_advisor:.1f}  |  '
      f'VISIBLE RESIDUAL {residual:.1f}\n      '
      'THAT is the property. Not "the row survives" (fabrication) and not "rep_bucket is null" (the '
      'defect) -- but "the loss is DISCLOSED rather than SILENT."')

# P4 -- the structural gate: the incoherent shape is UNCONDITIONALLY refused.
try:
    bad = pd.DataFrame({'account_id': [7], 'advisor_key': ['peter_lee'], 'rep_bucket': [pd.NA]})
    ar.attach_advisor_key(bad, resolution(), absent=None)
    check('A2.P4 the INCOHERENT shape (non-null advisor_key + NULL rep_bucket) is REFUSED', False,
          'IT RETURNED. The row that looks perfectly attributed and vanishes from every aggregate '
          'is emittable again.')
except RuntimeError as e:
    check('A2.P4 the INCOHERENT shape (non-null advisor_key + NULL rep_bucket) is REFUSED '
          '-- unconditionally, on EVERY path, incl. absent=None', True, f'RuntimeError: {str(e)[:96]}...')

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

# >> AND THE CENSUS ITSELF WAS ASSERTING MY REMEDY, NOT THE PROPERTY. <<
# Pre-59d70b95e this block FAILED whenever any call site did not RAISE -- i.e. it demanded ONE
# SPECIFIC FIX SHAPE ("make A_01 and C_07 raise like A_00 does"). That was MY proposed remedy, and
# a bar that encodes a remedy grades the fixer on obedience, not on correctness.
# DS chose a DIFFERENT and better shape: floor rep_bucket to an EXPLICIT 'unresolved' (so the
# exclusion is a DECISION), EXCLUDE the row from per-advisor rollups (never fabricate attribution),
# LEAVE it in the firm total (so the residual is VISIBLE and reconcilable), ALARM by account, and
# RAISE unconditionally on the incoherent shape. **That satisfies the property without the raise.**
# So the census now REPORTS the shapes and the VERDICT is rendered on P1-P4 above, not on this.
# A_00 additionally RAISES (:302) and runs FIRST in the chain -- a gate on top of the disclosure.
check('A4 per-call-site census (denominator 3): the SHAPES, reported -- not a pass/fail on my remedy',
      True,
      f'GATED (raises): {[n for n, s in states.items() if s == "GUARDED"]}   |   '
      f'DISCLOSING (floor+alarm+exclude-by-decision): {unguarded}\n      '
      'Both shapes satisfy the property. The verdict is P1-P4, not "did they adopt my fix".')

print('\n' + '=' * 100)
if FAILS:
    print(f'F2 ARM: {len(FAILS)} FAILURE(S) -- {FAILS}')
    print('  NOTE BEFORE YOU "FIX" THE CODE: ask FIRST whether this ARM was encoding the bug.')
    print('  It has done so twice already (absent=None; rep_bucket-must-be-null).')
    sys.exit(1)
print('F2 ARM: GREEN AT 59d70b95e. The absent-account loss can no longer be SILENT.')
print('  P1 the exclusion is a DECISION (rep_bucket -> explicit \'unresolved\', never <NA>)')
print('  P2 NO fabricated attribution -- the unattributable row is never rolled into a named advisor')
print('  P3 the loss is DISCLOSED -- the row stays in the firm total, so sum(advisors) < firm_total')
print('     is VISIBLE and reconcilable (INF_09:188 unfiltered / :193 filtered -- verified at source)')
print('  P4 the incoherent shape (non-null key + null bucket) is REFUSED unconditionally')
print('  + INF_A_00:302 RAISES and runs FIRST in the chain -- a gate on top of the disclosure.')
print('\n  RESIDUAL, NAMED HONESTLY AND *NOT* A BLOCKER: the residual is VISIBLE but not ASSERTED.')
print('  Nothing raises on `sum(advisors) + unattributed != firm_total` -- that is ruling (iii)\'s')
print('  durable fix and it is not built. A WARN IN A LOG IS NOT A GATE. It is not a blocker because')
print('  the absent set is empty by construction today (pin + source-digest assertion => the resolver')
print('  and every consumer read the SAME accounts_v2 bytes => identical account sets), A_00 raises,')
print('  and the incoherent shape raises. It is defence-in-depth for the day that invariant breaks.')
sys.exit(0)
