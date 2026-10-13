# Deploy Completion Record
**Date opened:** 2026-10-13T15:21:17.730981+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T154403Z
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R21: driven exercise of the status rule on irpt-directory-search: synthetic internal identities norow, disabled (and active) select cottonwood through the live edge; rows written for the sitting and removed; pair COO blob d1d4296341 + CTO half @decdd94c48 (choice A)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| E1 | verify | step 0: grants met, open-entry denominator (no open entry naming opal-users-v2 or irpt-directory-search); pair step 1: three USER# keys ABSENT by ConsistentRead and the email index returns nothing | reads printed | Pair blob d1d4296341 verified; CTO half @decdd94c48 (choice A, executor AQ2). Grants read by simulate-principal-policy for cloudops-dell2-agent-user, one resource per call: dynamodb GetItem/PutItem/DeleteItem on opal-users-v2 allowed, Query on email-index allowed, secretsmanager GetSecretValue on opal/auth/jwt-private-key-Av5dZz allowed (secret exists, describe-secret), logs FilterLogEvents on irpt-directory-search allowed (also used for A4); note the simulator also allowed a nonsense table, so it proves only the pattern; the real calls prove the rest. Denominator: 50 worktrees, 104 entries, 2 name opal-users-v2 or irpt-directory-search, both CLOSED on trunk. Pair step 1: the three USER# keys read ABSENT by ConsistentRead GetItem and the email-index Count is 0 for all three (the GSI read is positive-controlled by the written rows at step 2). | CLOSED 20261013T152230Z |
| E2 | activation | write disabled and active rows (attribute_not_exists(PK), with email); ConsistentRead each back | two items PRESENT as designed | Rows written 15:27:04Z with attribute_not_exists(PK): disabled (status disabled) and active (status active), each with email = its address, firmId opal-capital, userType test-filer, allowedFirmIds [cottonwood]; both read back PRESENT as designed by ConsistentRead; GSI positive control: the disabled row appeared on the email index. norow wrote nothing. | CLOSED 20261013T154239Z |
| E3 | verify | one token per identity (held in process only), three GETs norow then disabled then active-only-if-both-refused, >=60s apart; UTC start, status, refusal code, body sha256 | per-request record | Three requests, one token each (norow 15:27:04Z exp 15:39:04Z; disabled 15:28:45Z and active 15:29:50Z with life 300 s), held in memory only, never written; spacing 101 s and 65 s. norow: status 200, body sha cd0365b1.. ; disabled: status 200, REFUSED FIRM_BINDING, same body sha; active: status 200 ADMITTED, body sha e704b99c... Deviation: phase 1 classified a refusal only on a 4xx, so it stopped after norow; the function's own log said refused; phase 2 continued the same sitting on the same rows (second signing-key read). No body kept. Records EXERCISE_RESULT.txt, EXERCISE_TRACE.txt, EXERCISE_PHASE2_TRACE.txt. | CLOSED 20261013T154239Z |
| E4 | verify | per-sub-window INTERNAL-CALLER-CLASS counts with streams denominator | one line per sub-window with the expected class | Class lines per sub-window: norow 1 (row_absent/refused) MATCH; disabled 4 = 1 row_non_active/refused + 3 row_present/admitted from a second invocation not made by this seat -> FAIL on the count per the pair (surprise row IRPT_ANLREQ-D2-S74); active 1 (row_present/admitted) MATCH. Streams denominator: the executors' own read printed 0 (VOID, unreliable lastEventTimestamp); replaced by a filter read: 30 events in 3 streams for the sitting window. | CLOSED 20261013T154240Z |
| E5 | activation | after later exp: delete written rows (attribute_exists(PK)); all three addresses ABSENT by GSI and ConsistentRead | six ABSENT reads | Both written rows deleted 15:39:09Z with attribute_exists(PK), after the later exp (15:39:04Z); all three addresses read ABSENT by the email-index GSI and by ConsistentRead (6 of 6 ABSENT lines), repeated independently at ~15:41Z. EXERCISE_REMOVAL.txt. | CLOSED 20261013T154240Z |
| E6 | verify | counts to 1.0.0_SA_CTO~DELL2, report to 2.0.0_SA_COO~Y2, signing-key read reported via 0.0.0_AB_MSTR~DELL2 | messages sent | Counts sent to 1.0.0_SA_CTO~DELL2 (msg 7035) and 2.0.0_SA_COO~Y2 (7036); signing-key reads (2, at 15:27:04Z and 15:28:44Z) reported to 0.0.0_AB_MSTR~DELL2. | CLOSED 20261013T154403Z |

## Log

- 20261013T152117Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
- 20261013T152230Z LEG E1 closed: Pair blob d1d4296341 verified; CTO half @decdd94c48 (choice A, executor AQ2). Grants read by simulate-principal-policy f
- 20261013T154239Z LEG E2 closed: Rows written 15:27:04Z with attribute_not_exists(PK): disabled (status disabled) and active (status active), each with e
- 20261013T154239Z LEG E3 closed: Three requests, one token each (norow 15:27:04Z exp 15:39:04Z; disabled 15:28:45Z and active 15:29:50Z with life 300 s),
- 20261013T154240Z LEG E4 closed: Class lines per sub-window: norow 1 (row_absent/refused) MATCH; disabled 4 = 1 row_non_active/refused + 3 row_present/ad
- 20261013T154240Z LEG E5 closed: Both written rows deleted 15:39:09Z with attribute_exists(PK), after the later exp (15:39:04Z); all three addresses read
- 20261013T154403Z LEG E6 closed: Counts sent to 1.0.0_SA_CTO~DELL2 (msg 7035) and 2.0.0_SA_COO~Y2 (7036); signing-key reads (2, at 15:27:04Z and 15:28:44
- 20261013T154403Z CLOSED -- all 6 legs proven
