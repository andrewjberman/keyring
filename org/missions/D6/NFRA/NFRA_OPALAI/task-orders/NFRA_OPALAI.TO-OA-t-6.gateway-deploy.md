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

## 1. THE CELL -- `OA-t-6` (round 1, decomposition s.2/s.3)

`OA-t-5` (your previous order) built `opal_asker_query` in `infra/aws/ec2/opal-gateway/app/asker_scope.py`. It is merged
at the HEAD your new worktree carries. Deploy that HEAD's gateway to the live host with the existing path:
`infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. It builds a tarball of
`infra/aws/ec2/opal-gateway`, uploads it to S3, SSM-pulls it onto `i-07dccb1615503ac99`, and then updates and commits
`infra/aws/ec2/EC2_MANIFEST.json`. **In this order, every step before the act is a read, except one hookup line:**

0. **The audit hookup (commit it first, alone).** `infra/aws/ec2/opal-gateway/app/audit.py`'s `_ARGS_ALLOWLIST` does not
   declare the new tool, so its audit rows omit every field (row `NFRA_OPALAI-Z-W2-S2`). Add ONE entry directly after
   the `"query_v0":` line: `"opal_asker_query":             {"asker_oid", "key", "verdict"},` with a one-line comment
   naming NFRA_OPALAI C10. That is metadata only, `query_v0`'s precedent, and no value field. Change nothing else in
   that file. This commit is the one non-OA-t-5 gateway change the census below admits, because it is this order's own.

1. **Census what ships.** The manifest's `opal-gateway.deployed_commit` at the cut is
   `1764e54a16b7bb12d34b36eec7866589b6ea785e` (2026-09-18, by `0.9.0_WK_NFRA_OPLGTW~2`). List every commit that
   touched `infra/aws/ec2/opal-gateway/` between it and your HEAD (`git log --oneline <deployed>..HEAD --
   infra/aws/ec2/opal-gateway`), and name EVERY change that ships, not just yours. **If anything in that list is not
   OA-t-5's and is not already released, STOP: file a BLOCKING row naming each commit.** Shipping another project's
   unreleased gateway change under this order is not yours to decide.
2. **Rollback, named before the act:** the prior artifact (the S3 object `deploy-to-ec2.sh` uploaded for
   `1764e54a16`, located by reading the script, never guessed) and the command that re-deploys it.
3. **NEVER-2 ledger, in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-opalai-r1-gateway-asker-query`, one leg per act
     (artifact build + upload, SSM pull + restart, manifest commit), plus the census and the rollback;
   - commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-opalai-r1-gateway-asker-query.json`;
   - ACT;
   - close every leg with its proof, and commit the close BEFORE taking the AC reads. A death between act and commit
     leaves the world changed and the record silent.
   Run `python .tools/deploy_ledger.py --help` (and each subcommand's `--help`) first for the exact grammar.

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
