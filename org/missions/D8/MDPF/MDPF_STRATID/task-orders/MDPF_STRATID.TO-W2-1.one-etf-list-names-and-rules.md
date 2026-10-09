# TO MDPF_STRATID.TO-W2-1 -- workstream 2 ST-w-1: the one Opal ETF list gains full fund names and the SMA name rules as data
<to_id>MDPF_STRATID.TO-W2-1</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~4</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>2</workstream>
**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `ST-w-1` (`decompositions/MDPF_STRATID_DECOMP_W2.md`) | **outcome_ref:** FWD-5, FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`ST-w-1`. Opal has ONE list of its ETFs, `infra/aws/etfs/config/etf_universe.json` (deployed copy: `s3://opal-data-etfs/config/etf_universe.json`).
Today it holds 4 tickers (`DIVZ`, `IDVZ`, `PFDE`, `PFOE`) and no names. A client sleeve named after an Opal ETF, by ticker OR full fund
name, is an Opal ETF Strategy; a non-ETF strategy (Tax, Muni, open-ended) is found by a NAME RULE held as data beside the list. You
add both to the repo file. You do not touch `tickers`, and you write nothing in AWS.

**Add, in `infra/aws/etfs/config/etf_universe.json`:**
1. `"full_names": {"<TICKER>": {"name": "<full fund name>", "source": "<where you read it>"}}` for each of the 4 tickers. The source
   must be an Opal-owned artifact you actually read (a repo file with path:line, an Opal S3 object with its key). Prior art to start
   from: `data/assets/scripts/silver/rebalancer_schemas.py:218-223` ("Pathfinder Disciplined" = PFDE, "Pathfinder Focused Opportunit"
   = PFOE); search the repo's `data/etfs/` and `infra/aws/lambda/etfs-pipeline/` for the fund names. If a name cannot be sourced, do
   not invent it: file a surprise row and leave the criterion failing.
2. `"sma_name_rules": [{"member": "<registry member id>" | null, "pattern": "<python regex, case-insensitive>", "source": "<why>"}]`
   with AT LEAST these rows:
   - `{"member": "pfde", "pattern": "Pathfinder\\s+Disciplined", "source": "Andrew-direct 2026-10-01, record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261001_203xZ_COTTONWOOD_CUSTOM_MODELS_AND_SMA_SLEEVES_YES_TO_ALL_FOUR.md; rebalancer_schemas.py:221"}`
   - `{"member": "pfoe", "pattern": "Pathfinder\\s+Focused\\s+Opportunit", "source": "same record; rebalancer_schemas.py:222"}`
   - a Muni row with `"member": null` whose pattern matches `Opal_Muni_Income` and `Opal_Muni_Sleeve` (source: PRD C-MUNI-VERIFY and
     `org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_STRATID_S07_MUNI_VERIFY_20261009.md`, verdict UNDETERMINED -- so null: found, not
     counted, until a person verifies).
   Patterns must not let one name hit two different non-null members; ticker rows are NOT added here (tickers are matched from
   `tickers` by the matcher, whole word).
3. Update `last_updated` and `description` to say what the two new keys are. Keep every other key.

### ACCEPTANCE

<criterion id="W2-1-AC1" cell_refs="ST-w-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_1_list.py</invocation><expect>W21-LIST-OK</expect></criterion>
`W2-1-AC1` -- the file carries cited `full_names` for exactly the 4 tickers and `sma_name_rules` that give `pfde`, `pfoe` and a null
member for the three probe names. At the base: `W21-LIST-BAD full_names must key exactly ...`.

<criterion id="W2-1-AC2" cell_refs="ST-w-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_1_loaders.py</invocation><expect>W21-LOADERS-OK</expect></criterion>
`W2-1-AC2` -- BOUND: the three ETFS producers' `_load_universe` rule still reads exactly the 4 tickers from the amended file. At the
base: `W21-LOADERS-OK` (it must stay so).

<expected_criteria>W2-1-AC1 W2-1-AC2</expected_criteria>

Run each invocation from your worktree root.

### AMENDMENT A7 (issuer, 2026-10-09 ~05:5xZ) -- Andrew-direct: Opal_Muni_Income is a Custom model

Andrew-direct ~05:3xZ, VERBATIM: "no that is a custom model, we should not be putting that in ALT Strategies." (record `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/ANDREW_DIRECT_20261009_053xZ_OPAL_MUNI_INCOME_IS_A_CUSTOM_MODEL_NOT_ALT.md`).
In `infra/aws/etfs/config/etf_universe.json`, change the Muni row of `sma_name_rules` so its pattern matches `Opal_Muni_Sleeve` and does
NOT match `Opal_Muni_Income` (member stays `null`: the sleeve is still unverified under C-MUNI-VERIFY). Add the record path to its
`source`. `W2-1-AC1` now probes `Opal_Muni_Sleeve` -> {null} and `Opal_Muni_Income` -> no rule; re-run both criteria and re-flip
`<status>` to `complete` only when both pass.

## BOUNDS

- **GUARD 1:** no write to `s3://opal-data-etfs/config/etf_universe.json` and no deploy of anything. The issuer writes S3 after the
  2026-10-09 13:30Z read. Read-only AWS is allowed.
- **Grant.** The `<paths>` block plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_STRATID-W2-W4-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below. Rows are APPEND-ONLY.

<paths>
infra/aws/etfs/config/etf_universe.json
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (paths relative to your worktree root are the same files). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_W2.md</decomp_doc> (workstream 2), cell `ST-w-1`.
<owned_cells>ST-w-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: W2-1-AC1, W2-1-AC2. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~4/MDPF_STRATID.TO-W2-1.one-etf-list-names-and-rules.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> W2-1-AC1 W2-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the four full names with their sources, the rule rows, both check outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE repo data only; nothing scheduled moves.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; read-only under the worker's credentials.
comp-adversary: DECLARED-NOT-APPLICABLE recorded in the decomposition battery.
risk: WORLD (gate floor for an infra/ path) -- in effect a repo file only; the S3 copy is the issuer's drain act after the 13:30Z read (GUARD 1, ruling W1/W2).
direct_act: false -- workstream issuance with shared contracts.
</preflight>

Source: PRD ADDENDUM v0.4 @c690447ee7 (S02, S03; GUARD 1, GUARD 2); C-ONE-LIST, C-SMA-RULES, C-MUNI-VERIFY; decomposition rulings W1-W4.
