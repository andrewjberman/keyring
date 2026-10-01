# MDPF_SECCLASS decomposition -- ROUND 6 (issuer 2.0.0_SA_COO~M; drafted 2026-09-30 ~18:5xZ, ISSUED ~19:3xZ)

**Status: ISSUED** in ONE issuance on the CTO's rounds 4-5 analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND4_5_ANALYSIS_MDPF_SECCLASS_20260930.md` @533bcae124, section 4 (the
enrichment list, six items). Earlier drafts @81244a2bf3 and @000f3f6c5e (cells 13 and 14) are superseded by this text.

**Cut on:**
- The analysis's section 4: (1) the fix-forward, (2) the two CUSIP reader guards, (3) S4 hygiene, (4) MODEL_ROWS reader
  census first, then the half, (5) FWD-7's first scheduled fire read from its log, (6) carried: W5-S2 at the drain;
  TO-SC-e12 parked.
- 1.0.0_SA_CTO RULING 103369 (the rollback is the half's own branch; the fix-forward is cell 1 under a new half; E_18
  stays deployed and 2026-10-01 04:00Z is the expected negative control).
- 1.0.0_SA_CTO DECISION 103371 (all laptop issuers): a cell whose diff changes an import in a script that runs from a
  deployed code prefix carries ONE criterion that imports the module from the deployed layout itself, printed.
- Analysis ruling 2 (Q2): the MODEL_ROWS half carries a census of every reader of `etf-classifications` and each reader's
  behaviour on `classified_by = model` and on `low_confidence`; no reader may crash, refuse the row, or fail a strict
  contract (the Holdings contract's `additionalProperties:false`, W93-S1, is the named risk).
- REMEDIATION_v3 `MDPF_SECCLASS-S4` (graduated by 3.0.0_SA_CVO @0ae356c411; owner this seat, round v6).

**Rule 24.** Domain = the six enrichment items. Items 2 and 3 are REPAIRS and batch into ONE cell (canonical-drive
obligation 1). Item 5 is an ISSUER ACT: the scheduled classifier's first real fire can only be read after cell 1's
redeploy (E_18 crashes at import until then), so a worker cell for it would be a wait. Item 6 is drain hygiene plus a
parked order by reference. Three cells, no remainder, one intent each.

**Measured constraints (read at the base, 2026-09-30):**
1. The BD gold runner syncs `s3://opal-data-bd/code/gold/` FLAT into `/tmp/gold_layer_scripts/` (bd-gold-trigger header;
   the 17:47Z traceback path). Nothing outside `code/gold/` reaches it.
2. `.tools/safe_deploy_core.py` maps only `data/<tree>/scripts/{gold,silver,bronze}[/lib]/*.py`; `AUX_CODE_PREFIXES["bd"]`
   is `{}`. The one client has no deploy path to the BD prefix today.
3. PRD C-TABLE: no second client copy is made in the repo. Shipping the client's bytes as a deploy artifact (the way
   `_IRPT_HOLDINGS_CLOSURE` ships it into the Holdings bundle) is not a repo copy.
4. `data/black_diamond/scripts/silver/build_bd_assets_dim.py:56` imports `lib.etf_classifier` via `../gold`; the silver
   runner's layout is UNMEASURED and the cell measures it before relying on it.

## The cells

| cell | item | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `SC-e-13` | Item 1, THREAD-BREAKING FIRST: the BD thread imports the one shared client on the runner. A declared deploy mapping ships the client's bytes (and, for E_18, `etf_classification_scheduled.py` plus anything either imports at load) inside `code/gold/`; `lib/etf_classifier.py` and `E_18` resolve the client from their deployed directory first and the repo path second, the module-level `parents[N]` hop removed; the silver layout measured and covered; the NEW half BD_THREAD_R3 | FWD-1, FWD-7 (E_18), S5 disarm | NOT-EVALUATED | laptop | WORLD | A, `0.9.0_WK_MDPF_SECCLASS~10` |
| `SC-e-14` | Items 2+3, THE ROUND'S REPAIRS BATCHED: (a) the `find_by_asset_class` / `find_by_sub_asset_class` filter excluding `identifier_namespace == "CUSIP"` in the one client and its two byte-identical copies; (b) the two seed scripts' PRE-READ count excluding `CUSIP:` rows; (c) S4 -- `attribute_exists(ticker)` added to the ConditionExpressions of `label-legacy-classified-by.py:89` and `set-instrument-kind.py:96` | FWD-4 (reader hygiene), CUSIP_ROWS c5, S4 | NOT-EVALUATED | laptop | WORLD | B, `0.9.0_WK_MDPF_SECCLASS~11` |
| `SC-e-15` | Item 4: the MODEL_ROWS reader census -- every reader of `etf-classifications`, each exercised on a `classified_by = model` row carrying `classification_confidence` and `low_confidence`; verdict per reader (tolerates / crashes / refuses / fails a strict contract); the census section appended to the MODEL_ROWS half | FWD-4, FWD-7 (model rows), analysis ruling 2 | NOT-EVALUATED | laptop | WORLD | C, `0.9.0_WK_MDPF_SECCLASS~12` |

**By reference, not cut:** `SC-e-12` (W6-S2) stays PARKED on `0.7.0_AE_CloudOps` (CTO 103327); the row gate reads a
parked order as not-open (@867189a633).

## Write sets (disjoint)

- `SC-e-13`: `data/black_diamond/scripts/gold/lib/etf_classifier.py`, `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`,
  `data/black_diamond/scripts/silver/build_bd_assets_dim.py` (only if the silver layout needs it), `.tools/safe_deploy_core.py`,
  `data/black_diamond/scripts/gold/tests/test_etf_classifier_deployed_resolution.py`, `R6_CHECKS/r6_deployed_layout_import.py`,
  the BD_THREAD_R3 half, the surprise channel.
- `SC-e-14`: `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`, its two copies, the two seed scripts,
  `yang_pipeline/label-legacy-classified-by.py`, `yang_pipeline/set-instrument-kind.py`, two new test files,
  `R6_CHECKS/r6_client_copies_identical.py`, `R6_CHECKS/r6_seed_preread_count.py`, the surprise channel.
- `SC-e-15`: `R6_CHECKS/r6_model_reader_census.py`, `R6_MODEL_READER_CENSUS_20260930.json`, the MODEL_ROWS half, the
  surprise channel.
- Ordering: SC-e-14 edits the client bytes that SC-e-13 ships; both drain before the redeploy, so the shipped bytes are
  the filtered client. SC-e-15 reads readers at the base (SC-e-13 changes import resolution only, not row handling). No
  build-time dependency.

## Issuer acts carried with round 6 (not cells)

1. **Item 5, FWD-7's first scheduled fire:** after SC-e-13 drains and redeploys under BD_THREAD_R3, the first ordinary
   scheduled fire of the classifier is read from its log (written, refused, denominator). Until then 2026-10-01 04:00Z is
   the recorded negative control (E18 ledger, held).
2. **W5-S2 drain hygiene:** the second schema cites the contract's enum and carries no value of its own.
3. **The one window's BD legs re-attempt** under BD_THREAD_R3 after both SC-e-13 and SC-e-14 drain.

`fanout: 3` of 3 chains, cap 8.
