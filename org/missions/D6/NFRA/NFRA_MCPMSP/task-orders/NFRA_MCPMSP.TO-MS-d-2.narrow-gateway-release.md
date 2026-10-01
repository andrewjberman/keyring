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

**AMENDED A1 (2.0.0_SA_COO~MS, 2026-10-01 ~05:0xZ) -- slot 2 of the opal-gateway release train (1.0.0_SA_CTO~O msg
27517; ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d,
R1, R2, R5).**
- **When:** handed only after MS-r-1 is complete (@dddcd61f5b) AND MX-r-7 (slot 1) has landed. If OG-rl-1 is
  release-ready first, the two swap (R1); the issuer then re-amends the base and the key count.
- **Base, by REF (replaces item 1's "42c52ed4d9"):** cut the release at MX-r-7's deployed commit, read at PHASE A from
  the artifact's `git-ref` metadata and from `EC2_MANIFEST.json`, and re-read immediately before the ANNOUNCE. If the
  live ref is not MX-r-7's, STOP and report both values. Cherry-pick ON TOP of it only this project's round-2 gateway
  commits plus MS-r-1's `fe61befd60` and `720199de7d`. Exclude MDPF_TAXSMA TX-g-1 and NFRA_OPALAI OA-e-10 BY CONTENT
  (C5). Keep every live-only byte (C6); list each live file the release tree changes or drops and justify it as ours.
- **C1:** item 3's two keys go onto the LIVE `.env` printf line in the release tree, the line that already renders
  `MASTER_ADMIN_PRINCIPALS` and `WRITE_CAPABLE_PRINCIPALS`, by hand-merge. Never copy CLOUD's line onto it. CLOUD's own
  line also gains the two keys (it is not shipped).
- **C2:** both principal keys stay. The live script exits 3 without `OG_MASTER_ADMIN_PRINCIPALS` /
  `OG_WRITE_CAPABLE_PRINCIPALS`. The issuer supplies those values off-repo (from 2.0.0_SA_COO~O) in the PHASE B
  continuation, as environment only. Never write, print or commit them.
- **PHASE A, no deploy:** cut, cherry-pick, hand-merge, run item 4's suites, and build the rollback tree at the live
  commit. Then write `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~5/ANNOUNCE_MS-d-2.md` with:
  the pin (base and release commit), the file census against the base, the `.env` KEY set before and after (35 -> 37:
  the 35 live keys plus `INTERNAL_READER_ROLE_ARN` and `MSP_CALLING_IDENTITIES`; keys only, never values), and the
  unchanged tool count and ac08 pin (0 tools added; C3). An ANNOUNCE missing either principal key is a refusal. Report
  the pin and STOP. The issuer takes it to 1.0.0_SA_CTO~O for the CTO never-widen half and signs the COO half (R5,
  C12).
- **PHASE B, only on the issuer's GO after both halves are signed:** re-read the live ref; open item 5's ledger first;
  run `DEPLOY_BASE_REF=<the base> bash infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` from the release tree; read back;
  roll back on any failed leg.
- **Checks:** d2.AC2's allowed set gains `tests/test_deploy_base_guard.py` (MS-r-1's fixture). d2.AC3 also reads the
  host `.env` KEY count (= 37) and one line each of `MASTER_ADMIN_PRINCIPALS` and `WRITE_CAPABLE_PRINCIPALS`.
- **Paths:** `infra/aws/ec2/opal-gateway/app/admin_api.py` widens to `infra/aws/ec2/opal-gateway/**` for the
  release-tree cherry-picks; d2.AC2's census fences what ships.
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 grades only a newly-added order; GATE (viii)
  finds `<placeholders>NONE</placeholders>`).

## 2. BOUNDS

1. No Terraform. No push of any shared branch (the release branch stays local). No vendor call. The two new `.env`
   values: the ARN is not secret; never print any other `.env` value.
2. REFUSE a criterion you cannot meet as written, with its measurement; a half-landed deploy is rolled back to the
   previous deployed commit in the same session.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/**
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
  <criterion id="AC3" cell_refs="MS-d-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/d2.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; /health=200; internal_role=match sender_gate=match admin_refusals=match; tenant_registry=present; INTERNAL_READER_ROLE_ARN lines=1; MSP_CALLING_IDENTITIES lines=1; .env keys=37 (expect 37); MASTER_ADMIN_PRINCIPALS lines=1; WRITE_CAPABLE_PRINCIPALS lines=1 -- RESULT: PASS -- exit=0</expect></criterion>
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
