# IN-1 incremental-runs feasibility survey — 0.4.0_DS_ClientPlatform — 2026-04-15

**Agent:** 0.4.0_DS_ClientPlatform (base lane)
**Date:** 2026-04-15 (PM session, immediate after SL-P0 close)
**Scope:** ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey — per-script feasibility audit
**Acceptance:** 7 of 7 criteria PASS (commit pending).

## Headline outcomes

1. **Survey complete: 27 production gold scripts inventoried** (S/A/B/C/D layers; E_* diagnostics excluded per TO scope).
2. **Verdicts: 11 ELIGIBLE, 12 CONDITIONAL, 4 INELIGIBLE.** Today's `--incremental` whitelist is only A_00 + C_06; survey identifies 9 more candidates.
3. **5-wave incremental rollout plan** with effort estimates and inter-wave dependencies.
4. **Top-3 priority recommendation:** D_02 (22m wall, biggest payoff), A_03 (565s wall, lowest-risk first conversion), B_01 (1362s wall, highest design effort).
5. **6 cross-cutting design questions surfaced for IN-2 PRD** — watermark convention, merge strategy, parity validator (critical for B_01 FIFO state), rollback, chain-wave coupling, dispatcher hygiene gating.
6. **Surprising finding flagged:** B_01 has back-edge into ACCOUNTS_DIMENSION (re-emits A_00's output) — incremental skip would stale 16 downstream consumers. Wave-4 design must address.

## Files written

| File | Purpose |
|---|---|
| `docs/analysis/2026-04-15_incremental_runs_feasibility.md` | Human-readable memo |
| `docs/analysis/2026-04-15_incremental_runs_feasibility.json` | Machine-readable per-script + waves + concerns |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-15/in1_incremental_feasibility_survey.md` | This session log |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey.md` | Status flip pending -> complete |

## Compiler tools

| Run | Expected | Observed | Pass/Fail |
|---|---|---|---|
| `ls .../gold/ \| grep -E '^[A-Z]_[0-9].*\.py$' \| sort` | enumerate gold scripts | 27 production (incl. S_00 = build_canonical_prices_v2.py per gold_dispatch.sh L127) + 24 E_* diagnostics excluded | **PASS** |
| `comp-pipescript io D_02` | I/O graph for highest-cost script | 16 reads (broad upstream), 4 writes (per-entity JSONs identified as append-friendly target) | **PASS** |
| `comp-pipescript io B_01` | I/O graph | 1 static read + dynamic; 4 writes incl. surprising back-edge to ACCOUNTS_DIMENSION (Wave-4 design issue flagged in memo) | **PASS** |
| `comp-pipescript io C_06` | I/O for sole DOWNSTREAM incremental script | 9 reads incl. CLIENT_TIMESERIES_WATERMARK; 2 writes (per-client JSONs); confirms reference implementation | **PASS** |
| `comp-pipescript feeds D_02` | upstream dependency tree | 7 artifacts from 6 scripts (A_01, A_02, A_04, C_03, C_05, C_07); informs Wave 3 grouping | **PASS** |
| Batched `comp-pipescript io <each remaining>` | full inventory | A_00..A_04, B_00..B_03 + B_01b, C_00..C_08, D_00..D_04 + D_00b/D_00c (24 batched) — each WRITES list classified | **PASS** |
| Read `gold_dispatch.sh` for `--incremental` whitelist | identify currently-incremental | L232-236: only A_00 and C_06; all others stripped | **PASS** |
| Read `gold_pipeline_deps.yaml` | post-step + precondition map | S_00 -> inject_scoped_overrides.py blocking; D_01 + D_00b need dim_advisor_office.csv; B_00 needs canonical_prices | **PASS** |
| Read AE walltime baseline | per-script timing | full table reproduced in memo from `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-15/full_chain_recovery_b01_namerror_fix.md` | **PASS** |
| `jq -r '.scripts[].id' ... \| sort` vs disk id list | empty diff (Phase 2 acceptance gate) | empty after CRLF normalization (dos2unix); 27 IDs match exactly | **PASS** |
| `jq '[.scripts[] \| select(.verdict == "ELIGIBLE")] \| length'` | non-zero (Phase 2 acceptance gate) | 11 | **PASS** |

## Acceptance criteria status

| # | Criterion | Status |
|---|---|---|
| 1 | Memo + JSON sidecar exist | **PASS** |
| 2 | Every script under gold/ (S/A/B/C/D) listed; none skipped | **PASS** — 27/27 |
| 3 | Cross-script dep map cites comp-pipescript output for D_02/B_01/C_06 | **PASS** — full I/O blocks reproduced + feeds D_02 in dep map section |
| 4 | Priority ordering cites AE wall-time table; top-3 ELIGIBLE clear effort+risk | **PASS** — D_02 (L), A_03 (M), B_01 (L); citations to AE log |
| 5 | Cross-cutting concerns lists at least 4 IN-2 design questions | **PASS** — 6 surfaced |
| 6 | Session log Compiler Tools reproduces every run | **PASS** — this section |
| 7 | MCP COMPLETE to COO with memo path + JSON path + top-3 priority recommendation | **PASS** on commit close |

## Risks / flags surfaced to COO

1. **B_01 back-edge into ACCOUNTS_DIMENSION** — B_01 re-writes accounts_dimension_latest.parquet (A_00's output prefix) as RPS injection side effect. Wave-4 design must address: either remove back-edge (move classification upstream) or have B_01 incremental still emit dimension write even when FIFO replay skipped.
2. **D_02 RSS pressure** (per AE incident: 14 GB during 5b relationship timeseries) — performance regression candidate worth pairing with the Wave-3 incremental conversion pass to harvest both wins.
3. **D_01 incremental gated on ADVI_CANNNA convergence** — current D_01 partner_analytics shape is being reshaped by Wave 4 CN-P*; defer Wave-5 D_01 work to post-CN-P5 to avoid double-implementing.
4. **Dispatcher hygiene as IN-2 prerequisite** — per AE 2026-04-15 audit (gold-dispatcher-hygiene-cleanup TO HARD-GATED on chain close): dispatcher has 8 real bugs + 6 logic traps. IN-2 should NOT layer incremental capability onto an unhygienic dispatcher.
5. **No parity validator exists today** — proving "incremental output == full-rebuild output" is not a checked invariant. Critical for B_01 FIFO state correctness. Without this, Wave 4 is ungated and risks silent corruption.
6. **C_04 validate_aua marked INELIGIBLE intentionally** — must run every chain to certify outputs. Incremental does not apply.

## Next

1. **MCP COMPLETE to COO** with commit hash + memo path + JSON path + top-3.
2. **CTO** — IN-2 PRD authoring per claim. CTO will run additional compiler mandates (comp-pipescript io for every ELIGIBLE script depth + comp-pipescript overlap for cross-script dep map verification + comp-blast per affected artifact).
3. **COO** — IN-3+ implementation TO decomposition post IN-2 lands. First implementation TO recommendation: A_03 (lowest-risk path to validate watermark + skip pattern before tackling B_01 / D_02).

## RAVC loop

- COO GO (IN-1) -> me ACK 22:00:23Z -> [work in progress] -> MCP COMPLETE on commit push. Closing on commit.
