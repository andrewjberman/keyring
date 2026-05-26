# ADVI_DEMOV1 — Andrew UAT 2026-05-26 backend findings (routing to 0.6.0_AE_PartnerETL + frontend disposition)

**From:** 0.4.0_DT_ClientPlatform (TO-009 Phase 2 UAT scribe)
**To:** 0.6.0_AE_PartnerETL (primary owner for F1 + F2); CC 2.0.0_SA_COO (routing); CC 1.0.0_SA_CTO (PRD §6.1 wording)
**Date:** 2026-05-26 ~17:12Z
**UAT artifact:** portal local dev server (port 5175) serving DEV @ `03a85441`; Andrew on `andrew@opalinvest.com` (internal-staff + admin + isDev) selected "Demo" from `ALL_PARTNER_FIRMS` dropdown

---

## Phase 2 UAT outcome

| Smoke | Result |
|---|---|
| **A — Partner-selector visibility** | PASS — "Demo" appears alongside 49 Financial + Inflection Wealth Management |
| **B — Demo-view renders 3-tab layout** | PASS — Distribution + Advisors + Books canonical render |
| **C — Data populates** | PASS-WITH-FINDINGS — surfaces populate from `opal-data-demo`; finding F1 below |
| **D — No PII leak** | PASS-WITH-FINDINGS — **name pseudonymization excellent**; finding F2 below |

**Andrew sovereign disposition (verbatim):** *"all of that is backend issue, we can proceed with our frontend task orders and work on this subject unhindered."* Frontend UAT scope = PASS. Backend findings route to AE 0.6.0 + frontend label-edit to DT pod (F3) separately. TO-009 Phase 3 (cherry-pick → PROD) proceeds in same operational window per Andrew direct.

---

## Findings

### F1 — Numeric values NOT scaled by 2/3 (data transform gap; route to AE 0.6.0)

**Andrew citation (verbatim):** *"I thought I made it clear that all the numbers should be cut down by 2/3? Looks like the DT here did not apply a transformation to make that happen."*

**Scope:** every `$`-denominated field + every count field in the demo dataset currently mirrors the source 49 Financial value 1:1. Expected: each numeric value multiplied by 2/3 (0.667) during the demo transform pass, so the demo tenant does not visually mirror the actual 49 Financial scale.

**Likely fix location:** `data/demo/scripts/transform/demo_transform.py` value-rewrite pass — the pseudonymizer currently swaps identities (R1) but does not scale numerics (R7 was "verbatim pending Andrew call" — per PRD v0.1 §4 R7). Andrew's call landed here: scale to 2/3.

**Affected fields (non-exhaustive, in-scope for AE investigation):**
- `leaderboard.json` per-advisor: `aua_total`, `nna_ytd`, `nna_qtd`, `client_count`, `account_count`, `epsilon_*`, `twr_*`
- `summary.json` per-advisor + per-client: balance fields, fee fields, AUA fields
- Distribution-tab cohort histograms: bin counts
- Fee Summary: every $ field
- Books drill: every $ field

**Σ-identity preservation:** scaling by a constant 2/3 preserves Σ-identities provided the multiplier is applied uniformly across ALL numeric fields (including leaderboard → firm-headline reconciliation; identity_1 decomposition; per-window TWR/epsilon balances per PRD §3 binding constraint 2). **Recommend:** apply the 0.667 multiplier at a single chokepoint in the Pass-2 walk to avoid per-field drift.

**PRD-impact:** PRD §4 R7 needs amendment from "verbatim" to "scale by 0.667 (uniform across all numeric fields)." Route to ws CTO for v0.4.2 minor amendment when R7-fix lands.

---

### F2 — Account numbers in "Fee Summary" page still displaying (PII leak class; route to AE 0.6.0 first; verify-channel-class)

**Andrew citation (verbatim):** *"the account numbers in 'Fee Summary' page are still displaying, which must be adjusted."*

**Scope:** Fee Summary page (per-client view? per-advisor Books view?) renders account number values that appear to be raw / not-pseudonymized. The R5 leak scanner reportedly PASSED CLEAN at .007 closure (`opal-data-demo` parity to bd, no real names/IDs detected), so this is either:

1. **Pseudonymizer JSON-path-aware gap** — the account-number field path was not in the PII inventory; pseudonymizer didn't rewrite it. R1 says transform must be **JSON-path-aware, not field-name-driven** because field names are context-dependent (Phase 0 finding 3). Account-number field at `fee_summary.account_number` (or similar) may not have been catalogued.
2. **Display-but-fake leak** — pseudonymizer DID rewrite the account numbers (e.g., z-IDs → fake numerics), but the values are still displayed in the UI. Even if technically not real, "account numbers visible in demo" is a presentation concern Andrew flagged.

**Investigation steps for AE 0.6.0:**
- Pull a sample Fee Summary page artifact from `opal-data-demo` (e.g., `s3://opal-data-demo/platinum/clients/{demo-client-id}/fee_summary.json`).
- Compare account_number fields against `opal-data-bd` source.
- If demo values ≠ bd values (pseudonymized) → presentation-class issue; route to frontend (DT/DE pod) to mask/redact the field at render time for `firmId === 'demo'`.
- If demo values == bd values (not pseudonymized) → R1 gap; extend PII-field map + re-run transform.

**Verify-channel candidate:** CVO `/verify-channel` should re-run a Mode-A surface-level check on the Fee Summary surface specifically after fix (extending the R5 leak-scan coverage to account-number-class).

---

### F3 — "Data Source" label edit (FRONTEND fix; ~3-line patch — does NOT need AE 0.6.0)

**Andrew citation (verbatim):** *"the 'Data Source' for Demo should be edited from 'Black Diamond Connected: Source: SS&C Black Diamond Wealth Solutions.' to 'Database Connected: Source: Lone Pine Analytics.'"*

**This is a frontend fix** — already located in 3 places in `portal/src/pages/AdvisorIntelligence/_partners/demo/`:

| File | Line | Current | Target |
|---|---|---|---|
| `demo/index.tsx` | 262 | `<span ...>Black Diamond Connected:</span> {BD_SOURCE_ATTRIBUTION}` | `<span ...>Database Connected:</span> {DB_SOURCE_ATTRIBUTION}` (rename constant) |
| `demo/constants.ts` | 8 | `export const BD_SOURCE_ATTRIBUTION = 'Source: SS&C Black Diamond Wealth Solutions.'` | `export const DB_SOURCE_ATTRIBUTION = 'Source: Lone Pine Analytics.'` |
| `demo/layout.ts` | 20 | `primaryCustodian: 'SS&C Black Diamond',` | `primaryCustodian: 'Lone Pine Analytics',` |

**Routing:** DE 0.4_DE_ClientPlatform (frontend authorship lane) — small TO `ADVI_DEMOV1.010` candidate. **NOT in scope for AE 0.6.0** — AE doesn't own frontend; punting it here would cycle.

**Alternatives the COO/CTO can weigh:**
- (a) Tack onto current TO-009: extend DEV branch with the 3-line label patch as a follow-on commit; cherry-pick range to PROD instead of single commit. Adds ~10min to TO-009.
- (b) Standalone next-tick TO ADVI_DEMOV1.010: ship cleanly after current TO-009 closes; PROD-promote on next portal-vX.Y.Z cycle.
- (c) Bundle into ADVI_DEMOV1.006 follow-on if that surfaces.

DT 0.4 lean: **(b)** — keep TO-009 scope tight; F3 lands in a clean follow-on next /work tick.

---

## Routing summary

| Finding | Class | Owner | Effort |
|---|---|---|---|
| F1 (numbers × 2/3) | data-transform / backend | 0.6.0_AE_PartnerETL (with DS~C lane on transform-logic edit) | medium — single chokepoint multiplier; full re-run of transform on EC2 |
| F2 (account # PII / display) | data-transform OR frontend (TBD by investigation) | 0.6.0_AE_PartnerETL investigates first; routes back if frontend-class | small-medium — depends on Step 1 finding |
| F3 (data-source label) | frontend | 0.4.0_DE_ClientPlatform (pod-4 DE) | tiny — 3-line patch |

**TO-009 (current frontend ship) — UNHINDERED per Andrew direct.** Phase 3 cherry-pick `03a85441` → PROD proceeds same operational window. F3 frontend label-edit lands as next-tick TO-010 or follow-on (COO routing).

**PRD wording follow-on (FYI ws CTO):**
- PRD §4 R7 "verbatim" → "scale by 0.667 uniform across numeric fields" — v0.4.2 amendment when F1 fix lands
- PRD §1 + §6.1 "Cognito login" / "demo@demo.test" UAT path — wording rot (see DT 0.4 prior FYI `20260526T163549Z` + correction `20260526T163616Z`); fold into next minor revision

---

**Closing note:** Andrew's UAT was decisive + the framing "all backend" + "proceed unhindered" + the brief itself is the formalization. Frontend UAT scope = PASS; backend = enumerated findings ready for collective AE handling. F3 split out as frontend-not-AE for clean routing.

**0.4.0_DT_ClientPlatform — TO-009 Phase 2 UAT scribe**
**archetype:** SCRIBE+COORDINATE
