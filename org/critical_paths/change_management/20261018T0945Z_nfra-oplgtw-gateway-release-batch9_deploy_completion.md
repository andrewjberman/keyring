# Deploy Completion Record
**Date opened:** 2026-10-18T09:45:51.859522+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T103155Z
**Deploy:** NFRA_OPLGTW OG-ap-40 Phase B: the round-42 eighth batched gateway release 3b94a83e0572f9a14851c2f229ca4aba64c7e670 (the loopback probe listener, cut on aa2efa2cf3dee82030c00f85425f686132adcf4a; rollback tarball opal-gateway-aa2efa2cf3.tar.gz 903604 bytes sha256 1c9ead556da82e2747756cf2ec35ccbce31c88ca2ce460dd6fe800e927068a4f)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch9 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=aa2efa2cf3dee82030c00f85425f686132adcf4a under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, the harvest_research.py md5 equal to the blob | DEPLOYMENT COMPLETE 2026-10-18T09:52:22Z rc=0, base guard aa2efa2cf3 == live ref at both checkpoints, no HALT_OVERRIDE; SSM md5 walk 140 of 140 equal to release blobs 3b94a83e05; 65 env keys; health 200; marker == 3b94a83e0572f9a14851c2f229ca4aba64c7e670; harvest_research.py md5 596c299597067fe5a8afb8e3493a0ed9 == blob (CT1) | CLOSED 20261018T103155Z |
| served-read | verify | the single arming (one 25-minute lease) with the probes through the service, the lease lapse and the delete, the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, and the 30-minute service read-back | proof: W/CODE9_SERVED.json, NRestarts 0, the lease parameter absent (ParameterNotFound) | W/CODE9_SERVED.json: 27 of 27 under rlimit guard; ONE arming of 25 minutes: peers 57 rows heap 134 to 260 MB, 12-page chain median growth 1.65 MB first page 1.7 s max VmRSS 392 MB, other tool and account refused, lease lapsed and call refused, parameter deleted (ParameterNotFound) and call refused; read-back 32 probes 09:53:19Z-10:24:19Z 0 triggers NRestarts 0; clock Leap Normal synchronised and systemctl --failed 0 read 10:26:20Z before the close | CLOSED 20261018T103155Z |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 1.0.0_SA_CTO~Z and 0.0.0_AB_MSTR~Z in one message | proof: the commit hash carrying both, checksums cross-checked against the host md5 | commit 2028915904 (merged to box/sitez): manifest deployed_commit 3b94a83e05 previous aa2efa2cf3, file_checksums 10 of 10 cross-checked against host md5; runbook 7.2 names the live release and rollback target aa2efa2cf3 | CLOSED 20261018T103155Z |

## Log

- 20261018T094551Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261018T103155Z LEG deploy closed: DEPLOYMENT COMPLETE 2026-10-18T09:52:22Z rc=0, base guard aa2efa2cf3 == live ref at both checkpoints, no HALT_OVERRIDE; 
- 20261018T103155Z LEG served-read closed: W/CODE9_SERVED.json: 27 of 27 under rlimit guard; ONE arming of 25 minutes: peers 57 rows heap 134 to 260 MB, 12-page ch
- 20261018T103155Z LEG standing-clauses closed: commit 2028915904 (merged to box/sitez): manifest deployed_commit 3b94a83e05 previous aa2efa2cf3, file_checksums 10 of 1
- 20261018T103155Z CLOSED -- all 3 legs proven
