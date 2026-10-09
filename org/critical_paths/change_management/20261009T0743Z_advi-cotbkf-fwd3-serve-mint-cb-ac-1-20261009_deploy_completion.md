# Deploy Completion Record
**Date opened:** 2026-10-09T07:43:26.212610+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF round 29 CB-ac-1: MINT the three FWD-3 silver tables under s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/ via commonwealth_fwd3_serve.py --apply, under never-widen pair CTO half (AMENDMENT 1 @478334e021) + COO half GIVEN
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P0 | verify | before-state of the three target prefixes + positive control | all three prefixes hold 0 objects and the control commonwealth/cottonwood/silver/transactions/date=2026-06-23/ holds 14, so the zero is a real absence; IAM preflight recorded with its measured limit | BEFORE-STATE MEASURED 20261009T0740Z by 0.7.0_AE_CloudOps~CB2 (user/cloudops-dell2-agent-user, acct 313476888478). All three target prefixes hold ZERO objects: list-objects-v2 --bucket opal-data-assets --prefix commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/ returns no Contents key for each. POSITIVE CONTROL in the same loop: .../silver/transactions/date=2026-06-23/ returns 14, so the instrument reads objects where objects exist and the three zeros are a REAL ABSENCE, not a mangled prefix. The write therefore MINTS and moves no served output. ADDRESSES: all three equal lib/opal_naming.address output with addresses_from_builder=True, and they equal the three keys of the COO half section 1 byte for byte. IAM PREFLIGHT AND ITS MEASURED LIMIT: simulate-principal-policy for the dell2 user, ONE --resource-arns per call, s3:PutObject on the daily_returns key -> allowed; but a SEPARATE negative control on arn:aws:s3:::opal-data-assets-no-such-bucket-zzz9999/x.parquet ALSO -> allowed, so the simulator is NON-DISCRIMINATING for this principal and this result carries no key-level information (cloud-ops documented false-allow mode: an allowed proves the pattern matches the string typed, not that the resource exists or is the intended one). The sound oracle for the grant is the Put itself, graded at leg A1. | CLOSED 20261009T074509Z |
| B1 | verify | re-grade into .scratch/advi_cotbkf/r28 then --build --cash-leg method_r28 then --dry-run at this seat's own HEAD | the dry run names exactly the pair's three keys with addresses_from_builder=True; absent_months=4 and exactly B3S728504/B3S728506 x 2023-05/2023-06; row counts EQUAL the COO half's 1,691,729 / 21,102,041 / 82,593 (hashes may differ only by run_commit) |  | OPEN |
| A1 | activation | commonwealth_fwd3_serve.py --apply writes the three objects | rc 0; the three keys exist with their ETags read back by head-object |  | OPEN |
| V1 | verify | commonwealth_fwd3_serve.py --verify (criterion CB29ac1-AC1) | FWD3-VERIFY tables=3 match=True with row counts and hashes equal to the dry run's |  | OPEN |

## Log

- 20261009T074326Z OPENED by 0.7.0_AE_CloudOps~CB2 with 4 leg(s)
- 20261009T074509Z LEG P0 closed: BEFORE-STATE MEASURED 20261009T0740Z by 0.7.0_AE_CloudOps~CB2 (user/cloudops-dell2-agent-user, acct 313476888478). All t
