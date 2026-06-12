# DEBTSCAN ledger: comp-adapter-audit hardcoded-prefix tool defect

**Class:** TOOL-DEFECT
**Family:** MANUFACTURED-DRIFT (a tool fabricates schema-drift findings by comparing against the wrong live envelope)
**Incident anchor:** T1b false-positive (getPlatinumClientDetailStatic "schema drift"), 2026-06-12
**Found + fixed by:** 0.4.0_DE_ClientPlatform (CTO-dispositioned to DE lane 215721Z; root-caused during T1b verify-before-fix)
**Severity:** MEDIUM — the false drift almost became a false FIX (a blind T1-style backfill would have corrupted the client adapter `InflecClientDetailRaw` with advisor-shaped fields). The "near-corruption" is the load-bearing lesson (CTO).

---

## Defect

`org/modules/graph/adapter_audit_cli.py` `_fetch_s3_raw_fields` **hardcoded** the S3 prefix list to
`s3://opal-data-inf/platinum/advisors/{inflection_wealth_management,peter_lee}/` (old lines ~151-156)
and fetched `{advisors-prefix}/{artifact}`. For ANY adapter whose real fetch path is NOT under
`advisors/` (client adapters under `clients/{id}/`, firm adapters under `firm/`), the tool fetched the
**advisor** envelope and diffed it against the **non-advisor** raw type → every advisor-shaped field
("book", "role_breakdown", "fee_summary", "relationship_stacked_periods", "tax_exposure"…) reported as
SCHEMA-DRIFT, and the real client/firm fields reported as TYPE-ONLY (absent from S3). 100% manufactured.

## Incident (T1b)

T1b was filed as a "getPlatinumClientDetailStatic schema drift" portal fix (sibling of T1's advisor
type-backfill). Verify-before-fix: ground-truth `aws s3 cp s3://opal-data-inf/platinum/clients/100/
detail.json` = top-level keys `[accounts, advisor_key, data_as_of, display_name, firm_id, generated_at,
household_id, summary]` = EXACT 8/8 match to `InflecClientDetailRaw`. Portal type was CORRECT; the
"drift" was the tool fetching the advisor envelope. A blind backfill would have injected advisor
fields into the client adapter.

## Fix (condition a)

Derive the S3 prefix from the adapter's ACTUAL fetch path — no second hardcode:
- `_derive_s3_target(function_body, raw_type, artifact)` reads the `apiRequest<raw_type>(\`url\`)` call
  + resolves any `${base}` var it interpolates, then matches the path segment `firm` | `clients` | `advisors`.
- `firm/` → `s3://opal-data-inf/platinum/firm/{artifact}`; `clients/`|`advisors/` → `_sample_id()` lists a
  real id under that segment (deterministic sorted-first) → `…/platinum/{seg}/{id}/{artifact}`.
- Artifact is tied to the raw_type's own apiRequest URL (not the first `.json` in a multi-fetch body).
- When no static `.json` exists (Lambda-backed adapters, e.g. the BD branch of getPlatinumAdvisorSummary
  fetching `/partners/books/advisor/{id}/platinum-summary`) → returns no envelope → honest UNVERIFIED
  (the old tool forced these against `book.json`, a cross-source mismatch).

## Regression (condition c)

- CLIENT: `comp-adapter-audit getPlatinumClientDetailStatic` → S3 8 keys, **PASS (0 findings)** (was 46 findings / 43 manufactured drift).
- ADVISOR: `getPlatinumAdvisorSummaryStaticInflection` → correctly fetches `advisors/{id}/book.json` (16 keys, 18 typed); residual nested warns are real same-type findings, NOT cross-envelope artifacts.

## YAML sweep (condition b — regenerate ONLY affected)

Manufactured-drift class = non-advisor adapters diffed vs the advisor envelope. Regenerated + verified 0 advisor-shaped drift:
- `getPlatinumClientDetailStatic.yaml`: 46 findings → **0**.
- `getPlatinumClientSummary.yaml`: 39 drift / 7 advisor-shaped → **0 / 0**.
- `getPlatinumFirmDashboard.yaml`: 25 drift / 8 advisor-shaped → **11 / 0** (11 residual = real FeeEfficiencyResponse findings).
- Removed stale `getAdvisorBook.yaml` (its function was deleted in DC-round-2 `0ac642ad`).
- Advisor adapters (getPlatinumAdvisorSummary/StaticInflection/DrilldownSummary/Timeseries) were NOT
  manufactured-drift (advisor-vs-advisor envelope was correct even under the old hardcode) → left as-is.

## Follow-on / pointers

- The same manufactured-drift class would hit any FUTURE non-advisor adapter audited before this fix —
  re-run `comp-adapter-audit <fn>` (now self-correcting) when adding one.
- Related: ADVI_49NNAFIX (DE brief `docs/briefs/advi-49nnafix-project-request-20260612.md`) — the
  inflection canonical-NNA publisher is `org/modules/graph/gold-nan/INF_D_00f.advisor_nna_canonical.yaml`;
  the 49F/bd equivalent is what's missing.

*Filed by 0.4.0_DE_ClientPlatform 20260612. CC CTO + CVO.*
