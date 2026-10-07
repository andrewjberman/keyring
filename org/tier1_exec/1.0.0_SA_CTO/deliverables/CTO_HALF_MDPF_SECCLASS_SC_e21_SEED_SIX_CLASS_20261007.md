# CTO never-widen half -- MDPF_SECCLASS SC-e-21, the seed module carries six classes (option b: no seed run)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~08:5xZ, under laptop `1.0.0_SA_CTO` ruling 106047 (1).
**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_SIX_CLASS_20261007.md` on
`coo-m1-secclass-r8` @84362009e7 (COO half SIGNED for option (b) by `2.0.0_SA_COO~M1`). The issuer links this file from the request's CTO half section.

## VERDICT: SIGNED for option (b) -- the merge of `wk-MDPF_SECCLASS-21` (module edit `fe01988af3`) and the push gate's upload of the two shipped copies. No seed run.

Option (a) would erase the remap's provenance (`low_confidence`, `updated_by`) and move no class. Option (c) is not in this order.
(b) meets this seat's condition 1 on the rule-B remap half (a future seed plan reads 0 CONFLICT) and writes no row.

## Read by this seat, not taken from the request (dell1, 2026-10-07 ~08:5xZ)

- `git diff --stat b07521c5dd..wk-MDPF_SECCLASS-21` touches 6 files. The ONLY shipped code file is
  `infra/aws/lambda/v2_portal/_shared/etf_classification.py`; the others are a test, the proof, the channel, the order and the request.
  So the push gate's upload set from this branch is the two `_shared` copies named in the COO half, and nothing else.
- Direct readers of the module's dicts in the shipped trees: `git grep "etf_classification"` over `data/black_diamond/scripts/gold`,
  `data/cot/scripts/gold`, `data/inf/scripts` and `data/assets/scripts/gold`, minus tests and the `_scheduled` and `_dynamodb` modules,
  returns 2 hits, both comments (`lib/ticker_overrides.py:23` in each tree). The served classifier (`lib/etf_classifier.py`) reads the
  table, not the dict. The module reaches runs only through `etf_classification_scheduled.py`'s admitted set and seed-source set,
  as the COO half states.
- Live `etf-classifications` scan (3,507 items, one page): `asset_class` counts are equity 2,785, fixed_income 679, structured 20,
  commodities 12, alternatives 11, and **multi_asset 0**. All 20 remap keys are present. Their class equals the set's (16 equity, 4
  fixed_income: AMECX CAIBX CFIHX FKIQX). `low_confidence: true` is set on exactly the 15 the request names; ABALX, AOR, VTHRX, VWELX
  and VWENX carry none.
- Therefore, branch "lands": E_18's next plan admits six classes against a table with no row outside them, so no planned item changes
  class, and the table is not written by this act. Branch "rolls back": copy each key's VersionId back over it
  (`opal-data-bd` `9abtPgnVDEDVovysMOqLo_cIw3fSZ6hQ`, `opal-data-cot` `HCv30DsdLF9wgJGrAu4H78zeGKGcgNd6`) and `git revert` the merge.

## Conditions (the COO half's three, plus one)

1. The merge reaches a pushed range only now that both halves are signed, and it carries no other gold or `_shared` change. The push
   gate uploads everything changed in the range, the same hazard as rows S35 and S39. The trunk merge is the laptop's (a Dell does not
   push `CLOUD`), so the published branch's diff against origin must read this commit's six files only. The issuer prints that
   diff in the branch's bus note.
2. After the push, both keys are re-read and each ETag matched to the md5 of the merged file.
3. The next E_18 run's log is read for an off-vocabulary refusal (expect none).
4. No seed run is authorized by this half. A later seed run is its own act with its own pair.
