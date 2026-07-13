"""GATE-2 (3.0.0_SA_CVO~B) -- THE OFF-IS-A-NO-OP GUARD.

A PERMANENT REGRESSION GUARD AGAINST A DEFECT THAT DOES NOT EXIST YET.

WHY THIS EXISTS. DS refused to build CTO~B's F2-B ruling (a) as literally written, exercised it, and
reported it against the ruling. I confirmed the mechanism independently rather than take his word:

    apply_resolution_fold is MOVERS-ONLY -- it re-keys only the resolution's is_mover rows
    (aor_resolution :764-770: "ZERO movers -> a structural NO-OP (DELTA-0)").
    UNDER SWITCH-OFF THE RESOLVER FOLDS NOTHING, so the resolution carries ZERO MOVERS *BY DESIGN*.

    Ruling (a) would DEFAULT attach_advisor_key's `absent=` to a canonical label. But in
    apply_resolution_fold, "absent from the resolution" means "NOT A MOVER" -- and under OFF that is
    EVERY ACCOUNT.

    => every account's advisor_key OVERWRITTEN with the label. UNDER OFF. AT DEPLOY. Across all SEVEN
       movers-only consumers. The state we spent the entire night calling "DELTA-0, zero risk" is the
       state in which that ruling is MAXIMALLY DESTRUCTIVE.

THE POINT OF THIS FILE. That defect is currently only a RULING, not code. A guard written only after a
defect ships is a post-mortem. This one goes RED the moment anyone implements it -- so the fabric cannot
land it quietly, in either direction:

    * default `absent=` to a label            -> this arm goes RED (every key wiped under OFF)
    * or make `absent=` REQUIRED (DS's fix)   -> this arm stays GREEN, and a call-site that FORGETS the
                                                argument cannot compile past it (F4-B doctrine: a
                                                call-site cannot forget an argument that does not exist)

THE INVARIANT IT PINS, and it is the one the whole round rests on:
    >> UNDER OFF, THE FOLD IS A NO-OP. EVERY ACCOUNT KEEPS ITS SERVICING KEY. DELTA-0 IS NOT A HOPE,
    >> IT IS AN ASSERTION.
Every "nothing is served / switch OFF / zero risk" claim made tonight is a claim about THIS invariant.
Nothing else asserted it directly.

Hermetic: real lib, no prod touch, no gold run.
"""
from __future__ import annotations

import sys

import pandas as pd

sys.path.insert(0, r'C:\Users\AndrewBerman\Desktop\ajb_workspace\data\inf\scripts\gold\lib')

from aor_resolution import apply_resolution_fold  # noqa: E402

SERVICING = {1: 'peter_lee', 2: 'noel_soderblom', 3: 'patrick_scanlan'}

# Every account already carries its SERVICING advisor_key -- today's behaviour under OFF.
df = pd.DataFrame({'account_id': list(SERVICING), 'advisor_key': list(SERVICING.values()),
                   'rep_bucket': ['individual'] * 3})

# UNDER OFF the resolver folds NOTHING: the resolution carries ZERO movers, BY DESIGN.
res_off = pd.DataFrame({'account_id': pd.Series([], dtype='int64'),
                        'advisor_key': pd.Series([], dtype=object),
                        'rep_bucket': pd.Series([], dtype=object),
                        'servicing_advisor_key': pd.Series([], dtype=object),
                        'is_mover': pd.Series([], dtype=bool)})

print('=' * 96)
print('OFF-IS-A-NO-OP GUARD -- under switch-OFF, does every account KEEP its servicing key?')
print('=' * 96)

out, n_rekeyed = apply_resolution_fold(df, res_off)
print(out[['account_id', 'advisor_key']].to_string(index=False))

kept = [a for a in SERVICING if str(out.loc[out.account_id == a, 'advisor_key'].iloc[0]) == SERVICING[a]]
wiped = [a for a in SERVICING if a not in kept]

print(f'\n  accounts KEEPING their servicing key : {len(kept)} of {len(SERVICING)}')
print(f'  accounts OVERWRITTEN                 : {len(wiped)}   (re-keyed count reported: {n_rekeyed})')

print('\n' + '=' * 96)
if not wiped and n_rekeyed == 0:
    print('GREEN -- UNDER OFF THE FOLD IS A NO-OP. DELTA-0 HOLDS.')
    print('  Every "nothing served / switch OFF / zero risk" claim in this round rests on this invariant,')
    print('  and this is the arm that asserts it. If anyone DEFAULTS attach_advisor_key\'s `absent=`,')
    print('  zero movers under OFF makes EVERY account "absent" and this arm goes RED -- which is exactly')
    print('  what it is here to do, before that reaches a served artifact.')
    sys.exit(0)

print('*** RED -- THE FOLD IS NOT A NO-OP UNDER OFF. ***')
print(f'  {len(wiped)} account(s) had their advisor_key OVERWRITTEN with the switch OFF: {wiped}')
print('  This is the catastrophic shape: under OFF there are ZERO movers BY DESIGN, so "absent from the')
print('  resolution" means EVERY ACCOUNT. A defaulted `absent=` wipes the served advisor_key across all')
print('  seven movers-only consumers, AT DEPLOY, in the state we call "zero risk".')
print('  DO NOT SHIP. Make `absent=` REQUIRED, never defaulted.')
sys.exit(1)
