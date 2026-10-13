# IRPT_BCKEND: remediations, round 176 (workstream ~P)

<sweep_watermark>2026-10-13T07:53Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T07:53:00Z. Follows ADJUDICATION_v77. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_176_P_DRAIN_END_20261013.md` (eb697a8338, msg 6857). No judgment criterion.
Graduated, round label v177: 2 rows, OPEN, ARMED, owner `2.0.0_SA_COO~P2`.
- D2-W361-S1: a re-cut from HEAD would add an import the live packages lack; fenced by the minimal-pair ruling.
- D2-W361-S3: 4 live members equal no historical blob. The pair carries them unchanged and names them; their provenance is the CTO's question.
Still ARMED where they stand: D2-W345-S3 (v47; disarms with the pair's apply at the host's next scheduled Online) and D2-W348-S2 (v48).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W361-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "data/assets/scripts/silver/opal_strategy_matcher.py is in _IRPT_HOLDINGS_CLOSURE but in none of the 49financial, inflection or cottonwood holdings packages (45 rows each, 44 repository members plus SHA256SUMS); the inflection and cottonwood packages were uploaded after the commit that added the closure entry.",
  "evidence": [
   "investigation row D2-W361-S1",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_176_P_DRAIN_END_20261013.md",
   "row D2-S131 (the issuer's ruling)"
  ],
  "remedy": "The guard's closure lists opal_strategy_matcher.py, but no live per-firm package carries it, and HEAD's rebalancer_schemas.py imports it at module level. A re-cut from the closure at HEAD would ship other projects' changes and a new import. Fenced by the issuer's ruling (D2-S131): the pair is the LIVE bytes plus only the two merged changes. Disarmed when the pair's member-level diff against live equals exactly the intended members.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v177",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v177"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_BCKEND-D2-W361-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "25 rows per package differ from HEAD; 22 differing rows across the three packages (10, 6 and 6) have no commit since the package's last_modified (for example 49financial build_cottonwood_mdpf_slice.py equals its blob at 9efbec3c2f, while HEAD changed it at 0c72f3be00 before the 2026-10-11 upload); lib/opal_naming.py differs in all three packages with 12 or more commits since.",
  "evidence": [
   "investigation row D2-W361-S3",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_176_P_DRAIN_END_20261013.md",
   "row D2-S131 (the issuer's ruling)"
  ],
  "remedy": "25 of 45 members differ from HEAD in every live package; 22 differing rows have no commit since the upload, and 4 rows (49financial 2, inflection 1, cottonwood 1) equal NO historical blob at all. So live bytes run on the host that the repository cannot reproduce. The minimal pair must name those 4 members in its packet and carry them unchanged, and their provenance is asked of the CTO separately, since no repo history explains them.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v177",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v177"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 }
]
```
