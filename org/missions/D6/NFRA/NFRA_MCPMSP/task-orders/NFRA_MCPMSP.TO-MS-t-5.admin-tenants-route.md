# NFRA_MCPMSP task order -- `MS-t-5` -- ROUND 1, hop 3 caller: the owner-gated route that reaches `register_tenant`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-t-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~3</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a source change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reuses the gateway's existing lambda:InvokeFunction grant on the writer (MCPORTAL MP-t-3); no new grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the non-owner refusal test is the adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-t-5` (decomposition section 2)

Andrew approves a partner firm's tenant through the grant writer's new `register_tenant {tid, firm}` op (built by
`MS-w-1`, the previous order in your queue). The gateway's admin API already carries Andrew's approvals to the writer
for narrow/widen: `infra/aws/ec2/opal-gateway/app/admin_grants.py` -- the handlers sit behind the owner gate
(`app/owner_gate.py`), and `invoke_grant_writer(action, tid, oid, candidate, owner_header)` (`:137-160`) invokes the
function named by `GRANT_WRITER_FUNCTION_NAME` and relays its verdict; the gateway itself writes nothing.

Build, in a NEW module:
1. `app/admin_tenants.py`: `POST /tenants/{tid}` (mounted under `/api/admin`, so `POST /api/admin/tenants/{tid}`), body
   `{"firm": "<firm>"}`. Behind the SAME owner gate the grant handlers use (a non-owner is refused before any invoke,
   with the gate's own status). For the owner it invokes the writer with `action="register_tenant"`, the `tid`, the
   `firm` and the request's forwarded owner header, on `invoke_grant_writer`'s pattern (reuse its invoke/relay
   helpers by import where they fit; do not edit `admin_grants.py`), and relays the verdict. Export a `router` (or the
   same object shape `admin_grants.py` exports) so ONE registration line in `app/admin_api.py` mounts it -- **that
   line is the issuer's hookup at the merge; do NOT edit `admin_api.py`**. Name the exact line you need in your report.
2. `tests/test_admin_tenants.py` with at least: `test_non_owner_refused` (no invoke), `test_owner_forwards_register_tenant`
   (the fake invoke receives action, tid, firm and the owner header; the verdict is relayed),
   `test_gateway_writes_nothing` (a planted store that fails on any write is never touched). Mount your router on a
   test app yourself for the tests.

## 2. BOUNDS

1. Write surface: the two new files only. `admin_api.py`, `admin_grants.py`, `owner_gate.py`, `config.py` are read-only.
2. The approval VIEW (a mcportal page listing refused tenants) is FWD-4's enrichment, not this cell's.
3. No push, no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_tenants.py
infra/aws/ec2/opal-gateway/tests/test_admin_tenants.py
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~3/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/{admin_api,admin_grants,owner_gate,identity,config}.py`,
`infra/aws/ec2/opal-gateway/tests/test_admin_grants.py`, `infra/aws/ec2/opal-gateway/tests/test_admin_round2.py`,
`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`.

Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W3-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-t-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t5.AC1.sh; echo "exit=$?"</invocation><expect>pytest: N passed; test_non_owner_refused=1 test_owner_forwards_register_tenant=1 test_gateway_writes_nothing=1 (each >=1, 0 failed) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-t-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t5.AC2.sh; echo "exit=$?"</invocation><expect>admin suites: >=9 passed, 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~3/NFRA_MCPMSP.TO-MS-t-5.admin-tenants-route.proof_of_spec.json`.
Report once, with: the exact hookup line for `admin_api.py`; the two check lines; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985). Checks dry-run at base: AC1 FAIL as expected (test file absent);
AC2 PASS as expected (9 passed, the control). The hookup line in `app/admin_api.py` is the issuer's at the merge,
before MS-d-1's release.

<status>complete -- drained by 2.0.0_SA_COO~MS 2026-09-30 @47e80347c8: AC1 3/3 + AC2 9 passed on the issuer's re-run; instance VALID. The admin_api.py hookup (from . import admin_tenants; *admin_tenants.routes) moves to MS-d-1 (AMENDMENT 1): lane CLOUD_OPS_OR_ETL refuses this seat on infra/aws. Was: staged</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
