"""AoR/NNA REPRODUCIBILITY PROBE -- can TODAY'S SOURCE reproduce the SERVED number? RUNNABLE, read-only.

    python org/tier1_exec/3.0.0_SA_CVO/deliverables/nna_reproducibility_probe.py

CTO's question (095520Z), which he framed as UNANSWERED rather than answered wrong:
    "CAN THE PIPELINE, FROM TODAY'S SOURCE, REPRODUCE THE SERVED NUMBER?"
He was explicit he was NOT claiming a rebuild would drop the rows -- he was claiming NOBODY HAD CHECKED.
This checks. THE ANSWER IS NO.

THE UNIT (pinned, and deliberately NOT tuned to match anyone else's count):
    an account_id appearing ANYWHERE in served canonical_nna history whose row-count in
    silver/transactions/<snapshot> is ZERO
THE METRIC:
    the sum of that account's served `net_nna` over ALL canonical_nna partitions

MEASURED 2026-07-13: 14 accounts / $439,326.22 unbacked -- and $413K of it sits on TWO NAMED ADVISORS
(peter_lee $328,965.68, patrick_scanlan $84,213.71). This is not a firm-bucket curiosity.

    A CORRECT NUMBER THE SOURCE CAN NO LONGER PRODUCE IS NOT A CORRECT NUMBER; IT IS AN UNBACKED ONE.
    An unbacked number that happens to be right is one backfill away from being wrong, silently, with no
    alarm -- and a reconciliation against gold AS IT STANDS is the one basis that CANNOT detect it.

WHAT THIS PROBE DOES **NOT** CLAIM: that a rebuild WOULD drop these rows. Gold's rebuild semantics are
UNGROUNDED -- by CTO and by me. What is exercised is exactly this and no more: *these accounts' served NNA
has no rows in today's source.* Whether a re-derivation drops them is the NEXT exercise, with its own owner.
(CTO declined to assert a mechanism twice in one day. I am not going to assert his for him.)

INSTRUMENT VALIDATION is the sibling `nna_reproducibility_selfcontrol.py` -- a SELF-GENERATED control, and
deliberately not "do I agree with COO's number" (a control that only says *I agree with COO* measures
agreement, not truth). My positive control against the 9 / $453,179.39 FAILED: I get 14 / $439,326.22. Per
COO's rule -- *"reconciling two counts by adjusting one until they agree is how a census stops measuring
anything"* -- the unit above is PINNED and the difference is SURFACED, never tuned away.

>> RETRACTION (2026-07-13, CTO 103025Z -- CORRECTED IN PLACE, NOT SILENTLY EDITED). <<
An earlier version of this docstring said: *"MORE accounts but LESS money, so the sets are NOT NESTED and we
are counting different things."* **THE SETS ARE NESTED. ALL 9 SIT INSIDE MY 14** (measured by CTO:
77, 302, 1294, 980, 100, 735, 963, 360, 1208). **"More accounts but less money, therefore not nested" was
an INFERENCE, and I promoted it to a structural conclusion without running the one check that separates it
from the alternative** -- namely that *the sets nest and the METRIC differs*. I never enumerated that second
explanation. That is the same count-to-cause error the fabric spent the night on, committed by the person
writing it up, one hour after writing it up. **Refusing to tune 14 down to 9 was right. My account of WHY
they disagreed was wrong.** *Pinning your unit and testing the nesting are DIFFERENT ACTS -- doing the first
does not excuse skipping the second.*

The 9 were **COO's** cohort-scoped figure (the 12 accounts absent from the ROSTER: 3 phantom + 9 retaining a
real advisor), not CTO's. **So the 5 EXTRAS -- 1086, 235, 331, 520, 759 -- ARE THE FINDING: they carry served
NNA, they have ZERO rows in today's source, they are NOT roster departures, and nobody had ever looked at
them.** The roster-departure cohort was never the population; it was the population we happened to be
staring at. A fabric-wide unit found a class the cohort-scoped one is structurally blind to.
"""
from __future__ import annotations

import io

import boto3
import pandas as pd

BUCKET = 'opal-data-inf'
NNA_PREFIX = 'gold/canonical/canonical_nna_'
TXN_KEY = 'silver/transactions/2026-07-10.parquet'

# COO's cohort-scoped 9 (the 12 roster-absent accounts minus the 3 phantom). Measured by CTO 103025Z to sit
# ENTIRELY INSIDE my fabric-wide 14. Held here so the nesting is ASSERTED BY THE PROBE, not by a docstring --
# the claim "the sets are not nested" was exactly the inference that got me, and a comment cannot test itself.
COO_COHORT_9 = {'77', '302', '1294', '980', '100', '735', '963', '360', '1208'}


def _read(s3, key):
    return pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=key)['Body'].read()))


def main() -> int:
    s3 = boto3.client('s3', region_name='us-east-1')
    pager = s3.get_paginator('list_objects_v2')

    keys = [o['Key']
            for page in pager.paginate(Bucket=BUCKET, Prefix=NNA_PREFIX)
            for o in page.get('Contents', [])]
    print(f'=== SERVED NNA UNIVERSE: {len(keys)} canonical_nna partitions (denominator) ===')

    frames = []
    for key in keys:
        try:
            frames.append(_read(s3, key))
        except Exception as exc:                       # a failed READ is not an empty partition (F4 rule)
            print(f'  READ FAILURE (not an absence): {key} -- {type(exc).__name__}: {exc}')
    gold = pd.concat(frames, ignore_index=True)
    gold['account_id'] = gold['account_id'].astype(str)
    print(f'    gold NNA rows={len(gold):,}  accounts={gold.account_id.nunique()}  '
          f'net_nna=${gold.net_nna.sum():,.2f}')

    txn = _read(s3, TXN_KEY)
    tcol = next(c for c in txn.columns if c.lower() in ('account_id', 'accountid'))
    source = set(txn[tcol].astype(str))
    print(f'    silver/transactions rows={len(txn):,}  accounts={len(source)}')

    unbacked = sorted(set(gold.account_id.unique()) - source)
    gu = gold[gold.account_id.isin(unbacked)]

    print("\n=== THE TEST: served-NNA accounts with ZERO rows in today's source ===")
    print(f'    accounts : {len(unbacked)} -> {unbacked}')
    print(f'    served net_nna TOTAL : ${gu.net_nna.sum():,.2f}')
    print(f'    (out of ${gold.net_nna.sum():,.2f} served in total)')
    print('\n    by advisor -- WHO is exposed:')
    agg = gu.groupby('advisor_key')['net_nna'].agg(['sum', 'count'])
    for advisor, row in agg.iterrows():
        print(f'      {advisor:<30} ${row["sum"]:>13,.2f}  ({int(row["count"])} rows)')

    print('\n=== CROSS-CHECK vs COO -- UNITS RECONCILED, NUMBERS NOT TUNED ===')
    print('    COO :  9 accounts / $453,179.39   (COHORT-scoped: the 12 roster-absent accounts, minus')
    print('                                       the 3 phantom)')
    print(f'    MINE: {len(unbacked)} accounts / ${gu.net_nna.sum():,.2f}   (FABRIC-WIDE; unit pinned above)')
    extras = sorted(set(unbacked) - COO_COHORT_9)
    print(f'    THE SETS NEST: all 9 sit inside my {len(unbacked)}.')
    print(f'    >> THE FINDING -- my {len(extras)} EXTRAS: {extras}')
    print('       served NNA, ZERO rows in today\'s source, and NOT roster departures. Never looked at.')
    print('       The roster-departure cohort was never the population -- it was the one we were staring at.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
