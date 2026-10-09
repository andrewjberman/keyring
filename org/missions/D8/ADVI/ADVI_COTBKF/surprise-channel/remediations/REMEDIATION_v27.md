# ADVI_COTBKF: remediations, round 37

<sweep_watermark>2026-10-09T13:36Z</sweep_watermark>

Graduated at round 37's L9 (ADJUDICATION_v29.md), round label v38: D2-S62, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S62",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The 'bd' token is ambiguous inside Cottonwood's own data: cot GOLD holdings carry 86 rows for 95000U2D4 labelled bd_snapshot (2026-06-08 .. 2026-10-08), and Cottonwood's own pipeline is a Black Diamond session (cot-bd-session-daily-et, BD_FIRM_ID=cottonwood in ssm.tf). A 'bd' label can therefore name the Black Diamond PLATFORM serving Cottonwood's own accounts or the separate bd firm (49 Financial), and a token-based exclusion cannot tell them apart.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S62",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_37_DRAIN_END_20261009.md @7bc7b1fc1e (msg 3373)"
  ],
  "remedy": "Rule what 'bd_' means on a cot row (platform or firm), and make the cross-firm test read an explicit firm field or the registry's source-to-firm mapping rather than a name token.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v38",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v38"
  },
  "closed": false
 }
]
```
