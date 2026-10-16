# Deploy Completion Record
**Date opened:** 2026-10-16T20:08:11.797708+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T205516Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD1 window 4 (AR-y-375): ONE FWD-1 run on the r34g resident: mint the synthetic staff row fwd1-staff-r41b@opal.invalid (allowedFirmIds 49financial), sign in on the served 5174 portal, file ONE Analysis Request through the Ticket Center, poll read-only, remove the row; bound to addendum 4 COO blob 85115a4f03 and the CTO half signed @5337f4fda8; driver sha256 ed128153, mint helper sha256 f1c655c4; NO RETRY; nothing deleted; the ticket, input, request and objects stay as evidence
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | ONE users-table row in opal-users-v2 for fwd1-staff-r41b@opal.invalid (role user, test-filer, firm opal-capital, allowedFirmIds [49financial], exp 3 h), minted by the signed helper through the driver | MINT-OK READBACK-OK and the SCOPE line | mint rc 0 MINT-OK READBACK-OK at 20:34:40Z; SCOPE allowedFirmIds=49financial scope_all_firms=absent mfa=absent | CLOSED 20261016T205427Z |
| S | activation | ONE Analysis Request filed through the Ticket Center page by the driver: the form posts the upload (own retries) and up to four re-clicks of the SAME Submit; decisions file fixed | ticket id and request id recorded at the ticket answer | Submit clicked 20:34:53Z; the upload was refused NOT_AUTHORIZED at 20:34:57Z (ProspectOwnershipRefused: an on-behalf upload must name the firm advisor); NO ticket filed, 0 objects written, 0 resubmits; window spent, no retry | CLOSED 20261016T205427Z |
| P | verify | read-only poll up to 20 minutes for the four attachments; nothing pressed after the ticket answer | attachments count and run_report.json | NOT REACHED: no ticket answer, so no poll and no attachments (the driver's wait ended at 780 s); nothing pressed after the ticket step because it never arrived | CLOSED 20261016T205428Z |
| R | activation | removal of the run row (script finally, or by hand) and ABSENT by the email GSI and a ConsistentRead for the run address and the three probe viewers | eight ABSENT lines | row removed in the driver finally rc 0; F1 eight ABSENT lines (GSI and ConsistentRead for the run address and the three probe viewers) read at 20:5xZ after the run | CLOSED 20261016T205428Z |

## Log

- 20261016T200811Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261016T205427Z LEG M closed: mint rc 0 MINT-OK READBACK-OK at 20:34:40Z; SCOPE allowedFirmIds=49financial scope_all_firms=absent mfa=absent
- 20261016T205427Z LEG S closed: Submit clicked 20:34:53Z; the upload was refused NOT_AUTHORIZED at 20:34:57Z (ProspectOwnershipRefused: an on-behalf upl
- 20261016T205428Z LEG P closed: NOT REACHED: no ticket answer, so no poll and no attachments (the driver's wait ended at 780 s); nothing pressed after t
- 20261016T205428Z LEG R closed: row removed in the driver finally rc 0; F1 eight ABSENT lines (GSI and ConsistentRead for the run address and the three 
- 20261016T205516Z CLOSED -- all 4 legs proven
