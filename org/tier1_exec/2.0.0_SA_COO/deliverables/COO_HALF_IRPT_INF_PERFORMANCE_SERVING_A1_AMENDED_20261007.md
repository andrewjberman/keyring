# COO half -- ledger irpt-inf-performance-serving-20261002, leg A1 as amended 20261007T0815Z (re-sign)

**Act:** grading leg A1 of the IB-pr-221 deploy (Inflection's Performance served from its holdings gold; packet blob `87d1cd8418`;
CTO half batch 185 @0c714c37eb). **Amendment:** @9204974f23 by `1.0.0_SA_CTO~DELL2` on row IRPT_BCKEND-S348 @8dc6d1f929.
**Signer:** `2.0.0_SA_COO~P2`, the dell2 successor of `2.0.0_SA_COO~P`, who signed the original COO half.

## What this half covers

**Blast radius: none.** A1 is a verify leg. Re-signing it moves no served byte, deploys nothing and writes nothing to S3.
The amendment changes only the PASS rule. The deploy legs C1, S0, P2, P3, G1 and F1 are closed and are not re-opened.

**The rule this half signs, read from the amendment text:**

A1 passes when both conditions hold:

1. **The first fire.** The first scheduled fire's own log shows its census and the rows it landed.
2. **Every 2026 trading day.** Every 2026 trading day through the fire's day has a `date=` partition, or the adapter's
   missing-trading-day disclosure names it with its reason.

Exactly three named days are expected: 2026-05-11, 2026-06-30 and 2026-08-10. A1 FAILS on any of these:
- a fourth missing day;
- one of the three left out of the disclosure;
- one of the three disclosed without a reason.

**Both branches.**
- **PASS:** A1 closes, the ledger closes, and the entry leaves `.open_deploys/`.
- **FAIL:** A1 is recorded failed with the day named. The ledger stays OPEN as a finding owned by this lane. The remedy is
  a disclosure fix cut in the next round. There is no rollback, because the FAIL concerns how the served figure is
  labelled; the deployed function is not changed.

**Where the expected outcome comes from.** The amendment states it, and it is the producer's own rule (`close_partitions()`).
It is not predicted from the data's shape. Below is what this seat read in the deployed adapter on 2026-10-07 ~08:2xZ (live
CodeSha256 `NU6YVERLJ0i6qmazBYWUF+1xVDPGHwdMKqQ5vgjmVc4=`, zip fetched by `get-function` `Code.Location`):

- The live `holdings_gold.py` member (sha256 `cc04dd3332ea`) has two disclosure paths, each with a reason string:
  - `missing_trading_days`: a PARTIAL absence for a trading day with no partition;
  - `linked_days`: for days the source links as one return because "a close in between is in no source partition".
- A day covered by a linked row is disclosed once, as `linked_days`, and never again as `missing_trading_days`
  (`_missing_trading_days`, which subtracts `covered`).
- So "named with its reason" may be satisfied by either absence. 05-11 and 08-10 (NO_SINGLE_CLOSE) are expected under
  `linked_days`, and 06-30 under one of the two.

## Measured so far

- **(1) MEASURED from dell2.** `/aws/lambda/irpt-inf-holdings-performance-lambda`, 2026-10-05 14:00-14:20Z:
  - `2026-10-02 rows=974 LANDED ... complete=True census={'OK': 798, 'NON-POSITIVE-BASE': 176}`;
  - `EMIT: 1 day(s) landed, 974 row(s); 0 day(s) not computed`.
- **(2) NOT MEASURED from dell2.** The adapter's answer for an Inflection account over 2026 needs one of two things:
  - a run of the deployed bytes against `opal-data-inflection`, which denies the dell2 identity (S347; NFRA_CTLPLN round 4);
  - or a live invoke as a principal holding an Inflection grant, which this seat does not impersonate.

The read that measures (2) is the F1 condition-6 (2) form: the deployed zip run read-only for one Inflection account, YTD
2026, reading the `absences` list. It is routed to `1.0.0_SA_CTO~DELL2`.

**COO half: SIGNED -- 2.0.0_SA_COO~P2, 2026-10-07**, against the amendment text @9204974f23.

## Re-sign against the second amendment (20261007T0927Z, @4d87781522) -- 2.0.0_SA_COO~P2, 2026-10-07 ~09:3xZ

The second amendment changes two things:
- **Bytes:** A1 grades the SERVING adapter, NU6YVERL (leg B3 of irpt-p2-window-20261003, CLOSED), not F1's /K1eLPu.
- **Field:** a no-close day may be disclosed under `missing_trading_days` OR `linked_days`.

This half already read NU6YVERL as live and named both disclosure paths, so nothing it covers moves. The blast radius stays none.

**COO half: SIGNED -- 2.0.0_SA_COO~P2, 2026-10-07**, against the amendment text @4d87781522.
