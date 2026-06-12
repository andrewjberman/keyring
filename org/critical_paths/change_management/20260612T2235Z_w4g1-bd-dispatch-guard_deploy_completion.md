# Deploy Completion Record
**Date opened:** 2026-06-12T22:35:53.456224+00:00
**Status:** OPEN
**Deploy:** W4-G1: bd gold_dispatch.sh concurrency-aware shutdown arm (#9 port, both arm sites)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| commit | git | gold_dispatch.sh on CLOUD | hash pushed |  | OPEN |
| bd-gold-dispatch | s3-prefix | s3://opal-data-bd/code/gold/gold_dispatch.sh (runner syncs code/gold at boot -- S3 IS the activation) | sha256 deployed-diff MATCH |  | OPEN |
| verify | verify | bash -n + sim + next scheduled run log shows SHUTDOWN_ARMED | sim output + morning cue |  | OPEN |

## Log

- 20260612T223553Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
