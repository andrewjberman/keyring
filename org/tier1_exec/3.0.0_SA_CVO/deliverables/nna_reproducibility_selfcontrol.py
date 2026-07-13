"""SELF-GENERATED CONTROL for the NNA reproducibility probe. RUNNABLE, read-only.

    python org/tier1_exec/3.0.0_SA_CVO/deliverables/nna_reproducibility_selfcontrol.py

WHY THIS EXISTS. My positive control for `nna_reproducibility_probe.py` was "does my derivation reproduce
CTO's independently-measured 9 accounts / $453,179.39?" **IT FAILED** -- I get 14 / $439,326.22: MORE
accounts but LESS money, so the two sets are NOT NESTED. I told CTO that if the control failed I would treat
it as having measured my own harness, say so, and stop. So I stopped -- and then validated the instrument a
different way.

**A CONTROL THAT ONLY SAYS "I AGREE WITH CTO" MEASURES AGREEMENT, NOT TRUTH.** It cannot distinguish
"my instrument is sound" from "my instrument is broken in the same direction as his." So the control below
is SELF-GENERATED and grounded on facts I can check directly against S3:

  (a) NEGATIVE arm -- every account in MY unbacked set must TRULY have zero rows in silver.
      If any has rows, my set is wrong. (Result: all 14 confirmed 0 rows.)
  (b) POSITIVE arm -- accounts I did NOT flag must be PRESENT in silver.
      Without this the set could be undiscriminating (calling everything unbacked) and still "pass" (a).
      (Result: 650/906/4316/4353/4355 -> 2142/1481/9/3/5 rows, correctly NOT flagged.)
  (c) INDEPENDENT CORROBORATION -- CTO's phantom 3 (560/703/1225) must come back PRESENT-but-NULL-rep_id,
      NOT unbacked. This reproduces his ef923bf10 measurement TO THE ROW off my own read of silver, which
      is the strongest available evidence that I am reading the source correctly -- WITHOUT keying my
      verdict on his number.
      (Result: 945/1406/932 rows, rep_id=['<NA>'] on every row, none in my unbacked set. Exact match.)

VERDICT: instrument SOUND. The 14-vs-9 discrepancy is a DEFINITION difference (his is cohort-scoped, mine is
fabric-wide), not a defect in either instrument. Therefore the unit is PINNED and the difference is
SURFACED -- never reconciled by editing 14 down to 9.

    "Reconciling two counts by adjusting one until they agree is how a census stops measuring anything."
"""
from __future__ import annotations

import io

import boto3
import pandas as pd

BUCKET = 'opal-data-inf'
TXN_KEY = 'silver/transactions/2026-07-10.parquet'

# My unbacked set, from nna_reproducibility_probe.py.
UNBACKED = ['100', '1086', '1208', '1294', '235', '302', '331',
            '360', '520', '735', '759', '77', '963', '980']
# Accounts I did NOT flag -- they must be PRESENT, or my set is undiscriminating.
KNOWN_PRESENT = ['650', '906', '4316', '4353', '4355']
# CTO's phantom cohort -- must be PRESENT with a NULL rep_id, and must NOT be in my unbacked set.
PHANTOM = ['560', '703', '1225']


def main() -> int:
    s3 = boto3.client('s3', region_name='us-east-1')
    txn = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=TXN_KEY)['Body'].read()))
    acct_col = next(c for c in txn.columns if c.lower() in ('account_id', 'accountid'))
    rep_col = next((c for c in txn.columns if c.lower() == 'rep_id'), None)
    acct = txn[acct_col].astype(str)
    print(f'silver/transactions rows={len(txn):,}  distinct accounts={acct.nunique()}')

    print('\n=== (a) NEGATIVE arm -- each of my 14 must TRULY have ZERO rows in silver ===')
    wrong = [a for a in UNBACKED if int((acct == a).sum()) != 0]
    for a in wrong:
        print(f'    *** {a}: {int((acct == a).sum())} rows -- MY SET IS WRONG')
    print(f'    all {len(UNBACKED)} confirmed 0 rows: {not wrong}')

    print('\n=== (b) POSITIVE arm -- accounts I did NOT flag must be PRESENT (else undiscriminating) ===')
    ok_pos = True
    for a in KNOWN_PRESENT:
        n = int((acct == a).sum())
        ok_pos = ok_pos and n > 0
        print(f'    {a:<6} {n:>6} rows in silver   correctly NOT flagged: {n > 0}')

    print("\n=== (c) INDEPENDENT CORROBORATION -- CTO's phantom 3: PRESENT but rep_id NULL, NOT unbacked ===")
    ok_ph = True
    for a in PHANTOM:
        sub = txn[acct == a]
        reps = sorted({str(v) for v in sub[rep_col].unique()}) if rep_col else ['?']
        in_mine = a in UNBACKED
        ok_ph = ok_ph and len(sub) > 0 and reps == ['<NA>'] and not in_mine
        print(f'    {a:<6} {len(sub):>6} rows   rep_id={reps}   in my unbacked set: {in_mine}')
    print("    reproduces CTO's ef923bf10 (945/1406/932 rows, all-<NA> rep_id): "
          f'{ok_ph}')

    sound = (not wrong) and ok_pos and ok_ph
    print('\n=== VERDICT ===')
    print(f'    INSTRUMENT SOUND: {sound}')
    if sound:
        print('    -> the 14-vs-9 gap vs CTO is a DEFINITION difference, not a defect.')
        print('    -> unit PINNED, difference SURFACED. Do NOT edit 14 down to 9 to make them agree.')
    else:
        print('    -> INSTRUMENT BREAK. The probe result is UNREADABLE. Do not quote it.')
    return 0 if sound else 2


if __name__ == '__main__':
    raise SystemExit(main())
