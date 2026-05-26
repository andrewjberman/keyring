# ADVI_DEMOV1 — Andrew UAT 2026-05-26 backend findings (routing to 0.7.0_AE_CloudOps + DS~C/~D collaborators)

**From:** 0.4.0_DT_ClientPlatform (TO-009 Phase 2 UAT scribe)
**To:** 0.7.0_AE_CloudOps (infra owner: EC2 demo-transform-runner, IAM, bucket) + 0.4.0_DS_ClientPlatform~C/~D (transform code authors); CC 2.0.0_SA_COO (routing); CC 1.0.0_SA_CTO (PRD §6.1 wording)
**Date:** 2026-05-26 ~17:42Z (v2 revision per Andrew clarification on multiplier + account-# spec + AE owner)
**UAT artifact:** portal local dev server (port 5175) serving DEV @ `03a85441`; Andrew on `andrew@opalinvest.com` (internal-staff + admin + isDev) selected "Demo" from `ALL_PARTNER_FIRMS` dropdown

---

## v2 revision changes vs v1 (commit ad37838b1)

1. **AE owner reroute:** v1 said 0.6.0_AE_PartnerETL. v2 says **0.7.0_AE_CloudOps** per git-log audit. 0.7.0 owns demo-transform-runner EC2 + IAM + opal-data-demo bucket (TO-001/.005/.007). 0.6.0_AE_PartnerETL handles BD-pipeline only — does NOT own demo work. v2 also adds **0.4.0_DS_ClientPlatform~C/~D** as collaborators (they authored `demo_transform.py` + `fake_identities.py`).
2. **F1 multiplier:** v1 said "× 2/3" (× 0.667). v2 says **× 3** (Andrew direct clarification 2026-05-26 ~17:42Z: *"just incorporate some function to multiply all the numbers by 3"*).
3. **F2 spec:** v1 said "redact / mask". v2 says **generate fake account strings of pattern `OPAL######`** (Andrew direct: *"make up account strings like OPAL######"*). Also pin-pointed the data-source JSON path.

---

## Owner attribution (from git-log audit on `data/demo/scripts/transform/` + ADVI_DEMOV1 commits)

| Lane | Scope | Recent commits |
|---|---|---|
| **0.7.0_AE_CloudOps** (base) | demo-transform-runner EC2 + IAM + bucket + ec2-manifest + pipeline-inventory + snapshot-clean code-write (3cffa512b) | TO-007 SHIPPED; LD-0077 readouts |
| **0.7.0_AE_CloudOps~C** (lane-C) | initial demo-transform-runner EC2 + IAM + bucket (TO-001 / TO-005) | 16fd50aa6, 206cd4483, 611926658, 5e32c0f1d, 322a8fba0 |
| **0.4.0_DS_ClientPlatform~C** (lane-C) | `demo_transform.py` + `fake_identities.py` authoring (two-pass deterministic pseudonymizer; PII inventory; apply-mode live-write) | 7d6b1b835 (TO-002 transform COMPLETE), 173d4b43f (TO-004), 30333d1e3, c61d4da6e, dbf170b32 |
| **0.4.0_DS_ClientPlatform~D** (lane-D) | TO-006 Path B structured-PII-tagging primitive + factory.seal_real_names + FN-1 regression-test fixture | 115af15f8, 50176a86e |

**Recommended primary routing:** Andrew delivers brief to **0.7.0_AE_CloudOps** (active live agent, present session, demo-pipeline owner per current closeout). 0.7.0 coordinates with DS~C/~D as needed for transform-code edits — DS~C/~D may have been killed post-TO-007 closeout; if so, COO/MSTR can spawn-with-direction same pattern as my own DT 0.4 spawn today.

---

## Phase 2 UAT outcome (TO-009 Phase 2 scope)

| Smoke | Result |
|---|---|
| **A — Partner-selector visibility** | PASS — "Demo" appears alongside 49 Financial + Inflection Wealth Management |
| **B — Demo-view renders 3-tab layout** | PASS — Distribution + Advisors + Books canonical render |
| **C — Data populates** | PASS-WITH-FINDINGS — surfaces populate from `opal-data-demo`; finding F1 below |
| **D — No PII leak (name pseudonymization)** | PASS-WITH-FINDINGS — **name pseudonymization excellent**; account-# class gap is finding F2 below |

**Andrew sovereign disposition:** *"all of that is backend issue, we can proceed with our frontend task orders and work on this subject unhindered."* Frontend UAT scope = PASS; backend findings split-routed; TO-009 Phase 3+4 SHIPPED in same operational window (portal-v2.1.73 + parent CLOUD 794cf9c0a).

---

## Findings

### F1 — Numbers NOT multiplied by 3 (route: 0.7.0_AE_CloudOps + DS~C/~D)

**Andrew citation (verbatim 2026-05-26 ~17:42Z, supersedes earlier ~17:30Z framing):**
*"just incorporate some function to multiply all the numbers by 3"*

**Scope:** every `$`-denominated field + every count field in the demo dataset currently mirrors the 49 Financial source 1:1. Target: each numeric value multiplied by **3** (3.0×) during the demo transform pass — making demo headline larger than 49F so the demo presents as a "bigger book" rather than as 49F.

**Implementation suggestion:** single chokepoint multiplier in the Pass-2 walk of `data/demo/scripts/transform/demo_transform.py` (the JSON-path-aware engine). All `int`/`float` value-rewrites at numeric JSON paths × 3.0. **Critical:** uniform application across ALL numeric fields preserves Σ-identities (leaderboard → firm-headline; identity_1 decomposition; per-window TWR/epsilon balances per PRD §3 binding constraint 2). Per-field jitter breaks identities; single-chokepoint multiplier safe.

**Out-of-scope for the multiplier (verify):**
- Ratios / percentages (bps, twr_pct, epsilon — these ARE proportional and shouldn't change shape; only `$` and counts should ×3).
- Window-aligned dates / timestamps (no scaling).
- Account/client/advisor IDs (handled by F2 below).

**Affected fields (non-exhaustive):**
- `leaderboard.json` per-advisor: `aua_total`, `nna_ytd`, `nna_qtd`, `client_count`, `account_count`
- `summary.json` per-advisor + per-client: balance fields, fee-$ fields, AUA fields
- Distribution-tab cohort histograms: bin counts
- Fee Summary: every `$` field
- Books drill: every `$` field
- `cumulative_chart`: `value` series

**PRD impact:** PRD v0.1 §4 R7 "verbatim" → "scale by 3.0 uniform across numeric fields (preserving ratios + dates + IDs)". v0.4.2 amendment when fix lands; route to ws CTO.

---

### F2 — Account numbers in Fee Summary still real-looking; need `OPAL######` fake pattern (route: 0.7.0_AE_CloudOps + DS~C/~D)

**Andrew citation (verbatim):** *"the account numbers in 'Fee Summary' page are still displaying, which must be adjusted. ... make up account strings like OPAL###### (specifically in the fee summary panel, wherever that is sourcing data from maybe you can check and include that in this little brief on the changes)"*

**Data-source trace (Fee Summary panel):**
- Component: `portal/src/pages/AdvisorIntelligence/_shared/tabs/FeeSummaryPanel.tsx`
- Renders: `data.by_account[].account_id` at table row line 488 (visible "Account" column).
- Data prop: `FeeSummaryByAccount` type
- Source: `clientSummary.fee_summary` (per `AdvisorBookView.tsx:299` + `ClientsTab.tsx:414` + `AdvisorBookClientDetail.tsx:170`)
- S3 path: `s3://opal-data-demo/platinum/clients/{client_id}/summary.json` at JSON path **`.fee_summary.by_account[].account_id`**
- Transform-side input: `s3://opal-data-bd/platinum/clients/{real-client-id}/summary.json` at the same JSON path

**Diagnosis (most likely):** R1 JSON-path-aware-gap. The pseudonymizer's PII-field map in `fake_identities.py` does NOT include `.fee_summary.by_account[].account_id` as a rewritable path. Bd source has real account numbers (probably 9-digit numerics or BD-internal IDs); they pass through to demo unchanged — failing Smoke-D account-#-class even though name-class is clean.

**Target spec (per Andrew):** generate fake account strings matching pattern **`OPAL######`** (literal "OPAL" prefix + 6 deterministic-faker digits, e.g. `OPAL000001`, `OPAL427819`). Recommendation:
- Deterministic mapping `real_account_id` → `OPAL{seeded_6digit}` in the Pass-1 mapping table (same primitive as advisor-slug + client-z-ID + firm-faker mappings already established).
- Add JSON path `.fee_summary.by_account[].account_id` (+ any other account-id-class paths surfaced by R1 audit-extension) to the rewritable-path map.
- Re-run R5 leak scanner with account-#-class extension (verify no `BD-internal-id-format` strings remain anywhere in demo bucket).

**Investigation prerequisite:** AE 0.7 pulls a sample artifact from demo + bd:
```
aws s3 cp s3://opal-data-demo/platinum/clients/{any-demo-client-id}/summary.json /tmp/demo-summary.json
aws s3 cp s3://opal-data-bd/platinum/clients/{any-bd-client-id}/summary.json /tmp/bd-summary.json
jq '.fee_summary.by_account[].account_id' /tmp/demo-summary.json /tmp/bd-summary.json
```
If demo values == bd format/values → R1 gap confirmed; fix in `fake_identities.py` PII-field map + re-run transform.

**Other paths to audit (likely have account_id-class fields too):** `platinum/accounts/{id}/...`, `platinum/clients/{id}/book.json`, `platinum/clients/{id}/decomposition.json`, anywhere the transform engine walks an `account_id` JSON-path. R1 audit-sweep at the same time as the field-map extension.

**Verify-channel candidate (CVO):** post-fix Mode-A surface-level account-#-class extension to the R5 leak scanner.

---

### F3 — "Data Source" label text edit (FRONTEND fix; NOT AE scope; ~3-line patch)

**Andrew citation (verbatim):** *"the 'Data Source' for Demo should be edited from 'Black Diamond Connected: Source: SS&C Black Diamond Wealth Solutions.' to 'Database Connected: Source: Lone Pine Analytics.'"*

**This is a frontend patch — already located in 3 places in `portal/src/pages/AdvisorIntelligence/_partners/demo/`:**

| File | Line | Current | Target |
|---|---|---|---|
| `demo/index.tsx` | 262 | `<span ...>Black Diamond Connected:</span> {BD_SOURCE_ATTRIBUTION}` | `<span ...>Database Connected:</span> {DB_SOURCE_ATTRIBUTION}` (rename constant import) |
| `demo/constants.ts` | 8 | `export const BD_SOURCE_ATTRIBUTION = 'Source: SS&C Black Diamond Wealth Solutions.'` | `export const DB_SOURCE_ATTRIBUTION = 'Source: Lone Pine Analytics.'` |
| `demo/layout.ts` | 20 | `primaryCustodian: 'SS&C Black Diamond',` | `primaryCustodian: 'Lone Pine Analytics',` |

**Routing:** 0.4.0_DE_ClientPlatform (frontend authorship lane) — small TO `ADVI_DEMOV1.010` candidate. **NOT 0.7.0_AE_CloudOps scope.**

**DT 0.4 lean:** standalone TO-010 next /work tick after F1+F2 land (keeps F1+F2 close-out clean; PROD-promote on next portal-vX.Y.Z cycle).

---

## Routing summary

| Finding | Class | Primary owner | Collaborator | Effort |
|---|---|---|---|---|
| **F1** (numbers × 3.0) | data-transform | **0.7.0_AE_CloudOps** | 0.4.0_DS_ClientPlatform~C/~D | medium — single chokepoint multiplier in Pass-2 walk + full EC2 transform re-run + R5 re-pass |
| **F2** (account-# `OPAL######`) | data-transform PII-field-map extension | **0.7.0_AE_CloudOps** | 0.4.0_DS_ClientPlatform~C/~D | small-medium — add JSON-path to PII map in `fake_identities.py` + deterministic mapper + R5 account-#-class extension + transform re-run |
| **F3** (data-source label) | frontend | **0.4.0_DE_ClientPlatform** (or 0.4.0_DT for the deploy) | — | tiny — 3-line patch in `demo/{index.tsx,constants.ts,layout.ts}`; TO-010 |

**TO-009 (frontend Phase 6 ship) — SHIPPED unhindered per Andrew direct.** Portal/PROD now at `b7b201a610` (cherry-pick of `03a85441`); parent CLOUD `794cf9c0a`; tag `portal-v2.1.73`. opalinvest.dev CloudFront propagation in flight via `.github/workflows/deploy.yml`. F1+F2 backend fix lands on next transform re-run; F3 frontend lands as standalone TO-010.

---

## PRD wording follow-ons (FYI ws CTO)

- **§4 R7 "verbatim" → "scale by 3.0 uniform across numeric fields"** (v0.4.2 minor amendment with F1 fix)
- **§1 + §6.1 "Cognito login" / "demo@demo.test" language** (sister to F3 wording-rot; PRD describes Cognito auth but Opal uses DynamoDB user table — see DT 0.4 memory `project_opal_auth_dynamodb_never_cognito`)
- **§6.1 TO-VAL-FE smoke scope** could explicitly mention account-#-class as a Smoke-D check separate from name-class (would have caught F2 at design time, not UAT time)

---

**0.4.0_DT_ClientPlatform — TO-009 UAT scribe (v2 revision per Andrew clarification)**
**archetype:** SCRIBE+COORDINATE
