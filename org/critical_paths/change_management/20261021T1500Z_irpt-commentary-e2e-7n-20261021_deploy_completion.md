# Deploy Completion Record
**Date opened:** 2026-10-21T15:00:56.332636+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T151354Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-7N: one synthetic Overview with two kept unknown tickers BREIT and ZQXWVK on the r34t resident, via the API driver; PDF saved for the issuer outside the repository
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user and the synthetic advisor, login | A mint, A2 advisor, L login lines | A mint ok, A2 advisor ok, L login ok (15:02:57Z to 15:03:02Z) | CLOSED 20261021T151353Z |
| U | verify | upload the holdings (re-post while RESOLVING) and the Keep re-posts for BREIT and ZQXWVK (at most two), then the ticket | U line with keep and reasons, T line | upload ok tries=11 keep=sent n=1 87 s; door reasons TICKER_NOT_FOUND for BREIT and ZQXWVK printed; T ticket ok TCK-20261021-cc706caa | CLOSED 20261021T151353Z |
| S | verify | submit one Overview request, no comparables | S line | submit ok REQ-fcea18409c7a02212028c571, Overview, no comparables, 15:04:36Z | CLOSED 20261021T151353Z |
| P | verify | poll P1, P4, P6 kept rows; a job not READY is an answer | hops green or the answer named | P1 READY 15:05:49Z, P4 outcome=ATTACHED 15:07:08Z, P6 BREIT REPLACED proxy CTO, ZQXWVK NOT_ANALYSED; P2 P3 P5 green | CLOSED 20261021T151354Z |
| R | verify | Overview route /pdf, R3 save outside the repository, R5 placeholder page count | R, R3, R5 lines | route /pdf 200 PDF 43 pages; R3 263988 bytes sha256 0c2c05b7bc4a saved outside repo; R5 0 of 43 | CLOSED 20261021T151354Z |
| D | verify | delete only the recorded keys, residue listed with VersionIds | deleted n of m, residue file | deleted 17 of 25 recorded keys ABSENT; 8 S3 objects (9 versions) AccessDenied listed in residue_7n.json, rows IRPT_ANLREQ-D2-S258 and IRPT_ANLREQ-D2-S259 | CLOSED 20261021T151354Z |

## Log

- 20261021T150056Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
- 20261021T151353Z LEG A closed: A mint ok, A2 advisor ok, L login ok (15:02:57Z to 15:03:02Z)
- 20261021T151353Z LEG U closed: upload ok tries=11 keep=sent n=1 87 s; door reasons TICKER_NOT_FOUND for BREIT and ZQXWVK printed; T ticket ok TCK-20261
- 20261021T151353Z LEG S closed: submit ok REQ-fcea18409c7a02212028c571, Overview, no comparables, 15:04:36Z
- 20261021T151354Z LEG P closed: P1 READY 15:05:49Z, P4 outcome=ATTACHED 15:07:08Z, P6 BREIT REPLACED proxy CTO, ZQXWVK NOT_ANALYSED; P2 P3 P5 green
- 20261021T151354Z LEG R closed: route /pdf 200 PDF 43 pages; R3 263988 bytes sha256 0c2c05b7bc4a saved outside repo; R5 0 of 43
- 20261021T151354Z LEG D closed: deleted 17 of 25 recorded keys ABSENT; 8 S3 objects (9 versions) AccessDenied listed in residue_7n.json, rows IRPT_ANLRE
- 20261021T151354Z CLOSED -- all 6 legs proven
