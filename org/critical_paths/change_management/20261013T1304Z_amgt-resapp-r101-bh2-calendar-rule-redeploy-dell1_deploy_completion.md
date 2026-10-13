# Deploy Completion Record
**Date opened:** 2026-10-13T13:04:02.041282+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bh-2: ONE code leg redeploying opal-amgt-scoped-api from the MERGED pin 7da642c1ff (box/dell1 first-parent) carrying AMGT-bh-1's calendar rule, lib/research/freshness/snapshot.py f8df11bd6cce -> 64fa354a1e1c; scoped_amgt.py 9f72b58aa87e, dossier.py 7b67bf62afdd and monthly_chatter.py 38e9511ccc9c unchanged; live must read 42z0tn68.. first; no served byte moves (today's snapshot is current by both rules); rollback is a REBUILD from ba22af15f5; pair COO half @6d7a29efb8 + CTO half (msg 4356); GO msg 4823
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the pin read BY THIS SEAT in a DETACHED worktree: 7da642c1ff is a box/dell1 first-parent commit; r94_admission_table.py 7da642c1ff --pin ba22af15f5 prints EXACTLY ONE member, lib/research/freshness/snapshot.py f8df11bd6cce -> 64fa354a1e1c (any other member or blob is a STOP); r94_naming_replay.py --pin ba22af15f5 from the pin reads YES; the live CodeSha256 read first and equal to 42z0tn68.. | the outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK: the function keeps only LATEST, so the rollback is a REBUILD from merged pin ba22af15f5 -- its blob table printed BEFORE the apply -- plus the live package downloaded and hash-checked as a reference; the pre-act sweep of every live worktree's open deploys and the change-management ledger | the blob table + base64 sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; the source-map entry read BEFORE this act and compared with the live function | equal counts + the entry's fields before |  | OPEN |
| L4 | verify | PRE-ACT CAPTURES immediately before the apply: the timed route baseline and aw4_capture.py (95 names), in sequence, no other reader; the snapshot's generated_at and age read | capture counts, bytes per name, statuses, durations |  | OPEN |
| L5 | verify | BUILD from the DETACHED worktree at EXACTLY the pin and print the WHOLE content diff FIRST; the one admitted member by blob; any other member is a STOP | build sha + the whole content-diff list + off-list count + each blob |  | OPEN |
| L6 | activation | upload the built file, then ONE untargeted safe-apply on infra/aws/terraform/harvest/ with the plan read from the plan JSON; exactly ONE resource may move | plan counts from terraform show -json + the single resource named + apply output |  | OPEN |
| L7 | verify | the FIRST post-apply reads, single reader: the first overlay requests (ASML_NA_Equity, ADBE_US_Equity, a simultaneous pair) with the snapshot's generated_at and age, then the timed route replay and aw4_capture/ay4_compare: no served byte moves (status moved 0, paths outside clocks 0, growth 0), every request over 27 s re-invoked 3x | the first-request handler times, the changed-path list, the bytes per name |  | OPEN |
| L8 | verify | AC1 (bd-1's serve kept), AC2 (ay4_compare: no served byte moved), AC3 (r101_snapshot_equal, r101_cold_live, r89_deployed_close /15) on the live function | get-function-configuration + the live check outputs |  | OPEN |
| L9 | git | the record step: record-terraform-deploy.sh; entry printed before and after | commit hash + the entry's fields after |  | OPEN |
| L10 | verify | the CodeSha256 and apply time reported to the issuer; the hold released; the pin worktree and thesis captures disposed as the order says | the message ids and the final state |  | OPEN |

## Log

- 20261013T130402Z OPENED by 0.7.0_AE_CloudOps~RA1 with 10 leg(s)
