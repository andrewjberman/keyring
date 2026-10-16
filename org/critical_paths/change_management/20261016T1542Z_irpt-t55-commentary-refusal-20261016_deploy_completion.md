# Deploy Completion Record
**Date opened:** 2026-10-16T15:42:14.354299+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-t55 (AR-tf-78): drive ONE COMMENTARY hop refusal on the synthetic job row irpt-jobs 49financial REQ-d47252fe74634d0c5cdd8067: LEG A one direct invoke of outlook-global-commentary-draft-lambda with a WRONG_KIND body, the live fail op sets hop_failure {COMMENTARY, COMMENTARY_DRAFT_REFUSED, at}; the attribute STAYS until the issuer's leg-B message, then LEG B one conditional REMOVE of that attribute and the read-back ABSENT with the PRE-equal item hash; no deploy, no model call, no queue message; COO half and CTO ruling in the CTO round analysis @90926d9683
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | ONE invoke of the commentary function and the row read back with hop_failure set | preconditions green, the parsed answer, the HOP-FAILURE-REPORTED log line, the row hop_failure keys and at, state READY, hash without the attribute equals PRE, R55-HOPLOG-OK |  | OPEN |
| B | verify | ONE conditional REMOVE of hop_failure on the same row (only on the issuer's message citing this order) | read-back ABSENT, item hash equals PRE, R55-HOPABSENT-OK |  | OPEN |

## Log

- 20261016T154214Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 2 leg(s)
