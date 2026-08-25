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
