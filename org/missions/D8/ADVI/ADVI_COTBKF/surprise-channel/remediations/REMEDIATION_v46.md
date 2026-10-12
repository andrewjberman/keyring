# ADVI_COTBKF: remediations, round 77

<sweep_watermark>2026-10-12T00:56Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T00:56:37Z. Input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_77_DRAIN_END_20261012.md @dca4f4d16f (msg 6226)`.
Graduated, round label v78: 1 row, OPEN, BLOCKING, INERT.

**For the CTO's analysis:**
1. **Both criteria MET. No served figure carries the three-quarters error today,** with three limits: 7 of 15 funds matched as held;
   46 of 47 partitions unopened; a local copy of the store. Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_77_L9_GRADE_20261012.md`.
2. **This seat re-derived the window:** 480 fund-days, 0.9845 to 1.0061, median 1.0000. And the reason as numbers: the median ratio by
   year runs 0.46, 0.51, 0.63, 0.74, 0.79, 0.88, 1.00 from 2020 to 2026.
3. **Two latent hazards, row D2-S131:** a rebuild of the 47 early partitions from a later store, and the first reader of this project's
   own minted table. Neither is live; both are one ordinary act away, and neither had a row.
4. The store's writer is not in the live step list and its owner is not established (the issuer's statement). A defect in a store
   nobody owns has nobody to correct it.
5. Three readers are not established; the round names what would establish each.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S131",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Two latent hazards from round 77 that no row carried. (1) The 47 served holdings partitions of 2026-04-22 to 2026-06-07 are right only because they were written when the store's close was current; a REBUILD of them from a later copy of the store would price the 15 funds low, and nothing in the tree prevents one. (2) This project's own minted table holds 259,357 account-days valued from these closes and has no reader; the first reader built on it serves the error.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S131",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_77_L9_GRADE_20261012.md",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_77_DRAIN_END_20261012.md @dca4f4d16f (msg 6226)"
  ],
  "remedy": "The early partitions are marked or guarded so a rebuild from a later store is refused or known, until the fund closes are corrected at the store; and the minted table is not given a reader before then. Each is one sentence in the place a seat about to do the act would read.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v78",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v78"
  },
  "closed": false
 }
]
```
