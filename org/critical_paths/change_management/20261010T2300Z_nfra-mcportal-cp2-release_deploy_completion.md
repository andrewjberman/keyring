# Deploy Completion Record
**Date opened:** 2026-10-10T23:00:22.588125+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261010T231237Z
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-r-2: the CP2 gateway release (overlap, gitstate, calls + the A5 load remedy) on live base d3c31e972e
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

**PRE-ACT RECORD (the full census, the base-by-md5 read and its control, the cold samples with their population, the rollback proof and the tool surface -- AMENDMENT 4: re-added after `close` regenerated this entry and dropped it, rows Z-S24/Z-S25):** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-r-2_PRE_ACT_RECORD.md` on branch `rel-nfra-mcportal-cp2-v2`
**PRE-ACT RECORD (the full census, times, rollback proof and tool surface -- AMENDMENT 4; this entry carries only this pointer because `deploy_ledger.py` regenerates the entry and drops appended prose, rows Z-S24/Z-S25):** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-r-2_PRE_ACT_RECORD.md` on branch `rel-nfra-mcportal-cp2-v2`

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | bundle build: mcportal bc37107 dashboard built by deploy-to-ec2.sh from the manifest pin | build log + bun pre-check 77 of 77 | Bundle built by deploy-to-ec2.sh from the MANIFEST pin mcportal_commit=bc37107 (MP-p-2, descendant of d60b4e0), never a checkout HEAD. Bun cache pre-check against bc37107's own lockfile: 77 of 77 present, rc=0, so no package was fetched. Dashboard present on the host after the act: assets, index.html (ls of /opt/opal-gateway/dashboard). | CLOSED 20261010T231237Z |
| L2 | s3-prefix | release build + upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway | head-object len/ETag/git-ref on the versioned key AND -latest | head-object read-backs, independent of the deploy rc: VERSIONED key ec2/opal-gateway/opal-gateway-2a5966dfbd.tar.gz EXISTS, 535420 B, ETag 8a06aaa1ee91460aa1ece9f44911f6a5, Metadata.git-ref 2a5966dfbd89be9fe6cc0ef3566831e502b81d42 -- so MX-r-9's Z-S92 defect (versioned key never written) did NOT recur. -latest: same ETag 8a06aaa1ee91460aa1ece9f44911f6a5 and same git-ref. ROLLBACK key opal-gateway-d3c31e972e.tar.gz UNTOUCHED: ETag 8e81c94230a54ef80a88d03950e93c81, git-ref d3c31e972e, LastModified 2026-10-10T21:49:41Z (pre-act), so it was not overwritten. | CLOSED 20261010T231237Z |
| L3 | ec2-baked-asset | SSM pull + restart on i-07dccb1615503ac99 | SSM md5 of the RUNNING /opt/opal-gateway/app files equals the release bytes | SSM md5 of the RUNNING /opt/opal-gateway/app files (not an S3 ETag): 98 non-pycache files, compared against the release commit 2a5966dfbd -- 98 EQUAL, 0 DIFFERENT, 0 release-only, 0 host-only. The five CP2 modules each EQUAL by md5 (admin_api 012e661390c2, admin_fabric cbcb35cad051, overlap 6e0d547dc727, gitstate 09b8631aed0c, calls 9aaa782a1e9d, overlap_rules ccc3efbca9e9). NEGATIVE CONTROL against the old base d3c31e972e: exactly 2 DIFFERENT (admin_api.py, admin_fabric.py) and 4 NEW on host (the three modules + refs/overlap_rules.json), so the instrument discriminates and the world moved by exactly the payload. Service active, MainPID 915778 -> 919385. | CLOSED 20261010T231237Z |
| L4 | verify | post-act reads: /health 200, four routes 401/403 with no identity, tool surface difference EMPTY, manifest record | the read-backs, each independent of the deploy rc | /health 200 {ok:true} on an independent curl inside the 90 s window, so no rollback was triggered. The four new routes with NO identity: GET /api/admin/fabric/overlap 401, /gitstate 401, /calls 401, POST /calls/close 401 -- all owner-gated, and they were 404 before the act. MCP tool surface read from the live registry (app.tools.mcp._tool_manager.list_tools()) before and after through the SAME reader: 42 -> 42, 0 added, 0 removed, name-for-name identical, DIFFERENCE EMPTY. ENV key set unchanged, 52 keys before and after. Manifest record committed 9defac6133 after correcting the two fields safe-ec2-deploy.sh wrote from the release tree's stale vintage (previous_deployed_commit 2c0f84966d -> d3c31e972e, and the prior release's release_note). NO POST was made to /api/admin/fabric/calls/close beyond the unauthenticated 401 probe, which carried {} and no identity (BOUNDS 2). | CLOSED 20261010T231237Z |
| L1 | activation | bundle build: mcportal bc37107 dashboard built by deploy-to-ec2.sh from the manifest pin | build log + bun pre-check 77 of 77 |  | OPEN |
| L2 | s3-prefix | release build + upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway | head-object len/ETag/git-ref on the versioned key AND -latest |  | OPEN |
| L3 | ec2-baked-asset | SSM pull + restart on i-07dccb1615503ac99 | SSM md5 of the RUNNING /opt/opal-gateway/app files equals the release bytes |  | OPEN |
| L4 | verify | post-act reads: /health 200, four routes 401/403 with no identity, tool surface difference EMPTY, manifest record | the read-backs, each independent of the deploy rc |  | OPEN |

## Log

- 20261010T230022Z OPENED by 0.7.0_AE_CloudOps~MP with 4 leg(s)
- 20261010T231237Z LEG L1 closed: Bundle built by deploy-to-ec2.sh from the MANIFEST pin mcportal_commit=bc37107 (MP-p-2, descendant of d60b4e0), never a 
- 20261010T231237Z LEG L2 closed: head-object read-backs, independent of the deploy rc: VERSIONED key ec2/opal-gateway/opal-gateway-2a5966dfbd.tar.gz EXIS
- 20261010T231237Z LEG L3 closed: SSM md5 of the RUNNING /opt/opal-gateway/app files (not an S3 ETag): 98 non-pycache files, compared against the release 
- 20261010T231237Z LEG L4 closed: /health 200 {ok:true} on an independent curl inside the 90 s window, so no rollback was triggered. The four new routes w
- 20261010T231237Z CLOSED -- all 4 legs proven
