# NFRA_MCPORTAL task order -- `MP-d-1` -- ROUND 2, E4: the NARROW gateway release that serves Andrew's dashboard

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-d-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the host, its role and Terraform are untouched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is the CTO's ruling (@592e319a06 precedent, E4 @667f442b8a).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `MP-d-1` (round 2, decomposition section R2.1)

The gateway on `i-07dccb1615503ac99` runs `deployed_commit` **`f1f0fc6780`** (`infra/aws/ec2/EC2_MANIFEST.json`,
`services.opal-gateway`). That commit is the NARROW release of NFRA_OPALAI's change, cut at the previously deployed
commit. CLOUD HEAD's gateway tree carries other projects' unreleased commits that must NOT ship.

The CTO's round-1 analysis (`org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.round1.md` section 4, E4, READ
IT) rules this release: **`f1f0fc6780` plus ONLY NFRA_MCPORTAL's gateway commits.** Those are:
- MP-t-1 `98ad7e253f`, the owner gate and serving;
- MP-t-4 `17b7e01c0f`, the grant handlers;
- MP-g-1's gateway commit(s) on this branch: author `0.9.0_WK_NFRA_MCPORTAL~2`, touching `infra/aws/ec2/opal-gateway`,
  after this order's issuance;
- this order's own `deploy-to-ec2.sh` commit.

In order:
1. **The deploy script** (on THIS branch, committed first). In `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`:
   - (a) build `mcportal` at its checked-out commit (`bun install` + `bun run build`) and put `mcportal/dist/` into the
     artifact at the path `DASHBOARD_BUNDLE_DIR` names (default `dashboard/` beside `app/`);
   - (b) add to the host `.env` it writes: `DASHBOARD_OWNER_EMAILS=andrew@opalinvest.com`,
     `GRANT_WRITER_FUNCTION_NAME=mcportal-grant-writer-lambda` and `MCPORTAL_CHANGES_TABLE=mcportal-grant-changes-table`.
     Both writer names fail closed until the writer exists. Change NOTHING else there.
2. **The release tree.** `git worktree add -b rel-nfra-mcportal-r2-gateway /c/tmp/mp-2-rel f1f0fc6780`, then
   `git -C /c/tmp/mp-2-rel cherry-pick --no-commit` the commits above, in order, and commit on that branch under your
   serial.
   - **Census before anything else:** `git -C /c/tmp/mp-2-rel diff --stat f1f0fc6780 HEAD -- infra/aws/ec2/opal-gateway`
     names ONLY files those commits changed. Any other file: STOP, a BLOCKING row.
   - The release base predates this order, so the lane resolver cannot see your grant there. **The issuer authorizes
     the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_MCPORTAL~2` for exactly the release-branch commit(s) of
     those files.** Name each use in your report.
3. **The bundle.** The release tree's `mcportal` is a nested checkout at the commit THIS worktree's `mcportal` holds
   (opal's r1-drain with MP-p-1). Record that commit.
4. **Rollback proven before the act:** rebuild `f1f0fc6780`'s gateway artifact from a clean `f1f0fc6780` tree WITHOUT
   uploading, and name the command that would re-deploy it. If it cannot be shown: STOP, no deploy, a BLOCKING row.
5. **NEVER-2 ledger, on THIS branch (`wk-NFRA_MCPORTAL-2`), in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-r2-gateway-release`. Legs: bundle build,
     release build + upload, SSM pull + restart, manifest record. Plus the census, the rollback, and the analysis's path;
   - commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-r2-gateway-release.json`;
   - ACT from the RELEASE worktree with ITS copy of the scripts:
     `cd /c/tmp/mp-2-rel && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
     The script's Step-3 manifest auto-commit can fail on this device (jq.exe writes CRLF; row NFRA_OPALAI-Z-W2-S4).
     Read its ERROR line, and record by hand on an LF copy as below;
   - **record the release on THIS branch:** `EC2_MANIFEST.json` `services.opal-gateway` gets the release commit as
     `deployed_commit`, the bundle's commit as `mcportal_commit`, and a `release_note` naming in words the other
     projects' gateway commits CLOUD holds UNRELEASED (list them from `git log f1f0fc6780..HEAD -- infra/aws/ec2/opal-gateway`);
   - close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` is READ, never edited.
2. If a leg fails mid-act: roll back with the named command, close the entry as rolled back, and report. Never
   half-landed.
3. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcportal-r2-gateway-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~2/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/`, `mcportal/`.

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_MCPORTAL-Z-W2-S<k>` (next free k for W2).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-d-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/d1.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-d-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/d1.AC2.sh; echo "exit=$?"</invocation><expect>descends from f1f0fc6780=yes; gateway files shipped >=1, outside NFRA_MCPORTAL's set 0; carries gate+handlers+round-2 tests 3 of 3; mcportal_commit resolves=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-d-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/d1.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; /health=200; /api/admin/whoami=401 or 403; /=401 or 403 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~2/NFRA_MCPORTAL.TO-MP-d-1.narrow-gateway-release.proof_of_spec.json`.
Report once:
- the census of what shipped and the commits named unreleased;
- the rollback;
- the ledger entry path;
- each override use;
- the commit hashes;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E4. Never-widen (CTO+COO):
- The CTO half is the analysis's E4, which reuses ruling @592e319a06's shape.
- The COO half is this issuance. Blast radius: the gateway's `/` and `/api/admin/*` routes plus three `.env` keys.
  Rollback: `f1f0fc6780`'s artifact, rebuilt and proven before the act.

SPAWN ONLY after MP-g-1 and MP-p-1 have DRAINED (g-1's commits on CLOUD; p-1's nested commit in mcportal r1-drain).
Provision with `--nested mcportal=r1-drain`.

<status>pending</status>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
