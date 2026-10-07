# TO MDPF_SECCLASS.TO-SC-e61 -- round 10 SC-e-61: W38-S4: the FWD-10 producer's unresolved-US gate is re-keyed off sub_asset_class

<to_id>MDPF_SECCLASS.TO-SC-e61</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~50</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-61` (`decompositions/MDPF_SECCLASS_DECOMP_R10.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-61`. CTO round-9 analysis ruling 2.2: "SC-e-57 does not land until the producer's unresolved-US gate is re-keyed off
`sub_asset_class`, with a test that a new US stock with no sub-class still writes."

**Your base is the held branch `q/dell1/secclass-r9-held-38/r1` (4cb237fe22).** It carries SC-e-57's module change: a resolved GICS sector
now goes to `planned["gics_sector"]` only, and a US listing has no `sub_asset_class`. With that change, the 24 tests of
`infra/aws/lambda/mdpf-secclass/new-security-classifier/tests/test_new_security_classifier.py` read 7 failed and 17 passed (row W38-S4). The
cause is `is_unresolved_us()` in `infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py` (~:229-233). It returns True
for a bare-ticker item (`identifier_namespace` None or `TICKER`) with no `sub_asset_class`, and `run()` never writes an unresolved item.

**Build:**
- Re-key `is_unresolved_us()` on whether the shared module RESOLVED the item. A bare-ticker US item with a `gics_sector` is resolved.
  One with neither `gics_sector` nor `sub_asset_class` stays unresolved. Read the fields from the planned item; never re-derive them.
- Update the docstring.
- In the test file, add `test_a_new_us_stock_with_no_sub_class_and_a_resolved_sector_is_written`. Keep every existing test's intent; a
  test whose fixture assumed a sector in `sub_asset_class` may move its fixture to `gics_sector`, and must not be deleted or weakened.
- The producer writes put-on-absence only: do not change that.

### AMENDMENT 1 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~15:3xZ; release mode, CTO round-11 analysis @fc96f7c48c section 2 item 2)

**The release port.** e61 (c0eb742061, ~42) and e57 (a23415cd44, ~38) are complete and VALID on the held-38 line, which also carries
e55, e56 and e62. Their code files cherry-pick CLEAN onto the round head ae61f93efe (CLOUD plus round records): 0 conflicts, and
new-security-classifier + `_shared` 239 passed, sector-writer 29 passed.

Slot ~50 on branch `secclass-r12-rel-e57e61` commits that port, so the pair releases without e55, e56 or e62. The issuer's lane refuses
these paths.

**Your work:** the four files are ALREADY MODIFIED in your worktree (the issuer's cherry-pick, uncommitted). Do not rebuild.
1. Confirm with `git diff` that they equal the code of a23415cd44 + c0eb742061: `git diff HEAD -- <file>` against
   `git show a23415cd44 -- <file>` / `git show c0eb742061 -- <file>`.
2. Commit the four files.
3. Run AC1 and AC2, plus the two control suites.
4. Write and validate the proof instance (path below, slot ~50), flip status to complete, and commit.

### ACCEPTANCE

<criterion id="SC10-e61-AC1" cell_refs="SC-e-61"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/mdpf-secclass/new-security-classifier/tests/test_new_security_classifier.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e61-AC1` -- the producer's tests, the new one included, pass over SC-e-57's module.

<criterion id="SC10-e61-AC2" cell_refs="SC-e-61"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e61_us_no_subclass_written.py</invocation><expect>SC-E61 ok=True</expect></criterion>
`SC10-e61-AC2` -- a resolved bare-ticker US item is not unresolved; an unresolved one still is (difference control).
The check reads the tree it is run from (your worktree root).

<expected_criteria>SC10-e61-AC1,SC10-e61-AC2</expected_criteria>

Dry-run at the base (4cb237fe22, 2026-10-07): SC10-e61-AC1 FAIL as expected (7 failed, 17 passed); SC10-e61-AC2 FAIL as expected (`resolved_is_unresolved=True`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54).
- No deploy, no Lambda rebuild, no Terraform, no table write. Your branch rides the held-38 line, and SC-e-57's release is an issuer act
  under its pair. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W50-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py
infra/aws/lambda/mdpf-secclass/new-security-classifier/tests/test_new_security_classifier.py
infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py
infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R10.md</decomp_doc> (round 10), cell `SC-e-61`.
<owned_cells>SC-e-61</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC10-e61-AC1, SC10-e61-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~50/MDPF_SECCLASS.TO-SC-e61.fwd10-unresolved-gate-rekey.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC10-e61-AC1,SC10-e61-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the gate before and after, each moved fixture, AC1/AC2 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the producer's schedule is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes.
comp-adversary: RUN -- W38-S4 (a re-key that admits a truly unresolved item: AC2's difference arm); a test weakened to pass (refusal clause); BLIND: the producer's next live run (the e57 release's real run).
lane: the <paths> block IS the grant; base is the held-38 line by issuer ruling in DECOMP_R10.
</preflight>

Source: round-9 analysis @9b6348f15e section 2.2, section 3 item 2; row W38-S4; PRD v0.14 (ADMITTED); DECOMP_R10.
