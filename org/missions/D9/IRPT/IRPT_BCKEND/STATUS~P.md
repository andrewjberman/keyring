# IRPT_BCKEND~P (Performance, shared auth/routes/IaC/packaging) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE), `/canonical-drive 10m` (LIVE_ARMS RELAUNCH row, re-authorised by the 2026-09-30 13:0xZ post-crash
word). Workstream scope: shared auth, routes, IaC and packaging, plus Performance/Reporting; issuer of workstream ~E (CTO 102461).
Since 2026-09-30 14:0xZ this seat ALSO issues IRPT_DASHBD workstream B (Andrew's seating, PRD section 5) -- its state lives in
`org/missions/D9/IRPT/IRPT_DASHBD/`. As of 2026-09-30 ~17:0xZ. Earlier forms of this file are in git (the A2 freeze @025cef10fd).

## Standing Andrew words that govern this workstream (read first)

- **~22:2xZ call 3 (2026-09-28):** performance is end-of-day holdings only -- the weight-pro-rated daily price return of the securities
  held, no inflow/outflow logic (`ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md`).
- **~22:4xZ (2026-09-28):** every firm moves to that basis in ONE consolidated gold shape, run daily, verified at the vendors' periods
  (`ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md`).
- **~05:2xZ (2026-09-30):** precomputed gzipped JSON reporting under 2 s in each firm's gold/reporting home, asset-level after the
  architecture is proven; brief via the CRO (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_052xZ_PRECOMPUTED_GZIP_JSON_REPORTING_UNDER_2S_AND_PUSH_MANAGED.md`).
  That word became IRPT_DASHBD (PRD v0.2 @84cff9014b); this project's total-return narrowing is IRPT_DASHBD's, and IRPT_BCKEND's
  holdings gold is its guard rail (C-GUARD).
- **~04:3xZ (2026-09-30):** "the owner of YCharts is COO~Y as it has always been" (@fe6326f6b0). This seat does no YCharts or resident work.

## Served function -> live artifact (read at each move)

| Function | Live CodeSha256 | Applied (Z) | Source | Ledger |
|---|---|---|---|---|
| irpt-performance-adapter | `+h/AH/RY...` (S3 TBy0pL) | 09-29 16:40 | hD7G6YT1's source + installed.py @66469ce943 (49F reads the holdings gold; r3 re-switch) | irpt-adapter-holdings-gold-49f-r3-20260929 (D1 closed; A1 OPEN, waits on a SCHEDULED 49F producer fire that finds its silver -- row S235) |
| inf-ec2-launch-monitor | `t1QrzaDeMtjGgnFL0oez1DGtL6vLVz7fgV0/BMVuIQo=` | 09-30 16:19:48 | lambda_function.py @1431d66d9b (pr-242: an EMPTY stop reason is never suppressed) | inf-launch-monitor-empty-reason-served-20260930 CLOSED; a1-observation entry HELD on the next stop event (CTO 0386ab930c condition 4) |
| INF gold runner code | `code/silver/silver_ids.py` (byte copy of `lib/silver_ids.py`) + `code/silver/_orion_api_silver_lib.py` with the flat fallback import | 09-30 ~14:4xZ | @2e5173d3b6 on wk-IRPT_BCKEND-97 (pr-261) | inf-silver-ids-ship-20260930 CLOSED |
| irpt-holdings-performance-lambda (49F, scheduled 11:30Z Mon-Fri) | unchanged | -- | IB-er-203 | the 09-30 fire refused ABSENT: Schwab silver for 09-29 had not landed (S235) |

## Round 26 (~P) -- terminal, drain-end record `deliverables/2.0.0_SA_COO~P/IRPT_BCKEND_ROUND26_P_DRAIN_END_20260930.md`

| cell | state |
|---|---|
| IB-pr-261 (ship silver_ids, one real chain run) | COMPLETE @65144605a4 (WK~97; P26-1-AC1/AC2/AC3 PASS); the chain passes step 3 again, raw positions + transactions for 09-30 landed, then FAILS at step 33 INF_C_01 on the NNA coverage guard (row W97-S3, routed) |
| IB-pr-262 (the pr-242 served move) | APPLIED 16:19:48Z under both halves (packet @e0a2f524e4 blob 1bc65b9b16; CTO @0386ab930c) |
| IB-pr-263 (twr_daily two-partition fill) | SUPERSEDED @ed0be5b557 on row S236 (non-performance days by the producer's own rule) |

## The INF thread, honestly

The Inflection raw chain died at step 3 from 09-28 (the half-landed silver_ids deploy) and is repaired. It now dies at step 33 (the NNA
coverage guard needs a recorded excusal for accounts 866/769/1096; W97-S3). Independently, the ingest mirror and `opal-assets-silver-orion`
have not moved `fact_positions` past 09-27 on today's raw (read 16:3xZ), so S216 stays ARMED and the INF holdings producer and INF
adapter switch stay blocked. Round 27's cells: the API allowedFirmIds enforcement for service principals (CTO 103318, top), the
mirror/silver-orion diagnosis, the NNA excusal record once ruled.

## Open rows this seat holds (disarm owner)

S216 (ARMED; the mirror stage), W97-S3 (ARMED; routed to the CTO as a served-data decision), S237/S239 (ARMED; the retiring engine's
skipped-day flow error -- computed correctly in IRPT_DASHBD DB-b-1's face; no IRPT_BCKEND cell since the engine is retired for 49F
serving), W86-S2 (disarms on the held observation). S235 is placed with the CTO (the Schwab silver landing's owner is unnamed).

## Open ledger entries authored here (`org/critical_paths/.open_deploys/`)

irpt-adapter-holdings-gold-49f-r3-20260929 (A1 OPEN, past window; S235), inf-launch-monitor-empty-reason-a1-observation-20260930 (HELD
on the named event), and the six export/adapter A1 legs from 09-27/28 listed in the earlier form of this file (each closes on a live
walk's read; unchanged this session).

## Gates in force

- Every served zip: flat_zip_module_census + ~Y zip_module_census + a cold-start smoke BEFORE apply.
- A before/after read that DISCRIMINATES on the served surface, counting every reader of the served figure.
- Served moves need both never-widen halves at HEAD naming the packet blob; the ledger opens before the first write.
