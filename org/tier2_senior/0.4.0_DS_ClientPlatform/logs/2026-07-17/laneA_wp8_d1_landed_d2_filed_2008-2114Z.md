# Lane A delta: WP8 trn_nna D1 LANDED (fact_trn re-point, IAM-APPLIED-verified, deployed) + D2 FILED

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-17 ~20:08Z -> 21:14Z (delta since 1b266de71)

CTO ruled D1+D2 (204506Z) minutes after my 195254Z parity report. Both executed this window.

## 1. IAM gate (Rule 22a APPLIED truth -- CTO's D1 condition)

bd-exporter-ec2-role inline `monolith-schwab-08242234-silver-read`: UNCONDITIONED `s3:GetObject`
Allow on `opal-data-assets/schwab/08242234/silver/*` (wildcard covers fact_trn/); `cross-firm-bucket-
deny` denies only opal-data-cot (no override). `simulate-principal-policy` on the EXACT fact_trn key
= **allowed**; positive control (dim_transaction) = allowed; negative control (bronze/, outside
silver/*) = **implicitDeny** -> instrument discriminates. Both get-role-policy (document) AND simulate
(exact-key, controls SEPARATE) confirm. No +1 grant needed. GO.

## 2. D1 LANDED -- dim_transaction -> fact_trn re-point

- Edited `lib/schwab_trn_nna_gold.py` (prefix fn `monolith_dim_transaction_prefix` ->
  `monolith_fact_trn_prefix`, string -> `silver/fact_trn/`, docstrings/error-msg), `lib/schwab_flows.py`
  (import + call site + docstring path), `tests/test_schwab_trn_nna_gold.py` (import + prefix assert).
- commit-gate clean; 5 tests pass incl `test_ported_classifier_ties_the_retiring_bronze_converter_exactly`
  (the drift-detector). **Full AC1 harness RE-RUN on the fact_trn code path: 26,504 cells / 0 mismatch
  -- output-identical end-to-end** (not just per-partition).
- commit `37bd2fee1` (safe-commit, DS gold-lib lane). Deployed
  `s3://opal-data-bd/code/gold/lib/{schwab_trn_nna_gold,schwab_flows}.py` via `aws s3 cp`, **md5==ETag
  verified** (`cacc4c96..`, `8f13a83d..`) -- the upload-verify gate (no --quiet phantom-success).
  Pushed origin/CLOUD (VALGATE + safe-deploy pass). Runtime now reads fact_trn.

## 3. D2 FILED -- (a)+(b), NOT (c)

Retirement record `deliverables/WP8_TRN_NNA_OPTIONB_PARITY_20260717.md` (commit `8a0e1f5c5`):
57-day pre-2024-07-08 gap (+$18.07M net / 2,415 cells) ACCEPTED immaterial; frozen legacy TRN_NNA
partitions PRESERVED (do NOT secure-delete -- reachable via `SCHWAB_FLOW_SOURCE=legacy` env override
as historical-rebuild fallback); monolith-horizon-extend (c) rejected. Principle: retire the
PRODUCER, preserve the ARTIFACTS.

## Compiler Tools

| tool | run | result |
|---|---|---|
| aws iam get-role-policy / simulate-principal-policy | bd-exporter-ec2-role, fact_trn exact key + pos/neg controls | PASS -- APPLIED GetObject confirmed, instrument discriminates |
| commit-gate (safe-commit) | 3 .py (D1) + 1 md (D2) | PASS -- py_compile+ds-precommit+ruff clean |
| comp-blast | load_schwab_flows_by_date | EMPTY (honestly reported; consumers pre-censused: C_01 bd only, cot separate) |

**What worked:** the Rule-22a separate-control simulate cleanly proved APPLIED IAM (allowed + a
discriminating negative). **Gap (re-noted):** the AC1 re-run + fact-vs-dim identity remain boto3/pandas
parquet reads -- no comp-tool covers them.

## Blockers

None. Both CTO rulings executed. Open: converter step-5 retirement SEQUENCING question at CTO (msg
211315Z) -- (i) action now coordinating pod AE vs (ii) hold for the D-sequence cell. Not a blocker on
me; his sequencing call.

## Current State (handoff surface)

- WP8 trn_nna OPTION-B: **DONE through D1+D2.** Runtime reads monolith `fact_trn` (complete silver);
  AC1 parity to the cell (26,504/0); deployed==repo (md5==ETag). Legacy path preserved as
  `SCHWAB_FLOW_SOURCE=legacy` fallback.
- Commits: `37bd2fee1` (D1 re-point), `8a0e1f5c5` (D2 record), `1b266de71` (parity deliverable+log) --
  all origin/CLOUD.
- REMAINS: step-5 converter (`convert_schwab_trn_to_nna_silver.py`) retirement -- queued for the
  D-sequence, edits the AE-owned /49-schwab-conv skill, gated on CTO's sequencing answer.

## Next Steps

- **[1.0.0_SA_CTO]** Answer converter step-5 retirement sequencing (msg 211315Z): action-now-with-AE
  vs hold-for-D-cell.
- **[me / DS~A]** On his answer: execute or queue the step-5 removal (preserve artifacts per D2).
  Event-driven; Monitor bqifprts1 live; no crons.
