# NFRA_OPALAI task order -- `OA-g-2` -- ADDENDUM A2: the NARROW gateway release of OA-g-1 (portal-only asker grants)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-g-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~9</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the existing host and role (i-07dccb1615503ac99); no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release adds a narrower grant SHAPE; it writes no grant.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane -- one S3 artifact upload and one SSM pull/restart through the existing deploy scripts. No vendor.
</preflight>

## 1. THE CELL -- `OA-g-2` (decomposition ADDENDUM A2)

Spawned only after `OA-g-1` drained to CLOUD AND `OA-f-2` closed (one gateway deployer at a time). OA-g-1's commits are
named in the COO's hand-off message to you. Cherry-pick ONLY their `infra/aws/ec2/opal-gateway/` files; the contract
file under `org/standards/` is not part of the host artifact.

**The live base.** When this order was cut, the host served the laptop release `0af72fb1d0`. OA-f-2 (the Z-S18 release,
branch `rel-nfra-opalai-zs18-gateway`, release commit `c5f8099440`) deploys on top of it before this order runs. So the
expected base at YOUR cut is OA-f-2's release commit, but you resolve it BY CONTENT, never by the manifest. The
dashboard bundle is mcportal commit `a3bff71ffa3f5c73aa0fb7ea1e7386434e233054`.

In order:
0. **Resolve the live base BY CONTENT at your own cut** (never by the manifest or a branch name):
   - read the md5 of `/opt/opal-gateway/app/identity_scope.py`, `/opt/opal-gateway/app/data_entitlement.py` and
     `/opt/opal-gateway/app/asker_scope.py` over SSM;
   - compare them with `git show <candidate>:infra/aws/ec2/opal-gateway/app/<file> | md5sum`, for `c5f8099440`
     (OA-f-2's release), `0af72fb1d0`, and any later commit on `origin/rel-laptop-*` or `rel-nfra-*`;
   - the base is the commit whose files ALL match. If none matches, STOP and file a BLOCKING row.
1. **The announcement, BEFORE touching the instance** (CTO ruling @75117e60d6: ONE deployer at a time).
   - You cannot send, so write the announcement to
     `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~9/ANNOUNCE_OA-g-2.md`: branch, base commit,
     release commit, ledger slug.
   - Commit it, then STOP and report `ANNOUNCE READY` as your final message. The COO relays it through
     `0.0.0_AB_MSTR~Z` and continues you with `GO`.
   - Do no step below the release tree's census (step 2) before `GO`.
2. **The release tree.**
   - `git worktree add -b rel-nfra-opalai-portal-grant-gateway /c/tmp/oa-9-rel <base>`, then `git -C /c/tmp/oa-9-rel
     cherry-pick --no-commit` OA-g-1's commits, restore every file outside `infra/aws/ec2/opal-gateway/` to the base, and
     commit under your serial.
   - Census: `git -C /c/tmp/oa-9-rel diff --stat <base> HEAD -- infra/aws/ec2/opal-gateway` names ONLY the gateway files
     OA-g-1 changed (`app/data_entitlement.py`, `app/asker_scope.py`, `ops/schwab_entitlement_admin.py`,
     `tests/test_portal_grant.py`). Any other file: STOP, a BLOCKING row.
   - Put the nested `mcportal` checkout at `a3bff71ffa3f5c73aa0fb7ea1e7386434e233054` for the bundle build.
   - **The issuer authorizes the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPALAI~9` for exactly the
     release-branch commit(s).** Name each use in your report.
   - Run `tests/test_portal_grant.py`, `tests/test_asker_scope.py` and `tests/test_identity_scope.py` inside the
     release tree, and record the results.
3. **Rollback proven before the act:**
   - rebuild `<base>`'s gateway artifact from a clean `<base>` tree WITHOUT uploading, and name the redeploy command;
   - pre-acknowledge the rollback's halt gate now: `HALT_ACK=1` when the halt gate reads 0 STOP (rows
     `NFRA_MCPORTAL-Z-S8` and `NFRA_OPALAI-Z-W8-S2`: the gate takes up to ~24 minutes; the issuer accepts that, and the
     act runs only outside US business hours, row `NFRA_OPALAI-Z-S24`);
   - if the rollback cannot be shown, STOP: no deploy, a BLOCKING row.
4. **Guards (from the 2026-09-25 outage, row `NFRA_MCPORTAL-Z-W2-S7`):**
   - (i) render the release tree's `.env` `printf` line locally with a distinct marker per `%s`, and show every marker
     on its own key (markers only, no secrets). Any misalignment: STOP.
   - (ii) immediately after the restart, poll `/health`; not 200 within 90 seconds -> run the rollback at once, close
     the entry as rolled back, and stop.
   - (iii) list the registered MCP tool names on the host before and after (on-box, the service's own venv and
     `.env`). The difference must be empty; a non-empty difference means roll back.
5. **NEVER-2 ledger, on THIS worktree's branch, in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-opalai-portal-grant-gateway`. Legs: release build +
     upload, SSM pull + restart, manifest record. Plus the base resolution, the census, the rollback, and this order's
     path;
   - commit the entry AND its sentinel;
   - ACT from the release worktree with ITS scripts:
     `cd /c/tmp/oa-9-rel && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
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
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_portal_grant.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-opalai-portal-grant-gateway.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~9/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W9-S<k>`.

## 4. PROOF OF SPEC (literal; run from the WORKSPACE ROOT after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-g-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/g2.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-g-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/g2.AC2.sh; echo "exit=$?"</invocation><expect>release-branch md5 = live md5 of app/data_entitlement.py (ssm status Success) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-g-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/g2.AC3.sh; echo "exit=$?"</invocation><expect>release-branch md5 = live md5 of app/asker_scope.py (ssm status Success) -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~9/NFRA_OPALAI.TO-OA-g-2.portal-grant-release.proof_of_spec.json`.
Report once, with:
- the base resolution (the md5 pairs);
- the census;
- the rollback;
- the `.env` render;
- the tool-list counts and their difference;
- the ledger path and commits;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act on the CTO's ruling (B) (msg 25996). The COO is the single opal-gateway deployer
(@75117e60d6) and relays the announcement through MSTR. Dry-run at base: g2.AC1 FAIL (0 entries), g2.AC2 FAIL (no
release branch; live data_entitlement.py 85fddfe3).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~9</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
