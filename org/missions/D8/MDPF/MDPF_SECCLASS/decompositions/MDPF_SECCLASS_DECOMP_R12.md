# MDPF_SECCLASS decomposition -- ROUND 12 (2.0.0_SA_COO~M1, dell1, 2026-10-08 ~02:5xZ)

**Status: DECOMPOSED.** The issuer is this seat. Order: 1.0.0_SA_CTO~DELL1 msg 764, "cut these six cells in one issuance", from
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_12_20261008.md` @82c4790d6c, section 3.
Release mode ended at that analysis: e59 is on DEV, and 2 lines (the e32 and e49 AI legs) are unreleased.

**Cut on:**
- PRD v0.16, ADMITTED.
- The round-12 analysis, section 3 items 1-6 and its "Order" paragraph.
- CTO note msg 766: cells 1 and 5 build now, but their deploy to a firm code prefix waits on Andrew's limit item 5 (routes-host). Cells 2,
  3, 4 and 6 are not gated by item 5.

**State the round starts from (measured this session):**
1. etf-classifications: 9,155 rows, 0 multi_asset, 200 model rows. e32 V3 run 1 landed 187 of 2,291 AI keys; run 2 and e49's AI leg
   wait on the kimi grant (laptop item 1). Executor dell1 0.7.0_AE_CloudOps~SD.
2. Row S60: COT D_04 (`data/cot/scripts/gold/D_04.client_portal_summary.py`, the writer of platinum/clients/*/concentration.json) served
   SGIIX as multi_asset at its 2026-10-07T11:40Z run. D_04's own source has no `multi_asset` literal, so the value comes from a COT class
   input upstream of D_04. SGIIX is also one of the 12 SEED-SOURCE keys, and `etf_classification.ETF_CLASSIFICATIONS['SGIIX']` reads
   `equity` in the repo.
3. The canonical CASH row reads fixed_income / Ultra Short Duration, classified_by legacy, name "Cash & Cash Equivalents" (CTO live read,
   02:4xZ).
4. W26-S5: the AI runner's `landing_row()` (`infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py`) builds no
   identifier_namespace. The two dell1 executors wrap the table in `NamespaceTable`, but the runner itself does not. Contract
   `fields.identifier_namespace.values` = TICKER, CUSIP, BLOOMBERG, NAME.
5. The 12 SEED-SOURCE names sit in `infra/aws/lambda/v2_portal/_shared/etf_classification.py` `ETF_NAME_OVERRIDES` (~:937), all-caps.
   Check `R12_CHECKS/sc_r12_seed_names.py` reads 0/12 at the base.
6. FWD-15's 99 UNPLACED-KEY entries are in `R12_CHECKS/e49_replan/FWD15_AI_PLAN_<firm>_20261007.json` (route UNPLACED-KEY).

## Rule 24 record

- **Domain:** section 3 items 1-6, every clause of each. The denominator is 6 items with 11 clauses. Each clause is placed once:
  - a cell: 6 cells, SC-e-67 to SC-e-72;
  - an issuer act: each cell's deploy or table write behind its pair (1, 2, 3's backfill, 5), and the AI legs after cell 3;
  - a deferred cell: SC-e-73, the portal readers drop multi_asset. It is cut when cell 1's producer is live and a post-switch census of
    served multi_asset reads 0 (S60's condition, CTO msg 437).
- **(ii) Same grain:** one write set per cell. **(iii) Intent coherence:** one intent per cell.
- **(iv) State coherence:**
  - Cells 1 and 5 change shipped code. They change no served file until their deploy, which waits on limit item 5.
  - Cells 2 and 3 build writers and dry runs. They write no row until the issuer's act under a signed pair.
  - Cells 4 and 6 are read-only.

## The cells

| cell | item | what | serves | risk | depends on |
|---|---|---|---|---|---|
| `SC-e-67` | 1 | S60: trace the COT class input that gives SGIIX multi_asset at D_04, fix it at its source so no COT producer emits multi_asset, pin it by test, and write the half request for the served keys | FWD-16 | WORLD (shipped COT gold; deploy waits on item 5) | -- |
| `SC-e-68` | 2 | The CASH row to cash/Cash: a conditional-update writer (dry run, --write, --rollback) on `classified_by = legacy` and the current class, plus its half request naming the served mix delta (e42 condition 5) | FWD-2, FWD-16 | WORLD (table write by the issuer) | -- |
| `SC-e-69` | 3 | W26-S5: the AI runner's `landing_row()` sets identifier_namespace from the key form; then a backfill writer for rows that have none (dry run prints the count) and its half request | FWD-2, FWD-17 | WORLD (shipped runner + table backfill) | -- |
| `SC-e-70` | 4 | READ-ONLY census of FWD-15's 99 UNPLACED-KEY entries by firm and id pattern, with a proposal of key forms or a manual-entry route | FWD-15 | LOCAL | -- |
| `SC-e-71` | 5 | The 12 SEED-SOURCE names in `ETF_NAME_OVERRIDES` set to `clean_name()`'s output, pinned by test | FWD-14, FWD-3 | WORLD (shipped `_shared`; deploy waits on item 5) | -- |
| `SC-e-72` | 6 | READ-ONLY cash grade: cash/Cash rows by classified_by against the 316 the V3 set planned, run at e32's close | FWD-16 | LOCAL | -- |

## Write sets

- **SC-e-67:** the COT class source the trace finds, under `data/cot/scripts/gold/` (the cell names its one file), plus
  `data/cot/scripts/gold/tests/test_d04_no_multi_asset.py` and
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_D04_MULTI_ASSET_20261008.md`.
- **SC-e-68:** `.../MDPF_SECCLASS_M/R12_CHECKS/cash_row_write.py` and
  `.../MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CASH_ROW_20261008.md`.
- **SC-e-69:** `infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py`,
  `infra/aws/lambda/v2_portal/yang_pipeline/tests/test_runner_identifier_namespace.py`,
  `.../MDPF_SECCLASS_M/R12_CHECKS/namespace_backfill.py` and
  `.../MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_IDENTIFIER_NAMESPACE_BACKFILL_20261008.md`.
- **SC-e-70:** `.../MDPF_SECCLASS_M/R12_CHECKS/unplaced_key_census.py`, `.../MDPF_SECCLASS_M/UNPLACED_KEY_CENSUS_20261008.json` and
  `.../MDPF_SECCLASS_M/UNPLACED_KEY_PROPOSAL_20261008.md`.
- **SC-e-71:** `infra/aws/lambda/v2_portal/_shared/etf_classification.py` and `infra/aws/lambda/v2_portal/_shared/tests/test_seed_names_clean.py`.
- **SC-e-72:** `.../MDPF_SECCLASS_M/R12_CHECKS/cash_grade.py`.
- Every cell may append rows to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.
- The write sets are disjoint. SC-e-67 does NOT touch `_shared/etf_classification.py` (SC-e-71's file). If S60's source turns out to be
  that file, SC-e-67 stops and files a row, and the issuer re-points.

## Dependency edges

None between cells. **Chains:** 6 single-cell chains, so M = 6. Fan-out 6 of 6, cap 8.
Issuer-act order, per the analysis: SC-e-69's writer lands before the AI legs run. If the kimi grant lands first, the AI legs wait.
