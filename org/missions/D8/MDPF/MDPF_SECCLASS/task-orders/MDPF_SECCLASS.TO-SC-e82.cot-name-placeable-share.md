# TO MDPF_SECCLASS.TO-SC-e82 -- round 16 SC-e-82: measure, read-only, Cottonwood's unclassified share that a NAME:: row would place

<to_id>MDPF_SECCLASS.TO-SC-e82</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~72</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-82` (`decompositions/MDPF_SECCLASS_DECOMP_R16.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-82`, row MDPF_SECCLASS-D1-W66-S2. Black Diamond's classifier now reads a canonical `NAME::<normalized name>` row for a position its
identity chain cannot place (round 15). Cottonwood's classifier, `data/cot/scripts/gold/lib/etf_classifier.py` `classify_position(ticker,
cusip, cash_equivalent)` (:137-158), has no name path: cash flag, then ticker row, then `CUSIP:` row, else `unclassified`. Nobody has
measured how much of COT's unclassified a `NAME::` row would place. This cell MEASURES that, read-only. It ports nothing.

**Build:**
1. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/cot_name_share.py`, a read-only script that:
   - reads COT's newest canonical holdings partition, `s3://opal-data-cot/gold/canonical/holdings/<newest date>.parquet` (2026-10-07 at
     the cut; columns include `asset_name`, `ticker`, `market_value`, and a CUSIP if present);
   - classifies each position with COT's own `classify_position` from `data/cot/scripts/gold/lib/etf_classifier.py`, imported from the
     repo, exactly as COT gold does;
   - for each position that lands `unclassified`, reads `etf-classifications` for `'NAME::' + <the BD lib's
     ETFClassifier.normalize_name(asset_name)>`, the same key form the BD lib uses (`data/black_diamond/scripts/gold/lib/etf_classifier.py`).
     Use consistent get_item or a batch get; nothing else;
   - writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/COT_NAME_SHARE_20261009.json` with exactly these fields:
     `as_of`, `source` (the S3 key read), `positions`, `unclassified_positions`, `unclassified_mv`, `total_mv`,
     `name_placeable_positions`, `name_placeable_mv`, `threshold_pct` (use 0.5), `material`
     (`100*name_placeable_mv/total_mv >= threshold_pct`), `method` (one sentence), and a `top` list of the 10 largest name-placeable
     positions (name, NAME:: key, class, market_value).
2. Run it once and commit both files. Report the line `sc_r16_cot_name_share_check.py` prints.

### ACCEPTANCE

<criterion id="SC16-e82-AC1" cell_refs="SC-e-82"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/sc_r16_cot_name_share_check.py</invocation><expect>COT-NAME-SHARE ok=True</expect></criterion>
`SC16-e82-AC1` -- the record exists, carries every field and a non-empty denominator, its counts and dollars nest (placeable <=
unclassified <= total), and `material` follows from the percentage and the threshold. Do not edit this check.

<expected_criteria>SC16-e82-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-09 ~09:0xZ): SC16-e82-AC1 FAIL, as expected (the record is absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY**: `s3 get-object`/`list` on opal-data-cot, and get_item or batch_get_item on etf-classifications. No write to any
  table or bucket, no deploy, no invoke. Never push. Do not copy COT data into another firm's tree.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W72-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the check.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/cot_name_share.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/COT_NAME_SHARE_20261009.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R16.md</decomp_doc> (round 16), cell `SC-e-82`.
<owned_cells>SC-e-82</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC16-e82-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~72/MDPF_SECCLASS.TO-SC-e82.cot-name-placeable-share.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC16-e82-AC1`.
</proof_of_spec>

**REPORT:** the measured numbers (positions, unclassified and placeable counts and dollars, pct, material), what you read, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-off read-only measure.
comp-iam: DECLARED-NOT-APPLICABLE read-only S3 get on opal-data-cot and DynamoDB get on etf-classifications, both read by dell1 tonight.
comp-adversary: RUN -- a different NAME:: key form than BD's (step 1 names the BD normalize_name); an empty denominator (the check refuses); a materiality verdict not computed from its numbers (the check recomputes it)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO rounds 13-15 analysis section 3 item 4 (msg 2139); row D1-W66-S2; DECOMP_R16.
