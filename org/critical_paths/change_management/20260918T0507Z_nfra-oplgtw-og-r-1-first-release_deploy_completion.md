# Deploy Completion Record
**Date opened:** 2026-09-18T05:07:24.309664+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T061217Z
**Deploy:** NFRA_OPLGTW OG-r-1 first release: integrated Gateway build, OAuth cutover, Schwab flag OFF
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | opal-gateway /opt/opal-gateway | SSM sha256sum digest match vs the deployed build input, file by file, denominator printed (OGR1-AC4) | OGR1-AC4 PASS (1764e54a16b7bb12d34b36eec7866589b6ea785e) | CLOSED 20260918T061216Z |
| L2 | verify | post-deploy live checks: 401 resource challenge, discovery metadata, zero Schwab tools registered, error count vs baseline, restricted-profile principal count, renamed-role assume/deny | OGR1-AC3,AC5,AC6,AC7,AC9,AC12,AC13 PASS-by-output | OGR1-AC3/AC5/AC6/AC7/AC9/AC12/AC13 verdicts recorded in this run's own probe output | CLOSED 20260918T061216Z |
| L3 | git | EC2_MANIFEST.json services.opal-gateway.deployed_commit | git commit hash of safe-ec2-deploy.sh's own manifest-update commit | EC2_MANIFEST.json committed at ef11656176533a9aebfa3049c9beddcc4f8d98d9 | CLOSED 20260918T061216Z |

## Log

- 20260918T050724Z OPENED by 0.9.0_WK_NFRA_OPLGTW~2 with 3 leg(s)
- 20260918T061216Z LEG L1 closed: OGR1-AC4 PASS (1764e54a16b7bb12d34b36eec7866589b6ea785e)
- 20260918T061216Z LEG L2 closed: OGR1-AC3/AC5/AC6/AC7/AC9/AC12/AC13 verdicts recorded in this run's own probe output
- 20260918T061216Z LEG L3 closed: EC2_MANIFEST.json committed at ef11656176533a9aebfa3049c9beddcc4f8d98d9
- 20260918T061217Z CLOSED -- all 3 legs proven
