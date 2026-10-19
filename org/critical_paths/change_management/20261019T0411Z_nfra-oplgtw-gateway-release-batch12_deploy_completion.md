# Deploy Completion Record
**Date opened:** 2026-10-19T04:11:10.053227+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-46 Phase B: the round-44 eleventh batched gateway release e09c30c3f064296ae7f8eb2c47b91bfec0be9b60 (family_depth.py inert with its data and test, and the corrected probe-listener comment; UNARMED ONLY, no SSM write), cut on eff517546eeea48811cf13f3de38926c5944c6df; rollback tarball opal-gateway-eff517546e.tar.gz 915153 bytes sha256 e1a8eb744ad4452981bf396ff5a2204ee3642641287ba9b8b9fd895f602a98b5
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch12 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=eff517546eeea48811cf13f3de38926c5944c6df under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, dell1's four harvest files and graph.py equal to the release's |  | OPEN |
| served-read | verify | the served read UNARMED ONLY (lease parameter absent before and after, listener calls answering 403 probe_not_armed, armings 0), the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, and the 30-minute read-back with the journal POST /mcp count AND the audit-lake count for the same window | proof: W/CODE12_SERVED.json, NRestarts 0, the lease parameter absent, the journal non-zero against the non-zero lake |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 2.0.0_SA_COO~O | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261019T041110Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
