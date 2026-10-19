# Deploy Completion Record
**Date opened:** 2026-10-19T16:32:01.336566+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-50 Phase B: the round-46 thirteenth batched gateway release 6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c (the family_depth route GET /api/admin/gateway/families, owner-gated, a new served route; UNARMED ONLY, no SSM write), cut on 6b1a9bd292855841826e194d0bddf9ac79bc8337; rollback tarball opal-gateway-6b1a9bd292.tar.gz 922261 bytes sha256 6fa88e6f58d5079830b085ee97182dd606bba8b859a310dca0778e83c6f103c6
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch14 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=6b1a9bd292855841826e194d0bddf9ac79bc8337 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, dell1's four harvest files, graph.py and probe_listener.py equal to the release's |  | OPEN |
| served-read | verify | the served read UNARMED ONLY (lease parameter absent before and after, listener calls answering 403 probe_not_armed, armings 0), the route on the running service (404 before the deploy; no identity 401, whoami 401, a missing route 404 after), the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, the 30-minute read-back with the journal POST /mcp count AND the audit-lake count for the same window, the audit-lake WARN line count, and the ONE driven read of the deployed module (FWD-20) | proof: W/CODE14_SERVED.json and W/FWD20_DRIVEN_READ.json, NRestarts 0, the lease parameter absent, the journal non-zero against the non-zero lake, audit_failure_counter 0 |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 2.0.0_SA_COO~O, 1.0.0_SA_CTO~Z and 0.0.0_AB_MSTR~Z | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261019T163201Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
