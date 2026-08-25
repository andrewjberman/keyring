# PRE-FIRE EXPECTATION — the 12:45Z SCHEDULED 49F CHAIN RUN, 2026-08-25

**pinned by:** `2.0.0_SA_COO` · **published 2026-08-25 ~11:1xZ, BEFORE the artifact exists**
**source-confirmed by:** `0.4.0_DS_ClientPlatform~G` (70233), from the **DEPLOYED** `_code/` copy, not the repo
**why this file exists:** a message scrolls; the reader at 13:00Z opens an artifact set, not an inbox.

---

## THE EXPECTATION

```
DEPLOYED chain  _code/chain_49f_entrypoint.py  (the copy that RUNS)
  :313  "--date  explicit partition date (ad-hoc QA form); absent under --production => T-1 from the trading calendar"
  :326  date = _tc.prev_trading_day(dt.datetime.now(dt.timezone.utc)).isoformat()
        -> ONE date, passed to every stage as `--date D`. NO SECOND PARTITION IN THE PRODUCTION PATH.

lib/trading_calendar  (the ONE frontier definition -- NOT weekday arithmetic)
  prev_trading_day(2026-08-25 Tue)      = 2026-08-24     <- what today writes
  expected_last_trading_day(2026-08-25) = 2026-08-25
```

> ⛔ **TODAY'S RUN WRITES `date=2026-08-24`, AND ONLY `date=2026-08-24`.**
> ⛔ **`date=2026-08-25` WILL STILL BE ABSENT AT 13:00Z. THAT IS THE PASS.**
> Not a partial result. Not a failure. Not something to investigate. After the run the frontier sits **1 trading day
> behind — T-1 — which is the estate's HEALTHY default for every AUM/holdings/trading pipeline.**

---

## ⛔⛔ AMENDED ~11:3xZ — THE EXPECTATION HOLDS BUT ITS *REASON* WAS WRONG, AND THE CHAIN HAS BEEN ABORTING

`0.4.0_DS_ClientPlatform~G` (70295), found while answering the arming question. **SSM command history, materialised
across 15 pages — the FIRST PAGE REPORTED ZERO WITH A `NextToken`, the pagination trap this estate's law names:**
```
2026-08-24 12:45:41  advi-49f-chain-dispatch  FAILED   src=advi.49f.scheduled-floor
2026-08-23 12:45:41  advi-49f-chain-dispatch  FAILED   src=advi.49f.scheduled-floor
2026-08-22 12:46:01  advi-49f-chain-dispatch  Success
```
**BOTH FAILURES, FROM THE RUNS' OWN LOGS:** `ValueError: empty allocation map partition` -> `CHAIN ABORT
stage=a06_identity_crosswalk rc=1 wall=1.0s -- nothing after this stage ran.`
> ⛔ **`c02_twr_daily` IS STAGE 15 OF 16. `a06` IS STAGE 7. TWR HAS NOT EXECUTED SINCE 2026-08-22.**
> ⛔ **SO THE MISSING `date=2026-08-24` IS AN a06 ABORT — NOT the residue of the twr defect the remedy exists to close.**

**THE MECHANISM, AND IT IS SYSTEMATIC RATHER THAN A ONE-OFF:** `a06_dim_identity_crosswalk.py:103` takes
`map_dates[-1]` — the LATEST allocation-map partition — **with no trading-day filter and no non-empty check**
(raise at `:49`). The map **emits EMPTY partitions on weekends**:
```
08-21 Fri 7,321 rows | 08-22 Sat 0 ROWS | 08-23 Sun 0 ROWS | 08-24 Mon 7,332 rows
run 08-23 -> picks 08-22 (0) -> ABORT     run 08-24 -> picks 08-23 (0) -> ABORT     2/2, retrodicted
```
> ⛔ **THIS IS A SYSTEMATIC SUNDAY+MONDAY OUTAGE OF THE ENTIRE 49F GOLD CHAIN, BY CONSTRUCTION.** Not NEVER#1 — this
> is not a stale reading misread as a defect; **it is a real abort with a stack trace, two days a week, unnoticed.**
*(`~G` distinguished a THIRD failure rather than letting a partial fit pass: 08-20 aborted at `a00_dim_account` on
`fact_acc has no partition date=2026-08-20` — **upstream availability, a different stage and a different cause.**
The empty-map mechanism is **2/2 on the failures it claims** and does not claim 08-20.)*

⛔ **CONFIRMED ON THE APPLIED PLANE BY `0.0.0_AB_MSTR`, AND THE DEAD PARTITIONS HAVE A FREE SIGNATURE:**
```
s3 smartx/platform/silver/fact_allocation_account_map
  date=2026-08-21 Fri  775,217 B      date=2026-08-24 Mon  776,585 B
  date=2026-08-22 Sat    4,507 B  DEAD    date=2026-08-23 Sun    4,507 B  DEAD   <- BYTE-IDENTICAL
```
**A parquet file with a schema and a footer and ZERO ROWS. The 175-fold gap is a free discriminator — a dead
partition is distinguishable from a live one with `s3 ls` alone, no parquet read.** Put that in the remedy owner's
hands.
⛔ **AND MSTR's FIRST CONTROL COULD NOT HAVE CAUGHT IT: they checked "is the partition non-empty?" by OBJECT COUNT —
`08-24` -> 1 object, reassuring. Then the negative control: `08-23` -> 1 object, `08-22` -> 1 object. IDENTICAL.
THE EMPTINESS IS ROW-LEVEL AND AN OBJECT COUNT CANNOT SEE IT** — the control returned the same value for the healthy
case and both known-failing cases. *An instrument that cannot separate the two states it is being used to separate.*

**TODAY BOTH PRECONDITIONS HOLD AND IT SHOULD PROCEED:** `a00` needs `fact_acc date=2026-08-24` — **PRESENT**;
`a06` needs a non-empty latest map — **08-24 with 7,332 rows, and NO 08-25 partition exists as of 11:29:03Z.**
⛔ **THE 08-25 RESIDUAL IS NOW EXCLUDED — `0.7.0_AE_CloudOps~G` ruled out what MSTR and I both recorded as unrulable.**
All **41** map partitions materialised and counted client-side (auto-paginated — the trap that bit this thread twice):
```
PARTITIONS EVER WRITTEN BEFORE 12:45Z:  0 of 41.      earliest write in all history: 13:12Z
08-21 13:15:28Z | 08-22 13:15:03Z | 08-23 13:16:07Z | 08-24 13:15:53Z | 08-25 ABSENT at 11:35:25Z
```
**THE CHAIN FIRES AT 12:45Z; THE MAP WRITES `date=D` AT ~13:15Z ON DAY D — THIRTY MINUTES LATER.** An empty `08-25`
partition cannot reach `a06` today. *Bounded by its author: this measures the ARTIFACT's write times, not the
producer's schedule — 41/41 is strong evidence, not a source-confirmed guarantee.*

⛔⛔ **AND IT MAKES THE DEFECT DETERMINISTIC RATHER THAN INCIDENTAL — THIS IS THE STATEMENT THE REMEDY OWNER NEEDS:**
because the map always lands AFTER the chain, **`map_dates[-1]` at 12:45Z is ALWAYS THE PREVIOUS DAY'S PARTITION. The
chain structurally never sees the current day's map.**
```
Sunday  12:45Z -> reads Saturday's  (EMPTY, 4,507 B) -> ABORT
Monday  12:45Z -> reads Sunday's    (EMPTY, 4,507 B) -> ABORT
Tuesday 12:45Z -> reads Monday's    (776,585 B)      -> proceeds
```
**IT IS NOT *"sometimes the latest partition happens to be empty."* IT IS: THE CHAIN ALWAYS CONSUMES D-1's MAP BY
CONSTRUCTION, AND D-1 IS EMPTY EVERY SUNDAY AND MONDAY.** The 4,507-byte tell holds **4/4** across two weekends
(08-15, 08-16, 08-22, 08-23). **A remedy written against "handle empty partitions" fixes the symptom; the mechanism is
the D-1 read.**

**WHAT THIS CHANGES IN THIS DOCUMENT: only the WHY.** The expectation below is unchanged and still correct — today
writes `date=2026-08-24` only, and an absent `08-25` is the pass. **What was wrong was the assumption that 08-24 was
missing because of the twr defect. It was missing because the chain never reached stage 15.**

---

## ⛔ THE TRIGGER IS ARMED — VERIFIED LIVE, AND THE PLANE MATTERS

`0.0.0_AB_MSTR` asked 85 minutes ahead whether anything is actually armed, having enumerated **all 137 EventBridge
RULES in us-east-1** — positive control firing, denominators printed — and found **`cron at 12:45 = 0`**. They bounded
it themselves: *"this is an EventBridge-plane result and nothing more."* **They were right to ask and right to bound it.**

**MEASURED AT THIS SEAT, ON THE OTHER PLANE:**
```
infra/aws/terraform/opal-assets/advi_49f_floor.tf:242   resource "aws_scheduler_schedule" "advi_49f_gold_floor"
                                                 :252   schedule_expression = "cron(45 12 * * ? *)"  tz UTC
LIVE  aws scheduler get-schedule --name advi-49f-gold-floor --group-name default
      -> advi-49f-gold-floor   ENABLED   cron(45 12 * * ? *)   UTC
LIVE  advi-49f-publisher       DISABLED           <- consistent with the publish gate standing
```
> ⛔ **THE FIRE IS ARMED. `events list-rules` AND `scheduler list-schedules` ARE TWO DIFFERENT AWS SERVICES, AND A
> COMPLETE CENSUS OF ONE IS ENTIRELY SILENT ABOUT THE OTHER.** EventBridge **Scheduler** schedules do not appear in
> EventBridge **Rules** at any limit, ever.

**THIS IS THE WRONG-PLANE CLASS AT ITS MOST CONVINCING: 137 rules materialised, a positive control that fired, an
honest denominator, and a TRUE ZERO — about a plane the question was not on.** It cost nothing only because MSTR
published the bound with the number and asked 85 minutes early instead of reporting an unarmed pipeline.

---

## ⛔ WHY A NON-EVENT IS WORTH A RECORD

**This is the exact shape of the false outage NEVER#1 exists to prevent, and it is pre-loaded to fire at 13:00Z.**
A seat reading the artifact set after the run, finding no `date=2026-08-25`, and reporting *"the run wrote a stale
partition"* would be **wrong, confident, and entirely reasonable-looking.** The law's own record is that this recurred
to the point of an Andrew-direct — *"the 100th time this scenario has happened"* — with three seats independently
repeating the same instrument.

> **AN EXPECTATION PUBLISHED BEFORE THE MEASUREMENT CANNOT BE BENT BY THE MEASUREMENT.**

Same property that made `0.7.0_AE_CloudOps~H`'s pre-published `CodeSha256` worth confirming: **a value stated in
advance is a test; the same value produced afterward is a description.**

---

## ⛔ TODAY IS ONE VARIABLE CHANGED, NOT TWO UNKNOWNS — `1.0.0_SA_CTO`, MEASURED

They had written that today tests two things (*does the chain complete* AND *does the fix work*), since stages 8-14
had not run since 08-22 either. **They went and bounded it from the run's own log:**
```
s3://opal-data-49financial/gold/advi/_logs/chain_20260822T124602Z.log
  12 consecutive stage results, ALL rc=0 · c02 present (ran) · STAGE OK c04_validation rc=0
  CHAIN OK date=2026-08-21 wall=96.8s        <- ALL 16 STAGES, END TO END
```
> **THE FULL CHAIN COMPLETED THREE DAYS AGO. Stages 8-14 are not an unknown — they have a clean end-to-end run behind
> them, and every failure since is the a06 empty-map abort.**
```
08-22:  same chain, same 16 stages, OLD c02  -> CHAIN OK, c02 refused 7,335 of 7,335 rows
today:  same chain, same 16 stages, NEW c02  -> the ONLY thing that changed
```
**THIS IS THE CLEANEST TEST SHAPE AVAILABLE, AND IT SHARPENS WHAT A FAILURE WOULD MEAN:** a chain failure today at a
stage OTHER than a06 is **not** ambiguous between "the chain is flaky" and "the remedy broke something" — **stages
8-14 have a clean run behind them, so a new failure there points at the change.**

---

## WHAT *WOULD* BE A REAL FINDING AT 13:00Z

| observation | verdict |
|---|---|
| `date=2026-08-24` **ABSENT** after the run | ⛔ **REAL FAILURE — shout about this one.** |
| a **SECOND** partition appears | ⛔ **Falsifies the one-date-per-run reading — the deployed chain is not what we read.** |
| `REFUSED-NO-BMV` on accounts present at **BOTH** D and D-1 | ⛔ **`GLD-f-1`'s actual acceptance criterion.** |
| `date=2026-08-25` absent | **EXPECTED. Pre-stated here. Not a finding.** |

**Read against this table, not against intuition.**

## STANDING CONSTRAINTS ON THIS RUN

- **NOBODY ACCELERATES IT.** The 12:45Z fire is the exercise for a sovereign publish intent; **an ad-hoc run is a QA
  instrument and NEVER production evidence.**
- **The `c04` battery is NOT corroboration** — its check 7 passes `twr_daily=None` and has never evaluated a return.
- **`GLD-f-3` (the deploy-completion ledger entry) is an OPEN NEVER#6 item with a named owner and is not discharged by
  this run.**

**PROVENANCE:** the source read and the calendar derivation are `0.4.0_DS_ClientPlatform~G`'s, taken against the
DEPLOYED `_code/` copy rather than the repo — **the repo has no causal relationship to this run** — and reported
3/3 rather than generalised from one observation.
