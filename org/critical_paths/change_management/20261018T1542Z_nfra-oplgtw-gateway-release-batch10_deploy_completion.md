# Deploy Completion Record
**Date opened:** 2026-10-18T15:42:48.752745+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T163205Z
**Deploy:** NFRA_OPLGTW OG-ap-42 Phase B: the round-43 ninth batched gateway release a0c83303ee48c95c16a61c0d5e8bd186b1083b66 (the probe-lease firm pin and the Graph host pin, UNARMED ONLY, no SSM write), cut on 922ee425fea4b2cbce2beb8ca7930f3a474d877a; rollback tarball opal-gateway-922ee425fe.tar.gz 913956 bytes sha256 d025c8a103f39645558ddd48b600f671135604c2714ec08b96bfabfc95688424
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch10 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=922ee425fea4b2cbce2beb8ca7930f3a474d877a under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, the four harvest files equal to their blobs | DEPLOYMENT COMPLETE 2026-10-18T15:49:27Z rc=0, base guard 922ee425fe == live ref at both checkpoints, no HALT_OVERRIDE; SSM md5 walk 141 of 141 equal to release blobs a0c83303ee; 65 env keys; health 200; marker == a0c83303ee48c95c16a61c0d5e8bd186b1083b66; host md5 of dell1's four harvest files and the two taken app files equal to the release's (6 of 6) | CLOSED 20261018T163203Z |
| served-read | verify | the served read UNARMED ONLY (lease parameter absent before and after, the listener answering 403 probe_not_armed, armings 0), the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, and the 30-minute service read-back with the Graph-backed call counts | proof: W/CODE10_SERVED.json, NRestarts 0, the lease parameter absent | W/CODE10_SERVED.json: 27 of 27 under rlimit guard; UNARMED ONLY: lease parameter absent before, after and at the close (16:25:35Z), no SSM write, three calls answered 403 probe_not_armed, listener on 127.0.0.1 and the service PID, PID unchanged NRestarts 0; read-back 32 probes 15:50:20Z-16:21:19Z 0 triggers NRestarts 0; 1 Graph-backed call (whoami) ok, 0 GraphHostRefused lines, 0 /mcp requests; clock Leap Normal synchronised and systemctl --failed 0 read 16:23:01Z before the close | CLOSED 20261018T163204Z |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 1.0.0_SA_CTO~Z and 0.0.0_AB_MSTR~Z in one message | proof: the commit hash carrying both, checksums cross-checked against the host md5 | commit a8508544f9 (merged to box/sitez): manifest deployed_commit a0c83303ee previous 922ee425fe, file_checksums 10 of 10 cross-checked against host md5; runbook 7.2 names the live release and rollback target 922ee425fe | CLOSED 20261018T163204Z |

## Log

- 20261018T154248Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261018T163203Z LEG deploy closed: DEPLOYMENT COMPLETE 2026-10-18T15:49:27Z rc=0, base guard 922ee425fe == live ref at both checkpoints, no HALT_OVERRIDE; 
- 20261018T163204Z LEG served-read closed: W/CODE10_SERVED.json: 27 of 27 under rlimit guard; UNARMED ONLY: lease parameter absent before, after and at the close (
- 20261018T163204Z LEG standing-clauses closed: commit a8508544f9 (merged to box/sitez): manifest deployed_commit a0c83303ee previous 922ee425fe, file_checksums 10 of 1
- 20261018T163205Z CLOSED -- all 3 legs proven
