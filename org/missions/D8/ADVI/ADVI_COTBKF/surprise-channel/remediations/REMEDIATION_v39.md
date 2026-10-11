# ADVI_COTBKF: remediations, round 68

<sweep_watermark>2026-10-11T15:08Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T15:08:46Z. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_68_DRAIN_END_20261011.md @95eab5179c (msg 5186)`.
**L9:** CB68bp4-AC2 MET; CB68bp5-AC2 MET; **CB68bp3-AC2 NOT MET on its first limb**. `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_68_L9_GRADE_20261011.md`.
Graduated, round label v69: 2 rows, OPEN, INERT. Closed in place in REMEDIATION_v38: D2-S115 (the list at the pin is 2 day files,
re-derived by this seat).

**For the CTO's analysis:**
1. **Both lists now exist at the served instant's pin.** The withholding rule replaces 2 day files; the control is exact. At that pin
   the four spin-off events are not in the store, so the 30 drift days do not arise. Which pin a re-mint uses is yours.
2. **Nobody has shown whose print the "custodian's mark" is.** Its label is the portfolio system's. The four claims stand anyway.
3. **166 of the 179 outlier days are the form's treatment, not market returns:** income paid after the holdings left (119) and a fee
   refund after the assets left (43) are 162 of them. Whether those are flows is a policy call nobody has made. The worker's finding
   for the threshold: recent outflow separates the classes; a prior value of 100.00 does not.
4. One security's close series sits about 6.6 times below its traded price. No scan for others has been made.
5. 41 withholding days are blank under both rules and would change under method_r29 if priced later.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W103-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The store the code calls the custodian's mark starts 2026-06-08, after all four spin-off events, so no date exists to compare and each claim is UNAPPLIED_NO_HELD_DATE. And the print is not shown to be the custodian's: its label is the portfolio system's snapshot (CB68bp3-AC2 NOT MET on that limb).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W103-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_68_DRAIN_END_20261011.md @95eab5179c (msg 5186)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_68_L9_GRADE_20261011.md"
  ],
  "remedy": "The CTO rules whether a price derived from the custodian's trade rows may decide a spin-off claim, and what evidence makes a print 'the custodian's own'. Until then no spin-off factor is applied.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W101-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The as-traded regrade reads an untracked price cache of 3,580 files from a fixed path with no flag. A truly empty checkout stops there; the round's runs used a copy of the pinned directory.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W101-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_68_DRAIN_END_20261011.md @95eab5179c (msg 5186)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_68_L9_GRADE_20261011.md"
  ],
  "remedy": "The cache is given by a flag and named in the pin record, so 'from a clean checkout' holds for every input.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v69"
  },
  "closed": false
 }
]
```
