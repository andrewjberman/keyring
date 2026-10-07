# Never-widen half request, MDPF_SECCLASS -- the old list's reclassification write (TO-SC-e32; FWD-17, FWD-15)

**Author:** `0.9.0_WK_MDPF_SECCLASS~26` (worker, L7), 2026-10-07, for `2.0.0_SA_COO~M1` to issue. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
The write is the issuer's act, never the worker's. The worker ran only the read-only set build, the read-only check and the writer's DRY RUN (no put, no model call), and tested the writer's `--write` and `--rollback` limbs against an in-memory fake table in `.scratch/` (uncommitted).
Records: `ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md` (six classes); `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_0003Z_AI_CLASSIFIER_RUNS_ON_THE_FULL_OLD_TABLE.md` (outside-model use at the full old-list volume); the contract's key form `NAME::<slug>` (`org/standards/MDPF_SECCLASS_CONTRACT.json` 0.5.0, `identifier_namespace` NAME) and its proposal `KEY_FORM_PROPOSAL_20261007.md`; the census `OLD_LIST_CENSUS_20261007.json`.

## The act

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_write.py --write --half <this file> --snapshot <snapshot path>`, by the issuer, once both halves below read SIGNED and after `SC-e-31`'s AI path and `SC-e-30`'s `clean_name` are merged into the tree the act runs from. The writer refuses unless both `## COO half -- SIGNED` and `## CTO half -- SIGNED` headings are present in this file, and refuses if the snapshot path already exists.
Order of the act: (1) snapshot the table's key set (written BEFORE any put); (2) DIRECT rows, held first, by `etf_classification_scheduled.write()` -- a conditional put on an absent key; (3) AI rows, held first, through `yang_pipeline/classify-residual-model.py` `run()` with its model enabled, in chunks of 250 keys (classify, bound, conditional put, AI listing rewritten per chunk). The model is the one `etf_classification_model.MODEL` names, sent the security's name and key only.

## Blast radius

**One table: `etf-classifications` (us-east-1), plus the AI listing object the runner rewrites per chunk (`s3://opal-data-mdpf/mdpf/global/gold/ai_classified_securities/date=<run day>/index.json`, address from `index_address()`). Nothing else. `bd-securities` is read, never written.**
Set: `OLD_LIST_RECLASSIFY_SET_20261007.tsv`, 10,965 rows = the `bd-securities` scan of 2026-10-07 (denominator 10,965; shared list 3,507 rows, 0 `multi_asset`, 0 `cash`). `held` = the census definition over the local Holdings-producer builds (cottonwood and 49financial as-of 2026-10-05, inflection 2026-10-02, producer at repo HEAD b07521c5dd, no upload, the builds `old_list_census.py` read; claim **inferred**: the firm buckets answer AccessDenied to this device). Measured by `sc_e32_reclassify_set_check.py`: `RECLASSIFY-SET ok=True old_rows=10965 present=2381 direct=5796 ai=2785 unplaced_key=3 held=3152`.

| route | old rows | of them held | distinct shared keys the act would write | what happens |
|---|---|---|---|---|
| PRESENT | 2,381 | 1,652 | 0 | key already in the shared list; never touched |
| DIRECT | 5,796 (equity 3,820; fixed_income 1,939; alternatives 37) | 1,257 | 5,446 (1,259 held) | conditional put, `classified_by=scheduled`, `updated_by=mdpf-secclass-old-list-reclassify`, class and sub-class as the plan placed them |
| AI | 2,785 | 243 | 2,306 (241 held) | the runner; a row lands only if the model's class is one of the six AND its sub-class is already carried by the table for that class; otherwise UNRESOLVED, listed by name |
| UNPLACED-KEY | 3 | 0 | 0 | no declared key form: `NAME::` (empty slug, refused by the key rule), `The Hartford`, `Xometry` (the two of the old list's 7 non-ticker, non-`NAME::` keys that the shared list does not hold; the other 5 are PRESENT as themselves) |

Key forms written: 7,133 old rows are `NAME::`; re-slugged under the declared rule, 822 shared keys are named by more than one old row (829 rows collapse, max 3 rows per key; the TSV carries every old row, the writer puts each key ONCE: DIRECT over AI, else the earlier row). Rows keyed `NAME::` are written with `identifier_namespace = NAME`. Distinct keys: 7,752 = 5,446 DIRECT + 2,306 AI.
**Model volume** (the AI route at the volume Andrew's word covers): **2,306 keys = 2,306 model calls at one call per key; at most 4,612** (the model client retries a malformed or out-of-vocabulary reply once). Name and key only on the wire; no firm, holding, amount or client data. The key is read from the same secret the estate-report runner reads (`astn/kimi/api-key`), only on the `--write` run.
**Beyond these keys: nothing.** Every put is `attribute_not_exists(ticker)`; a key another writer lands first is refused and left as it is.

**What the act does not reach.** It places the old list's rows. Of the 1,449 held securities (three firms, census, claim inferred) with no shared entry, 1,046 have no old row at all, so FWD-15 is not at zero after this act (surprise row `MDPF_SECCLASS-W26-S8`). Of the 15 old `cash` rows, none can land: the table holds no `cash` row and so no cash sub-class, and the AI bound refuses a class with no live sub-class (`MDPF_SECCLASS-W26-S6`); they end UNRESOLVED by name. DIRECT carries 406 rows whose old row had `needs_review = True`; the plan's rule (i) takes a vocabulary-member value from any old row, and the plan's rule is unchanged here.

## Dry run, verbatim

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_write.py`, rc=0, read-only:
```
INFO set_rows=10965 live_rows=3507 direct_keys=5446 ai_keys=2306 collapsed_duplicate_keys=829 now_present=0 off_vocab=0
INFO AI-RUN held=2306 present=0 direct=0 to_model=2306 would_land=0 written=0 model_calls=0 index_address=s3://opal-data-mdpf/mdpf/global/gold/ai_classified_securities/date=2026-10-07/index.json
RECLASSIFY-DRY-RUN direct=5796 to_ai=2785 unplaced_key=3 present=2381 puts=0 model_calls=0
```
The table handle and the model transport are wrapped with counters in the dry run; either non-zero exits 1 as `RECLASSIFY-DRY-RUN-BAD`.

## Writers counted (`etf-classifications`)

The seed-six-class half of 2026-10-07 counted N = 7 (seed path; E_18 `detect_new_securities`; CUSIP rows writer; `write-model-rows.py`; FWD-9 writer; FWD-10 producer; remap writer). This writer is the eighth. Any of them that lands a new key by a conditional put on absence can race this act on a key: the put refuses the second writer, so the outcome is the same either way (read from `write()`, which every conditional-put writer shares; not re-read per writer here); the issuer re-runs the dry run and `sc_e32_reclassify_set_check.py` immediately before the act and refuses on any difference from the counts above (a row added to either table after 2026-10-07 moves the denominator).

## Both branches

Lands: each DIRECT and AI key above gets a row; 5,446 + (2,306 less UNRESOLVED) new keys in the shared list; no existing key changes. Does not land (a put refused, a model verdict outside the bound): that key is left absent and named UNRESOLVED; the act is repeatable, since a present key is never touched.

## Rollback per key

Before any put the writer writes `<snapshot>` (the table's key set, the two `updated_by` values the run uses: `mdpf-secclass-old-list-reclassify` and `mdpf-secclass-model`). `--rollback --half <this file> --snapshot <snapshot>` takes, per key, a conditional delete of every DIRECT/AI shared key of the set that is NOT in the snapshot, with `ConditionExpression attribute_exists(ticker) AND updated_by IN (the two values)`, then rewrites the AI listing. A key that existed before the act, or one another writer put, is never deleted. Tested only against an in-memory fake table.

## Acceptance (after the act, if run)

1. A consistent scan reads every DIRECT key at its set class and sub-class, `classified_by scheduled`; every landed AI key `classified_by model` with `classification_confidence`; the row count equals the snapshot's plus the written count; 0 `multi_asset` rows; no key of the 2,381 PRESENT changed.
2. The AI listing's count equals the number of `classified_by = model` rows.
3. `sc_e32_reclassify_set_check.py` is a PRE-act check: after the act the DIRECT and AI keys are in the shared list and it prints `direct_key:`/`ai_key:` failures by design, so the post-act check is the scan in item 1, not the set check.

## COO half -- UNSIGNED

## CTO half -- UNSIGNED

## ADDENDUM V3 + COO half (2.0.0_SA_COO~M1, 2026-10-07 ~19:0xZ; release mode, the e32/e50 line)

**The set is now V3** (`OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv`, built by `R12_CHECKS/old_list_set_v3.py` @15f9c9a411 from SC-e-50's
V2). It reads `OLD-LIST-SET-V3 ok=True rows=10965 live=10965 contract=0.8.0 n_problems=0`. Three changes from V2:
- Names: every clean_name is recomputed by `clean_name()` at R12 + R12b + R12c (one casing per form, X&Y upper, ASCII only;
  SC-e-48's refusal and row S62). 3,894 names differ from V2, and the set carries 0 non-ASCII names.
- Cash: S58's three (CSHI cash/T-Bill; FIGXX, FISXX cash/Money Market), plus 313 more DIRECT fixed_income/Cash rows re-planned
  cash/Cash. That is PRD v0.14 ruling 2.4, and the same rule the SC-e-49 conditions set. S58 had counted 3 from a `problems[:3]` page
  (row S62).
- 279 rows whose key landed since V2 (SC-e-49's DIRECT leg and others) are now PRESENT and are never touched.

**The writer is bound by the contract** (`old_list_reclassify_write.py` @15f9c9a411):
- DIRECT and the AI runner's bound are the contract 0.8.0 closed list per class, not the live table's vocabulary (which still carries
  legacy fixed_income/Cash).
- Each AI chunk prints keys_sent, model_calls and landed_outside_contract, and stops on any landed row outside the contract.
- The AI key set refuses above 8,495, the volume of Andrew's word.

**Dry run at 15f9c9a411, read-only** (`--set OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv`):
```
INFO set_rows=10965 live_rows=3786 direct_keys=5182 ai_keys=2291 collapsed_duplicate_keys=829 now_present=0 off_vocab=0 bound=contract 0.8.0 vendor_ceiling=8495
INFO AI-RUN held=2291 present=0 direct=1 to_model=2290 would_land=0 written=0 model_calls=0
RECLASSIFY-DRY-RUN-BAD to_model=2290!=ai_keys=2291
```
The one key is `NAME::FT UNIT 9273 INT RATE HEDGE PORT SER 135 MONTHLY CASH` (row S63). The live cash-token ticker leg reads a NAME::
key's words, so the runner places this unit trust cash/Cash. Its write path then never puts it. TO-SC-e65 amendment 3 (@f4aed6106d)
removes that defect, and the act runs only at a head carrying it, where the dry run must read `to_model == ai_keys`.

| route | distinct keys | held | by class |
|---|---|---|---|
| DIRECT | 5,182 | 852 | equity 3,402; fixed_income 1,421; cash 328 (Cash 310, T-Bill 9, Money Market 9); alternatives 31 |
| AI | 2,291 | 174 | the runner, in chunks of 250 |

Model volume: at most 2,291 keys and at most 4,582 calls (one retry). This is the old list itself, the population Andrew's word of
2026-10-06 00:03Z names ("RUn on the full old table": up to 8,495 rows, Kimi K3, name and key only, after the direct-match step).
Together with SC-e-49's AI leg, if that is ruled in, the distinct keys sent stay at or under 3,321.

## COO half -- SIGNED WITH CONDITIONS (2.0.0_SA_COO~M1, V3)

Signed for:
- the snapshot;
- the 5,182 DIRECT conditional puts;
- the AI leg over the 2,291 old-list keys, on the one table plus the AI listing;
- the per-key rollback stated above.
Both branches are covered: a key either lands, or is refused or left UNRESOLVED and stays absent. Conditions, each a STOP:
1. The act runs at a head carrying TO-SC-e65 amendment 3 and R12c, and its dry run reads off_vocab=0 and to_model == ai_keys. Any
   count other than the table above goes back to the signers.
2. Per AI chunk, landed_outside_contract=0, or the run stops and rolls back.
3. The model and payload are the existing writer's (kimi-k3, name and key only). Anything else stops the AI leg.

## CTO half -- requested of 1.0.0_SA_CTO~DELL1

## CTO half -- SIGNED (1.0.0_SA_CTO~DELL1 @8779dcc505, recorded by 2.0.0_SA_COO~M1)

Signature: org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_SECCLASS_SC_e32_e50_OLD_LIST_V3_20261007.md. Added conditions:
(1) the live _shared deploy of TO-SC-e65 amendment 3 needs its own pair, and only after the e65 ledger closes; this act's runner
reads the amended module from the release head; (2) this act runs before SC-e-49's.
