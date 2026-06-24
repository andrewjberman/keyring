# DATA_PLATFORM reverse-ETL — CHUNK-2: ALLOCATIONS (data-calibrated tier row)

**Lane:** 0.4.0_DS_ClientPlatform~B (2nd DS lane) · **Lead/integrator:** 0.4.0_DS_ClientPlatform (base, owns the unified tier table)
**Date:** 2026-06-24 · **Status:** chunk-2 COMPLETE — tier calibrated on live 2026-06-18 data, RAVC2 base-DS+COO+CTO (cc CVO/0.6.0)
**Frame:** base-DS v0.1 method/map/gradient — `docs/briefs/DATA_PLATFORM_reverse_etl_census_and_method_v0.1.md` (Parts 1-3 + Part-3 refinement)
**Diff question:** can BD's served `silver/allocations` be reproduced from the Schwab custodian-raw (RPS) we hold? Match -> T0/T1; not reproducible from Schwab-raw alone -> T2.

---

## HEADLINE REFRAMING (the load-bearing finding)

**BD `silver/allocations` is NOT an asset-allocation / position-MV breakdown. It is the BD ACCOUNT / RELATIONSHIP / ADVISOR-ATTRIBUTION / FEE-SCHEDULE DIMENSION** — one row per account (6,847 accounts, 92 columns, 2026-06-18). "ALLOC" = *advisor* allocation/attribution + the relationship rollup, NOT asset allocation. The file splits into two content classes with different tiers:

| Content class | Columns (of 92) | What it is | TIER |
|---|---|---|---|
| **Value** | 5: `account_market_value`, `cash_market_value`, `portfolio_group_market_value`, `account_allocation`, `cash_allocation` | account-grain MV + cash + fractional weights | **T1** (deterministic rollup of Schwab RPS positions + cash) |
| **Dimension / attribution / fee** | 86: relationship hierarchy (portfolio_group->relationship->portfolio->account), advisor splits (architect/implementor/consultant/local_ops + split %), fee schedules (basis_points, fee_schedule_*, flat_fee, billing), account config (tax_lot_methodology, tax_status, benchmark, goal, style, investment_strategy, registration, owner, rep_code) | firm-owned operational metadata | **T2-HOST** (see below) |

---

## TIER ROWS (data-calibrated — replace the hypotheses)

### Row A — allocation VALUE (account_market_value et al.): **T1 — deterministic rollup, custodian-reproducible**
Empirical diff, BD `account_market_value` vs Schwab RPS `market_value` rolled to account grain, **2026-06-18** (both ends live; joined via `gold/dimensions/schwab_bd_account_mapping`):

- **Aggregate (matched 5,427 accts):** BD $1,566.9M vs Schwab $1,562.4M = **net +0.29%** (essentially exact).
- **Per-account:** 94.5% within 5%; **99.3% within 1.0% after the deterministic cash adjustment** (BD MV includes account cash absent from the RPS position feed; median raw |pct_diff| 1.25%).
- **BD-over-Schwab overage fully deterministic/explainable, NOT computation IP:**
  - BD-only accounts (no Schwab map): **979 accts / $244.0M** = BD's universe is broader than one custodian's position feed (held-away / other-custodian / unmapped / closed).
  - Mapped-but-no-RPS-positions: 441 accts / $38.0M (cash-only / zero-position / closed).
  - `>5%` outliers (300 accts): **join-grain artifacts** — many-BD-to-one-Schwab mappings (e.g. BD `z0817527711` + `z0817527741` both joined to Schwab `0065559837` = $1.5M, double-attributed by the rollup). Not BD computation.
- **Verdict:** account MV is reproducible from Schwab-raw with deterministic repackaging + cash + the broader-universe delta. **Structurally already supplanted** — per the Part-3 refinement, our `positions_cube` (A_03) already sources positions Schwab-RPS-DIRECT (`schwab/silver/rps`), BD out of the loop for positions. Corroborates the 2026-03 ACAT_ALLOCATIONS_RECONCILIATION finding (same gap direction; same deterministic factors: pricing/dedup/settlement/status) on fresh data.

### Row B — relationship/portfolio rollups (`portfolio_group_market_value`, `account_allocation`, `cash_allocation`): **T1**
Deterministic rollups/weights (account share of its portfolio group) — derivable given the hierarchy + the account MVs. (`portfolio_group_market_value` is denormalized per-row; do not naive-sum.)

### Row C — dimension / attribution / fee (86 cols): **T2-HOST (firm-owned reference data BD *hosts*, NOT vendor-computed)**
This is the key supplant-blueprint nuance. These columns — advisor attribution (real names + split %: Travis Penfield, David Farrell, ...), the relationship/portfolio/household hierarchy, fee schedules, account config — appear in NO custodian feed (Schwab delivers positions/lots/transactions, not advisor splits or fee schedules). **But they are NOT vendor-COMPUTED IP either** — they are 49 Financial's own CRM / billing / org reference data that BD merely *hosts* as a system-of-record.
- **Supplant implication:** unlike a computed T2 (performance attribution, tax-lot optimization), there is **no algorithm to reverse-engineer** — supplant = **migrate the system-of-record** (own the firm's advisor/relationship/fee config, which the firm already owns). Materially LOWER supplant difficulty than computed-T2. **Recommend the blueprint distinguish T2-HOST (data-ownership/migration) from T2-COMPUTE (IP-replication).**

---

## CHUNK-4 BOUNDARY FLAG (coordination — base-DS + ~B chunk-4)
The **advisor-grouping + relationship/household hierarchy substrate lives in THIS allocations file** (architect/implementor/consultant splits; portfolio_group->relationship->portfolio->account). Chunk-4's T2 "household/relationship grouping + advisor grouping" analysis should treat `silver/allocations` as its primary substrate. Clean split: **chunk-2 catalogs the file + tiers its content (done here); chunk-4 characterizes the grouping METHODOLOGY** (how the relationship star is built / maintained, reproducibility) **+ performance attribution (C_03)**. No rework — chunk-4 builds on Row C.

---

## GROUNDING (Rule-22) + RESIDUALS
- **Mechanism (source-confirmed):** producer = BD DataMining `ALLOC_DAILY_*.xlsx` -> `convert_daily_allocation_to_parquet.py` / `merge-daily-allocation-incremental.py` (silver = snake_case + dedup on (account_id, as_of_date) ONLY; Rule-17 clean, no value transform). Graph: `comp-pipescript io B_00` / `A_03` (A_03 reads `silver/allocations <- external/silver` AND writes it -> B_00,B_01,C_02,C_04,D_04; the read+write of the same key is a rolling-window/enrichment pattern — immaterial to the tier since the allocation CONTENT originates from the BD export, source-confirmed).
- **State (served/live-grounded):** all diffs read LIVE S3 artifacts (`silver/allocations/2026-06-18`, `schwab/silver/rps/date=20260618`, `gold/dimensions/schwab_bd_account_mapping`) — not source/self-report.
- **Residuals / INFERRED:** (1) single primary diff date (2026-06-18) + the 2026-03 ACAT corroboration = 2 points; a 2nd-date spot-check would harden (low risk). (2) The `>5%` join-grain outliers are characterized, not de-duped (immaterial to the T1 verdict; the aggregate + cash-adjusted match is decisive). (3) **Scope = 49F/Schwab only** (the sole fully-diffable pair). cot/inf allocations are **bounded/INFERRED** (no custodian-raw below the vendor) — project the 49F-calibrated tiers per the census, flagged INFERRED until a custodian-direct feed lands.
- **comp-rail:** comp-which -> comp-pipescript io (routed); native source Reads; live data-access via boto3 (off-rail per Rule-21 row data-access). No raw repo-grep.
