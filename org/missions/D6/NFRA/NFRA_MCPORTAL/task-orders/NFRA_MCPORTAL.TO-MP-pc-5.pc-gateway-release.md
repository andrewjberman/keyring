# NFRA_MCPORTAL task order -- `MP-pc-5` -- WORKSTREAM PC ROUND 1: the gateway release -- the People view and the three refusal states go live

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pc-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pc-5</to_id>
<issued_to>0.7.0_AE_CloudOps~MQ</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a release; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the grant-store Scan the People view reuses is MP-z-4's grant, already applied.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's no-identity arms and its three-state limb are the adversary.
EGRESS CLASS, declared: S3 artifact upload + SSM pull and restart of opal-gateway on i-07dccb1615503ac99, by safe-ec2-deploy.
</preflight>

## 1. THE CELL -- `MP-pc-5` (workstream PC round 1, decomposition sections PC.1, PC.4 and PC.5)

**Do not start before the issuer's GO message.** The GO names the gateway commits to ship and the mcportal commit. It
comes when G-REL5 holds:
- MP-pc-1, MP-pc-2 and MP-pc-3 are drained;
- the gateway queue is free (one release in flight at a time; today NFRA_OPLGTW r30, the tier-admission fix and OG-mg-1
  are ahead of this release);
- the never-widen pair is signed against YOUR release ASK (step 2).

**Your worktree.** Cut it from `box/sitez` HEAD. If you go sparse, use a NO-CONE pattern list and pass it on STDIN
(`git sparse-checkout set --no-cone --stdin`), never as argv, because Git Bash rewrites `/`-leading argv into
`C:/Program Files/Git/...` and the cone silently comes up empty (row Z-S44). The list:
- `/.tools/ /org/ /lib/ /infra/logic/ /infra/aws/terraform/ /infra/aws/lambda/ci/ /infra/aws/lambda/mcportal/`
  `/infra/aws/ec2/ /data/transcripts/scripts/teams/`;
- the 12 root-level tracked blobs: `.gitattributes .gitignore .gitmodules .mcp.json .owned-paths.yaml AGENTS.md
  CLAUDE.md README.md ajb.ps1 comp-constants.config.yaml pytest.ini requirements.txt`.

`/infra/logic/` carries `infra/logic/registry`, which every deploy cell needs (the five recipe rows, C17 round-2 analysis
ruling 5). `/data/transcripts/scripts/teams/` is read by `deploy-to-ec2.sh` (row Z-S46). A full checkout also works.

The gateway on `i-07dccb1615503ac99` runs the commit recorded as `services.opal-gateway.deployed_commit` in
`infra/aws/ec2/EC2_MANIFEST.json`. Read it there at the act; never assume it. The trunk carries other projects'
unreleased gateway changes, so build the release on THAT live base, with ONLY:
- the gateway commits named in the GO: `app/admin_fabric_gitstate.py` and its test (MP-pc-1), `app/admin_people.py` and
  its test (MP-pc-2);
- the route hookup you commit in step 0;
- the dashboard bundle at the mcportal commit named in the GO (MP-pc-3's, a descendant of `0e02a1f`).

In order:
0. **The route hookup (the CP2.10 precedent: `app/admin_api.py` is your lane).** In your worktree on `box/sitez` HEAD,
   add `from . import admin_people` beside the other `admin_*` imports, and this line directly after
   `Route("/gateway/breakdown", ...)`, verbatim:
   ```
   Route("/people", admin_people.people, methods=["GET"]),
   ```
   Run `tests/test_admin*.py tests/test_owner_gate.py` there: 0 failed. Commit, then cherry-pick it in step 1.
1. **The release tree.** `git worktree add -b rel-nfra-mcportal-pc <path> <live deployed_commit>`. Cherry-pick the GO's
   WORKER commits in the GO's order, then your step-0 commit. If a pick's `org/` path conflicts, take the release base's
   side for that `org/` path only (`git checkout --ours`). Any conflict under `infra/aws/ec2/opal-gateway/` STOPS with a
   BLOCKING row. If the owned-paths hook refuses a pick's author, re-author it to your lane and name the source commit in
   the message.
   - **Census:** `git diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY `app/admin_fabric_gitstate.py`,
     `app/admin_people.py`, `app/admin_api.py`, `tests/test_admin_fabric_gitstate.py` and `tests/test_admin_people.py`.
     Any other file STOPS with a BLOCKING row.
   - **Tests:** run `tests/test_admin_fabric_gitstate.py tests/test_admin_people.py tests/test_admin*.py
     tests/test_owner_gate.py` on `box/sitez` HEAD with the payload: 0 failed. Then run them on the release tree. There,
     a test may fail ONLY if its failure is `FileNotFoundError` on a repo path outside `infra/aws/ec2/opal-gateway/` whose
     `git ls-tree` reads 0 at the live base AND 1 at HEAD, and the same test passes at HEAD. A release tree's `org/` is
     frozen at the release chain's vintage (row Z-S45). List each such test id with its path and both counts in the ASK.
     Any other failure STOPS.
   - Set `EC2_MANIFEST.json` `services.opal-gateway.mcportal_commit` to the GO's mcportal commit on that branch.
   - Run `ops/bun_cache_precheck.py bun.lock` against that commit's lockfile. A miss STOPS: no package is fetched.
2. **The ASK and the pair.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NEVER_WIDEN_ASK_MP-pc-5.md`
   with:
   - the blast radius: the five files, the one new admin route, the `/people` deep link (served by the existing
     catch-all from the bundle's `routes.json`), the gitstate shape change (PC.2), and the bundle swap;
   - what it may never touch: the MCP tool surface, any IAM, any store write;
   - the census, the tests, and the rollback (step 3);
   - the read-backs: AC1, AC2.

   Commit it, then send ONE message, to BOTH `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~MP`, naming the ASK path and commit and
   asking each for its half. WAIT for both halves at HEAD of `box/sitez`
   (`deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MP-pc-5_<date>.md`,
   `deliverables/2.0.0_SA_COO~MP/NEVER_WIDEN_HALF_COO_MP-pc-5_<date>.md`), each citing your ASK by path. A refused half
   STOPS the act.
3. **Rollback, proven before the act.** Rebuild the live base's artifact from a clean tree WITHOUT uploading. Compare it to
   the live artifact by md5 per member, with a negative control against the release tree. Name the command that would
   re-deploy it. **Also measure the rollback TIME (row Z-W2-S8, unmeasured since 2026-09-25):** run the named rollback's
   build and the host's pull-and-restart steps against the CURRENT live artifact as a no-op rehearsal if the deploy
   scripts allow one; otherwise time the release's own pull-and-restart in step 4 and record it as the bound. Record
   which, and the seconds. If the rollback cannot be shown: STOP, no deploy, a BLOCKING row.
4. **NEVER-2 ledger, on your branch, in this order.**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-pc-release`. Legs: bundle build, release build
     and upload, SSM pull and restart, manifest record. Write the census, the test results, the rollback and its time,
     and this order's path to `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-pc-5_PRE_ACT_RECORD.md`,
     and put ONE pointer line to it in the entry.
   - Commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-pc-release.json`.
   - ACT from the release tree with ITS scripts: `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway
     infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. Its stale-base guard must read the live ref unchanged at both reads.
   - Immediately after the restart, poll `/health`. If it is not 200 within 90 seconds, run the named rollback AT ONCE,
     close the entry as rolled back, and stop.
   - The MCP tool surface does not move. Before and after the act, list the registered tool names on the host and record
     the two counts and their difference, which must be empty.
   - **Record the release on your branch:** in `EC2_MANIFEST.json`, `services.opal-gateway` gets the release commit as
     `deployed_commit`, the previous one as `previous_deployed_commit`, the GO's mcportal commit as `mcportal_commit`, and
     a `release_note`. The wrapper writes a stale `previous_deployed_commit` from the tree's own vintage; correct it.
   - Close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. The release branch's cherry-picks carry the build cells' files; you
   author only the step-0 hookup. No IAM, no Terraform, no store write.
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement.
   Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/*nfra-mcportal-pc-release*
org/critical_paths/.open_deploys/nfra-mcportal-pc-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, every gateway file
the GO names, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pc-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/pc5.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel=no; listed OPEN/HELD=0; descends=yes; outside PC's set=0; people page=1 routes.json lists /people=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pc-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/pc5.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; no-identity people and /people each 401 or 403; people_s<=30 persons>=2 population=1 tools>=1 cadence_absent=tools grant_store=read; refused_states holds "no" and at least two states -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NFRA_MCPORTAL.TO-MP-pc-5.pc-gateway-release.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with:
- the census;
- the before/after tool counts;
- the two check outputs;
- the rollback time, and how it was measured;
- the ledger entry path and its CLOSED state;
- the release commit and the mcportal commit;
- every commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the PC issuance (decomposition v9). Every lesson of MP-z-5 and MP-n-4 is baked in at the
cut:
- the sparse list (Z-S43), passed on stdin (Z-S44), with the teams path (Z-S46);
- the release-tree test rule (Z-S45 / MP-n-4 A1);
- the `import app.server` probe (Z-S48);
- `infra/logic/registry` (analysis ruling 5);
- Z-W2-S8's rollback time (analysis ruling 2).

Checks dry-run at base 9be88c9134:
- AC1 FAIL (people page=0; routes.json does not list /people; no entry).
- AC2 FAIL (SSM cd49eb5f Success: /health 200, people 404, /people 404, `ImportError: cannot import name 'admin_people'`).

Gate G-REL5, holder the issuer.

<status>complete</status>
<round>1</round>
<workstream>PC</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
