# TO-AR-tz-69 -- FWD-5 mint helper: read back the scope and the entitlement rows (AR-tz-69, round 59, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-69</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~271</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>59</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-69` (`decompositions/IRPT_ANLREQ_DECOMP_R59_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (the mint helper and its tests are merged)

---

## WORKER FACE

### THE CELL

`AR-tz-69`: "the second-firm mint reads back its scope and its entitlement rows." The helper `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py` (merged, AR-ty-56) writes ONE row of the users table (`opal-users-v2`, key `PK = USER#<email>`, `SK = PROFILE`) with `allowedFirmIds` as a list of strings, and its read-back prints only `MINT-OK READBACK-OK` or `MINT-OK READBACK-BAD <word>`. The CTO's ruling (msg 9670, 2026-10-16): a synthetic user minted after the ticket-service release carries `allowedFirmIds` = [the ONE firm the run files under], never a global marker, and the mint's read-back PRINTS the scope and the entitlement rows. An "entitlement row" is any OTHER item under the same `PK` (an item whose `SK` is not `PROFILE`); a fresh synthetic principal must have none.

**What to do (in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py`, `cmd_mint`, after the existing consistent `get_item`).**
1. Query the table for the principal's partition: `ddb.query(TableName=TABLE, KeyConditionExpression="PK = :p", ExpressionAttributeValues={":p": {"S": "USER#" + email}}, ConsistentRead=True, ProjectionExpression="SK")`. Count the returned items whose `SK` is not `PROFILE`; the response may carry no `Items` key (the test fake returns only a `Count`), which counts as zero rows. Name the function `entitlement_rows(resp)`.
2. When the existing read-back is OK AND the entitlement rows are zero, print the existing line `MINT-OK READBACK-OK` and then ONE more line `MINT-SCOPE allowedFirmIds=<ids joined by comma> entitlement_rows=0`, and return 0. When the read-back is OK and the rows are not zero, print `MINT-OK READBACK-BAD entitlement` plus the line `MINT-SCOPE allowedFirmIds=<ids> entitlement_rows=<n>` and return 1. When the query raises, print `MINT-OK READBACK-BAD query <ExceptionTypeName>` and return 1. The existing `READBACK-BAD shape` path is unchanged and prints no scope line. The ids are firm identifiers, not secrets; the password, its hash, an address and a token are still never printed.
3. Keep every existing test green; the fake's `query` stays as is for the remove path (do not change `cmd_remove`). Add tests named `test_scope_<what>`: the scope line on a green mint; entitlement rows non-zero refused with rc 1 and the BAD word; a query error refused; an `Items` list holding only the `PROFILE` row counts as zero; two ids print comma-joined; the password and hash never appear in the output. At least 20 tests in the file pass in total (it had 15 before this cell, so the base reads FAIL).

Standard library and pytest only. No AWS, no network, no secret, no mint, no run. Use plain names.

### ACCEPTANCE

<criterion id="AR69-tz-AC1" cell_refs="AR-tz-69"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 20 --prefix=test_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/test_cross_firm_mint.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR69-tz-AC1` -- the tests pass and at least 20 pass. Dry-run at box/dell2 5d59abbb3d (`5d59abbb3d`): `R46-TESTS-FAIL only 15 test functions defined, need 20` -- FAIL as expected.

<expected_criteria>AR69-tz-AC1</expected_criteria>

## BOUNDS

- **Grant.** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/test_cross_firm_mint.py` only (plus this order's file, your deliverables folder, the surprise channel). Nothing else; `cmd_remove` and the driver are not touched.
- **No AWS, no network, no run, no mint, no deploy.** The password handling is unchanged.
- **Refusal clause.** If the file at your base already prints a scope line, say so in a surprise row and make no edit to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py`; still add the tests.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/test_cross_firm_mint.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R59_TX.md</decomp_doc> (round 59, workstream ~TX), cell `AR-tz-69`.
<owned_cells>AR-tz-69</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR69-tz-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~271/IRPT_ANLREQ.TO-AR-tz-69.mint-scope-readback.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR69-tz-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the diff size of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py` (lines added and removed), the count passed, the printed lines for the green, the entitlement and the query-error cases (ids only), the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a print line and a read-only query added to a helper nobody has run; no edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call in this cell; the query reaches only the helper's own users-table partition when the applier later runs it under its own pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: counting the PROFILE row itself as an entitlement row (the real partition always holds it); a query that sets Select COUNT and so cannot tell the PROFILE row from the others; printing the password, its hash or an address; changing the fake's query in a way that breaks the remove tests; treating a missing Items key as an error.
</preflight>

- Cut on the CTO's ruling msg 9670 (relayed by `2.0.0_SA_COO~V2` msg 9673): the FWD-5 live run's pair (draft `R58_FWD5_LIVE_EXERCISE_PACKET_DRAFT_20261016.md`) cannot be signed until the helper prints scope and entitlement rows. Risk LOCAL: a helper file and its tests in a deliverables folder, nothing run.
- Base: `AR69-tz-AC1` FAIL as expected at box/dell2 5d59abbb3d.
