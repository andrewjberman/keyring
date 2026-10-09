# NFRA_MCPORTAL task order -- `MP-x-4` -- ROUND 5, E2: the NARROW gateway release that serves the Control Plane page

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-x-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-x-4</to_id>
<issued_to>0.7.0_AE_CloudOps~MP</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the read grant is MP-x-3's, applied before this starts.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is the CTO's ruling R-13 (ROUND_ANALYSIS.round4.md @460bc0af2f).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `MP-x-4` (round 5, decomposition section R5.1; analysis R-13)

Work in a linked worktree you cut from `box/sitez` HEAD, using a NO-CONE pattern list if sparse (row NFRA_MCPORTAL-Z-W5-S2).

The gateway on `i-07dccb1615503ac99` runs the commit recorded as `services.opal-gateway.deployed_commit` in
`infra/aws/ec2/EC2_MANIFEST.json`. When this order starts, that commit is NFRA_OPLGTW's r29 release. Read it there at the act;
never assume it. Build the release on THAT live base, with ONLY:
- MP-x-1's gateway commit `06bfb80b54`: `app/admin_fabric.py` (new), the one route line in `app/admin_api.py`,
  `app/refs/fabric_boxes.json` (new) and `tests/test_admin_fabric.py` (new);
- the dashboard bundle at mcportal `d60b4e0`. That is the Control Plane page with its 60-second refresh, a LOCAL commit on
  mcportal branch `wk-NFRA_MCPORTAL-r4-6-mcportal`, in this box's shared mcportal object store.

In order:
1. **The release tree.** Run `git worktree add -b rel-nfra-mcportal-r5-control-plane <path> <live deployed_commit>`, then
   `git cherry-pick 06bfb80b54` there.
   - **Census:** `git diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY the four files above. Any other
     file: STOP with a BLOCKING row.
   - Set `EC2_MANIFEST.json` `services.opal-gateway.mcportal_commit` to `d60b4e0` on that branch, because
     `deploy-to-ec2.sh:33-60` builds the bundle from the manifest's commit.
   - Run `ops/bun_cache_precheck.py bun.lock` against d60b4e0's lockfile. A miss STOPS: no package is fetched.
2. **The load condition (R-13), measured BEFORE the cutover.** The cold `_compute(6)` measured 21.1 s from site Z with
   2,150 records.
   - Measure it ON THE HOST, before the release: over SSM, run the release's `app/admin_fabric.py` from a temp directory
     with the host venv and the instance role. MP-x-3's grant must already be applied.
   - If it takes more than 30 s (half the ALB's 60-second idle timeout): before release, narrow the handler's default window
     (6 to 2 hours) or warm the body cache at boot, in `app/admin_fabric.py` only. Re-run `tests/test_admin_fabric.py`,
     and record the change and the new time. A page whose first open can time out never ships.
3. **Rollback, proven before the act.** Rebuild the live base's artifact from a clean tree WITHOUT uploading, and name the
   command that would re-deploy it. If it cannot be shown: STOP, no deploy, a BLOCKING row.
4. **NEVER-2 ledger, on your branch, in this order.**
   - Run `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-r5-control-plane-release`. The legs are: bundle
     build, release build and upload, SSM pull and restart, manifest record. Record the census, the cold-read time, the
     rollback and this order's path.
   - Commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-r5-control-plane-release.json`.
   - ACT from the release tree with ITS scripts: `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway
     infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. Its stale-base guard must read the live ref unchanged at both reads.
   - Immediately after the restart, poll `/health`. If it is not 200 within 90 seconds, run the named rollback AT ONCE,
     close the entry as rolled back, and stop.
   - The MCP tool surface does not move. Before and after the act, list the registered tool names on the host, and
     record the two counts and their difference, which must be empty.
   - **Record the release on your branch:** in `EC2_MANIFEST.json`, `services.opal-gateway` gets the release commit as
     `deployed_commit`, the previous one as `previous_deployed_commit`, `mcportal_commit` = `d60b4e0`, and a
     `release_note`.
   - Close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` is READ, never edited.
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report. Never leave it
   half-landed.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement.
   Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/admin_fabric.py
infra/aws/ec2/opal-gateway/tests/test_admin_fabric.py
org/critical_paths/change_management/*nfra-mcportal-r5-control-plane-release*
org/critical_paths/.open_deploys/nfra-mcportal-r5-control-plane-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/`, `mcportal/`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k). `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`. Rows are
append-only.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-x-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/x4.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-x-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/x4.AC2.sh; echo "exit=$?"</invocation><expect>descends=yes; gateway app/tests files changed>=2, outside MP-x-1's set=0; mcportal_commit contains d60b4e0=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-x-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/x4.AC3.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; /api/admin/fabric/boxes (no identity)=401 or 403; compute_s<=30 reporting>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/NFRA_MCPORTAL.TO-MP-x-4.control-plane-release.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with:
- the census;
- the cold-read time, and any load change;
- the rollback;
- the tool-surface counts;
- the ledger path;
- every commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E2 of ROUND_ANALYSIS.round4.md @460bc0af2f (R-13).

**Never-widen pair (CTO+COO).** The CTO half is R-13. The COO half is this issuance. Blast radius:
- the gateway's `/` bundle;
- one new owner-gated route, `GET /api/admin/fabric/boxes`;
- no `.env` key and no IAM.

Rollback: the live base's artifact, rebuilt and proven before the act.

Checks dry-run at base, 2026-10-09 ~01:4xZ: all three FAIL.
- AC1: no entry.
- AC2: the manifest's current previous-to-deployed diff carries r28's two deploy tests, which are outside MP-x-1's set.
- AC3: the live host serves `/api/admin/fabric/boxes` 404, and `from app import admin_fabric` fails with ImportError.

**SPAWN ONLY when G-REL holds:** MP-x-3 drained, AND NFRA_OPLGTW r29 drained by `2.0.0_SA_COO~O`.

**GO (issuer, 2026-10-09 ~12:5xZ):** G-REL met.
- MP-x-3 drained @93052772a7.
- NFRA_OPLGTW r29 is LIVE on 91811b648a (`0.7.0_AE_CloudOps~Z` @5f1400c4a2, verify 5 of 5). Its ledger
  `20261009T1126Z_nfra-oplgtw-gateway-release-r29_deploy_completion.md` CLOSED 20261009T124413Z.
- The live base for step 1 is 91811b648a.
- r29 touches none of MP-x-1's four files (issuer diff, tick 5).
Was: staged

<status>pending</status>
<round>5</round>
<slot>0.7.0_AE_CloudOps~MP</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
