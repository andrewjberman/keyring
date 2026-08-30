# Deploy Completion Record
**Date opened:** 2026-08-30T05:54:31.453602+00:00
**Status:** OPEN
**Deploy:** ADVI_49F.C02-g-7 B-4: FORWARD PRODUCTION of the five never-produced dates 2026-08-11/12/13/14/17 on the FULL 49F chain via advi-49f-chain-dispatch, oldest-first. 5 dates x 18 gold tables = 87 NEW keys + 3 DECLARED overwrites at 08-11 (dim_boundary/dim_calendar/dim_security, from the 2026-08-19T01:13:37Z ad-hoc run). Never-widen BOTH halves signed on one shape: CTO 86149 (A)(B)(C), COO 86183 + (C) word 86229. Build-only: the perfrp projection writes 0 S3 keys (world: 0 platinum objects in the bucket).
**Authored by:** 0.7.0_AE_CloudOps~L
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | verify | date-list control BEFORE the first send | derived (dim_calendar trading days MINUS stored twr_daily, never flow_ledger) printed with its denominator and EQUAL to the pre-registered five, else REFUSE | PASS, re-run AT SEND TIME (08:0xZ) rather than trusted from the plan 90 min earlier. stored twr_daily 535; dim_calendar trading days in span 539 (DENOMINATOR); derived = calendar MINUS stored = 5 -> 2026-08-11, 08-12, 08-13, 08-14, 08-17; pre-registered = identical. Note the control is a SET difference and not arithmetic: 539-535=4, not 5, because 2025-01-09 is a STORED non-trading day. Per CTO 86149 (B) a mismatch would have REFUSED the run before the first send. | CLOSED 20260830T081401Z |
| G2 | verify | the five new twr_daily partitions | exist, POPULATED as pre-registered, gross_leg_vintage 946b5c5a3c, schema_version 1.2, no OK row with bmv<0 |  | OPEN |
| G3 | verify | existing 535 twr_daily UNTOUCHED | 0 new versions on any of the 535, prior VersionId by time, the f862baac5a instrument |  | OPEN |
| G4 | verify | 18-table write set, enumerated | 0 new versions on every chain table EXCEPT the five date partitions in each; +5 keys per table printed; the 3 declared 08-11 overwrites on their OWN line with before/after row count, column set and content hash |  | OPEN |
| G5 | verify | 2026-08-18 re-emitted LAST on the c02 mirror-pull | its D-1 (08-17) exists for the first time; pre-registered POPULATED; a refusal is a finding stated with its status |  | OPEN |
| G6 | verify | process | mutex limb (ii) re-read before EVERY date with the limb printed; readers of all 18 tables announced before the first send; proof VALID rc=0 unpiped with the checker vintage |  | OPEN |

## Log

- 20260830T055431Z OPENED by 0.7.0_AE_CloudOps~L with 6 leg(s)
- 20260830T081401Z LEG G1 closed: PASS, re-run AT SEND TIME (08:0xZ) rather than trusted from the plan 90 min earlier. stored twr_daily 535; dim_calendar 
