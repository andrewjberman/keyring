# 0.4.0_DE_ClientPlatform — ADVI_INFLEC W5.0.2: Folder Structure Proposal
**Date:** 2026-04-21 ET
**TO:** ADVI_INFLEC.W5.0.2.de-propose-folder-structure
**Status:** COMPLETE — pending W5.0.3 CTO review
**Deliverable:** `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/advi_inflec_folder_structure_proposal.md`

---

## Phase 1 Compiler Tools

**comp-transform schema-check AdvisorIntelligence**
Result: 11 UNUSED (expected — page root is orchestrator; unchanged from W5.0.1 baseline), 0 MISSING, 0 NOTE.
Status: PASS

---

## Design Decisions

**1. Prop-extraction over file-duplication for attribution-copy 49F-isms.**
AUATrendChart, PartnerAnalytics, and DistributionTab have only hardcoded vendor-name strings as their 49F-ism. Duplicating these large files (DistributionTab is ~3200 lines, PartnerAnalytics ~2000 lines) to `_partners/49financial/overrides/` would create two nearly identical files to maintain. Instead: keep in `_shared/`, add `sourceAttribution` / `sourceLabel` / `tooltipAttribution` props, partner page-root supplies the BD strings from `_partners/49financial/constants.ts`. Net: zero logic change, zero test risk.

**2. AdvisorIntelligence.tsx page root becomes `_partners/49financial/index.tsx` — not extractable.**
This file has structural 49F decisions (AVAILABLE_FIRMS policy, firmId default, Black Diamond Connected panel as a hardwired layout element). These can't be abstracted as props — they ARE the partner's page assembly. The new `index.tsx` router dispatches to this file for firmId='bd'.

**3. ClientDetailPage.tsx firmId fallback extracted to `defaultFirmId` prop.**
The `|| 'bd'` URL-param fallback is a single prop injection point. Extracting it allows `ClientDetailPage` to be SHARED without changing any rendering logic.

**4. SmallAccountsByRoleModal — concrete R1 recommendation: required `thresholdUsd` prop.**
This resolves CTO Q2 without waiting for the answer. A required prop is safer than an optional default that might silently carry the 49F value to Inflection.

**5. 5 AMBIGUOUS files provisionally placed in `_shared/`** pending CTO W5.0.3 review. Role taxonomy (Q1) and access model (Q3) are the two architectural decisions that could reclassify them. See §5 of proposal for detailed CTO questions and dependency tree.

---

## Acceptance Criteria Status

| # | Criterion | Status |
|---|---|---|
| 1 | Proposal at `deliverables/advi_inflec_folder_structure_proposal.md` | PASS |
| 2 | All 40 W5.0.1 components have src→target row | PASS |
| 3 | index.tsx composition pattern specified | PASS |
| 4 | At least one AMBIGUOUS with concrete resolution recommendation | PASS (R1: SmallAccountsByRoleModal `thresholdUsd` prop) |
| 5 | Session log written | PASS (this file) |

---

## Files Created/Modified

| File | Change |
|---|---|
| `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/advi_inflec_folder_structure_proposal.md` | New — 40-component file-move plan + index.tsx router pattern + CTO questions |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_INFLEC.W5.0.2.de-propose-folder-structure.md` | Status: staged → complete |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/logs/2026-04-21/advi_inflec_w5_0_2_folder_structure_proposal.md` | This file |

---

## Next Steps

- `[CTO 1.0.0_SA_CTO]` W5.0.3 review: accept/modify proposal; answer Q1 (role taxonomy), Q3 (Book/Profile access), R1 (thresholdUsd) — then GO for W5.0.4 execution
- `[DE]` W5.0.4 execution unblocked for 30 SHARED + 5 49F-SPECIFIC components after CTO sign-off; AMBIGUOUS 5 remain blocked until Q1/Q3 resolved
- W5.0.3 is CTO-owned; no DE action until CTO MCP
