# Deploy Completion Record
**Date opened:** 2026-10-12T04:06:47.624118+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bg-3: the SECOND apply -- ONE code leg redeploying opal-amgt-scoped-api from the MERGED pin ba22af15f5 (box/dell1 first-parent) carrying AMGT-bg-2's one-S3-client scoped_amgt.py (9b13bf0371d4 -> 9f72b58aa87e, pool 32), /15 dossier.py 7b67bf62afdd and bd-1's monthly_chatter.py 38e9511ccc9c unchanged; NO served byte moves; the cold first overlay request for ASML_NA and ADBE_US under 27 s after the apply and after a 15-minute quiet period; pair COO half @7d8d398673 + CTO half (msg 4262); GO msg 4263
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the pin read BY THIS SEAT in a DETACHED worktree: ba22af15f5 is a box/dell1 first-parent commit; r94_admission_table.py ba22af15f5 --pin 6e8dcaf414 shows exactly ONE member, scoped_amgt.py 9b13bf0371d4 -> 9f72b58aa87e, with dossier.py 7b67bf62afdd, monthly_chatter.py 38e9511ccc9c and opal_naming.py 3902e0e93ee4 byte-equal to the live package (a second member or any other blob is a STOP) | the outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK CAPTURE (the kept live package 7DUlZxhl.. downloaded and hash-checked) plus the pre-act sweep of every live worktree's open deploys and the change-management ledger | base64 sha equality + kept path + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; the source-map entry read BEFORE this act and compared with the live function | equal counts + the entry's fields before |  | OPEN |
| L4 | verify | PRE-ACT CAPTURES immediately before the apply: the timed route baseline and aw4_capture.py (95 names), in sequence, no other reader | capture counts, bytes per name, statuses, durations |  | OPEN |
| L5 | verify | BUILD from the DETACHED worktree at EXACTLY the pin and print the WHOLE content diff FIRST; the one admitted member by blob; any other member is a STOP | build sha + the whole content-diff list + off-list count + each blob |  | OPEN |
| L6 | activation | upload the built file, then ONE untargeted safe-apply on infra/aws/terraform/harvest/ with the plan read from the plan JSON; exactly ONE resource may move | plan counts from terraform show -json + the single resource named + apply output |  | OPEN |
| L7 | verify | the FIRST post-apply reads, single reader, replay FIRST: the timed route replay (its position-1 ASML_NA and position-3 ADBE_US overlay are the cold first requests, each 200 and under 27 s), then aw4_capture and ay4_compare: NO served byte moves (status moved 0, paths outside clocks 0, growth 0 for every name), every request over 20 s re-invoked 3x | the cold durations, the changed-path list, the bytes per name |  | OPEN |
| L8 | verify | AC1 (bd-1's serve kept), AC2 (ay4_compare: no served byte moved), AC3 (no-regression, dossier /15, CodeSha256 different) on the live function | get-function-configuration + the live check outputs |  | OPEN |
| L9 | verify | the COLD-FIRST-REQUEST ARM after a QUIET PERIOD of at least 15 minutes with no read of the function by any seat: the first overlay request of ASML_NA_Equity and ADBE_US_Equity, each 200 and under 27 s (27 to under 29 s with 3 identical re-invokes is recorded; a timeout or a differing re-invoke is Branch 2) | durations, statuses, request ids, the quiet period's start and end |  | OPEN |
| L10 | git | the record step: record-terraform-deploy.sh; entry printed before and after | commit hash + the entry's fields after |  | OPEN |
| L11 | verify | the CodeSha256 and apply time reported to the issuer; the hold released; the pin worktree and thesis captures disposed as the order says | the message ids and the final state |  | OPEN |

## Log

- 20261012T040647Z OPENED by 0.7.0_AE_CloudOps~RA1 with 11 leg(s)
