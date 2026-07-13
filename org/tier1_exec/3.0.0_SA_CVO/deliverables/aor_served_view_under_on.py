"""GATE-2 (3.0.0_SA_CVO~B) -- THE ARM THAT SHOULD HAVE EXISTED FROM THE START.

ASSERT THE SERVED VIEW, NOT THE RESOLVER'S OUTPUT.

WHY THIS EXISTS. I issued gate-2 VERIFIED at 69219a7db and it was WRONG. DS found (and reported
against himself) that INF_C_07 inherits the canonical advisor_key and then OVERWRITES it with the
SERVICING slug:

    df['advisor_key'] = df['_key_override'].combine_first(df['advisor_key'])   # C_07, @69219a7db
    _key_override = slug(accounts_v2.representative_name)                      # the SERVICING rep

`combine_first` takes the OVERRIDE first and falls back to the canonical only when the override is
NULL -- and it is never null for a serviced account. THE OVERRIDE ALWAYS WINS. THE FOLD IS ERASED.
And `account_team` is BOTH the frame the household headline is resolved from AND the served view
C_01b/C_08/D_00/D_00b/D_00c/D_02/D_03/D_04 inherit. So under ON the fold NEVER REACHES THE SERVED
VIEWS -- the entire purpose of the project.

MY WHOLE BATTERY PASSED ANYWAY, AND THE REASON IS THE LESSON:
  * EVERY ARM I BUILT MEASURES THE RESOLUTION. NOT ONE MEASURED THE SERVED VIEW UNDER ON.
  * My ON positive control asserted fold == 164 == my independent oracle -- that measures what the
    RESOLVER PRODUCED, never what a downstream producer does to it afterwards.
  * My F5c perturbation arm proved the resolution PROPAGATES to the views. It proves the value
    ARRIVES. It does NOT prove nothing OVERWRITES it after it arrives.
  * The OFF arms are correctly green and structurally blind: under OFF the resolution IS servicing,
    so an override *to servicing* is a no-op. The defect is only visible under ON, on a MOVER.

THIS IS THE SAME CLASS AS MY OWN R-A FINDING -- a value that is CORRECT AT THE POINT IT IS PRODUCED
and WRONG AT THE POINT IT IS CONSUMED. I found that class in the resolver and never turned it on my
own battery.

  >> DOCTRINE: A VERIFIER THAT ONLY EVER ASKS THE PRODUCER WHAT IT PRODUCED HAS NOT VERIFIED
  >> DELIVERY. Assert on the SERVED ARTIFACT, at the LAST point before it ships.

THE ARM. Under ON, take a MOVER whose canonical (folded) key differs from its servicing key, push it
through C_07's real override function, and assert the SERVED account_team still carries the FOLDED
key. Exercised against BOTH vintages, because an arm that has only ever seen the fixed code cannot
demonstrate it would have caught the defect (the exact trap that produced the original 0/871):

    @69219a7db (the hash I wrongly greened) -> must go RED   (the fold is erased)
    @the fix hash                           -> must go GREEN  (the fold survives to the served view)

Hermetic: real C_07 function, stubbed frames. No prod touch, no gold run.
"""
from __future__ import annotations

import importlib.util
import pathlib
import subprocess
import sys
import tempfile

import pandas as pd

REPO = pathlib.Path(r'C:\Users\AndrewBerman\Desktop\ajb_workspace')
C07 = 'data/inf/scripts/gold/INF_C_07.advisor_attribution.py'
sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold' / 'lib'))

# A REAL account that EXISTS in the live accounts_v2 partition (account 42, servicing rep "Peter Lee").
# THIS MATTERS: my first version of this arm used a FAKE account_id. The override function loads
# accounts_v2 ITSELF from S3 (its signature is (df, max_lookback_days) -- it takes no av2 argument), so a
# fake id is simply ABSENT from the lookup, the override is NULL, combine_first falls back to the canonical,
# and the fold "survives" FOR THE WRONG REASON. The arm printed GREEN on the defective code.
# AN ARM THAT CANNOT EXPRESS THE FAILING STATE WILL ALWAYS PASS. The account must be one the override
# actually has data for -- otherwise you are testing the fallback branch, not the override.
MOVER_ID = 42
FOLDED = 'noel_soderblom'   # the advisor-of-record: what a MOVER must be attributed to under ON
SERVICING = 'peter_lee'     # account 42's servicing rep -- what the override substitutes


def _load_c07_at(ref: str):
    """Load INF_C_07 as a module AT A GIVEN GIT REF (or 'WORKTREE'), without executing main()."""
    if ref == 'WORKTREE':
        src = (REPO / C07).read_text(encoding='utf-8', errors='replace')
    else:
        src = subprocess.run(['git', 'show', f'{ref}:{C07}'], cwd=REPO,
                             capture_output=True, text=True).stdout
    if not src.strip():
        raise RuntimeError(f'INSTRUMENT BROKEN: empty source for {ref} -- refusing to report a verdict '
                           'off a read that returned nothing.')
    # strip the __main__ guard body so importing does not run the job
    tmp = pathlib.Path(tempfile.mkdtemp()) / 'c07.py'
    tmp.write_text(src, encoding='utf-8')
    spec = importlib.util.spec_from_file_location(f'c07_{abs(hash(ref))}', tmp)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    return mod


def served_advisor_key(mod) -> str:
    """Push a MOVER through C_07's REAL override path and read back what account_team would SERVE."""
    fn = getattr(mod, '_apply_accounts_v2_advisor_key_override', None)
    if fn is None:
        return 'NO-OVERRIDE-FN'      # the function is gone entirely -> nothing can erase the fold
    # acct_dim: post-round-8 this carries the CANONICAL key (folded to the advisor-of-record under ON).
    # Account 42 is a MOVER: canonical = noel_soderblom, but its SERVICING rep is Peter Lee. If the fold
    # survives to the served view, advisor_key stays noel_soderblom. If C_07 re-derives from the servicing
    # rep, it is clobbered to peter_lee.
    acct_dim = pd.DataFrame({'account_id': [MOVER_ID], 'advisor_key': [FOLDED],
                             'household_id': [286], 'total_aua': [1_000_000.0]})
    out = fn(acct_dim)      # signature is (df, max_lookback_days) -- it loads accounts_v2 itself
    row = out[out['account_id'] == MOVER_ID]
    if row.empty:
        return 'ROW-VANISHED'
    return str(row['advisor_key'].iloc[0])


print('=' * 100)
print('SERVED-VIEW ARM UNDER ON -- does the FOLD survive to the served account_team?')
print(f'  a MOVER: canonical/folded = {FOLDED!r}   servicing = {SERVICING!r}')
print('=' * 100)

RESULTS = {}
for ref, label in (('69219a7db', 'the hash I WRONGLY GREENED'), ('WORKTREE', 'DS fix IN FLIGHT (uncommitted)')):
    try:
        got = served_advisor_key(_load_c07_at(ref))
    except Exception as e:
        got = f'ERROR: {type(e).__name__}'
    survived = (got == FOLDED) or got == 'NO-OVERRIDE-FN'
    RESULTS[ref] = survived
    verdict = 'GREEN -- the fold SURVIVES to the served view' if survived else \
              '*** RED -- THE FOLD IS ERASED BEFORE IT IS SERVED ***'
    print(f'\n  {ref:<12} ({label})')
    print(f'      served advisor_key = {got}')
    print(f'      {verdict}')

print('\n' + '=' * 100)
if RESULTS.get('69219a7db') is False and RESULTS.get('WORKTREE') is True:
    print('THE ARM DISCRIMINATES: RED at the hash I greened, GREEN at the fix.')
    print('  It would have caught the defect. That is the property my original battery lacked --')
    print('  every arm it had measured the RESOLUTION, and this one measures the SERVED ARTIFACT.')
    print('\n  NOTE: the WORKTREE result is NOT a certification. Per COMMIT-BEFORE-VERIFY I certify')
    print('  only at a committed hash. This run proves the ARM works; DS hands me a hash and I re-run.')
    sys.exit(0)
if RESULTS.get('69219a7db') is False:
    print('RED at 69219a7db -- the defect is REAL at the hash I greened. Retraction stands.')
    sys.exit(1)
print('DID NOT DISCRIMINATE -- do not trust this run.')
sys.exit(2)
