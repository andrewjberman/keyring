# TO MDPF_SECCLASS.TO-SC-e31 -- round 8 SC-e-31: FWD-11 -- the AI classifier in service after the direct-match plan

<to_id>MDPF_SECCLASS.TO-SC-e31</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~26</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-31` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-11 (C-AIINDEX, C-VENDOR) | **depends_on:** MDPF_SECCLASS.TO-SC-e30 (imports
`infra/aws/lambda/v2_portal/_shared/security_name.py` `clean_name()`; starts after it drains, same slot `~26`).

---

## WORKER FACE

### THE CELL

`SC-e-31`. "The AI classifier in service after the direct-match plan: the residual writer called for what the plan leaves
UNRESOLVED, the value bound (six classes, the table's own sub-classes), the conditional put, the clean name from `SC-e-30`,
and the AI-made index listing rewritten by each run" (R8).

FWD-11 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12): "A security that no source Opal already
holds can place still gets its entry in the shared list, classified by Opal's AI classifier, and every entry made that way can
be listed." ACCEPT: "an entry with an asset class, a sub class and a clean, properly capitalized name, and no person has to
review it first. Anyone can pull up one list of every entry the AI made."

**The contract notes that bind this cell (PRD addendum v0.4, inlined):**
- **C-WRITER.** The writer is `infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py`. It runs AFTER the
  direct-match plan, for what the plan leaves UNRESOLVED. It writes by the same conditional put
  (`attribute_not_exists(ticker)`), so it never replaces a row. A seed row always wins.
- **C-VENDOR.** Andrew's word is recorded for this use (below). It names no model: use the model the existing writer
  already calls (`etf_classification_model.MODEL = "kimi-k3"`) and send what it sends today, the security's NAME and
  TICKER only. A different model or a wider payload needs his word and is out of this cell.
- **Value bound.** A verdict lands only if its `asset_class` is one of the SIX classes and its `sub_asset_class` is a value
  the live table already carries for that class. A verdict outside it leaves the key UNRESOLVED. The model never mints a
  class or a sub-class. A class the table holds no rows of today (`cash`: 0 rows, measured) therefore has no sub-class to
  land on and stays UNRESOLVED; do not add a path around that.
- **Clean naming.** The row's `name` is `clean_name(<source name>)` from `SC-e-30`, never a model output.
- **C-AIINDEX.** The index of AI-landed rows is the rows themselves: `classified_by = model` with
  `classification_confidence`, `low_confidence` and the write time. One readable listing of them is rewritten by each
  classifier run, at the builder address
  `lib/opal_naming.py address('mdpf','global','gold','ai_classified_securities','date=<run day>', object='index.json')`
  (issuer ran it 2026-10-07: `s3://opal-data-mdpf/mdpf/global/gold/ai_classified_securities/date=2026-10-07/index.json`).
  A row a later seed run corrects leaves the listing, because it is no longer `classified_by model`.
- **Moratorium.** The classifier is a scheduled producer. The listing is an artifact, not a notification: no alarm, SNS,
  SES or metric filter.

**The six classes (Andrew-direct 2026-10-07 ~00:4xZ, record
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md`,
VERBATIM: "there should be no multi-asset class. There are 6 classes: cash, fixed income, equity, structured, alternatives,
commodities.")**: `cash`, `fixed_income`, `equity`, `structured`, `alternatives`, `commodities`. 1.0.0_SA_CTO's remap half
condition 1 names "the AI classifier's vocabulary" as a member of this round's six-class cut. **Measured at the base:**
`infra/aws/lambda/v2_portal/_shared/etf_classification_model.py:58` `ASSET_CLASS_VOCAB` holds FIVE values (no `cash`) and
`build_prompt()` (`:89`) tells the model "one of equity|fixed_income|alternatives|commodities|structured". No `multi_asset`
appears in either. The issuer's bound check reads `VOCAB-BOUND ok=False ... prompt_missing=['cash']`.

**Measured at the base, the pieces you build on:**
- The direct-match plan: `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` `plan_rows(...)` (`:426`)
  returns `(rows, unresolved_names, seed_pending_names)`. Note: `unresolved` is a list of NAMES (`name or ticker`), not of
  (ticker, name) pairs. The AI path needs the ticker, so carry the pair: add nothing to `plan_rows` (it is not in your
  grant); derive the unresolved pairs in your runner from the held input minus the planned rows, present keys and seed keys.
- The model client: `etf_classification_model.classify_one/classify_many(..., send=..., api_key=...)` -- `send` is always
  injected; `_parse` refuses an out-of-vocabulary class to null (`KIMI_VOCAB_VIOLATION`). Confidence threshold
  `LOW_CONFIDENCE_THRESHOLD = 0.80`.
- The writer today: `classify-residual-model.py` (196 lines) has NO write mode. It reads a fixed residual file
  (`R2_UNRESOLVED_REVIEW_20260930.json`) and writes a census JSON. You turn it into the in-service writer.
- **A pre-existing red at the base:** `test_model_classifier.py::test_contract_version_is_0_3_0` fails (`'0.4.0' == '0.3.0'`):
  it pins a contract version and the contract moved. Cell `SC-e-27` moves the contract again this round. Replace the pin
  with a check that the contract's `classified_by.values` carries `model` and declares `classification_confidence` and
  `low_confidence` (the fields this cell writes), with no version literal. File one surprise row naming the stale pin.
- The 13 rows already `classified_by model` carry no `name` (measured). They are out of this cell's writes (a conditional put
  never touches an existing row); name them in your report.

**Build (code, tests and a dry run; NO model call, NO table write, NO S3 write; the first real run is the issuer's act):**
1. `etf_classification_model.py`: the vocabulary becomes the six classes; the prompt names the six and nothing else.
   Keep `send` injection, the name+ticker-only payload and the refuse-to-null discipline exactly.
2. `classify-residual-model.py` becomes the in-service runner:
   - input: one firm's held `(ticker, name)` pairs (the same input `plan_rows` takes) or a JSON file of them;
   - run the direct-match plan first; only the pairs it leaves UNRESOLVED go to the model;
   - apply the value bound to each verdict (six classes; sub-class a live-table member for that class); outside -> UNRESOLVED;
   - build each landing row: `asset_class`, `sub_asset_class`, `name = clean_name(source name)`, `classified_by = model`,
     `classification_confidence`, `low_confidence`, `updated_by`, write time; write it through
     `etf_classification_scheduled.write()` (the conditional put);
   - after the writes, rewrite the C-AIINDEX listing (step 3) from a consistent scan of `classified_by = model` rows;
   - `--write` is required to write; the default is a dry run that calls no model unless `--model` is passed AND `--write`
     is passed. In a dry run the model is replaced by a stub that returns null for every entry, so nothing would land.
   - the Kimi secret stays read from `astn/kimi/api-key` as today; never printed.
3. `infra/aws/lambda/mdpf-secclass/ai-index/`: the listing writer (`index_writer.py`: given the model rows, produce the
   listing JSON -- key, name, asset_class, sub_asset_class, classification_confidence, low_confidence, write time, count --
   and put it to the address above) and `tests/test_ai_index.py` with S3 and DynamoDB stubbed: a model row is listed; a
   `seed` row is not; a row a seed run corrected leaves the listing; the address is `address()` output, never typed.
4. `test_model_classifier.py`: extend it with the network stubbed: the six-class vocabulary; a `multi_asset` reply refused
   to null; a verdict whose sub-class the table lacks leaves the key UNRESOLVED; a planned (direct-match) ticker never
   reaches the model (count the `send` calls); a landing row carries the clean name; a present key is never written
   (count the puts). Fix the stale version pin as above.
5. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/ai_classifier_dry_run.py`: runs the runner in dry
   run (stub model, no write) against one real firm's held input you can read without a write (state which one and why),
   reading the live table for presence and vocabulary, and prints
   `AI-DRY-RUN held=<n> present=<n> direct=<n> to_model=<n> would_land=0 model_calls=0 index_address=<address>`.
   It must assert `model_calls == 0` and that no put was attempted (wrap the table and `send` with counters).

### ACCEPTANCE

<criterion id="SC8-e31-AC1" cell_refs="SC-e-31"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_model_classifier.py infra/aws/lambda/mdpf-secclass/ai-index/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC8-e31-AC1` -- the classifier and the listing writer pass their stubbed tests, the stale pin replaced.

<criterion id="SC8-e31-AC2" cell_refs="SC-e-31"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sc_e31_vocab_bound.py</invocation><expect>VOCAB-BOUND ok=True</expect></criterion>
`SC8-e31-AC2` -- the vocabulary and the prompt are the six classes, and a `multi_asset` reply is refused (issuer's bound check).

<criterion id="SC8-e31-AC3" cell_refs="SC-e-31"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/ai_classifier_dry_run.py</invocation><expect>model_calls=0</expect></criterion>
`SC8-e31-AC3` -- the runner dry-runs end to end on a real firm's input with the model stubbed and no put.

<expected_criteria>SC8-e31-AC1,SC8-e31-AC2,SC8-e31-AC3</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`PYTEST-BAD rc=4`: no `ai-index/tests`; the existing file alone reads
`1 failed, 17 passed`, the stale pin); AC2 FAIL as expected (`VOCAB-BOUND ok=False fails=vocab=[five];prompt_missing=['cash']`);
AC3 FAIL as expected (no dry-run file).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No model call, no table write, no S3 write, no secret read.** Andrew's word covers the AI classifier in service; it is
  exercised by the issuer's first real run under its own half, not by you. Your tests and dry run stub `send`.
- **Shipped-file hazard (rows S35, S39).** `etf_classification_model.py` is an `_shared` Lambda module and its name matches
  the `etf_classification*.py` shipped-copy pattern the push deploy gate uploads at a push, before any half is signed. You do
  not push; the issuer signs its half before your commits reach a pushed range. Say in your report every `_shared` file you
  changed.
- Do not edit `etf_classification_scheduled.py`, `etf_classification.py` (cell `SC-e-21`), the contract (cell `SC-e-27`) or
  any Terraform. Scheduling the runner is not this cell.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W26-S<k>`), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification_model.py
infra/aws/lambda/v2_portal/_shared/tests/test_model_classifier.py
infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py
infra/aws/lambda/mdpf-secclass/ai-index/
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/ai_classifier_dry_run.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-31`.
<owned_cells>SC-e-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e31-AC1, SC8-e31-AC2, SC8-e31-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~26/MDPF_SECCLASS.TO-SC-e31.ai-classifier-in-service.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e31-AC1,SC8-e31-AC2,SC8-e31-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the firm input the dry run read and its counts line, every `_shared` file changed, the 13 unnamed model rows, the
index address used, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): 8 gates name the lane, all open deploy-ledger entries; none names the AI classifier. This cell declares no schedule; the first real run and any schedule are issuer acts under their own pair.
comp-iam: RUN (R8 battery, DESIRED plane): 0 gap lines on etf-classifications; the role an in-service runner needs is not declared yet, so that zero says nothing about it. No role is declared by this cell (no Terraform in the grant).
comp-adversary: RUN -- R8 compose (2 cited commits verified; SC-e-30's files flagged GONE, expected). Cell reads by the issuer 2026-10-07: etf_classification_model.py:58 five-value vocabulary, :89 five-value prompt; classify-residual-model.py has no write mode; plan_rows returns unresolved NAMES not pairs; test_model_classifier.py carries a stale 0.3.0 pin (1 failed, 17 passed at the base); 13 model rows carry no name; 0 cash rows in the table. BLIND: which held input per firm is readable without a write (the worker names it).
Andrew word (C-VENDOR): org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_205xZ_AI_CLASSIFIER_YES_NO_HUMAN_REVIEW_INDEX_OF_AI_ROWS_YAHOO_PRICE_TABLE_OK_IF_NECESSARY.md, VERBATIM "Yes add the AI Classifier. Those can land without human review, but we want an index somewhere of all those that land by AI"; volume: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_0003Z_AI_CLASSIFIER_RUNS_ON_THE_FULL_OLD_TABLE.md ("RUn on the full old table", PRD addendum v0.11).
lane: the <paths> block IS the grant. etf_classification_model.py is added to R8's SC-e-31 write set: R8 says the classifier's vocabulary "is this cell's line, because this cell owns the file", but the vocabulary lives in etf_classification_model.py, which R8 does not list; no other R8 cell names that file.
</preflight>

Source: PRD v0.12 FWD-11, addenda v0.4 and v0.11 @87ad6d2e4c; R8 @495efa3c32; Andrew-direct six classes (record above).

## AMENDMENT 1 (2.0.0_SA_COO~M1, 2026-10-07 ~08:4xZ) -- Andrew-direct ~08:1xZ: LGIC naming and registration for every new resource

Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_081xZ_LGIC_NAMING_DILIGENCE_AND_REGISTRATION_FOR_EVERY_NEW_RESOURCE.md`
(origin 4cea56993a), relayed by 1.0.0_SA_CTO~DELL1 msg 49. Verbatim: "everyone is being very diligence with LGIC_NAMING for any new
resource creation, everything should be registered as well".

This cell declares no Terraform and creates no resource; it writes code, tests and a dry run, and its index listing lands at an S3
ADDRESS under an existing bucket, which is `address()` output (already required above). The rule binds the cell by these bounds:
1. Create no resource of any kind, by Terraform, CLI or SDK. If the in-service runner needs a function, role or schedule, name it in your
   report with the `name()` output it would take; the issuer cuts it later with its Terraform and its `resources.json` row in one commit.
2. Hand-type no resource name or S3 address in code or tests; a builder refusal is a surprise row naming the missing registry row.
Criteria unchanged. Gate limb: none graded this modification (no new order; no `<placeholders>`).
