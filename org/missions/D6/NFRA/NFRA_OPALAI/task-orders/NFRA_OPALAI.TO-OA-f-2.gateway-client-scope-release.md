# NFRA_OPALAI task order -- `OA-f-2` -- ADDENDUM A1 (Z-S18, Andrew's option 2): the NARROW gateway release of OA-f-1

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~8</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the existing host and role (i-07dccb1615503ac99); no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release NARROWS one grant.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane -- one S3 artifact upload and one SSM pull/restart through the existing deploy scripts. No vendor.
</preflight>

## 1. THE CELL -- `OA-f-2` (decomposition ADDENDUM A1)

Spawned only after `OA-f-1` drained to CLOUD. Its commits are named in the COO's hand-off message to you; they touch
only `infra/aws/ec2/opal-gateway/`.

**The live base is NOT the CLOUD manifest's.** At this order's cut the host served
`0af72fb1d071209b953168924bc64d391dfb92ff`, which is `1.0.0_SA_CTO`'s laptop release (branch
`origin/rel-laptop-teams-reader-gw`, recorded at `88377e148e`, deployed 2026-09-25T23:01:38Z). The CLOUD manifest still
reads `1f7128201a`. The dashboard bundle is byte-identical to `opal-gateway-1f7128201a.tar.gz`: mcportal commit
`a3bff71ffa3f5c73aa0fb7ea1e7386434e233054`.

In order:
0. **Resolve the live base BY CONTENT at your own cut** (never by the manifest or a branch name):
   - read the md5 of `/opt/opal-gateway/app/identity_scope.py` and `/opt/opal-gateway/app/tools.py` over SSM;
   - compare them with `git show <candidate>:infra/aws/ec2/opal-gateway/app/<file> | md5sum`, for `0af72fb1d0` and for
     any later laptop release commit you find on `origin/rel-laptop-*`;
   - the base is the commit whose files BOTH match. If none matches, STOP and file a BLOCKING row.
1. **The announcement, BEFORE touching the instance** (CTO ruling @75117e60d6: ONE deployer at a time).
   - You cannot send, so write the announcement to
     `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~8/ANNOUNCE_OA-f-2.md`: branch, base commit,
     release commit, ledger slug.
   - Commit it, then STOP and report `ANNOUNCE READY` as your final message. The COO relays it through
     `0.0.0_AB_MSTR~Z` and continues you with `GO`.
   - Do no step below the release tree's census (step 2) before `GO`.
2. **The release tree.**
   - `git worktree add -b rel-nfra-opalai-zs18-gateway /c/tmp/oa-8-rel <base>`, then `git -C /c/tmp/oa-8-rel
     cherry-pick --no-commit` OA-f-1's commits and commit under your serial.
   - Census: `git -C /c/tmp/oa-8-rel diff --stat <base> HEAD -- infra/aws/ec2/opal-gateway` names ONLY the files
     OA-f-1 changed. Any other file: STOP, a BLOCKING row.
   - Put the nested `mcportal` checkout at `a3bff71ffa3f5c73aa0fb7ea1e7386434e233054` for the bundle build.
   - **The issuer authorizes the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPALAI~8` for exactly the
     release-branch commit(s).** Name each use in your report.
   - Run `tests/test_identity_scope.py` inside the release tree, and record the result.
3. **Rollback proven before the act:**
   - rebuild `<base>`'s gateway artifact from a clean `<base>` tree WITHOUT uploading, and name the redeploy command;
   - pre-acknowledge the rollback's halt gate now: `HALT_ACK=1` when the halt gate reads 0 STOP (row
     `NFRA_MCPORTAL-Z-S8`: the gate takes ~12 minutes, too long for a rollback);
   - if the rollback cannot be shown, STOP: no deploy, a BLOCKING row.
4. **Guards (from the 2026-09-25 outage, row `NFRA_MCPORTAL-Z-W2-S7`):**
   - (i) render the release tree's `.env` `printf` line locally with a distinct marker per `%s`, and show every marker
     on its own key (markers only, no secrets). Any misalignment: STOP.
   - (ii) immediately after the restart, poll `/health`; not 200 within 90 seconds -> run the rollback at once, close
     the entry as rolled back, and stop.
   - (iii) list the registered MCP tool names on the host before and after (on-box, the service's own venv and
     `.env`). The difference must be empty; a non-empty difference means roll back.
5. **NEVER-2 ledger, on THIS worktree's branch, in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-opalai-zs18-gateway-client-scope`. Legs: release build +
     upload, SSM pull + restart, manifest record. Plus the base resolution, the census, the rollback, and this order's
     path;
   - commit the entry AND its sentinel;
   - ACT from the release worktree with ITS scripts:
     `cd /c/tmp/oa-8-rel && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
     If Step 3's manifest auto-commit fails (jq.exe writes CRLF), record by hand on an LF copy;
   - **record the release on THIS branch:** `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway` gets the release
     commit as `deployed_commit`, `a3bff71ffa3f5c73aa0fb7ea1e7386434e233054` as `mcportal_commit`, and a
     `release_note` naming in words the base (the laptop release) and what CLOUD holds unreleased;
   - close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` and `deploy-to-ec2.sh`
   are READ, never edited. NEVER deploy `rel-nfra-mcportal-r2-gateway` (@`c97839d7c8`). No HEAD deploy.
2. If a leg fails mid-act: roll back, close the entry as rolled back, and report. Never half-landed.
3. Standing rule: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with
   its measurement. Never repair, widen or route around a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/identity_scope.py
infra/aws/ec2/opal-gateway/app/context.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/integrations/base.py
infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt
infra/aws/ec2/opal-gateway/tests/test_identity_scope.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-opalai-zs18-gateway-client-scope.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~8/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W8-S<k>`.

## 4. PROOF OF SPEC (literal; run from the WORKSPACE ROOT after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/f2.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/f2.AC2.sh; echo "exit=$?"</invocation><expect>release-branch md5 = live md5 (ssm status Success) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-f-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/f2.AC3.sh; echo "exit=$?"</invocation><expect>live upload rows: unqualified=0 client-qualified=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~8/NFRA_OPALAI.TO-OA-f-2.gateway-client-scope-release.proof_of_spec.json`.
Report once, with:
- the base resolution (the md5 pairs);
- the census;
- the rollback;
- the `.env` render;
- the tool-list counts and their difference;
- the ledger path and commits;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act on Andrew's option 2 (CTO msg 25935). The COO is the single opal-gateway deployer
(@75117e60d6) and relays the announcement through MSTR. Dry-run at base: f2.AC1 FAIL (0 entries), f2.AC2 FAIL (no
release branch; live 06b5f86a = the identity_scope.py at laptop release `b4101ea371`/`0af72fb1d0`), f2.AC3 FAIL
(unqualified=1).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~8</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
