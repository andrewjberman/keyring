# Deploy Completion Record
**Date opened:** 2026-10-19T04:11:10.053227+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T045103Z
**Deploy:** NFRA_OPLGTW OG-ap-46 Phase B: the round-44 eleventh batched gateway release e09c30c3f064296ae7f8eb2c47b91bfec0be9b60 (family_depth.py inert with its data and test, and the corrected probe-listener comment; UNARMED ONLY, no SSM write), cut on eff517546eeea48811cf13f3de38926c5944c6df; rollback tarball opal-gateway-eff517546e.tar.gz 915153 bytes sha256 e1a8eb744ad4452981bf396ff5a2204ee3642641287ba9b8b9fd895f602a98b5
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch12 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=eff517546eeea48811cf13f3de38926c5944c6df under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, dell1's four harvest files and graph.py equal to the release's | DEPLOYMENT COMPLETE 2026-10-19T04:14:32Z rc=0 (deploy started 04:12:55Z), base guard eff517546e == live ref at both checkpoints, no HALT_OVERRIDE (the first call stopped at the halt gate, no halt among the messages listed, then HALT_ACK=1); SSM md5 walk 143 of 143 equal to release blobs e09c30c3f0; 65 env keys; health 200; marker == e09c30c3f064296ae7f8eb2c47b91bfec0be9b60; host md5 of dell1's four harvest files, graph.py, probe_listener.py, family_depth.py and silver_families.json equal to the release's (8 of 8, CT2 printed) | CLOSED 20261019T045103Z |
| served-read | verify | the served read UNARMED ONLY (lease parameter absent before and after, listener calls answering 403 probe_not_armed, armings 0), the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, and the 30-minute read-back with the journal POST /mcp count AND the audit-lake count for the same window | proof: W/CODE12_SERVED.json, NRestarts 0, the lease parameter absent, the journal non-zero against the non-zero lake | W/CODE12_SERVED.json: 27 of 27 under the hard guard; UNARMED ONLY: lease parameter absent before, after and at the close (04:48:42Z), no SSM write, three calls answered 403 probe_not_armed, listener on 127.0.0.1 and the service PID, PID unchanged NRestarts 0; DUAL COUNT over the same 04:16:00Z-04:46:00Z window: journal 149 POST /mcp lines vs 270 audit-lake records (ratio 0.552; baseline 168), listener /probe/ lines 3 == 3 requests made; read-back 32 probes 04:15:59Z-04:46:58Z 0 triggers NRestarts 0; clock Leap Normal synchronised and systemctl --failed 0 read before the close | CLOSED 20261019T045103Z |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 2.0.0_SA_COO~O | proof: the commit hash carrying both, checksums cross-checked against the host md5 | commit e5c576716d (merged to box/sitez d4a76df5aa): manifest deployed_commit e09c30c3f0 previous eff517546e, file_checksums 10 of 10 cross-checked against host md5 (none moves); runbook 7.2 names the live release and rollback target eff517546e | CLOSED 20261019T045103Z |

## Log

- 20261019T041110Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261019T045103Z LEG deploy closed: DEPLOYMENT COMPLETE 2026-10-19T04:14:32Z rc=0 (deploy started 04:12:55Z), base guard eff517546e == live ref at both chec
- 20261019T045103Z LEG served-read closed: W/CODE12_SERVED.json: 27 of 27 under the hard guard; UNARMED ONLY: lease parameter absent before, after and at the close
- 20261019T045103Z LEG standing-clauses closed: commit e5c576716d (merged to box/sitez d4a76df5aa): manifest deployed_commit e09c30c3f0 previous eff517546e, file_checks
- 20261019T045103Z CLOSED -- all 3 legs proven
