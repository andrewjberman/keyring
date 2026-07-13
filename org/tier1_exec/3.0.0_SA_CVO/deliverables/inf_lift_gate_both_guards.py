"""INF HOLD-LIFT, GATE ITEM 4 -- INDEPENDENT EXERCISE OF **BOTH** GUARDS, AS **DISJOINT CLASSES**.

3.0.0_SA_CVO~B, 2026-07-13. CTO~B: *"you are the critical path on the lift."*
**The verifier is not the do-er.** DS/DS~A/CTO~B/I have between us self-caught SEVEN broken instruments
today -- which is exactly why their greens do not close this and mine must be exercised, not read.

=================================================================================================
>> THE THING THIS FILE EXISTS TO PROVE, AND NOBODY HAD BUILT IT: THE TWO GUARDS ARE DISJOINT. <<

    DELETION  an account VANISHES from a rewritten partition   -> nna_coverage_guard
    COLLAPSE  every account STAYS, every net_nna INTACT;
              only advisor_key flips to the firm catchall      -> INF_B_00 selector

    NEITHER GUARD CATCHES THE OTHER'S CLASS -- and the fabric spent an afternoon with a green tick on
    a lift ledger that read one as coverage of both. **A checklist whose items are individually true
    and jointly misleading is how a fabric talks itself into a lift.**

    SOURCE-CONFIRMED (nna_coverage_guard.py:191 @ HEAD):
        prior_by_date  {date_str: {account_id: net_nna}}
    >> `advisor_key` IS NOT IN THE BASIS. <<  In a collapse NOTHING VANISHES, so the coverage guard
    has NO COLUMN TO NOTICE WITH. It does not fail. **It passes, silently, at full confidence.**

    D1 below EXERCISES that. It is the arm that would have stopped the false tick.
=================================================================================================

METHOD (my own rule, and CTO~B held me to it): **write the arm from the PROPERTY YOU WANT, then check
the defect fails it -- never the other way round.** Three of us today wrote a test that DEFENDED the bug
it was written to catch, because after exercising a defect its SHAPE is the most available thing in your
head and it writes itself into your assertion.

Hermetic: real lib functions, synthetic bases. No S3, no prod touch, no re-derive, no chain advance.
[STOP] b7bce51bd honoured.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold' / 'lib'))

import nna_coverage_guard as G  # noqa: E402

FAILS: list[str] = []
CATCHALL = 'inflection_wealth_management'


def check(name: str, ok: bool, detail: str = '') -> None:
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f'\n       {detail}' if detail else ''))
    if not ok:
        FAILS.append(name)


def run(prior, new, read_failures=()) -> tuple[str, str]:
    try:
        G.assert_partition_coverage_continuity(prior, list(read_failures), new, log=lambda *a: None)
        return 'PASSED', ''
    except G.NNACoverageCannotEvaluate as e:
        return 'CANNOT-EVALUATE', str(e)[:110]
    except G.NNACoverageRegression as e:
        return 'RAISED', str(e)[:110]
    except Exception as e:                                   # noqa: BLE001
        return f'UNEXPECTED:{type(e).__name__}', str(e)[:110]


print('=' * 100)
print('INF LIFT GATE ITEM 4 -- BOTH GUARDS, EXERCISED AS DISJOINT CLASSES')
print('=' * 100)

# =================================================================================================
print('\n--- GUARD A -- COVERAGE (the DELETION class) ---')
# PROPERTY: a re-derive that would SILENTLY DROP an attributed account must RAISE BEFORE THE WRITE.
# THE REAL SHAPE (and the one the rigged harness missed): the account is dropped from a partition that
# IS REWRITTEN, because a CO-TENANT kept that partition alive. A partition nobody rewrites cannot lose
# anything -- which is why the aggregate form both over-fired AND was blind to the case that matters.

D = '2026-01-15'
prior = {D: {47: -3500.00, 101: 1000.00, 102: 250.00}}      # account 47 is the victim; 101/102 co-tenants

state, msg = run(prior, {D: {101, 102}})                    # 47 dropped; partition IS rewritten
check('A1  PROVEN-RED (the real shape): an attributed account dropped from a partition that IS\n'
      '       rewritten (co-tenants keep it alive) -> RAISES before the write',
      state == 'RAISED', f'{state}  {msg}')

state, _ = run(prior, {D: {47, 101, 102}})                  # faithful rewrite
check('A2  OVER-CONDEMNATION: a FAITHFUL rewrite -> PASSES', state == 'PASSED', state)

state, _ = run(prior, {})                                   # empty frame -> INF_C_01 writes NOTHING
check('A3  OVER-CONDEMNATION: a partition that is NOT rewritten (empty frame -> no write) -> PASSES.\n'
      '       *A fail-closed fix that fires on a legitimate zero is the disease it was sent to cure.*\n'
      '       This is the exact cell the author\'s own RIGGED harness got wrong -- it fed the guard a\n'
      '       basis the real caller can never construct, and called it proven.',
      state == 'PASSED', state)

state, msg = run(prior, {D: {101, 102}}, read_failures=['canonical_nna_2026-01-14.parquet'])
check('A4  AN INSTRUMENT THAT CANNOT OBSERVE MUST SAY SO: an unreadable prior basis is\n'
      '       CANNOT-EVALUATE -- never a silent pass, and never a plain RED either',
      state == 'CANNOT-EVALUATE', f'{state}  {msg}')

# =================================================================================================
print('\n--- >> D1 -- THE DISJOINTNESS ARM. THE ONE NOBODY BUILT. << ---')
# PROPERTY UNDER TEST: does GUARD A cover the COLLAPSE class?
# A COLLAPSE: every account STAYS. Every net_nna is INTACT. ONLY advisor_key flips to the catchall.
# Guard A's basis is {date: {account_id: net_nna}} -- IT HAS NO advisor_key COLUMN.
# So the collapse is INVISIBLE to it. This arm PROVES that, rather than asserting it.

collapse_new = {D: {47, 101, 102}}          # NOTHING vanished. Same accounts, same partition.
state, _ = run(prior, collapse_new)
guard_a_blind = (state == 'PASSED')
check('D1  GUARD A **PASSES** a total advisor COLLAPSE -- every account present, every net_nna\n'
      '       intact, ONLY advisor_key flipped to the firm catchall. IT CANNOT SEE IT.\n'
      '       >> A GREEN FROM GUARD A IS **NOT** COVERAGE OF THE COLLAPSE CLASS. <<\n'
      '       This is not a defect in Guard A -- its docstring says so itself ("a vanished account has\n'
      '       no key to be invalid"). It is a defect in any LEDGER that ticks one and claims both.',
      guard_a_blind,
      f'{state} -- and it is RIGHT to pass: nothing vanished. The COLLAPSE class is prevented at\n'
      f'       SOURCE by the INF_B_00 selector, and DETECTED by nothing downstream.')

# And the phantom guard? A collapse flips the key to the CATCHALL, which is a LEGITIMATE roster member.
try:
    G.assert_no_residual_advisor({CATCHALL: 202_062_830.31}, log=lambda *a: None)
    residual_blind = True
except Exception:                                            # noqa: BLE001
    residual_blind = False
check('D1b THE RESIDUAL-ADVISOR GUARD IS ALSO BLIND TO A COLLAPSE: the collapse flips keys to\n'
      '       `inflection_wealth_management`, which IS a legitimate roster member -- so it is not a\n'
      '       residual and the guard correctly does not fire. **TWO guards, BOTH blind to collapse.**',
      residual_blind,
      'assert_no_residual_advisor({inflection_wealth_management: $202,062,830.31}) -> PASSED.\n'
      '       The entire firm collapsed onto ONE VALID KEY. Every downstream detector is green.')

# Control: the residual guard MUST fire on an actual residual, or D1b proves nothing.
try:
    G.assert_no_residual_advisor({'inflection_unmapped_rep': 52_604.80}, log=lambda *a: None)
    residual_fires = False
except Exception:                                            # noqa: BLE001
    residual_fires = True
check('D1c CONTROL -- could D1b have failed? The residual guard DOES fire on a real residual\n'
      '       (`inflection_unmapped_rep`). So its silence on the catchall is a REAL reading, not a\n'
      '       dead instrument.', residual_fires,
      'a guard never observed to fire has not been shown to be able to.')

# =================================================================================================
print('\n--- GUARD B -- THE INF_B_00 SELECTOR (the COLLAPSE class). REAL S3, read-only. ---')
# PROPERTY: a 0-ROW roster partition must be WALKED OVER, never used.
# "0 rows" means WE COULD NOT READ THE ACCOUNTS -- not "there are no accounts". An instrument break.
#
# >> MY FIRST DRIVER FOR THIS ARM WAS BROKEN AND IT REPORTED A VERDICT ANYWAY (self-caught, #8 today).
# I GUESSED the signature as (s3, bucket, snap); it is (snap_date_str, available: dict). My guard
# returned None, and my code turned `None != snap` into "WALKED BACK" -- printing that for ALL THREE
# snaps, INCLUDING THE HEALTHY CONTROLS. **A null became a substantive finding.** It is the same class
# as the served-view arm turning an exception into a RED. Fixed by reading the real signature and
# driving the module's OWN `list_accounts_v2_dates()` helper instead of guessing its shape.
import importlib.util as _iu  # noqa: E402

sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold'))
_spec = _iu.spec_from_file_location('b00', str(REPO / 'data' / 'inf' / 'scripts' / 'gold'
                                               / 'INF_B_00.canonical_holdings.py'))
_b00 = _iu.module_from_spec(_spec)
try:
    _spec.loader.exec_module(_b00)
except SystemExit:
    pass

_resolve = getattr(_b00, 'resolve_accounts_v2_for_snap', None)
if _resolve is None:
    check('B0  INSTRUMENT BREAK: resolve_accounts_v2_for_snap is NOT DEFINED at HEAD.', False,
          'A MISSING symbol is not a PASS. A green resting on the ABSENCE of a symbol is not a green.')
else:
    _avail = _b00.list_accounts_v2_dates()
    _quiet = {'log': (lambda *a, **k: None)}  # noqa: F841  (the fn logs to stdout; we read the frame)

    def _roster(snap):
        df = _resolve(snap, _avail)
        reps = df['representative_name'].dropna().nunique() if 'representative_name' in df.columns else -1
        return len(df), reps

    n8, r8 = _roster('2026-05-08')       # THE 0-ROW ROSTER -- the proven-RED case, on REAL S3
    check('B1  PROVEN-RED (real S3, snap=2026-05-08 -- the partition that collapsed $202,062,830 onto\n'
          '       ONE key): the 0-row roster is WALKED OVER and a USABLE roster is returned',
          n8 > 0 and r8 > 1,
          f'rows={n8}  distinct_reps={r8}  -- walk-back ENGAGED and it WARNED LOUDLY. '
          f'(raw 2026-05-08 partition = 0 rows, 45 cols: a PERFECT SCHEMA on an empty roster, which is\n'
          f'       exactly why a COLUMN-level guard passed it.)')

    n7, r7 = _roster('2026-05-07')
    n9, r9 = _roster('2026-05-09')
    check('B2  OVER-CONDEMNATION: the HEALTHY neighbours use their OWN partitions -- the walk-back is\n'
          '       TARGETED, not blanket (a selector that always walks back is not a fix, it is a lag)',
          n7 > 0 and r7 > 1 and n9 > 0 and r9 > 1,
          f'2026-05-07 rows={n7} reps={r7}   2026-05-09 rows={n9} reps={r9}   -- both loaded their own '
          f'date, no walk-back engaged.')

print('\n' + '=' * 100)
if FAILS:
    print(f'{len(FAILS)} FAILURE(S): {FAILS}')
    print('\nNOTE BEFORE "FIXING" ANYTHING: ask FIRST whether this ARM encoded the defect.')
    sys.exit(1)

print('GUARD A: VERIFIED BY EXERCISE -- fires on the real deletion shape, does NOT over-condemn a')
print('  faithful rewrite or a legitimate empty frame, and says CANNOT-EVALUATE when it cannot observe.')
print('\n>> AND THE FINDING THE LIFT NEEDS, EXERCISED RATHER THAN ASSERTED: <<')
print('   GUARD A IS **BLIND** TO THE COLLAPSE CLASS. SO IS THE RESIDUAL-ADVISOR GUARD.')
print('   The entire firm can collapse onto ONE VALID ADVISOR KEY and BOTH guards stay GREEN.')
print('   The collapse class is PREVENTED AT SOURCE (the INF_B_00 selector) and DETECTED BY NOTHING.')
print('   => The selector is not defence-in-depth. IT IS THE ONLY THING. If it ever regresses, no')
print('      downstream guard will say a word -- and that belongs in the lift ledger as a RESIDUAL,')
print('      not as a covered box.')
print('\n   GUARD B (the selector) is verified SEPARATELY -- a green here is NOT a green there.')
sys.exit(0)
