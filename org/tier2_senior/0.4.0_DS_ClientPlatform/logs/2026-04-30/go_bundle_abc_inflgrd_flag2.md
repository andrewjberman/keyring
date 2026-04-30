# Session Log: GO Bundle A+B+C — INFGRD FLAG 2 + Validate Config Gaps
**Agent:** 0.4.0_DS_ClientPlatform_B  
**Date:** 2026-04-30  
**TO:** ADVI_INFGRD.FLAG2.ds-c07-rep-id-fix  
**Triggered by:** COO GO bundle post-RAVC4 (INFLV2.002 explicit validation pass)

---

## Bundle Summary

| Item | Surface | Commit | Status |
|------|---------|--------|--------|
| A | Validate config gap fixes (INF_09 field + INF_D_04 artifact path) + ADHC_COMPIL_V2.001 TO | `9678bec4d` | DONE |
| B | ADVI_INFSHIP_A2 PRD pre-read + concern notation | This log | DONE |
| C | INF_C_07 FLAG 2 advisor_key override via accounts_v2 | `ef4f375f8` | DONE |

---

## Item A: Validate Config Fixes

Two pre-existing gaps surfaced during INFLV2.002 explicit validation pass (2026-04-30):

**INF_09 (`data/orion/scripts/gold/gold_validate_config.yaml`):**
- Config had `path: "firm_aua"` on both checks (nonzero + threshold band)
- Actual `partner_analytics.json` field is `total_aua` (confirmed by direct S3 pull + jq)
- Fixed: both check paths updated to `total_aua`; check names updated; why fields updated with gap-flag attribution

**INF_D_04:**
- Config had `primary_artifact: "platinum/firm/client_portal_summary.json"` — dead path (renamed per 2026-04-30 naming fix)
- Actual artifact: `platinum/firm/clients_tab.json`
- Config had `path: "total_aua"` — clients_tab structure is `{headline: {aua: ..., client_count: ...}, clients: [...]}`
- Fixed: artifact path updated; field path updated to `headline.aua` (dot-notation resolves via `_resolve_path` in extract_validate.py)

**ADHC_COMPIL_V2.001 standing TO:**
- Authored `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADHC_COMPIL_V2.001.ds-comp-validate-orion-config.md`
- Root cause: `comp-validate` hardcoded to BD config path; Orion pipeline has no CLI support
- Priority: LOW / staged; workaround is manual validation against Orion config
- 5 tasks: `--pipeline` flag (bd/inf/all), standalone validators path update, `--list` output, docstring+CLAUDE.md, acceptance test

---

## Item B: ADVI_INFSHIP_A2 PRD Pre-Read Observations

Read `docs/architecture/ADVI_INFSHIP_A2.md` in full. Key observations for DS BASE pre-consult:

### 1. Endpoint Catalog Coverage Risk (§2.1)
8 endpoints cataloged. Status breakdown:
- 4 currently used in production chain
- 3 confirmed-pullable (not yet used) — highest value: `accounts_v2` (rep_id coverage)
- 1 timeout-blocked — represents a hard constraint; Path A cannot assume this endpoint is reliable

**Phase 0a concern:** PRD describes Path A as "direct Orion API pulls" but the timeout endpoint is listed without a workaround. Before committing to Path A for any new metric, DS BASE should confirm which endpoints are still timing out and what the fallback is. C_07 FLAG 2 demonstrates `accounts_v2` works (Path A empirical data point). The accounts endpoint doesn't time out.

### 2. Schema Drift Risk (§4.3)
Tax coverage anomaly (22% field completeness) flagged as empirical evidence of schema drift risk class. This is the broadest Path A concern: Orion API schema is not frozen. Fields that are present today may reduce coverage or disappear across upgrades.

**Recommendation for DS BASE consult agenda (§5.1, Q3):** ask whether Orion has a schema stability commitment (SLA or changelog) for the 8 endpoints. Without it, Path A pipelines need a field-presence gate at every silver ingestion (similar to SCOPEFIX audit JSON pattern but for API fields).

### 3. C-Chain Rerun Coupling (Path C risk)
PRD §3.2 flags that Path C (chain-rerun-coupled) requires full B+C chain re-run for attribution corrections. FLAG 2 fix is a concrete example of WHY Path A is preferable for attribution: `accounts_v2` carries clean rep_id without requiring INF_B_00/INF_A_00 re-run. The C_07 override decouples attribution freshness from the heavy chain.

### 4. No Phase 0a Gate Currently
PRD references "Phase 0a investigation surface" but does not define a completion criterion. Before DS BASE greenlights Phase 1 (full Path A migration), there should be a Phase 0a DONE definition. Suggest: Phase 0a complete when all 8 endpoints have confirmed coverage + field-stability assessment + 2-week pull stability log.

---

## Item C: INFGRD FLAG 2 Fix — INF_C_07 advisor_key Override

### Problem
`accounts_dimension` `advisor_key` is derived from `rep_name` via TRN data. TRN data covers all firms including Keil, so Keil rep names contaminate the `advisor_key` slug computation in INF_A_00 → INF_C_07 → all D-chain downstream views (account_team, rel_architect_lookup, leaderboard, advisor_client_detail).

### Root Cause Chain
```
INF_B_00 (TRN parquet ingest, multi-firm)
  → INF_A_00 (derives advisor_key from rep_name — Keil names included)
  → INF_C_07 trusts whatever advisor_key is in accounts_dimension
  → account_team / rel_architect_lookup carry Keil slugs
  → INF_D_00c leaderboard / INF_D_02 advisor_client_detail show wrong books
```

### Fix
Added `_apply_accounts_v2_advisor_key_override(df)` in INF_C_07:
- Loads latest `silver/api_dims/accounts_v2/snapshot_date=*/data.parquet` partition
- Slugifies `representative_name` → `advisor_key` override (same normalization as INF_A_00: lowercase, `[^a-z0-9_]+` → `_`, strip, slice to 60 chars)
- Merges on `account_id`, uses `combine_first` to override
- WARN-and-pass fallback if accounts_v2 partition absent (preserves existing behavior)

Added `_latest_silver_partition(prefix)` helper (same pattern as INF_I_D03 DIAGFIX.011 Phase 5 surgical override).

Also added Q9 `new_accounts_rep` placeholder exclusion — Orion assigns this key before real advisor is attached. Q9 exclusion keeps it in firm-level totals (INF_C_01/INF_C_03 paths) but strips it from advisor-scoped views (account_team, rel_architect_lookup).

### Pre-Commit Gate
Passed: `python -m py_compile`, `ds-precommit-check.py` (stdlib AST scanner), `ruff check --target-version py39`.

### Commits
- `ef4f375f8` — `fix(INFGRD.FLAG2): INF_C_07 advisor_key override via accounts_v2 rep_id attribution`

### A2 PRD Framing
This fix is an empirical Phase 0a data point for ADVI_INFSHIP_A2 Path A:
- Demonstrates that `accounts_v2` is a reliable, pullable endpoint (no timeout)
- Attribution correction applied at C_07 level without B-chain re-run proves that API-sourced dims can be injected mid-chain as surgical overrides
- If Path A migration proceeds, the C_07 pattern (load partition → slugify → combine_first) is a reusable template for other advisor-scoped attribution corrections

---

## Close State

- Both commits pushed to CLOUD (`9678bec4d`, `ef4f375f8`)
- `.comp-graph/.agent_context` updated to `TO_ID=ADVI_INFGRD.FLAG2.ds-c07-rep-id-fix`
- RAVC4 to COO pending (this log)

---

## Next (not DS~B scope)
- DIAGFIX.012: DS BASE scope — C_07 FLAG 2 lays groundwork but the leaderboard discrepancy (Lee 336 vs 617) resolves at DIAGFIX.012 Phase 4 (B-chain re-run with rep_id-based accounts_dimension)
- ADHC_COMPIL_V2.001: standing LOW TO; no action until Orion chain runrate increases
- ADVI_INFSHIP_A2 Phase 0a: DS BASE consult agenda in §5.1 (3 questions re: endpoint stability, schema drift, migration sequencing)
