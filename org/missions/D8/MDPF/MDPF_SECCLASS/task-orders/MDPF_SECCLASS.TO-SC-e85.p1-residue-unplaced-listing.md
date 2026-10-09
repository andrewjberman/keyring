# TO MDPF_SECCLASS.TO-SC-e85 -- round 17 SC-e-85: the p1 residue's 11 keys join FWD-15's UNPLACED-KEY census (read-only listing)

<to_id>MDPF_SECCLASS.TO-SC-e85</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~75</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-85` (`decompositions/MDPF_SECCLASS_DECOMP_R17.md`) |
**outcome_ref:** FWD-15 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-85`, CTO round-16 analysis item 2. The `bd-securities-cot-new-p1` ledger closed with 16 keys absent from `etf-classifications`.
Five are e49 FINAL refusals; the other 11 were never in FWD-15's plan and were routed to FWD-15's UNPLACED-KEY census. That census
(`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNPLACED_KEY_CENSUS_20261008.json`, written by
`R12_CHECKS/unplaced_key_census.py`) covers 99 plan entries and does not hold these 11. This cell lists them beside it, read-only.

The 11 keys:
- `ETHA`
- `NAME::AST INVESTMENT GRADE BOND PORTFOLIO`
- `NAME::AXA MODERATE ALLOCATION`
- `NAME::BENEFIT FIXED RATE OPTION`
- `NAME::CALAMOS STRATEGIC TOTAL RETURN COM SH BEN INT`
- `NAME::GRAYSCALE ETHEREUM STAKING MINI ETF`
- `NAME::JOHN HANCOCK LIFE INSURANCE CO 5 06 15 2028`
- `NAME::MFS MULTIMARKET INCOME TR SH BEN INT`
- `NAME::MORGAN STANLEY 6 25 08 09 2026`
- `NAME::PATRIOT BK N A 4 5 2026`
- `NAME::PRUDENTIAL ANNUITY`

**Build:** write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/P1_RESIDUE_UNPLACED_20261009.json`. Its top level holds
`claim` (one sentence naming it a read-only measure), `sources` (the S3 keys and table read) and `entries`, one per key, each with:
- `key`;
- `pattern`: the census's own `pattern_of(key, {})`, imported from `R12_CHECKS/unplaced_key_census.py`;
- `table_row_present`: a consistent get-item on `etf-classifications`, us-east-1;
- `bd_positions` and `bd_mv`: from the newest `s3://opal-data-bd/gold/canonical/holdings/<date>.parquet`;
- `cot_positions` and `cot_mv`: from the newest `s3://opal-data-cot/gold/canonical/holdings/<date>.parquet`;
- `as_of_bd` and `as_of_cot`: the partition dates read.

How a position matches a key:
- a plain key matches a row whose `ticker` equals it;
- a `NAME::` key matches a row whose `'NAME::' + normalize_name(asset_name)` equals it, using BD's
  `ETFClassifier.normalize_name` (`data/black_diamond/scripts/gold/lib/etf_classifier.py`) for both firms.

Positions are integers and mv values are numbers (a NaN market value counts as 0). Write it with a scratch script under `.scratch/`;
commit only the JSON.

### ACCEPTANCE

<criterion id="SC17-e85-AC1" cell_refs="SC-e-85"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R17_CHECKS/sc_r17_p1_residue_check.py</invocation><expect>P1-RESIDUE ok=True</expect></criterion>
`SC17-e85-AC1` -- the record holds exactly the 11 keys once each, carries every field, its patterns equal the census's, and its table
presence equals a live consistent read. Do not edit this check.

<expected_criteria>SC17-e85-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-09 ~09:5xZ): SC17-e85-AC1 FAIL, as expected (the record is absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY**: `s3 get-object`/`list` on opal-data-bd and opal-data-cot, and get_item on etf-classifications. No write to any
  table or bucket, no deploy, no invoke. Never push. The record carries counts and dollars per key only; copy no position row into
  any tree.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W75-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the check.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/P1_RESIDUE_UNPLACED_20261009.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R17.md</decomp_doc> (round 17), cell `SC-e-85`.
<owned_cells>SC-e-85</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC17-e85-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~75/MDPF_SECCLASS.TO-SC-e85.p1-residue-unplaced-listing.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC17-e85-AC1`.
</proof_of_spec>

**REPORT:** the 11 entries (key, pattern, table presence, BD and COT holdings), the criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-off read-only listing.
comp-iam: DECLARED-NOT-APPLICABLE read-only S3 get on opal-data-bd and opal-data-cot and DynamoDB get on etf-classifications, all read by dell1 workers this session.
comp-adversary: RUN -- a key dropped or doubled (AC1 arm 1); a pattern not the census's own (arm 3); a stale table read (arm 4 re-reads live)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-16 analysis section 3 item 2 (msg 2187); p1 ledger leg R1; DECOMP_R17.
