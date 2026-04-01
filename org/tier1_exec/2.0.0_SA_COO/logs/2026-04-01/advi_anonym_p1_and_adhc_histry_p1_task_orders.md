# ADVI_ANONYM P1 + ADHC_HISTRY P1 Task Order Issuance -- 2.0.0_SA_COO

**Date:** 2026-04-01
**Start Time:** Startup
**Session:** 8

## Objective

Ground truth reconciliation on startup, then issue blocked P1 task orders for
ADVI_ANONYM (pseudonymization) and ADHC_HISTRY (Schwab-authority injection).

---

## Startup Audit (Step 3 MCP Scan)

### Org Summary at Startup

- 2 live agents: 1.0.0_SA_CTO (starting session) and self.
- Inbox: empty.
- No stale pending TOs found. All pending TOs verified legitimate by agent log cross-check.

### Pending TO Verification

| Agent | TO | Verdict |
|---|---|---|
| 2.0.0_SA_COO | DEBT_1STRUN.001.scan | Legitimately pending -- COO aggregate scan not done |
| 0.2.0_DE | DEBT_1STRUN.001.scan | Legitimately pending -- last log 2026-03-02, scan not done |
| 0.3.0_DE | DEBT_1STRUN.001.scan | Legitimately pending -- last log 2026-03-05, scan not done |
| 0.4.0_DE | DEBT_1STRUN.001.scan | Legitimately pending -- last log 2026-03-26, scan not done |
| 0.7.0_AE | DEBT_1STRUN.001.scan | Legitimately pending -- last log 2026-03-30 |
| 0.1.2_RD | DEBT_1STRUN.001.scan | Legitimately pending |
| 0.4.2_RD | DEBT_1STRUN.001.scan + page_inventory | Legitimately pending |
| 0.1.0_DT, 0.2.0_DT, 0.4.0_DT | deployment_map.md | Legitimately pending (CTO-issued) |
| 0.5.0_AE, 0.6.0_AE, 0.7.0_AE | infrastructure_inventory.md | Legitimately pending |
| 0.4.1_RD | xtick_spacing_fix.md | Legitimately pending (issued 2026-03-02) |

**Zero stale TOs corrected.** COO dashboard was accurate from 2026-03-31 update.

### Key Correction Found (PRD False Blocker)

PRD ADVI_ANONYM_PRD.md states "portal_authorizer update -- add role to context" as
a prerequisite for P1. COO verified the actual deployed source:

- Source map points to: `infra/aws/users/lambda/portal-authorizer/index.mjs`
- That file (line 198): `role: decoded.role` -- ALREADY IN CONTEXT
- Deployed: 2026-03-04 (well before P1 was specified)

**Impact:** No DE task order needed for portal_authorizer. Task order .002 (DS) and
.004 (DT) both updated to reflect this. Eliminates one prerequisite step from the
deployment chain and unblocks DS from waiting on DE.

This finding was NOT in the PRD. It was discovered by COO reading the actual source file.

---

## Task Orders Issued

### ADVI_ANONYM P1

| TO | Agent | Status | Summary |
|---|---|---|---|
| ADVI_ANONYM.002.ds-pseudonymizer-lambda.md | 0.4.0_DS | STAGED | Write pseudonymizer.py + wire into lambda_function.py. Extract user_role at line 1158. Apply per role matrix. |
| ADVI_ANONYM.003.ae-secrets-provisioning.md | 0.7.0_AE | STAGED | Provision opal/pseudonym/{firmId} secrets in Secrets Manager. Update Lambda IAM role. |
| ADVI_ANONYM.004.dt-lambda-deploy-cf-update.md | 0.4.0_DT | STAGED | Deploy Lambda (after DS). Attach auth-validator-edge to CF behaviors 13+14. Remove P0 gate last. |

**Dependency chain:**
```
AE (.003 secrets) ────────────────────────────────┐
                                                   v
DS (.002 pseudonymizer) ──> DT (.004 deploy + CF + gate removal)
```

No DE TO needed (portal_authorizer already correct).
P2 (frontend graduated UI) not yet decomposed -- awaiting CTO direction or Andrew GO on P1 first.

### ADHC_HISTRY P1

| TO | Agent | Status | Summary |
|---|---|---|---|
| ADHC_HISTRY.002.ds-schwab-authority-injection.md | 0.4.0_DS | STAGED | Phase 1: diagnostic script (injection_units = schwab_units - fifo_units). Phase 2: implement in scripts 02/03 after diagnostic reviewed. |

**Note:** AE Schwab TRN daily ingestion pipeline is a follow-on TO not yet issued.
Schwab data through 2026-03-30 is sufficient for Phase 1 diagnostic.

---

## Documents Corrected

| File | Change |
|---|---|
| org/projects/ADVI_ANONYM.json | phase + blocking updated |
| org/projects/ADHC_HISTRY.json | phase + blocking updated |
| org/projects/REGISTRY.md | ADVI_ANONYM + ADHC_HISTRY rows updated |
| org/tier1_exec/2.0.0_SA_COO/prompt.md | Dashboard updated (session 7 -> 8, ANONYM + HISTRY rows) |

---

## Current State

**Status:** COMPLETE (task orders issued, docs corrected)
**Active branch:** `CLOUD`

4 task orders written and staged across 3 projects. ADVI_ANONYM P1 is fully decomposed
(DS + AE + DT). ADHC_HISTRY P1 is ready for DS diagnostic. All TOs are STAGED -- awaiting
Andrew GO before agents activate. ADVI_GLDRST P3 TOs remain staged (12 TOs, not activated
this session -- awaiting Andrew's explicit GO for P3 kickoff). CTO is live concurrently.

---

## Next Steps

1. **Andrew GO for ADVI_ANONYM P1** -- Send go messages to DS (.002), AE (.003) in parallel.
   DT (.004) activates after DS + AE complete.

2. **Andrew GO for ADHC_HISTRY P1** -- Send go message to DS (.002). DS runs Phase 1
   diagnostic, reports gap numbers. COO reviews and sends Phase 2 GO.

3. **ADVI_GLDRST P3 activation** -- 12 TOs staged. Andrew must direct COO to send GO
   to kick off P3. Dependency order: .003 (DE) in parallel with .004-.006 (DS).

4. **ADVI_ANONYM P2 decomposition** -- Frontend graduated UI (AuthContext, DistributionTab,
   ClientsTab, ClientDetailPage). Awaiting P1 deploy + verification first.

5. **AE Schwab TRN daily ingestion** -- Follow-on TO for 0.6.0_AE after ADHC_HISTRY P1
   diagnostic confirms injection approach. Not yet issued.

6. **DEBT_1STRUN remaining 7 scans** -- COO aggregate scan (self) + 6 agent TOs still pending.
   Low priority relative to ANONYM P1 and HISTRY P1.

**Do NOT:**
- Activate ADVI_GLDRST P3 without explicit Andrew GO
- Issue P2 frontend TOs for ADVI_ANONYM before P1 is verified end-to-end
- Remove the P0 role gate before DS pseudonymizer is confirmed working

---

## ADVI_ANONYM P1 Findings Summary (for CTO visibility)

| Finding | Impact |
|---|---|
| portal_authorizer already returns role (deployed 03-04) | Eliminates DE prerequisite step. P1 chain is DS + AE -> DT only. |
| auth-validator-edge attached to behaviors 2 and 5 only (not 13/14) | DT Track B must attach edge to /api/scoped/partners/* and /api/partners before P0 gate removal. |
| lambda_function.py line 1158 extracts tier but not role | DS adds 1 line: user_role = auth_context.get('role', ''). |
| Some response paths use cors_response (5-min cache) not cors_response_nocache | DS must audit and fix all PII handlers. Cleartext caching is a security risk. |
