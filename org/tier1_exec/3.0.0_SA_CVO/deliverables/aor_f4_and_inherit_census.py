"""GATE-2 (3.0.0_SA_CVO~B) -- F4 arms + the F2 inherit-mode CENSUS. Run both at any hash.

Two instruments, one file, because they answer the two questions still open on round-8.2.

=====================================================================================
PART 1 -- F4: the guard covers the branch that almost never fires and misses the one
that does.
=====================================================================================
The four states INF_C_02 can actually hand household_headline_map:

  None  (account_team READ FAILED -- C_02's own WARN path) -> {} SILENTLY   FAIL-OPEN
  EMPTY frame (0 rows)                                     -> {} SILENTLY   FAIL-OPEN
  STALE frame (readable, missing the stamped column)       -> RAISES        (correct)
  HEALTHY (C_07 stamped) -- POSITIVE CONTROL               -> the map       (non-placebo)

A STALE DEPLOY -- rare, and it announces itself -- fails CLOSED and LOUD.
A TRANSIENT S3 READ BLIP -- common, invisible -- fails OPEN and SILENT.

Mechanism: aor_resolution :588-589 `if account_team is None or len(...)==0: return {}`, and
INF_C_02 :468-471 catches the read error, sets `_acct_team = None`, then calls the map OUTSIDE
the try. THE TRY/EXCEPT DOES NOT PROTECT -- IT CONVERTS A LOUD READ FAILURE INTO A SILENT
WRONG-SERVE. Under ON: households keep the pre-fold groupby-first advisor WHILE ACCOUNTS ARE
FOLDED -- accounts say noel, households say peter. The per-view divergence the SSOT exists to
eliminate, coming back through an ERROR path (which no census test and no ledger-diff detector
can see).

=====================================================================================
PART 2 -- the F2 inherit-mode CENSUS: classify by FUNCTION, never by MENTION.
=====================================================================================
CTO's F2 blast selected consumers carrying "ZERO INF_AOR_ASOF references" and named six. It was
wrong in BOTH directions, and this census is why:

  * The six are NOT exposed. They inherit via `apply_resolution_fold` (MOVERS-ONLY), which leaves
    an account absent from the resolution holding its SERVICING key -- that is DELTA-0, the whole
    point of the mode. Exercised below: NaN count 0. The NaN/<NA>-rep_bucket severity that makes
    F2 a ship-blocker never reaches them.
  * INF_A_01 IS exposed -- full-attach, no `absent=` floor, loads accounts_v2 itself -- and it was
    FILTERED OUT of the blast because it carries ONE pin reference. That reference (INF_A_01:175)
    IS A COMMENT. The script does not read the pin; it talks about it.

WHEN YOU MEASURE WITH GREP, PROSE COUNTS AS CODE. Census by FUNCTION ("which mode does it inherit
by? does it READ the value?"), never by mention. (My own first census had the same bug in another
form: a shell integer comparison silently failed and DEFAULTED 8 scripts to 'movers-only' -- a
default, not a measurement. Caught on the denominator. Put the control on the retrieval.)

Hermetic: real lib, no prod touch, no gold run.
"""
from __future__ import annotations

import pathlib
import re
import sys

import pandas as pd

REPO = pathlib.Path(r'C:\Users\AndrewBerman\Desktop\ajb_workspace')
GOLD = REPO / 'data' / 'inf' / 'scripts' / 'gold'
sys.path.insert(0, str(GOLD / 'lib'))

from aor_resolution import apply_resolution_fold, household_headline_map  # noqa: E402

FAIL = 0

# ---------------------------------------------------------------- PART 1: F4
print('=' * 100)
print('F4 -- the four states INF_C_02 can hand household_headline_map')
print('=' * 100)

HEALTHY = pd.DataFrame({'household_id': [286], 'advisor_key': ['peter_lee'],
                        'household_headline_advisor_key': ['noel_soderblom']})
STALE = pd.DataFrame({'household_id': [286], 'advisor_key': ['peter_lee']})
EMPTY = pd.DataFrame({'household_id': [], 'household_headline_advisor_key': []})

F4_ARMS = [
    ('None  (account_team READ FAILED -- C_02 WARN path)', None, True),
    ('EMPTY frame (0 rows) -- caller DECLARED non-empty', EMPTY, True),  # F4-B: declared -> must RAISE
    ('STALE frame (missing stamped col)', STALE, True),
    ('HEALTHY (C_07 stamped) -- POSITIVE CONTROL', HEALTHY, False),
]
for name, frame, should_raise in F4_ARMS:
    try:
        # F4-B (CTO~B): expect_nonempty is now a REQUIRED positional -- THE CALLER DECLARES
        # whether zero households is legitimate. INF cannot have zero (~286 across 4 advisors),
        # so every INF caller declares True, and a 0-row read is therefore UNOBSERVABLE-shaped
        # and must RAISE. (Omitting the arg made EVERY arm raise on a TypeError -- including the
        # HEALTHY control. The control caught my stale fixture, not the code.)
        got = household_headline_map(frame, expect_nonempty=True)
        result, raised = (f'RETURNED {got if got else "{} (EMPTY -- SILENT)"}', False)
    except Exception:
        result, raised = ('RAISED (fail-closed)', True)
    ok = raised == should_raise
    if name.startswith('None') and not raised:
        FAIL += 1
        tag = '*** FAIL-OPEN: an UNREADABLE account_team is not an EMPTY one ***'
    elif name.startswith('HEALTHY') and raised:
        FAIL += 1
        tag = '*** PLACEBO: the control raised -- the INSTRUMENT is wrong, not the code ***'
    else:
        tag = 'ok' if ok else 'note'
    print(f'  {name:<52} -> {result:<34} {tag}')

# ---------------------------------------------------------------- PART 2: census
print('\n' + '=' * 100)
print('F2 CENSUS -- inherit mode by FUNCTION (denominator = 10)')
print('=' * 100)
CONSUMERS = ['INF_A_00.accounts_dimension', 'INF_A_01.advisor_assignments',
             'INF_B_00.canonical_holdings', 'INF_C_01.canonical_nna',
             'INF_C_07.advisor_attribution', 'INF_09.generate_partner_analytics',
             'INF_D_00c.portal_leaderboard', 'INF_D_00d.cumulative_chart',
             'INF_D_00f.advisor_nna_canonical', 'INF_D_02b.top_holdings']
full = []
for f in CONSUMERS:
    src = (GOLD / f'{f}.py').read_text(encoding='utf-8', errors='replace')
    n_attach = len(re.findall(r'attach_advisor_key\(', src))
    n_fold = len(re.findall(r'apply_resolution_fold\(', src))
    # MENTIONS of the pin (prose included) vs a FUNCTIONAL read of it
    n_mention = len(re.findall(r'INF_AOR_ASOF', src))
    n_read = len(re.findall(r"environ(?:\.get)?[\[(]\s*['\"]INF_AOR_ASOF", src))
    if n_attach:
        full.append(f)
        mode = f'FULL-ATTACH (x{n_attach})  <== NaN RISK'
    elif n_fold:
        mode = f'movers-only  (x{n_fold})'
    else:
        mode = 'load_resolution only'
    print(f'  {f:<34} {mode:<36} pin: mentions={n_mention} READS={n_read}')

print(f'\n  FULL-ATTACH (the NaN / <NA>-rep_bucket / silent-row-loss class): {len(full)} of 10')
for f in full:
    print(f'      {f}')

print('\n  DECISIVE -- does MOVERS-ONLY NaN an account absent from the resolution?')
df = pd.DataFrame({'account_id': [1, 4], 'advisor_key': ['peter_lee', 'patrick_scanlan'],
                   'rep_bucket': ['individual'] * 2})
res = pd.DataFrame({'account_id': [1], 'advisor_key': ['noel_soderblom'], 'rep_bucket': ['individual'],
                    'servicing_advisor_key': ['peter_lee'], 'is_mover': [True]})
out, n = apply_resolution_fold(df, res)
n_nan = int(out['advisor_key'].isna().sum()) + int(out['rep_bucket'].isna().sum())
print(f'      account 4 (ABSENT from the resolution) -> advisor_key='
      f'{out.loc[out.account_id == 4, "advisor_key"].iloc[0]!r}, NaN count = {n_nan}')
if n_nan == 0:
    print('      => movers-only KEEPS the servicing key. DELTA-0. The F2 severity does NOT reach these 7.')
else:
    FAIL += 1
    print('      => *** movers-only DOES NaN -- F2 is systemic ***')

print('\n' + '=' * 100)
print(f'{"FAILURES: " + str(FAIL) if FAIL else "all arms behaved as characterized"}')
sys.exit(1 if FAIL else 0)
