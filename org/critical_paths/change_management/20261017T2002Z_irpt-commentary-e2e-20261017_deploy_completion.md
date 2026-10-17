# Deploy Completion Record
**Date opened:** 2026-10-17T20:02:36.881714+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E: ONE fresh synthetic commentary run end to end (one synthetic staff user, one upload, one ticket, one request, resident, drafter, packager, commentary route read), then delete by recorded key; COO half blob 394e573a4a, CTO half f0fbfde004; nothing deployed
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | activation | mint the one synthetic staff user (opal-users-v2) and record every key created | mint read-back present |  | OPEN |
| S | activation | login, upload, ticket and submit once each as the synthetic actor | closed states and the REQ id |  | OPEN |
| P | verify | poll job READY, commentary_ref, draft artifact, packager line, PDF artifact within the 30 minute budget | the hop results |  | OPEN |
| R | verify | the commentary-pdf route read as the same user | pass or the closed code |  | OPEN |
| D | activation | delete exactly the recorded synthetic keys, each read back ABSENT | keys deleted of recorded |  | OPEN |

## Log

- 20261017T200236Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
