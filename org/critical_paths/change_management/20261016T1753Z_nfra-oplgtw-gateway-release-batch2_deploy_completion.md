# Deploy Completion Record
**Date opened:** 2026-10-16T17:53:06.598642+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-28 Phase B: the round-38 batched gateway release bf9d23b518527e0e5f9a26aa240fd5af72af6c11 (prelude 2dc919cf26) onto live base d14445961dd6d04275ca8186372a4df4c4fcc5cc, all three halves signed (CTO 87e4e8a540, COO ce4ce4fea9, CVO ffc2045889) against ask sha256 aa5d0a37682e, GO msg 35174
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch2 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=d14445961dd6d04275ca8186372a4df4c4fcc5cc under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release tree over app, deploy and lib, 65 env keys, health 200 |  | OPEN |
| served-read | verify | the served read through the INSTALLED code and the public endpoint: seven round-38 arms by Opal stand-in principals, registry 103 and tools/list unchanged, 27 of 27 tools, seven reader keys | proof: W/CODE2_SERVED.json with every arm true and no trigger |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; 2.0.0_SA_COO~O told the live commit | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261016T175306Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
