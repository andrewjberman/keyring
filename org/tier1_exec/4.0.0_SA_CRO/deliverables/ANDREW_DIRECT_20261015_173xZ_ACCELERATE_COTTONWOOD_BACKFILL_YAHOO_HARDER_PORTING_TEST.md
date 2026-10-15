# ANDREW DIRECT -- accelerate the Cottonwood backfill; push Yahoo harder; the Yahoo-vs-Bloomberg targeted parity draw (2026-10-15 ~17:3xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. He was answering this seat's Cottonwood backfill state
read (`RESEARCH_20261015_COTTONWOOD_BACKFILL_STATE.md` @03d1a87a9c).

**Verbatim:**

> Yeah I want to accelerate this project, I am fine with pushing yahoo finance harder, as well. I believe we had a strategy whereby we checked yahoo finance against bbg on a targeted draw basis to establish acceptable parity. We need to pick up the pace on this.

## What it sets (surfaced, not adjudicated)

1. **Accelerate the Cottonwood backfill** (ADVI_COTBKF; today `status: hold`, placement DELL1). This reads as Andrew's word to un-park it.
   The owner (`1.0.0_SA_CTO~DELL1`) applies it, or asks him once if it reads it narrower.
2. **Push Yahoo finance harder** for the price fill.
3. **The strategy he recalls exists** and was approved by his "Go with your rec" on 10-13, recorded in the MDPF_DEMQUE decomposition round 9
   amendment 14:
   - **The PORTING TEST:** Bloomberg prices a targeted sample. Returns over 5 intervals per security must agree within 10 bps, at most 10
     cells a security.
   - Until a Yahoo-sourced price passes, it reads UNVERIFIED.
4. **The pace is to pick up.**

## Measured state of that strategy (2026-10-15 ~17:3xZ, from the repo)

- **The request is built and filed but frozen:** `MDPF_SECHIST-CARD-A-PORTING-TEST`, 326 CUSIPs, 1,630 intervals, 3,195 cells, comparator
  `porting_test.py` (DQ-t-49 @567a058ddb, DQ-t-51 @adbdc57967).
- **The drawer can draw it:** it learned CUSIP entries, DQ-t-56 @3885d9eef1, 10-13.
- **No porting draw result or verdicts file is recorded.** `~/.opal/demque/porting_verdicts.json` "is written by a later cell after the
  Bloomberg porting draw" (amendment 22). So every Yahoo-sourced Cottonwood price still reads UNVERIFIED (the `porting_verdict` column,
  DQ-t-59).
- **Bloomberg budget:** about 62,700 cells wanted over two weeks against 23,432 at the day rate. The fit is UNMEASURED until the
  2026-10-17 receipt (CTO msg 5174).

-- recorded by 4.0.0_SA_CRO~DELL2
