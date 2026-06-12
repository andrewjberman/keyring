# 0.6.0_AE_PartnerETL — work 2026-06-12 1410Z

**archetype:** IMPLEMENT (+ VALIDATE)

## ADHC_GLDINC.COT-FIX — cot A_01 + A_04 CLASS-N oracle-fix mirror

Engineered the 2 FIX sites from CENSUS-XT (CTO adjudication 0e745d9ed): cot
A_01.advisor_assignments + cot A_04.client_dimension. Commit **b9754025b**;
DS Rule-13 deployed to opal-data-cot/code/gold/ ONLY (md5 MATCH 812200e5 / 4d01fa99,
cross-firm clean). DELTA=0 verified via offline shadow battery → no never-widen hold.

### Changes
- **A_04**: index-slot assembly (`dfs=[None]*len`, `dfs[futures[fut]]=...`) + `_file_date`/`_intra_pos`
  provenance + total-order `sort_values(['transaction_id','_file_date','_intra_pos'])` before
  `keep='last'`, then `drop(columns=provenance)`. Mirrors bd 9a89926fd verbatim.
- **A_01**: provenance in `_load_one` + total-order sort at the L192 transaction_id dedup (the live
  defect; append retained, sort defeats nondeterminism — mirrors bd 73ec87a84) + provenance-extended
  sorts at the 2 downstream `(account_id,trade_date)` dedups (defensive `prov_cols` guard + drop).
  `build_history_for_account` (dead code) fixed for consistency.
- **Both**: added `from __future__ import annotations` (Rule 15 — cot tree had escaped the 71-script
  backfill; both files lacked it).
- **Incidental gate-required ruff hygiene** (pre-existing, behavior-equivalent, NOT logic): A_01 unused
  `import sys` (F401) + `log(f'')`→`log('')` (F541); A_04 `isin()==False`→`~isin()` (E712) +
  `print(f"\n...")`→`print("\n...")` (F541). The DELTA=0 battery proves no output movement.

### Compiler Tools section (acceptance-required)

**Phase-1 (before change):**
- `comp-pipescript io data/cot/scripts/gold/A_01...; ...A_04...` → "Script not found" — **comp-pipescript
  indexes the bd-gold tree only; cot is not indexed.** Portal-consumer question (does any consumer read
  the new provenance columns?) resolved BY CONSTRUCTION: `_file_date`/`_intra_pos` are dropped before the
  frame is written (A_04 `drop(columns=...)`; A_01 downstream-dedup `drop`) → never reach any output
  artifact → zero portal-consumer exposure. Battery confirmed PROV-LEAK=none on both fixed outputs.
- Read both cot scripts full + bd templates (9a89926fd A_04, 73ec87a84 A_01) — fix sites matched CTO's
  cited shape (A_04 L112-115/L120; A_01 L174-181/L192 + L373 + dead L231).

**Phase-2 (before commit):**
- `.tools/ds-commit-gate.sh A_01 A_04` → **All checks passed** (py_compile + ds-precommit-check + ruff py39), both files.
- `python .tools/ds-precommit-check.py A_01 A_04` → rc=0, **AST-DEDUP check_completion_order_dedup()
  SILENT on both** (A_04 index-slot, A_01 sort-guarded) — the structural regression guard (DS ab0cd8ba0). Zero WARN lines.

**Phase-3 (after DS deploy):**
- `comp-pipescript deployed` cot A_01/A_04 → "local repo vs s3://opal-data-bd/..., no scripts matched" —
  **comp-pipescript deployed is bd-only, BLIND to cot.** DS's direct md5 MATCH on opal-data-cot is the
  authoritative deploy verification (A_01 812200e5, A_04 4d01fa99; cross-firm clean — opal-data-bd copies
  unchanged, no leak).
- `comp-validate` cot A_01/A_04 → registry covers **BD + INF configs only; no cot config** →
  NO_CONFIG (UNVALIDATED per §10.1, not a pass). cot lacks a gold_validate_config.yaml (FYI gap to COO).
- **Offline DELTA=0 shadow battery** (the TO's HEADx2/FIXEDx2 acceptance requirement; non-serving,
  read-only cot S3, no EC2 runner, no SSM — cot nightly was stale 06-09, not imminent; cot data tiny:
  201 households / 623 SCD rows). Ran OLD (b9754025b^) ×2 + FIXED (HEAD) ×2 on current cot input,
  order-independent content hash excluding wall-clock now()-stamps:
  - **A_04**: FIXED1==FIXED2 (deterministic), OLD==FIXED → **DELTA=0** (hash 8c26a9facfa2 across all 4), PROV-LEAK none.
  - **A_01**: FIXED1==FIXED2, OLD==FIXED → **DELTA=0** (hash 05f48c5478ca across all 4), PROV-LEAK none.
  - The ONLY cross-run difference on A_04 was `created_date`/`updated_date` (201/201 cells) = wall-clock
    `now()` build-stamps — benign, inherently per-run, the exact bd A_04 "now()-stamps" precedent. Excluded
    from the content signature.

### Verdict
DELTA=0 hardening on both → fix moves NOTHING in served output, only removes future nondeterminism.
Per banked doctrine (never-widen gates served MOVEMENT, not deploys; verified DELTA=0 = no dual-hold).
RAVC2 to COO. Findings of note: (1) cot lacks comp-validate + comp-pipescript coverage (bd/inf only);
(2) A_04 carries now()-stamp columns (created_date/updated_date) — expected, not a defect.

## Commits
- b9754025b — cot A_01 + A_04 oracle-fix mirror (deployed by DS to opal-data-cot)
