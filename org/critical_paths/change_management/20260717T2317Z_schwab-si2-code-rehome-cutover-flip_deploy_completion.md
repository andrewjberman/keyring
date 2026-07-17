# Deploy Completion Record
**Date opened:** 2026-07-17T23:17:58.602403+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260717T231803Z
**Deploy:** WP8-DECOM cell 3 CUTOVER: flip SI2 code-pull literals opal-data-schwab/_ops -> opal-data-assets/code (byte-identical, behavior-neutral; old grant+data HELD to D5)
**Authored by:** 0.6.2_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | flip commit on CLOUD | hash pushed | flip commit 66e6be74d pushed to CLOUD (tf:119 + bootstrap.ps1:40 -> opal-data-assets/code/canonical-schwab-si2 + DoR doc-sync) | CLOSED 20260717T231758Z |
| L2 | verify | 0.5.0 GO(1) + CTO apply-gate | both cleared | 0.5.0 GO(1) 222210Z (flips orthogonal to D1 parity clock); CTO apply-gate granted 205035Z | CLOSED 20260717T231759Z |
| L3 | verify | byte-identity repo==old==new | MD5 + size | MD5 0017f9b549ca9f8013704f50c4327bed / 35842B identical across repo + opal-data-schwab/_ops (old) + opal-data-assets/code (new) -- flip behavior-neutral | CLOSED 20260717T231800Z |
| L4 | activation | safe-apply the 2 SSM-target flips | 0-add/2-change/0-destroy + 0-diff + live target confirmed | safe-apply Apply complete 0 added/2 changed/0 destroyed; re-plan No changes; live list-targets-by-rule 08242234 = $s3='s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1' | CLOSED 20260717T231800Z |
| L5 | verify | prove-on-fire behavior-neutral + code-read proven | SSM pull from new home == pre-flip fire; guard-FATAL pre-existing+orthogonal | SSM 08242234 pull from new home (CID a5af639c): CredRead OK, enum=230/skip=230/dl=0/fail=0 == pre-flip 22:15Z fire (behavior-neutral). rc=6 guard-FATAL is PRE-EXISTING since 07-16 22:15Z (~24h pre-flip) + ORTHOGONAL (01_raw double-occupancy in bronze DATA, source-confirmed bronze/upt/20260622 = 2 objects) -- 0.5.0's item, NOT the flip | CLOSED 20260717T231801Z |
| L6 | verify | 0.5.0 WP8-lead cutover cert | ACCEPTED, leg CLOSED | 0.5.0 WP8-lead cert ACCEPTED 230929Z: flip DONE (byte-identical/behavior-neutral/code-read-proven); guard-FATAL is their separate 01_raw item; leg CLOSED | CLOSED 20260717T231802Z |

## Log

- 20260717T231758Z OPENED by 0.6.2_AE_PartnerETL with 6 leg(s)
- 20260717T231758Z LEG L1 closed: flip commit 66e6be74d pushed to CLOUD (tf:119 + bootstrap.ps1:40 -> opal-data-assets/code/canonical-schwab-si2 + DoR doc
- 20260717T231759Z LEG L2 closed: 0.5.0 GO(1) 222210Z (flips orthogonal to D1 parity clock); CTO apply-gate granted 205035Z
- 20260717T231800Z LEG L3 closed: MD5 0017f9b549ca9f8013704f50c4327bed / 35842B identical across repo + opal-data-schwab/_ops (old) + opal-data-assets/cod
- 20260717T231800Z LEG L4 closed: safe-apply Apply complete 0 added/2 changed/0 destroyed; re-plan No changes; live list-targets-by-rule 08242234 = $s3='s
- 20260717T231801Z LEG L5 closed: SSM 08242234 pull from new home (CID a5af639c): CredRead OK, enum=230/skip=230/dl=0/fail=0 == pre-flip 22:15Z fire (beha
- 20260717T231802Z LEG L6 closed: 0.5.0 WP8-lead cert ACCEPTED 230929Z: flip DONE (byte-identical/behavior-neutral/code-read-proven); guard-FATAL is their
- 20260717T231803Z CLOSED -- all 6 legs proven
