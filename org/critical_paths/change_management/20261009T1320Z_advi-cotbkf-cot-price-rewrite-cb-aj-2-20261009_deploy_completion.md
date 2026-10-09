# Deploy Completion Record
**Date opened:** 2026-10-09T13:20:50.316875+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF round 36 CB-aj-2: write ONE NEW VERSION of each of 38 cot price keys in opal-data-cot silver/prices/ (49F rows removed, 3 bonds UNPRICED), as built from CB-aj-1's manifest, under never-widen pair COO half @2f2f1e52aa + CTO half @a614350d84 GIVEN under conditions 1-5. NO VERSION DELETED -- deletes are Andrew's act (condition 5)
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | verify | CTO condition 2 STOP GATE -- read the cot code mirror code/gold/ in opal-data-cot ONE OBJECT AT A TIME, closing the BLIND | the full object denominator printed; ZERO writers of silver/prices/ and ZERO readers of another firm's price input, graded against the ratified cross-firm enumeration for a data/cot/ script; any hit is a STOP and nothing is written |  | OPEN |
| C2 | verify | CTO condition 3 STOP GATE -- cite the gold chain's code line that values a holding with no price on a date | the line cited by path and number; it must mark the holding missing/NaN/excluded WITH A REASON to proceed; valuing at 0 or carrying a stale price forward unflagged is a STOP; on proceed, name the count of gold account-days the next run moves for 05613L3H2, 95000U2D4, 651639AX4 |  | OPEN |
| C3 | verify | preflight comp-schedule -- re-read CB-aj-1's writer census at apply time | writers=7 scheduled=0 still holds; a scheduled writer of silver/prices/ enabled since CB-aj-1 stops the apply |  | OPEN |
| W1 | activation | the 38 writes: per key re-read the prior VersionId and STOP on change, put the local file as built, record the new VersionId, read back and confirm sha256 equals the manifest | 38 of 38 keys written with prior VersionId matched before each write and served sha256 equal to the manifest after it; no version deleted |  | OPEN |
| V1 | verify | CB36aj2-AC1 -- commonwealth_cot_price_rewrite.py --verify-served | COT-PRICE-REWRITE-VERIFY keys=38 AND match=38/38 with rc 0; keys=38 alone is not the bar, because the printed line carries keys=38 even when every key mismatches |  | OPEN |

## Log

- 20261009T132050Z OPENED by 0.7.0_AE_CloudOps~CB2 with 5 leg(s)
