# Deploy Completion Record
**Date opened:** 2026-10-18T06:17:07.636240+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T070117Z
**Deploy:** NFRA_OPLGTW OG-ap-39 Phase B (re-cut, amendment A4): the round-42 seventh batched gateway release aa2efa2cf3dee82030c00f85425f686132adcf4a (cut on 4257a2aa42e5366270b3652f21dba90872dbb1e0, trunk 23efa6e1f4f6873e66d812c6e8b0e1a0ba0ac0c4) onto the live ref 4257a2aa42e5366270b3652f21dba90872dbb1e0: the absent_reason codes in the client tools' served descriptions (the fee note reworded by OG-en-30) and the db3 test that reads the worktree; no page-size change. Three halves signed (CTO 43b1f58f19, COO 2ce52fead7, CVO 50c8f718bf) on ask sha256 034d2c346e5d, GO msg 35636. Code-only release: no image, so the image-family check does not apply. harvest_research.py carried at blob 574959b682d4. Rollback: the live ref tarball opal-gateway-4257a2aa42.tar.gz, 902884 bytes, sha256 f59e4b4009cef1afa662f30bcd2caa821d33cf91641fba0fb97366c6f778d33f; the unit is not changed, the marker is rewritten to the live ref's sha
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch8 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=4257a2aa42e5366270b3652f21dba90872dbb1e0 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, the unit limits unchanged, harvest_research.py host md5 beside its blob | DEPLOYMENT COMPLETE 2026-10-18T06:22:23Z rc=0, base guard 4257a2aa42 == live ref at both checkpoints, no HALT_OVERRIDE; SSM md5 walk 139 of 139 equal to release blobs aa2efa2cf3; 65 env keys; health 200; marker == aa2efa2cf3dee82030c00f85425f686132adcf4a; harvest_research.py md5 596c299597067fe5a8afb8e3493a0ed9 == 4257a2aa42 blob (CT1) | CLOSED 20261018T070117Z |
| served-read | verify | the 27-tool read under the hard guard, the four arms and served_notes through the installed code (fresh process), the host clock and systemctl --failed read BEFORE the close, and the 30-minute service read-back every 60 s with NRestarts and the count of /mcp window calls | proof: W/CODE8_SERVED.json, no trigger fired, NRestarts 0 through the read-back | W/CODE8_SERVED.json: 27 of 27 under rlimit guard; served notes 5 of 5 client tools, fee note source-scoped true; e10/e13/e14/e15 true; read-back 31 probes 06:23:45Z-06:53:45Z, 0 triggers, NRestarts 0, 157 /mcp requests, 0 window calls; clock Leap Normal synchronised and systemctl --failed 0 read 06:55:17Z before the close | CLOSED 20261018T070117Z |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 1.0.0_SA_CTO~Z and 2.0.0_SA_COO~O | proof: the commit hash carrying both, checksums cross-checked against the host md5 | commit 6d98c6a326 (merged box/sitez 765d4dd899): manifest deployed_commit aa2efa2cf3 previous 4257a2aa42, file_checksums 10 of 10 cross-checked against host md5; runbook 7.2 names the live release and rollback target 4257a2aa42 | CLOSED 20261018T070117Z |

## Log

- 20261018T061707Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261018T070117Z LEG deploy closed: DEPLOYMENT COMPLETE 2026-10-18T06:22:23Z rc=0, base guard 4257a2aa42 == live ref at both checkpoints, no HALT_OVERRIDE; 
- 20261018T070117Z LEG served-read closed: W/CODE8_SERVED.json: 27 of 27 under rlimit guard; served notes 5 of 5 client tools, fee note source-scoped true; e10/e13
- 20261018T070117Z LEG standing-clauses closed: commit 6d98c6a326 (merged box/sitez 765d4dd899): manifest deployed_commit aa2efa2cf3 previous 4257a2aa42, file_checksums
- 20261018T070117Z CLOSED -- all 3 legs proven
