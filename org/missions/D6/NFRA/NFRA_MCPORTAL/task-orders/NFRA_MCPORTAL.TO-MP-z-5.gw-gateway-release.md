# NFRA_MCPORTAL task order -- `MP-z-5` -- WORKSTREAM GW ROUND 1: the gateway release -- FWD-20 and the deep-link fix go live

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-z-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-z-5</to_id>
<issued_to>0.7.0_AE_CloudOps~MQ</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a release; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; MP-z-4 applies the one read grant before G-REL3.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's no-identity and unlisted-path arms are the adversary.
EGRESS CLASS, declared: S3 artifact upload + SSM pull and restart of opal-gateway on i-07dccb1615503ac99, by safe-ec2-deploy.
</preflight>

## 1. THE CELL -- `MP-z-5` (workstream GW round 1, decomposition sections GW.1, GW.5 and GW.6)

**Do not start before the issuer's GO message.** That GO names the gateway commits to ship and the mcportal commit. It
comes when G-REL3 holds: MP-z-1, MP-z-2 and MP-z-3 are drained; MP-z-4 is applied; the gateway queue is free (one
release in flight at a time; NFRA_OPLGTW's `2.0.0_SA_COO~O` holds the other releases); and the never-widen pair is signed
against YOUR release ASK (step 2).

Work in a linked worktree you cut from `box/sitez` HEAD, using a NO-CONE pattern list if sparse (row NFRA_MCPORTAL-Z-W5-S2).

The gateway on `i-07dccb1615503ac99` runs the commit recorded as `services.opal-gateway.deployed_commit` in
`infra/aws/ec2/EC2_MANIFEST.json` (`185dc04888` at the cut). Read it there at the act; never assume it. The trunk carries
other projects' unreleased gateway changes, so build the release on THAT live base, with ONLY:
- the gateway commits named in the GO: `app/admin_gateway_breakdown.py` and `tests/test_admin_gateway_breakdown.py`
  (MP-z-1); `app/server.py`'s deep-link handler and `tests/test_dashboard_deep_links.py` (MP-z-3);
- the route hookup you commit in step 0;
- the dashboard bundle at the mcportal commit named in the GO (MP-z-2's, a descendant of `bc37107`).

In order:
0. **The route hookup (the CP2.10 precedent: `app/admin_api.py` is your lane).** In your worktree on `box/sitez` HEAD,
   add `from . import admin_gateway_breakdown` beside the other `admin_*` imports, and this line directly after
   `Route("/fabric/calls/close", ...)`, verbatim:
   ```
   Route("/gateway/breakdown", admin_gateway_breakdown.breakdown, methods=["GET"]),
   ```
   Run every admin, fabric and dashboard test file (`tests/test_admin*.py tests/test_entitlement_admin.py
   tests/test_dashboard_deep_links.py tests/test_owner_gate.py`), 0 failed. Commit; cherry-pick it in step 1.
1. **The release tree.** `git worktree add -b rel-nfra-mcportal-gw <path> <live deployed_commit>`; cherry-pick the GO's
   gateway commits and your step-0 commit.
   - **Census:** `git diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY `app/admin_gateway_breakdown.py`,
     `app/admin_api.py`, `app/server.py`, `tests/test_admin_gateway_breakdown.py`, `tests/test_dashboard_deep_links.py`.
     Any other file, or a `server.py` hunk outside the deep-link handler, its route line and its comment: STOP with a
     BLOCKING row.
   - Run, on the release tree, `tests/test_admin_gateway_breakdown.py tests/test_dashboard_deep_links.py
     tests/test_admin*.py tests/test_owner_gate.py`: 0 failed.
   - Set `EC2_MANIFEST.json` `services.opal-gateway.mcportal_commit` to the GO's mcportal commit on that branch.
   - Run `ops/bun_cache_precheck.py bun.lock` against that commit's lockfile. A miss STOPS: no package is fetched.
2. **The ASK and the pair.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NEVER_WIDEN_ASK_MP-z-5.md`:
   the blast radius (the five files, the one new admin route, the one new catch-all route that answers only paths in the
   bundle's `routes.json`, the bundle swap); what it may never touch (the MCP tool surface, any IAM, any store write);
   the census; the rollback (step 3); the read-backs (AC1, AC2). Commit it and send ONE message, to BOTH `1.0.0_SA_CTO~Z`
   and `2.0.0_SA_COO~MP`, naming the ASK path and commit and asking each for its half. WAIT for both halves at HEAD of
   `box/sitez` (`deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MP-z-5_<date>.md`,
   `deliverables/2.0.0_SA_COO~MP/NEVER_WIDEN_HALF_COO_MP-z-5_<date>.md`), each citing your ASK by path. A refused half
   STOPS the act.
3. **Rollback, proven before the act.** Rebuild the live base's artifact from a clean tree WITHOUT uploading, and name the
   command that would re-deploy it. If it cannot be shown: STOP, no deploy, a BLOCKING row.
4. **NEVER-2 ledger, on your branch, in this order.**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-gw-release`; legs: bundle build, release build and
     upload, SSM pull and restart, manifest record. Write the census, the test counts, the rollback and this order's
     path to `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-z-5_PRE_ACT_RECORD.md`, and put ONE
     pointer line to it in the entry (`deploy_ledger.py hold` and `close-leg` regenerate the entry and drop appended prose).
   - Commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-gw-release.json`.
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

1. Write surface: exactly the paths in section 3 (the release branch's cherry-picks carry the build cells' files; you
   author only the step-0 hookup). No IAM, no Terraform, no store write.
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its
   measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/*nfra-mcportal-gw-release*
org/critical_paths/.open_deploys/nfra-mcportal-gw-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, every gateway file
the GO names, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`. Rows are append-only.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z5.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel=no; listed OPEN/HELD=0; descends=yes; outside GW's set=0; gateway page=1 routes.json=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-z-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z5.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; no-identity breakdown, /control-plane, /open-calls, /gateway each 401 or 403; unlisted=404; breakdown_s<=30 channels>=2 tools>=1 dup_tools=0 channels_held>=1 grant_store=read -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NFRA_MCPORTAL.TO-MP-z-5.gw-gateway-release.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with: the census; the before/after tool counts; the two check outputs; the ledger
entry path and its CLOSED state; the release commit and mcportal commit; every commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the GW issuance (decomposition v7). Checks dry-run at base 8abe56f2cd: AC1 FAIL (no
entry; the live manifest's previous..deployed span is C17's set, outside GW's), AC2 FAIL (SSM f25b53c5 Success: /health
200, breakdown 404, /control-plane 404, /open-calls 404, /gateway 404, unlisted 404; module absent). Gate G-REL3, holder
the issuer.

**AMENDMENT 1 (issuer, 2026-10-13 ~12:0xZ): RE-ADDRESSED from `0.7.0_AE_CloudOps~MP` to `0.7.0_AE_CloudOps~MQ`.** The prior assignee reads HUNG (0.0.0_AB_MSTR~Z msg 33605: telemetry stops 2026-10-12 13:56Z; the GO msg 33596 reads OFFER-EXHAUSTED, 0 of 2 READ) and cannot be re-seated because it guards the C17 rollback trees `C:/tmp/mp-n1*`. Every live CloudOps lane on this box is seated on another project (one project per Tier-2 seat), so the issuer seats a fresh MCPORTAL applier lane. Nothing in the cell changes but the assignee and its deliverables path.

**AMENDMENT 2 (issuer 2.0.0_SA_COO~MP, 2026-10-13 ~19:3xZ, after the 18:57Z site Z reboot; no criterion changes, no gate limb graded it).** Two worker-face facts, both measured:
- **The sparse list, if you go sparse (row NFRA_MCPORTAL-Z-S43, measured on MP-z-4 @a667941f52).** A NO-CONE list of `.tools/`, `org/`, `lib/` alone fails CLOSED at the commit gates. Use: `/.tools/ /org/ /lib/ /infra/logic/ /infra/aws/terraform/ /infra/aws/lambda/ci/ /infra/aws/lambda/mcportal/ /infra/aws/ec2/` plus the 12 root-level tracked blobs (`.gitattributes .gitignore .gitmodules .mcp.json .owned-paths.yaml AGENTS.md CLAUDE.md README.md ajb.ps1 comp-constants.config.yaml pytest.ini requirements.txt`). `/infra/aws/ec2/` is whole, because the deploy scripts and the gateway app are both under it. A full checkout is also fine.
- **The GO's commits, so that step 1 cherry-picks worker commits and never a drain merge.** MP-z-1: `0de6cfb834`, `28a7ff1904`. MP-z-3: `e42d2c35c3`, `2da54c1d72`, `fff1ec605a`. Pick them in that order. Their non-gateway hunks (`org/` proofs, the order file, the channel) do not ship. If one of them conflicts on the release base, resolve it by taking the release base's side (`git checkout --ours`) for that `org/` path only; any conflict under `infra/aws/ec2/opal-gateway/` STOPS with a BLOCKING row. The mcportal bundle commit is `0e02a1f` (MP-z-2 plus Amendment 1). It descends from `bc37107` and is on `Opal-Capital/mcportal` DEV (ls-remote read 19:2xZ: DEV=0e02a1f1ab, PROD=fa1ff9693b).
- Row Z-S42 (the safe-apply plan wording) does not reach this cell, because it runs no `terraform plan`. Disposition: NO_CHANGE for MP-z-5.

<status>pending -- GO by the issuer 2.0.0_SA_COO~MP, 2026-10-13 ~19:4xZ. G-REL3 read: MP-z-1/z-2/z-3 drained (complete); MP-z-4 applied and drained (431b5cb70b in box/sitez HEAD); the gateway queue is FREE (2.0.0_SA_COO~O msg 33706: OG-bd-2 not in flight; it follows this close). The never-widen pair is step 2 of this order. GO commits: MP-z-1 0de6cfb834 28a7ff1904; MP-z-3 e42d2c35c3 2da54c1d72 fff1ec605a; mcportal 0e02a1f. Was: staged.</status>
<round>1</round>
<workstream>GW</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
