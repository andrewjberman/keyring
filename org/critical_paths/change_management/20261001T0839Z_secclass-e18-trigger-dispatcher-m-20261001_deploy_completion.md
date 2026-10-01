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
| P | verify | window invariants read live before the put: runner stopped; next scheduled gold fire more than 30 minutes away; live VersionId and ETag | UTC-stamped reads |  | OPEN |
| D | s3-prefix | opal-data-bd code/gold/gold_dispatch.sh: put-object of the git-show bytes | returned ETag d6ab7998...b171 + head-object readback + new VersionId |  | OPEN |
| A | verify | acceptance on the first scheduled gold fire whose gate PROCEEDS: PHASE_B3b E_18 done rc=0 and phase complete; 0 CALGUARD lines; chain exit 0 with PHASE_B4 onward run; E_18 written/refused equals e18-scheduled rows gained. CTO additions: (1) read on EVERY proceeding fire until the round closes, rc!=0 is a row the same day; (2) a stop at or after PHASE_B3b and before PHASE_B4 rolls this act back first; (3) the first branch-B row is compared with the fallback's class for that ticker before the next fire | log lines from s3 logs/gold-layer + table read |  | OPEN |

## Log

- 20261001T083923Z OPENED by 2.0.0_SA_COO~M with 3 leg(s)
