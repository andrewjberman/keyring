# Deploy Completion Record
**Date opened:** 2026-10-19T16:32:01.336566+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T172323Z
**Deploy:** NFRA_OPLGTW OG-ap-50 Phase B: the round-46 thirteenth batched gateway release 6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c (the family_depth route GET /api/admin/gateway/families, owner-gated, a new served route; UNARMED ONLY, no SSM write), cut on 6b1a9bd292855841826e194d0bddf9ac79bc8337; rollback tarball opal-gateway-6b1a9bd292.tar.gz 922261 bytes sha256 6fa88e6f58d5079830b085ee97182dd606bba8b859a310dca0778e83c6f103c6
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch14 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=6b1a9bd292855841826e194d0bddf9ac79bc8337 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, dell1's four harvest files, graph.py and probe_listener.py equal to the release's | proof: DEPLOYMENT COMPLETE at 2026-10-19T16:35:59Z from C:/tmp/og-rel-batch14 (release 6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c) through safe-ec2-deploy.sh with DEPLOY_BASE_REF=6b1a9bd292855841826e194d0bddf9ac79bc8337, the stale-base guard equal at both checkpoints, no HALT_OVERRIDE; host md5 walk 143 of 143 equal to the release blobs (ap50_pb/host_md5_after.json), 65 env keys, health 200, the marker reads the release sha, tools/list 103, dell1's four harvest files, graph.py, probe_listener.py and audit.py equal to the release's | CLOSED 20261019T172156Z |
| served-read | verify | the served read UNARMED ONLY (lease parameter absent before and after, listener calls answering 403 probe_not_armed, armings 0), the route on the running service (404 before the deploy; no identity 401, whoami 401, a missing route 404 after), the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, the 30-minute read-back with the journal POST /mcp count AND the audit-lake count for the same window, the audit-lake WARN line count, and the ONE driven read of the deployed module (FWD-20) | proof: W/CODE14_SERVED.json and W/FWD20_DRIVEN_READ.json, NRestarts 0, the lease parameter absent, the journal non-zero against the non-zero lake, audit_failure_counter 0 | proof: W/CODE14_SERVED.json and W/FWD20_DRIVEN_READ.json (commit a4fd9a23a4): NRestarts 0 across a 31-probe 30-minute read-back, lease parameter absent before, after and at the close, three listener calls 403 probe_not_armed, 27 of 27 under the hard guard, route 404 before / 401 after / whoami 401 / missing 404, 185 POST /mcp journal lines against 295 lake records, audit-lake WARN lines 0 counter 0, host clock Leap Normal and systemctl --failed 0 read 2026-10-19T17:12Z before the close, FWD-20 driven read 13 of 13 rows 59 values with schedule, frontier and earliest date equal to independent CLI reads | CLOSED 20261019T172157Z |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 2.0.0_SA_COO~O, 1.0.0_SA_CTO~Z and 0.0.0_AB_MSTR~Z | proof: the commit hash carrying both, checksums cross-checked against the host md5 | proof: commit a4fd9a23a4 carries the EC2_MANIFEST opal-gateway block (deployed_commit 6d1b5dcb64, previous 6b1a9bd292; no file_checksums key moves, all 10 cross-checked against the host md5) and runbook 7.2 naming 6d1b5dcb64 as live with rollback target 6b1a9bd292 | CLOSED 20261019T172157Z |

## Log

- 20261019T163201Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261019T172156Z LEG deploy closed: proof: DEPLOYMENT COMPLETE at 2026-10-19T16:35:59Z from C:/tmp/og-rel-batch14 (release 6d1b5dcb64b945deb98664c6ae078d8f1
- 20261019T172157Z LEG served-read closed: proof: W/CODE14_SERVED.json and W/FWD20_DRIVEN_READ.json (commit a4fd9a23a4): NRestarts 0 across a 31-probe 30-minute re
- 20261019T172157Z LEG standing-clauses closed: proof: commit a4fd9a23a4 carries the EC2_MANIFEST opal-gateway block (deployed_commit 6d1b5dcb64, previous 6b1a9bd292; n
- 20261019T172323Z CLOSED -- all 3 legs proven
