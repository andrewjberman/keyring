# NFRA_OPALAI task order -- `OA-f-1` -- ADDENDUM A1 (Z-S18, Andrew's option 2): identity_scope keys on (identity, OAuth client_id)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~8</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface; one read-only DynamoDB scan to measure a client_id.
comp-adversary: DECLARED-NOT-APPLICABLE -- the change NARROWS a grant; it widens nothing.
EGRESS CLASS, declared: Opal's own AWS, read only.
</preflight>

## 1. THE CELL -- `OA-f-1` (decomposition ADDENDUM A1)

**The defect (row `NFRA_OPALAI-Z-S18`):** `infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt:13` grants
`opal_data_refresh_upload` to `opalbloomberg@opalinvest.com` for ANY OAuth client. So every session signed in as that
identity can fire the production upload, including the Analyst seat, which should not. Andrew ruled the fix (option 2,
CTO msg 25935): identity_scope keys on (identity, OAuth client_id), and the upload goes to the operator's registered
client only.

**What exists, read it first:**
- `app/identity_scope.py`:
  - `_SEED` is the code seed;
  - `_load_scopes()` parses overlay lines `'<email> <tool>'`;
  - `check(email, tool)` returns None or a denial string.
- `app/oauth_as.py:255-278`: the verified access token already CARRIES `client_id`; `validate_access_token` returns the
  claims.
- `app/server.py:~160-173`: the middleware calls `_bearer_principal(request)` and then `set_current_principal(...)`.
- `app/context.py:79-104`: holds the request contextvars, and has no client_id today.
- The two chokepoints that call `check`:
  - `app/tools.py:~134-139` (`_run`);
  - `app/integrations/base.py:~139-146` (`run_integration_tool`).
  - `app/asker_scope.py:120` also calls it.

Do:
1. **Carry the verified client_id to the check.** Add a request contextvar for the client_id, set ONLY from the
   validated token's `client_id` claim in the same place the principal is set, and never from a header, body or
   argument. `check()` takes it from there (or as an argument the two chokepoints pass). If no client_id is present, a
   client-qualified row does NOT admit.
2. **Grammar:** an overlay line may carry an optional third token `client=<id>`:
   - a qualified row admits that tool only when the request's client_id equals `<id>`;
   - an unqualified row behaves exactly as today;
   - the seed is untouched.
3. **The tracked row** at `identity_tool_allowlist.txt:13` becomes `opalbloomberg@opalinvest.com opal_data_refresh_upload
   client=<id>`, with a comment citing Andrew's option 2 (CTO msg 25935) and keeping the existing authorization comment.
   `<id>` is the operator's registered client, MEASURED:
   - do a read-only scan of `gateway-access-state-table` for `record_type = oauth_refresh_family` rows with
     `status = active` and `email = opalbloomberg@opalinvest.com`;
   - at this order's cut there was exactly ONE live such family, one client;
   - if you find more than one client, STOP and file a BLOCKING row naming the count.
   - Print that client_id into your report and the row only. It is a registration id, not a claim value.
4. **Tests** in `tests/test_identity_scope.py`:
   - `test_upload_admitted_only_for_operator_client`: a fixture overlay with a qualified row admits its client;
   - `test_upload_refused_for_other_client_same_identity`: the same identity on another client_id, and on no
     client_id, is refused;
   - `test_scoped_deny_by_default`: repoint it to a FIXTURE overlay (`tmp_path`), never the live tracked file.
   - Keep `tests/test_data_entitlement_guard.py` (OGZ1-AC11 reads the tracked overlay) passing.

## 2. BOUNDS

1. Only the files in `<paths>`. There is no deploy (that is `OA-f-2`), no push and no vendor call.
2. No other tool or identity changes its admission. The change is a NARROWING of one row.
3. Standing rule: REFUSE a criterion you cannot meet as written, and report the refusal with its measurement. Never
   repair, widen or route around a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/identity_scope.py
infra/aws/ec2/opal-gateway/app/context.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/integrations/base.py
infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt
infra/aws/ec2/opal-gateway/tests/test_identity_scope.py
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~8/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W8-S<k>`.
The gateway suite appends to the tracked `infra/aws/ec2/opal-gateway/audit.jsonl`. Restore it (`git checkout --` it)
before every commit.

## 4. PROOF OF SPEC (literal; run from your worktree root after your last commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/f1.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/f1.AC2.sh; echo "exit=$?"</invocation><expect>unqualified upload rows=0; client-qualified=1; live match=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~8/NFRA_OPALAI.TO-OA-f-1.identity-scope-client-key.proof_of_spec.json`.
Report once, with:
- the measured client_id and the family count;
- the commit hashes;
- the full `tests/test_identity_scope.py` and `tests/test_data_entitlement_guard.py` results;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act on Andrew's option 2 (CTO msg 25935), ahead of round 2. Measured at the cut: 1 live
opalbloomberg@ refresh family, 1 client (so today the Analyst seat and the operator share it). This closes the grant's
SHAPE; TODAY's reach closes at the cutover or with a fence change (decomposition ADDENDUM A1). Checks were dry-run at
base: f1.AC1 FAIL (0 of 3), f1.AC2 FAIL (unqualified=1, match=no).

<status>complete</status>
<direct_act>true</direct_act>
<slot>~8</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
