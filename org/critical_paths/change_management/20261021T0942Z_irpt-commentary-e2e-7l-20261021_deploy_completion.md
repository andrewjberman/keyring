# Deploy Completion Record
**Date opened:** 2026-10-21T09:42:14.546681+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T095445Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-7L: one synthetic Overview with the kept unknown ticker ZQXWVK on the r34s resident, via the API driver; PDF saved for the issuer outside the repository
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user and the synthetic advisor, login | A mint, A2 advisor, L login lines | A mint, A2 advisor ok, L login ok (09:43:49Z to 09:43:54Z) | CLOSED 20261021T095444Z |
| U | verify | upload the holdings (re-post while RESOLVING) and the Keep re-post for ZQXWVK, then the ticket | U line with keep and reason, T line | upload ok tries=9 keep=sent 49 s; door reason TICKER_NOT_FOUND for ZQXWVK printed; T ticket ok TCK-20261021-553ca002 | CLOSED 20261021T095445Z |
| S | verify | submit one Overview request, no comparables | S line | submit ok REQ-de7555f49544199204061b8a, Overview, no comparables, 09:44:54Z | CLOSED 20261021T095445Z |
| P | verify | poll P1, P4, P6 kept-row; a job not READY is an answer | hops green or the answer named | P1 READY 09:45:21Z, P4 outcome=ATTACHED 09:47:00Z, P6 UNRESOLVED/KEPT_AS_TYPED swap NOT_ANALYSED, P2 P3 P5 green | CLOSED 20261021T095445Z |
| R | verify | Overview route /pdf, R3 save outside the repository, R5 placeholder page count | R, R3, R5 lines | route /pdf 200 PDF 42 pages; R3 260336 bytes sha256 be9b2b7bc891 saved outside repo; R5 0 of 42 | CLOSED 20261021T095445Z |
| D | verify | delete only the recorded keys, residue listed with VersionIds | deleted n of m, residue file | deleted 17 of 25 recorded keys ABSENT; 8 S3 objects (9 versions) AccessDenied listed in residue_7l.json, row S255 | CLOSED 20261021T095445Z |

## Log

- 20261021T094214Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
- 20261021T095444Z LEG A closed: A mint, A2 advisor ok, L login ok (09:43:49Z to 09:43:54Z)
- 20261021T095445Z LEG U closed: upload ok tries=9 keep=sent 49 s; door reason TICKER_NOT_FOUND for ZQXWVK printed; T ticket ok TCK-20261021-553ca002
- 20261021T095445Z LEG S closed: submit ok REQ-de7555f49544199204061b8a, Overview, no comparables, 09:44:54Z
- 20261021T095445Z LEG P closed: P1 READY 09:45:21Z, P4 outcome=ATTACHED 09:47:00Z, P6 UNRESOLVED/KEPT_AS_TYPED swap NOT_ANALYSED, P2 P3 P5 green
- 20261021T095445Z LEG R closed: route /pdf 200 PDF 42 pages; R3 260336 bytes sha256 be9b2b7bc891 saved outside repo; R5 0 of 42
- 20261021T095445Z LEG D closed: deleted 17 of 25 recorded keys ABSENT; 8 S3 objects (9 versions) AccessDenied listed in residue_7l.json, row S255
- 20261021T095445Z CLOSED -- all 6 legs proven
