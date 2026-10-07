# Never-widen half request, MDPF_SECCLASS -- the seed run after the seed module carries six-class values (TO-SC-e21; 1.0.0_SA_CTO's condition 1 on the rule-B remap half)

**Author:** `0.9.0_WK_MDPF_SECCLASS~21` (worker, L7), 2026-10-07, for `2.0.0_SA_COO~M1` to issue. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
The seed run is the issuer's act, never the worker's. The worker ran only `--dry-run` and the read-only check below.
Records: `ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md`, `ANDREW_DIRECT_20261007_00xxZ_RULE_B_CATEGORY_RULE_FOR_MULTI_ASSET_FUNDS.md`;
the remap half `NEVER_WIDEN_HALF_REQUEST_SECCLASS_MULTI_ASSET_REMAP_B_20261007.md` and the CTO's condition 1 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_SECCLASS_MULTI_ASSET_REMAP_B_20261007.md` @ed687ec668.

## The act

`python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` (no `--dry-run`), by the issuer, after both halves sign and after the module edit is merged and its S3 copy decision is made (push-gate hazard below).
The module edit (this worker's commit, branch `wk-MDPF_SECCLASS-21`): in `infra/aws/lambda/v2_portal/_shared/etf_classification.py`, the 20 seed keys of the remap set carry the set's class in `ETF_CLASSIFICATIONS` (16 `equity`, 4 `fixed_income`, listed below), the five restored sub-classes
(ABALX `US Large Cap`, AOR `Global`, VTHRX `Global`, VWELX `US Large Cap`, VWENX `US Large Cap`) are in `ETF_SUB_ASSET_CLASS`, and the 15 keys the remap cleared have NO entry there. The token `multi_asset` occurs 0 times in the module (25 at base `b07521c5dd`). No other key and no other dict changed. The local candidate diff is `git diff b07521c5dd..wk-MDPF_SECCLASS-21 -- infra/aws/lambda/v2_portal/_shared/etf_classification.py` (30 insertions, 45 deletions).

## Blast radius (literal key list)

`etf-classifications` (us-east-1), the 20 remap-set keys that are `seed` rows:
AAETX ABALX AMECX AOR CAIBX CFIHX CLBAX FBALX FKIQX FTYPX KAGIX LIPKX MDLOX SGIIX VSMGX VTHRX VTIVX VTTHX VWELX VWENX.
Class per the set (column 5): `fixed_income` AMECX CAIBX CFIHX FKIQX; `equity` the other 16.

**What the seed run writes (measured by the script's own `--dry-run`, read-only, 2026-10-07T08:13Z):**
`rows to write: 15 of 197`, `rows already correct (skipped): 182 of 197`, 1 PRESERVED (`VNQ management_style`, the table's value stands). Items written 15, untouched 182, 0 created beyond those.
**Beyond the 20 keys: nothing.** The 15 are inside the 20; the five NOT written are ABALX AOR VTHRX VWELX VWENX (their live row already equals the module). Per-key difference between the live row and the planned item
(scratch plan reusing the script's `merge_item` and `item_differs` over a consistent scan, 3,507 rows), identical for all 15:
`low_confidence`: `True` -> absent; `updated_by`: `mdpf-secclass-remap-b` -> `seed-script`. Class and sub-class do not change on any of the 15.
The 15 keys: AAETX AMECX CAIBX CFIHX CLBAX FBALX FKIQX FTYPX KAGIX LIPKX MDLOX SGIIX VSMGX VTIVX VTTHX.

## Dry run, verbatim

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/seed_six_class_dry_run.py` (read-only), rc=0:
```
INFO low_confidence_would_drop=15 keys=AAETX,AMECX,CAIBX,CFIHX,CLBAX,FBALX,FKIQX,FTYPX,KAGIX,LIPKX,MDLOX,SGIIX,VSMGX,VTIVX,VTTHX
SEED-SIX-CLASS ok=True module_tickers=197 live_rows=3507 remap_seed_keys=20 conflicts=0 off_vocab=0 remap_keys_moved=0 multi_asset_tokens=0
```
At base the same check printed `ok=False ... conflicts=25 off_vocab=20 remap_keys_moved=40 multi_asset_tokens=25`.

## The open question for the CTO's half: the low_confidence hazard

`merge_item` in the seed script drops `low_confidence` on every row it writes (`MODEL_ONLY_FIELDS`). The rule-B remap set `low_confidence: true` on 15 of the 20 seed keys (the 15 above) to mark that their sub-class was cleared and their class is name-inferred.
A seed run strips that flag on all 15 and rewrites `updated_by` to `seed-script`. Because the class and sub-class already equal the module on every key, **the seed run moves no class; its only effects are those two.**
The CTO's half decides one of: (a) run the seed, accept the flag loss and the `updated_by` change; (b) do not run the seed at all (the module edit alone makes any future seed plan read 0 CONFLICT, which is the condition the remap half set); (c) the script is changed to preserve `low_confidence` first (not in this order; the script was not edited).
Filed as surprise row `MDPF_SECCLASS-W21-S1`.

## Writers counted (`etf-classifications`)

N = 7 as counted in the remap half (seed path; E_18 `detect_new_securities`; CUSIP rows writer; `write-model-rows.py`; FWD-9 writer; FWD-10 producer; remap writer). Branch A: the seed run writes the 15 keys above, each by a full-item `put_item`.
Branch B: a row changed between the script's pre-read scan and its put is overwritten with the planned item (a put, not a compare-and-set); the issuer re-runs `--dry-run` and the check immediately before the act and refuses on any difference from this file.

## Push-gate hazard (rows MDPF_SECCLASS-S35, S39)

The CLOUD push deploy gate uploads changed gold scripts and the shipped `lib/_shared/etf_classification*.py` copies to S3 AT THE PUSH, before any half is signed. The module is a shipped `_shared` module. The worker's commit stays on its branch; the issuer holds the merge into a pushed range until this half is signed.

## Rollback

Rollback per key: put the row back to its pre-state. The pre-state of each of the 15 is the live row at the issuer's pre-act read (class and sub-class as served, `low_confidence: true`, `updated_by: mdpf-secclass-remap-b`); the issuer writes that snapshot before the run. The 5 untouched keys need none.

## Acceptance (after the act, if run)

1. Consistent get of the 15 keys: class and sub-class unchanged from the set, `low_confidence` absent, `updated_by seed-script`. The 5 other keys unchanged.
2. A full scan reads zero `multi_asset` rows and the same row count (3,507, plus any put-on-absence rows other writers add).
3. `seed_six_class_dry_run.py` re-run prints `SEED-SIX-CLASS ok=True`.

## COO half -- UNSIGNED

## CTO half -- UNSIGNED
