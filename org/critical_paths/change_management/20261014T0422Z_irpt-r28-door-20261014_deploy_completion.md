# Deploy Completion Record
**Date opened:** 2026-10-14T04:22:45.316921+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R28b: upload door D1-D4 and C1 as ONE synthetic Opal-internal viewer (no allowedFirmIds, no partner row) under Addendum 1 (COO blob 909ca2c466) and 1b (COO blob fe221dfcf1, CTO half signed); one users row for one sitting removed after exp; two synthetic stored inputs stay
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | step 1 reads (addendum COO halves hashed, three legs at expected CodeSha256, census); IV key and email index ABSENT; write one users row (attribute_not_exists, active, internal class, NO allowedFirmIds); read back; mint one token, memory only | row PRESENT as designed, one token minted |  | OPEN |
| D | verify | D1 to D4 through the upload door as the internal viewer (selected_tenant=49financial), then C1 parseIrEnvelope on answer bodies only | per-arm record (status, code, sha256 only) |  | OPEN |
| X | activation | after exp: delete the row (attribute_exists); ABSENT by GSI and ConsistentRead within a bounded 5 minutes | two ABSENT lines |  | OPEN |

## Log

- 20261014T042245Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
