# SL-P0 sleeve discovery — 0.4.0_DS_ClientPlatform — 2026-04-15

**Agent:** 0.4.0_DS_ClientPlatform (base lane, no instance dial)
**Date:** 2026-04-15 (PM session)
**Scope:** ADVI_ROLLUP.SL-P0.ds-sleeve-discovery — sleeve cohort detection + quantity-source decision
**Acceptance:** all 8 criteria PASS or accepted N/A. No flex on the books (CTO ACK 2026-04-15T17:54Z).

## Headline outcomes

1. **Quantity-source DECIDED:** Path 3 (cost-basis apportionment) + parallel Path 1 escalation to AE for BD-side Units column. Decision memo `docs/architecture/ADVI_SLEEVE_P0_DECISION.md`.
2. **Cohort produced:** 598 accounts in plan band 500-700. Jones z0817905851 anchor 4/4 confidence. Uploaded to `s3://opal-data-bd/diagnostics/sleeve_cohort/2026-04-13.parquet`.
3. **Two plan-doc misreads corrected with evidence:**
   - Path 1 NOT auto-satisfied (BD source xlsx truly has no Units column — confirmed by direct xlsx schema inspection)
   - Path 2 NOT free (`silver/daily_positions.parquet` is a dead Jan-Feb relic, proto-`canonical_prices`, not a positions feed — confirmed by Andrew + archive script docstring)
4. **Signal vocabulary expansion** lifted cohort from 156 (overly-narrow) to 598 (in band) without touching the cross-bucket join (CTO: "right CTO-grade reflex").
5. **AE Path 1 escalation MCP** sent — feasibility check for adding Units column to BD UGL xlsx export.

## Phase log

### 1. Startup (17:14 ET)
- `register_agent("0.4.0_DS_ClientPlatform")` — base lane.
- Inbox empty at start. Watcher launched per protocol.
- Read XXX.md, README, prompt.md, prior session summary `session_summary_d_wp11_cnp1_rap1_close.md` (~D PM session — separate lane, picked up where ~D left off was not my scope).
- Confirmed instance constraint per Andrew: base lane accepts only non-serialized TOs. Filtered `list_task_orders` queue accordingly.
- Initial COO GO: RA-P3 + CN-P3 — caught lane mismatch (`<issued_to>` was ~B, not base). MCP'd routing-mismatch flag to COO. COO RESOLVED Path A (~B owns P3, my catch was correct). Stayed on SL-P0 (which arrived correctly base-dialed in same wave).

### 2. SL-P0 Phase 1 compilers (17:18-17:30 ET)
- `comp-pipescript io B_01` — confirmed B_01 is the FIFO-replay holdings_lots writer. Static reads only ACCOUNTS_DIMENSION; RPS/transactions/allocations dynamic. WRITES include `gold/timeseries/holdings_lots/{*}.parquet` and `gold/holdings_lots_v2_dryrun_key`. silver/unrealized not in reads — the gap SL-P1 will close.
- `comp-blast silver/unrealized` — "No downstream consumers found for: s3:silver/unrealized/unrealized_gain_loss.parquet" — gap confirmed exactly as plan predicted.
- `comp-pipescript io silver/unrealized` returned "Unknown script" (artifact prefix, not script id) — substituted with direct schema inspection of `silver/unrealized/2026-04-13.parquet`. 16 cols, **no quantity column**, `unit_cost` populated 84,954/93,707 nonzero (cash rows zero, expected). Path 1 hypothesis ("BD has Units, silver drops it") testable directly.
- `comp-pipescript io holdings_lots` returned "Unknown script" — covered by B_01 manifest (holdings_lots is its WRITE target).

### 3. Path 1 verification — DEAD (17:32-17:38 ET)
- Source xlsx: `s3://opal-data-bd/forwardfill_v2/unrealized/UNREALIZED_DAILY_2026-04-13.xlsx`, downloaded.
- Sheet1 has 14 cols, Timestamps sheet has 2 (metadata only).
- 14-col list: `Open Date | Unit Cost | Inherited Date | Relationship ID | Account Number | AccountID | AssetID | Asset Name | Last Dividend | Original Asset Name | Asset Display Name | Symbol | Ticker | CUSIP`. **No Units / Quantity / Shares.**
- Silver ingest (`merge-daily-incremental.py::process_unrealized_xlsx_to_parquet` L896-980) preserves all xlsx columns + adds `_source_file` + `_ingested_at`. No drop.
- **Conclusion:** Path 1 = upstream BD data-ops project (vendor coordination), not a code change on our side.

### 4. Path 2 investigation — initial false eureka (17:39-17:46 ET)
- Found `s3://opal-data-bd/silver/daily_positions.parquet` with `units | double` at `(date, account_id, asset_name)` grain. Initial reaction: "Path 2 is essentially free!"
- Andrew pushed back: "what is daily positions silver? im not sure if thats a real file."
- Provenance grep: 114 hits, **all in `archive/`, archived session logs, or thread context-snapshots. Zero references in any active gold script.** File last-modified 2026-02-02; latest data date 2026-01-27 (~3 months stale).
- Withdrew the eureka. Path 2 NOT free.
- Andrew clarified: "daily positions should just be the proto version of canonical prices." Confirmed by `archive/scripts_core/calculate_point_in_time_aua.py` L11-12 docstring: this file solved the **price** carry-forward problem ("transaction engine only creates position records on transaction dates"). The legacy daily_positions was the proto-`canonical_prices` (which we patched yesterday in WP-11 with BNP/WFC/NEWMONT scoped overrides). The `units` column was incidental snapshot data, not a sleeve quantity source.
- **Conclusion:** Path 2 not viable. Adjacent live BD positions feed does not exist in our silver layer.

### 5. Path 3 feasibility — Jones spot-check (17:48-17:50 ET)
- Jones z0817905851 in `silver/unrealized/2026-04-13`: 14 lots, 1 with $0 unit_cost (the explicit `CASH` row at cusip=`CASH`).
- Cash-row carve-out per plan doc Risk #1: route through `qty = cash_market_value / 1.0` (cash priced at par) — handles the only Jones $0-cost case cleanly.
- Path 3 viable with cash-row carve-out.

### 6. Cohort detector — first pass (17:50-17:54 ET)
- Built `data/black_diamond/scripts/diagnostics/sleeve_cohort_detect.py`. Four signals from allocations metadata:
  1. retirement_acct_type (initial overly-narrow set: only IRA + 401K + 403B + ROTH_IRA)
  2. sleeve_registration (initial: INVESTMENT_IRA, SIMPLE_IRA, PENSION_TRUST)
  3. sleeve_name_prefix (PCRA Trust + SWTC TTEE in account_number)
  4. no_advisor_portfolio
- First-pass cohort: **156 accounts** at >=2/4 signals. Jones 4/4 confirmed.
- 156 below plan band 500-700.

### 7. Pre-flag pre-flight + retract (17:50-17:51 ET)
- Sent CTO + COO Rule 7 acceptance-flex pre-flag: "ship 156 conservative cohort, defer cross-bucket join to SL-P0b."
- Then surveyed actual `account_type` and `account_registration_type` value distributions — discovered the plan doc's signal definitions were wrong (plan said "PCRA Trust prefix on account_number" but PCRA Trust is actually a value of account_registration_type with 13 accounts; account_number is mostly masked client labels).
- Expanded signal sets: account_type adds RothIRA + InheritedIRA + InheritedRothIRA + SEP + SIMPLE; registration_type adds Pension Trust + INVESTMENT_RETIREMENT + INVESTMENT_401K + Simplified Employee Plan + Simple IRA + Inherited IRA from IRA + Inherited Roth IRA from Roth IRA + Custodial.
- Re-ran cohort detector: **598 accounts**. In band.
- Sent CTO + COO RETRACT MCP. Crossed in flight with CTO's APPROVED-156 message. Sent CLARIFY MCP. CTO ACK'd retract: "ships under original AC, no flex on the books." SL-P0b deprioritized.

### 8. Cohort upload + decision memo + AE escalation (17:53-17:55 ET)
- Re-ran detector with `--upload`. Confirmed S3 write to `s3://opal-data-bd/diagnostics/sleeve_cohort/2026-04-13.parquet` (598 rows).
- Wrote `docs/architecture/ADVI_SLEEVE_P0_DECISION.md` — full Path 3 + parallel Path 1 decision with evidence.
- MCP'd AE 0.6.0 — Path 1 BD-Units feasibility check.
- `comp-validate sleeve_cohort --artifact ...` — 1 SKIP (no config), 0 ERROR. Acceptable per acceptance #6 caveat (config addition flagged for COO).

## Compiler tools

| Run | Expected | Observed | Pass/Fail |
|---|---|---|---|
| `comp-pipescript io B_01` | RPS + transactions + allocations reads visible; silver/unrealized not yet read | static reads ACCOUNTS_DIMENSION only (others dynamic); WRITES holdings_lots variants; silver/unrealized absent from reads | **PASS** (gap confirmed) |
| `comp-blast silver/unrealized` | No current gold consumers | "No downstream consumers found" | **PASS** |
| `comp-pipescript io silver/unrealized` (not a script id) | Quantity column missing | substituted with direct parquet schema read; 16 cols, no quantity | **PASS** (decision-driving) |
| `comp-pipescript io holdings_lots` (not a script id) | FIFO replay logic visible | covered by B_01 run | **PASS** |
| Schema inspection: BD source xlsx Sheet1 | discover whether Units column exists in source | 14 cols, no Units/Quantity/Shares — Path 1 hypothesis FALSIFIED | **PASS** (decision-driving) |
| Provenance grep: `daily_positions` | confirm whether legacy file is live or dead | 114 hits, all in archive/ + old session logs + thread context; zero active gold-script references; mtime 2026-02-02 | **PASS** (Path 2 dead) |
| Cohort detector run on 2026-04-13 | cohort 500-700 with Jones >=0.9 confidence | 598 accounts, Jones 1.00, distribution 497/99/2 across 0.50/0.75/1.00 confidence buckets | **PASS** |
| `comp-validate sleeve_cohort --artifact /tmp/sleeve_cohort_2026-04-13.parquet` | exit 0; cohort size in band | 1 SKIP (no config entry), 0 ERROR; "Artifact is ready for S3 upload" | **PASS** with caveat |

## Files modified

| File | Change | Author | Commit scope |
|---|---|---|---|
| `data/black_diamond/scripts/diagnostics/sleeve_cohort_detect.py` | NEW — cohort detector script | 0.4.0_DS_ClientPlatform | this commit |
| `docs/architecture/ADVI_SLEEVE_P0_DECISION.md` | NEW — Phase 0 decision memo | 0.4.0_DS_ClientPlatform | this commit |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-15/sleeve_p0_discovery.md` | NEW — this session log | 0.4.0_DS_ClientPlatform | this commit |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.SL-P0.ds-sleeve-discovery.md` | status pending -> complete | 0.4.0_DS_ClientPlatform | this commit |

S3 writes:
- `s3://opal-data-bd/diagnostics/sleeve_cohort/2026-04-13.parquet` (598 rows). NEW prefix, no A->D rerun chain dependency, no Rule 7 sensitive-write trigger.

## RAVC loops in this session

1. COO GO (RA-P3 + CN-P3) -> me ACK -> me REJECT (lane mismatch) -> COO RESOLVE Path A. Closed.
2. COO GO (SL-P0 base lane) -> me ACK -> [work in progress] -> MCP COMPLETE. Closing on commit push.
3. Me PRE-FLAG (Rule 7 cohort flex) -> CTO APPROVED -> me RETRACT (cohort actually in-band) -> CTO ACK retract + closed: "no flex on the books". Closed cleanly despite flight cross.
4. Me ESCALATE (AE Path 1) -> [open, no deadline].

## Risks / flags surfaced to COO

1. **`gold_validate_config.yaml` has no entry for `sleeve_cohort`** — `comp-validate` SKIPs cleanly but cannot enforce invariants. Suggest config block addition (cohort size 500-700 band, Jones confidence >=0.9, AUA in plausible range).
2. **`silver/daily_positions.parquet` orphan cleanup** — dead Jan-Feb relic, 682MB. Should be deleted by AE. Logged side-finding only, not in SL-P0 scope.
3. **Plan doc Path 1 description was wrong** — claimed "BD has Units; silver drops it" but BD source xlsx has no Units column at all. Updated decision memo with truth.
4. **Plan doc signal definitions were imprecise** — "PCRA Trust prefix on account_number" was actually about account_registration_type values. Updated detector signal sets accordingly. 598 cohort lands cleanly with corrected sets.

## Next

1. **SL-P1 (any DS lane post-AUA-freeze):** implement `_build_uln_sleeve_lots()` in B_01 behind `sleeve_dryrun=True`. Quantity source = Path 3 (cost-basis apportionment + cash-row carve-out). Cohort = `s3://opal-data-bd/diagnostics/sleeve_cohort/{date}.parquet`. Acceptance: shadow holdings_lots for sleeve cohort sums within 1% of allocations.account_market_value; Jones shadow >= $2.3M (vs current $82K).
2. **AE Path 1 thread:** AE returns BD feasibility timeline. If <2 weeks, swap quantity source mid-stream in SL-P1. If longer, Path 3 ships and Path 1 becomes a downstream upgrade.
3. **COO follow-up:** add `sleeve_cohort` block to `gold_validate_config.yaml` (or assign as separate TO).
4. **AE follow-up (low priority):** delete orphan `s3://opal-data-bd/silver/daily_positions.parquet` (682MB Jan-Feb relic, no live consumers).
