# TO MDPF_SECCLASS.TO-SC-e63 -- round 10 SC-e-63: W31-S1 + W34-S1: E_18 (BD and COT) passes a canonical lookup to plan_rows, and the deploy gate ships rivalfunds_classification.py

<to_id>MDPF_SECCLASS.TO-SC-e63</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~44</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-63` (`decompositions/MDPF_SECCLASS_DECOMP_R10.md`) |
**outcome_ref:** FWD-5, FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-63`. CTO round-9 analysis section 3 item 4: "FWD-5: the E_18 switch (W31-S1); a shipped caller of the canonical lookup with
`rivalfunds_classification.py` on the deploy gate's shipped list (W34-S1)."

**Your base is the held branch `q/dell1/secclass-r9-held-34/r1` (18f721a1e8).** It carries SC-e-44: the canonical producer module
`infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` gains `canonical_lookup_from_records` and a `canonical_lookup` input to
`plan_rows`, and imports `rivalfunds_classification` lazily.

The rows, measured:
- **W31-S1:** `data/black_diamond/scripts/gold/E_18.detect_new_securities.py` hands `plan_rows` only keys NOT in the old list (it skips
  every key found by the scan near :215 and :247). Its only lookup is a GetItem on that same old list (~:291), so `e18-scheduled` writes 0.
  The COT copy `data/cot/scripts/gold/E_18.detect_new_securities.py` has the same shape.
- **W34-S2:** no shipped caller passes `canonical_lookup`.
- **W34-S1:** `.tools/safe_deploy_core.py` ships three `lib/_shared` members, in two `"members"` tuples (~:96-100 and ~:132-136):
  `etf_classifications_dynamodb.py`, `etf_classification_scheduled.py` and `etf_classification.py`. `rivalfunds_classification.py` is not
  one, so a gold caller of `canonical_lookup_from_records` would hit ImportError at run time.

**Build:**
1. Both E_18 scripts build a canonical lookup with `canonical_lookup_from_records` and pass it as `canonical_lookup=` to `plan_rows`. The
   records come from the inputs E_18 already reads (the canonical table through the one client, and the Bloomberg/GICS leg the module
   names). The old-list lookup stays as the fallback.
2. Add `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py` to both `"members"` tuples, and extend the comment above them.
   First confirm, by importing it with only `lib/_shared/` on the path, that it imports no other repo module at load. If it does, file a row
   and stop on this step.
3. Tests:
   - `data/cot/scripts/gold/tests/test_e18_scheduled_caller.py`: extend it.
   - `data/black_diamond/scripts/gold/tests/test_e18_canonical_caller.py`: new.
   Each asserts that, for a fixture first-held key with a canonical-leg record and no old-list row, `plan_rows` receives a canonical lookup
   and plans that key (more than 0 canonical rows). The difference control: a key with neither plans nothing.

### ACCEPTANCE

<criterion id="SC10-e63-AC1" cell_refs="SC-e-63"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests/test_e18_canonical_caller.py data/cot/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e63-AC1` -- both E_18 callers plan a first-held key from the canonical leg (with the no-record control), and the COT gold suite still
passes (21 passed at the base).

<criterion id="SC10-e63-AC2" cell_refs="SC-e-63"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e63_shipped_member.py</invocation><expect>SC-E63 ok=True</expect></criterion>
`SC10-e63-AC2` -- both member tuples ship `rivalfunds_classification.py`, and both E_18 scripts pass `canonical_lookup=`.
The check reads the tree it is run from (your worktree root).

<criterion id="SC10-e63-AC3" cell_refs="SC-e-63"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e63-AC3` -- the BD gold suite still passes (control: 76 passed at the base). The third criterion's reason: two firm trees change in
one cell.

<expected_criteria>SC10-e63-AC1,SC10-e63-AC2,SC10-e63-AC3</expected_criteria>

Dry-run at the base (18f721a1e8, 2026-10-07): SC10-e63-AC1 FAIL as expected (no BD caller test file); SC10-e63-AC2 FAIL as expected (`member_lists=2 with_rivalfunds=0 e18_bd=False e18_cot=False`); SC10-e63-AC3 PASS as expected (control, 76 passed).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54).
- Never run `safe-deploy.sh`, no upload, no S3 write, no table write. These are shipped gold scripts and a deploy-gate member list: your
  branch rides the held-34 line, and SC-e-44's deploy plus the "producer live" run are issuer acts under their pairs. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W44-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/black_diamond/scripts/gold/E_18.detect_new_securities.py
data/cot/scripts/gold/E_18.detect_new_securities.py
data/cot/scripts/gold/tests/test_e18_scheduled_caller.py
data/black_diamond/scripts/gold/tests/test_e18_canonical_caller.py
.tools/safe_deploy_core.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R10.md</decomp_doc> (round 10), cell `SC-e-63`.
<owned_cells>SC-e-63</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC10-e63-AC1, SC10-e63-AC2, SC10-e63-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~44/MDPF_SECCLASS.TO-SC-e63.e18-canonical-caller-and-shipped-member.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC10-e63-AC1,SC10-e63-AC2,SC10-e63-AC3` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the E_18 change in each tree, the import-at-load read for rivalfunds_classification, AC1-AC3 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the BD and COT E_18 runs (BD 23:00Z) are the deploy's timing input, an issuer act.
comp-iam: RUN at the cut from TO-DEPLOY-e42's preflight (bd-exporter-ec2-role's bd-securities-access allows Scan on etf-classifications); the COT host role is read by the deploying seat.
comp-adversary: RUN -- W31-S1/W34-S1/W34-S2; a fourth member that imports a fifth at load (step 2's read); BLIND: the live canonical write count (the "producer live" run).
lane: the <paths> block IS the grant; base is the held-34 line by issuer ruling in DECOMP_R10.
</preflight>

Source: round-9 analysis @9b6348f15e section 3 item 4; rows W31-S1, W34-S1, W34-S2; PRD v0.14 (ADMITTED); DECOMP_R10.
