# Deploy Completion Record
**Date opened:** 2026-10-17T05:16:03.399442+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-34 Phase B: the round-40 fourth batched gateway release 9d5b7125571520b977401634a01935924f4c9787 (cut on d3ae88be463d88c6f4ea22fb297659bf44f43758) onto the live ref d3ae88be463d88c6f4ea22fb297659bf44f43758, three halves signed (CTO 9bbfd119eb, COO 1c5a9ba7ee, CVO b94a795131) against ask sha256 bdccc464670e, CT1 Amendments 1 and 2 (CTO ddb0eded30, 24bc48799d), GO msgs 35362 and 35383. Rollback byte reference: S3 tarball opal-gateway-d3ae88be46.tar.gz, 895333 bytes, sha256 764f565cffef310156c85a4c31ad972d10615f0fbc0c732c8fa8fceca3f8b236
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch5 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=d3ae88be463d88c6f4ea22fb297659bf44f43758 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs over app, deploy and lib, 65 env keys, health 200 |  | OPEN |
| served-read | verify | the arms through the installed code (fresh process) plus the 30-minute service read-back every 60 s, the count of /mcp window calls served | proof: W/CODE5_SERVED.json, no trigger of CT1 Amendment 2 |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; 2.0.0_SA_COO~O told the live commit | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261017T051603Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
