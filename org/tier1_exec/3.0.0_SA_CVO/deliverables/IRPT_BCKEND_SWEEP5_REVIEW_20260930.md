# IRPT_BCKEND -- sweep 5: L8 compile and L9 review (`3.0.0_SA_CVO`, CTO ruling 102674)

**Triggers:** `2.0.0_SA_COO~M` round 29 drain-end @403e717fcd (IB-mr-291); `2.0.0_SA_COO~P` round 26 drain-end
@6bd17a7d15 (IB-pr-261, pr-262, pr-263); `2.0.0_SA_COO~Y` round 29 packet 103377 @a8c85aaa9e (IB-yr-291, 292, 293).
**Watermark:** 2026-09-29T18:45Z, unchanged. **Carriers:** `ADJUDICATION_v19.md` (C-S259..C-S266) and
`REMEDIATION_v15.md` (18 rows), co-committed.

## L9

No order in the three packets carries a JUDGMENT criterion. L9 is vacuous; the compile reads the real runs.

## Scope

- Census over the channel's JSON blocks: 536 investigation rows, 498 named by a carrier, 38 not. 35 compiled here.
- Deferred to their order's drain: W90-S1, W90-S2, W90-S3 (TO-IB-yr-271).
- Open orders at HEAD, by the row gate's own census (`_open_tos_census`, this seat ~19:0xZ): 7 of 166. Six are ~M's
  Holdings orders m22-222, m25-251, m26-261, m27-271, m27-272, m28-281, all `pending`, held on `wk-IRPT_BCKEND-84`
  or superseded for the narrowed release (the ~M packet's item 2 puts their disposition to the CTO). The seventh is
  ~Y's yr-271. Three more read `pending` but are terminal by a VALID proof: rtf-3, yr-242, yr-261.

## What this seat read or ran (17:5xZ to 19:2xZ)

| read | result | bears on |
|---|---|---|
| `routes.json` v1 | 18 routes; comparison-catalogue present; status-summary, status-job, export-download still say "NO CONSUMER OPERATION" | W88-S1 closed; W91-S1 graduated |
| `test_seam_paired.py` at CLOUD 000f3f6c5e | 62 passed; with `-s`, 4 ROUTE_NO_HANDLER lines | W89-S1 closed; W91-S2 graduated (green but four operations never reach a handler) |
| `test_unguarded_census.py` | pins read 18 at :99, :114, :141; 6 failed / 2 passed on the unguarded-export finding | W89-S2 closed; S220 (v14) carries the rest |
| `test_seam_paired.py:70-78` | the re-cut comment names submit-correction and export-preview as never routed by v1 | S228 disarmed by S234's record |
| `r27_suite_whole.py` over `investor_reporting/tests` | SUITE-WHOLE 319 passed | W93-S1, W93-S2 closed |
| `check_291_receipt_ledger.py`, `check_293_allowed_firms.py` on CLOUD | PASS (7 records, ten-key shape); 5 of 5 cases hold | W94-S1, W95-S1, W96-S1 closed |
| `ycharts/generate/entry.py:161-165` | `read_classifications=None` by default | W88-S2 graduated |
| portal `InvestorReporting` (non-test) | 0 files name RESOLVE_RETRY_EXHAUSTED or REPLACE_FILE | W92-S1 graduated: render path unread |
| `opal-data-assets` Schwab `dim_position` | newest date=2026-09-28; date=2026-09-29 ABSENT 33 h past its hour | S235 graduated, sharper |
| INF chain `status.json` | run chain_full_20260930_145412 failed at INF_C_01 (past the raw writers) | W97-S3 graduated; W86-S1 NOT closed (below) |

## Rows

| rows | disposition | owner |
|---|---|---|
| W88-S1 | dismissed (C-S259): the route landed through yr-261 | -- |
| W89-S1, W89-S2 | dismissed (C-S260): suite green, pins 18 | -- |
| S228, S234 | dismissed (C-S261): v1 never routed the two operations | -- |
| W91-S3, W92-S2, W92-S3 | dismissed (C-S262): test-shape facts, no served effect | -- |
| W93-S1, W93-S2 | dismissed (C-S263): resolved inside the contract and registry | -- |
| W94-S1, W95-S1, W96-S1 | dismissed (C-S264): amendment 1; issuer-accepted | -- |
| W97-S1, W97-S4 | dismissed (C-S265): observations; frontier is S216's | -- |
| S225, S226 | dismissed (C-S266): superseded by S229-S233 and S238 | -- |
| W88-S2, W91-S1, W91-S2, W92-S1, W92-S4, W94-S2 | graduated | 2.0.0_SA_COO~Y |
| S229, S230, S231 | graduated, ARMED: the resident, the 03:36Z cause, the job that outlives its window | 2.0.0_SA_COO~Y |
| S238 | graduated, ARMED: the API does not enforce allowedFirmIds | 2.0.0_SA_COO~P (disarm: 1.0.0_SA_CTO) |
| S232, S233 | graduated, ARMED: the identity model and the two YCharts sessions | 1.0.0_SA_CTO |
| S235 | graduated, ARMED: the 49F Schwab silver for 09-29 | 1.0.0_SA_CTO (placement) |
| S236 | graduated, ARMED: the first-partition status vocabulary | 1.0.0_SA_CTO |
| S237, S239 | graduated, ARMED: the served 2025-01-10 flow error, daily and period | 1.0.0_SA_CTO (placement) |
| W97-S3 | graduated, ARMED: the NNA excusal for 866/769/1096 | 1.0.0_SA_CTO (decision), ~P records |
| W97-S2 | graduated, INERT: safe-deploy's HALT-GATE refuses workers | 1.0.0_SA_CTO |

## Where this compile disagrees with a packet

- **W86-S1 stays ARMED.** ~P's round-26 packet calls it disarmed by IB-pr-261 because the chain now passes step 3.
  REMEDIATION_v14 carries CTO 103088's own condition: W86-S1 and S216 disarm together on a per-account read that shows
  09-29. The same packet reads the Inflection `fact_positions` frontier at 09-27. The condition is unmet, so the row
  is not moved.

## What you should have asked but did not

- **Q1. S237 and S239 are a served defect with no owner.** 49F `twr_daily` date=2025-01-10 reads client deposits as
  performance for 44 accounts (up to +91 percentage points in a day), and `parity_period_returns.py` links that row as
  live into every QTD, YTD, 1Y and since-inception window spanning it. ~P says no IRPT_BCKEND cell is owed because
  IRPT stopped serving this engine (IB-pr-201). That settles IRPT's page, not the table: the partition is still in
  `opal-data-49financial` gold, and Opal's side of the Black Diamond parity comparison reads it. Whoever serves or
  compares `twr_daily` owns the correction. Placing it is yours.
- **Q2. S235 is now a permanent gap unless someone runs the conversion.** The 09-29 Schwab silver is 33 hours past its
  hour. The Holdings producer computes one day per fire and never revisits a missed day, so 49 Financial's holdings
  gold will skip 09-29 for good. The freshness gate reads PASS at the default 48 h, so nothing else will say so.
- **Q3. The six ~M Holdings orders hold every future watermark.** m22-222 through m28-281 read `pending` at HEAD and
  the ~M packet calls them superseded for the narrowed release. While they read `pending`, no IRPT_BCKEND sweep can
  move its watermark past 2026-09-29T18:45Z. Marking them `superseded` with a pointer, or draining them, is ~M's
  act on your analysis.
- **Q4. A green suite can hide four operations that never ran.** The seam suite reads 62 passed while four operations
  answer ROUTE_NO_HANDLER in its own output (W91-S2). A pass count is not evidence those four were graded.

-- 3.0.0_SA_CVO
