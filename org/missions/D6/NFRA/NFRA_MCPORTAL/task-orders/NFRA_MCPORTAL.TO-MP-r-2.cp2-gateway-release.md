# NFRA_MCPORTAL task order -- `MP-r-2` -- WORKSTREAM CP2 ROUND 1: the gateway release that serves FWD-15..17 (STAGED on G-REL2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-r-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-r-2</to_id>
<issued_to>0.7.0_AE_CloudOps~MP</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a release; no cron, alarm, monitor or cadence is added.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the read is MP-x-3's grant and the one write is MP-k-2's, both applied before this order's GO.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's narrowness census and AC3's no-identity arms are the adversary reads.
EGRESS CLASS, declared: none beyond AWS control-plane calls in Opal's own account (SSM, the artifact bucket).
</preflight>

## 1. THE CELL -- `MP-r-2` (workstream CP2 round 1, decomposition sections CP2.1, CP2.5 and CP2.6)

**Do not start before the issuer's GO message.** That GO names the gateway commits to ship and the mcportal commit. It
comes when G-REL2 holds:
- round 5's MP-x-4 is drained and live;
- MP-o-1, MP-s-1, MP-k-1 and MP-p-2 are drained (the route hookup is YOUR step 0 below, AMENDMENT 2);
- MP-k-2 is applied.

Work in a linked worktree you cut from `box/sitez` HEAD, using a NO-CONE pattern list if sparse (row NFRA_MCPORTAL-Z-W5-S2).

The gateway on `i-07dccb1615503ac99` runs the commit recorded as `services.opal-gateway.deployed_commit` in
`infra/aws/ec2/EC2_MANIFEST.json`. When this order starts, that is MP-x-4's release. Read it there at the act; never assume
it. Build the release on THAT live base, with ONLY:
- the gateway commits named in the GO:
  - `app/admin_fabric_overlap.py`, `app/refs/overlap_rules.json` and `tests/test_admin_fabric_overlap.py` (MP-o-1);
  - `app/admin_fabric_gitstate.py` and `tests/test_admin_fabric_gitstate.py` (MP-s-1);
  - `app/admin_fabric_calls.py` and `tests/test_admin_fabric_calls.py` (MP-k-1);
  - the four route lines in `app/admin_api.py` that you commit in step 0;
- the dashboard bundle at the mcportal commit named in the GO (MP-p-2's, a descendant of `d60b4e0`).

In order:
0. **The route hookup (AMENDMENT 2).** In your worktree on `box/sitez` HEAD, add to `app/admin_api.py`:
   - three imports: `from . import admin_fabric_calls`, `from . import admin_fabric_gitstate` and
     `from . import admin_fabric_overlap`, beside `from . import admin_fabric`;
   - these four lines, directly after `Route("/fabric/boxes", ...)`, verbatim:
     ```
     Route("/fabric/overlap", admin_fabric_overlap.overlap, methods=["GET"]),
     Route("/fabric/gitstate", admin_fabric_gitstate.gitstate, methods=["GET"]),
     Route("/fabric/calls", admin_fabric_calls.calls, methods=["GET"]),
     Route("/fabric/calls/close", admin_fabric_calls.close_call, methods=["POST"]),
     ```
   Then run every admin and fabric test file (`tests/test_admin*.py tests/test_entitlement_admin.py`). The issuer
   measured 58 passed with exactly these lines. Commit, and cherry-pick that commit in step 1 with the others.
1. **The release tree.** Run `git worktree add -b rel-nfra-mcportal-cp2 <path> <live deployed_commit>` and cherry-pick the
   GO's gateway commits there.
   - **Census:** `git diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY the files above. Any other file:
     STOP with a BLOCKING row.
   - Set `EC2_MANIFEST.json` `services.opal-gateway.mcportal_commit` to the GO's mcportal commit on that branch
     (`deploy-to-ec2.sh` builds the bundle from it).
   - Run `ops/bun_cache_precheck.py bun.lock` against that commit's lockfile. A miss STOPS: no package is fetched.
2. **The load condition, measured BEFORE the cutover.** Over SSM, run the release's three `_compute` functions
   (`admin_fabric_overlap._compute(6)`, `admin_fabric_gitstate._compute()`, `admin_fabric_calls._compute('open')`) from a
   temp directory, with the host venv and the instance role.
   - Any one over 30 s (half the ALB's 60-second idle timeout): STOP with a BLOCKING row naming the time. The issuer
     re-cuts.
3. **Rollback, proven before the act.** Rebuild the live base's artifact from a clean tree WITHOUT uploading, and name the
   command that would re-deploy it. If it cannot be shown: STOP, no deploy, a BLOCKING row.
4. **NEVER-2 ledger, on your branch, in this order.**
   - Run `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-cp2-release`. The legs are: bundle build,
     release build and upload, SSM pull and restart, manifest record. Write the census, the three times, the rollback and this order's path to
     `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-r-2_PRE_ACT_RECORD.md`, and put ONE pointer
     line to it in the entry (AMENDMENT 4: `deploy_ledger.py hold` and `close-leg` regenerate the entry and drop appended
     prose, rows Z-S24 and Z-S25).
   - Commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-cp2-release.json`.
   - ACT from the release tree with ITS scripts: `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway
     infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. Its stale-base guard must read the live ref unchanged at both reads.
   - Immediately after the restart, poll `/health`. If it is not 200 within 90 seconds, run the named rollback AT ONCE,
     close the entry as rolled back, and stop.
   - The MCP tool surface does not move. Before and after the act, list the registered tool names on the host and record
     the two counts and their difference, which must be empty.
   - **Record the release on your branch:** in `EC2_MANIFEST.json`, `services.opal-gateway` gets the release commit as
     `deployed_commit`, the previous one as `previous_deployed_commit`, the GO's mcportal commit as `mcportal_commit`,
     and a `release_note`.
   - Close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` is READ, never edited. No
   handler is edited in this cell. A load-condition failure stops it, it does not tune.
2. Make no live POST to `/api/admin/fabric/calls/close`: the one real close is Andrew's, in MP-q-1.
3. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report. Never leave it
   half-landed.
4. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement.
   Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/admin_api.py
org/critical_paths/change_management/*nfra-mcportal-cp2-release*
org/critical_paths/.open_deploys/nfra-mcportal-cp2-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/` (except `app/admin_api.py`, step 0), `mcportal/`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`. Rows are append-only.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-r-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/r2.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-r-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/r2.AC2.sh; echo "exit=$?"</invocation><expect>descends=yes; gateway app/tests files changed>=4, outside CP2's set=0; contains d60b4e0=yes, has src/pages/open-calls=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-r-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/r2.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; /health=200; no-identity overlap, gitstate, calls, close(POST) each 401 or 403; overlap deploys_read>=1, recorded>=1, published>=1, each <=30 s -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/NFRA_MCPORTAL.TO-MP-r-2.cp2-gateway-release.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with:
- the census;
- the three cold times;
- the tool-surface counts;
- the three check outputs;
- the ledger entry path and its CLOSED state;
- every commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the CP2 issuance (decomposition v6; row Z-S19: every cell of a round is cut in its one issuance).
G-REL2 is the issuer's to read. MP-x-4's own gate is G-REL (NFRA_OPLGTW r29 deployed: Phase A merged @76ff10095c, msg 32482;
Phase B waits on the CVO~Z half). Checks dry-run at base 2851a9190d: AC1 FAIL (no entry), AC2 FAIL (live manifest = r28,
mcportal a3bff71 lacks d60b4e0), AC3 FAIL against the live r28 host (ssm 56a9dedd: /health=200 control; the four routes 404;
`cannot import name 'admin_fabric_overlap'`). The first AC3 dry run (ssm d4b2c3ed) exposed a probe defect (`No module named
'app'`: the probe ran from /tmp); fixed with PYTHONPATH before the cut. GO by message, the applier being a seat.

**AMENDMENT 2 (issuer, while staged):** the route hookup moves into this order as step 0, and `app/admin_api.py` joins
`<paths>`. The issuer's own hookup commit was REFUSED by the owned-paths gate: `infra/aws/ec2/opal-gateway/app/admin_api.py`
is lane CLOUD_OPS_OR_ETL, and 2.0.0_SA_COO~MP holds no grant there. This order's assignee does. The four lines were
measured by the issuer, uncommitted: routes 4 of 4, admin and fabric test files 58 passed. See decomposition CP2.10.

**AMENDMENT 4 (issuer, 2026-10-09 ~14:5xZ, disarming row Z-S24 by row Z-S25):** the pre-act record goes to a deliverables
file, and the ledger entry carries only a pointer. `deploy_ledger.py` regenerates the entry on hold and close-leg, and
silently drops appended prose (MP-x-4's entry went from 137 to 23 lines at rc=0). The drain reads the deliverables file.

<status>staged</status>
<round>1</round>
<workstream>CP2</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
