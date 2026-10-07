# Never-widen half request, MDPF_SECCLASS -- the AI classifier's run over each firm's missing list (TO-SC-e49; FWD-15 via FWD-11)

**Author:** `0.9.0_WK_MDPF_SECCLASS~36` (worker, L7), 2026-10-07, for `2.0.0_SA_COO~M1` to issue. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
The run is the issuer's act, never the worker's. The worker ran only the read-only planner (`R11_CHECKS/fwd15_ai_plan.py`: consistent scans of `bd-securities` and `etf-classifications`, the runner's own `run()` in its stub mode behind a transport that counts and refuses every call) and the read-only issuer check `fwd15_plan_check.py`. No model call, no table write.
Vendor word it rests on: FWD-11's recorded word (PRD ADDENDUM, contract note C-VENDOR; Andrew-direct 2026-10-05 "Yes add the AI Classifier. Those can land without human review, but we want an index somewhere of all those that land by AI"), applied by analysis ruling 2.3 (`CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md`): the same model (`etf_classification_model.MODEL`, kimi-k3) and the same payload (the security's name and key only); no new word is needed for it. Bound: ruling 2.5, the contract 0.6.0 closed sub-class list (`fields.sub_asset_class.values_by_class`). Plans: `FWD15_AI_PLAN_{49financial,cottonwood,inflection}_20261007.json`, over `MISSING_LIST_<firm>_20261007.json` (1,565 held securities with no shared entry; claim **inferred**: local Holdings-producer builds as-of 2026-10-05, the firm buckets answer AccessDenied to this device, W25-S1).

## The act

By the issuer, once both halves below read SIGNED, with the tree carrying SC-e-31 (the runner and model module), SC-e-30 (`clean_name`) and SC-e-54 (contract 0.6.0), after re-running `fwd15_ai_plan.py` and `fwd15_plan_check.py` and refusing on any difference from the counts below (a row added to `etf-classifications` or `bd-securities` after 2026-10-07 moves them):

1. Snapshot the table's key set to a file, BEFORE any put.
2. Per firm, held-first (each plan file's `entries` order, `amount` largest first), DIRECT entries (301): a conditional put through `etf_classification_scheduled.write()` (`attribute_not_exists(ticker)`), class and sub-class as the plan placed them, `classified_by=scheduled`. Proposed `updated_by` for these rows: `mdpf-secclass-fwd15-direct` (the signers may name another; the rollback below reads it).
3. Per firm, held-first, AI entries (1,165): `yang_pipeline/classify-residual-model.py --model --write` over a held file of `[shared_key, name]` pairs built from each plan's `route = AI` entries (the shared key as the pair's key, so a 9-character CUSIP goes in as `CUSIP:<9>`), in chunks of 250 keys: classify, apply the bound, conditional put, AI listing (`ai-index/index_writer.py`) rewritten per chunk. Rows: `classified_by=model`, `updated_by=mdpf-secclass-model`, `classification_confidence`, `low_confidence`.
4. UNPLACED-KEY entries (99) and PRESENT entries (0) are not touched.

The model key is read from `astn/kimi/api-key` (the secret the estate-report runner reads) only on the `--model --write` run, never printed. The bound the runner applies is the live table's sub-classes per class; the live table holds NO sub-class outside the contract's closed list for any of the six classes (measured by the planner, field `live_subclasses_outside_the_contract_closed_list`, all six lists empty), so the runner's bound and the contract's closed list admit the same values today.

## Blast radius

**One table: `etf-classifications` (us-east-1), plus the AI listing object the runner rewrites per chunk (`s3://opal-data-mdpf/mdpf/global/gold/ai_classified_securities/date=<run day>/index.json`, address from `index_address()`). Nothing else. `bd-securities` is read, never written.** Denominators at the scans of 2026-10-07: `bd-securities` 10,965 rows, `etf-classifications` 3,507 rows, contract 0.6.0.

| firm | missing | DIRECT (put, `scheduled`) | AI (runner) | UNPLACED-KEY (untouched) | PRESENT | planned model calls | at most (retry) | model calls this task |
|---|---|---|---|---|---|---|---|---|
| 49financial | 451 | 16 (all equity) | 432 (USD 7.85M held; 15 CUSIP-keyed) | 3 | 0 | 432 | 864 | 0 |
| cottonwood | 341 | 131 (equity 77, fixed_income 51, alternatives 3) | 123 (USD 16.92M held; 6 CUSIP-keyed) | 87 (USD 76.84M held) | 0 | 123 | 246 | 0 |
| inflection | 773 | 154 (equity 142, fixed_income 11, alternatives 1) | 610 (121 CUSIP-keyed; 570 of the 610 carry amount 0.0) | 9 | 0 | 610 | 1,220 | 0 |
| **total** | **1,565** | **301** | **1,165** | **99** | **0** | **1,165** | **2,330** | **0** |

Attributes put per key: DIRECT `ticker` (the shared key), `asset_class`, `sub_asset_class`, `classified_by`, `updated_by`, `name`; AI the same plus `classification_confidence`, `low_confidence`, `classified_by=model`. A key lands as a NEW row only; every put is `attribute_not_exists(ticker)`, so a key another writer lands first is refused and left as it is.
**Model volume:** 1,165 keys = 1,165 calls at one per key; at most 2,330 (`classify_one` retries once on a 5xx, a malformed reply or an out-of-vocabulary reply; a 4xx or a timeout is terminal). Name and key only on the wire; no firm, holding, amount or client data.
**Candidate diff (local, the plans, not the table):** each plan file lists every key with its `route`, `shared_key`, `key_form`, `amount`, and for DIRECT its `asset_class` and `sub_asset_class`. Largest candidate rows: 49financial AI `CUSIP:48134WGU5` (USD 1.85M), DIRECT `CART` equity/US Mid Cap; cottonwood AI `FCASH` (USD 9.73M), DIRECT `FIGXX` fixed_income/Cash; inflection AI `FCASH` (USD 0.85M), DIRECT `AAGIY` equity/International (amount 0.0). The diff against the live table is the whole of `entries` with `route` DIRECT or AI: 1,466 candidate new keys, 0 existing keys changed.

Carried from round 8, not fixed here: **0 of the 1,165 AI entries carry a `NAME::` key** (W26-S7: the runner sends the key to the model as its "ticker"; none of these 1,565 keys is name-keyed, so it does not bite on this set); **all 1,165 AI rows would land with no `identifier_namespace`** (W26-S5: the runner builds none; the 142 CUSIP-keyed AI rows would land with the `CUSIP:` prefix in the key and no namespace attribute). `cash`: the table holds no `cash` sub-class (W26-S6), so an AI verdict `cash` is refused by the bound and ends UNRESOLVED by name; two AI entries are named `FCASH` (cottonwood, inflection), the planner has not predicted their verdicts.
**Overlap with SC-e-32's old-list act:** 150 of the 1,165 AI entries (49financial 46, cottonwood 45, inflection 59) are also keys of the old list's AI set, and the 301 DIRECT entries are placed from old-list rows. Whichever act runs first lands the key, the conditional put refuses the second, and the second's model call for that key is spent for nothing (up to 150 calls, 300 with retry); the issuer sequences the two acts or accepts the overlap in the signed word.
**What the plan does not reach:** 99 UNPLACED-KEY entries (87 in cottonwood, USD 76.84M held, internal ids such as `4175_VOYA`, `CXMANUAL_HOME`; no declared key form fits them, so FWD-15 is not at zero after this act), and any AI verdict the bound refuses.

## Writers counted (`etf-classifications`)

The seed-six-class half of 2026-10-07 counted N = 7 writers (seed path; E_18 `detect_new_securities`; CUSIP rows writer; `write-model-rows.py`; FWD-9 writer; FWD-10 producer; remap writer); SC-e-32's old-list writer is the eighth and this run the ninth. Every one that lands a new key does so by a conditional put on absence (read from `write()`, which they share; not re-read per writer here), so a race on a key has the same outcome either way: the second put is refused.

## Both branches

Lands: each DIRECT key gets its row; each AI key whose verdict is one of the six classes AND whose sub-class is a member of the contract's closed list for that class gets its row, flagged `low_confidence` below 0.80 but never held back. Does not land (a put refused because the key now exists; a verdict outside the bound; a failed call): the key is left absent and named UNRESOLVED; the run is repeatable, since a present key is never touched.

## Rollback per key

Before any put the run writes the snapshot (step 1). Rollback: for each key of the plans' DIRECT and AI entries that is NOT in the snapshot, a conditional delete with `ConditionExpression attribute_exists(ticker) AND updated_by IN (mdpf-secclass-fwd15-direct, mdpf-secclass-model)`, then rewrite the AI listing. A key that existed before the run, or one another writer put under another `updated_by`, is never deleted. The run's writer is the issuer's; this rollback is stated, not tested by the worker.

## Acceptance (after the act, if run)

1. A consistent scan reads every landed DIRECT key at its plan class and sub-class; every landed AI key `classified_by model` with `classification_confidence`; the row count equals the snapshot's plus the written count; 0 `multi_asset` rows.
2. The AI listing's count equals the number of `classified_by = model` rows.
3. `fwd15_plan_check.py` is a PRE-act check; after the act the planned keys are in the table and `fwd15_ai_plan.py` re-run reads them PRESENT.

## COO half -- UNSIGNED

## CTO half -- UNSIGNED
