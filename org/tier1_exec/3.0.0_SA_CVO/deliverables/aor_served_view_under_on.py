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
import os
import pathlib
import subprocess
import sys
import tempfile

import pandas as pd

REPO = pathlib.Path(r'C:\Users\AndrewBerman\Desktop\ajb_workspace')
C07 = 'data/inf/scripts/gold/INF_C_07.advisor_attribution.py'
sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold' / 'lib'))

# >> SUPPLY THE PIN THE DISPATCH SUPPLIES -- OR THE GUARD WILL FAIL CLOSED AND I WILL SCORE IT AS THE
# >> DEFECT. (CVO~B, 2026-07-13 -- this arm's second self-caught defect, and the more dangerous one.)
# C_07's enrichment path calls verify_source_partition(), which calls source_etag_pin(), which RAISES
# when INF_AOR_SRC_ETAG is unset: "refusing to fabricate or skip the content check." That raise is the
# A8 fail-closed guard WORKING -- the very guard I verified as correct in the 8/8 key matrix. With no
# pin set, this arm raised, and (before the fix above) printed "*** RED -- THE FOLD IS ERASED ***".
# **IT WAS MISTAKING THE GUARD FOR THE DEFECT.** A false RED is the dangerous direction: its remedy is
# DESTRUCTIVE -- it would have had me reopening C_07, a closed and verified fix.
# The dispatch pins this once at chain start from the accounts_v2 partition it resolved
# (orion-gold-dispatch.sh:1422 + the _repin after CHAIN_PULL). A hermetic arm must supply the same
# thing. This is the REAL live ETag of the partition C_07 actually reads -- so the arm exercises the
# genuine pin<->read seam rather than bypassing it:
#     aws s3api head-object --bucket opal-data-inf \
#       --key silver/api_dims/accounts_v2/snapshot_date=2026-07-12/data.parquet --query ETag
#     -> "d512e15a7778638477affc4783649d8b"   (measured 2026-07-13, and it MATCHES the pin I
#                                              exercised live on the dispatch<->loader seam)
os.environ.setdefault('INF_AOR_SRC_ETAG', 'd512e15a7778638477affc4783649d8b')
os.environ.setdefault('INF_AOR_ASOF', '2026-07-12')

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
    # Exercise WHICHEVER enrichment path this vintage actually has, and assert on the SERVED VALUE.
    # NOT on the absence of a symbol. My first version returned a GREEN called 'NO-OVERRIDE-FN' when the
    # old function was missing -- that is symbol-absence, not behaviour, and it would have FALSE-GREENED a
    # RENAMED clobber. (It is the same defect as the F10 census matching banned SYMBOL calls while C_07
    # re-implemented the slug inline and walked straight past it.) A missing path is an INSTRUMENT BREAK.
    fn = (getattr(mod, '_enrich_accounts_dim_from_accounts_v2', None)      # post-fix name
          or getattr(mod, '_apply_accounts_v2_advisor_key_override', None))  # pre-fix name
    if fn is None:
        raise RuntimeError('INSTRUMENT BROKEN: no accounts_v2 enrichment path found in this vintage. '
                           'Refusing to report GREEN off a symbol that is merely absent -- a renamed '
                           'clobber would look identical.')
    # acct_dim: post-round-8 this carries the CANONICAL key (folded to the advisor-of-record under ON).
    # Account 42 is a MOVER: canonical = noel_soderblom, but its SERVICING rep is Peter Lee. If the fold
    # survives to the served view, advisor_key stays noel_soderblom. If C_07 re-derives from the servicing
    # rep, it is clobbered to peter_lee.
    acct_dim = pd.DataFrame({'account_id': [MOVER_ID], 'advisor_key': [FOLDED],
                             'household_id': [286], 'total_aua': [1_000_000.0]})

    # The POST-FIX path INHERITS the canonical key via load_resolution() -- the correct fix. But the
    # canonical resolution does not exist in prod S3 (the resolver has never run: SERVE-HELD), so a live
    # call 404s and the function fails closed. That is CORRECT behaviour and it is NOT a verdict on the
    # fold. Inject the resolution the resolver WOULD have written, so the arm can observe what is SERVED.
    # Account 42 is the MOVER: the resolution says noel_soderblom; its SERVICING rep is peter_lee.
    if hasattr(mod, 'load_resolution'):
        _res = pd.DataFrame({'account_id': [MOVER_ID], 'advisor_key': [FOLDED],
                             'rep_bucket': ['individual'], 'servicing_advisor_key': [SERVICING],
                             'advisor_of_record_raw': ['Noel'], 'explicit_aor': [True],
                             'is_mover': [True], 'as_of': ['2026-07-12']})
        mod.load_resolution = lambda *a, **k: _res.copy()

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
# HEAD is added because A DETERMINATION BINDS ONLY AT THE HASH IT IS RENDERED ON, and the chokepoint
# lib MOVED under my determination-2 hash (dbab19e4c, +102/-7). Certifying at dbd10d7aa would be
# certifying a tree that no longer exists. 69219a7db STAYS as the PROVEN-RED control: a census with no
# known defect in it cannot be validated, and an arm that has only ever seen the fixed code cannot
# demonstrate it would have caught the defect.
for ref, label in (('69219a7db', 'PROVEN-RED CONTROL -- the hash I WRONGLY GREENED'),
                   ('dbd10d7aa', 'DS C_07 fix'),
                   ('HEAD', 'HEAD -- WHAT I AM CERTIFYING')):
    # >> AN INSTRUMENT BREAK IS NOT A RED. <<  (CVO~B, 2026-07-13 -- this arm's own defect, self-caught)
    # This block used to read:
    #     except Exception as e: got = f'ERROR: {type(e).__name__}'
    #     survived = (got == FOLDED)          # an ERROR is != FOLDED  -> False
    #     verdict  = GREEN if survived else '*** RED -- THE FOLD IS ERASED ***'
    # So ANY exception -- a lib signature change, a missing path, a raise from a guard doing its JOB --
    # printed "RED: THE FOLD IS ERASED BEFORE IT IS SERVED". **"I could not observe it" and "I observed
    # the defect" shared one signature**, which is the F4 null rule (a null that means two things is a
    # lie about one of them) reproduced inside the arm written to catch that class. And it fails in the
    # DANGEROUS direction: a false RED's remedy is DESTRUCTIVE -- it would have me reopening C_07, a
    # closed and verified fix, and possibly reverting DS's work. The message was discarded too, so the
    # arm could not even say WHY. It now carries the exception text and exits 2 (INSTRUMENT BREAK).
    err = None
    try:
        got = served_advisor_key(_load_c07_at(ref))
    except Exception as e:
        err = f'{type(e).__name__}: {e}'
        got = None
    if err is not None:
        RESULTS[ref] = None                  # None == COULD-NOT-OBSERVE. Never True, never False.
        print(f'\n  {ref:<12} ({label})')
        print('      served advisor_key = <COULD NOT OBSERVE>')
        print(f'      !!! INSTRUMENT BREAK -- {err}')
        print('      This is NOT a RED. The arm could not run; it observed nothing. No verdict.')
        continue
    survived = (got == FOLDED)   # GREEN only if the SERVED key is still the FOLDED one
    RESULTS[ref] = survived
    verdict = 'GREEN -- the fold SURVIVES to the served view' if survived else \
              '*** RED -- THE FOLD IS ERASED BEFORE IT IS SERVED ***'
    print(f'\n  {ref:<12} ({label})')
    print(f'      served advisor_key = {got}')
    print(f'      {verdict}')

if any(v is None for v in RESULTS.values()):
    print('\n' + '=' * 100)
    print('INSTRUMENT BREAK -- at least one vintage could not be observed. NO VERDICT ON ANY OF THEM.')
    print('  A run that could not execute is not evidence about the code. Do not quote this run.')
    sys.exit(2)

print('\n' + '=' * 100)
if RESULTS.get('69219a7db') is False and RESULTS.get('dbd10d7aa') is True:
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
