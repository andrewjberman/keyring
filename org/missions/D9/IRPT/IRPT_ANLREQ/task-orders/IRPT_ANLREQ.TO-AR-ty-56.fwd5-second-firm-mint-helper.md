# TO-AR-ty-56 -- FWD-5 build: a mint helper for a SCOPED principal of a second firm (AR-ty-56, round 46, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-ty-56</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~219</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>46</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-ty-56` (`decompositions/IRPT_ANLREQ_DECOMP_R46_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-ty-56`: "FWD-5 build: a mint helper for a scoped principal of a second firm." FWD-5's done-when is a seat-driven exercise: a sign-in at another firm tries the ticket and each package file and is refused every time. Round 45 found the existing FWD-1 mint helper cannot serve it: it writes one synthetic staff user in the firm `opal-capital` WITHOUT an `allowedFirmIds` attribute, and the ticket service admits every firm to such a row. This cell builds the BUILD half only (offline, no AWS call): the run is a later act under a pair.

**What to do.** Copy `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py` (read it first; it is short) to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py` and change it, keeping its structure, its stdin-only password rule and its never-print rule, as follows:

1. The email, the firm and the allowed firm list are PARAMETERS of `mint` and `remove`, never constants: `fwd5_mint.py mint --email <addr> --firm <firm> --allowed-firm-ids <id1,id2,...>` and `fwd5_mint.py remove --email <addr>`. The email must end in `@opal.invalid`; `--firm` and `--allowed-firm-ids` are required for mint; a missing or empty value answers `MINT-REFUSED args` and returns 1 before any AWS import. The email must NOT equal the FWD-1 helper's address (`fwd1-staff-r41b@opal.invalid`).
2. The item written is the FWD-1 item with `firmId` = the `--firm` value, the `email` and key from `--email`, and one more attribute `allowedFirmIds` holding the parsed ids as a DynamoDB string set (`{"SS": [...]}`); the older helper's `not any(... allowedFirmIds ...)` readback check is inverted: `READBACK-OK` requires `allowedFirmIds` to be present and equal to the ids given. Read how the ticket service reads that attribute at `infra/aws/lambda/ticket_center/lambda_function.py:419` (and the lines near it) and write the attribute in the shape the service reads; if the service reads another type than a string set, use that type and say so in your report.
3. `item_for`, the argument parser and the readback decision are plain functions that take the boto client as an argument (or return the item), so the tests need no AWS.
4. Never print or log the password or the hash. The default TTL stays (the row expires).

**Tests (file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/test_cross_firm_mint.py`):** offline tests that import `fwd5_mint` from its own folder (add the folder to `sys.path` inside the test file) and use a fake DynamoDB client object: the item carries the parameter firm and the ids as a set; two different emails give two different keys; an email not ending in `@opal.invalid`, an empty ids list, or the FWD-1 address is refused before any client call; the readback is BAD when `allowedFirmIds` is absent; the item holds no password in clear (it holds only a `$2b$12$` hash). Name EVERY test function `test_cross_firm_mint_<what>`. Run with `python -m pytest -q org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/test_cross_firm_mint.py`; `bcrypt` is needed for the hash test: if it is not installed, file a `BLOCKING` row and test the hash through an injected `hash_password` instead.

### ACCEPTANCE

<criterion id="AR56-ty-AC1" cell_refs="AR-ty-56"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 5 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/test_cross_firm_mint.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR56-ty-AC1` -- the test file exists, every test function is named `test_cross_firm_*` (yours: `test_cross_firm_mint_*`), the tests pass and at least 5 pass. Dry-run at box/dell2 39eef25c48: `R46-TESTS-FAIL absent: ...` -- FAIL as expected.

<expected_criteria>AR56-ty-AC1</expected_criteria>

## BOUNDS

- **Grant.** Your deliverables folder (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver` and this order's proof instance), the surprise channel. You edit no existing file; `fwd1_mint.py` stays as it is.
- **No network, no AWS call, no run.** You do not mint anything. Importing the module touches no AWS and no bcrypt at import time.
- **Refusal clause.** If `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py` is absent in your cone, file a `BLOCKING` row and stop.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/test_cross_firm_mint.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R46_TX.md</decomp_doc> (round 46, workstream ~TX), cell `AR-ty-56`.
<owned_cells>AR-ty-56</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR56-ty-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/IRPT_ANLREQ.TO-AR-ty-56.fwd5-second-firm-mint-helper.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR56-ty-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the two files, the count passed, the attribute type you wrote for `allowedFirmIds` and the line of the service that reads it, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- new files in a deliverables folder; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is made and no permission changes; the later run is a separate WORLD act.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage c39947a0a2: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates (the new test file(s) or record, and the proof instance). Traps named for the worker: a test that mocks the very guard it claims to prove; a lookup that misses before the firm binding is reached, which proves nothing about the binding; a test that passes with the guard removed; a cited line that is a comment instead of the code that decides.
</preflight>

- Cut on the CTO's Move 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`, msg 8742). The run (mint the principal on DEV, drive the refusals, remove it) is a later WORLD act through `0.7.0_AE_CloudOps~AQ2` under a pair, not this cell.
- Base: `AR56-ty-AC1` FAIL as expected at box/dell2 39eef25c48.
