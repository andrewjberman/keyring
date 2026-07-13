"""GATE / TIME-LOCK -- THE PROPERTY AND THE PROVENANCE, ATTACKED.

3.0.0_SA_CVO~B, 2026-07-13. DS asked to be attacked, not trusted. COO's two rulings were BOTH corrected
by DS against himself, and my arms must test the CORRECTED shapes -- **the PROPERTY, never the named
instance, and the ROW, never the RUN.**

=================================================================================================
P1  THE CLASS, NOT THE NAMED INSTANCE.
    COO ruled: "an unstamped OLD row takes the FIRST-OBSERVED AoR."
    >> THAT IS CORRECT **ONLY WHILE EXACTLY ONE OBSERVATION EXISTS.** The moment a SECOND lands, a
       late-arriving row dated AFTER that change must take the **NEW** advisor -- and a first-observed
       rule hands it to the OLD one, SILENTLY, FOREVER, UNDER A STAMP. <<
    The ruling named the shape the ruler happened to see. The defect does not know that.
    ARM: build a SECOND observation and prove the first-observed rule would have been WRONG.

P2  ...AND IT MUST STILL COLLAPSE TO THE RULING WHERE THE RULING'S PREMISE HOLDS (n=1).
    A property that breaks the ruling's own case is not a generalisation, it is a replacement.

P3  PROVENANCE IS KEYED ON THE **ROW**, NOT THE **RUN**.
    COO ruled: "stamped during the one-shot -> BACKFILLED; stamped on a later nightly -> OBSERVED."
    >> THE FALSIFIER IS THE P1 GUARD ITSELF: the late-arriving 2019 row -- **THE EXACT ROW THAT GUARD
       EXISTS TO CATCH** -- is stamped on a LATER NIGHTLY. A run-keyed flag would label it `observed`.
       **IT WOULD LAUNDER THE PRESUMPTION AS A FACT, ON THE ONE ROW WE BUILT A GUARD FOR.** <<
    A RUN IS A PROXY FOR THE ROW'S DATE, AND A PROXY IS WHAT KEEPS CATCHING US.

P4  THE FAIL-DIRECTION. When the basis cannot be established, it must fail toward BACKFILLED.
    **OVER-CLAIMING `observed` IS THE DIRECTION THAT LIES.** A presumption mislabelled a fact is
    frozen under the stamp and can never be found again; a fact mislabelled a presumption is merely
    conservative. Assert the ASYMMETRY, not just the value.

Hermetic: real lib functions. No S3, no prod touch, no chain advance.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold' / 'lib'))

import advisor_timelock as tl  # noqa: E402

FAILS: list[str] = []


def check(name: str, ok: bool, detail: str = '') -> None:
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f'\n       {detail}' if detail else ''))
    if not ok:
        FAILS.append(name)


print('=' * 100)
print('THE PROPERTY AND THE PROVENANCE -- attacked, not trusted')
print('=' * 100)

# ---- P1: TWO observations. The first-observed rule breaks; the PROPERTY holds. -------------------
# acct 59: first seen as noel (2026-07-10). Then a SECOND observation: it moves to joe (2026-09-01).
TWO = [('2026-07-10', 'noel_soderblom'), ('2026-09-01', 'joe_brandenburg')]

late_2019 = tl.aor_in_effect_at(TWO, '2019-05-01')      # predates EVERY observation -> backward extend
late_aug = tl.aor_in_effect_at(TWO, '2026-08-15')       # between obs 1 and 2 -> noel
late_oct = tl.aor_in_effect_at(TWO, '2026-10-15')       # AFTER obs 2 -> MUST be joe

first_observed = TWO[0][1]                               # what COO's rule would have handed EVERY row
print('\n  observations for acct 59:', TWO)
print(f"    a 2019 row  -> {late_2019!r}   (backward extension of the FIRST observation)")
print(f"    a 2026-08 row -> {late_aug!r}   (most recent observation at-or-before)")
print(f"    a 2026-10 row -> {late_oct!r}   <- COO's rule would have said {first_observed!r}")

check('P1  THE CLASS: a late row dated AFTER a SECOND observation takes the NEW advisor.\n'
      "       COO's 'first-observed' rule would have handed it to the OLD one -- silently, forever,\n"
      '       under a stamp. The ruling named the shape the ruler happened to see.',
      late_oct == 'joe_brandenburg' and late_oct != first_observed,
      f'property -> {late_oct!r}   first-observed rule -> {first_observed!r}   THEY DISAGREE, and the '
      f'property is right.')

check('P2  ...AND IT COLLAPSES TO THE RULING WHERE THE RULING HOLDS (exactly ONE observation)',
      tl.aor_in_effect_at([('2026-07-10', 'noel_soderblom')], '2019-05-01') == 'noel_soderblom',
      'n=1: a 2019 row takes the first-observed AoR -- the backward extension IS the backfill. '
      'A property that broke the ruling\'s own case would be a replacement, not a generalisation.')

# ---- P3: provenance keyed on the ROW, not the RUN ------------------------------------------------
OBS = {59: TWO}
df = pd.DataFrame({
    'account_id': [59, 59, 59],
    'date': ['2019-05-01', '2026-08-15', '2026-10-15'],
    'advisor_key': ['noel_soderblom', 'noel_soderblom', 'joe_brandenburg'],
})
out = tl.stamp_attribution_basis(df.copy(), OBS, log=lambda *a: None)
out = out[0] if isinstance(out, tuple) else out
basis = dict(zip(out['date'], out[tl.BASIS_COL]))
print(f"\n  attribution_basis by row date: {basis}")

check('P3  PROVENANCE IS KEYED ON THE ROW: the 2019 row is BACKFILLED (a PRESUMPTION) -- even though\n'
      '       it would be stamped on a LATER NIGHTLY, which a RUN-keyed flag would have called `observed`.\n'
      '       >> IT WOULD HAVE LAUNDERED THE PRESUMPTION AS A FACT, ON THE ONE ROW THE GUARD EXISTS FOR. <<',
      basis['2019-05-01'] == tl.BASIS_BACKFILLED,
      f"2019-05-01 -> {basis['2019-05-01']!r}  (predates the first observation 2026-07-10 -> a PRESUMPTION)")

check('P3b ...and a row dated AFTER the first observation is OBSERVED -- a FACT. The two rules disagree\n'
      '       in BOTH directions, which is why the ROW is the unit and the RUN is a proxy.',
      basis['2026-08-15'] == tl.BASIS_OBSERVED and basis['2026-10-15'] == tl.BASIS_OBSERVED,
      f"2026-08-15 -> {basis['2026-08-15']!r}   2026-10-15 -> {basis['2026-10-15']!r}")

# ---- P4: THE FAIL-DIRECTION -- when the basis cannot be established, it must say BACKFILLED -------
none_df = pd.DataFrame({'account_id': [999], 'date': ['2024-01-01'], 'advisor_key': ['peter_lee']})
out2 = tl.stamp_attribution_basis(none_df.copy(), {}, log=lambda *a: None)   # NO observations at all
out2 = out2[0] if isinstance(out2, tuple) else out2
got = out2[tl.BASIS_COL].iloc[0]
check('P4  THE FAIL-DIRECTION: with NO observation at all, the basis fails toward BACKFILLED.\n'
      '       >> OVER-CLAIMING `observed` IS THE DIRECTION THAT LIES. A presumption mislabelled a FACT is\n'
      '       >> frozen under the stamp and can NEVER be found again; a fact mislabelled a presumption is\n'
      '       >> merely conservative. The ASYMMETRY is the property, not the value. <<',
      got == tl.BASIS_BACKFILLED,
      f'no observations -> {got!r}   (never `observed`, never null)')

print('\n' + '=' * 100)
if FAILS:
    print(f'{len(FAILS)} FAILURE(S): {FAILS}')
    print('  Before "fixing" anything: ask FIRST whether this ARM encoded the defect.')
    sys.exit(1)
print('GREEN. The PROPERTY holds (not the named instance), and the PROVENANCE is keyed on the ROW')
print('  (not the RUN) and fails toward BACKFILLED.')
print('\n  >> RESIDUAL, AND DS NAMED IT AGAINST HIMSELF RATHER THAN BURYING IT: <<')
print('  THE LEDGER RECORDS *WHEN WE NOTICED*, NOT *WHEN IT HAPPENED*. A resolver that is down for days')
print('  and then catches up stamps TODAY as the effective-from for a change that already happened.')
print('  That hazard is REAL, it is NOT closed by this code, and it is closed only by running the')
print('  resolver EVERY NIGHT. It is disclosed, not fixed -- and under Andrew\'s ruling it is exactly')
print('  right for the BACKFILL ("the first AVAILABLE AoR" IS "the first one we noticed"), and exactly')
print('  wrong after a CATCH-UP. That distinction is the whole residual.')
sys.exit(0)
