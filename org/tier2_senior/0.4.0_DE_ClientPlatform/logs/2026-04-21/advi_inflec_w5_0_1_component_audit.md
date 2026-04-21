# 0.4.0_DE_ClientPlatform — ADVI_INFLEC W5.0.1: AdvisorIntelligence Component Audit

**Date:** 2026-04-21 ET  
**TO:** ADVI_INFLEC.W5.0.1.de-audit-advisor-intelligence-components  
**Status:** COMPLETE  
**Deliverable:** `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/advi_inflec_component_inventory.md`

---

## Work Completed

### Phase 1 Compiler Mandate Runs

All Phase 1 tools executed per TO mandate before analysis.

**1. comp-transform schema-check AdvisorIntelligence**
Output:
- 1 UNUSED group (11 fields: adv, aua, cla, firm_name, geo, nna, +6 more) — expected; page root is an orchestrator, data fields are rendered by child components, not by AdvisorIntelligence.tsx directly.
- 0 MISSING, 0 NOTE.
- Baseline captured. No schema gaps that would affect refactor scope.

**2. File count**
```
find portal/src/pages/AdvisorIntelligence -type f *.tsx *.ts | sort
```
Result: 40 files (38 .tsx + 2 .ts + 0 .ts in lib = actually 7 .ts + 33 .tsx = 40 total).

**3. grep -rn "49financial|'49fin|BD\b|schwab|Schwab" portal/src/pages/AdvisorIntelligence/**
Result: **ZERO MATCHES.** No literal `49financial`, `schwab`, or `BD\b` strings inside AdvisorIntelligence/. 49F-specific references take the form of 'bd' firm IDs and "Black Diamond" source copy rather than the literal firm name.

**4. grep -rn "firmId|allowedFirmIds" portal/src/pages/AdvisorIntelligence/**
Result: 32 hits across 7 files. Key findings:
- AdvisorIntelligence.tsx:159 — `internal ? 'bd' : (claims?.firmId ?? 'bd')` — 'bd' default hardcoded
- ClientDetailPage.tsx:31 — `const firmId = searchParams.get('firmId') || 'bd'` — 'bd' fallback hardcoded
- AdvisorsTab, DistributionTab, ClientsTab — all accept firmId as a PROP (correct pattern; SHARED)

Additional targeted grep run: `49financial|'bd'|"bd"|Schwab|Black Diamond|custodian` across components/, panels/, tabs/, ClientDetail/:
- 10 hits concentrated in 5 files (see inventory evidence table for exact lines)
- Black Diamond source attribution in 3 components (PartnerAnalytics.tsx, AUATrendChart.tsx, DistributionTab.tsx)
- 'bd' hardcodes in 2 files (AdvisorIntelligence.tsx, ClientDetailPage.tsx)

**Grep for role-name hardcodes (ROLE_LABELS, ROLE_ORDER):**
- AdvisorBookView.tsx:483-492 — inline ROLE_LABELS not from chartColors (architect/consultant/implementor/additional_advisor/local_ops)
- AdvisorsTab.tsx:87-92 — ROLE_LABELS sourced from ADVISOR_ROLE_LABELS in @/lib/chartColors (not hardcoded inline)
- AdvisorPublicProfile.tsx:130 — ROLE_ORDER_INDEX hardcoded with same 5 roles

### Phase 3 — comp-transform fields AdvisorIntelligence
Run after inventory drafted. Output: 3 rendered fields at page-root level (analyticsData root, .generated_at, employeeData root). Expected — page root is an orchestrator; child components render the actual data fields.

---

## Inventory Results

| Category | Count |
|----------|-------|
| SHARED | 30 |
| 49F-SPECIFIC | 5 |
| AMBIGUOUS | 5 |
| **Total** | **40** |

**49F-SPECIFIC files:**
1. `AdvisorIntelligence.tsx` — AVAILABLE_FIRMS hardcode + 'bd' default + "Black Diamond Connected" panel text
2. `ClientDetail/ClientDetailPage.tsx` — 'bd' fallback in firmId URL param parse
3. `components/PartnerAnalytics.tsx` — "SS&C Black Diamond Wealth Solutions." footer (2 locations)
4. `components/AUATrendChart.tsx` — "SS&C Black Diamond Wealth Solutions." footer
5. `tabs/DistributionTab.tsx` — "Black Diamond" source attribution in footer + 2 tooltip copy locations

**AMBIGUOUS files (CTO questions):**
1. `AdvisorBookView.tsx` — inline ROLE_LABELS/ROLE_ORDER (same 5 role names); are these 49F-specific?
2. `AdvisorPublicProfile.tsx` — ROLE_ORDER_INDEX hardcode; Book vs Profile access policy
3. `tabs/AdvisorsTab.tsx` — role-filter logic keyed on 49F role vocabulary via chartColors lib
4. `SmallAccountsByRoleModal.tsx` — $40k threshold in display text; is this 49F-specific?
5. `types.ts` — AdvisorRole union + architect field in TaxDeferredCandidate

Full inventory with exact evidence and CTO questions at deliverable path above.

---

## Methodology Note

Primary 49F-ism detection strategy:
1. Grep for literal firm IDs ('bd', '49financial', 'schwab') — found 'bd' hardcodes in 2 files
2. Grep for vendor names (Black Diamond, SS&C) — found in 3 components
3. Read all files individually for structural 49F assumptions (AVAILABLE_FIRMS list, role vocab, access-model logic)
4. Distinguish: prop-accepting components (SHARED) vs hardcode-embedding (49F-SPECIFIC)

No Explore agent used (banned per org/XXX.md). All analysis done via Grep, Read, and Bash comp-* tools.

---

## Compiler Tools

| Phase | Tool | Result | Pass/Fail |
|-------|------|--------|-----------|
| Phase 1 | `comp-transform schema-check AdvisorIntelligence` | 11 UNUSED (expected orchestrator pattern), 0 MISSING | PASS |
| Phase 1 | File count (find) | 40 files | PASS |
| Phase 1 | `grep 49financial/schwab/BD` in AdvisorIntelligence/ | 0 matches | PASS (expected — 49F refs use 'bd' and "Black Diamond") |
| Phase 1 | `grep firmId/allowedFirmIds` in AdvisorIntelligence/ | 32 matches, 2 hardcoded 'bd' defaults, rest are prop-plumbing | PASS |
| Phase 1 | Targeted grep: `'bd'/"bd"/Black Diamond/custodian` | 10 matches in 5 files | PASS |
| Phase 3 | `comp-transform fields AdvisorIntelligence` | 3 rendered fields at root level (expected) | PASS |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_INFLEC.W5.0.1.de-audit-advisor-intelligence-components.md` | Status: staged -> pending | Not committed yet |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/advi_inflec_component_inventory.md` | New — 40-component inventory table | Not committed yet |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/logs/2026-04-21/advi_inflec_w5_0_1_component_audit.md` | This log | Not committed yet |

---

## Next Steps

- `[0.0_DE_ClientPlatform]` Commit this audit to CLOUD (DT to push after review)
- `[CTO 1.0.0_SA_CTO]` W5.0.3 review of 5 AMBIGUOUS rows — 3 CTO questions require architectural decision before W5.0.4 refactor can be scoped
- `[DE]` W5.0.2 — propose folder structure based on this inventory (input: 30 SHARED, 5 49F-SPECIFIC, 5 pending CTO resolution)
- `[STAUDT.CHART-ALIGN-FE]` Standing by at inbox-watch for DS CHART-ALIGN artifact-ready MCP (no-op TO likely)
