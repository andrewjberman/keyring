"""GATE-2 BATTERY RUNNER (3.0.0_SA_CVO~B) -- THE DENOMINATOR OF MY OWN BATTERY, MADE EXPLICIT.

WHY THIS EXISTS. On 2026-07-13 I re-ran my AoR battery at HEAD and **FIVE of my own instruments were
broken** -- and the two worst were broken in the direction that LIES CONFIDENTLY:

    aor_served_view_under_on.py   turned a fail-closed GUARD into "*** RED -- THE FOLD IS ERASED ***"
    aor_r182_key_verify.py        verified a key that no longer ships, and concluded, at exit 1,
                                  in my own voice: "DOES NOT DISCRIMINATE -- do not ship this key."

Both were CORRECT WHEN WRITTEN. The ground moved under them. **A STALE ARM DOES NOT GO QUIET; IT GOES
CONFIDENT.** And a false RED is the dangerous direction, because its remedy is DESTRUCTIVE -- reopen a
closed fix, revert good work, or (worst) "fix" the guard that was doing its job.

So: **anyone who runs `python *.py` across this directory WILL be misled.** This runner exists so that
the LIVE battery is a named, executable set, and every arm NOT in it is DECLARED, not silently omitted.

    NO SILENT CAPS. If an arm is excluded, this file says so and says WHY.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# -- THE LIVE GATE-2 BATTERY -------------------------------------------------------------------
# (arm, what a GREEN means, expected exit at HEAD as of 59c24b46e)
LIVE = [
    ('aor_gate2_final_matrix.py', 'the (source_digest, fold_mode, code_digest) key discriminates on '
                                  'all 3 inputs AND does not brick --single', 0),
    ('aor_round8_battery.py', 'the round-8 regression battery (35 arms)', 0),
    ('aor_served_view_under_on.py', 'the fold SURVIVES to the served view (RED at the proven-RED '
                                    'control 69219a7db -- it can see the defect it clears)', 0),
    ('aor_off_is_a_noop_guard.py', 'under OFF the fold is a structural no-op (DELTA-0)', 0),
    ('aor_f4_and_inherit_census.py', 'F4 fails closed on the UNOBSERVABLE', 0),
    # v2 @ 59d70b95e -- WITHHOLDS DISCHARGED. Both flipped 1 -> 0 when DS's fixes landed, and the
    # over-condemnation controls STAYED green. If either ever flips back, the runner says CHANGED.
    ('aor_f2_pin_does_not_bind_a00.py', "an absent account's loss is DISCLOSED, never SILENT "
                                        '(exclusion by DECISION + no fabricated attribution + visible '
                                        'residual + incoherent shape refused)', 0),
    # I PREDICTED THIS WOULD STAY AT 1 AND THE RUNNER CAUGHT ME. It exits 0 at 59d70b95e: base CVO's
    # falsifier now RAISES on both attacks (N1, N2) while its non-placebo control C1 still RETURNS.
    # Her arm confirms the fix independently of mine. **The runner refused to accept a changed arm
    # silently -- which is the entire reason it exists.**
    ('aor_r2_null_stamp.py', 'the chokepoint asserts the ROW, not the column', 0),
    ('aor_phantom_advisor_arm.py', 'no key on the served per-advisor NNA is a non-advisor', 1),  # RED
    # -- LIVE on the served spine, but NOT a gate-2 blocker (switch-independent on today's data).
    ('aor_phantom_switch_arm.py', 'the go-live switch does not move the phantom bucket', 0),
    ('aor_gate2_fix_bar.py', 'BOTH withholds discharged AND neither fix over-condemns', 0),  # 5/5
]

# -- DECLARED EXCLUSIONS -- these are NOT run, and here is exactly why -------------------------
EXCLUDED = {
    'aor_r182_key_verify.py':
        'SUPERSEDED. Verifies the 2-input key; the shipped key grew `code_digest`. Its unstamped '
        'fixtures raise CORRECTLY, so it concluded "do not ship this key" -- a CONFIDENT FALSE RED. '
        'It now self-detects and refuses (exit 2). Live replacement: aor_gate2_final_matrix.py.',
    'aor_a3_through_the_dispatch.py':
        'SUPERSEDED BY R5. Its premise was "the dispatch proves the resolver is NOT SCHEDULED under '
        'OFF." R5 de-multiplexed exactly that: chain entry is PRESENCE-gated, not switch-gated '
        '(orion-gold-dispatch.sh:445-452, all EIGHT chains; :433 fails closed). It correctly refuses '
        'to report rather than emitting a false verdict.',
    'aor_f1_chokepoint_verify_v2.py':
        'HISTORICAL. Verified an EARLIER proposed key (pre-(source_digest,fold_mode)). Kept as the '
        'record of how that key was killed. Its verdict text does NOT describe the shipped key.',
    'aor_f1_rollback_falsifier.py':
        'HISTORICAL. The arm that falsified the (as_of) key by finding the same-pin rollback. Its '
        'job is done and its output is about a key that no longer exists.',
    'aor_r1_run_vs_source.py':
        'HISTORICAL (R1 round). Exits 2 -- it already refuses to render.',
    'aor_r1_two_vintage_matrix.py':
        'HISTORICAL (R1 round). Crashes at HEAD (IndexError) -- an INSTRUMENT BREAK, not a verdict. '
        'Its question (does the 2-vintage matrix discriminate?) was answered NO and superseded.',
    # -- declared 2026-07-15 (det-#5 pre-read; the four arms built 07-13 PM, after this runner) --------
    'aor_timelock_bar.py':
        'TIME-LOCK CHAPTER, and SUPERSEDED BY v2 ON THE GRAIN: DS ran it and found the as_of oracle '
        'truncates the quarter it was cut in (fork-BLIND, not fork-neutral -- it never checked Q2-2026, '
        'the quarter holding the contested money). Not a gate-2 arm.',
    'aor_timelock_bar_v2_account_grain.py':
        'TIME-LOCK CHAPTER (the pre-registered lock bar, account grain). Fires at the LOCK MOMENT on the '
        'dry-run/served artifacts per the stamp-order law -- inside the V4 window, NOT the gate-2 '
        'mechanism battery. Running it tonight would grade a lock that has never executed.',
    'aor_property_and_provenance_arm.py':
        'TIME-LOCK CHAPTER (P1-P3: backfill property vs named instance; row-keyed provenance). The '
        'properties now live in the timelock suite at HEAD; the arm re-fires with the lock verify at the '
        'V4 window, not in the gate-2 mechanism battery.',
    'aor_served_layer_stamp_arm.py':
        'RIDES THE SERVE MOMENT (V4): asserts stamp-survival on the SERVED layer, which cannot be '
        'exercised before the first stamped artifact exists. Its question is folded into det-#5 section-6 '
        '(V4 bar). NOTE 07-15: its INF_09:406 serve-time re-fold citation is one of the three consumers '
        'whose --upload legs CTO held this window (194d3d674) -- the arm and the hold agree.',
}

print('=' * 100)
print('AoR GATE-2 BATTERY -- LIVE ARMS ONLY. Every exclusion below is DECLARED, never silent.')
print('=' * 100)

# Fail loud if the directory contains an arm this runner has never heard of -- a NEW arm that nobody
# declared is exactly how a silent cap gets in.
on_disk = {p.name for p in HERE.glob('aor_*.py')}
known = {a for a, _, _ in LIVE} | set(EXCLUDED) | {Path(__file__).name}
undeclared = on_disk - known
if undeclared:
    print(f'\n!! UNDECLARED ARMS ON DISK: {sorted(undeclared)}')
    print('   This runner does not know whether they are LIVE or SUPERSEDED. Declare them, then re-run.')
    print('   (An arm nobody declared is how a silent cap gets in.)')
    sys.exit(2)

rows, broke = [], []
for arm, means, expect in LIVE:
    r = subprocess.run([sys.executable, str(HERE / arm)], capture_output=True, text=True, cwd=HERE.parents[3])
    got = r.returncode
    if got == 2:
        broke.append(arm)
        state = 'INSTRUMENT BREAK'
    elif got == expect:
        state = 'GREEN' if expect == 0 else 'RED (expected -- a WITHHOLD)'
    else:
        state = f'*** CHANGED *** (expected {expect}, got {got})'
    rows.append((arm, state, means))

w = max(len(a) for a, _, _ in rows)
for arm, state, means in rows:
    print(f'\n  {arm:<{w}}  {state}')
    print(f'  {"":<{w}}  -> {means}')

print('\n' + '-' * 100)
print('  DECLARED EXCLUSIONS (NOT run -- and this is the whole point of the file):')
for arm, why in EXCLUDED.items():
    print(f'\n  {arm}\n      {why}')

print('\n' + '=' * 100)
changed = [a for a, s, _ in rows if 'CHANGED' in s]
if broke:
    print(f'INSTRUMENT BREAK in: {broke}. NO VERDICT -- an arm that could not run is not evidence.')
    sys.exit(2)
if changed:
    print(f'!! AN ARM CHANGED STATE: {changed}')
    print('   Something moved under the battery. RE-GROUND before quoting any of it.')
    sys.exit(1)
print(f'BATTERY CONSISTENT AT 59d70b95e: {len(rows)} live arms, {len(EXCLUDED)} declared exclusions.')
print('  GATE-2 = CLEARED (determination #4). Both withholds DISCHARGED at 59d70b95e:')
print('    F2 -- an absent account\'s loss is now DISCLOSED, never silent (exclusion by DECISION, no')
print('          fabricated attribution, visible reconcilable residual, incoherent shape refused).')
print('    R2 -- the chokepoint asserts the ROW. Confirmed independently by base CVO\'s own falsifier')
print('          (its attacks N1/N2 now RAISE while its non-placebo control C1 still RETURNS).')
print('  And the OVER-CONDEMNATION controls STAYED GREEN -- neither fix fires on a legitimate run.')
print('\n  THE ONE RED IS EXPECTED AND IS **NOT** A GATE-2 BLOCKER:')
print('    the PHANTOM is LIVE on the served spine ($52,604.80 on a key that is not an advisor), but it')
print('    is EXERCISED switch-independent on TODAY\'s data (the 3 accounts are ROSTER-ABSENT, so the')
print('    fold cannot reach them). Separate chapter; its fix is blocked by the INF hold.')
print('\n  >> CLEARING GATE-2 DOES NOT AUTHORIZE GO-LIVE, AND NOTHING IN THIS BATTERY DOES. <<')
print('  V4 SERVED-VERIFY: NOT RUN. It verifies the FIRST NIGHTLY *AFTER* the switch flips, so it is a')
print('  POST-cutover step and cannot be a precondition of a PRE-cutover gate. It remains an EXPLICIT')
print('  GAP -- never a PASS -- and NO fixture green in this battery closes it. Still required and NOT')
print('  mine: CHANGE-2, the never-widen co-sign, the INF hold-lift, and Andrew\'s GO.')
sys.exit(0)
