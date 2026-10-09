# TO MDPF_SECCLASS.TO-SC-e84 -- round 17 SC-e-84: COT classify_position falls back to the canonical NAME:: row (the BD port)

<to_id>MDPF_SECCLASS.TO-SC-e84</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~74</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-84` (`decompositions/MDPF_SECCLASS_DECOMP_R17.md`) |
**outcome_ref:** FWD-16 | **depends_on:** e67 leg G clean (10:30Z COT run)

---

## WORKER FACE

### THE CELL

`SC-e-84`, row MDPF_SECCLASS-D1-W66-S2, CTO ruling R1 (round-16 analysis). Black Diamond's classifier reads the canonical
`NAME::<normalized name>` row of `etf-classifications` when a position's identity chain cannot place it. Cottonwood's does not.
`data/cot/scripts/gold/lib/etf_classifier.py` `classify_position(ticker, cusip=None, cash_equivalent=None)` (:137-158) runs the cash
flag, then the ticker row, then the `CUSIP:` row, else returns `('unclassified', 'none')`. Round 16 measured that a `NAME::` row would
place 1,060 COT positions, $17,769,409.83 (3.21 pct of COT market value).

**Build:**
1. Give `classify_position` a fourth keyword argument, `asset_name=None`. Only when the cash flag, the ticker row and the `CUSIP:` row
   ALL miss, and `asset_name` is non-blank, read `'NAME::' + <normalized name>`. The key form must be exactly BD's
   `ETFClassifier.normalize_name` (`data/black_diamond/scripts/gold/lib/etf_classifier.py`). Port that function into the COT lib; do not
   import across firm trees. If the row has an `asset_class`, return `(asset_class, 'table name')`.
2. Keep every other answer exactly as today:
   - a position placed by cash flag, ticker row or `CUSIP:` row returns the same `(class, rule)` with or without the name;
   - no name, or a name with no `NAME::` row, returns `('unclassified', 'none')`.
   - Update the docstring: add rule `'table name'` as step 4 and cite "CTO ruling R1, MDPF_SECCLASS round-16 analysis" beside the
     "never from a name" line, since the class comes from a table row keyed by the name.
3. Pass the position's name at every call site that has it:
   - `data/cot/scripts/gold/C_06.client_mix_timeseries.py` :185 and :205;
   - `data/cot/scripts/gold/D_03.composition_artifacts.py` :131.
   Use the same row's `asset_name` the caller already reads, as a parallel series where the caller zips series. C_06 :229 re-classifies
   a retired-class holding dict: pass `h.get('asset_name')` if the dict carries it, else leave the call as is. Change nothing else in
   either producer.
4. Extend `data/cot/scripts/gold/tests/test_cot_position_rule.py`, keeping its 3 existing tests green, with the table client stubbed:
   - a no-ticker-row, no-`CUSIP:`-row position with a live `NAME::` row returns `(class, 'table name')`;
   - a ticker-row position given a name with a different `NAME::` class keeps its ticker answer (control);
   - a name with no `NAME::` row stays `('unclassified', 'none')` (control).
5. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PORT_20261009.md`,
   shaped like `NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_TICKER_FALLBACK_20261009.md` in that folder (`## The act`, `## Blast radius`,
   `Rollback per key`). It must name:
   - the act: deploy exactly the three files (the lib, C_06, D_03) to `s3://opal-data-cot/code/gold/`, with `safe-deploy.sh` naming
     the three paths;
   - the writers of the served COT class: C_06 and D_03 (N = 2), each calling `classify_position`;
   - the blast radius: the candidate diff from AC1's run (placed positions, dollars, and the class totals they move into);
   - the rollback per key: each of the three objects' current served VersionId and ETag (read with `aws s3api head-object`,
     read-only).
   Leave both halves unsigned.

### ACCEPTANCE

<criterion id="SC17-e84-AC1" cell_refs="SC-e-84"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R17_CHECKS/sc_r17_cot_port_check.py</invocation><expect>COT-PORT ok=True</expect></criterion>
`SC17-e84-AC1` -- over the round-16 partition, no position placed without the name changes, every newly placed position carries
rule `table name`, at least 1,060 positions are placed, and the residue stays `('unclassified', 'none')`. Do not edit this check.
<criterion id="SC17-e84-AC2" cell_refs="SC-e-84"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/cot/scripts/gold/tests/test_cot_position_rule.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC17-e84-AC2` -- the COT position-rule tests pass, the new arms included.
<criterion id="SC17-e84-AC3" cell_refs="SC-e-84"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PORT_20261009.md</invocation><expect>HALF-READY</expect></criterion>
`SC17-e84-AC3` -- the half request carries the act, the blast radius with a candidate diff, and the rollback per key.

<expected_criteria>SC17-e84-AC1,SC17-e84-AC2,SC17-e84-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-09 ~09:5xZ):
- SC17-e84-AC1: FAIL, as expected (`reason=classify_position-rejects-asset_name`). A scratch port calling BD's `normalize_name` read
  `COT-PORT ok=True positions=21024 placed=1060 placed_mv=17769409.83 floor=1060 overridden=0 wrong_rule=0` in 7.5 s, so the criterion is
  satisfiable.
- SC17-e84-AC2: PASS, as expected (control, 3 passed).
- SC17-e84-AC3: FAIL, as expected (the half is absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, batch get): no write to any table or bucket, no deploy, no invoke. Never push.
- **No cross-firm import:** the COT lib must not import from `data/black_diamond/`. Port the normalizer's code.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W74-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.

<paths>
data/cot/scripts/gold/lib/etf_classifier.py
data/cot/scripts/gold/C_06.client_mix_timeseries.py
data/cot/scripts/gold/D_03.composition_artifacts.py
data/cot/scripts/gold/tests/test_cot_position_rule.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PORT_20261009.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R17.md</decomp_doc> (round 17), cell `SC-e-84`.
<owned_cells>SC-e-84</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC17-e84-AC1, SC17-e84-AC2, SC17-e84-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~74/MDPF_SECCLASS.TO-SC-e84.cot-name-key-port.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC17-e84-AC1,SC17-e84-AC2,SC17-e84-AC3`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, the candidate diff, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the scheduled COT gold fire (cron 30 10 * * ? *) is unchanged; the cell changes what it computes, and the deploy is the issuer's act under the pair.
comp-iam: DECLARED-NOT-APPLICABLE read-only for the worker: S3 get on opal-data-cot and get/batch-get on etf-classifications, both read by dell1 workers this session.
comp-adversary: RUN -- a placed position overridden by a name (AC1 arm 1, AC2 control); a different key form than BD's (AC1 floor equals SC-e-82's BD-form count); a cross-firm import (bounds); a residue answered with a wrong rule (AC1 arm 4)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-16 analysis section 2 R1 and section 3 item 1 (msg 2187); row D1-W66-S2; DECOMP_R17.
