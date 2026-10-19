# Deploy Completion Record
**Date opened:** 2026-10-19T06:58:25.366752+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T074453Z
**Deploy:** NFRA_OPLGTW OG-ap-48 Phase B: the round-45 twelfth batched gateway release 6b1a9bd292855841826e194d0bddf9ac79bc8337 (the audit lake leg bounded and audible, OG-pr-6; UNARMED ONLY, no SSM write), cut on e09c30c3f064296ae7f8eb2c47b91bfec0be9b60; rollback tarball opal-gateway-e09c30c3f0.tar.gz 921536 bytes sha256 ebc920a03536cd0f7004e995eb8d7d242536599be0fbeb8b1c45021fd6c291be
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch13 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=e09c30c3f064296ae7f8eb2c47b91bfec0be9b60 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, dell1's four harvest files, graph.py and probe_listener.py equal to the release's | DEPLOYMENT COMPLETE 2026-10-19T07:05:17Z rc=0 (deploy started 07:02:30Z), base guard e09c30c3f0 == live ref at both checkpoints, no HALT_OVERRIDE (the first call stopped at the halt gate, no hold among the messages listed, then HALT_ACK=1); SSM md5 walk 143 of 143 equal to release blobs 6b1a9bd292; 65 env keys; health 200; marker == 6b1a9bd292855841826e194d0bddf9ac79bc8337; host md5 of dell1's four harvest files, graph.py, probe_listener.py and audit.py equal to the release's (7 of 7) | CLOSED 20261019T074451Z |
| served-read | verify | the served read UNARMED ONLY (lease parameter absent before and after, listener calls answering 403 probe_not_armed, armings 0), the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, and the 30-minute read-back with the journal POST /mcp count AND the audit-lake count for the same window, and the audit-lake WARN line count and counter value | proof: W/CODE13_SERVED.json, NRestarts 0, the lease parameter absent, the journal non-zero against the non-zero lake, audit_failure_counter 0 | W/CODE13_SERVED.json: 27 of 27 under the hard guard; UNARMED ONLY: lease parameter absent before, after and at the close (07:40:03Z), no SSM write, three calls answered 403 probe_not_armed, listener on 127.0.0.1 and the service PID, PID unchanged NRestarts 0; DUAL COUNT over the same 07:07:00Z-07:37:00Z window: journal 149 POST /mcp lines vs 270 audit-lake records (ratio 0.552; baseline 168), listener /probe/ lines 3 == 3 requests made; AUDIT FAILURE COUNTER: 0 audit-lake WARN lines over the read-back, counter value 0; read-back 32 probes 07:06:32Z-07:37:32Z 0 triggers NRestarts 0; clock Leap Normal synchronised and systemctl --failed 0 read before the close | CLOSED 20261019T074452Z |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 2.0.0_SA_COO~O | proof: the commit hash carrying both, checksums cross-checked against the host md5 | commit 444568e38f (merged to box/sitez 08d4fba81a): manifest deployed_commit 6b1a9bd292 previous e09c30c3f0, file_checksums 10 of 10 cross-checked against host md5 (one moves: app/audit.py); runbook 7.2 names the live release and rollback target e09c30c3f0 | CLOSED 20261019T074452Z |

## Log

- 20261019T065825Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261019T074451Z LEG deploy closed: DEPLOYMENT COMPLETE 2026-10-19T07:05:17Z rc=0 (deploy started 07:02:30Z), base guard e09c30c3f0 == live ref at both chec
- 20261019T074452Z LEG served-read closed: W/CODE13_SERVED.json: 27 of 27 under the hard guard; UNARMED ONLY: lease parameter absent before, after and at the close
- 20261019T074452Z LEG standing-clauses closed: commit 444568e38f (merged to box/sitez 08d4fba81a): manifest deployed_commit 6b1a9bd292 previous e09c30c3f0, file_checks
- 20261019T074453Z CLOSED -- all 3 legs proven
