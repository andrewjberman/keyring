# Deploy Completion Record
**Date opened:** 2026-10-09T14:14:25.738253+00:00
**Status:** HELD-PRE-APPLY -- gate: external / NFRA_OPLGTW OG-ap-4 (env-only 4-meeting allowlist, all halves signed) ledger CLOSE commit, delivered to this seat by 2.0.0_SA_COO~MP; CTO~Z msg 32788 relayed by 2.0.0_SA_COO~O msg 32795 put OG-ap-4 AHEAD of MP-x-4 because only one gateway release is in flight at a time (held since 2026-10-09T14:22:43.500475+00:00)
**Deploy:** NFRA_MCPORTAL MP-x-4 (round 5, E2): the narrow gateway release that serves the Control Plane page -- MP-x-1's four files onto the live r29 base, dashboard bundle mcportal d60b4e0
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | bundle build: mcportal d60b4e0 built by deploy-to-ec2.sh from EC2_MANIFEST.json services.opal-gateway.mcportal_commit (never the checkout's HEAD); bun cache pre-check must pass so no package is fetched | pre-check 77 of 77 rc=0 against d60b4e0's own bun.lock; INFO: building mcportal @ d60b4e0 then dist/index.html present |  | OPEN |
| L2 | s3-prefix | release build and upload: artifact opal-gateway-<sha>.tar.gz to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ with git-ref metadata, + latest | head-object ContentLength/ETag and Metadata.git-ref == the release sha |  | OPEN |
| L3 | activation | SSM pull and restart on i-07dccb1615503ac99, then /health 200 within 90 s or the named rollback runs AT ONCE | ssm:<command_id> Status=Success; /health=200; MainPID moves off 857046 |  | OPEN |
| L4 | verify | manifest record + MCP tool surface unmoved + the three ACs | EC2_MANIFEST deployed_commit=<release sha>, previous_deployed_commit=91811b648a, mcportal_commit=d60b4e0; tools 66 -> 66 difference empty; AC1/AC2/AC3 PASS |  | OPEN |

## Log

- 20261009T141425Z OPENED by 0.7.0_AE_CloudOps~MP with 4 leg(s)
- 20261009T142243Z HELD-PRE-APPLY gate=external/NFRA_OPLGTW OG-ap-4 (env-only 4-meeting allowlist, all halves signed) ledger CLO
