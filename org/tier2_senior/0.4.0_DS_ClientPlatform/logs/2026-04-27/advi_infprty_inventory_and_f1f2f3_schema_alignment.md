# Session Log — 0.4.0_DS_ClientPlatform~A — 2026-04-27

**Lane:** ~A (tilde lane; base lane `0.4.0_DS_ClientPlatform` ran SCOPEFIX work in parallel)
**Projects:** ADVI_RDVSDS (Phase 1 follow-up — advisor data unblock), ADVI_INFPRTY (NEW — DS+DE BD/49F vs Inflection field-set parity reconciliation)
**Drivers:** Andrew direct directive (16:35Z PRIORITY DISPATCH; 17:24Z ADVI_INFPRTY framing; 18:07Z F1-F3 priority override)

---

## Summary

Three sequential work items, all driven by user-visible Inflection advisor panels being blank in the portal:

1. **Inflection advisor S3 audit + I_D03 root-cause fix** (commits `345d6e3c`, `9f98dc46`). 9 advisor `book.json` + `composition.json` files now LIVE in `s3://opal-data-inf/platinum/advisors/`.
2. **DS-side data inventory** for the new ADVI_INFPRTY project (commit `7d28f000`). 385-line `INFLEC_DATA_INVENTORY.md` covering bronze/silver/gold/platinum schemas, 27-script catalog, advisor-mapping topology, Orion vs BD field-set deltas, answers to DE's 10 open questions.
3. **F1+F2+F3 platinum schema alignment** (commit `f4cabe05`). Restructured `leaderboard.json`, `partner_analytics_*.json`, `header_metrics.json` to match portal TypeScript contract. Re-validation gate cleared for RD 0.4.2.

Joint INFLEC_BD_PARITY_MATRIX.md v0.1 authored by DE (commit `5dfa6a12`) using my data-side verdicts; v0.2 review pass remains open.

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/D_02.advisor_client_detail.py` | Added `load_account_team()` + `_PLACEHOLDER_KEYS`; `build_advisor_books()` now sources advisor mapping from `gold/views/account_team.parquet` (replaces empty `rep_bucket=='individual'` filter); `build_client_details()` overrides placeholder advisor_key per account from account_team. (Commit `345d6e3c`) |
| `data/orion/scripts/gold/I_D03.composition_artifacts.py` | v1: switched per-advisor architect derivation from `rel_architect_lookup` (relationship_id keyed) to `account_team` (account_id keyed); placeholder filter added. v2: switched holdings source from `gold/holdings/` (759 firm-placeholder accounts only) to `gold/canonical/holdings_*.parquet` (35,087 rows × 2,755 accounts × 11 advisor_keys, advisor_key already enriched); `asset_name` fallback prefers `product_name`. (Commits `345d6e3c`, `9f98dc46`) |
| `docs/architecture/INFLEC_DATA_INVENTORY.md` | NEW — 385-line DS-side data inventory for ADVI_INFPRTY parity reconciliation. (Commit `7d28f000`) |
| `data/orion/scripts/gold/D_00c.portal_leaderboard.py` | F1: added `_aua_growth_pct()` + `_compute_new_clients_per_advisor()` helpers; `compute_leaderboard_entries()` emits per-entry `role_breakdown` (degenerate `{rep: EmployeeRoleBreakdown}` for individual advisors, `{firm: ...}` for firm bucket), `new_clients` (households whose `first_trade_date` falls in window), `aua_growth_pct` (computed from existing `total_aua`/`period_start_aua`), `primary_role`. Summary now carries `total_new_clients`, `positive_nna_count`, `negative_nna_count`. (Commit `f4cabe05`) |
| `data/orion/scripts/gold/D_04.client_portal_summary.py` | F3: `build_header_metrics()` rewritten — flat 245-byte scalar replaced with nested `total: HeaderTotal {aua, nna_mtd, nna_qtd, nna_ytd, nna_12m, client_count, account_count, new_client_*, q0..q3 QuarterlyNNA}` + `dates.{q0..q3}` + `firm_name` + `radial_12m` (NMNC/NMEC/Existing 3-segment from `first_trade_date`) + `account_distribution`. `by_architect: []` (DROP per matrix). Legacy flat fields preserved. New helpers: `_quarter_bounds`, `_quarter_nna`, `_window_nna_sum`, `_build_radial_12m`, `_build_account_distribution`. F2: `build_partner_analytics()` rewritten — flat `rows[]` replaced with nested `views.{aua,nna,geo,adv}.{donut,distribution,metrics}` per portal `PartnerAnalyticsResponse`. `views.aua` populated from holdings + accounts_dim NMNC/Existing cohort split; `views.nna.current` populated; `views.geo`/`adv` schema-valid empty stubs (per matrix DROP). `ofc`/`cla` intentionally omitted. `periods.current` + `firm_name` + `geo_aua_grain` added. Legacy `rows[]` preserved. New helpers: `_empty_partner_analytics_view`, `_empty_nna_view`, `_build_aua_view`. (Commit `f4cabe05`) |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Data inventory | `docs/architecture/INFLEC_DATA_INVENTORY.md` | DE (joint matrix), future Inflection panel TO authors |

(No `docs/briefs/` files written this session — all DS-side work landed as architecture docs / commits / direct MCP messages.)

---

## Compiler Tools

| Tool | Run | Result |
|------|-----|--------|
| `.tools/ds-commit-gate.sh` (D_02 + I_D03 v1) | Before commit `345d6e3c` | PASS — py_compile + AST + ruff all clean for both files |
| `.tools/ds-commit-gate.sh` (I_D03 v2) | Before commit `9f98dc46` | PASS |
| `.tools/ds-commit-gate.sh` (D_00c + D_04, F1+F2+F3) | Before commit `f4cabe05` | PASS for both files |
| `comp-pipescript io <script>` | NOT run | Comp-tools graph builder is BD-focused; Inflection scripts in `data/orion/scripts/gold/` are not yet indexed (ADHC_COMPIL.001 is the in-flight project to extend it). Verified field-deps via direct script reads + parquet schema dumps instead. |
| `comp-pipescript deployed <script>` | NOT run | Same — Orion runner not yet indexed. Verified S3 ETags via `aws s3api head-object` post-upload, and confirmed AE chain ran by polling `platinum/firm/*` size + LastModified. |
| `comp-validate <script> --artifact` | NOT run | No `gold_validate_config.yaml` rules currently match these specific publishers for INFLEC. Spot-checked output schema directly via `aws s3 cp - | python3 -c json.loads`. |
| Manual schema spot-check (post-AE chain) | `aws s3 cp - | python3 ...` on `leaderboard.json`, `header_metrics.json`, `partner_analytics_quarterly.json` | All three PASS — `entry.role_breakdown` is dict; `total: HeaderTotal` nested with q0..q3 QuarterlyNNA; `views.aua.donut.segments` populated with NMNC + existing cohorts |

`org/compiler-tools-log.md` not appended — gate runs auto-log via `.comp-graph/.agent_context` if configured; no comp-* tool was run beyond the gate.

---

## Commits

| SHA | Subject | Author |
|-----|---------|--------|
| `345d6e3c` | fix(ADVI_RDVSDS): D_02 + I_D03 advisor mapping via account_team for INFLEC | 0.4.0_DS_ClientPlatform~A |
| `9f98dc46` | fix(ADVI_RDVSDS): I_D03 switch to canonical/holdings_* (already has advisor_key) | 0.4.0_DS_ClientPlatform~A |
| `7d28f000` | doc(ADVI_INFPRTY): INFLEC_DATA_INVENTORY.md v0.1 (DS-side parity input) | 0.4.0_DS_ClientPlatform~A |
| `f4cabe05` | fix(ADVI_INFPRTY): F1+F2+F3 platinum schema alignment for INFLEC | 0.4.0_DS_ClientPlatform~A |

All four pushed to `origin/CLOUD`. Commit `--only` pattern + author serial used per CLAUDE.md Rule 14a (no shared-index sweeps).

---

## S3 Uploads (DS-direct per CLAUDE.md Rule 13)

| File | S3 key | Size | ETag | Modified |
|------|--------|------|------|----------|
| D_02.advisor_client_detail.py | `s3://opal-data-inf/code/gold/D_02.advisor_client_detail.py` | 20,016 B | `04af08652e479f598e16989349dd0eb7` | 16:47:57Z |
| I_D03.composition_artifacts.py (v1) | `s3://opal-data-inf/code/gold/I_D03.composition_artifacts.py` | 15,507 B | `68d9719f8115a9c11bb570dc7ceaefe9` | 16:47:59Z |
| I_D03.composition_artifacts.py (v2) | same key (overwrite) | 16,377 B | `32b6f8755e993f8525f18d097e3118de` | 17:02:19Z |
| D_00c.portal_leaderboard.py | `s3://opal-data-inf/code/gold/D_00c.portal_leaderboard.py` | 24,907 B | `5854e80395e252ddc25fb55ab3260739` | 18:48:18Z |
| D_04.client_portal_summary.py | `s3://opal-data-inf/code/gold/D_04.client_portal_summary.py` | 39,602 B | `9520a6acf6630473293d5de4827ba31e` | 18:48:23Z |

---

## RAVCs Sent

| When | To | Step | Subject |
|------|----|------|---------|
| 16:36Z | 2.0.0_SA_COO | step 2 | RAVC2 ACK — Inflection advisor data audit, starting now |
| 16:41Z | 2.0.0_SA_COO + 0.6.1_AE_PartnerETL | step 4 | RAVC2 — audit findings (per-advisor data MISSING; root cause D_02 rep_bucket filter) |
| 16:48Z | 0.6.1_AE_PartnerETL | step 2 | RAVC2 ACK — D_02 + I_D03 v1 patches shipped, dispatch ready |
| 17:02Z | 0.6.1_AE_PartnerETL | step 4 | RAVC2 — I_D03 v2 fix ready (canonical/holdings source switch) |
| 17:31Z | 0.6.1_AE_PartnerETL | clarification | etag mismatch + 6-step plan disambiguation (base lane vs ~A) |
| 17:46Z | 0.4.0_DE_ClientPlatform | step 1 | Initiated DS+DE parity reconciliation per Andrew directive |
| 17:49Z | 0.4.0_DE_ClientPlatform | step 4 | RAVC2 — INFLEC_DATA_INVENTORY.md v0.1 shipped, answers to 10 open questions |
| 18:39Z | 2.0.0_SA_COO | step 2 | RAVC2 ACK — F1+F2+F3 schema fix scope, starting |
| 18:48Z | 0.6.1_AE_PartnerETL | step 4 | RAVC2 — F1+F2+F3 ready, dispatch `--single D_00c` then `--single D_04` |
| 18:59Z | 2.0.0_SA_COO | step 4 | RAVC4 — F1+F2+F3 LIVE, platinum/firm/* shapes verified, RD gate cleared |
| 19:00Z | 0.4.2_RD_AdvisorIntelligence | dispatch | GATE CLEARED — re-validation can proceed |

---

## Memories Saved

| File | Reason |
|------|--------|
| `memory/project_inflec_bd_parity_reconciliation.md` | Standing constraint — Orion field ceiling vs BD/49F; DS+DE must produce parity matrix per panel before porting any new BD-pattern frontend. Andrew directive 2026-04-27. |
| `memory/feedback_inbox_watch_always_running.md` | Andrew called this out twice in session — relaunch inbox-watch IMMEDIATELY in same turn on every task-notification exit, before any other tool call. Hard rule. |

---

## Critical Findings

### Inflection advisor mapping topology (this session crystallized it)

Inflection silver layer carries firm-placeholder `advisor_key` only on `transactions` and `accounts_dim` (pre-SCOPEFIX-broaden). Real per-advisor mapping lives in:

- `silver/aum_snapshot.parquet` (household-keyed, 11 advisor_keys = 9 individual + 2 placeholders)
- `gold/views/account_team.parquet` (account-keyed, materialized by C_07 from aum_snapshot ↔ accounts ↔ households)
- `gold/canonical/holdings_*.parquet` (account-keyed with advisor_key + rep_bucket already enriched by B_00)

This is a structural difference from BD where silver carries advisor mapping per-row natively. Today's three incidents all root-cause to scripts reading silver expecting per-row advisor_key:

- D_00c `account_count=0` for leaderboard (fixed earlier in commit `0233aee1` by base lane)
- D_02 `0 advisor books written` (fixed in `345d6e3c` ~A)
- I_D03 `0 advisor compositions` (root cause was source-prefix mismatch, NOT placeholder filter — fixed in `9f98dc46` ~A by switching to `gold/canonical/holdings_*`)

Base lane's `f2dfee9a` (SCOPEFIX cohort_mask broadening) addresses the same problem at silver layer; both fixes are valid and complementary. After silver rebuild via base lane's chain (completed 18:12Z, COO confirmed), client_details count went from 297 → 995 (3.3× pre-SCOPEFIX).

### F1+F2+F3 schema alignment unblocks 5 portal panels

Per `INFLEC_BD_PARITY_MATRIX.md` v0.1: panels #2 (header tiles), #5 (Distribution snapshot), #7 (leaderboard), #8 (top-3 highlights), #15 (AdvisorPublicProfile) all unblock with these three publisher fixes. Panels #6 (cumulative_chart), #11 (BooksTab dashboard), and per-advisor extras (#9, #13) remain follow-on TOs.

---

## Pending / Next

| Item | State | Blocker | Owner |
|------|-------|---------|-------|
| RD 0.4.2 re-validation pass | Triggered | None (gate cleared) | RD 0.4.2 |
| INFLEC_BD_PARITY_MATRIX.md v0.2 review pass | Pending | DS~A bandwidth | DS~A + DE |
| F4 — `cumulative_chart.json` (panel #6) | Not started | Needs new emitter or extend I_D00b | DS~A (post-matrix-v0.2) |
| F5 — `mix_summary.json` (panel #11) | Not started | Extend D_04 | DS~A |
| Per-advisor extras: `mix.json`, `nna_clients.json`, `exec_summary.json`, `timeseries.json` | Not started — confirmed missing across all 9 advisors | New publishers (or extend D_02 / I_D03) | DS~A |
| `unknown/` PLACEHOLDER exclusion | Not started | Add `'unknown'` to `_PLACEHOLDER_KEYS` in D_02 + I_D03 publishers; delete stale `s3://opal-data-inf/platinum/advisors/unknown/book.json` (379 B) | DS~A |
| INF_ rename pass (~30 .py files in `data/orion/scripts/gold/`) | Queued | Andrew approved 2026-04-27; runs after parity reconciliation stable | DS~A |
| ADHC_COMPIL.005 (nested-key reverse lookup) | GO received from COO 16:55Z, on hold | Sequenced after ADVI_INFPRTY follow-ons | DS~A |
| ADVI_INFLEC W4.13b + ORNREN Q8/Q9 | Unblocked (AE 0.6.1 chain completed 18:12Z) | DS bandwidth | base DS lane (per COO ruling — ~A defers) |
| Lambda-served path INF-awareness smoke (panels #11, #12, #14) | Pending | DT smoke TO scoping | DT 0.4.0 |
| DE-side panel suppression PR (DistributionTab OFC + CLA hide; FeeEfficiencyPanel hide) | Pending — post-schema-fix | RD re-validation result | DE 0.4.0 |

---

## Cross-Lane Notes

- Base lane `0.4.0_DS_ClientPlatform` ran SCOPEFIX work in parallel: silver-layer `convert_orion_to_silver.py` cohort_mask broadening (`f2dfee9a`), C_07 household_id pyarrow fix (COO override `f84c2df4`), full A→C→D_02→I_D03 chain rerun. Client details went 297 → 995. Independent of ~A's script-level fixes; both fixes complementary.
- COO HOLD'd base lane's separate D_00c+D_04 dispatch attempt at 18:50Z to prevent double-run with ~A's already-dispatched chain.
- COO noted `B_00` rebuild deferred to maintenance window per ruling (a) at 18:48Z (non-blocking for current portal unblock).
- DE shipped `INFLEC_PORTAL_FIELD_USAGE.md` (`0c241ee0`) and joint `INFLEC_BD_PARITY_MATRIX.md` v0.1 (`5dfa6a12`) using my v0.1 inventory verdicts — joint v0.2 review pass remains.

---

## Notes on Inbox-Watch Discipline

Andrew called out twice this session that `inbox-watch.sh` must run continuously across the entire session. Saved hard rule to `memory/feedback_inbox_watch_always_running.md`: every task-notification reporting watcher exit gets an immediate same-turn relaunch via Bash `run_in_background: true`, batched in parallel with `check_inbox` + `get_agent_status`. No exceptions. Subsequent watcher cycles in the session held this discipline.
