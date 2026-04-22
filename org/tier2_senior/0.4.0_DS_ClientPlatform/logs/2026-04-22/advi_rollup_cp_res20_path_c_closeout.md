---
session: ADVI_ROLLUP CP-RES20 Path C Closeout
agent: 0.4.0_DS_ClientPlatform
date: 2026-04-22
task_order: ADVI_ROLLUP.CP-RES20.ds-chronic-zero-residual-20-account-cohort.md
status: complete (Path C)
commits: none (Path C = no code change)
---

## Session Context

CP-WP5 RAVC4 closed by COO (296b778e, all 8 ACs PASS). CP-RES20 GO issued by COO
(20260422T202524Z) with explicit Path C bias per $6M / $1.66B = 0.36% < Gate 2 band and
COO confirmation that positions_cube preliminary elimination tracked cleanly.

## Phase 1 — Empirical Gates

### Gate 1: silver/positions_cube freshness (Path B viability)

Run: `aws s3 ls s3://opal-data-bd/silver/positions_cube/ | tail -5`
Result: (no output — prefix does not exist)

Confirmation: `aws s3 ls s3://opal-data-bd/silver/` listed prefixes:
  allocations/, assets/, fees/, prices/, realized/, transactions/, transactions_enriched/, unrealized/
  NO positions_cube prefix.

Verdict: **silver/positions_cube ABSENT. Path B eliminated.**

`<if_mismatch>` trigger: silver/positions_cube is stale — eliminate Path B; choose A or C.
Action taken: Path B eliminated. Proceeding to A vs C decision.

### Gate 2: 5-account cohort coverage in positions_cube

Run: cohort coverage check
Result: N/A — positions_cube prefix does not exist. Gate 2 skipped (Path B already eliminated
at Gate 1, per TO `<if_mismatch>` logic).

### Gate 3: comp-blast B_01 (downstream consumer audit)

Run: `comp-blast build_holdings_lots`
Result:
  BLAST RADIUS: gold:B_01.holdings_lots:build_holdings_lots_snapshot
  GOLD_SCRIPT (31): all internal B_01 functions
  S3_ARTIFACT (6): silver/bd_assets_dim, gold/dimensions/schwab_bd_account_mapping,
    gold/dimensions/ticker_resolution, silver/unrealized/*.parquet, silver/allocations/*.parquet
  WARNING: 37 downstream nodes

Run: `comp-pipescript consumers B_01`
Result: B_01: no downstream pipeline consumers (terminal or portal-only)

Interpretation: B_01 output (gold/timeseries/holdings_lots/) goes directly to portal
(via bd-portal-publisher) and to B_01b/C_02/C_05 via S3 artifact path. The graph tracer
reports "terminal" because those downstream scripts are not captured as pipeline edges.
Manual knowledge: B_01b (classify), C_02 (canonical_lots), C_05 (tax_liability) all read
holdings_lots — any Path A stub would need filtering in all three.

Verdict: No new consumers beyond expected set. Gate 3 PASS. But Path A stub risk remains:
3 downstream scripts need `price_quality != 'allocation_stub'` filters before cost-basis/
classify/tax logic.

### Gate 4: comp-platinum reverse price_quality

Run: `comp-platinum reverse price_quality`
Result: "no portal component reads this field" — DIAGNOSTIC case [a]: genuinely new field,
not in portal dataflow index.

Interpretation: price_quality is a gold-layer field, not a portal-layer field. No portal
consumer would break. However, Path A risk still applies to gold-layer consumers (B_01b,
C_02, C_05). Gate 4 outcome is informational, not a blocker for Path C.

## Path Decision: C — Document as Feed-Boundary Residual

### Evidence summary

| Gate | Check | Result | Path B status | Path A status |
|------|-------|--------|--------------|--------------|
| 1 | positions_cube prefix exists | ABSENT | Eliminated | N/A |
| 2 | 5-account cohort in positions_cube | Skipped (B eliminated) | Eliminated | N/A |
| 3 | comp-blast B_01 consumers | 37 nodes (all internal/inputs); terminal re: pipeline | N/A | 3 downstream scripts need filter |
| 4 | comp-platinum price_quality | New field, no portal consumer | N/A | Gold-layer risk only |

### Decision rationale

1. Path B: Eliminated — positions_cube absent.
2. Path A: Feasible but cost-benefit unfavorable:
   - $6,013,161 / $1,660,263,546 = 0.36% — inside Gate 2 band
   - No real cost basis, no acquisition_date, no term for stub lots
   - B_01b, C_02, C_05 all need explicit `price_quality != 'allocation_stub'` guard logic
   - Distorts lot-level semantics without proportionate gain
   - COO directive: "bias toward Path C" confirmed in GO (20260422T202524Z)
3. Path C: Selected.
   - $6M residual within Gate 2 band — does not block any portal feature or nightly gate
   - Root cause is feed-boundary: accounts exist in silver/allocations but absent from
     silver/unrealized (custody feed coverage gap, not a gold script bug)
   - Correct fix is vendor/feed-expansion (AE pod), not a gold-layer synthetic stub
   - Firm non-cash gold MV at $1,660,263,546 is already within Gate 2 target band

## Compiler Tools

| Tool | Run | Result | Pass/Fail vs Expect |
|------|-----|--------|---------------------|
| aws s3 ls positions_cube | Gate 1 freshness | ABSENT (no prefix) | PASS (Path B eliminated per <if_mismatch>) |
| comp-blast build_holdings_lots | Gate 3 downstream consumers | 37 nodes internal; terminal re pipeline | PASS (no new consumers) |
| comp-pipescript consumers B_01 | Gate 3 confirmation | terminal or portal-only | PASS (consistent with expected) |
| comp-platinum reverse price_quality | Gate 4 portal consumer | Genuinely absent (new field) | PASS (informational; Path C no impact) |
| py_compile / ds-commit-gate | Phase 2 (no code change) | N/A — Path C, no script edit | N/A |
| comp-pipescript deployed B_01 | Phase 3 (no QA run) | N/A — Path C, no script edit | N/A |
| comp-validate B_01 | Phase 3 (no QA run) | N/A — Path C, no script edit | N/A |

## Path C Deliverables

### 1. Feed-expansion follow-on TO

Authored: `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_ROLLUP.CP-FEEDEXP.ae-silver-feed-expansion-res20-cohort.md`
Issued to: 0.6.0_AE_PartnerETL
Status: staged (P4 — informational, no portal gate)
Scope: BD data-ops inquiry + silver ingestion expansion for 20-account cohort

### 2. CP-RES20 TO status flip

File: ADVI_ROLLUP.CP-RES20.ds-chronic-zero-residual-20-account-cohort.md
Change: pending → complete (path_selected=C, completed_date=2026-04-22)

### 3. $6M residual documentation (inline)

Cohort: 20 accounts, all alloc_billable, all silver-invisible (0 rows in silver/unrealized)
Aggregate alloc_noncash: $6,013,161
Firm non-cash gold MV after CP-DS1: $1,660,263,546
Residual as % of firm: 0.36%
Gate 2 band: comfortably within (typical gate = ~2% tolerance)

Top accounts (full list in CP-FEEDEXP TO):
  z0820721041 — $2,000,000 | z0820721031 — $1,750,000 | z0814308771 — $519,815

Root cause: feed-boundary. Accounts appear in BD allocation export (silver/allocations)
but are absent from BD unrealized/positions snapshot (silver/unrealized). BD data-ops
investigation required to determine whether cash-only, newly onboarded, or custodian
exclusion.

## SL-P1 Nightly Check

Checked EventBridge rule `bd-gold-nightly-fallback`:
  State: ENABLED | Schedule: cron(0 23 ? * MON-SAT *)

SL-P0 decision memo: LOCKED (Path 3 cost-basis apportionment). Hard gate cleared.

Conclusion: nightly fallback is re-enabled. SL-P1 shadow emit will naturally fire tonight
at 23:00 UTC. First-fire artifact (gold/timeseries/holdings_lots_shadow/{date}.parquet)
expected tomorrow morning. Will report via RAVC after artifact confirmed.

## Current State

- CP-RES20: COMPLETE (Path C, no code change, $6M documented residual 0.36%)
- CP-FEEDEXP TO: authored, staged with AE (P4, vendor-coord dependency)
- SL-P1: nightly fires tonight 23:00Z (ENABLED confirmed) — first-fire report tomorrow AM
- INFLEC W4.9 C-chain: re-dispatch pending (I_A03 crashed, C-chain outputs MISSING)
- AUAGAP.002 D-chain: with AE, awaiting confirmation

## Next Steps

- [COO] MCP COMPLETE with CP-RES20 path + evidence + SL-P1 nightly state (this session)
- [AE] CP-FEEDEXP TO staged — pursue BD data-ops inquiry as capacity allows (P4)
- [DS] INFLEC A+C chain re-dispatch — skip I_A03, run C_02 → C_08
- [DS] RA-P1c execution — per CTO task order
- [DS] SL-P1 first-fire RAVC report — tomorrow AM after 23:00Z artifact confirmed
- [AE] AUAGAP.002 D-chain confirmation → DS portal validation Step 5
