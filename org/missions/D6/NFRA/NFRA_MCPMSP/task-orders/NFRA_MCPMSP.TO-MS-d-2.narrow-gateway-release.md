# NFRA_MCPMSP task order -- `MS-d-2` -- ROUND 2, release: the NARROW gateway release of round 2's code

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-d-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~5</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant; the release ships an ARN the role cell already applied.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2 (narrow census) is the read against shipping a sibling's code.
EGRESS CLASS, declared: none (Opal's own host over the existing deploy path).
</preflight>

## 1. THE CELL -- `MS-d-2` (decomposition v2, R2.2) -- the join of MS-ig-1, MS-ir-2, MS-sg-1, MS-rq-1, MS-r-1

The issuer hands you this order only after those five are merged to CLOUD. Release their code to the gateway host
(instance `i-07dccb1615503ac99`) NARROWLY:
1. **Re-read the deployed commit at your own start** (`infra/aws/ec2/EC2_MANIFEST.json`
   `services.opal-gateway.deployed_commit`; `42c52ed4d9` at the cut -- a sibling may have released since). Cut the release
   branch AT that commit and bring ONLY this project's round-2 gateway commits onto it (merge or cherry-pick ON TOP of
   it, so the release commit descends from it). The gateway files the release may change vs that commit: `app/{internal_role,
   query_v0,sender_gate,asker_scope,audit,admin_refusals,admin_api}.py`, `deploy-to-ec2.sh`,
   `tests/{test_mcpmsp_internal_role,test_mcpmsp_sender_gate,test_admin_refusals}.py`, `tests/run_release_suites.sh`.
   Anything else is a sibling's and a BLOCKING row.
2. **Item 0 -- the hookup:** in `app/admin_api.py` add `from . import admin_refusals` and `*admin_refusals.routes,`
   beside `*admin_tenants.routes,` (`:51`) -- on CLOUD and on the release branch.
3. **`.env`:** in `deploy-to-ec2.sh`'s `.env` printf (`:281`) add `INTERNAL_READER_ROLE_ARN=<the role ARN MS-ir-2
   reported: arn:aws:iam::313476888478:role/gateway-global-internal-reader-role>` and `MSP_CALLING_IDENTITIES=` (EMPTY
   unless the order is amended with gate G-MSPID's value) -- on CLOUD and on the release branch.
4. **Suites on the release tree:** `bash tests/run_release_suites.sh <every gateway suite the release touches plus the
   asker/admin suites>`; all green, tracked `audit.jsonl` unchanged.
5. **Ledger first** (NEVER-2): `python .tools/deploy_ledger.py open --slug nfra-mcpmsp-r2-gateway-release ...`, commit
   the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcpmsp-r2-gateway-release.json` before the deploy;
   deploy from the release tree with `bash infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (its own mcportal resolution,
   R-4); `EC2_MANIFEST.json` records the release commit as `deployed_commit`; close the entry; commit.
6. The MCP tool list is unchanged (no new tool); `/health` 200.

## 2. BOUNDS

1. No Terraform. No push of any shared branch (the release branch stays local). No vendor call. The two new `.env`
   values: the ARN is not secret; never print any other `.env` value.
2. REFUSE a criterion you cannot meet as written, with its measurement; a half-landed deploy is rolled back to the
   previous deployed commit in the same session.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpmsp-r2-gateway-release.json
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~5/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: every other `infra/aws/ec2/opal-gateway/**` file, `.tools/deploy_ledger.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W5-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your last commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-d-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/d2.AC1.sh; echo "exit=$?"</invocation><expect>slug nfra-mcpmsp-r2-gateway-release: entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-d-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/d2.AC2.sh; echo "exit=$?"</invocation><expect>deployed_commit=X prev=P descends=yes; gateway files shipped >=1, outside round 2's set 0; carries the three new modules 3 of 3 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-d-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/d2.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; /health=200; internal_role=match sender_gate=match admin_refusals=match; tenant_registry=present; INTERNAL_READER_ROLE_ARN lines=1; MSP_CALLING_IDENTITIES lines=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~5/NFRA_MCPMSP.TO-MS-d-2.narrow-gateway-release.proof_of_spec.json`.
Report once, with: the base and release commits; the suite line; the three check lines; the ledger path; the commit
hashes; any row. Then STOP: this slot's next order (MS-dn-1) is HELD.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance (release join). Staged: handed only after MS-ig-1, MS-ir-2, MS-sg-1, MS-rq-1, MS-r-1
merge. If G-MSPID's value arrives first, item 3 is amended with it (issuer amendment). Checks dry-run at base: AC1 FAIL
as expected; AC2 FAIL as expected (0 of 3 modules; the manifest's pre-value 093fc247c6 is not an ancestor of
42c52ed4d9 -- round 1's and MCPINDEX's releases were cherry-picked; AC2 reads PREV at the release's own value change,
so the release must build ON the deployed commit); AC3 FAIL as expected (modules absent on host; /health 200).

<status>staged</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
