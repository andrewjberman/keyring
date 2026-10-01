# Deploy Completion Record
**Date opened:** 2026-10-01T08:39:23.919017+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS item 4: E_18's scheduled trigger -- ONE key, s3://opal-data-bd/code/gold/gold_dispatch.sh, candidate blob 631d6e6f4a (commit 6f4bde6b6a, md5 d6ab79987610f5144ad393bcacb5b171) with the calendar guard switched off; halves COO+CTO SIGNED @985bae1fee (NEVER_WIDEN_HALF_REQUEST_SECCLASS_E18_TRIGGER_DISPATCHER_20261001.md); prior VersionId Ar2kBAqtNnkXz7BDSvRYOS7daMqTgYyM (ETag 6e6483449644bc600a7b9153c3e8fd37) is the rollback target, copy-object, no delete
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | window invariants read live before the put: runner stopped; next scheduled gold fire more than 30 minutes away; live VersionId and ETag | UTC-stamped reads | Read live before the put: runner i-01003b035d2988dfb stopped at 08:39:24Z and again at 08:41:21Z (the BD_THREAD_R3 exercise run completed 08:34:33Z, instance stopped 08:35:51Z); next scheduled gold fire bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *) = 23:00Z, 14 h 18 min after the put (bd-canonical-prices-daily 04:00Z; bd-gold-layer-monthly-trigger DISABLED); live key VersionId Ar2kBAqtNnkXz7BDSvRYOS7daMqTgYyM ETag 6e6483449644bc600a7b9153c3e8fd37 66,915 bytes (head-object 08:39Z); candidate file md5 d6ab79987610f5144ad393bcacb5b171. | CLOSED 20261001T084247Z |
| D | s3-prefix | opal-data-bd code/gold/gold_dispatch.sh: put-object of the git-show bytes | returned ETag d6ab7998...b171 + head-object readback + new VersionId | put-object 08:41:28Z of the git show 6f4bde6b6a bytes (content-type application/x-sh, AES256): returned ETag d6ab79987610f5144ad393bcacb5b171, new VersionId VikjYXAEPXBxYRenSPh6YfD_PuuHLvTM. Readback 08:42Z: head-object ETag d6ab7998...b171, 74,731 bytes; a streamed get of the key md5 d6ab79987610f5144ad393bcacb5b171; list-object-versions shows the prior version Ar2kBAqt... (ETag 6e648344...) kept as the rollback target. Runner stopped before and after. One key written; no other key touched. | CLOSED 20261001T084248Z |
| A | verify | acceptance on the first scheduled gold fire whose gate PROCEEDS: PHASE_B3b E_18 done rc=0 and phase complete; 0 CALGUARD lines; chain exit 0 with PHASE_B4 onward run; E_18 written/refused equals e18-scheduled rows gained. CTO additions: (1) read on EVERY proceeding fire until the round closes, rc!=0 is a row the same day; (2) a stop at or after PHASE_B3b and before PHASE_B4 rolls this act back first; (3) the first branch-B row is compared with the fallback's class for that ticker before the next fire | log lines from s3 logs/gold-layer + table read |  | OPEN |

## Log

- 20261001T083923Z OPENED by 2.0.0_SA_COO~M with 3 leg(s)
- 20261001T084247Z LEG P closed: Read live before the put: runner i-01003b035d2988dfb stopped at 08:39:24Z and again at 08:41:21Z (the BD_THREAD_R3 exerc
- 20261001T084248Z LEG D closed: put-object 08:41:28Z of the git show 6f4bde6b6a bytes (content-type application/x-sh, AES256): returned ETag d6ab7998761
