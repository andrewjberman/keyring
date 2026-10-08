# TO MDPF_SECCLASS.TO-SC-e74 -- round 13 SC-e-74: clean_name() drops the "/<state>" incorporation suffix; the CSCO row's rewrite is staged

<to_id>MDPF_SECCLASS.TO-SC-e74</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~64</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-74` (`decompositions/MDPF_SECCLASS_DECOMP_R13.md`) |
**outcome_ref:** FWD-14, FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-74`. `clean_name()` in `C:/Dev/ajb_workspace/infra/aws/lambda/v2_portal/_shared/security_name.py` keeps a "/<state>"
incorporation suffix: "Cisco Systems Inc/Delaware" serves as is. The ETF positioning publisher serves the table row's `name`, so the
suffix reaches the page.

**Measured:** in the etf-classifications table, exactly 1 row carries the suffix: `CSCO` "Cisco Systems Inc/Delaware".

**Build:**
1. In `clean_name()`, drop a trailing incorporation suffix, and only one that comes DIRECTLY after a corporate-form token (Inc, Corp,
   Co, Ltd, LLC, LP, PLC, and the module's other forms). The suffix is "/<US state name or 2-letter postal code>" or "/NEW", optionally
   closed by "/", possibly repeated, with optional spaces around the slash. Put the state list in a module constant. Any other slash
   stays: dates, "LARGE/MID", "MUNI/CA". The output stays idempotent. Standard library and ASCII only.
2. Write `infra/aws/lambda/v2_portal/_shared/tests/test_security_name_state_suffix.py`. It must pin:
   - the four strip cases;
   - the eight unchanged controls in `R13_CHECKS/sc_r13_state_suffix.py`.
3. In `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py`, add `--set <tsv>`. With no
   `--set`, it reads the V2 set exactly as today.
4. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_R13_STATE_SUFFIX_20261008.tsv`:
   - the V2 set's columns, with one WRITE line for `CSCO`;
   - source `table`, the current name read live, and the clean name from the new `clean_name()`.
5. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_STATE_SUFFIX_NAME_20261008.md`.
   Shape it like `NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_V2_20261007.md`. It must contain:
   - the one key, before and after;
   - the write command, the snapshot path and the rollback command;
   - the blast radius: one `name` attribute and `updated_by`, no class.
   Leave `## COO half` and `## CTO half` unsigned.

### ACCEPTANCE

<criterion id="SC13-e74-AC1" cell_refs="SC-e-74"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R13_CHECKS/sc_r13_state_suffix.py</invocation><expect>STATE-SUFFIX ok=True</expect></criterion>
`SC13-e74-AC1` -- the four strip cases and the eight controls read as pinned, each idempotent.
<criterion id="SC13-e74-AC2" cell_refs="SC-e-74"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py --set org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_R13_STATE_SUFFIX_20261008.tsv</invocation><expect>CLEAN-NAME-V2-DRY-RUN write=1 custody=0 seed_source=0 unchanged=0 refused_stale=0 puts=0</expect></criterion>
`SC13-e74-AC2` -- the dry run over the one-row set plans exactly the CSCO write and writes nothing.
<criterion id="SC13-e74-AC3" cell_refs="SC-e-74"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC13-e74-AC3` -- the whole _shared suite still passes, the new pin included.

<expected_criteria>SC13-e74-AC1,SC13-e74-AC2,SC13-e74-AC3</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~18:3xZ):
- SC13-e74-AC1: FAIL, as expected (ok=False, pass=8 of 12).
- SC13-e74-AC2: FAIL, as expected (no `--set`, no set file).
- SC13-e74-AC3: PASS, as expected (control, 328 passed).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **No write of any kind to AWS:**
  - Reads are allowed: a consistent get of the CSCO row for the set's current name.
  - Never run `--write` or `--rollback`; the write is the issuer's act.
  - No deploy. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-W64-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/security_name.py
infra/aws/lambda/v2_portal/_shared/tests/test_security_name_state_suffix.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_R13_STATE_SUFFIX_20261008.tsv
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_STATE_SUFFIX_NAME_20261008.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R13.md</decomp_doc> (round 13), cell `SC-e-74`.
<owned_cells>SC-e-74</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC13-e74-AC1, SC13-e74-AC2, SC13-e74-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~64/MDPF_SECCLASS.TO-SC-e74.clean-name-state-suffix.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC13-e74-AC1,SC13-e74-AC2,SC13-e74-AC3`. Record a
judgment criterion as `UNVERIFIABLE-BY-INSTRUMENT`, with a `status_reason` naming 3.0.0_SA_CVO, never as PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the table write is the issuer's act under its pair; the _shared deploy follows in the deploy lane.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (a read of one row under the seat's existing role).
comp-adversary: RUN -- a slash that is not a suffix (dates, LARGE/MID, MUNI/CA) kept; idempotence; BLIND: names produced outside clean_name() (the seed overrides; CSCO has none).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL1 msg 1039 (DECISION, SELF-DRIVE tick 17); SECHIST round-1 analysis @0141533760 section 2.2; DECOMP_R13.
