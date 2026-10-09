# Deploy Completion Record
**Date opened:** 2026-10-09T11:26:04.046180+00:00
**Status:** OPEN
**Deploy:** OG-ap-3 step 3: gateway release r29 (91811b648a) over live r28 (aa75078e1b) -- one service restart
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PRE | verify | opal-gateway | live re-read by host md5 equals r28 aa75078e1b; a live sha other than r28 is a STOP, not a judgment call |  | OPEN |
| DEP | ec2-baked-asset | opal-gateway | safe-ec2-deploy of 91811b648a from C:/tmp/og-rel29 with DEPLOY_BASE_REF=aa75078e1b; one service restart |  | OPEN |
| VER | verify | opal-gateway | r29_verify.py after --expect-changed MAIL_BEARER,MAIL_BEARER_LABELS; md5 98/98; tools 66; consent 9; /health 200 |  | OPEN |
| CACHE | verify | opal-gateway | r29_bun_cache_count.py since deploy_started_utc MUST read 0 -- above 0 is a fetch and a rollback trigger (R45) |  | OPEN |
| MAN | git | infra/aws/ec2/EC2_MANIFEST.json | manifest entry recorded BY HAND (the wrapper own manifest commit is refused by the lane gate, expected); release_note holds r29 alone |  | OPEN |

## Log

- 20261009T112604Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
