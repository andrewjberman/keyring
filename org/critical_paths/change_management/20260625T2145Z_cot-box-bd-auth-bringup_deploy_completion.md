# Deploy Completion Record
**Date opened:** 2026-06-25T21:45:18.784591+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T214519Z
**Deploy:** cot-exporter box: BD auto-login runtime + script + env bring-up
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| cot-bringup | verify | node+playwright+chromium + script + secret-ids.env on i-0643a5bee8a8feabf | true | i-0643a5bee8a8feabf (started from stopped, SSM-online): node v18.20.8+npm10.8.2 installed; 3 canonical artifacts pulled from ec2/bd-cot-auto-login/ to /opt/bd-cot-auto-login/ + npm install (node_modules) + playwright install chromium (AL2023 ubuntu-fallback, same as 49F); secret-ids.env written + cat-verified (BD_FIRM_ID=cot, BD_OTP_ADAPTER=relay, BD_OTP_RELAY_SECRET_ID=blackdiamond/cot/otp-relay, BD_KIMI_SECRET_ID=astn/kimi/api-key, BD_APP_URL=https://bd3.bdreporting.com, BD_HEADLESS=1, native-IP). Artifact-pull IAM applied (ec2/bd-cot-auto-login/* cot-named, firm-sep). Box left RUNNING for the CVO completing-run. | CLOSED 20260625T214519Z |

## Log

- 20260625T214518Z OPENED by 0.7.0_AE_CloudOps with 1 leg(s)
- 20260625T214519Z LEG cot-bringup closed: i-0643a5bee8a8feabf (started from stopped, SSM-online): node v18.20.8+npm10.8.2 installed; 3 canonical artifacts pulled 
- 20260625T214519Z CLOSED -- all 1 legs proven
