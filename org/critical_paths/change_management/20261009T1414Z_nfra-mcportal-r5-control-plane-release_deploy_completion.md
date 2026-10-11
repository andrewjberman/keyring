# Deploy Completion Record
**Date opened:** 2026-10-09T14:14:25.738253+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T162737Z
**Deploy:** NFRA_MCPORTAL MP-x-4 (round 5, E2): the narrow gateway release that serves the Control Plane page -- MP-x-1's four files onto the live r29 base, dashboard bundle mcportal d60b4e0
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | bundle build: mcportal d60b4e0 built by deploy-to-ec2.sh from EC2_MANIFEST.json services.opal-gateway.mcportal_commit (never the checkout's HEAD); bun cache pre-check must pass so no package is fetched | pre-check 77 of 77 rc=0 against d60b4e0's own bun.lock; INFO: building mcportal @ d60b4e0 then dist/index.html present | BUNDLE BUILT from the MANIFEST's commit, not a checkout HEAD. deploy-to-ec2.sh:33-60 resolved mcportal_commit=d60b4e0 from EC2_MANIFEST.json and printed 'INFO: building mcportal @ d60b4e0'. bun cache pre-check ran first in the same subshell: 77 of 77, rc=0, against d60b4e0's own bun.lock (30903 bytes, lockfileVersion 1, extracted by git show), so NO package was fetched from the internet. Verified ON THE HOST after the act: /opt/opal-gateway/dashboard/index.html present. d60b4e0 verified beforehand as a real commit in this box's mcportal store (branch wk-NFRA_MCPORTAL-r4-6-mcportal). | CLOSED 20261009T162513Z |
| L2 | s3-prefix | release build and upload: artifact opal-gateway-<sha>.tar.gz to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ with git-ref metadata, + latest | head-object ContentLength/ETag and Metadata.git-ref == the release sha | RELEASE BUILT AND UPLOADED. s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-1e32562729.tar.gz -- head-object: ContentLength 518165, ETag b96315a523842ec46579b146c450faa9, Metadata.git-ref 1e32562729495695c6addaed05f047e46090776f (equal to the release commit), LastModified 2026-10-09T16:11:31Z. opal-gateway-latest.tar.gz now carries the SAME size, ETag and git-ref, i.e. latest moved to this release -- which is why the rollback names the VERSIONED key. ROLLBACK TARGET SURVIVED THE ACT, measured after it: opal-gateway-c97232408d.tar.gz still present at 514278 bytes, ETag 16c5f801b546836ddf577696c69d597d, git-ref c97232408d..., DISTINCT from latest. The stale-base guard refused the first invocation outright (DEPLOY_BASE_REF unset -> 'ERROR: REFUSED (no upload)', rc=1, nothing uploaded); the act ran with DEPLOY_BASE_REF=c97232408d72bc649c92da7e4e711c0ebf0a3950. | CLOSED 20261009T162514Z |
| L3 | activation | SSM pull and restart on i-07dccb1615503ac99, then /health 200 within 90 s or the named rollback runs AT ONCE | ssm:<command_id> Status=Success; /health=200; MainPID moves off 857046 | SSM PULL + RESTART, and /health 200 well inside the 90 s bar so the named rollback was NOT run. Deploy rc=0 with its own read-back 'OK: opal-gateway active' / {"ok":true} / 'OK: AS metadata serves' / '/mcp unauth -> 401 (expect 401)'. NOT taken from that rc: an INDEPENDENT SSM read afterwards (command a356c9bf-5140-48e0-8c6a-b205dcd47a3d, Status=Success) measured SERVICE_ACTIVE=active, HEALTH_CODE=200, HEALTH_BODY={"ok":true} on 127.0.0.1:8080, and MainPID 862375 -> 864717 so the restart demonstrably happened. CODE CURRENCY by CONTENT, not filename (CLAUDE.md 22a CODE layer): deployed /opt/opal-gateway/app/admin_fabric.py md5 caa21f671e60c21e4b0a77c566c18149 EQUALS the release module's local md5, and app/refs/fabric_boxes.json is present -- both were ABSENT live on three separate pre-act reads. OG-tl-1 PRESERVED: .env TRANSCRIPT_MEETING_ALLOWLIST still non-empty (grep count 1) before and after, and the script's ENV_KEYS_BEFORE/AFTER lists are identical at 52 keys. | CLOSED 20261009T162619Z |
| L4 | verify | manifest record + MCP tool surface unmoved + the three ACs | EC2_MANIFEST deployed_commit=<release sha>, previous_deployed_commit=91811b648a, mcportal_commit=d60b4e0; tools 66 -> 66 difference empty; AC1/AC2/AC3 PASS | MANIFEST RECORDED on the trunk branch wk-mcportal-r5-x4 (the release branch is never merged AND its auto-record carries previous_deployed_commit=2c0f84966d, the stale value its own tree held -- wrong, and corrected here): deployed_commit=1e32562729495695c6addaed05f047e46090776f, previous_deployed_commit=c97232408d72bc649c92da7e4e711c0ebf0a3950, mcportal_commit=d60b4e0, plus deployed_at/deployed_by and a release_note; 6 lines changed, and a guard refused to write unless the trunk's pre-act deployed_commit read c97232408d. MCP TOOL SURFACE UNMOVED: 66 before, 66 after, name-for-name, 0 added and 0 removed -- the DIFFERENCE IS EMPTY as the order requires. Both counts were read from the live in-process registry (app/server.py:507 mcp._tool_manager.list_tools()) via the S3->host path, printing names and the count only, never an env value. NEW ROUTE LIVE AND GATED: GET /api/admin/fabric/boxes with no identity returns 401 {"error":"no verified identity"}. AC1/AC2/AC3 are run AFTER this close is committed, per the order. | CLOSED 20261009T162619Z |

## Log

- 20261009T141425Z OPENED by 0.7.0_AE_CloudOps~MP with 4 leg(s)
- 20261009T142243Z HELD-PRE-APPLY gate=external/NFRA_OPLGTW OG-ap-4 (env-only 4-meeting allowlist, all halves signed) ledger CLO
- 20261009T160116Z HOLD RELEASED -> OPEN
- 20261009T162513Z LEG L1 closed: BUNDLE BUILT from the MANIFEST's commit, not a checkout HEAD. deploy-to-ec2.sh:33-60 resolved mcportal_commit=d60b4e0 fr
- 20261009T162514Z LEG L2 closed: RELEASE BUILT AND UPLOADED. s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-1e32562729.tar.gz -- h
- 20261009T162619Z LEG L3 closed: SSM PULL + RESTART, and /health 200 well inside the 90 s bar so the named rollback was NOT run. Deploy rc=0 with its own
- 20261009T162619Z LEG L4 closed: MANIFEST RECORDED on the trunk branch wk-mcportal-r5-x4 (the release branch is never merged AND its auto-record carries 
- 20261009T162737Z CLOSED -- all 4 legs proven

## PRE-ACT RECORD -- POINTER (this file is regenerated by the tool; the record is NOT kept here)

Steps 1-3 are recorded in full at
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-x-4_PRE_ACT_RECORD.md`:
the census (MP-x-1 four files, 0 outside the gateway scope), FOUR cold `_compute(6)` samples
(16.767 / 15.336 / 13.964 / 13.615 s against the 30 s bar, 1.79x headroom at the worst, no load change
made), the CONTENT-verified rollback (`opal-gateway-91811b648a.tar.gz`, local md5 == S3 ETag
`3157ad0796dae6f9ad26dea7a1e46469`, 0 occurrences of `app/admin_fabric.py`), the halt-gate pre-flight
(rc=0 from the release worktree) and the MCP tool surface BEFORE (66).

A pointer rather than the record, because `deploy_ledger.py hold` regenerated this entry and dropped
115 lines of appended prose at `b8fc617e2e`, rc=0 and silently (row `NFRA_MCPORTAL-Z-S24`). If this
pointer is dropped by a later `close`, the record is still at that path and in `ca9b6c05f0`.
