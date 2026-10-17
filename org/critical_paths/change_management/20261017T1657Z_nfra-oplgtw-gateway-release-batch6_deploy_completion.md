# Deploy Completion Record
**Date opened:** 2026-10-17T16:57:22.794418+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-36 Phase B: the round-41 fifth batched gateway release efcc8ae19f7eebb04e2f45f45c0def28af037c24 (cut on 1753c741d988faa05fa424386bcd9aa0c5efbf71, trunk 409399f8716a) onto the live ref 1753c741d988faa05fa424386bcd9aa0c5efbf71, three halves signed (COO 23e5a7b07e, CTO f02ad0309a, CVO 1df8f8a2df) against ask sha256 20815be2b2c6, GO msgs 35534 and 35535. Code-only tarball: no image, so the image-family check does not apply. Rollback: the live ref tarball opal-gateway-1753c741d9.tar.gz, 898460 bytes, sha256 7cf249065b6b0a1e0b0f8abd78b8068debf9f9fb2238abd4c5cf643f04ba09f5; the rollback also removes /opt/opal-gateway/.deployed_commit
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch6 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=1753c741d988faa05fa424386bcd9aa0c5efbf71 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker /opt/opal-gateway/.deployed_commit equal to the release sha |  | OPEN |
| served-read | verify | the nine arms through the installed code (fresh process) plus the 30-minute service read-back every 60 s, the count of /mcp window calls served, harvest_research.py host md5 against its 1753c741d9 blob | proof: W/CODE6_SERVED.json, no trigger fired |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; 2.0.0_SA_COO~O told the live commit | proof: the commit hash carrying both, checksums cross-checked against the host md5 |  | OPEN |

## Log

- 20261017T165722Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
