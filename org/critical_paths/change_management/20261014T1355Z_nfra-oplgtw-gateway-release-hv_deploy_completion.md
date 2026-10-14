# Deploy Completion Record
**Date opened:** 2026-10-14T13:55:02.698912+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-hv-2 ACT 2: the gateway release of harvest_list/harvest_read (7c558b4e21 on base 90967e39ba, three halves signed)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the deploy source is the signed release: C:/tmp/og-rel-hv HEAD = 7c558b4e2176a632d13e6301af3e06d434aa1540 and its parent = live deployed_commit 90967e39ba | both hashes read at the act, not from the Phase A record |  | OPEN |
| L2 | activation | safe-ec2-deploy lands the release on i-07dccb1615503ac99 and the service comes back | the deploy output plus GET /health on 127.0.0.1:8080 |  | OPEN |
| L3 | ec2-baked-asset | the RUNNING path carries the release bytes | one SSM md5 read over app/, deploy/, dashboard/ equal to 7c558b4e21, WITH the negative control against base 90967e39ba (the two harvest files must differ) |  | OPEN |
| L4 | verify | the triggers hold and a real served read works | registry tools 65 (not the decorator census), .env key NAMES unchanged, and W/HV2_SERVED.json from harvest_read through the INSTALLED code with the two refusal arms |  | OPEN |

## Log

- 20261014T135502Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
