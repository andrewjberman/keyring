# Session Log — HISTBF.003 Client Universe Fix (294 → 313)

**Agent:** 0.4.0_DS_ClientPlatform  
**Date:** 2026-04-30  
**Session type:** Context-resumption continuation  
**Session window:** ~19:00Z – 19:45Z

---

## Context at Resumption

Continued from prior session (session_diagfix012_ph5_histbf003_scripts.md). HISTBF.003 pull
scripts had been authored and committed (f4190d327). Andrew raised a blocking question:

> "We need to be categorical and have everything that has ever come up because remember the
> whole purpose of this is to build around full historical time series so we can't exclude anything."

This triggered the 294 vs 314 client source investigation (Wave D item).

---

## Investigation Summary

### Root Cause of AUM Gap ($197.16M vs $198.16M Orion UI)

Prior session had concluded the gap was definitively traced to a custodian filter:

- `build_accounts_v2()` in `convert_orion_api_to_silver.py` filtered to `custodian == 'Fidelity_Inflection'` only
- NewPortfolio contains a second Orion custodian code, `Fidelity_LH`, covering 9 Inflection-rep households (~$1,112,972 current AUA)
- These 9 households were entirely excluded from accounts_v2 silver, the accounts map in pull_inflection_transactions_rest.py, and the client_ids list in pull_inflection_performance_rest.py

### 294 vs 313 Client Gap

Three categories of missing clients identified:

| Category | Count | AUA Impact | Source |
|----------|-------|-----------|--------|
| Fidelity_LH households | 9 | ~$1.1M current | In NewPortfolio, wrong custodian filter |
| Ghost HH with historical AUA | 8 | $0 now, $100K–$800K historically | In rep_mapping; absent from NewPortfolio |
| True zero-history HH | ~10 | $0 always | In rep_mapping; no accounts anywhere |

**Ghost household historical AUA confirmed via Assets API probes:**
- hh=132 (Douglas Stubsten): $232K AUA at 2022-01-03, $0 now
- hh=274 (Lisa Zukaitis): $129K AUA at 2022-01-03, $0 now
- hh=327 (Nadia Cook): $601K AUA at 2022-01-03, $0 now
- hh=474 (Zosia Damis): $459K AUA at 2022-01-03, $0 now
- hh=546 (Brian Markley): $279K AUA at 2022-01-03, $0 now
- hh=19 (Adam Marshall): $798K AUA at 2024-01-02, $0 now

These households must be included in the full backfill time series — omitting them creates
a silent data gap in the 2020–2025 historical record.

**Ghost household transactions:** 13 "orphan" account_ids (41, 87, 235, 331, 672, 707, 712,
727, 759, 765, 788, 1086, 1219) from historical gold holdings files map to ghost household_ids
(19, 116, 132, 274, 327, 366, 474, 546). These accounts exist in Orion (`custodian=Fidelity_Inflection,
status=Normal Downloading, currentValue=$0.00`) but are absent from NewPortfolio — exclusion
reason unknown. Their transactions are inaccessible via the account-level endpoint without
known account_ids from a source other than NewPortfolio.

---

## Work Done This Session

### 1. Custodian Filter Expansion — `convert_orion_api_to_silver.py` (commit 7ef7d7ccf)

`build_accounts_v2()` line 354:
```python
# Before
inf_mask = df['custodian'] == 'Fidelity_Inflection'

# After
inf_mask = df['custodian'].isin(['Fidelity_Inflection', 'Fidelity_LH'])
```

Effect: accounts_v2 silver now captures all Fidelity_LH accounts. Next `convert_orion_api_to_silver.py --dim accounts_v2 --upload` run will produce a 313-household-capable silver snapshot.

### 2. Performance Script Client Source — `pull_inflection_performance_rest.py` (commit 7ef7d7ccf)

- Replaced `ACCOUNTS_V2_PREFIX` with `HH_REP_MAP_PREFIX = "silver/api_dims/household_rep_mapping/"`
- Replaced `_latest_accounts_v2_key()` + old `_load_inflection_client_ids()` with:
  - `_latest_hh_rep_map_key(s3)` — finds latest household_rep_mapping silver snapshot
  - `_load_inflection_client_ids(s3)` — extracts 313 household_ids from rep_mapping silver

Effect: performance pull now iterates all 313 Inflection households. Ghost households return
404 or empty details — both handled gracefully (logged as INFO, counted as empty/404).

### 3. Transactions Script Accounts Source — `pull_inflection_transactions_rest.py` (commit 7ef7d7ccf)

- Added `HH_REP_MAP_PREFIX = "silver/api_dims/household_rep_mapping/"`
- Added `_latest_hh_rep_map_key(s3)` helper (same pattern as performance script)
- Rewrote `_load_accounts_map(s3)`:
  - Stage 1: loads 313 client_ids from household_rep_mapping silver (authoritative universe)
  - Stage 2: loads account_ids from accounts_v2 silver (now includes Fidelity_LH post-filter-fix)
  - Ghost households (in rep_mapping but absent from accounts_v2) logged as WARN with household_id list; produce zero API calls

**Remaining gap:** ghost households' orphan account_ids are inaccessible via NewPortfolio. The
13 known orphan accounts discovered from gold holdings files lack a confirmed account→household_id
mapping derivable from local data. Flagged for follow-up (HISTBF.003 ghost account discovery
sub-task before Phase 1 GO).

---

## Validation

All three files passed `ds-commit-gate.sh`:
- `python -m py_compile`: PASS
- AST undefined-name scan: PASS
- `ruff check --target-version py39`: PASS

---

## Commits This Session

| Commit | Description |
|--------|-------------|
| `7ef7d7ccf` | fix(ADVI_INFLEC.HISTBF.003): expand client universe to 313 households — Fidelity_LH + ghost HH |

Pushed to `origin/CLOUD`.

---

## Open Items Carried Forward

| Item | Gate | Status |
|------|------|--------|
| HISTBF.003 Phase 1 bronze execution | CTO+COO wave plan GO | ON HOLD |
| accounts_v2 silver re-run with LH expansion | Next `convert_orion_api_to_silver --dim accounts_v2 --upload` | Unblocked (script fixed) |
| Ghost household orphan account_ids | Confirm account→household mapping for 13 known orphans; add to transactions pull | Pre-Phase-1 follow-up |
| HISTBF.004 silver backfill | HISTBF.003 Phase 1 close + AE S3 path ACK | ON HOLD |
| INF_D_08 NMEC run | HISTBF.003 Phase 1 bronze at `bronze/orion-api/probe/transactions.csv` | ON HOLD |
