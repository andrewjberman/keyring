"""TIME-LOCK NNA -- BAR v2, ACCOUNT GRAIN. AMENDED IN THE OPEN, AT DS'S FINDING AGAINST MY OWN BAR.

3.0.0_SA_CVO~B, 2026-07-13.

>> WHY v1 IS SUPERSEDED: **DS RAN MY BAR INSTEAD OF TRUSTING IT AND FOUND A BLIND SPOT WHERE THE
>> CONTESTED MONEY LIVES.** I verified his finding independently and HE IS RIGHT.

v1's `closed_windows()` compared only windows whose (start,end) bounds are IDENTICAL in both artifacts.
That bounds-matching is CORRECT -- it is what stops the shifting quarter labels from comparing different
date ranges. But its CONSEQUENCE is that v1 gated on exactly TWO windows:

    oracle[q1] == live[q2]    2026-01-01 .. 2026-03-31    (Q1-2026)
    oracle[q2] == live[q3]    2025-10-01 .. 2025-12-31    (Q4-2025)

**Q2-2026 (Apr-Jun) IS NOT COMPARABLE AND WAS THEREFORE NEVER CHECKED:**
    oracle QTD/q_current : 2026-04-01 .. 2026-06-29   <- TRUNCATED at the ORACLE'S OWN as_of
    live   q1            : 2026-04-01 .. 2026-06-30   <- the FULL closed quarter
    bounds differ by ONE DAY -> dropped from the comparison entirely.

**AND THAT IS EXACTLY THE QUARTER THE CONTESTED MONEY SITS IN:**
    4273  $705,895.51   flows 2026-05-21 .. 2026-06-30   -> Q2-2026
    4156  $  3,512.28   flow  2026-04-15                 -> Q2-2026
    -----------------
          $709,407.79   INVISIBLE TO v1'S T1 UNDER **EITHER** BRANCH OF THE FORK.

So v1 would have gone GREEN on the ruled predicate AND on the overruled one. **It could not tell them
apart. It was fork-BLIND, not fork-NEUTRAL** -- and I had claimed the latter.

>> THE GENERAL LAW, AND IT IS THE PART WORTH KEEPING:
>> **AN ORACLE'S `as_of` TRUNCATES THE PERIOD IT WAS CUT IN, SO THE MOST RECENT COMPLETE PERIOD CAN
>> NEVER BE COMPARED AGAINST IT** -- and that is precisely where the freshest, most contested money is.
>> A window-grain bar anchored on a snapshot oracle has a structural hole at its own leading edge.

THE FIX IS GRAIN, NOT A BETTER ORACLE. (There IS no better oracle -- `platinum/_rebuild/` holds exactly
ONE snapshot, verified.) **COO ruled it this morning and it is the fourth instance today:**

    >> IF YOU CAN BE WRONG ABOUT AN ACCOUNT, THE ACCOUNT IS THE UNIT. <<
    (siblings: count at the unit the verdict is rendered at - control on the defect LINE not the FILE -
     assert the ROW not the COLUMN. **The grain is always the grain of the harm.**)

At ACCOUNT + FLOW-DATE grain there are no windows, so there is no window blind spot. **The hole closes
by construction, not by patching.**

=================================================================================================
WHAT THIS BAR ASSERTS

For EVERY flow (account, date) in gold canonical_nna, the served advisor_key must equal the RULED
advisor -- which this file DERIVES ITSELF FROM THE ROSTER. **No expected number is taken from DS.**

    ruled_advisor(account, flow_date, mode):
        usable = roster snapshots for this account, at-or-before flow_date, with a NON-NULL rep_id
        if usable:  the LATEST one          (the roster at-or-before -- the FORWARD rule)
        else:       the EARLIEST usable one (the BASELINE -- the flow predates any roster)
        mode HONOUR_CATCHALL : return it verbatim, catchall included   <- Andrew's ruling
        mode REFUSE_CATCHALL : if it is the house, walk forward to the first NAMED advisor

    T1a  FORK-NEUTRAL   -- both modes agree. The verdict is HARD and binding.
    T1b  FORK-DEPENDENT -- the modes disagree. Rendered under the RULING; the other branch is
                           reported alongside so the bar can render a verdict EITHER WAY.

PROVEN-RED: the 16 named<->named transfers must be observed RED under the CURRENT code before any
green is trusted. A census never observed to say RED has not been shown to be able to.

Read-only: gold canonical_nna + silver accounts_v2. No re-derive, no write, no chain advance.
[STOP] b7bce51bd honoured.
"""
from __future__ import annotations

import io
import sys
from collections import defaultdict

import boto3
import pandas as pd

B = 'opal-data-inf'
HOUSE = 'inflection_wealth_management'
PHANTOM = 'inflection_unmapped_rep'
REP = {'3': HOUSE, '6': 'joe_brandenburg', '11': 'patrick_scanlan', '12': 'peter_lee'}
s3 = boto3.client('s3')


def roster_history() -> dict[int, list[tuple[str, str]]]:
    """{account_id: [(snapshot_date, advisor)]} -- USABLE snapshots only (a NULL rep_id is not a roster
    reading, it is a missing one; 4156's first snapshot is <NA> and that is load-bearing)."""
    parts = sorted(p['Prefix'].split('=')[1].strip('/') for p in s3.list_objects_v2(
        Bucket=B, Prefix='silver/api_dims/accounts_v2/', Delimiter='/')['CommonPrefixes'])
    hist: dict[int, list] = defaultdict(list)
    for d in parts:
        raw = s3.get_object(Bucket=B,
                            Key=f'silver/api_dims/accounts_v2/snapshot_date={d}/data.parquet'
                            )['Body'].read()
        df = pd.read_parquet(io.BytesIO(raw))[['account_id', 'rep_id']]
        df['account_id'] = pd.to_numeric(df['account_id'], errors='coerce')
        df['rep_id'] = df['rep_id'].astype(str).str.split('.').str[0]
        for _, r in df.iterrows():
            a = r['account_id']
            adv = REP.get(r['rep_id'])
            if pd.isna(a) or adv is None:      # <NA> / unmapped rep -> NOT a usable roster reading
                continue
            hist[int(a)].append((d, adv))
    print(f'  roster: {len(parts)} accounts_v2 partitions, {len(hist)} accounts with a usable reading')
    return hist


def ruled_advisor(hist: list[tuple[str, str]], flow_date: str, mode: str) -> str | None:
    if not hist:
        return None
    at_or_before = [adv for d, adv in hist if d <= flow_date]
    adv = at_or_before[-1] if at_or_before else hist[0][1]    # FORWARD, else BASELINE
    if mode == 'REFUSE_CATCHALL' and adv == HOUSE:
        named = [a for _, a in hist if a != HOUSE]
        return named[0] if named else HOUSE
    return adv


print('=' * 100)
print('TIME-LOCK BAR v2 -- ACCOUNT GRAIN. Closes the Q2-2026 blind spot DS found in v1.')
print('=' * 100)
hist = roster_history()

keys = [o['Key'] for p in s3.get_paginator('list_objects_v2').paginate(
    Bucket=B, Prefix='gold/canonical/canonical_nna_') for o in p.get('Contents', [])]
print(f'  gold: {len(keys)} canonical_nna partitions   (DENOMINATOR -- a silent truncation cannot read '
      'as a green)')

rows = []
for k in keys:
    raw = s3.get_object(Bucket=B, Key=k)['Body'].read()
    df = pd.read_parquet(io.BytesIO(raw))
    df['account_id'] = pd.to_numeric(df['account_id'], errors='coerce')
    for _, r in df.iterrows():
        if pd.isna(r['account_id']):
            continue
        rows.append((str(r['date'])[:10], int(r['account_id']), r['advisor_key'], float(r['net_nna'])))
f = pd.DataFrame(rows, columns=['date', 'account_id', 'served', 'nna'])
print(f'  gold flows: {len(f):,} rows, {f["account_id"].nunique()} accounts\n')

f['honour'] = [ruled_advisor(hist.get(a, []), d, 'HONOUR_CATCHALL')
               for d, a in zip(f['date'], f['account_id'])]
f['refuse'] = [ruled_advisor(hist.get(a, []), d, 'REFUSE_CATCHALL')
               for d, a in zip(f['date'], f['account_id'])]

# >> THREE-WAY, NOT TWO-WAY. **MY FIRST CUT WROTE `f['honour'] != f['refuse']` AND IT WAS WRONG.** <<
# An account with NO usable roster reading gets honour=None AND refuse=None -- and **pandas scores
# `None != None` as TRUE** (it treats None as NaN, and NaN != NaN). So every account the roster cannot
# describe was silently swept into the FORK-DEPENDENT bucket, INFLATING the contested set and crashing
# the print on a None. **"I cannot evaluate this" was being reported as "the branches disagree".**
# That is the F4 null rule, in my own classifier: A NULL THAT MEANS TWO THINGS IS A LIE ABOUT ONE OF
# THEM. An instrument that cannot observe must SAY SO -- as its own class, never folded into a verdict.
# (Instrument defect #10 today. Caught because the crash forced me to look at WHY a None was there.)
_known = f['honour'].notna() & f['refuse'].notna()
f['klass'] = 'ROSTER-SILENT'                                     # no usable roster reading at all
f.loc[_known & (f['honour'] == f['refuse']), 'klass'] = 'NEUTRAL'
f.loc[_known & (f['honour'] != f['refuse']), 'klass'] = 'DEPENDENT'

# >> ROSTER-SILENT: THE UNSTATED RULE, AND MY OWN INSTRUMENT'S LIMIT. <<
# I derive the advisor ONLY from accounts_v2. The PRODUCER has a SECOND source -- the `rep_id` carried on
# the TRANSACTION ROW -- so it can attribute an account the roster has never heard of. My bar cannot.
# **That is a limit in MY instrument, not a defect in the fix**, and it is why my firm total did not
# conserve: `groupby` SILENTLY DROPS NaN keys, so these rows vanished from my expected totals while
# remaining in the served ones. THE DRIFT LINE IS WHAT CAUGHT IT -- a time-lock RE-ATTRIBUTES money and
# must never create or destroy it, so a non-zero drift is always an instrument bug or a real leak.
#
# The producer's effective rule -- **derived, because it is written down NOWHERE** -- is:
#     ROSTER SILENT  ->  THE EXISTING ATTRIBUTION STANDS (the time-lock does not re-key it).
# Reconciled EXACTLY: the 4 IWM-served roster-silent accounts sum to +$26,146.83 and acct 331 (served
# peter_lee) is -$40,000.00 -- precisely the two lines where my totals differed from DS's run.
#
# >> IT IS A CORRECT RULE AND AN UNSTATED ONE, AND IT IS WORTH $66,146.83 GROSS OF SERVED ATTRIBUTION.
# >> It is SAFE TODAY only because none of these accounts is currently served under the PHANTOM. If one
# >> ever were, "keep the existing attribution" would PRESERVE THE DEFECT WE ARE FIXING. Assert it.
f.loc[f['klass'] == 'ROSTER-SILENT', 'honour'] = f.loc[f['klass'] == 'ROSTER-SILENT', 'served']

silent = f[f['klass'] == 'ROSTER-SILENT']
if len(silent):
    print(f'  >> ROSTER-SILENT: {len(silent):,} flow(s), {silent["account_id"].nunique()} account(s) '
          f'{sorted(int(x) for x in silent["account_id"].unique())} have gold flows and are NEVER in')
    print('     the roster. The time-lock cannot re-key them; the EXISTING attribution stands.')
    print(f'     net ${silent["nna"].sum():,.2f}  (gross ${silent["nna"].abs().sum():,.2f}).')
    ph = silent[silent['served'] == PHANTOM]
    print(f'     SAFETY ASSERTION 1 -- none of them is served under the PHANTOM: '
          f'{"PASS" if len(ph) == 0 else "*** RED: " + str(len(ph)) + " ARE ***"}')
    print('     (if one ever were, "keep the existing attribution" would PRESERVE the defect.)')
    # >> AND THE ONE THE **LOCK** MAKES LOAD-BEARING (DS: "the first run's derivation is FROZEN. If it
    # >> is wrong, it is wrong FOREVER."). "Keep the EXISTING attribution" is only well-defined if there
    # >> IS exactly one. An account served under TWO different advisors across its history has no single
    # >> "existing" key -- the rule would pick one ARBITRARILY, and the LOCK would then freeze the
    # >> coin-flip PERMANENTLY. This must be asserted, never assumed.
    amb = (silent.groupby('account_id')['served'].nunique() > 1)
    n_amb = int(amb.sum())
    print(f'     SAFETY ASSERTION 2 -- each roster-silent account has exactly ONE served advisor, so '
          f'"keep the existing attribution" is UNAMBIGUOUS: '
          f'{"PASS" if n_amb == 0 else "*** RED: " + str(n_amb) + " AMBIGUOUS ***"}')
    print('     (the LOCK freezes the first run forever -- an ambiguous key would be frozen as a '
          'coin-flip.)\n')

# ---- PROVEN-RED: the CURRENT code must be observed WRONG on the fork-neutral set ------------------
neutral = f[f['klass'] == 'NEUTRAL']
wrong = neutral[neutral['served'] != neutral['honour']]
print('-' * 100)
print('T1a  FORK-NEUTRAL (both branches agree) -- the HARD, binding verdict.')
print('-' * 100)
print(f'  fork-neutral flows: {len(neutral):,}     MIS-ATTRIBUTED under the CURRENT code: {len(wrong):,}')
if len(wrong):
    bad = (wrong.groupby(['served', 'honour'])['nna'].agg(['sum', 'count'])
           .sort_values('sum', key=abs, ascending=False))
    print('\n  PROVEN-RED -- the current code attributes these flows to the WRONG advisor:')
    print('    served (today)                 -> RULED (roster at-the-time)          '
          'net_nna         flows')
    for (sv, hn), r in bad.head(8).iterrows():
        print(f'    {str(sv):<30} -> {str(hn):<30} {r["sum"]:>14,.2f} {int(r["count"]):>7}')
    print(f'\n  accounts affected: {sorted(int(x) for x in wrong["account_id"].unique())}')

# ---- T1b: the FORK-DEPENDENT set, reported under BOTH branches -----------------------------------
dep = f[f['klass'] == 'DEPENDENT']
print('\n' + '-' * 100)
print('T1b  FORK-DEPENDENT (the branches genuinely DISAGREE) -- both shown; ruled by Andrew, not me.')
print('-' * 100)
print(f'  fork-dependent flows: {len(dep):,}   accounts: '
      f'{sorted(int(x) for x in dep["account_id"].unique())}')
for a in sorted(dep['account_id'].unique()):
    g = dep[dep['account_id'] == a]
    print(f'    acct {int(a):<6} ${g["nna"].sum():>14,.2f}  {len(g):>2} flow(s)  '
          f'{g["date"].min()}..{g["date"].max()}   '
          f'HONOUR->{str(g["honour"].iloc[0]):<30} REFUSE->{str(g["refuse"].iloc[0])}')
print(f'\n  >> CONTESTED TOTAL: ${dep["nna"].sum():,.2f}')
print('     v1 (window grain) could see NONE of this -- it all sits in Q2-2026, the quarter the')
print('     oracle truncated. THIS is what the account grain buys.')

# ---- THE CORRECTED REGISTRATION -- DERIVED HERE, NOT TAKEN FROM DS -------------------------------
print('\n' + '=' * 100)
print('THE EXPECTED POST-FIX PER-ADVISOR TOTALS, DERIVED FROM THE ROSTER BY THIS FILE.')
print('  (NOT taken from DS. He told me the registration was short by $3,512.28 and asked me to amend')
print('   the bar rather than let him amend his output. I re-derived it; he is right.)')
print('=' * 100)
exp = f.groupby('honour')['nna'].sum().sort_values(ascending=False)
cur = f.groupby('served')['nna'].sum()
print(f"  {'advisor':<32}{'EXPECTED (ruled)':>20}{'SERVED (today)':>18}{'DELTA':>16}")
for a in sorted(set(exp.index) | set(cur.index)):
    e, c = float(exp.get(a, 0.0)), float(cur.get(a, 0.0))
    mark = '   <<< PHANTOM: must go to ZERO' if a == PHANTOM else ''
    print(f'  {str(a):<32}{e:>20,.2f}{c:>18,.2f}{e - c:>16,.2f}{mark}')
print(f'\n  firm total EXPECTED {exp.sum():>18,.2f}   SERVED {cur.sum():>18,.2f}   '
      f'drift {exp.sum() - cur.sum():>12,.2f}')
print('  (firm total conserved is NECESSARY AND NOT SUFFICIENT -- it is green on the defect today.)')

print('\n' + '=' * 100)
if len(wrong):
    print(f'T1a PROVEN-RED: {len(wrong):,} fork-neutral flows are MIS-ATTRIBUTED by the current code.')
    print('  The instrument SEES the defect. Re-run against the post-fix gold; T1a must go to ZERO.')
    sys.exit(1)
print('T1a GREEN: every fork-neutral flow is attributed to the advisor the roster named at the time.')
sys.exit(0)
