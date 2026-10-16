# Deploy Completion Record
**Date opened:** 2026-10-16T09:12:39.976396+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-23 Phase B (second): the code batch release again -- release 3d5c9c8bf1dea0854c9b59d58b83fdf9dcb480e4 onto live base d577e0e7297b3ecba183023d8374855a93f148a7 after the first attempt was rolled back (row Z-S164); the four missing internal-reader grants are live (OG-ap-27, ap27.AC2 PASS); halves signed CTO 2665f19c6a, COO f94bcaf1e5, CVO 49ebdc867a against ask sha256 ba5b9325bca5; re-GO msg 34876
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-code through safe-ec2-deploy.sh with DEPLOY_BASE_REF=d577e0e7297b3ecba183023d8374855a93f148a7 under the A1 guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the wrapper stale-base guard equal at both checkpoints, an SSM md5 walk showing the host equal to the release across app deploy and lib, and app/refs/partner_roster.json and scopes.json equal to trunk blobs |  | OPEN |
| env-keys | verify | the host .env gains exactly the six vendor reader keys (58 to 64 key names), names only over SSM, no value printed | proof: the 64 key names read over SSM, the six present, the 58 prior names unchanged |  | OPEN |
| served-read | verify | the served read through the INSTALLED code: per_tool_good 27 of 27, client_admission three fields true, via_internal_reader true, reader_env_keys_present 6, CVO C1 and C2 | proof: W/CODE_SERVED.json written on the host, ap23.AC2 clauses true |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; 2.0.0_SA_COO~O told the live commit | proof: the commit hash carrying both, every recomputed checksum cross-checked against the host measured md5 |  | OPEN |

## Log

- 20261016T091239Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
