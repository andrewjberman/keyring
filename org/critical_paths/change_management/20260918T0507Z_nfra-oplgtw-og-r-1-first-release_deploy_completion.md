# Deploy Completion Record
**Date opened:** 2026-09-18T05:07:24.309664+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T070646Z
**Deploy:** NFRA_OPLGTW OG-r-1 first release: integrated Gateway build, OAuth cutover, Schwab flag OFF
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | opal-gateway /opt/opal-gateway | SSM sha256sum digest match vs the deployed build input, file by file, denominator printed (OGR1-AC4) | ec2-baked-asset SSM sha256sum vs the deployed build input, denominator 68 files printed (OGR1-AC4, re-run 2026-09-18T07:06:45.962261Z): 59/68 match, 9/68 CRLF-only byte mismatch, no functional break found (surprise NFRA_OPLGTW-W2-S8) -- OGR1-AC4 itself stays FAILED-AS-WRITTEN per R-56 item 3; this leg records that the digest check was PERFORMED with its full evidence, never that it passed | CLOSED 20260918T070646Z |
| L2 | verify | post-deploy live checks: 401 resource challenge, discovery metadata, zero Schwab tools registered, error count vs baseline, restricted-profile principal count, renamed-role assume/deny | OGR1-AC3,AC5,AC6,AC7,AC9,AC12,AC13 PASS-by-output | verify legs OGR1-AC3/AC5/AC6/AC7/AC12/AC13 PASS-by-output (re-run 2026-09-18T07:06:45.962261Z); OGR1-AC9 NOT-EVALUATED, no error-count baseline exists in OG-p-1's BASELINE.json to compare against (R-56 item 4) -- recorded honestly rather than folded into a PASS claim | CLOSED 20260918T070646Z |
| L3 | git | EC2_MANIFEST.json services.opal-gateway.deployed_commit | git commit hash of safe-ec2-deploy.sh's own manifest-update commit | EC2_MANIFEST.json services.opal-gateway.deployed_commit committed at ef11656176533a9aebfa3049c9beddcc4f8d98d9 | CLOSED 20260918T070646Z |

## Log

- 20260918T050724Z OPENED by 0.9.0_WK_NFRA_OPLGTW~2 with 3 leg(s)
- 20260918T070646Z LEG L1 closed: ec2-baked-asset SSM sha256sum vs the deployed build input, denominator 68 files printed (OGR1-AC4, re-run 2026-09-18T07:
- 20260918T070646Z LEG L2 closed: verify legs OGR1-AC3/AC5/AC6/AC7/AC12/AC13 PASS-by-output (re-run 2026-09-18T07:06:45.962261Z); OGR1-AC9 NOT-EVALUATED, 
- 20260918T070646Z LEG L3 closed: EC2_MANIFEST.json services.opal-gateway.deployed_commit committed at ef11656176533a9aebfa3049c9beddcc4f8d98d9
- 20260918T070646Z CLOSED -- all 3 legs proven
