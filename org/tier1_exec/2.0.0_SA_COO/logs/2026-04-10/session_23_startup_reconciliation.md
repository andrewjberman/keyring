# COO Session 23 — Startup Ground Truth Reconciliation
**Date:** 2026-04-10
**Agent:** 2.0.0_SA_COO
**Session scope:** MCP org scan, project state reconciliation, ADVI_GLDRST reopen, dashboard refresh

---

## Startup Protocol

1. `register_agent("2.0.0_SA_COO", summary="Session 23 startup — ground truth reconciliation")` — LIVE, PID 16300, broker connected.
2. `inbox-watch.sh` launched via Bash `run_in_background`. Exited immediately on inbound: DS message about ADVI_GLDRST.021 shipment. Read output file, relaunched watcher, continued.
3. Read previous session log (session 22 post-mortem, 2026-04-09).
4. Read `org/projects/REGISTRY.md`.

## MCP Scan Findings

### Live Agents (4)
- `1.0.0_SA_CTO` — reconciling org state (session start)
- `2.0.0_SA_COO` — this session
- `0.4.0_DS_ClientPlatform` (+DS~A) — just shipped ADVI_GLDRST.021
- `0.4.2_RD_AdvisorIntelligence` — session start

### Not Registered
- `0.4.0_DE_ClientPlatform` — has 6-message inbox backlog from previous COO (DataTooltip guidance) + pending REBORN W5-005 + pending ADHC_DESIGN .025/.028/.032
- `0.4.0_DT_ClientPlatform` — shipped bd-v2.21.8 API GW route registration 04-10 but not currently registered
- All other pod DEs/DSs/DTs and AEs

### Pending Task Order Audit

Surfaced via `get_org_summary()`:

| Agent | Pending TO | Verdict |
|-------|-----------|---------|
| 0.1.0_DT | deployment_map.md | Legitimately pending (meta-doc, ongoing) |
| 0.2.0_DT | deployment_map.md | Legitimately pending |
| 0.4.0_DE | ADVI_REBORN.W5-005.de-advisors-tab-data-path | Legitimately pending — DE 0.4.0 not registered |
| 0.4.0_DT | deployment_map.md | Legitimately pending |
| 0.4.2_RD | ADVI_REBORN.W5-002.rd-advisors-tab-case-fix | Legitimately pending — RD LIVE this session |
| 0.4.2_RD | ADVI_REBORN.W5-006.rd-advisors-tab-rendering | Legitimately pending |
| 0.4.2_RD | page_inventory.md | Legitimately pending |
| 0.5.0_AE | infrastructure_inventory.md | Legitimately pending |
| 0.6.0_AE | infrastructure_inventory.md | Legitimately pending |

No stale TOs to flip in this scan.

## Ground-Truth Corrections Applied

### 1. ADVI_GLDRST reopened

CTO had already flipped `org/projects/ADVI_GLDRST.json` status `complete` → `active`
with the v2 canonical_prices phase description. CTO also added the project back to
the REGISTRY.md Active table in parallel with this session.

COO layered the dashboard update in `2.0.0_SA_COO/prompt.md` (new Active Projects
row; pipeline tags table bumped).

Reopen reason: DS trace work in `0.4.0_DS/logs/2026-04-10/b00_hybrid_price_fill_easter_dropout_root_cause.md`
and `gold_trigger_chain_trace_and_d00c_role_split_fix.md` identified that the Apr 3-5
"mystical" chart dropout is caused by `bd-price-update` Lambda (post-ADVI_PRICES migration)
having no T3 linear_interpolation / gap-fill for weekend and holiday dates, and
`bd-allocation-processor` only fires on weekdays. Every gold script that reads
canonical_prices with a naive date lookup will hit this regression on every weekend and
every US holiday through 2026.

Andrew's decision: reinstate `build_canonical_prices_v2.py` as a scheduled nightly
pre-step in gold_dispatch, running as a full rebuild (~10-20 min on c6i.16xlarge) on
every daily boot.

### 2. ADVI_GLDRST.021 shipped (by 0.4.0_DS)

- **Scope:** build_t1_from_transactions writes `capped` bool; resolve_prices_for_asset emits `source='transaction_observed_capped'`. Strictly additive. Inline tradeoff comment at v2:T1.
- **Diff-before-ship:** 197,408 T1 rows identical old vs new. 31 newly-tagged rows / 14 assets. Zero price drift. Zero capped-mask mismatch.
- **Regression check 2024-08-07:** INVESCO STABLE VALUE RET CL 1 ($60,077.44 → $1.00) still caught. 8 capped rows total. PASS.
- **Finding flagged:** 4 of 31 capped rows are legitimate pre-split Chipotle (CMG 50:1 on 2024-06-25). Pre-split $3,200 rewritten to post-split ~$55. This is the known tradeoff documented in the inline comment; downstream consumers can now detect via the source tag.
- **Compiler audit:** A_03/B_01/bd-price-update/E_00/E_05 pass-through (safe). E_06:87 and E_14:80 filter on source values, will exclude capped rows (diagnostic-only, acceptable per TO).
- **Deliverables:** Commits 9b4f7a77 + 5d4756e2 (author=0.4.0_DS_ClientPlatform), S3 `silver/build_canonical_prices_v2.py` etag `d51a8260513a46d8ab94bde4e49bea69`, session log `v2_source_tag_and_diff_before_ship.md`.

### 3. ADVI_GLDRST.022 staged

Task order already on disk at `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_GLDRST.022.ds-v2-prestep-gold-runner-integration.md`.
Scope: v2 silver-prep chain in gold_dispatch.sh, script location decision (gold/ vs
silver/), freshness gate decision (v2 must run even when silver has not advanced),
AE handoff brief for EventBridge daily cron + Job 1 deprecation. Status: `staged`.
Prerequisite (.021) is satisfied — ready for COO GO when Andrew directs.

### 4. REGISTRY.md pipeline / project corrections

- `ADVI_49PUSH` row: bd-v2.21.7 → bd-v2.21.8. Added D_00 client_city + D_00c role_split ship note.
- `ADHC_DESIGN` row: updated from generic "20/24 original + .025-.032 GOed" to concrete "pods 0.1/0.2/0.3 COMPLETE (.026/.027/.029/.030/.031). Pod 0.4 PENDING (.025/.028/.032) -- DE 0.4.0 not registered."

### 5. COO dashboard refreshed (prompt.md)

New Active Projects table includes ADVI_GLDRST reopened row + ADVI_INCMTL row.
Pipeline Tags table bumped to bd-v2.21.8 + news-v2.9.5 (missing previously).
Operational notes 04-10 section added: bd-v2.21.8 content, ADHC_DESIGN Phase 2 split,
DS session log catalog, agent liveness truth.
Pod 4 + Shared Services sections refreshed.

### 6. bd-v2.21.8 contents (for future reference)

From `git log bd-v2.21.7..bd-v2.21.8`:
- `21e3b3f2` 0.4.0_DT: register missing bd-pipeline API GW routes (advisor/client drilldowns in BooksTab)
- `f75a3599` 0.4.0_DS: revert fix_3b strip in D_00b (market = raw sum(growth))
- `011ac15c` 0.4.0_DS: re-apply fix_3b in D_00b + strip economic_total from GRO schema
- `5779ec46` feat(gold_dispatch): freshness gate — skip chain if no new silver data
- `257d588f` fix(D_00b/D_01): exclude 'No City' meta value from city drill top-N
- `7ee3db59` feat(D_00c): tagged NNA/inflows/outflows/GRO + per-bucket fee breakdown
- `6396f385` fix(D_04): pass through fee_breakdown to platinum leaderboard
- `ef526221` fix(D_00b/D_01): crash on missing churn cols + ADV quarterly AUA frozen
- `f43fb30d` log(0.6.0_AE): gold runner IAM fix + watchdog loop RCA (bd-v2.21.7)
- `1a3318af` fix(B_01b): upgrade classification model gpt-4o-mini → gpt-5.4-mini
- `b0fe3d42` docs(gold-pipeline): incremental processing briefing

Portal-side in same window:
- pod 0.1 ADHC_DESIGN.026/.029 session logs (43263521)
- pod 0.2 ADHC_DESIGN.027 (f5b87e2d) + .030 (efcd4418)
- pod 0.3 ADHC_DESIGN.031 lint cleanup — 152 warnings (989ebef4)

## Current Blockers

1. **ADVI_49PUSH:** AE gold re-run (D_00/D_01/D_04) needed to land the D_00 client_city fix and D_00c role_split fix. Unblocks .020 e2e (also needs JWT from Andrew), .024 Phase 2, .026 GRO panel validation. .038 DE QTD default still pending (1-line fix).
2. **ADVI_REBORN:** W5-002 (RD case fix) + W5-006 (RD rendering) pending — RD 0.4.2 LIVE this session. W5-005 DE data path pending — DE 0.4.0 not registered.
3. **ADVI_GLDRST.022:** Awaiting COO GO. Prerequisite satisfied.
4. **ADHC_DESIGN Phase 2:** Pod 0.4 (.025/.028/.032) — need DE 0.4.0 spawn.
5. **DEBT_1STRUN.005:** AE 0.5.0 session needed.
6. **ADHC_TMSTEL:** Azure AD app registration (Andrew/IT) still outstanding.
7. **ADVI_PROFIL (NEW 04-10):** CTO added Advisor Profile + Book Architecture to the REGISTRY mid-session. P0: PRD complete, RD has portal DEV mods staged (uncommitted, tsc+eslint clean). 8 TOs across 4 waves; Wave 1 includes DT ship + DS book.tax_exposure + DT/AE JWT advisorId claim. Wave 2 AE Lambda@Edge advisor scoping blocks on Wave 1 JWT work. COO needs to decompose into task orders once Andrew directs.

## Files Touched

- `org/projects/REGISTRY.md` — ADHC_DESIGN + ADVI_49PUSH row rewrites.
- `org/tier1_exec/2.0.0_SA_COO/prompt.md` — dashboard refresh (sections: Active Projects, Pipeline Tags, Operational Notes, Pod 4, Shared Services).
- `org/tier1_exec/2.0.0_SA_COO/logs/2026-04-10/session_23_startup_reconciliation.md` — this log.

ADVI_GLDRST.json status flip to active was done by CTO in parallel; COO layered dashboard updates on top.

## ADVI_PROFIL Decomposition (mid-session)

Andrew delivered the ADVI_PROFIL handoff brief with CTO PRD, RD briefing, and recommended 8-TO / 4-wave split. COO decomposed into eight task orders, all staged:

| TO | Owner | Wave | Blocks on | Status |
|----|-------|------|-----------|--------|
| `ADVI_PROFIL.001.dt-ship-rd-portal-rewrite` | 0.4.0_DT_ClientPlatform | 1 | — | staged |
| `ADVI_PROFIL.002.dt-jwt-advisor-claim` | 0.4.0_DT_ClientPlatform (+0.7.0_AE_CloudOps) | 1 | — | staged |
| `ADVI_PROFIL.003.ds-book-tax-exposure` | 0.4.0_DS_ClientPlatform | 1 | — | staged |
| `ADVI_PROFIL.004.ae-advisor-scoping-enforcement` | 0.7.0_AE_CloudOps (+0.4.0_DT) | 2 | .002 | staged |
| `ADVI_PROFIL.005.rd-client-drilldown-lift` | 0.4.2_RD_AdvisorIntelligence | 3 | .001 | staged |
| `ADVI_PROFIL.006.rd-client-cache-policy` | 0.4.2_RD_AdvisorIntelligence | 3 | .001 + Andrew decision | staged |
| `ADVI_PROFIL.007.rd-admin-my-profile-toggle` | 0.4.2_RD_AdvisorIntelligence | 4 | .002 | staged |
| `ADVI_PROFIL.008.de-frontend-dev-visual-test` | 0.4.0_DE_ClientPlatform | 4 | .001 + Andrew dev server | staged |

Each TO carries full XML structure: metadata, objective, context, compiler_tools_mandate (3-phase), cross_domain_coordination (shared resources + last_write_owner + required_action), acceptance_criteria, scope, requirements, deliverables, do_not. Shared-resource coordination documented for the three hot spots: `ClientsTab.tsx` (.001 DT commit vs .005 RD lift), `AuthContext.context.ts` (.002 DT claim vs .007 RD reader), `auth-validator-edge` Lambda@Edge (.002 AE claim issuance vs .004 AE enforcement).

All TOs use `<status>staged</status>` per COO protocol — agents receive the scope but will not begin until COO sends a GO broker message. Wave 1 can GO immediately; Wave 2/3/4 gated on Wave 1 delivery.

ADVI_PROFIL.json `phase` and `blocking` updated to reflect decomposition.

## Next Steps

1. **[Andrew]** Decide whether to GO ADVI_GLDRST.022 now or sequence behind an AE gold re-run. .022 is DS code-staging only (no production impact) so it's safe to green-light immediately.
2. **[Andrew]** JWT for ADVI_49PUSH.020 auth smoke test + browser QA at opalinvest.dev.
3. **[0.6.0_AE / 0.7.0_AE]** AE gold re-run for D_00/D_01/D_04 to land client_city + D_00c role_split into platinum/cumulative_chart/timeseries_chart/leaderboard. Unblocks REBORN W5-001 (timeseries_chart.json regen), .020/.024/.026 validation, geo_drill state clickability.
4. **[COO me]** Commit session 23 startup changes (REGISTRY.md + prompt.md + this log) with `--author=2.0.0_SA_COO`.
5. **[COO me]** Monitor inbox for DS .022 scoping questions or further CTO directives.
