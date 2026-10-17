# Deploy Completion Record
**Date opened:** 2026-10-17T01:49:35.066152+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-32 Phase B: the round-40 batched gateway release b124377b41caf5665b999378fd0ca08ad8a1fb7d (cut on 4be300110e, three harvest files whole from trunk) onto the live ref 319c9413a20895a63517c5ca1b9ced0f78a5573a, all three halves signed (CTO 094d2ffa08, COO a09c5ce348, CVO 5b3b3b7d3a) against ask sha256 dc9230a4ada7, GO msg 35308. Rollback byte reference: S3 tarball opal-gateway-319c9413a2.tar.gz, 895292 bytes, sha256 6202213c503fd8d3c8a197beed35f76544c47978687213672391965f8874408f
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch4 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=319c9413a20895a63517c5ca1b9ced0f78a5573a under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs over app, deploy and lib, 65 env keys, health 200 |  | OPEN |
| served-read | verify | the served read through the INSTALLED code and the public endpoint: the paging chain one call at a time, newest first, host memory sampled, catalog md5 on the host, registry 103 and tools/list unchanged, MUSE_CLIENT_ID absent | proof: W/CODE4_SERVED.json with every arm true and no trigger |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; 2.0.0_SA_COO~O told the live commit | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261017T014935Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
