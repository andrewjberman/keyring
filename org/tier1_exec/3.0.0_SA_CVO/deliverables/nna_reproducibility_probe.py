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
deliberately not "do I agree with CTO's number" (a control that only says *I agree with CTO* measures
agreement, not truth). My positive control against his 9 / $453,179.39 FAILED: I get 14 / $439,326.22 --
MORE accounts but LESS money, so the sets are NOT NESTED and we are counting different things. Per COO's
rule, *"reconciling two counts by adjusting one until they agree is how a census stops measuring anything"*,
the unit above is PINNED and the difference is SURFACED, not reconciled away.
"""
from __future__ import annotations

import io

import boto3
import pandas as pd

BUCKET = 'opal-data-inf'
NNA_PREFIX = 'gold/canonical/canonical_nna_'
TXN_KEY = 'silver/transactions/2026-07-10.parquet'


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

    print('\n=== CROSS-CHECK vs CTO ef923bf10 -- SURFACED, NOT RECONCILED ===')
    print('    CTO :  9 accounts / $453,179.39   (cohort-scoped)')
    print(f'    MINE: {len(unbacked)} accounts / ${gu.net_nna.sum():,.2f}   (fabric-wide; unit pinned above)')
    print('    MORE accounts, LESS money -> the sets are NOT NESTED -> a different cohort and/or metric.')
    print('    To reconcile the UNITS (never the NUMBERS): his 9 account_ids + his summation basis.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
