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
    ('aor_f2_pin_does_not_bind_a00.py', 'the absent-account path fails closed at EVERY full-attach '
                                        'call site', 1),   # RED: 2 of 3 UNGUARDED -- a WITHHOLD
    ('aor_r2_null_stamp.py', 'the chokepoint asserts the ROW, not the column', 1),  # RED -- a WITHHOLD
    ('aor_phantom_advisor_arm.py', 'no key on the served per-advisor NNA is a non-advisor', 1),  # RED
    ('aor_phantom_switch_arm.py', 'the go-live switch does not move the phantom bucket', 0),
    ('aor_gate2_fix_bar.py', 'BOTH withholds discharged AND neither fix over-condemns', 1),  # RED by
                                                                                            # construction
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
print(f'BATTERY CONSISTENT AT HEAD: {len(rows)} live arms, {len(EXCLUDED)} declared exclusions.')
print('  GATE-2 = WITHHELD. The REDs are the two withholds (F2 at INF_A_01/INF_C_07; R2 row-vs-column)')
print('  plus the phantom (RED, but NOT a gate-2 blocker -- exercised switch-independent on TODAY\'s data)')
print('  and the pre-registered fix bar (RED by construction until the fixes land).')
print('  V4 SERVED-VERIFY: NOT RUN -- blocked by the INF chain freeze. An EXPLICIT GAP, never a PASS,')
print('  and NO fixture green in this battery closes it.')
sys.exit(0)
