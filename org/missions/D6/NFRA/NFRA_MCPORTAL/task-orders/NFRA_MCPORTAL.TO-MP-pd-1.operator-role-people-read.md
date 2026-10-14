# NFRA_MCPORTAL task order -- `MP-pd-1` -- WORKSTREAM PC ROUND 2: the People view read under the OPERATOR role against the grant store (R1, row Z-W24-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pd-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pd-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~25</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time read; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only: it ASSUMES the existing operator role (no IAM change) and does GetItem/Query/Scan on the grant store; the served modules are read over SSM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the equality is between two independently read lists (the store under the operator role, the served module under the host role), the MP-pc-6 method.
EGRESS CLASS, declared: AWS reads (sts assume-role on the operator role, DynamoDB read on the grant store, SSM send-command read-only probe); no write.
</preflight>

## 1. THE CELL -- `MP-pd-1` (workstream PC round 2, decomposition section PD.1)

Your worktree is `C:/tmp/mp-pd-25` (branch `wk-NFRA_MCPORTAL-pd-25`). Work and commit only there.

Background you need. The gateway serves `GET /api/admin/people`, the per-person view of what each person reaches through the
gateway. It is owner-gated and you hold no owner identity, so the page's logic is read from the SERVED module on the host: over
SSM on instance `i-07dccb1615503ac99`, from `/opt/opal-gateway` with the host's `.venv`, as `ec2-user`, beginning the probe with
`import app.server` (row Z-S48), calling `app.admin_people._compute()`. The previous close run (`MP-pc-6`) compared that module's
data-grant tools for one person with the grant store, but read the store under the HOST INSTANCE ROLE, so the page and the store
were read with one credential (row Z-W24-S2). This cell repeats the comparison with the store read under the OPERATOR role
`opal-gateway-access-admin` (ARN `arn:aws:iam::313476888478:role/opal-gateway-access-admin`), for EVERY principal the page lists
with a data grant, with the denominators printed. The pattern files are
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~24/pc6_probe.py` (the served probe), `.../pc6_run.json`
(its output shape) and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/_pc5_probe.py`.

1. **Assume the operator role.** Through the AWS shim `.tools/aws` (never a bare `aws`), run `sts assume-role` on the ARN
   above with a session name starting `mp-pd-1` and a duration of 900 seconds. Take the three temporary credential values into
   process environment variables of the commands that need them, and nowhere else: never print them, never write them to a
   file, a log or your report. Then run `sts get-caller-identity` with those variables set and keep the returned ARN ->
   `caller_arn` (it must contain `assumed-role/opal-gateway-access-admin/`). If the assume fails, STOP and file a BLOCKING row
   with the error text.
2. **The page side.** Over SSM, as above, in ONE probe run call `app.admin_people._compute()` and take, for every person row whose
   `how` contains "data grant revision", its `who` and the tool names in its channels that are data-grant tools (`schwab_*` and
   `blackdiamond_list_fees`) -> `page_tools` per principal. In the same run, call `app.admin_gateway_breakdown._scan_principals()`
   (read its signature first) to get each profiled principal's `tid` and `oid`, the keys the store is read by. Print the number of
   page rows with a data grant and the number of principals the scan returned.
3. **The store side, under the operator role.** The operator role is MEASURED DENIED `dynamodb:Scan` on the table (AccessDenied,
   issuer dry run, 18:1xZ), so you do not enumerate the table with it. The principal list comes from step 2. With the assumed
   credentials, read the grant store table `gateway-access-state-table` (region us-east-1) with Query by partition key
   `POLICY#<tid>#<oid>` (or GetItem on a known key; try Query first), for each principal from step 2: its `principal_profile`
   item and its ACTIVE `data_entitlement` item (the revision the profile's `grant_revision` names). Read
   `infra/aws/ec2/opal-gateway/app/access_state.py` and `app/data_entitlement.py` (`parse_scope`, `SCHWAB_TOOLS`) first to learn
   the item shape and the operation each tool needs. From each grant's `operations`, list the data-grant tools it admits, using the
   operation each tool needs in `SCHWAB_TOOLS` -> `store_tools`. A principal whose profile is not `active`, or that has no active
   grant, has an empty `store_tools` and is still listed. The operator read is GetItem and Query only: you write nothing, and you
   must not call `ops/schwab_entitlement_admin.py`'s `activate` or `revoke`. If the operator role is denied the read of a
   principal's partition, file a BLOCKING row with the principal key and the error, and list that principal with the reason; do
   not fall back to the host role for it.
4. **Pair and count.** Match the page rows to the store principals by the principal key (`who` is the email, or `<tid>/<oid>`,
   exactly as the page shows it; use the scan's email/key fields to match, and say how you matched). For every principal build
   `{"who", "store_tools", "page_tools"}`. A store principal with no page row, or a page row with no store principal, is NOT
   dropped: list it with the missing side as an empty list and name it in your report.
5. **Write the run file** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~25/pd1_run.json`:
   `{"caller_arn", "principals": <int>, "tools_compared": <int>, "per_principal": [{"who", "store_tools", "page_tools"}, ...],
   "page_rows_with_grant": <int>, "unmatched": [...], "ssm_command_id"}`, where `principals` is the length of `per_principal` and
   `tools_compared` is the sum of the lengths of the `store_tools` lists. Commit it (and your probe script and a stdout capture
   of the served probe), then run AC1.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway file, no store write, no grant write, no deploy, no role change.
2. The assumed credentials never leave the process environment of your commands. If any credential value, session token or
   access key id appears in a file you are about to commit, remove it first.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a).
   If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~25/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/**`, `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`, the pattern files
named in section 1, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W25-S<k>` (the next free k for W25). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd1.AC1.sh; echo "exit=$?"</invocation><expect>run=read operator_role:yes; every principal's store tools equal its page tools; denominators_match:yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~25/NFRA_MCPORTAL.TO-MP-pd-1.operator-role-people-read.proof_of_spec.json`.
Report once, with:
- the check output;
- the commit hash;
- `caller_arn`, the principal count, the tools-compared count, and each principal's `who` with its two lists;
- how you matched page rows to store principals, and every unmatched row;
- the SSM command id;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC round-2 issuance (decomposition v10) from `ledger/ROUND_ANALYSIS.pc-round1.md` ruling 1 (R1):
"The operator role reads `/api/admin/people` through the served route and compares it with the grant store for the same person,
for each data-grant tool, with the denominator printed." The route is owner-gated and no seat holds an owner identity, so "the
served route" is read as the served module's `_compute()` on the host, as in MP-pc-6; the operator role is the store reader.
That removes the one-credential limit of Z-W24-S2. Assuming the role was dry-run by the issuer at 18:0xZ (assumed-role ARN
returned; trust policy admits any principal of the account except `opal-gateway-role`). The operator role was MEASURED DENIED `dynamodb:Scan`
(issuer dry run at 18:1xZ, AccessDenied on the table), so the face reads the principal list from the served module's own scan
and reads each principal's partition by Query under the operator role. Whether Query on `POLICY#...` partitions succeeds for the
operator role is not yet measured here (its trust and LeadingKeys design say yes); if it is denied, the worker files a BLOCKING
row and the issuer rules. Check dry-run at base: AC1 FAIL (run file absent); green and red arms exercised with synthetic run
files.

<status>pending</status>
<round>2</round>
<workstream>PC</workstream>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
