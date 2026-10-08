# TO MDPF_SECCLASS.TO-SC-e67 -- round 12 SC-e-67: S60: no COT producer emits multi_asset (the class input behind D_04's SGIIX)

<to_id>MDPF_SECCLASS.TO-SC-e67</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~57</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-67` (`decompositions/MDPF_SECCLASS_DECOMP_R12.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-67`. CTO round-12 analysis section 3 item 1: "S60: the COT `D_04` producer stops emitting `multi_asset`."

**Row S60, measured:** COT's D_04 (`data/cot/scripts/gold/D_04.client_portal_summary.py`, the writer of
`platinum/clients/*/concentration.json`) served SGIIX as `asset_class: multi_asset` in z09305621 and z09305679 at its 2026-10-07T11:40Z
run. D_04's own source has no `multi_asset` literal, so the value enters from a COT class input upstream of it. The canonical table holds
0 multi_asset, and `_shared/etf_classification.ETF_CLASSIFICATIONS['SGIIX']` reads `equity` in the repo.

**Build:**
1. Trace, by reading the COT gold chain from D_04 back (its class-producing input: a COT dimension script, a lib, or a mapping), the ONE
   place that yields `multi_asset` for SGIIX. Read only: `data/cot/scripts/gold/`, `infra/aws/lambda/v2_portal/_shared/`, and
   read-only S3 GET on `opal-data-cot` (allowed). Name the file and line in your report.
2. Fix it at that source so no COT producer emits `multi_asset`. A former multi_asset key takes its canonical class (the table, or the
   six-class seed), and never a new value you invent.
   - **Bound:** if the source is `infra/aws/lambda/v2_portal/_shared/etf_classification.py`, STOP. That file belongs to SC-e-71, so file
     a row naming it and write no code.
3. Add your source file's path to this order's `<paths>`. Do it with ONE line in your first commit, and say so in the report.
4. Write `data/cot/scripts/gold/tests/test_d04_no_multi_asset.py`. On a small fixture holding SGIIX and one ordinary equity, the
   producer path emits no `multi_asset`. The difference control: an unrelated ticker's class is unchanged.
5. Write the half request `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_D04_MULTI_ASSET_20261008.md`, shaped like
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md`. It names:
   - the shipped code key(s) the fix moves and the served keys it changes (the two concentration.json files at least);
   - both branches (SGIIX reads equity, or stays put if absent);
   - the rollback by prior VersionId;
   - the COT gold schedule as the timing input;
   - that the deploy waits on Andrew's limit item 5 (routes-host), which today denies dell1 any opal-data-cot code write.

### ACCEPTANCE

<criterion id="SC12-e67-AC1" cell_refs="SC-e-67"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/cot/scripts/gold/tests/test_d04_no_multi_asset.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC12-e67-AC1` -- the producer path emits no multi_asset, with its control.
<criterion id="SC12-e67-AC2" cell_refs="SC-e-67"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_D04_MULTI_ASSET_20261008.md</invocation><expect>HALF-READY</expect></criterion>
`SC12-e67-AC2` -- the half request for the served COT keys is ready to sign.

<expected_criteria>SC12-e67-AC1,SC12-e67-AC2</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~02:5xZ): SC12-e67-AC1 FAIL as expected (PYTEST-BAD rc=4: the test file is absent); SC12-e67-AC2 FAIL as expected (NOT-READY: absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- No deploy and no S3 write: the COT code-prefix deploy waits on limit item 5. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W57-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/cot/scripts/gold/C_06.client_mix_timeseries.py
data/cot/scripts/gold/tests/test_d04_no_multi_asset.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_D04_MULTI_ASSET_20261008.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/MDPF/MDPF_SECCLASS/task-orders/MDPF_SECCLASS.TO-SC-e67.cot-d04-no-multi-asset.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R12.md</decomp_doc> (round 12), cell `SC-e-67`.
<owned_cells>SC-e-67</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC12-e67-AC1, SC12-e67-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~57/MDPF_SECCLASS.TO-SC-e67.cot-d04-no-multi-asset.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC12-e67-AC1,SC12-e67-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the COT gold cron(30 10 * * ? *) is the release's timing input, named in the half.
comp-iam: DECLARED-NOT-APPLICABLE no grant change; the cot code-prefix deny (item 5) is why the deploy is held, recorded in the half.
comp-adversary: RUN -- S60; an invented class (step 2 takes the canonical class); a fix in another cell's file (step 2 bound); BLIND: the COT run after the deploy (its pair's real run).
lane: the <paths> block IS the grant.
</preflight>

Source: round-12 analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_12_20261008.md @82c4790d6c section 3 item 1; CTO note msg 766; DECOMP_R12.
