# ADVI_ROLLUP.ORPHRELID — Session closeout log
# 0.4.0_DS_ClientPlatform — 2026-04-22
# Commit: e28e0f5d (CLOUD)

## Compiler Tools Run Log

| Step | Command | Observed | Pass? |
|------|---------|----------|-------|
| P0.1 | canonical_nna/2026-04-22.parquet orphan query | 20 orphans, $1.6M AUA (TO said 164 at EOP2025 -- date-specific) | PASS |
| P0.2 | comp-blast A_00 | "No nodes matching" (graph node naming mismatch; 17 consumers confirmed via comp-pipescript io) | OK |
| P0.3 | comp-pipescript io A_00 | READS external/silver -> WRITES 17 consumers (A_01, A_04, B_00, B_01, B_02, C_00, C_01, C_02, C_03, C_05, C_06, C_07, D_00, D_00b, D_01, D_04) | PASS |
| P1.1 | historical sweep (2025-12-31 through 2026-04-22) | Oscillation pattern: 167 orphans EOP2025, 13 persistent floor; 161 resolved Jan 2026 | PASS |
| P1.2 | cross-ref 20 today-orphans vs accounts_dimension_latest | 13 found; 3 sub-cohorts (4 missing, 7 rel_id=0, 6 valid-but-dim-lagged) | PASS |
| P1.3 | silver/accounts_dimension existence check | prefix absent; A_00 reads from BD txn parquet directly | PASS |
| P1.4 | AST scan A_00 relationship_id refs | L75 TXN_ACCOUNT_COLS, L453-455 normalization (strips None/nan/'' but NOT "0") | PASS |
| P1.5 | C_01 outer merge code trace | L218 joins gains-path; L238 outer merge for flow-only accounts bypasses acct_dim join (rel_id stays null) | PASS |
| P2   | N/A -- no A_00/B_00 code fix; trace-only + data-fix path chosen | — | SKIP |
| P3.1 | YAML parse: gold_validate_config.yaml | OK | PASS |
| P3.2 | comp-validate C_01c --artifact gold/canonical/role_aua/2026-04-17.parquet | 5 SKIP, 0 ERROR, exit 0 | PASS (AC#4) |
| push  | git push CLOUD | e28e0f5d pushed | PASS |

## Root-cause classification

PRIMARY: H1 (BD feed gap) -- AE scope
  - 4 accounts structurally absent from accounts_dimension (~$670K AUA persistent)
  - 2095 accounts with BD relationship_id="0" (unlinked sentinel)
SECONDARY: H4 (timing) -- self-resolving
  - ~150 EOP2025 orphans resolved by 2026-01-19 (new-account dimension lag)
CODE-CONTRIBUTOR (documented, not fixed): C_01 outer merge at L238 bypasses acct_dim join
  for flow-only accounts -- separate backlog item for CTO

## Deliverables shipped

1. data/black_diamond/diagnostics/ROLLUP/orphan_rel_id_trace.md -- AC#1+2+3
2. data/black_diamond/scripts/gold/gold_validate_config.yaml -- C_01c block -- AC#4

## Follow-on required

AE scope: CP-FEEDEXP-style TO to inquire with BD about 4 structurally-missing accounts:
  z0819052671, z0819070781, z0819926011, z0820769131 (~$670K AUA, persistent since EOP2025)
