# NFRA_OPALAI task order -- `OA-t-6` -- HOP 5, LIVE: the gateway deploy that puts opal_asker_query on the served host

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-t-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the deploy moves code on the existing host and role (opal-gateway-role, instance i-07dccb1615503ac99); no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane -- one S3 artifact upload and one SSM pull/restart on the gateway host, through the existing deploy scripts. No vendor.
</preflight>

## 1. THE CELL -- `OA-t-6` (round 1, decomposition s.2/s.3) -- AMENDED to the CTO's narrow-release ruling

The earlier worker on this slot built the audit hookup (`050035f941`, `app/audit.py` `_ARGS_ALLOWLIST` gains
`opal_asker_query`) and then correctly STOPPED at the census. Between the deployed commit `1764e54a16` and CLOUD HEAD,
`infra/aws/ec2/opal-gateway` carries five unreleased commits of three other projects (row `NFRA_OPALAI-Z-W2-S3`). The CTO
ruled (`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/RULING_OA-t-6_NARROW_GATEWAY_RELEASE_20260925.md`
@`592e319a06`, READ IT FIRST): **the release is `1764e54a16` plus NFRA_OPALAI's two changes and nothing else.** The two
changes are `cc22fdfb9d` (OA-t-5: `app/asker_scope.py` new, one registration in `app/tools.py`, one `NATIVE_TOOLS` line in
`app/data_entitlement.py`, `tests/test_asker_scope.py`) and `050035f941` (the audit row). Do this, in order:

1. **The release tree.** `git worktree add -b rel-nfra-opalai-r1-gateway /c/tmp/oa-2-rel 1764e54a16`. Apply the two
   commits BY CONTENT (`git -C /c/tmp/oa-2-rel cherry-pick --no-commit cc22fdfb9d 050035f941`), then commit on that branch
   under your serial. **Census the release tree before anything else:** `git -C /c/tmp/oa-2-rel diff --stat 1764e54a16
   HEAD -- infra/aws/ec2/opal-gateway` names ONLY `app/asker_scope.py`, `app/tools.py`, `app/data_entitlement.py`,
   `app/audit.py` and `tests/test_asker_scope.py`. Any other file: STOP, a BLOCKING row. That release worktree's base
   predates this order, so the lane resolver cannot see your grant there. **The issuer authorizes the audited
   `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPALAI~2` for exactly the release-branch commits of these five files**;
   name each use in your report.
2. **Rollback proven before the act** (the ruling's condition): show that `1764e54a16`'s gateway artifact can be
   rebuilt, by building the deploy script's tarball from a clean `1764e54a16` tree WITHOUT uploading, and name the
   command that would re-deploy it. If it cannot be shown, STOP: no deploy, a BLOCKING row.
3. **NEVER-2 ledger, on THIS worktree's branch (`wk-NFRA_OPALAI-2`), in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-opalai-r1-gateway-asker-query`: legs = release build +
     upload, SSM pull + restart, manifest record; plus the release-tree census, the rollback, and the ruling's path;
   - commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-opalai-r1-gateway-asker-query.json`;
   - ACT from the RELEASE worktree with ITS copy of the scripts: `cd /c/tmp/oa-2-rel && bash infra/aws/ec2/safe-ec2-deploy.sh
     opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`;
   - **record the release on THIS branch:** `infra/aws/ec2/EC2_MANIFEST.json`'s `services.opal-gateway` gets the
     release commit as `deployed_commit` (plus the script's other fields verbatim from the release worktree's manifest),
     and a `release_note` stating in words that CLOUD HEAD holds the five foreign commits
     (`650c9a99cb`, `6abf60e5d5`, `8dce9aeb0b`, `e8f800e6a9`, `9e4074c33a`, `6c37cc6b00`) UNRELEASED;
   - close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Terraform, the host, its role and its secrets are untouched. The deploy script and `safe-ec2-deploy.sh` are READ,
   never edited. If either refuses or needs a change, that is a BLOCKING row.
2. If a leg fails mid-act: roll back with the named command, close the entry as rolled back, and report. Never leave
   it half-landed.
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_asker_scope.py
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-opalai-r1-gateway-asker-query.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~2/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, `infra/aws/ec2/opal-gateway/`.

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W2-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-t-6"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t6.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-t-6"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t6.AC2.sh; echo "exit=$?"</invocation><expect>deployed_commit contains asker_scope.py=yes; after the cut=yes; deployed_by=0.9.0_WK_NFRA_OPALAI~2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-t-6"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t6.AC3.sh; echo "exit=$?"</invocation><expect>committed md5 = live md5 read over SSM (status Success) -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~2/NFRA_OPALAI.TO-OA-t-6.gateway-deploy.proof_of_spec.json`. Report once: the census of what shipped, the rollback you named, the ledger entry path, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** WORLD. Spawned only after OA-t-5 merges; the slot's new worktree is provisioned off the post-merge
HEAD. Adds the CTO's exercised read. The live refusal of an un-profiled asker is the close run's.

<status>pending</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
