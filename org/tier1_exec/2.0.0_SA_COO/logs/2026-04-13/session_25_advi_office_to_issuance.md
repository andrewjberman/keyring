# COO Session 25 -- ADVI_OFFICE Task Order Issuance
**Date:** 2026-04-13
**Agent:** 2.0.0_SA_COO
**Scope:** Ground truth reconciliation (session 25) + ADVI_OFFICE 4-wave TO decomposition.

---

## Startup Protocol

1. `register_agent("2.0.0_SA_COO")` -- LIVE, PID 28272, broker connected.
2. `bash org/mcp/check-inbox.sh 2.0.0_SA_COO` -- no pending messages.
3. `inbox-watch.sh` launched via Bash `run_in_background`.
4. Read org/XXX.md, org/ref/COO_STARTUP.md, session 24 logs + closeout memo.

## MCP Scan Results

Live agents at startup (7): 1.0.0_SA_CTO, 2.0.0_SA_COO, 0.4.0_DE, 0.4.0_DS, 0.4.0_DT, 0.5.0_AE_OpalETL, 0.6.0_AE_PartnerETL.

Pending TOs per org_summary:
- 0.4.0_DS: ADVI_REBORN.W6-003 (pending, self-authored).
- 0.4.0_DT: deployment_map.
- 0.1.0_DT, 0.2.0_DT: deployment_map.
- 0.5.0_AE, 0.6.0_AE: infrastructure_inventory.
- 0.4.2_RD: page_inventory.

## Ground Truth Corrections (this session)

| Finding | Action |
|---------|--------|
| yang-v2.3.8 deployed (ci commit abf039c1/c9b382d5, 2026-04-13 DS session). Dashboard still showed yang-v2.3.6. | prompt.md Pipeline Tags updated to yang-v2.3.8. |
| DEBT_1STRUN closed per REGISTRY (0.5.0_AE .005 complete, HEAD 66af3ad5). Dashboard still showed it as active with .005 in-flight. | Moved to Closed in prompt.md dashboard. |
| ADVI_OTHDED + ADVI_HDRSPL closed per REGISTRY (2026-04-13 ship). Not yet reflected in dashboard. | Added to Closed note in prompt.md. |
| ADVI_OFFICE registered (new active project, COO TO issuance blocking). | Added to Active Projects table. 4 TOs written this session. |
| ADVI_PROFAU active (.001+.002 complete, .003+ pending). Not in dashboard. | Added to Active Projects table. |
| ADHC_DESIGN .025 COMPLETE-IN-FACT, .028+.032 shipped per REGISTRY (3096108+f3274f3). Dashboard said all 3 pending. | Updated ADHC_DESIGN row in dashboard. |
| Pod 4 + Shared Services status tables stale (session 24 startup data, 3 full agent sessions ago). | Rewritten to reflect 2026-04-13 session activity. |

Documents corrected: `org/tier1_exec/2.0.0_SA_COO/prompt.md` (dashboard rewrite).

## ADVI_OFFICE TO Decomposition

PRD read: `docs/architecture/ADVI_OFFICE_PRD.md` (v2, decisions resolved by Andrew 2026-04-13).

Key decisions (all resolved): Other bucket for unresolved advisors; Continuous AUA by OFC in V1 scope; ADV toggle stays.

### Compiler Tools (pre-TO mandate)

| Tool | Command | Result |
|------|---------|--------|
| `comp-pipescript io D_01` | `comp-pipescript io D_01` | PASS. D_01 reads account_team, writes partner_analytics artifacts. dim_advisor_office is dynamic S3 read (not graph-tracked, expected). |
| `comp-pipescript io D_00b` | `comp-pipescript io D_00b` | PASS. D_00b reads account_team + client_performance, writes timeseries_chart.json. |
| `comp-blast DistributionTab` | `comp-blast DistributionTab` | PASS. 8 downstream nodes (4 endpoints, all via opal-partners-data Lambda). OFC additive to same endpoints -- no blast radius change. |
| `comp-transform schema-check DistributionTab` | `comp-transform schema-check DistributionTab` | PASS with note. Existing `chartData` (L658/L687/L859) and `analyticsData` (L606/L687/L841) are destructured aliases not in TypeScript types -- pre-existing pattern, not introduced by OFC. Captured in W3 DE TO context. |

All 4 compiler runs logged to `org/compiler-tools-log.md` (append below).

### Wave Structure

| Wave | Agent | Scope | Status |
|------|-------|-------|--------|
| W1 | 0.4.0_DS_ClientPlatform | D_01 OFC view + D_00b timeseries OFC | staged |
| W2 | 0.6.0_AE_PartnerETL | dim_advisor_office.csv S3 upload + D_00b+D_01+D_04 QA+PROD gold run | staged |
| W3 | 0.4.0_DE_ClientPlatform | DistributionTab OFC toggle + types + chartColors | staged |
| W4 | 0.4.0_DT_ClientPlatform | Portal DEV -> PROD deploy | staged |

Sequencing: W1 GO now. W2 GO on DS MCP signal (commit hash + S3 upload). W3 GO on AE MCP signal (PROD artifact live). W4 GO on DE complete + AE PROD artifact confirmed.

Cross-domain note captured in W3 TO: types.ts will also be touched by ADVI_REBORN.W6-004. DE must pull latest after W6-003 ships before editing types.ts.

### Task Orders Written

| File | Agent |
|------|-------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_OFFICE.W1.ds-d01-d00b-ofc-view.md` | DS |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_OFFICE.W2.ae-dim-upload-gold-run.md` | AE |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_OFFICE.W3.de-ofc-frontend.md` | DE |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_OFFICE.W4.dt-portal-deploy.md` | DT |

## ADVI_REBORN Status

W6-003 DS TO already self-authored and pending. W6-004 DE TO exists and is staged (dependent on DS W6-003 ship). COO monitors -- will issue GO to DE when DS MCP-signals W6-003 gold run complete.

## Pending Work Not Yet Started This Session

| Item | Reason |
|------|--------|
| ADVI_PROFAU .003+ TOs | Need to read profau_gap_audit_response.md and understand 5 remaining gaps. Awaiting Andrew priority signal. |
| ADVI_OFFICE W1 GO signal to DS | Will send MCP to DS after this commit (DS should complete W6-003 first, then proceed with W1). |

## Next

1. Commit this session (TOs + dashboard + session log).
2. MCP message to DS: W6-003 first, then ADVI_OFFICE W1 staged for GO on W6-003 completion.
3. Stand by to issue DE W6-004 GO when DS W6-003 gold run confirms.
4. Stand by to issue W3 DE + W4 DT GO on AE W2 completion.
