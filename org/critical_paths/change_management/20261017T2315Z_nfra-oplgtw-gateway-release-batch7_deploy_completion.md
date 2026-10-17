# Deploy Completion Record
**Date opened:** 2026-10-17T23:15:20.563030+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-38 Phase B: the round-41 sixth batched gateway release d077cef04333500595a7a531ebddc2f43e5f8789 (cut on efcc8ae19f7eebb04e2f45f45c0def28af037c24, trunk bae898b6a70997f5f632c17a9cb5b9a39cfe8848) onto the live ref efcc8ae19f7eebb04e2f45f45c0def28af037c24: the repair of the ARMED hazard Z-S375 (streamed typed Parquet reads, bounded etfs_compare_peers, a memory ceiling on the gateway unit). Three halves signed (CTO f6807b0bba, CVO f1ac7e004e, COO 371e908238) on ask sha256 33686c0a63cb, GO msg 35574, conditions C1-C17. Code-and-unit release: no image, so the image-family check does not apply. Rollback: the live ref tarball opal-gateway-efcc8ae19f.tar.gz, 900200 bytes, sha256 b07656f114f982374407bcb2b70de3ebb4dd758f73d579bd256f0a26aaa9edd0; the rollback reinstalls the old unit WITHOUT the limits and rewrites the marker to the live ref's sha
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch7 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=efcc8ae19f7eebb04e2f45f45c0def28af037c24 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, the unit limits live |  | OPEN |
| served-read | verify | the 27-tool read under the hard guard, the four arms through the installed code, the host clock and systemctl --failed read BEFORE the close, and the 30-minute service read-back every 60 s with NRestarts and the count of /mcp window calls | proof: W/CODE7_SERVED.json, no trigger fired, NRestarts 0 through the read-back |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 1.0.0_SA_CTO~Z and 2.0.0_SA_COO~O | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261017T231520Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
