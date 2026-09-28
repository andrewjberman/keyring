# NFRA_MCPINDEX task order -- `MX-r-3` -- ROUND 2, E3's release: the NARROW gateway release, shipped DORMANT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the host, its role and Terraform are untouched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is ruled (R-8; the @592e319a06 precedent).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `MX-r-3` (round 2, decomposition section R2.1)

CLOUD now carries this project's gateway work, drained from the held branch:
- MX-c-4's build: classification composes from each integration's declaration, and `read_teams_attachment` becomes SAFE;
- MX-c-5's 9 classes;
- the new integrations `opal_discover` (MX-d-2) and `portal_index` (MX-t-8);
- the routing harness (MX-v-6).

The CTO's ruling R-8 (`org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round1.md`, READ IT): **every gateway
release is NARROW, cut at the deployed commit plus this project's own changes.** Read the deployed commit from
`infra/aws/ec2/EC2_MANIFEST.json` (`services.opal-gateway.deployed_commit`) at YOUR cut; never assume it.

In order:
1. **Name this project's commits.** They are the commits on CLOUD touching `infra/aws/ec2/opal-gateway` whose author
   is `0.9.0_WK_NFRA_MCPINDEX~<n>`. List them, oldest first.
2. **The release tree.**
   - `git worktree add -b rel-nfra-mcpindex-r2-gateway /c/tmp/mx-rel <deployed_commit>`, then
     `git -C /c/tmp/mx-rel cherry-pick --no-commit` those commits in order, and commit under your serial.
   - **Census:** `git -C /c/tmp/mx-rel diff --stat <deployed_commit> HEAD -- infra/aws/ec2/opal-gateway` names ONLY files
     those commits changed. Anything else: STOP, a BLOCKING row.
   - **The issuer authorizes the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_MCPINDEX~1`** for exactly the
     release-branch commit(s). Name each use.
3. **Dormant:** the host `.env`'s `ENABLED_INTEGRATIONS` is NOT changed. The new integrations ship and add zero tools
   until Andrew's word (G-A).
4. **Rollback proven before the act:** rebuild `<deployed_commit>`'s artifact from a clean tree WITHOUT uploading, and
   name the re-deploy command. If it cannot be shown: STOP.
5. **NEVER-2 ledger, on THIS branch, in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcpindex-r2-gateway-release`;
   - commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcpindex-r2-gateway-release.json`;
   - ACT from the RELEASE worktree with ITS scripts:
     `cd /c/tmp/mx-rel && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
     Its Step-3 manifest auto-commit can fail on this device (jq CRLF; row NFRA_OPALAI-Z-W2-S4). Read its ERROR line,
     then record by hand on an LF copy;
   - **record on THIS branch:** `EC2_MANIFEST.json` `services.opal-gateway` gets the release commit as `deployed_commit`,
     the commit you cut from as `previous_deployed_commit`, and a `release_note` naming the other projects' gateway
     commits CLOUD holds UNRELEASED;
   - close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` and `deploy-to-ec2.sh` are
   READ, never edited.
2. If a leg fails mid-act: roll back with the named command, close the entry as rolled back, and report. Never
   half-landed.
3. Standing: the interpreter is `python`; no push, no vendor call. REFUSE a criterion you cannot meet as written, and
   report the refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not
   name.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r2-gateway-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_MCPINDEX-Z-W1-S<k>`, fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-r-3"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/r3.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-3"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/r3.AC2.sh; echo "exit=$?"</invocation><expect>descends=yes; gateway files shipped>=1, outside NFRA_MCPINDEX's set 0; new integrations carried 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-3"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/r3.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; /health=200; new integrations shipped 2 of 2; new ones enabled=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~1/NFRA_MCPINDEX.TO-MX-r-3.narrow-release.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once:
- the census, and the commits named unreleased;
- the rollback;
- the ledger path;
- each override use;
- the commit hashes;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** R-8 release. Never-widen (CTO+COO):
- The CTO half is R-8 plus D-3's "releases NARROW".
- The COO half is this issuance. Blast radius: `read_teams_attachment` becomes SAFE (AC8, graded by the CVO before the
  drain), the 9 new classes, and two DORMANT integrations. Rollback: the prior deployed artifact.

SPAWN ONLY after:
- the CVO has graded MX-c-5's AC4;
- the held branch has drained to CLOUD;
- no other project's gateway release is mid-act (read `.open_deploys/` across every live worktree).

<status>pending</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

<status>complete</status>
<!-- flipped by the issuer 2026-09-27T06:0xZ after the drain @857050f815. AC1/AC2/AC3 re-run on CLOUD: PASS exit=0 each
     (AC3 ssm 3095c5bb, /health=200, new integrations enabled=0). Instance VALID (rc=0). opal-gateway serves 110d93fb73
     since 05:03:34Z. Pre-upload conditions both held: ENABLED_INTEGRATIONS literal read before the upload; the ledger's
     L1 line reads 'building mcportal @ a3bff71ffa'. -->
