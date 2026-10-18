# Deploy Completion Record
**Date opened:** 2026-10-18T19:19:28.873905+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-44 Phase B: the round-43 tenth batched gateway release eff517546eeea48811cf13f3de38926c5944c6df (the access-log repair OG-pr-5, UNARMED ONLY, no SSM write), cut on a0c83303ee48c95c16a61c0d5e8bd186b1083b66; rollback tarball opal-gateway-a0c83303ee.tar.gz 914681 bytes sha256 77236429527690cd47483769f45493bf1a141ca4f1074a6ed981c3e81226e1a9
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch11 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=a0c83303ee48c95c16a61c0d5e8bd186b1083b66 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, the four harvest files and graph.py equal to the release's |  | OPEN |
| served-read | verify | the served read UNARMED ONLY (lease parameter absent before and after, three listener calls answering 403 probe_not_armed, armings 0), the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, and the 30-minute read-back with the journal POST /mcp count AND the audit-lake count for the same window | proof: W/CODE11_SERVED.json, NRestarts 0, the lease parameter absent, the journal non-zero against the non-zero lake |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 1.0.0_SA_CTO~Z and 0.0.0_AB_MSTR~Z in one message | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261018T191928Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
