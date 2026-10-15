# NFRA_OPLGTW task order -- `OG-nw-2` -- the five G6 news tools read DynamoDB through the internal reader role (PRD v3.9, the owed follow-up cell)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-nw-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-nw-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~95</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests only; nothing is deployed or applied. The Terraform move (the same actions on the internal reader role, the instance-role statement destroyed by name) is Phase A of the release order that carries this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM; it changes WHICH identity the code uses (the assumed internal reader role, as the S3 readers do). The AWS calls stay `dynamodb:Query` and `dynamodb:GetItem` on the same three tables and index.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z`'s PRD v3.9 (@8c84e01428): "one cell moves the news readers onto the internal reader and destroys the instance-role statement by name".
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-nw-2` (decomposition addendum R3-T.64, workstream G6-INTERNAL, FWD-22)

PRD v3.9 accepted the G6 news read on the gateway INSTANCE role for the release `OG-ap-19` only, and owes one cell that moves the news readers to the internal reader role. THIS is the code half. All paths relative to the repo root; the gateway is `infra/aws/ec2/opal-gateway` (`GW`).

Today `GW/app/news_typed.py` `_ddb()` builds a default-credential boto3 DynamoDB client (the instance role). `GW/app/internal_role.py` builds an S3 client from credentials assumed from `INTERNAL_READER_ROLE_ARN` (cached until shortly before expiry; env unset -> None; env set and AssumeRole failing -> `InternalRoleUnavailable`, NO fallback to another identity).

1. **`internal_role.py`: a DynamoDB client from the same assumed role.** Add a function `dynamodb_client(sts_factory=None, dynamodb_factory=None, now=None)` that mirrors `s3_client` exactly (same env key, same refresh skew, same no-fallback rule, its own cache entry keyed by ARN AND service so the S3 cache is untouched), builds the client with `boto3.client("dynamodb", region_name=<AWS_REGION env or us-east-1>, <the assumed credentials>)` INSIDE a function (a test injects the factories), and returns None when the env is unset. Do not change `s3_client`'s behaviour or signature.
2. **`news_typed.py`: `_ddb()` prefers the internal role.** `_ddb()` returns `internal_role.dynamodb_client()` when it returns a client; when it returns None (env unset) it returns today's lazily created default client. When it raises `InternalRoleUnavailable`, the TOOL answers an unavailable refusal (reuse the module's existing `news_unavailable` shape or the typed refusal with a code naming the internal role) with ZERO DynamoDB calls and NO fallback to the default identity. Nothing else in the module changes.
3. **Tests `GW/tests/test_og_nw2.py`** (offline; factories injected; no network), named exactly: `test_ognw2_ac01` (env set: the client comes from the assumed credentials, recorded, and `boto3.client` is never called for the default path), `test_ognw2_ac02` (env unset: the default client is created lazily inside the function, once), `test_ognw2_ac03` (env set, AssumeRole raises: a tool answers an unavailable refusal, zero DynamoDB calls, the default client never created), `test_ognw2_ac04` (`s3_client` still returns the S3 client and shares no cache entry with `dynamodb_client`).

## 2. BOUNDS

- Code and tests only. No release, no deploy, no IAM or Terraform change, no write to any table or bucket. Edit only the files in `<paths>`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an item's content, a person's name or a full email address; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/news_typed.py
infra/aws/ec2/opal-gateway/tests/test_og_nw2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~95/`. Rows: id `NFRA_OPLGTW-Z-W95-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-nw-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/nw2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*existing internal-role and news suites: rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-nw-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/nw2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)module-scope boto3 client constructions: 0 \(want 0\).*parents\[N.=3\] in shipped app modules: 0 of \d+ file\(s\) scanned \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the news client comes from the assumed internal role, the default path is unchanged when the env is unset, a failed assume refuses with zero reads, S3 behaviour is unchanged. `AC2`: no module-scope AWS client and no fixed-depth parents index.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-nw-2.news-internal-role.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G6-INTERNAL (decomposition addendum R3-T.64). PRD v3.9 @8c84e01428: the instance-role statement `gw_news_read` is destroyed BY NAME and the same actions move to a policy on the internal reader role in the release that carries this cell (Phase A of that applier order); the code and the Terraform must land in ONE release, grant first.
- Release: after `OG-ap-19` and `OG-ap-20`, with the person reader `OG-cp-1`.
- Pre-cut: nw2.AC1 base FAIL as expected (test file absent); nw2.AC2 base: the module-scope check passes at base and the parents scan passes, so AC2 is a regression guard, not a build criterion.

<status>complete</status>
<round>37</round>
<workstream>G6-INTERNAL</workstream>
<slot>~95</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
