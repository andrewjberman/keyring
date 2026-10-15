# NFRA_OPLGTW task order -- `OG-gt-13` -- the published-analysis tool invokes its Lambda through the internal reader role (no new instance-role reach)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-13</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-13</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~96</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests only; nothing is deployed or applied. Retargeting the invoke grant (`harvest_published_invoke_iam.tf`) from the instance role to the internal reader role is Phase A of the release order that carries this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM; it changes WHICH identity the code uses for the one `lambda:InvokeFunction`. The grant moves in Terraform, in the release order.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act follows PRD v3.1's rule that gateway reads go through the internal reader role and PRD v3.9's recorded exception (news only, one release): a second instance-role exception is not asked for.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-13` (decomposition addendum R3-T.65, workstream G1-INTERNAL, FWD-22)

All paths relative to the repo root; the gateway is `infra/aws/ec2/opal-gateway` (`GW`). `GW/app/harvest_published.py` `_invoke(function_name, payload)` builds a default-credential boto3 Lambda client (the instance role) and invokes the published-analysis Lambda once.
`GW/app/internal_role.py` already builds an S3 client (`s3_client`) and, since OG-nw-2, a DynamoDB client (`dynamodb_client`) from credentials assumed from `INTERNAL_READER_ROLE_ARN` (cache keyed by (ARN, service); env unset -> None; env set and AssumeRole failing -> `InternalRoleUnavailable`, NO fallback).

1. **`internal_role.py`: a Lambda client from the same assumed role.** Add `lambda_client(sts_factory=None, lambda_factory=None, now=None, config=None)` mirroring `dynamodb_client` exactly (same env key, refresh skew, no-fallback rule, its own cache entry keyed (ARN, "lambda")); the client is built inside the function with the assumed credentials, region `AWS_REGION` env or `us-east-1`, and an optional botocore `Config` argument (the published tool passes read_timeout 50, connect_timeout 5, one attempt, as today). Do not change `s3_client` or `dynamodb_client`.
2. **`harvest_published.py`: `_invoke` prefers the internal role.** `_invoke` uses `internal_role.lambda_client(config=<today's Config>)` when it returns a client; when it returns None (env unset) it builds today's default client inside the function. When it raises `InternalRoleUnavailable`, the TOOL answers the module's existing unavailable refusal (`harvest_published_unavailable` shape, with a message naming the internal role) with ZERO invokes and NO fallback to the default identity. Nothing else in the module changes (admission, route, projection, envelope).
3. **Tests `GW/tests/test_og_gt13.py`** (offline; factories injected; no network), named exactly: `test_oggt13_ac01` (env set: the Lambda client comes from the assumed credentials, recorded, and the default `boto3.client` path is never taken), `test_oggt13_ac02` (env unset: the default client is created lazily inside the function), `test_oggt13_ac03` (env set, AssumeRole raises: the tool answers the unavailable refusal, zero invokes, no default client), `test_oggt13_ac04` (`s3_client` and `dynamodb_client` still return their clients and share no cache entry with `lambda_client`).

## 2. BOUNDS

- Code and tests only. No release, no deploy, no IAM or Terraform change, no invoke of any real Lambda. Edit only the files in `<paths>`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/harvest_published.py
infra/aws/ec2/opal-gateway/tests/test_og_gt13.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~96/`. Rows: id `NFRA_OPLGTW-Z-W96-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt13.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*existing internal-role and published-analysis suites: rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt13.AC2.sh; echo "exit=$?"</invocation><expect>(?s)module-scope boto3 client constructions: 0 \(want 0\).*parents\[N.=3\] in shipped app modules: 0 of \d+ file\(s\) scanned \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the Lambda client comes from the assumed internal role, the default path is unchanged when the env is unset, a failed assume refuses with zero invokes, the other two clients are unchanged. `AC2`: no module-scope AWS client and no fixed-depth parents index.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-13.published-internal-role.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-INTERNAL (decomposition addendum R3-T.65). The grant file `harvest_published_invoke_iam.tf` names `aws_iam_role.gw`; the release order retargets it to `aws_iam_role.int_reader` in Phase A (grant first), so no second instance-role exception is needed.
- Release: with `OG-cp-1` and `OG-nw-2`, after `OG-ap-20`.
- Pre-cut: gt13.AC1 base FAIL as expected (test file absent); gt13.AC2 is a regression guard that passes at base.

<status>complete</status>
<round>37</round>
<workstream>G1-INTERNAL</workstream>
<slot>~96</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
