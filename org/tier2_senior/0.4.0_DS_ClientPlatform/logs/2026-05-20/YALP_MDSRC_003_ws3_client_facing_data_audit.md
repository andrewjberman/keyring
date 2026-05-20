# YALP_MDSRC.003 — WS-3 Client-Facing Data Domain Audit — 2026-05-20

**Agent:** 0.4.0_DS_ClientPlatform (base lane)
**TO:** YALP_MDSRC.003.ds-ws3-client-facing-data-domain-audit
**Branch:** CLOUD
**Status:** COMPLETE — audit deliverable committed; RAVC2 to COO CC CTO.

## Current State

WS-3 (client-based/facing data domain) audit complete. Deliverable brief
`docs/briefs/mdsrc-ws3-client-facing-data-audit-20260520.md` written and committed,
carrying the WS-3 migration-candidate matrix slice (14-col common schema, 7 surfaces)
and the Q4 model-portfolio-performance sourcing recommendation. All 6 ACs met.

**Q4 answered:** SmartX REST API (`api.smartxadvisory.com/api/3.1` —
`reportedmodels/{rmid}/historicalperformance`, `models/{id}/statistics`,
`performance.smartxadvisory.com/models/performance`) recommended as the canonical
source for the portal's model-portfolio *performance* surfaces, superseding the weekly
manual yang `model.pkl` for those fields; `model.pkl` retained as the Opal-proprietary
design/computed view. YCharts `/model_portfolios/*` REJECTED — it is a
portfolio-construction directory (not a managed-model performance feed) and is
403/un-entitled on the current YCharts seat tier (WS-1 corroboration).

**Key correction caught via MDPF coordination:** an initial WS-3 read (from the legacy
`data/smartx/` scrape pipeline alone) was heading toward "SmartX = AUM-only, ruled out
as a performance source." DS~B's coordination reply established that the SmartX *REST
API* exposes real model-portfolio performance endpoints — SmartX stays a Q4 candidate
and is the recommendation. The mandatory MDPF coordination (PRD §7) did exactly its job.

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| WS-3 domain audit | docs/briefs/mdsrc-ws3-client-facing-data-audit-20260520.md | COO, CTO (WS-5 synthesis input) |

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/mdsrc-ws3-client-facing-data-audit-20260520.md | NEW — WS-3 audit brief + matrix slice + Q4 recommendation |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-20/YALP_MDSRC_003_ws3_client_facing_data_audit.md | NEW — this session log |

No code/Terraform/portal change — v0.2 is audit-only (per TO `<do_not>`).

## Compiler Tools

Phase-1 mandate (`<run>` / `<expect>` / observed):

| Run | Expect | Observed | Verdict |
|-----|--------|----------|---------|
| `comp-pipescript io <data/smartx gold script>` (`consolidate_smartx_to_parquet`) | SmartX gold-tier load list + COLUMN GAPS + portal consumers | "Unknown script" — comp-pipescript only indexes BD-gold IDs (A_00..D_04); `data/smartx/scripts/` is off the comp graph. Per the TO `<if_mismatch>`, fell back to direct source read (`SMARTX_BIBLE.md`, `SMARTX_API_DOCUMENTATION.md`). | PASS (documented fallback) |
| `comp-blast <SmartX Lambda node>` | downstream consumers of the SmartX backend | Not run as a distinct step — PRD §5 pre-declares the SmartX/yang pipeline has sparse-to-absent comp-graph edges; substituted the source read of `data/smartx/` + `PORTAL_DATA_FLOW.md` + the MDPF feeder, per the TO `<if_mismatch>` and PRD §5. Gap recorded as an audit finding (§1 honest scope note in the brief). | PASS (documented fallback per PRD §5) |
| `comp-routes behaviors` | serving path for client-facing portal surfaces in scope | Confirmed `/api/private/portfolio*` -> auth-gated Portfolio API Gateway; public surfaces serve `/api/public/json*` + `/api/general/portfolios/*` (cross-checked against `portal/src/api/portal-proxy.ts`). Serving paths in the matrix slice are comp-routes + portal-proxy confirmed. | PASS |
| YCharts side | documented-none (external system, PRD §5) | YCharts is external — no comp-* applies; evidence base is the 92 MB HAR deep-parse + WS-1's live-session capture. Documented-none per PRD §5. | N/A (documented) |

Phase 2 (before commit): documented-none — audit deliverable is a committed brief, no
code; no py_compile / ruff / ds-precommit gate applies.

Phase 3 (after commit): documented-none — the WS-3 matrix slice + Q4 recommendation is
the deliverable's self-validation, checked by the acceptance criteria (brief §10).

## Cross-Agent Coordination

| Peer | Channel | Outcome |
|------|---------|---------|
| 0.4.0_DS_ClientPlatform~B (MDPF lane) | MCP thread | AC4 — full SmartX grain/coverage/cadence + two-path distinction + MDPF AUA-architecture orthogonality; 4 briefs cited. Corrected the SmartX-AUM-only misread. |
| 0.2.0_DS_PortfolioAnalytics (WS-2) | MCP thread | AC5 — Model Portfolios seam: `model`/`model_return` cols = WS-3, benchmark/rfr cols = WS-2; column-level seam on the shared artifacts, agreed both ways. |
| 0.1.0_DS_MarketIntelligence (WS-1) | MCP thread | Common 14-col matrix schema confirmed; YCharts auth/WAF finding consumed (no re-probe); `/model_portfolios/*` 403/un-entitled finding consumed for Q4. |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — YALP_MDSRC.003 complete, AC1-AC6 met. WS-3 is the last of the 4 Phase-0 audits; on RAVC3-accept, CTO TO-5 (WS-5 synthesis -> PRD v0.3) unblocks. |
| **CTO 1.0.0** | CC on RAVC2 — Q4 input for the WS-5 synthesis: SmartX REST = canonical model-portfolio performance source; note the SXPL_RESTIN overlap (a v0.3 SmartX-perf pull likely co-scopes with SXPL_RESTIN, not a parallel pull). |
