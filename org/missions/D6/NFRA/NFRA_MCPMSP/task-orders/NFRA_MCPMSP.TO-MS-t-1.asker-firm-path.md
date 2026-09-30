# NFRA_MCPMSP task order -- `MS-t-1` -- ROUND 1, hop 1: the gateway's asker path learns partner firms

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~1</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for this cell -- it calls sts:AssumeRole through a config-supplied ARN; the role and the gateway's grant are MS-t-2/MS-a-1's, where the lens RUNs.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the never-uses-gateway-identity test is this cell's adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-t-1` (decomposition section 2)

The Opal gateway (`infra/aws/ec2/opal-gateway/`) answers a Teams asker's data question through the MCP tool
`opal_asker_query` (`app/asker_scope.py`). Today it serves only Opal's own tenant: `resolve_asker_class`
(`asker_scope.py:226-233`) returns `("opal-internal", "")` for Opal's tenant and `None` for every other tenant, and
`handle_asker_query` then refuses `asker_tenant_denied` (`:299-304`). There is no tenant-to-firm registry. The data
fetch runs through `query_v0._fetch_capped(key)` (`query_v0.py:94-101`), which reads `opal-data-portal-v2` with the
gateway's OWN instance credentials.

This project serves partner firms (Inflection first) from the same gateway. Build, in the gateway only:

1. **`app/tenant_registry.py` (new).** `firm_of(tid) -> Optional[str]` reads the `tenant_firm` record at partition
   `POLICY#TENANT#<tid>` in the gateway's access-state table, through the existing store (`app/access_state.py`: strong
   reads; an unreachable store raises `DependencyUnavailable`, never a default). Absent record -> `None`. The record
   is written ONLY by NFRA_MCPORTAL's grant writer (`register_tenant`, another cell this round); this module never
   writes. Define the key in ONE constant (`TENANT_PK_PREFIX = "POLICY#TENANT#"`) and the sort key per
   `access_state.policy_key`'s convention for a single-record partition; state both in your report (the writer cell
   uses the same shape, and the issuer reconciles them at the merge). The firm value is one of
   `graphql_plumbing/catalog_gate.KNOWN_FIRMS` (`"inflection"`, `"cottonwood"`); any other value is `Malformed`.
2. **`app/asker_scope.py`.** `resolve_asker_class(tid)` returns `("opal-internal", "")` for Opal's tenant (unchanged),
   `("firm", <firm>)` for a tenant `firm_of` resolves, and `None` for an unregistered one. On the `None` path the
   existing `asker_tenant_denied` refusal stays, and it now ALSO writes ONE refusal entry through `audit.log_call`
   under the tool name `"asker_sender_refusal"` with the fields `tid`, `oid`, `display_name`, `chat_id`, `reason`.
   **The message text is never stored** (PRD C4). The display name comes from the message's own `from.user`
   (extend `_ASKER_SELECT`/`resolve_asker_message` only as far as that needs; the sender is still read from the
   message itself, never from an argument). A store failure in `firm_of` is `asker_store_unavailable`, not a tenant
   refusal. The group-chat branch (`:339-370`) uses the same `resolve_asker_class`; keep its behaviour (a member
   outside Opal's tenant AND not registered is refused).
3. **The firm fetch.** For a `("firm", <firm>)` asker the catalog verdict is computed exactly as today
   (`catalog_gate.gate(catalog, key, "firm", firm)` AND the calling identity's gate), and the fetch then goes through
   `app/firm_role.py` (new): `fetch_capped(firm, key) -> (bytes, int)` assumes the role ARN in
   `config.FIRM_ROLE_ARNS[firm]` with `sts:AssumeRole` (session name carrying the run's asker oid), caches the
   credentials until shortly before expiry, reads `opal-data-portal-v2/<key>` with THOSE credentials, and enforces
   the same byte cap as `query_v0._fetch_capped` (raise the same `_OverCap`). **A firm asker's fetch never falls back
   to the gateway identity's own S3 client**, for any reason: a missing ARN, an AssumeRole failure or a read
   AccessDenied is a refusal (`asker_firm_role_unavailable` / `asker_fetch_failed`), never a retry on another
   identity. (PRD v0.3 names this as the residual only the router closes: the gateway identity can still read
   `opal-data-portal-v2`, so the router must never send a partner request through it.) Opal-internal askers keep the
   existing `query_v0._fetch_capped` path, unchanged.
4. **`app/config.py`.** `FIRM_ROLE_ARNS`: a JSON object firm -> role ARN from the environment variable of the same
   name; default EMPTY (every firm refused until the deploy sets it).
5. **`app/audit.py`.** `_ARGS_ALLOWLIST` gains `"bytes"` on `"opal_asker_query"` (today `asker_oid`, `key`,
   `verdict`; this closes row NFRA_OPALAI-Z-W2-S2), and a new entry `"asker_sender_refusal"` with `tid`, `oid`,
   `display_name`, `chat_id`, `reason`. No text/message/body field anywhere.
6. **`tests/test_mcpmsp_asker_firm.py` (new)** with at least these five named tests, using fakes for the store, Graph,
   STS and S3 in the style of `tests/test_asker_scope.py`:
   `test_registered_tenant_is_firm_principal`, `test_unregistered_tenant_refused_and_logged` (exactly one
   `asker_sender_refusal` entry, no text field), `test_firm_fetch_assumes_firm_role` (the assumed ARN is
   `FIRM_ROLE_ARNS[firm]`), `test_missing_role_arn_refuses`, `test_firm_fetch_never_uses_gateway_identity` (plant a
   gateway S3 client that fails the test if called; drive a firm asker through AssumeRole failure AND through read
   AccessDenied; both refuse and the planted client is never touched).

**AMENDMENT 1 (issuer, 2026-09-30, on your row NFRA_MCPMSP-Z-W1-S1).** The CTO's N1 ruling (msg 26956, @c2f5d5a071)
added the `tenant_firm` record type to NFRA_OPLGTW's contract `org/standards/NFRA_OPLGTW_CONTRACT.json`, but the
adapter was not changed: `app/access_state.py:64` `POLICY_RECORD_TYPES` still lacks it, so `_as_key`/`_decode` refuse
the key (your AC2 failure), the writer's `register_tenant` put would be refused live, and the adapter's own
`tests/test_access_state.py::test_ogd1_ac03` (contract types == `RECORD_TYPES`) has been RED at CLOUD since that
commit. You are now granted `app/access_state.py` for exactly this:
7. Add `"tenant_firm"` to `POLICY_RECORD_TYPES`, and make any key-shape check the adapter applies admit the tenant
   partition `POLICY#TENANT#<tid>` with sk `tenant_firm` (the `email_deny` precedent, `EMAIL_DENY_RECORD_TYPE`, is the
   model). `operator_transact` already requires one `operator_audit` put in one partition; a `register_tenant`
   transaction is `tenant_firm` put + `operator_audit` put, both in `POLICY#TENANT#<tid>` -- confirm the adapter
   admits exactly that and still refuses a tenant partition carrying a principal record type. Change nothing else.
8. Add to `tests/test_mcpmsp_asker_firm.py` the named test `test_tenant_firm_admitted_by_adapter`: the adapter decodes
   a `tenant_firm` item at `POLICY#TENANT#<tid>`, and `operator_transact` admits the two-item tenant transaction
   (fake client) and refuses a tenant partition with a `principal_profile` put.
`app/access_state.py` is NFRA_OPLGTW's module; no non-terminal order of any project writes it at this amendment
(measured). Keep your earlier commits; add this as a new commit on your branch.

## 2. BOUNDS

1. Write surface: exactly the `<paths>` below. No Terraform, no deploy, no `.env`, no other gateway module.
   `app/admin_api.py`, `app/data_entitlement.py`, `app/query_v0.py`, `catalog_gate.py` and `app/context.py` are
   read-only (other projects' files); `app/access_state.py` only as AMENDMENT 1 names.
2. Round-1 scope: a registered tenant's asker is served under its firm role; an unregistered tenant is refused and
   logged. The domain half of the sender gate (FWD-3) is NOT this cell's.
3. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tenant_registry.py
infra/aws/ec2/opal-gateway/app/firm_role.py
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/app/access_state.py
infra/aws/ec2/opal-gateway/tests/test_mcpmsp_asker_firm.py
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/{access_state,data_entitlement,query_v0,context,graph,identity_scope}.py`,
`infra/aws/ec2/opal-gateway/app/graphql_plumbing/catalog_gate.py`, `infra/aws/ec2/opal-gateway/tests/test_asker_*.py`,
`org/standards/NFRA_OPLGTW_CONTRACT.json` (the `tenant_firm` record type),
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W1-S<k>` (next free k for W1), `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t1.AC1.sh; echo "exit=$?"</invocation><expect>pytest: N passed; test_registered_tenant_is_firm_principal=1 test_unregistered_tenant_refused_and_logged=1 test_firm_fetch_assumes_firm_role=1 test_missing_role_arn_refuses=1 test_firm_fetch_never_uses_gateway_identity=1 test_tenant_firm_admitted_by_adapter=1 (each >=1, 0 failed) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t1.AC2.sh; echo "exit=$?"</invocation><expect>asker + adapter suites: >=41 passed, 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t1.AC3.sh; echo "exit=$?"</invocation><expect>opal_asker_query includes asker_oid,bytes,key,verdict; asker_sender_refusal includes chat_id,display_name,oid,reason,tid; text_fields=[] verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/NFRA_MCPMSP.TO-MS-t-1.asker-firm-path.proof_of_spec.json`.
Report once, with: the tenant record's exact pk and sk shape; the refusal codes you added; the three check lines; the
commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the round-1 issuance on Andrew's "go ahead and dispatch round 1" (CTO msg 26985, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_06xxZ_NFRA_MCPMSP_DISPATCH_ROUND_1.md`). Checks
dry-run at base: AC1 FAIL as expected (test file absent); AC2 PASS as expected (23 passed, the control); AC3 FAIL as
expected (`bytes` and the refusal entry absent). Measured at the cut: the gateway role already reads `implicitDeny` on
`opal-data-inf` and `opal-data-cot` (A1n arm 3 holds today). Slot `~1` continues to MS-d-1 at the join. Fourth
behaviour asserted inside AC1 (never-uses-gateway-identity) is the PRD v0.3 residual's router control, not a
fourth criterion.

**AMENDMENT 1 (issuer):** on row Z-W1-S1 (the worker's AC2 FAIL, 22/23, cause measured). Grants `app/access_state.py`
for the `tenant_firm` record type the CTO's N1 ruling put in the OPLGTW contract; AC1 gains
`test_tenant_firm_admitted_by_adapter`; AC2's control widens to the adapter's own suites (`test_access_state.py`,
`test_email_deny.py`). Re-run at base after the amendment: AC1 FAIL as expected; AC2 FAIL as expected (1 failed,
40 passed: `test_ogd1_ac03`, red since @c2f5d5a071 -- the same contract-vs-adapter gap, which this change closes).
Graded by: no gate limb grades a modification's criteria (to-pipeline-gate GATE (viii) grades a modified order only
for `<placeholders>`, which stay NONE).

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
