# Deploy Completion Record
**Date opened:** 2026-10-06T21:42:03.820971+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T215736Z
**Deploy:** MX-s-17: point opal-bd-transaction-download and opal-bd-realized-download at code/silver/merge-daily-incremental.py (never-widen halves CTO @fb8486aa9f + COO @27501e83dd)
**Authored by:** 0.7.0_AE_CloudOps~MI
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S9 | verify | read-only SSM import check (boto3+pandas) on the documents target instance -- Z-W24-S9 disarm | yes | MEASURED ON BOTH TARGET INSTANCES, and they DISAGREE. i-0800437d1dbb0b5cc (realized, command 7ffa4edf-7a1e-4db3-87a4-df3d027ec7a6): Status Success, ResponseCode 0, stdout 'OK: 1.42.97 2.3.3'. i-00c7568bc510f7423 (transaction, command fd0656b1-d849-4859-b03f-c57c8bda3292): Status Failed, ResponseCode 1, stderr "ModuleNotFoundError: No module named 'boto3'". ModuleNotFoundError subclasses ImportError, so A1's BLOCKING branch fires: nothing published. Both reads were taken while the boxes were up on their own 21:45Z/21:53Z schedule; no instance was started. | CLOSED 20261006T215618Z |
| D1 | activation | opal-bd-transaction-download v4 set DEFAULT, Default==Latest read back | yes | NOT APPLIED. No update-document was issued for opal-bd-transaction-download. Served state re-read after the decision: DefaultVersion 3 = LatestVersion 3, Active -- unchanged from the base pin. Blocked by leg S9's measured ImportError on this document's own target instance i-00c7568bc510f7423, per amendment A1's BLOCKING branch. | CLOSED 20261006T215619Z |
| D2 | activation | opal-bd-realized-download v4 set DEFAULT, Default==Latest read back | yes | NOT APPLIED. No update-document was issued for opal-bd-realized-download. Served state re-read after the decision: DefaultVersion 3 = LatestVersion 3, Active -- unchanged from the base pin. Its own instance i-0800437d1dbb0b5cc passed the import check, but the two documents are one signed act and NEVER-2 forbids a half-landed deploy, so neither was published. | CLOSED 20261006T215619Z |

## Log

- 20261006T214203Z OPENED by 0.7.0_AE_CloudOps~MI with 3 leg(s)
- 20261006T215618Z LEG S9 closed: MEASURED ON BOTH TARGET INSTANCES, and they DISAGREE. i-0800437d1dbb0b5cc (realized, command 7ffa4edf-7a1e-4db3-87a4-df3
- 20261006T215619Z LEG D1 closed: NOT APPLIED. No update-document was issued for opal-bd-transaction-download. Served state re-read after the decision: De
- 20261006T215619Z LEG D2 closed: NOT APPLIED. No update-document was issued for opal-bd-realized-download. Served state re-read after the decision: Defau
- 20261006T215736Z CLOSED -- all 3 legs proven
