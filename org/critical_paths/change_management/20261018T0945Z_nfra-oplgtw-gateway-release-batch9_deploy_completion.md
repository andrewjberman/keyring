# Deploy Completion Record
**Date opened:** 2026-10-18T09:45:51.859522+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-40 Phase B: the round-42 eighth batched gateway release 3b94a83e0572f9a14851c2f229ca4aba64c7e670 (the loopback probe listener, cut on aa2efa2cf3dee82030c00f85425f686132adcf4a; rollback tarball opal-gateway-aa2efa2cf3.tar.gz 903604 bytes sha256 1c9ead556da82e2747756cf2ec35ccbce31c88ca2ce460dd6fe800e927068a4f)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch9 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=aa2efa2cf3dee82030c00f85425f686132adcf4a under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, the harvest_research.py md5 equal to the blob |  | OPEN |
| served-read | verify | the single arming (one 25-minute lease) with the probes through the service, the lease lapse and the delete, the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, and the 30-minute service read-back | proof: W/CODE9_SERVED.json, NRestarts 0, the lease parameter absent (ParameterNotFound) |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 1.0.0_SA_CTO~Z and 0.0.0_AB_MSTR~Z in one message | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261018T094551Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
