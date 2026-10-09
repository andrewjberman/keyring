# Deploy Completion Record
**Date opened:** 2026-10-09T14:51:19.234726+00:00
**Status:** OPEN
**Deploy:** OG-ap-4: TRANSCRIPT_MEETING_ALLOWLIST becomes the 4 committed online_meeting_ids (one .env value, one restart)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| DEP | ec2-baked-asset | opal-gateway | safe-ec2-deploy of c97232408d from C:/tmp/og-tl1b with DEPLOY_BASE_REF=91811b648a; halt gate premise true as OG-ap-3 A3, no HALT_OVERRIDE |  | OPEN |
| RB | verify | opal-gateway | CTO C1: ENV_KEYS_BEFORE == ENV_KEYS_AFTER (a missing key is a STOP and rollback); only TRANSCRIPT_MEETING_ALLOWLIST moved by value; /health 200; tool count unchanged; shipped md5 equal the release |  | OPEN |

## Log

- 20261009T145119Z OPENED by 0.7.0_AE_CloudOps~Z with 2 leg(s)
