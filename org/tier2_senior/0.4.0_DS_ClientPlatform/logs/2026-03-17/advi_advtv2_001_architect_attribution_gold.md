# Architect Attribution Gold Productionization — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-17

## Objective

Productionize the architect attribution decision tree (validated in `.tmp_architect_attribution.py` on 2026-03-13) into the gold layer pipeline. New script 08b writes a deterministic attribution of every funded account to one of 19 true architects, replacing the raw `architect` field as the canonical assignment for all downstream ADV views.

---

## Work Completed

### 1. Modified `00_build_accounts_dimension.py` (Req 4, 5)

- Added `consultant` and `additional_advisor` to `TXN_ACCOUNT_COLS` — these fields exist in silver transactions but were previously dropped during the gold build. They are needed for T11-T15 in the attribution tree.
- Added both columns to `output_cols` list so they appear in `accounts_dimension_latest.parquet`.
- Added normalization: `"Olivia Shin"` -> `"Liv Shin"` (confirmed typo duplicate with overlapping relationship, per 2026-03-13 investigation).
- Fixed emoji in `save_dimension()` print statement (CLAUDE.md rule 13).

### 2. Created `08b_build_architect_attribution.py` (Req 1, 3)

New gold script implementing the full T0-T16 decision tree:
- **T0:** Dynamically computes 19 true architects from AUA >= $5M, rels >= 5, not 49F House/Unassigned, active in trailing 12M.
- **T1-T4:** Direct architect, implementor (is true, 80%, 60%).
- **T5:** Relationship inheritance pass 1.
- **T6-T7:** Portfolio group (true, junior 80%).
- **T8:** Relationship inheritance pass 2.
- **T9:** Local relationship 60% pairing.
- **T10:** Relationship inheritance pass 3.
- **T11-T13:** Consultant (true, 80%, 60%).
- **T14-T15:** Additional advisor (true, 80%, 60%).
- **T16:** Relationship inheritance pass 4.
- Scoped to FUNDED accounts only (from account_performance).
- Outputs: `architect_attribution.parquet` (per-account) + `rel_architect_lookup.parquet` (per-relationship modal).
- Conservation check: resolved + unresolved = total funded accounts.

### 3. Modified `08_build_nna_aua_by_advisor.py` (Req 2)

- `load_relationship_advisors()` now reads `gold/views/rel_architect_lookup.parquet` from S3 instead of deriving from raw accounts_dimension.
- If the lookup file is missing, raises a clear error: "Run 08b_build_architect_attribution.py first."
- `save_rel_lookup()` is now a no-op (retained for caller compatibility). The file is written by 08b.
- `modal_str` function retained (other callers may use it, per constraint).

### 4. Updated `run_gold_layer.sh` (Req 6)

- Inserted `08b_build_architect_attribution.py` before `08_build_nna_aua_by_advisor.py` in both incremental and full modes.
- Updated dependency chain comments and header script list.

### 5. Updated `data_contract.xml`

- Added `architect_attribution.parquet` and `rel_architect_lookup.parquet` gold_script entries.
- Updated `accounts_dimension_latest.parquet` entry with new columns and normalization note.
- Updated `nna_aua_by_advisor.parquet` entry to note architect assignment sourced from 08b lookup.

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DevOps deploy instructions | `docs/briefs/devops-brief-architect-attribution.md` | DevOps |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| 08b reads previous run's nna_aua_by_advisor for T0 | Avoids circular dependency. The T0 filter uses aggregate stats (total AUA, num_relationships) which are stable across runs. First run uses the old (unattributed) advisor view to qualify architects — the architect list itself doesn't change. |
| save_rel_lookup in 08 is a no-op, not deleted | Constraint says do not remove modal_str; similarly, keeping the function signature avoids breaking callers while making 08b the single writer of the lookup file. |
| consultant/additional_advisor in TXN_ACCOUNT_COLS | These are standard BD transaction columns. If they don't exist in a given file, the `keep_cols` filter skips them gracefully. |
| FULL mode required for first deploy | Incremental mode won't backfill consultant/additional_advisor into existing accounts. |

---

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/00_build_accounts_dimension.py` | +consultant, +additional_advisor columns; +Olivia->Liv normalization; emoji fix |
| `data/black_diamond/scripts/gold/08b_build_architect_attribution.py` | NEW -- full T0-T16 decision tree |
| `data/black_diamond/scripts/gold/08_build_nna_aua_by_advisor.py` | load_relationship_advisors reads attributed lookup; save_rel_lookup is no-op |
| `data/black_diamond/scripts/gold/run_gold_layer.sh` | 08b added before 08 in incremental + full modes |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml` | +architect_attribution, +rel_architect_lookup entries; updated accounts_dimension |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ADVTV2.001.gold-architect-attribution.md` | Status: complete |
| `docs/briefs/devops-brief-architect-attribution.md` | NEW -- deploy instructions for DT |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE (pending commit + DT deployment)
**Active branch:** `CLOUD`

All 7 requirements from the task order are addressed. The 4 gold layer files are ready for S3 upload and a FULL gold layer run. Scripts 09 and 10 require no changes — they already consume `rel_architect_lookup.parquet` and will automatically pick up the attributed architect names.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Commit** all modified files to CLOUD
2. **[0.4.0_DT_ClientPlatform] Upload** 4 scripts to `s3://opal-data-bd/code/gold/` per `docs/briefs/devops-brief-architect-attribution.md`
3. **[0.4.0_DT_ClientPlatform] Run** gold layer in FULL mode on bd-gold-layer-runner
4. **[0.4.0_DT_ClientPlatform] Verify** rel_architect_lookup has 19 architects + Unresolved, no 49F House
5. **[0.4.0_DE_ClientPlatform] Verify** ADV leaderboard shows 19 named architects after portal data refresh

**Files to touch next:**
- None for DS — handoff to DT for deployment

**Do NOT:**
- Run incremental mode for first deploy (consultant/additional_advisor need full history rebuild)
- Hardcode architect names in any script (they are computed dynamically from the data)
