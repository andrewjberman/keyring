# Deploy Completion Record
**Date opened:** 2026-10-07T21:19:39.783854+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T212955Z
**Deploy:** ETFS_RIVALS round 24 (RIV-cu-1, the chart UI): five rivalfunds Lambdas at CLOUD f9f8334ef6, one republish of 2026-10-07 refresh_a1 false (halves: COO 47cbfebcf2, CTO db4ab8faec; J1 MET ADJUDICATION_v28 f97c41e692)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of C:/tmp/rv_apply24.tfplan: 5 aws_lambda_function.stage in place | five live CodeSha256 equal the plan after-set, MemorySize 3008, 5 of 5 | safe-apply rc=0, Apply complete 0 added 5 changed 0 destroyed (halt gate: the same 76 automated ledger nudges, all from deploy_ledger.py). list-functions 21:2xZ: 5 of 5 at MemorySize 3008; CodeSha256 daily 3BFfLeYC, fetch mHg1VZz2, canonical vTjVc2Ym, silver 0hmlWkob, publish 8PjWCoxj = the plan after-set; daily Active, LastUpdateStatus Successful | CLOSED 20261007T212534Z |
| L2 | verify | ONE republish etfs-rivalfunds-daily-lambda only publish-page date 2026-10-07 refresh_a1 false | return status OK plus REPORT Max Memory Used and Duration | invoke 21:25:34Z StatusCode 200, no FunctionError, status OK, batch rv-publish-1007r24, RequestId 4b61643e-d9f2-4bb1-b718-1d215c0da7c2; REPORT Duration 73,563.01 ms of 900 s, Memory Size 3008 MB, Max Memory Used 557 MB; one attempt | CLOSED 20261007T212955Z |
| L3 | verify | served read: C1 the same keys as round 23 and no other key under the product prefix in that minute; C2 one script block and its one fetch target; sizes against the prediction | the reads printed | round24/served_grade_2026-10-07.after_r24.json: manifest not older than index, 13 chart objects; index 1,693,555 B, audit 1,255,777 B, charts 5,675,727 B, 5,894 markers, each equal to the prediction; fund_sections 0 missing of 2,247. CTO C1: 32 keys written under rivalfunds/etfs/ since 21:24Z (round24/keys_written_r24.txt) in the same 8 classes and counts as round 23 recorded -- index, audit, manifest, 13 charts, 15 copies under revisions/<stamp> (index, manifest, 13 charts), one state record; no key outside platinum/page/date=2026-10-07 and state/publish_page/date=2026-10-07; a1_produced all three SKIPPED. A time-window re-list of round 23 cannot show its live keys (this run overwrote them), so the comparison is against round 23's ledger record. CTO C2: 1 script block on the page, 0 on the audit page; its one fetch target is /rivalfunds/<day>/chart/<fund>; no XMLHttpRequest, no import( | CLOSED 20261007T212955Z |

## Log

- 20261007T211939Z OPENED by 2.0.0_SA_COO~RV with 3 leg(s)
- 20261007T212534Z LEG L1 closed: safe-apply rc=0, Apply complete 0 added 5 changed 0 destroyed (halt gate: the same 76 automated ledger nudges, all from 
- 20261007T212955Z LEG L2 closed: invoke 21:25:34Z StatusCode 200, no FunctionError, status OK, batch rv-publish-1007r24, RequestId 4b61643e-d9f2-4bb1-b71
- 20261007T212955Z LEG L3 closed: round24/served_grade_2026-10-07.after_r24.json: manifest not older than index, 13 chart objects; index 1,693,555 B, audi
- 20261007T212955Z CLOSED -- all 3 legs proven
