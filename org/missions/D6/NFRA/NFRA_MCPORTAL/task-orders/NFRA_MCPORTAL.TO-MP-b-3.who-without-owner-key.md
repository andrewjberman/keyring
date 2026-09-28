# NFRA_MCPORTAL task order -- `MP-b-3` -- ROUND 3: the writer's record never carries the owner-key value (row Z-S10)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-b-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~1</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a source change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the writer's POLICY#* grant already covers every record type.
comp-adversary: DECLARED-NOT-APPLICABLE -- the new test is the adversary read (it plants the configured value and looks for it).
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MP-b-3` (round 3, decomposition section R3.2)

The grant writer is `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`. Every outcome writes
one record item to its changes table (`_record_item`, around `:185-201`). After the owner check passes, `:266` sets
`ctx["who"] = "%s:%s%s" % (owner.claim, owner.key, ...)`, so a WRITTEN item's `who` field carries the **owner-key
value** (Andrew's `sub` or `oid`). The PRD owner has RULED (1.0.0_SA_CTO~O, 2026-09-28 ~20:57Z): *"`who` on a WRITTEN
item carries the claim NAME and the email only, for example "sub <email>". The owner-key VALUE never reaches
mcportal-grant-changes-table, the history, a log or a committed file."*

Build, in the writer only:
1. `who` becomes `"<claim name> <email>"` (the claim name alone when there is no email). Search the file for any other
   place `owner.key` (or the configured `MCPORTAL_OWNER_KEY` / `owner_key` / `owner_oid` value) reaches an outcome, a
   record field, `detail`, or a `print`/log, and remove it there too. Name each place you found in your report.
2. A test `test_written_item_never_carries_owner_key`, **parametrized over both branches (`oid` and `sub`)**, in
   `tests/test_owner_key_and_record.py`. Drive a WRITTEN outcome with a fake store and a fake changes client, as the
   file's existing tests do, then assert that the configured owner-key value appears in NO field of the recorded item
   (serialise the whole item and search it), and that `who` equals `"<claim> <email>"`.
3. **The stale expectation.** `tests/test_grant_writer.py::test_owner_write_lands_with_operator_audit` FAILS at HEAD
   before your change: at `:141` it expects the record types `["data_entitlement", "operator_audit",
   "principal_profile"]`, but `admin.activate` now also puts an `email_deny` record. That came from another project's
   change @3e936f77bd: `infra/aws/ec2/opal-gateway/app/access_state.py:64`, `POLICY_RECORD_TYPES`, and `:447-469`,
   `operator_transact` allowing "the principal's partition plus at most email_deny puts". Read `access_state.py` and
   `ops/schwab_entitlement_admin.py` at HEAD, then bring the expectation to the record set a narrow actually writes.
   **Do not change `access_state.py` or `schwab_entitlement_admin.py`**, which belong to another project. If the new set
   looks WRONG for a narrow (for example, a deny record written for a principal the narrow does not deny), file a
   BLOCKING row with the measurement instead of adjusting the test to it.

## 2. BOUNDS

1. Write surface: the writer's `lambda_function.py` and its `tests/`. No Terraform, no gateway file, no deploy. This
   change goes live through the next cell's apply.
2. Standing: no push and no vendor call. REFUSE a criterion you cannot meet as written, with its measurement. Never
   repair a criterion.

## 3. SURFACES

<paths>
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/access_state.py`,
`infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`,
`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W1-S<k>` (the next free k for W1).

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-b-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/b3.AC1.sh; echo "exit=$?"</invocation><expect>writer tests: 0 failed; test_written_item_never_carries_owner_key PASSED cases>=2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-b-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/b1.AC2.sh; echo "exit=$?"</invocation><expect>build rc=0; in-package lambda_handler (Lambda depth) with no owner header -> verdict=REFUSED NO-OWNER-HEADER -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/NFRA_MCPORTAL.TO-MP-b-3.who-without-owner-key.proof_of_spec.json`.
Report once, with:
- every place the value reached, and what you changed there;
- the record set a narrow writes now;
- the pytest line;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the round-3 issuance, on the CTO's ruling of Z-S10 (msg 26207, "Cut it ahead of MP-c-1").
It also carries row Z-S12: the writer test that was stale from NFRA_OPLGTW OG-e-1. Checks dry-run at base: AC1 FAILS
as expected ("1 failed, 9 passed", 0 cases of the named test); AC2 PASSES as expected (the bound, the in-zip refusal).
The writer's grant (`mcportal_grant_writer.tf:87-91`, PutItem/UpdateItem on `POLICY#*` leading keys) already covers
`POLICY#EMAILDENY#...`. No gate. Slot `~1` continues to MP-a-2 after this drains.

<status>pending</status>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
