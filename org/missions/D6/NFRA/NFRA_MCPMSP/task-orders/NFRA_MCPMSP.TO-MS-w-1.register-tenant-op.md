# NFRA_MCPMSP task order -- `MS-w-1` -- ROUND 1, hop 3: the grant writer's `register_tenant` op

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-w-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~3</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a source change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change: POLICY#TENANT#<tid> sits inside the writer's existing POLICY# LeadingKeys grant (precedent POLICY#EMAILDENY#<sha>).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the refusal tests are the adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-w-1` (decomposition section 2; NFRA_MCPORTAL PRD v0.4 C4 addendum)

NFRA_MCPORTAL's grant writer, `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`, is the ONE
writer of Opal's grant records. It verifies Andrew's ALB owner header itself (`_verify_owner_header`), then serves
`action` in `narrow|widen|revoke` (anything else is `BAD-ACTION`), and writes one record item per outcome to its own
changes table (`_record_item` / `_append_record`). The NFRA_MCPORTAL v0.4 C4 addendum (2026-09-30, CTO msg 26956)
grants THIS cell its paths for one op, verbatim:

> The writer gains one op, `register_tenant {tid, firm}`. It writes the `tenant_firm` record at `POLICY#TENANT#<tid>`,
> which sits inside the existing `POLICY#` LeadingKeys guard, so no IAM change is needed. [...] The op is
> owner-verified exactly as narrow and widen are. It is refused for a firm Andrew has not brought live (NFRA_MCPMSP
> C11), and it leaves one audit item in the writer's own record. This writer is the ONLY writer of that record; the
> gateway only reads it.

Build, in the writer only:
1. `action == "register_tenant"` with `tid` and `firm` from the event. AFTER the existing owner verification (unchanged)
   and BEFORE any store call, refuse:
   - `firm` not in `("inflection", "cottonwood")` -> `BAD-FIRM`;
   - `firm` not in the writer's `LIVE_FIRMS` config (env var, comma-separated; ABSENT or empty = no firm is live) ->
     `FIRM-NOT-LIVE`;
   - a `tid` that is not a GUID -> `BAD-TID`.
2. Otherwise write the `tenant_firm` record at partition `POLICY#TENANT#<tid>` through the store's conditional write
   (the record type is declared in `org/standards/NFRA_OPLGTW_CONTRACT.json`; read it and conform). Condition: the
   record is absent, OR it already names the SAME firm (idempotent, `WRITTEN` with `before == after`). A record
   naming ANOTHER firm refuses `TENANT-OTHER-FIRM` and writes nothing. The sort key follows
   `access_state.policy_key`'s convention for a single-record partition; state the exact pk/sk in your report (the
   gateway's reader, another cell this round, uses the same shape; the issuer reconciles them at the merge).
3. Every outcome, written or refused, leaves ONE item in the changes table, as narrow/widen do (`who` = claim name +
   email, never the owner-key value -- MCPORTAL ruling, already enforced in `_record_item`).
4. `tests/test_register_tenant.py` (new) with at least: `test_register_tenant_writes_tenant_firm`,
   `test_register_tenant_refused_firm_not_live` (store never called), `test_register_tenant_refused_other_firm_row`,
   `test_register_tenant_records_each_outcome`. Use the fakes the existing tests use
   (`tests/test_grant_writer.py`, `tests/test_owner_key_and_record.py`).

## 2. BOUNDS

1. Write surface: `lambda_function.py` and the new test file. Do NOT touch narrow/widen/revoke, the owner check, the
   Terraform, `build_package.py`, or any gateway file (`infra/aws/ec2/opal-gateway/**` is read-only here).
2. No deploy: the op goes live through `MS-a-2`, later in your queue.
3. No push, no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/test_register_tenant.py
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~3/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/`,
`infra/aws/ec2/opal-gateway/app/access_state.py`, `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`,
`org/standards/NFRA_OPLGTW_CONTRACT.json`, `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`.

Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W3-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-w-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/w1.AC1.sh; echo "exit=$?"</invocation><expect>pytest: N passed; test_register_tenant_writes_tenant_firm=1 test_register_tenant_refused_firm_not_live=1 test_register_tenant_refused_other_firm_row=1 test_register_tenant_records_each_outcome=1 (each >=1, 0 failed) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-w-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/w1.AC2.sh; echo "exit=$?"</invocation><expect>existing writer tests: >=12 passed, 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~3/NFRA_MCPMSP.TO-MS-w-1.register-tenant-op.proof_of_spec.json`.
Report once, with: the record's exact pk/sk and fields; the refusal codes; the two check lines; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985); paths granted by the NFRA_MCPORTAL v0.4 C4 addendum @c2f5d5a071
for this op alone. Sibling surface at the cut: MP-a-2 complete; MP-c-1 and MP-v-1 staged, deliverables-only. Checks
dry-run at base: AC1 FAIL as expected (test file absent); AC2 PASS as expected (12 passed, the control). Slot `~3`
continues to MS-t-5, then MS-a-2.

<status>complete</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
