# NFRA_MCPMSP task order -- `MS-d-1` -- ROUND 1, hop 1 live: the NARROW gateway release (join)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-d-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~1</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the release moves code and one static .env line; the role and its grants are MS-a-1's (applied before this spawns).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the narrow-release census (AC2) and the tool-surface diff are the adversary reads.
EGRESS CLASS, declared: none (Opal's own AWS account and host).
</preflight>

## 1. THE CELL -- `MS-d-1` (decomposition section 2; the join of MS-t-1, MS-t-5 and MS-a-1)

Ship NFRA_MCPMSP's gateway code to the served host `i-07dccb1615503ac99` (`/opt/opal-gateway`) as a NARROW release:
the commit the host runs NOW plus ONLY this project's gateway commits, never other projects' unreleased gateway work.
You continue here after `MS-t-1` (your earlier order) has merged; the issuer's spawn note names this project's gateway
commits on CLOUD (MS-t-1's, MS-t-5's, and the issuer's one-line `app/admin_api.py` hookup) and the Inflection role ARN
from `MS-a-1`.

1. **The deploy script, on YOUR branch, committed first.** The deploy rewrites the host's whole `.env` every time
   (`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:108-111`, the `REMOTE_SCRIPT`), so a hand-edited host line would be
   wiped by the next deploy. Add ONE static line to the `.env` it writes: `FIRM_ROLE_ARNS={"inflection": "<the role
   ARN>"}` (a role ARN is not a secret; quote it so the JSON survives the `printf`). Change NOTHING else there.
2. **The release tree.** Read the deployed commit PREV from `infra/aws/ec2/EC2_MANIFEST.json`
   (`services.opal-gateway.deployed_commit`; `093fc247c6` at the cut -- re-read it, a sibling may have deployed since).
   `git worktree add -b rel-nfra-mcpmsp-r1-gateway /c/tmp/ms-1-rel <PREV>`, then `cherry-pick --no-commit` the
   project's gateway commits and your deploy-script commit, in order, and commit on that branch under your serial.
   - **Census first:** `git -C /c/tmp/ms-1-rel diff --stat <PREV> HEAD -- infra/aws/ec2/opal-gateway` names ONLY
     `app/tenant_registry.py`, `app/firm_role.py`, `app/asker_scope.py`, `app/audit.py`, `app/config.py`,
     `app/admin_tenants.py`, `app/admin_api.py`, `tests/test_mcpmsp_asker_firm.py`, `tests/test_admin_tenants.py`,
     `deploy-to-ec2.sh`. Any other file: STOP, a BLOCKING row.
   - The release base predates this order, so the lane resolver cannot see your grant there. **The issuer authorizes
     the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_MCPMSP~1` for exactly the release-branch commit(s) of those
     files.** Name each use in your report.
3. **Before the act:** (i) render the `.env` locally: extract the release tree's `.env` `printf` line, run it with every
   `%s` replaced by a distinct marker, and print the `KEY=VALUE` lines -- every marker on ITS OWN key and
   `FIRM_ROLE_ARNS` present with valid JSON; any misalignment: STOP. (ii) Prove the rollback: rebuild PREV's artifact
   from a clean PREV tree WITHOUT uploading, and name the command that re-deploys it; if it cannot be shown: STOP.
   (iii) List the registered MCP tool names on the host (on-box, the service's own venv and `.env`) -- the "before"
   list.
4. **NEVER-2 ledger, on YOUR branch:** `python .tools/deploy_ledger.py open --slug nfra-mcpmsp-r1-gateway-release ...`
   with legs: release build + upload, SSM pull + restart, manifest record, verify; plus the census, the rollback
   command and the task families the artifact tag reaches (the gateway service only; say how you measured it). Commit
   the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcpmsp-r1-gateway-release.json`.
5. **Act from the RELEASE worktree with ITS scripts:** `cd /c/tmp/ms-1-rel && bash infra/aws/ec2/safe-ec2-deploy.sh
   opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. Immediately poll `/health` on the host; not 200 within
   90 seconds -> run the named rollback AT ONCE, close the entry as rolled back, and stop. Then list the MCP tool names
   again: the difference from the "before" list must be EMPTY (this release adds an admin route, no MCP tool); a
   non-empty difference -> roll back.
6. **Record on YOUR branch:** `EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` = the release commit, plus a
   `release_note` naming in words the other projects' gateway commits CLOUD holds UNRELEASED
   (`git log <PREV>..HEAD -- infra/aws/ec2/opal-gateway` on CLOUD). The script's own manifest auto-commit can fail on
   this device (jq.exe writes CRLF; row NFRA_OPALAI-Z-W2-S4): read its ERROR line and record by hand on an LF copy.
   Close every leg with its proof and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Terraform, the ALB, the host's role and its secrets are untouched. `safe-ec2-deploy.sh` is READ, never edited.
2. Mid-act failure: the named rollback, the entry closed as rolled back, a report. Never half-landed.
3. No push, no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpmsp-r1-gateway-release.json
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/**` (other than the deploy script),
`org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-d-1.narrow-gateway-release.md` (the precedent this
procedure follows), `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`. Rows:
`INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-d-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/d1.AC1.sh; echo "exit=$?"</invocation><expect>slug nfra-mcpmsp-r1-gateway-release: entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR present -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-d-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/d1.AC2.sh; echo "exit=$?"</invocation><expect>descends=yes; gateway files shipped >=1, outside NFRA_MCPMSP's set 0; carries the three new modules 3 of 3 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-d-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/d1.AC3.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; tenant_registry=match firm_role=match admin_tenants=match; FIRM_ROLE_ARNS lines=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/NFRA_MCPMSP.TO-MS-d-1.narrow-gateway-release.proof_of_spec.json`.
Report once, with: PREV and the release commit; the census; the rendered `.env` marker list (no values); the rollback
command; the tool-list counts before/after and their difference; each override use; the three check lines; the ledger
path; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985); WORLD: a deploy. Spawn preconditions (decomposition sequencing
(d)): MS-t-1, MS-t-5 and MS-a-1 drained and the `admin_api.py` hookup committed; no other project's gateway deploy
entry open; NFRA_OPLGTW's `OG-t-2` (staged at the cut; it also edits `deploy-to-ec2.sh`) terminal or confirmed not
mid-edit. **Write-surface ruling:** the decomposition lists `deploy-to-ec2.sh` under "reads"; this cut grants it as a
WRITE because the deploy rewrites the host `.env` on every run (`deploy-to-ec2.sh:108-111`, read at the cut), so the
cell's `.env` line can only live there -- the issuer's in-decomposition path grant, graded by no gate limb beyond
GATE (v)'s `<paths>` presence. Checks dry-run at base: AC1 FAIL as expected; AC2 FAIL as expected (manifest
`093fc247c6`, 8 foreign files vs its prior value, 0 of 3 modules); AC3 FAIL as expected (`/health=200` -- the
control -- with three MISMATCH and 0 `FIRM_ROLE_ARNS` lines). The override for release-branch commits follows the
MCPORTAL MP-d-1 precedent.

<status>staged</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
