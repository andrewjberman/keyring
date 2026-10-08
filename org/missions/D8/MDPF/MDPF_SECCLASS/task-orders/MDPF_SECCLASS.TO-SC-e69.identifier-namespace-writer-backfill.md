# TO MDPF_SECCLASS.TO-SC-e69 -- round 12 SC-e-69: W26-S5: the AI runner sets identifier_namespace; a backfill writer for rows without one

<to_id>MDPF_SECCLASS.TO-SC-e69</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~59</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-69` (`decompositions/MDPF_SECCLASS_DECOMP_R12.md`) |
**outcome_ref:** FWD-2, FWD-17 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-69`. CTO round-12 analysis section 3 item 3: "identifier_namespace on every CUSIP-keyed row the AI runner and the DIRECT writers
land. The writer change comes first, then a conditional backfill of rows that have none (count printed)." It must land before the AI
legs run.

**Measured:** `landing_row()` in `infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py` builds no identifier_namespace
(row W26-S5). The two executors wrap the table in a NamespaceTable, but the runner itself does not. The contract's
`fields.identifier_namespace.values` are TICKER, CUSIP, BLOOMBERG and NAME (`org/standards/MDPF_SECCLASS_CONTRACT.json`).

**Build:**
1. In `landing_row()`, set `identifier_namespace` from the key form:
   - `CUSIP:` -> CUSIP;
   - `NAME::` -> NAME;
   - otherwise TICKER, unless the contract's definitions say a bare form is something else (read them; quote the rule you apply).
   Change nothing else in the runner.
2. Write `infra/aws/lambda/v2_portal/yang_pipeline/tests/test_runner_identifier_namespace.py`. It covers one key of each form, and
   the difference control that every other landing_row field is unchanged.
3. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/namespace_backfill.py`:
   - dry run by default; it scans etf-classifications (paginated, ConsistentRead) and plans a conditional update
     (`attribute_not_exists(identifier_namespace)`) for each CUSIP: or NAME:: keyed row lacking one;
   - `--write --half --snapshot` and `--rollback`;
   - it prints `NAMESPACE-BACKFILL-DRY-RUN rows=<n> missing_cusip=<n> missing_name=<n> puts=0`.
4. Write the backfill half request `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_IDENTIFIER_NAMESPACE_BACKFILL_20261008.md`, shaped like
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_V2_20261007.md`, with the count, both branches, the rollback and the readers.

### ACCEPTANCE

<criterion id="SC12-e69-AC1" cell_refs="SC-e-69"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/yang_pipeline/tests/test_runner_identifier_namespace.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC12-e69-AC1` -- landing_row sets the namespace per key form, with its control.
<criterion id="SC12-e69-AC2" cell_refs="SC-e-69"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/namespace_backfill.py</invocation><expect>NAMESPACE-BACKFILL-DRY-RUN</expect></criterion>
`SC12-e69-AC2` -- the backfill's dry run prints its count and makes no write.
<criterion id="SC12-e69-AC3" cell_refs="SC-e-69"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_IDENTIFIER_NAMESPACE_BACKFILL_20261008.md</invocation><expect>HALF-READY</expect></criterion>
`SC12-e69-AC3` -- the backfill's half request is ready; a table write needs its pair, which is the third criterion's reason.

<expected_criteria>SC12-e69-AC1,SC12-e69-AC2,SC12-e69-AC3</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~02:5xZ): SC12-e69-AC1 FAIL as expected (PYTEST-BAD rc=4: absent); SC12-e69-AC2 FAIL as expected (absent); SC12-e69-AC3 FAIL as expected (NOT-READY: absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- No table write and no model call: the runner is not run except by its tests, and the backfill only in dry run. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W59-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py
infra/aws/lambda/v2_portal/yang_pipeline/tests/test_runner_identifier_namespace.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/namespace_backfill.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_IDENTIFIER_NAMESPACE_BACKFILL_20261008.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R12.md</decomp_doc> (round 12), cell `SC-e-69`.
<owned_cells>SC-e-69</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC12-e69-AC1, SC12-e69-AC2, SC12-e69-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~59/MDPF_SECCLASS.TO-SC-e69.identifier-namespace-writer-backfill.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC12-e69-AC1,SC12-e69-AC2,SC12-e69-AC3` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the runner is ad hoc; it must land before the AI legs run (issuer order).
comp-iam: DECLARED-NOT-APPLICABLE dell1 writes etf-classifications already.
comp-adversary: RUN -- W26-S5; overwriting a namespace a row already has (attribute_not_exists); a value outside the contract (the four-value enum); BLIND: the AI legs' rows (graded by ai_leg_verify at their close).
lane: the <paths> block IS the grant.
</preflight>

Source: round-12 analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_12_20261008.md @82c4790d6c section 3 item 3; CTO note msg 766; DECOMP_R12.
