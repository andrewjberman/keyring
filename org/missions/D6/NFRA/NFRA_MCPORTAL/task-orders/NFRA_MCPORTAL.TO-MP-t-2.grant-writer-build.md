# NFRA_MCPORTAL task order -- `MP-t-2` -- HOP 3 (build): the separate grant writer that verifies Andrew itself

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-t-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: RUN by the apply cell (MP-t-3) on the APPLIED plane; this order writes the Terraform and applies nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: NONE. No terraform init, plan or apply; no AWS call.
</preflight>

## 1. THE CELL -- `MP-t-2` (round 1, decomposition s.2/s.3)

PRD C4: the gateway must never be able to grant itself access. Today the grant store's `POLICY#<tid>#<oid>` partition
is writable only by the operator role (`opal-gateway-access-admin`). Its trust condition `ArnNotEquals
aws:PrincipalArn = <gateway role>` (`infra/aws/terraform/opal-gateway/schwab_access_state.tf:125-133`) keeps the gateway
out, and the runtime write guard in `infra/aws/ec2/opal-gateway/app/access_state.py:14-16` refuses runtime writes to
`POLICY#`. Both STAND. The dashboard's grant writes go through a NEW, separate function. Build it, carrying the existing
operator path and building no second one:
1. **The name, from the builder (Rule 30).** `lib/opal_naming.py` `name('mcportal', None, 'grant-writer', 'lambda')`
   refuses today ("system 'mcportal' is not a systems.json key"). Add the `mcportal` row to
   `infra/logic/registry/systems.json`, following that file's existing row grammar (`key`, `class` `PRODUCT`, `long`,
   `long_basis`, `owner_directive` `D6`, `owner_claim`, `owner_basis` citing
   `org/missions/D6/NFRA/NFRA_MCPORTAL/project.json`). Then use `name()`'s output VERBATIM everywhere; never type the
   name. A further refusal is a missing row to add, or a BLOCKING row.
2. **The source**, under `infra/aws/lambda/`, with its entry in `infra/aws/lambda/ci/lambda-source-map.json` keyed by
   that name (`source_dir`, `tf_file`, `tf_resource`, `iam_role`, per the map's existing entries). The handler:
   - takes `{"action": "narrow"|"widen"|"revoke", "tid", "oid", "candidate", "owner_header"}` and answers
     `{"verdict": "WRITTEN"|"REFUSED", "reason": ...}`;
   - verifies `owner_header` (the ALB-signed `x-amzn-oidc-data` the gateway forwards) ITSELF: ES256 against the regional
     ELB public key (the same verification as `app/identity.py:50-62`, reimplemented in the writer, which never imports
     from or asks the gateway);
   - exact-matches the identity against its OWN owner config (Andrew's Entra object id, from the writer's own
     environment, never from the gateway), and refuses a header older than a short window (state it; e.g. 120 s);
   - reasons: `NO-OWNER-HEADER`, `HEADER-UNVERIFIED`, `NOT-OWNER`, `HEADER-STALE`. Every refusal happens BEFORE any
     store call;
   - on success it runs the operator path's own functions (`infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`
     `prepare` / `activate` / `revoke`), so the grant revision and its `operator_audit` land in ONE transaction, with
     the optimistic revision check. A revoke is a tombstone, never a delete;
   - every write AND every refusal leaves the writer's own audit record, which the gateway role cannot write.
   `ops/schwab_entitlement_admin.py` stays byte-unchanged and working; package what you need from it.
3. **Tests** in `<source_dir>/tests/test_grant_writer.py`, with a fake store that records calls and a TEST signing key
   injected for the header (never the network), naming exactly: `test_refused_without_owner_header`,
   `test_refused_for_non_owner`, `test_refused_for_stale_header` (each asserting ZERO store calls), and
   `test_owner_write_lands_with_operator_audit`.
4. **Terraform**, `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`:
   - the function named by the builder;
   - its execution role, allowed to write the `POLICY#` partition the way `opal-gateway-access-admin` is (read that
     role in `schwab_access_state.tf` and mirror its data-plane statement), plus its own audit writes and logs;
   - ONE `lambda:InvokeFunction` grant for the gateway role (`opal-gateway-role`) on this function only;
   - NO `sts:AssumeRole` for the gateway role anywhere, and no change to the operator role or its trust policy;
   - `terraform fmt` clean. Andrew's owner oid is a Terraform variable with NO default. The apply cell supplies it.

## 2. BOUNDS

1. **Nothing is applied, planned or initialised.** `MP-t-3` applies it.
2. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/logic/registry/systems.json
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/mcportal/
infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

The source goes under `infra/aws/lambda/mcportal/<the builder name>/`, the directory prefix granted above.

Read (never write): `lib/opal_naming.py`, `infra/logic/registry/` (every file), `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`,
`infra/aws/ec2/opal-gateway/app/access_state.py`, `.../app/data_entitlement.py`, `.../app/identity.py`,
`infra/aws/terraform/opal-gateway/schwab_access_state.tf`.

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W3-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-t-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t2.AC1.sh; echo "exit=$?"</invocation><expect>name() returns a name; source-map entries=1 whose key equals it; source_dir exists=yes; tf_file exists=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-t-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t2.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-t-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t2.AC3.sh; echo "exit=$?"</invocation><expect>fmt rc=0; builder name literal occurrences>=1; lambda:InvokeFunction>=1; sts:AssumeRole outside a Lambda trust policy=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/NFRA_MCPORTAL.TO-MP-t-2.grant-writer-build.proof_of_spec.json`. Report once: the builder name, what you changed and where, the commit hash, the header window you chose, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** S4 build. WORLD by floor (infra/ + terraform). The next order in this slot's queue is MP-t-3 (the
apply), provisioned off the post-merge HEAD.

<status>complete</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
