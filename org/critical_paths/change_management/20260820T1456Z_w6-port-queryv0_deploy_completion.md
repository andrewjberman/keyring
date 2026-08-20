# Deploy Completion Record
**Date opened:** 2026-08-20T14:56:23.952800+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260820T151350Z
**Deploy:** OPAL_ANALYST.W6-PORT: catalog port + /query/v0 plumbing endpoint + IAM read grant + gateway EC2 deploy
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | code+catalog+TF committed pre-apply (Rule 2) | commit hashes | commits e52a039d64 (port+endpoint+audit+TF) + a2a4f63ea8 (4MB amendment per CTO Msg 63157) on CLOUD pre-apply; commit-gate PASS x5 | CLOSED 20260820T145829Z |
| L2 | activation | safe-apply infra/aws/terraform/opal-gateway (ONE add: gw_queryv0_portal_read policy) | apply + 0-diff + live simulate allowed | apply 1/0/0 == staged w6.tfplan; 0-diff 'No changes'; LIVE simulate: json/ servable key allowed + json-tiered/ excluded-prefix implicitDeny (scope exact, separate invocations) | CLOSED 20260820T150032Z |
| L3 | s3-prefix | safe-ec2-deploy opal-gateway (S3 tarball -> SSM pull -> service restart) | deploy output + manifest entry | safe-ec2-deploy run 3 SUCCESS (runs 1-2 failed on the wrapper's unretried health curl -- fixed, committed; service live+healthy throughout, journal-verified); artifact opal-gateway-8908b39d5c @7dda75128d; manifest committed @fca8aaa750 | CLOSED 20260820T151350Z |
| L4 | verify | on-box battery 13/13 (SSM) + endpoint exercises ALLOW/DENY/403-floor/limit-trip + audit-lake object | SSM outputs + curl outputs + S3 audit key | on-box 13/13 (SSM Success) + E1-E7 exercises: ALLOW 200 w/ data, off-catalog 403, floor 403, zero-mint deny 403, rate 429 at exactly the window boundary, unauth 401, audit floor rows + lake object audit/dt=2026-08-20/2026-08-20T15:08:41.646073+00:00-cd4803c4.jsonl; PROOF_OF_SPEC VALID rc=0 | CLOSED 20260820T151350Z |

## Log

- 20260820T145623Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260820T145829Z LEG L1 closed: commits e52a039d64 (port+endpoint+audit+TF) + a2a4f63ea8 (4MB amendment per CTO Msg 63157) on CLOUD pre-apply; commit-ga
- 20260820T150032Z LEG L2 closed: apply 1/0/0 == staged w6.tfplan; 0-diff 'No changes'; LIVE simulate: json/ servable key allowed + json-tiered/ excluded-
- 20260820T151350Z LEG L3 closed: safe-ec2-deploy run 3 SUCCESS (runs 1-2 failed on the wrapper's unretried health curl -- fixed, committed; service live+
- 20260820T151350Z LEG L4 closed: on-box 13/13 (SSM Success) + E1-E7 exercises: ALLOW 200 w/ data, off-catalog 403, floor 403, zero-mint deny 403, rate 42
- 20260820T151350Z CLOSED -- all 4 legs proven
