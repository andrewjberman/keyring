# ADVI_COTBKF: remediations, round 31

<sweep_watermark>2026-10-09T09:31Z</sweep_watermark>

Round 31 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~09:3xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_31_DRAIN_END_20261009.md @f4e9cd50fc` (msg 2996). CB-ae-1 complete, 0 judgment
criteria, MAY-CLOSE. D2-S45 closed in place in REMEDIATION_v21 (clocks only): the outside as-traded closes put r28's level right up to a
base-close residual, and r26 short by the split factor. W58-S1 (BLOCKING) graduates below, round label v32, as that residual. ARMED: 0.

Compile record:

```json
[
 {
  "id": "ADVI_COTBKF-D2-W58-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "CB-ae-1: Yahoo (yfinance 1.2.0, auto_adjust=False) Close on 2022-10-12 x Yahoo's own later splits (both x3/x2 on 2024-10-11, same ratios as the rows) gives as_traded SCHB 13.98 x3 = 41.94 vs r28 39.9906 (+4.9%) and r26 13.3302; SCHZ 22.465 x2 = 44.93 vs r28 39.4362 (+13.9%) and r26 19.7181. Neither CUSIP is within 2% of r28 or r26, so the pre-written rule prints branch OTHER. Direction: the store close is below the outside level on both (r28 -4.7% / -12.2% of as_traded), and the shortfall differs per CUSIP, so it is not a split-factor error alone. Evidence stored at the price_evidence key (2 rows, read back).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W58-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_31_DRAIN_END_20261009.md @f4e9cd50fc",
   "this seat's reading of the stored evidence (s3://opal-data-assets/commonwealth/cottonwood/silver/price_evidence/date=2022-10-12/, 2 rows read back): SCHB as-traded 41.94 vs r28 39.9906 (-4.6%) and r26 13.3302 (-68%); SCHZ as-traded 44.93 vs r28 39.4362 (-12.2%) and r26 19.7181 (-56%); Yahoo's own split series names x3 and x2 on 2024-10-11, the ratios r28 applied"
  ],
  "remedy": "Trace the chain's base close for SCHB (808524102) and SCHZ (808524839) over the held window against Yahoo's series (source, date, carry-forward; SCHZ is on the need list as unpriced through 2022-10-11), say which days differ and by how much, and re-mint only the affected served values under a pair if the served levels or month grades move.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v32",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v32"
  },
  "closed": true
 }
]
```
