# NFRA_MCPMSP task order -- `MS-rq-1` -- ROUND 2, E3: the refusal list and one approval, owner-gated

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-rq-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~4</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reuses the gateway's existing invoke of the grant writer.
comp-adversary: DECLARED-NOT-APPLICABLE -- the non-owner test is the adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-rq-1` (decomposition v2, R2.2; PRD C4 -- the refusal log is the onboarding queue)

Build **`infra/aws/ec2/opal-gateway/app/admin_refusals.py` (new)**, behind `owner_gate.owner_only` exactly as
`app/admin_tenants.py` is (read it: it carries the owner's request to the grant-writer Lambda as `action=register_tenant
{tid, firm, owner_header}` via `admin_grants._lambda_client()` and relays the verdict; the gateway writes nothing):
1. `GET /api/admin/refusals` lists `asker_sender_refusal` audit entries (the host `audit.jsonl` via `app.audit`'s path,
   plus the audit lake under the env `AUDIT_S3_BUCKET` when set), newest first, each with the C4 fields only (ts, tid,
   oid, display_name, sender_email, sender_domain, chat_id, reason) -- never a text field; optional `limit`.
2. `POST /api/admin/refusals/approve` with `{tid, oid, firm, ...}`: when the tid has no tenant row
   (`app.tenant_registry`), invoke `register_tenant` first (reuse `admin_tenants.invoke_register_tenant`), then carry
   the advisor's `widen` to the writer through the same path `app/admin_grants.py` uses; relay each verdict; stop on
   the first REFUSED.
3. Export a module-level `routes` list (as `admin_tenants.routes`). **Do NOT edit `app/admin_api.py`** -- the mount is a
   hookup added at the release (MS-d-2 item 0).
4. **`tests/test_admin_refusals.py` (new)** with at least: `test_non_owner_refused`,
   `test_lists_refusals_newest_first_c4_fields`, `test_approve_unregistered_tenant_registers_then_widens`,
   `test_approve_registered_tenant_only_widens`, `test_gateway_writes_nothing` (fake Lambda client; the app built from
   `routes` in the test, as `tests/test_admin_tenants.py` does).

## 2. BOUNDS

1. Write surface: exactly the `<paths>` below. No push, no vendor call. REFUSE a criterion you cannot meet.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_refusals.py
infra/aws/ec2/opal-gateway/tests/test_admin_refusals.py
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/{admin_tenants,admin_grants,admin_api,owner_gate,audit,tenant_registry}.py`,
`infra/aws/ec2/opal-gateway/tests/`, `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`.
Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W4-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-rq-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e3g.AC1.sh; echo "exit=$?"</invocation><expect>pytest: N passed, 0 failed; each of the five named tests >=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-rq-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e3g.AC2.sh; echo "exit=$?"</invocation><expect>admin suites: >=12 passed, 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/NFRA_MCPMSP.TO-MS-rq-1.admin-refusal-routes.proof_of_spec.json`.
Report once, with: the hookup line MS-d-2 must add to `admin_api.py`; the two check lines; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance (E3). Checks dry-run at base: AC1 FAIL as expected (test absent); AC2 PASS as
expected (12 passed, control).

<status>complete</status>
<round>2</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
