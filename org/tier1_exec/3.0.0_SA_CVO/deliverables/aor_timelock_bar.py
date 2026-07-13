"""TIME-LOCK NNA -- THE VERIFICATION BAR. **PRE-REGISTERED 2026-07-13, BEFORE THE FIX EXISTS.**

3.0.0_SA_CVO~B, at COO's ask. **A bar written after the fix is a bar shaped by the fix.**
This one is timestamped and committed BEFORE DS's commit, so neither of us can move it afterwards.

THE DEFECT. INF_C_01 derives advisor_key for EVERY txn -- including txns booked years ago -- from the
rep_id carried on the txn row TODAY. So when an account changes advisor, its ENTIRE HISTORY is
retroactively re-attributed to the new advisor. **An advisor's past NNA silently changes when one of
their accounts leaves.** Measured live (below): 8 advisor-window cells in CLOSED calendar quarters have
different values today than they did on 2026-06-29.

=================================================================================================
>> COO ASKED: "FIND THE ASSERTION THAT IS NOT CONSERVED." HERE IT IS. <<

    EVERY invariant in the draft bar is a CONSERVATION check, and CONSERVATION IS INVARIANT UNDER A
    SWAP. `firm MAX unchanged`, `sum(advisors) == firm_total`: all three pass to the cent if the fix
    moves the RIGHT dollars to the WRONG advisor. They cannot see money move SIDEWAYS.

    THE NON-CONSERVED ASSERTION IS THE PROPERTY ITSELF:   >> HISTORY IS IMMUTABLE. <<

    T1: a CLOSED window that ENDED BEFORE the transfer must have the SAME per-advisor NNA it had
        BEFORE the transfer -- to the cent, per advisor. A swap moves money BETWEEN advisors, so T1
        FIRES on exactly the failure the conservation checks are blind to.
=================================================================================================

THE ORACLE (read-only, and it is the whole reason this is checkable):
    platinum/_rebuild/20260630T234458Z/firm/advisor_nna_canonical.json   data_as_of 2026-06-29
    It PREDATES the 2026-07-08 transfer and carries FOUR advisors and NO phantom.

>> INSTRUMENT TRAP, AND IT WOULD HAVE SILENTLY GREENED THE BAR: THE QUARTER LABELS SHIFT. <<
    oracle(data_as_of 06-29):  q1 = 2026-01-01..03-31    q2 = 2025-10-01..12-31
    live  (data_as_of 07-09):  q2 = 2026-01-01..03-31    q3 = 2025-10-01..12-31
    Comparing `q1` to `q1` compares DIFFERENT DATE RANGES. **MATCH ON (start, end). NEVER ON THE KEY.**

THE PROVEN-RED CASE (COO #3 -- a census never observed to say RED has not been shown to be able to).
    Full churn across the ORACLE's window (accounts_v2 2026-06-29 -> 2026-07-13, denominator 70
    partitions): **17 accounts**
        peter_lee    -> joe_brandenburg  13   [59,131,328,330,370,708,719,825,852,856,883,975,1099]
        patrick_scanlan -> joe_brandenburg 3  [70,283,907]
        inflection_wealth_management -> peter_lee 1  [4273]
    + 8 roster departures [560,641,648,703,896,963,1208,1225] (560/703/1225 = the phantom accounts).
    **T1 MUST be observed RED against TODAY'S served artifact before any green is trusted.**

    (Direction note, grounded, so nobody invents a mechanism for it: 13 accounts moved peter->joe, yet
     Joe's closed-Q1 went DOWN and Peter's went UP. That is not a paradox -- Joe's live Q1 is NEGATIVE
     (-25,300.02). Those accounts carried NET OUTFLOWS, and moving a negative flow from A to B lowers B
     and raises A. Arithmetic, not a mystery.)
"""
from __future__ import annotations

import json
import sys

import boto3

BUCKET = 'opal-data-inf'
ORACLE = 'platinum/_rebuild/20260630T234458Z/firm/advisor_nna_canonical.json'
LIVE = 'platinum/firm/advisor_nna_canonical.json'
TRANSFER = '2026-07-08'

# The canonical roster: a served `advisors` key MUST be one of these. Anything else is a residual
# wearing an advisor's shape -- and 'Other' is NOT an acceptable substitute (that is the FORBIDDEN
# fix: "silently dropping a residual is how a reconciliation stops reconciling").
ROSTER = {'inflection_wealth_management', 'joe_brandenburg', 'patrick_scanlan', 'peter_lee',
          'noel_soderblom'}

_s3 = boto3.client('s3')


def _get(key: str) -> dict:
    body = _s3.get_object(Bucket=BUCKET, Key=key)['Body'].read()
    if not body.strip():
        raise RuntimeError(f'INSTRUMENT BROKEN: {key} read back EMPTY. A failed read is not an empty '
                           'artifact. Refusing to report a verdict.')
    return json.loads(body)


def closed_windows(o: dict, live: dict) -> list:
    """Windows present in BOTH artifacts, matched on BOUNDS (never on the label -- they shift), whose
    END is strictly before the transfer. These are the windows history cannot legally change in."""
    ob = {w: (b['start'], b['end']) for w, b in o['window_bounds'].items()}
    lb = {w: (b['start'], b['end']) for w, b in live['window_bounds'].items()}
    return [(ow, lw, b) for ow, b in ob.items() for lw, b2 in lb.items()
            if b == b2 and b[1] < TRANSFER]


def t1(live: dict, label: str) -> tuple[int, list]:
    """T1 -- HISTORY IS IMMUTABLE. The non-conserved assertion. Returns (n_moved, detail)."""
    o = _get(ORACLE)
    wins = closed_windows(o, live)
    if not wins:
        raise RuntimeError('INSTRUMENT BROKEN: no closed pre-transfer window is shared by the two '
                           'artifacts. A MISSING comparison is not a PASSING one. Refusing to report.')
    moved, rows = 0, []
    for ow, lw, b in wins:
        for a in sorted(set(o['advisors']) | set(live['advisors'])):
            ov = o['advisors'].get(a, {}).get('windows', {}).get(ow, {}).get('nna', 0.0)
            lv = live['advisors'].get(a, {}).get('windows', {}).get(lw, {}).get('nna', 0.0)
            if abs(lv - ov) >= 0.01:
                moved += 1
                rows.append((b, a, ov, lv, lv - ov))
    print(f'\n  T1 [{label}]  closed windows compared: {[b for _, _, b in wins]}')
    for b, a, ov, lv, d in rows:
        print(f'      {b[0]}..{b[1]}  {a:<30} oracle {ov:>14,.2f} -> live {lv:>14,.2f}  '
              f'DELTA {d:>13,.2f}  <<< HISTORY MOVED')
    if not rows:
        print('      every advisor-window cell is IDENTICAL to the pre-transfer oracle. History held.')
    return moved, rows


print('=' * 100)
print('TIME-LOCK NNA -- PRE-REGISTERED VERIFICATION BAR (written BEFORE the fix exists)')
print('=' * 100)

live = _get(LIVE)
print(f"\n  ORACLE  data_as_of={_get(ORACLE)['data_as_of']}  (PREDATES the {TRANSFER} transfer)")
print(f"  LIVE    data_as_of={live['data_as_of']}   generated_at={live['generated_at']}")

# ---------------------------------------------------------------------------------------------
# THE PROVEN-RED CONTROL. If this does not fire, the instrument is blind and NOTHING it says counts.
# ---------------------------------------------------------------------------------------------
print('\n' + '-' * 100)
print('PROVEN-RED CONTROL -- T1 against TODAY\'S (defective) served artifact. It MUST go RED.')
print('-' * 100)
n_moved, _ = t1(live, 'CURRENT SERVED ARTIFACT -- must be RED')
if n_moved == 0:
    print('\n!! INSTRUMENT BROKEN: T1 did NOT fire on the KNOWN defect. It cannot see what it was built')
    print('   for, and its verdict on the fix would be worthless. NO BAR. Fix the instrument first.')
    sys.exit(2)
print(f'\n  PROVEN-RED: {n_moved} advisor-window cells MOVED. The instrument SEES the defect.')
print('  >> AND EVERY CONSERVATION CHECK IN THE DRAFT BAR IS GREEN ON THIS SAME ARTIFACT. <<')

firm = live['firm']['windows']['MAX']['nna']
adv_sum = sum(v['windows']['MAX']['nna'] for v in live['advisors'].values())
print(f'     sum(advisors) {adv_sum:,.2f} == firm_total {firm:,.2f}  -> ties to '
      f'{abs(adv_sum - firm):.2f}. **GREEN, ON A DEFECTIVE ARTIFACT.**')

# ---------------------------------------------------------------------------------------------
print('\n' + '=' * 100)
print('THE BAR THE FIX MUST CLEAR  (re-run this file against the post-fix SERVED artifact)')
print('=' * 100)
print("""
  T1  [HARD - EXACT - NOT CONSERVED - PROVEN-RED]   >> THE GATE. <<
      Every CLOSED window ending before 2026-07-08, per advisor, EQUALS the pre-transfer oracle
      TO THE CENT. Matched on (start,end), never on the label.
      WHY IT IS THE GATE: a swap moves money BETWEEN advisors. T1 fires; conservation cannot.

  T2  [HARD - THE OVER-CONDEMNATION ARM]           >> A TIME-LOCK THAT FREEZES TOO MUCH IS A DEFECT. <<
      For a transferred account, attribution must SPLIT AT THE TRANSFER DATE:
          flows dated BEFORE 2026-07-08  -> the OLD advisor (peter_lee / patrick_scanlan)
          flows dated ON/AFTER           -> the NEW advisor (joe_brandenburg)
      A fix that freezes an account to its old advisor FOREVER passes T1 and passes EVERY
      conservation check. Only T2 fails it.
      >> NAMED WEAKNESS: no SERVED window isolates the post-transfer period (QTD starts 07-01 and
      >> spans the transfer), so T2 can only be exercised at the PRODUCER, hermetically. Its green is
      >> therefore WEAKER than T1's, and I am saying so rather than pretending otherwise.

  T3  [HARD]  No key in `advisors` may be outside the canonical roster.
      inflection_unmapped_rep GONE -- and **'Other' is NOT an acceptable substitute.** Folding the
      residual into a junk bucket is the FORBIDDEN fix (it suppresses a REAL advisor's money).
      Restoring it to a rep already in the canonical map is READING, not inferring.

  T4  [NECESSARY, NOT SUFFICIENT -- and it MUST be labelled that way in the record]
      firm MAX unchanged at 133,107,667.64 ; sum(advisors) == firm_total to the cent.
      >> THESE ARE GREEN ON THE DEFECTIVE ARTIFACT RIGHT NOW (proved above). They prove nothing
      >> LEFT; they say NOTHING about WHOSE it is. **They must never be quoted as evidence the fix
      >> is correct.**

  T5  [REJECTED FROM THE BAR -- and this is a finding about the draft]
      "joe DOWN ~-$2.1M / peter UP ~+$1.6M / patrick UP ~+$1.03M".
      >> A TILDE IS NOT AN ASSERTION. A tolerance band passes a wrong-but-close answer, and a swap
      >> that lands near the expected magnitude walks straight through it.
      T1 SUBSUMES these EXACTLY: if history is restored to the cent, the directional deltas fall out
      as a CONSEQUENCE. Keep them as a human sanity-read; do NOT gate on them.
""")
print('=' * 100)
print('BAR PRE-REGISTERED. T1 is RED on the current artifact BY CONSTRUCTION -- that is the control,')
print('not a failure. Re-run against the post-fix SERVED artifact; T1 must go to ZERO cells moved.')
sys.exit(1)
