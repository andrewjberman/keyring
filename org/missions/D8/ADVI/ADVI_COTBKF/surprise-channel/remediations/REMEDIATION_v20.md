# ADVI_COTBKF: remediations, round 28

<sweep_watermark>2026-10-09T07:21Z</sweep_watermark>

Graduated at round 28's L9 (ADJUDICATION_v22.md), round label v29: 2 rows, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W53-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "AC2 (python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method_r26 --after-cash-leg method_r28 ...) ends 'regressions=4' against the expected 'regressions=0'; the refusal clause applies, nothing further was tuned",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W53-S3",
   "last line of the AC2 run (rc 0) @8137a94e91: SWEEP-REGRADE sweeps=2 rejected=517 double_drop_months=0 fixed=0 months_before=3098/886/78609 months_after=3133/838/78622 control_same=True regressions=4 movers_back=139 year_chain_same=True r22_named=25/25 dividend_both=NA"
  ],
  "remedy": "Explain the 4 named regressions (B3S728504, B3S728506; 2023-05, 2023-06) from the rows -- dividend dating is suspected, unmeasured -- or keep them ABSENT in the served tables with the reason; a fifth regression voids the mint's amendment.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v29",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v29"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W53-S4",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "method_r28 detects 61 split events over the accounts' rows and the store (round 27's trace named 14 for the traced months); 33 are applied, 28 are UNCONFIRMED (close not continuous across the day, or no row that day) and left as they are, named; 1086 account-days on 35 distribution close-step security-days are blank (DVR_CLOSE_STEP), the cause of that step is not measured",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W53-S4",
   "AC2 run 2 stdout: R28-REPAIRS splits_applied=33 splits_not_applied=28 disagreements=0 dvr_close_step_security_days=35 dvr_account_days_blank=1086; every unconfirmed split is printed as an R28-SPLIT line and in org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53/sweep_regrade.md"
  ],
  "remedy": "Resolve the 28 UNCONFIRMED split events (close not continuous across the day, or no row that day) against a second source, or keep them named and unapplied; re-count after the price fill.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v29",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v29"
  },
  "closed": false
 }
]
```
