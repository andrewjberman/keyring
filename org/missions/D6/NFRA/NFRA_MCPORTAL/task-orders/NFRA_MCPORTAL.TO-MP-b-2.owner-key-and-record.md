# NFRA_MCPORTAL task order -- `MP-b-2` -- ROUND 2, R-2 + R-4: the writer's owner key and the writer's own record

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-b-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a build cell; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE at this cell -- the two new grants are written, not applied; MP-a-1 applies them.
comp-adversary: DECLARED-NOT-APPLICABLE -- enrichment round of a thread.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MP-b-2` (round 2, decomposition section R2.1)

The grant writer `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py` verifies Andrew as the
caller from the ALB-signed `x-amzn-oidc-data` header. Today it keys on the header's `oid` claim, with freshness on
`iat` (`_verify_owner_header`). Microsoft's userinfo response, which the ALB signs into that header, may carry neither
claim. The PRD owner has ruled both branches now (ROUND_ANALYSIS.round1.md R-2), and a later measurement picks the one
that holds. Build both, selected by configuration:
1. **The owner key.**
   - Config `MCPORTAL_OWNER_KEY_CLAIM` is `oid` or `sub`, and `MCPORTAL_OWNER_KEY` is the value. An unset or other
     claim refuses every write (`OWNER-CONFIG-MISSING`).
   - A verified header is the owner when its value for THAT claim matches the config, case-insensitive.
   - A verified header carrying neither `oid` nor `sub` refuses (`HEADER-UNVERIFIED`). No owner key is invented.
2. **Freshness.** When the header carries `iat`, keep today's window (`HEADER_MAX_AGE_SECONDS`). When it has no `iat`,
   the bound is the ALB-signed `exp`: an expired header refuses (`HEADER-STALE`).
3. **The writer's own record** (R-4). Every WRITTEN or REFUSED outcome appends exactly ONE item to the table
   `mcportal-grant-changes-table`, named by `lib/opal_naming.py name('mcportal', None, 'grant-changes', 'table')`, from
   env `MCPORTAL_CHANGES_TABLE`. The item holds who, when, action, tid, oid, verdict, reason, and before/after where a
   write happened.
   - It is written with PutItem ONLY.
   - A record write that fails never changes the verdict the caller gets. The failure is printed with the outcome.
   - Refusals before any config is read still record, when the table is configured.
4. **Terraform, in `mcportal_grant_writer.tf`** (written, NOT applied):
   - the table (on-demand; hash key and sort key your choice, stated);
   - the writer role's statement `Sid = "McportalGrantChangesPutOnly"`, with Action exactly `["dynamodb:PutItem"]` on it;
   - the gateway role's statement `Sid = "GatewayReadsMcportalGrantChanges"`, read actions only (a subset of GetItem,
     Query, Scan) on it;
   - env `MCPORTAL_OWNER_KEY_CLAIM` / `MCPORTAL_OWNER_KEY` (from variables, no defaults) replacing
     `MCPORTAL_OWNER_OID`;
   - env `MCPORTAL_CHANGES_TABLE`.
5. **`tests/test_owner_key_and_record.py`** (new), with an injected test key and clock (never the network), naming
   exactly:
   - `test_owner_key_oid_branch`
   - `test_owner_key_sub_branch`
   - `test_iat_absent_uses_exp`
   - `test_no_owner_claim_refuses`
   - `test_each_outcome_appends_one_record`
   - `test_record_write_is_put_only` (a trapped UpdateItem/DeleteItem/BatchWriteItem fails it)

## 2. BOUNDS

1. The staged build (MP-b-1, merged on this branch) stays green: `build_package.py` and its in-zip refusal still work.
2. The four refusal reasons keep their names; the existing `tests/test_grant_writer.py` stays green.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/test_owner_key_and_record.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/test_grant_writer.py
infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `lib/opal_naming.py`, `infra/aws/ec2/opal-gateway/app/access_state.py`,
`infra/aws/terraform/opal-gateway/schwab_access_state.tf` (the gateway role's name, `aws_iam_role.gw`).

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_MCPORTAL-Z-W1-S<k>` (next free k for W1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-b-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/b2.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-b-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/b2.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 2 of 2; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-b-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/b2.AC3.sh; echo "exit=$?"</invocation><expect>changes table declared=yes; writer statement PutItem only=yes; gateway statement read-only=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/NFRA_MCPORTAL.TO-MP-b-2.owner-key-and-record.proof_of_spec.json`.
Report once:
- what you changed and where, and the commit hash;
- the table's keys;
- the new variables MP-a-1 must supply;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** R-2 (both branches, configured) and R-4 (the writer's own record, writer side and grants).
Chain A, after MP-b-1 on the same slot.

<status>pending</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
