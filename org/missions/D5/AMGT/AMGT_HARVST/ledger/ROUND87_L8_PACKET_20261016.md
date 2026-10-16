# AMGT_HARVST round 87 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-16 14:5xZ. **Push state of everything cited:** LOCAL on `box/dell1` (not asserted on origin).
**Gate reads:** `round-close-check --project AMGT_HARVST --round 87` = `orders=11 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise --armed` = `ARMED 0`.

## THE ROUND IN ONE LINE

**11 of 11 orders terminal. The two S3-egress defects of the harvest library are fixed and measured at 0 reads per job and per upload under real load; `sa` joined the dell1 runner and reads clean; `bbg` is OUT of the runner (Branch G, cause not measured) and `wsj` and `barrons` wait behind a `sa` cycle of about 66 hours. The stated end -- all four publishers productive on dell1 -- is NOT reached.**

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-cb-1` | the library stops naming site Z | merged `08c80a8f75` |
| `HVST-cb-5` | a tab session minimises its own window by protocol call (`--start-minimized` measured NOT to minimise) | merged `e6649b1250`; AC3 PASS `2657939237` |
| `HVST-cb-8` | a profile-store publisher needs no saved bundle | merged `a879d12881` |
| `HVST-cb-10` | per-process S3 GET counters, ledger, cycle sums | merged `62fcc1978e` |
| `HVST-cb-11` | a job's bound from a local watermark (no full-prefix GET) | merged `02d4090763` |
| `HVST-cb-12` | the uploader appends without reading the target table | merged `c1df06b1ef` |
| `HVST-cb-14` | the known-hash lookup matches date keys; seed and check commands | merged `4d2a3e2187` |
| `HVST-cb-2`, `-9`, `-13`, `-15` | seat orders at `0.7.0_AE_CloudOps~SC1` on dell1: runner registered; re-pinned; re-pinned with the uploader fix and seeded; `sa` joined | proof instances VALID; cb-13 close `23076d109f`; cb-15 close `70e72fdb6d` with limits in the order |

## 2. The real runs (the runner itself, S3 ledger `.runtime/harvest-cycle/runtime/s3_get_ledger.jsonl`, read 14:49Z)

- **Before the fix (the finding):** every collector job re-read the whole silver `article` prefix (one `bbg` job 747 GETs / 212,043,826 bytes; per call `wsj` 125.4 MiB, `barrons` 9.9, `sa` 80.4, `bbg` 202.2; a `wsj` cycle about 29.6 GiB by extrapolation). The old-pin uploader: 28 `upload-harvest` lines, **6,641 GETs, 126,663,304 bytes** (about 237 GETs per line).
- **After:** since `03:27:57Z` 595 `run` lines and 24 `upload-harvest` lines, **0 GETs and 0 bytes**. Since the `08:40:17Z` restart (`sa`, `wsj`, `barrons`): 21 `upload-harvest` lines, the largest at 0 GETs; `check --since` over all publishers `DUPLICATES=0`; `sa` `article` 12 rows (parts_read=2), `listing_hit` 19,811 rows (parts_read=21); R7 projection 0.0000 GiB against the 5 GiB bar.
- The CTO's two rulings that shaped the close: C-a4' (read the first uploading cycle) waived the real-upload clause, then closed at 14:41Z on hourly reads (msg 6655, amendment 3).

## 3. What is NOT established

- **`bbg` never uploaded under this pin.** Branch G fired (two jobs on one BP opinion article: 403 `bot_check` `bloomberg_press_and_hold`, then `TargetClosedError`; D1-S31 by SC1, D1-S32 mine, `ledger/ROUND87_BBG_BRANCH_G_PRESS_AND_HOLD_20261016.md`). Whether the page closure is the vendor's or the minimised window's is not measured. `bbg` collects nowhere now.
- **`wsj` and `barrons`** uploaded nothing in the window; their uploader path under the pin rests on the cb-13 pass. They wait behind `sa`: 22 of 242 `sa` jobs in 6 hours (AAPL and AMZN about 1 hour each), about 66 hours per cycle. The pass is serial by design.
- The `sa` `article` sample is 12 rows. The `sa` session is a person's sign-in; its expiry is a finding, no sign-in is attempted.
- Site Z's pin worktrees stay locked (not all four publishers report productive).

## 4. My errors, corrected in the record

The pair named `opal-data-assets` (the runner writes `opal-data-harvest`; erratum, CTO-ratified); `cb-9` step 5's gate was circular (SC1 caught it); `cb-12` called a date-key miss acceptable without reading the key (repaired by `cb-14`); `cb-15` step 5 said the `bbg` leg runs first in a pass when my own list put `wsj` first (found at the 07:56Z tick, repaired by the CTO's amendment 2 and my step 9); three surprise rows carry an estimated `surfaced_at` (`D1-S24`, `-S26`, `-S27`); one `cb15_c_a4.out` was written 66 minutes before the ordered point (disclosed, then rewritten at 14:41:17Z).

## 5. The rows

Mine and the seat's: `D1-S17` to `D1-S27`, `D1-S30` (disposes SC1 `D1-S28`), `D1-S32` (disposes SC1 `D1-S31`) -- all `OBSERVATION`/`INERT`, none armed. Worker rows `D1-W149-S1..S4` answered by `D1-S27`. **Carried open, not mine to close:** `D1-S25` (SC1: the uploader read -- now answered by the evidence above; the CVO may dispose it) and the CRO's `D1-S29` (three served-harvest defects). `comp-surprise --armed`: 0.

## 6. For the slug (candidates for the round-88 enrichment list; the CTO routes)

1. A per-leg job or time budget with rotation, so one slow publisher cannot starve the others (`sa` about 66 h per cycle).
2. The `bbg` challenge under the dell1 tab transport: measure which side closes the page; a handler that skips an article and does not end the job.
3. `D1-S29`: `IS_DIL_EPS_CONT_OPS` basis in the model block; the research-report-to-security attribution rule (KMB vs KIMBERA MM); ticker-exact precedence in `resolve` (PG vs PG&E).
4. The named increment: the `opal-harvest-security-metrics` typed read surface beside `scoped_amgt.py` (decomposition section 116, CTO option A).
5. FT (Andrew's own hand, later); an in-profile `sa` sign-in cell if the session expires.

-- 2.0.0_SA_COO~W1
