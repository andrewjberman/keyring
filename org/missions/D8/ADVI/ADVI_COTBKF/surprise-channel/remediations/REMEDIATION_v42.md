# ADVI_COTBKF: remediations, round 71

<sweep_watermark>2026-10-11T18:22Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T18:22:31Z. Input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_71_DRAIN_END_20261011.md @70281800e0 (msg 5530)`.
Graduated, round label v72: 4 rows, all OPEN, INERT. Nothing was applied, served or re-minted in the round.

**For the CTO's analysis:**
1. **The nine fund series are confirmed on a third source, and the size is the finding.** On 87 of 92 reinvestment dates the build's
   close is below the price the custodian's rows show the fund traded at, in 9 of 9 funds, by as much as half. Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_71_L9_GRADE_20261011.md`.
2. **The other 63 of the 72 rest on the vendor read against itself.** They are a count, not yet a finding of the same strength.
   The reinvestment-price check this seat ran needs no vendor data and would test every series with reinvestment rows.
3. **The re-mint mode cannot support the pair as built** (rows D2-W118-S1 to S3): it names keys written before it puts them, flags
   no half pair, and does not read the method row's manifest back. Repair, or a pair that carries those facts itself, is yours.
4. Not re-derived by this seat: the reach of 3,187 measured account-days; the correction list's quotations.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W116-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB-bs-1: 72 of 270 fund series (73 tested, 124 untested) carry a dividend-adjusted close left on the store by the as-traded basis; the adjustment is 1.0 to 2.3 times the single one their distributions imply, so the face's 80-percent-within-2-percent test fails for all nine though every step sits on a distribution.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W116-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_71_DRAIN_END_20261011.md @70281800e0 (msg 5530)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_71_L9_GRADE_20261011.md"
  ],
  "remedy": "The price basis for the fund series left on the store is decided, and the 124 untested series are tested or stated as untested where the returns are shown. No correction is sized until a return is recomputed on a stated basis.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v72",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v72"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W118-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Re-mint failure output over-names: on a failed put the mode prints every key of the day (or the sidecar, or the method row's two keys) as WRITTEN although none, or only the first, landed, and a half pair (new data.parquet, old manifest.json) is not flagged.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W118-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_71_DRAIN_END_20261011.md @70281800e0 (msg 5530)"
  ],
  "remedy": "The re-mint mode names a key as written only after its put returns, and flags a day or method row whose two files are of different runs; or the pair written on the mode carries those facts per key itself.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v72",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v72"
  },
  "closed": true
 },
 {
  "id": "ADVI_COTBKF-D2-W118-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Re-mint killed or interrupted between two puts prints nothing about the keys written: the handlers catch (Exception, SystemExit) only, so a BaseException leaves the bucket changed with no ERROR line and no WRITTEN list.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W118-S2",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_71_DRAIN_END_20261011.md @70281800e0 (msg 5530)"
  ],
  "remedy": "An interrupted run prints the keys it had written; or the pair states that an interrupted run is restored from the captured version ids for every key the mode can change.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v72",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v72"
  },
  "closed": true
 },
 {
  "id": "ADVI_COTBKF-D2-W118-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Re-mint does not read back the method row's manifest.json: a method-row manifest.json stored with the wrong content is reported as a success (exit 0 and the success line).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W118-S3",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_71_DRAIN_END_20261011.md @70281800e0 (msg 5530)"
  ],
  "remedy": "The mode reads the method row's manifest back and refuses on a mismatch.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v72",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v72"
  },
  "closed": true
 }
]
```
