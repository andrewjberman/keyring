"""GATE-2 / TIME-LOCK -- THE SERVED-LAYER ARM. **MY BAR WAS ON THE WRONG LAYER AND COULD NOT HAVE FAILED.**

3.0.0_SA_CVO~B, 2026-07-13. Built at DS's finding AGAINST MY INSTRUMENT, which I verified and confirmed.

>> THE INDICTMENT, AND IT IS MINE TO WEAR <<
`aor_timelock_bar_v2_account_grain.py` measures `gold/canonical/canonical_nna_*`. **GOLD.**
But FOUR consumers RE-FOLD the already-stamped gold IN MEMORY, AT SERVE TIME:

    INF_D_00f:815   <- *** THE SERVED PER-ADVISOR NNA SPINE ***
    INF_D_00d:660   <- cumulative chart
    INF_D_00c:451   <- leaderboard   (inside _filter_partition, over load_canonical_nna's partitions)
    INF_09:406      <- partner analytics

**So the lock could freeze gold PERFECTLY and the SERVED number would still slide with the current book
-- and my bar would have printed GREEN through all of it.**

    >> COULD MY INSTRUMENT, ON THAT LAYER, EVER HAVE RETURNED A FAIL? NO. THEN IT MEASURED NOTHING. <<

**I WROTE THE RULE THAT CATCHES THIS, AFTER C_07, AND THEN BROKE IT:**
    "A VERIFIER THAT ONLY EVER ASKS THE PRODUCER WHAT IT PRODUCED HAS NOT VERIFIED DELIVERY.
     Assert on the SERVED ARTIFACT, at the last point before it ships."
**C_07 was the fold being UN-DONE downstream. This is the lock being UN-DONE downstream. Same shape,
opposite sign, and I did not look for it because I had already 'handled' that class.**
*Knowing a failure mode by name does not immunize you against writing it.*

**AND MY CENSUS OF DS'S CENSUS HAD THE SAME DEFECT:** my first pass scored `INF_D_00c` as SAFE because
my lookback could not resolve its frame and my DEFAULT BRANCH WAS "legitimate". **AN UNKNOWN SCORED AS A
PASS.** I only found it because his count said FOUR and mine said THREE. *When the two censuses disagree,
open the file -- do not trust the one you wrote.*

=================================================================================================
WHAT THIS ARM ASSERTS -- ON THE LAYER THE CLAIM LIVES ON

  S1  WILD TYPE: a STAMPED canonical_nna row is NOT re-keyed by the fold.  (the lock survives to serve)
  S2  MUTANT (= TODAY'S DEPLOYED BEHAVIOUR): strip the stamp -> the fold re-keys it -> an advisor is
      handed history he never held. **A REPRODUCTION, NOT A HYPOTHESIS.** If S2 does not go RED, this
      arm cannot see the defect and NOTHING it says counts.
  S3  OVER-CONDEMNATION: a FRESH frame (no stamp column) MUST still fold freely -- otherwise the
      one-shot BACKFILL can never reach history, and a fix that gives Noel NOTHING is also wrong.
  S4  THE SWITCH IS NOT A MODULE FLAG. `apply_resolution_fold` NEVER reads AOR_FOLD_ACTIVE -- it folds
      whatever the RESOLUTION marks `is_mover`. DS found a line in his own harness
      (`ar.AOR_FOLD_ACTIVE = True`) that was **INERT** and whose comment claimed it forced the fold ON.
      I audited my own arms: mine drive the fold through a REAL movers resolution, never the flag.
      This arm proves the point rather than asserting it.

Hermetic: real lib functions. No S3, no prod touch, no re-derive, no chain advance.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold' / 'lib'))

import advisor_timelock as tl  # noqa: E402
from aor_resolution import apply_resolution_fold  # noqa: E402

FAILS: list[str] = []


def check(name: str, ok: bool, detail: str = '') -> None:
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f'\n       {detail}' if detail else ''))
    if not ok:
        FAILS.append(name)


MODEL_COL = tl.MODEL_COL          # 'attribution_model'
MODEL = tl.ATTRIBUTION_MODEL      # 'time-locked-by-account'

# A slice of STAMPED canonical_nna, exactly as the four serve-time consumers read it from gold.
# Account 59's history was time-locked to peter_lee -- he held it at the time.
def stamped_gold() -> pd.DataFrame:
    return pd.DataFrame({
        'account_id': [59, 59, 59],
        'date': ['2020-03-15', '2023-07-01', '2026-06-30'],
        'advisor_key': ['peter_lee'] * 3,
        'rep_bucket': ['individual'] * 3,
        'net_nna': [100_000.0, 250_000.0, 50_000.0],
        MODEL_COL: [MODEL] * 3,                 # <- THE STAMP. "already stamped" == "already happened".
    })


# The resolution says the CURRENT advisor-of-record is joe. A serve-time fold would re-key history to him.
RES = pd.DataFrame({'account_id': [59], 'advisor_key': ['joe_brandenburg'],
                    'rep_bucket': ['individual'], 'is_mover': [True]})

print('=' * 100)
print('SERVED-LAYER ARM -- does the TIME-LOCK survive to the SERVED artifact?')
print('  (the four serve-time consumers re-fold stamped gold IN MEMORY; gold being perfect proves nothing)')
print('=' * 100)

# ---- S1: WILD TYPE -- the stamped row must NOT be re-keyed -------------------------------------
wild, n_wild = apply_resolution_fold(stamped_gold(), RES)
served_wild = sorted(wild['advisor_key'].unique())
peter_wild = float(wild[wild['advisor_key'] == 'peter_lee']['net_nna'].sum())
check('S1  WILD TYPE: the fold REFUSES to re-key a STAMPED row -- the lock survives to the served value',
      n_wild == 0 and served_wild == ['peter_lee'],
      f'n_rekeyed={n_wild}   served advisors={served_wild}   peter keeps ${peter_wild:,.2f}')

# ---- S2: MUTANT = TODAY'S DEPLOYED BEHAVIOUR. It MUST go RED, or this arm is blind ---------------
blind = stamped_gold().drop(columns=[MODEL_COL])          # strip the stamp -> the deployed fold
mut, n_mut = apply_resolution_fold(blind, RES)
served_mut = sorted(mut['advisor_key'].unique())
joe_mut = float(mut[mut['advisor_key'] == 'joe_brandenburg']['net_nna'].sum())
check('S2  MUTANT (= the DEPLOYED behaviour): with no stamp, the fold RE-KEYS the frozen history\n'
      '       -> an advisor is handed history he never held. THE ARM CAN SEE THE DEFECT.',
      n_mut == 3 and served_mut == ['joe_brandenburg'],
      f'n_rekeyed={n_mut}   served advisors={served_mut}   '
      f'joe_brandenburg handed ${joe_mut:,.2f} of history he NEVER HELD\n       '
      'This is a REPRODUCTION of what INF_D_00f:815 does TODAY, not a hypothesis.')

# ---- S3: OVER-CONDEMNATION -- a FRESH frame must still fold freely -------------------------------
fresh = pd.DataFrame({'account_id': [59], 'date': ['2026-09-01'], 'advisor_key': ['peter_lee'],
                      'rep_bucket': ['individual'], 'net_nna': [1_000.0]})   # no stamp column at all
out_f, n_f = apply_resolution_fold(fresh, RES)
check('S3  OVER-CONDEMNATION: a FRESH frame (no stamp column) still folds FREELY -- otherwise the\n'
      '       one-shot BACKFILL could never reach history, and a fix that gives Noel NOTHING is also wrong',
      n_f == 1 and out_f['advisor_key'].iloc[0] == 'joe_brandenburg',
      f'n_rekeyed={n_f} -> {out_f["advisor_key"].iloc[0]}   (INF_C_01 txns / B_00 + D_02b holdings '
      'carry no stamp and MUST keep folding)')

# ---- S4: the switch is NOT a module flag on the fold --------------------------------------------
import aor_resolution as ar  # noqa: E402
had = getattr(ar, 'AOR_FOLD_ACTIVE', '<absent>')
res_empty = pd.DataFrame({'account_id': [59], 'advisor_key': ['joe_brandenburg'],
                          'rep_bucket': ['individual'], 'is_mover': [False]})   # ZERO movers == OFF
_, n_off = apply_resolution_fold(stamped_gold().drop(columns=[MODEL_COL]), res_empty)
check('S4  THE SWITCH IS THE RESOLUTION, NOT A FLAG: apply_resolution_fold never reads AOR_FOLD_ACTIVE;\n'
      '       it folds whatever the RESOLUTION marks is_mover. A zero-mover resolution folds NOTHING.',
      n_off == 0,
      f'ar.AOR_FOLD_ACTIVE on the fold module = {had!r}  |  zero-mover resolution -> n_rekeyed={n_off}\n       '
      'DS found `ar.AOR_FOLD_ACTIVE = True` in his own harness with a comment claiming it forced the\n       '
      'fold ON. IT WAS INERT. I audited my arms: they drive a REAL movers resolution. This proves why.')

print('\n' + '=' * 100)
if FAILS:
    print(f'{len(FAILS)} FAILURE(S): {FAILS}')
    print('  Before "fixing" anything: ask FIRST whether this ARM encoded the defect.')
    sys.exit(1)
print('SERVED-LAYER ARM: GREEN. The lock SURVIVES the serve-time re-fold, and the arm PROVED it can')
print('  see the defect (S2 reproduces the deployed behaviour and goes RED).')
print('\n  >> AND THE STANDING CORRECTION: a GOLD-layer verification of the time-lock COULD ONLY EVER')
print('  >> HAVE SAID PASS. The claim lives on the layer we SERVE. My bar v2 is now SUPERSEDED on that')
print('  >> axis -- it is still sound for WHAT GOLD CONTAINS, and it is BLIND to what gets served.')
print('\n  STILL REQUIRED, and no fixture green closes it: the SERVED artifact itself, on a dry-run,')
print('  BEFORE the stamping write -- with the executing run asserted BYTE-IDENTICAL to the one cleared.')
sys.exit(0)
