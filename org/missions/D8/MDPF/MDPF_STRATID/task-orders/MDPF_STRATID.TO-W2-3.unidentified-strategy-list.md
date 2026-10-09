# TO MDPF_STRATID.TO-W2-3 -- workstream 2 ST-w-3: the unidentified-strategy list (what looks Opal but matched nothing)
<to_id>MDPF_STRATID.TO-W2-3</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~6</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>2</workstream>
**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `ST-w-3` (`decompositions/MDPF_STRATID_DECOMP_W2.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none (imports today's `opal_sma_member_of`)

---

## WORKER FACE

### THE CELL

`ST-w-3`. FWD-7: anything that looks like an Opal strategy but matched nothing is listed with its firm, its name and its dollars,
instead of disappearing into a catch-all. You build the function that produces that list, prove it with tests, and record the list
for Cottonwood on its latest Rebalancer date. You serve nothing and write nothing in AWS.

**Build `data/assets/scripts/silver/opal_unidentified.py`:**
`unidentified_candidates(rows, member_of, cfg) -> list[dict]`, where `rows` is an iterable of `{"firm_id", "name", "dollars"}`,
`member_of` is a callable `name -> str|None` (pass `rebalancer_schemas.opal_sma_member_of` from
`data/assets/scripts/silver/rebalancer_schemas.py:226`), and `cfg` is the ETF list dict:
```
{"tickers": ["DIVZ","IDVZ","PFDE","PFOE"],
 "full_names": {"PFDE": {"name": "..", "source": ".."}, ...},
 "sma_name_rules": [{"member": "pfde"|null, "pattern": "<regex>", "source": ".."}, ...]}
```
A row "looks Opal" when its name contains `Opal` as a word (case-insensitive; `Opal_Muni_Income` counts, underscore is a separator),
or a `tickers` entry as a whole word, or a `full_names` name, or matches an `sma_name_rules` pattern. It is LISTED when it looks Opal
and `member_of(name)` returns None, OR when it matches a rule whose `member` is null. Each listed row:
`{"firm_id", "name", "dollars", "reason"}`, reason one of `NO_MEMBER` / `RULE_NOT_COUNTED` (null-member rule; e.g. Muni until a person
verifies it). A name that raises in `member_of` (two members) is listed with reason `AMBIGUOUS`. Sorted by dollars, descending.

**Tests** `data/assets/scripts/silver/tests/test_opal_unidentified.py` with exactly these test names:
`test_opal_named_unmatched_sleeve_is_listed`, `test_ticker_named_unmatched_is_listed`, `test_matched_sleeve_is_not_listed`,
`test_null_member_rule_is_listed_with_reason`, `test_non_opal_name_is_not_listed`, `test_row_carries_firm_name_dollars_reason`.

**Record** `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~6/UNIDENTIFIED_STRATEGY_CANDIDATES.md` for Cottonwood:
names from `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_model_roster/` and `.../fact_model_definition/` (columns
`model_name`, `sleeve_name`, `component_name`), latest `date=` partition; dollars per name from the served Cottonwood slice
`s3://opal-data-assets/gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json` `by_model[*].model_value` on its last date where a
name maps, else from `fact_holdings` joined through `fact_model_assignment` (say which per row; `None` where neither gives dollars,
never 0). Use the cfg rows in the contract above (the Muni rule matching `Opal_Muni_Income`/`Opal_Muni_Sleeve` with member null). The
file must have lines starting `SOURCE:` (objects read), `DENOMINATOR:` (distinct names scanned), `RESULT:` (`LISTED <n>`), then the
table. `Opal_Muni_Income` (one account, about $64.1M) must appear, reason `RULE_NOT_COUNTED`.

### ACCEPTANCE

<criterion id="W2-3-AC1" cell_refs="ST-w-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_3_tests.py</invocation><expect>W23-OK</expect></criterion>
`W2-3-AC1` -- the six named tests pass. At the base: `W23-BAD no file ...`.

<criterion id="W2-3-AC2" cell_refs="ST-w-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_3_seam.py</invocation><expect>W23-SEAM-OK</expect></criterion>
`W2-3-AC2` -- SEAM on real data: the recorded list has SOURCE, DENOMINATOR and RESULT lines and carries the control `Opal_Muni_Income`.
At the base: `W23-SEAM-BAD no file ...`.

<expected_criteria>W2-3-AC1 W2-3-AC2 W2-4-AC1 W2-4-AC2</expected_criteria>

Run each invocation from your worktree root.

### AMENDMENT A1/A4 (issuer, 2026-10-09 ~05:3xZ) -- cell `ST-w-4`, continued by this slot on its branch

Your first pass is complete and stands. This amendment adds cell `ST-w-4` (decomposition amendment A1/A4). Re-flip `<status>` to
`complete` only when every criterion in `<expected_criteria>` passes.

`ST-w-4`. You built `unidentified_candidates` (ST-w-3). Its Cottonwood record listed 38 names, most of them ordinary Opal MODELS
(`Opal Satellite 40..80`, `Opal Short-Term`, `Opal Fixed Income`, ...). An Opal Model is not an unidentified strategy: the PRD says
reclassifying an Opal Model as an SMA is out of scope. Change the rule, keep everything else.

**Change `data/assets/scripts/silver/opal_unidentified.py`:** `unidentified_candidates(rows, member_of, cfg, opal_models=frozenset())`.
`opal_models` is a set of names that are Opal Model figures. A name in `opal_models` is NOT listed, unless it also matches a sleeve
rule: a `cfg["tickers"]` entry as a whole word, a `cfg["full_names"]` name, or a `cfg["sma_name_rules"]` pattern. Matching is
case-insensitive on stripped names. Every other behaviour stays as you built it.

**Tests** in `data/assets/scripts/silver/tests/test_opal_unidentified.py`: keep the six existing tests passing and add exactly
`test_opal_model_is_not_listed` and `test_opal_model_matching_a_sleeve_rule_is_listed`.

**Re-make the record** `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~6/UNIDENTIFIED_STRATEGY_CANDIDATES.md`,
same sources and method as before, with `opal_models` = the UNION of the `model_name` values where `is_opal` is true in
`s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_model_roster/` AND in `.../fact_model_definition/` (latest `date=` partition
of each). RULING A6 (issuer, ~05:3xZ, row D1-W6-S2): the roster alone misses five Opal models (`Opal Short-Term`, `Opal Fixed Income`,
...) that appear only in the definition table. Add a line
starting `EXCLUDED-AS-MODEL:` with the count and the names excluded. Keep `SOURCE:`, `DENOMINATOR:`, `RESULT:`. `Opal_Muni_Income`
must still be listed with reason `RULE_NOT_COUNTED` (whatever `is_opal` says for it, it matches the Muni rule).

The checks live in the shared tree, not on your branch: run them with the absolute path below from your worktree root (they read
your worktree's files by relative path).

<criterion id="W2-4-AC1" cell_refs="ST-w-4"><invocation>python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_4_tests.py</invocation><expect>W24-OK</expect></criterion>
`W2-4-AC1` -- the eight named tests pass. On your branch now: `W24-BAD not-passed=test_opal_model_is_not_listed,...`.

<criterion id="W2-4-AC2" cell_refs="ST-w-4"><invocation>python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_4_seam.py</invocation><expect>W24-SEAM-OK</expect></criterion>
`W2-4-AC2` -- SEAM on real data: the re-made record lists neither `Opal Satellite 50` nor `Opal Short-Term`, still lists
`Opal_Muni_Income` as `RULE_NOT_COUNTED`, and carries the four lines. On your branch now: `W24-SEAM-BAD no EXCLUDED-AS-MODEL: line`.

### AMENDMENT A7 (issuer, 2026-10-09 ~05:5xZ) -- Andrew-direct: Opal_Muni_Income is a Custom model

Andrew-direct ~05:3xZ, VERBATIM: "no that is a custom model, we should not be putting that in ALT Strategies." (record `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/ANDREW_DIRECT_20261009_053xZ_OPAL_MUNI_INCOME_IS_A_CUSTOM_MODEL_NOT_ALT.md`).
Re-make the Cottonwood record with the Muni rule in its cfg narrowed to `Opal_Muni_Sleeve` (member `null`), so `Opal_Muni_Income` is
an Opal Model excluded as one (it appears in EXCLUDED-AS-MODEL) and is not listed; `Opal_Muni_Sleeve` stays listed `RULE_NOT_COUNTED`.
Correct the EXCLUDED-AS-MODEL line to say the set is the roster+definition `is_opal` union (ruling A6). Code and tests do not change.
`W2-3-AC2` and `W2-4-AC2` now require `Opal_Muni_Income` NOT listed and `Opal_Muni_Sleeve` listed; re-run all four criteria and re-flip
`<status>` to `complete` only when all pass.

## BOUNDS

- **GUARD 1:** no deploy and no write to the ETF universe config before the 2026-10-09 13:30Z read. You write nothing in AWS;
  read-only S3 is allowed.
- Do not edit `rebalancer_schemas.py` (another worker owns it) or any gold script.
- **Grant.** The `<paths>` block plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_STRATID-W2-W6-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below. Rows are APPEND-ONLY.

<paths>
data/assets/scripts/silver/opal_unidentified.py
data/assets/scripts/silver/tests/test_opal_unidentified.py
org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~6/UNIDENTIFIED_STRATEGY_CANDIDATES.md
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_W2.md
</paths>

The block is your WRITE grant (paths relative to your worktree root are the same files). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_W2.md</decomp_doc> (workstream 2), cell `ST-w-3`.
<owned_cells>ST-w-3 ST-w-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: W2-3-AC1, W2-3-AC2. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~6/MDPF_STRATID.TO-W2-3.unidentified-strategy-list.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> W2-3-AC1 W2-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the RESULT and DENOMINATOR lines, the top 10 listed rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing wired into a running path (ruling W5).
comp-iam: DECLARED-NOT-APPLICABLE read-only S3 under the worker's credentials.
comp-adversary: DECLARED-NOT-APPLICABLE recorded in the decomposition battery.
risk: LOCAL -- code, tests and a recorded document on a branch; serving the list at a builder address is a drain act (ruling W5).
direct_act: false -- workstream issuance with shared contracts.
</preflight>

Source: PRD ADDENDUM v0.4 @c690447ee7 (S08; GUARD 1, GUARD 2); C-UNIDENTIFIED, C-MUNI-VERIFY; decomposition rulings W1-W5.
