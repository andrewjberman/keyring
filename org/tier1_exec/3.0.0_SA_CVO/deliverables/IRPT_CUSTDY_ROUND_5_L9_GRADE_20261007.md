# IRPT_CUSTDY round 5 -- L9 grade: CU15-AC3 (C-SHAPE)

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~13:1xZ. Input: the drain-end packet
`org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_5_DRAIN_END_20261007.md` @2e68ccd2d2 (msg 587); the
portal candidate 99addd80 (branch `wk-IRPT_CUSTDY-12-portal`, not on DEV). Read with `git show`; no bun was run.

The criterion: "C-SHAPE: the document is built from the custodian-shaped model and names no field after a Black Diamond field". PRD
C-SHAPE: "no table, field or template is designed around Black Diamond. Black Diamond is a field map only".

**Grade: MET, with one finding on the instrument.**

## Built from the custodian-shaped model

- `render/clientreport/types.ts` types the document as the producer's contract (`client_report_figures.py`), one document per household,
  and every key list it declares (`CLIENT_REPORT_KEYS`) is that producer's.
- The producer reads the custodian (`client_report_figures.py`: 32 mentions of schwab, 0 of blackdiamond or black_diamond).

## Names no field after a Black Diamond field

- This seat compared the contract's 45 keys with the key vocabulary of a REAL Black Diamond record:
  `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/acct=12152081.json`, 75 distinct keys.
- Normalized (case and underscores ignored), 6 coincide: `accounts`, `fees`, `market_value` (BD `marketValue`), `name`, `symbol`,
  `value`. Each is a generic financial word that the custodian's own data carries too; none is a Black Diamond construct.
- None of Black Diamond's distinctive fields appears in the contract or the template: `netAdditions`, `daysHeld`,
  `beginningMarketValue`, `endingMarketValue`, `timeWeightedReturns`, `moneyWeightedReturns`, `performingBmv`, `performingEmv`,
  `contributionOfReturnToParent`, `allocationOfTotal`, `levelKey`, `asOfDatePoints`.

## Finding: the instrument's deny list is not Black Diamond's vocabulary

The check the worker's AC2 ran (`bd_field_names=0`) uses `BLACK_DIAMOND_FIELD_NAMES` in `types.ts`, a list the worker wrote. It names
report-style words (`beginningValue`, `periodReturn`, `householdName`, ...), most of which are not in a real BD record, and it omits BD's
real fields above. A zero against that list proves little. The deny list should be drawn from BD's actual key vocabulary (one bronze
record, as here) so the test fails on a real BD name. This does not change the grade, which rests on this seat's comparison.

-- 3.0.0_SA_CVO
