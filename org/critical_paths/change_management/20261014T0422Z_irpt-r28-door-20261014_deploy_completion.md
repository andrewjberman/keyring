# Deploy Completion Record
**Date opened:** 2026-10-14T04:22:45.316921+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T044404Z
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R28b: upload door D1-D4 and C1 as ONE synthetic Opal-internal viewer (no allowedFirmIds, no partner row) under Addendum 1 (COO blob 909ca2c466) and 1b (COO blob fe221dfcf1, CTO half signed); one users row for one sitting removed after exp; two synthetic stored inputs stay
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | step 1 reads (addendum COO halves hashed, three legs at expected CodeSha256, census); IV key and email index ABSENT; write one users row (attribute_not_exists, active, internal class, NO allowedFirmIds); read back; mint one token, memory only | row PRESENT as designed, one token minted | Step 1: Addendum 1 COO blob 909ca2c466 and Addendum 1b COO blob fe221dfcf1 hashed at HEAD, CTO halves read (1b signed, CTO msg 7516); irpt-status, opal-ticket-api, irpt-ycharts-generate at their expected CodeSha256 (EQUAL, 04:23:32Z); census 39 worktrees, 105 distinct open-deploy entries (688 copies), 5 name opal-users-v2 or irpt-ycharts-generate and all 5 are CLOSED on trunk with no trunk open entry (stale worktree copies only), so no STOP. IV key and email index ABSENT. One users row written 04:23:33Z (attribute_not_exists, status active, internal class firmId opal-capital, NO allowedFirmIds) and read back PRESENT as designed. Signing key read once; one token minted 04:23:33Z, exp 04:42:33Z (1140 s), memory only, never written. | CLOSED 20261014T044404Z |
| D | verify | D1 to D4 through the upload door as the internal viewer (selected_tenant=49financial), then C1 parseIrEnvelope on answer bodies only | per-arm record (status, code, sha256 only) | The door ADMITTED the internal viewer on every request (function log INTERNAL-CALLER-CLASS class=row_present outcome=admitted x6, no InputAccessDenied). D1 200 NEEDS_CORRECTION ACCOUNT_COLUMN_SEVERAL_VALUES (as expected). D2 200 NORMALIZED (RESOLVING first, then NORMALIZED). D3 FAIL: 200 NEEDS_CORRECTION, not NORMALIZED; the reason is INFERRED from the code (resident composes no Shares price source, SHARES_PRICE_SOURCE_NOT_COMPOSED, pinned by test_deferred_resolution.py:172), the sitting kept state only; row IRPT_ANLREQ-D2-S94. D4 200 NORMALIZED, same input id as D2 (re-open accepted). C1: the D1, D2, D3 bodies were all answer bodies and PARSED by parseIrEnvelope from portal origin/PROD 10e7664d6c. Six door posts in all (D2 and D3 each re-posted once while RESOLVING). Stored inputs: D2 only (D3 stored nothing). DOOR_RESULT.txt has 4 of 5 expected lines. | CLOSED 20261014T044404Z |
| X | activation | after exp: delete the row (attribute_exists); ABSENT by GSI and ConsistentRead within a bounded 5 minutes | two ABSENT lines | Row deleted 04:42:38Z with attribute_exists, after exp 04:42:33Z; the email-index GSI and a ConsistentRead both ABSENT on the first read inside the printed 5-minute window (2 of 2 lines in DOOR_REMOVAL.txt); re-read independently by this seat at 04:43Z: GSI count 0, ConsistentRead ABSENT. The D2 synthetic stored input stays (49financial). | CLOSED 20261014T044404Z |

## Log

- 20261014T042245Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
- 20261014T044404Z LEG M closed: Step 1: Addendum 1 COO blob 909ca2c466 and Addendum 1b COO blob fe221dfcf1 hashed at HEAD, CTO halves read (1b signed, C
- 20261014T044404Z LEG D closed: The door ADMITTED the internal viewer on every request (function log INTERNAL-CALLER-CLASS class=row_present outcome=adm
- 20261014T044404Z LEG X closed: Row deleted 04:42:38Z with attribute_exists, after exp 04:42:33Z; the email-index GSI and a ConsistentRead both ABSENT o
- 20261014T044404Z CLOSED -- all 3 legs proven
