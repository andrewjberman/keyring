# MCP Startup Protocol + Stale TO Cleanup — 1.0.0_SA_CTO

**Date:** 2026-03-25
**Session:** 9

## Objective

Establish MCP org scan as the mandatory first action in CTO and COO startup,
then execute it — cleaning up stale task orders that session 8's file-only
reads missed.

---

## Work Completed

### 1. MCP Org Scan Execution

Ran the full `opal-agent-comms` tool suite for the first time as a startup
protocol rather than ad hoc. The scan surfaced 10 stale pending task orders
across 3 agents — all on completed projects. Session 8 earlier today used
file-only reads (project JSONs, REGISTRY.md) and found 0 issues because
the project-level documents were already correct. The agent-level task orders
were not.

**Root cause:** File-only reads check the project JSON (which said "complete")
and stop. The MCP `get_org_summary()` scans every agent's `task_orders/`
directory and surfaces pending TOs regardless of project status. That's the
gap.

### 2. Stale Task Orders Corrected (10 total)

| Agent | Task Order | Project | Evidence |
|---|---|---|---|
| 0.4.0_DT_ClientPlatform | ADVI_PRICES.001.dt-push-and-verify | ADVI_PRICES (complete) | Code on CLOUD, gold reruns verified |
| 0.4.0_DT_ClientPlatform | ADVI_PRICES.003.dt-push-and-verify | ADVI_PRICES (complete) | All commits on CLOUD, AE verified |
| 0.4.0_DT_ClientPlatform | ADVI_APISCP.002.lambda-edge-v4-tag | ADVI_APISCP (complete) | Router v7 live, E2E verified 03-10 |
| 0.4.0_DT_ClientPlatform | ADVI_APISCP.003.cloudfront-oai-wire-v5-deploy | ADVI_APISCP (complete) | OAI + cache key deployed by CloudOps |
| 0.4.0_DT_ClientPlatform | ADVI_YANGV2.portal-push.phase3 | ADVI_YANGV2 (complete) | Subsumed by portal-v2.1.17 merge |
| 0.6.0_AE_PartnerETL | ADVI_MVP318.003.ae-final-gold-layer-run | ADVI_MVP318 (complete) | Gold reruns done under GLDPRE+BKSCMP |
| 0.6.0_AE_PartnerETL | aua-scoped-price-overrides-deploy | GLDPRE-related (complete) | Scoped overrides deployed under GLDPRE |
| 0.4.0_DE_ClientPlatform | ADVI_APISCP.006.final-browser-verification | ADVI_APISCP (complete) | APISCP routing verified through subsequent work |
| 0.4.0_DE_ClientPlatform | ADVI_MVPLVL.004.p4-books-proxy-wiring | ADVI_MVPLVL (complete) | Books proxy routes delivered under BKSCMP |
| 0.4.0_DE_ClientPlatform | ADVI_MVPLVL.009.mix-composition-e2e | ADVI_MVPLVL (complete) | DE log 03-23 confirms delivery at 0444d10 |

### 3. COO Dashboard Corrected

Updated Pod 4 and Shared Services tables in COO `prompt.md` to reflect the
10 closed TOs:
- `0.4.0_DE`: 4 pending -> 1 pending (DEBT_1STRUN.001 only)
- `0.4.0_DT`: 6 pending -> 1 pending (deployment_map only)
- `0.4.0_DS`: 1 pending -> 0 pending
- `0.6.0_AE`: 4 pending -> 1 pending (infrastructure_inventory only)

### 4. Startup Protocol Rewrite (CTO prompt.md, CTO README.md, COO prompt.md)

Rewrote the "On Launch" section for both exec agents. Changes:

**Removed:**
- "Read your task orders" — CTO doesn't receive task orders
- "Check today's daily log" — CTO's daily log IS the startup scan
- "Read DE logs manually" (COO) — MCP `get_agent_status()` does this
- "Scan task order status fields manually" (COO) — `get_org_summary()` does this
- "Re-scan to verify" step — circular; re-reading files you just edited proves
  nothing. The fix is doing Steps 3+4 correctly, not running them twice.

**New 5-step protocol (both agents):**

| Step | Action |
|------|--------|
| 1 | Read own last session log (continuity) |
| 2 | Read project registry (identify the tree) |
| 3 | MCP org scan — drill to every agent with pending TOs, validate against git |
| 4 | Roll corrections back up — TOs, JSONs, registry, both dashboards |
| 5 | Oriented summary to Andrew |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| MCP scan before file reads | `get_org_summary()` covers the full org in one call; file reads only cover what you think to look at |
| Remove "re-scan to verify" step | Circular — MCP reads the files you just edited. Not an independent validation source. Doing Step 3 correctly eliminates the need. |
| Remove CTO "read task orders" step | CTO does not receive task orders. Misleading instruction. |
| Remove CTO "check daily log" step | CTO has no daily log file. The startup scan IS the daily log. |

---

## Files Modified

| File | Change |
|---|---|
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | Rewrote On Launch to 5-step MCP-first protocol. Updated dashboard. |
| `org/tier1_exec/1.0.0_SA_CTO/README.md` | Rewrote Ground Truth Correction section to match prompt.md. |
| `org/tier1_exec/2.0.0_SA_COO/prompt.md` | Rewrote On Launch to 5-step MCP-first protocol. Corrected Pod 4 + Shared Services tables. |
| 10 task order files | `pending` -> `complete` with evidence comments |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD (local, not pushed)

All 3 exec startup docs now use the same 5-step MCP-first protocol. 10 stale
task orders cleaned. COO dashboard reflects corrected pending counts. Two active
projects remain: ADVI_GLDRST (blocked on COO task orders, now unblocked) and
DEBT_1STRUN (Phase 1 partial, remaining pod scans pending).

## Next Steps

1. **[Andrew] Direct next work** — GLDRST PRD is approved and unblocked, or new initiative
2. **[2.0.0_SA_COO] GLDRST task order decomposition** — BKSCMP + CLSPT2 blocker cleared
3. **[DEBT_1STRUN] Remaining pod scans** — 0.1-0.3 DS, all remaining RD, all DE, AE 0.5.0/0.7.0

**Do NOT:**
- Revert to file-only reads for startup — always MCP-first
- Add a "re-scan" step back — it's circular
