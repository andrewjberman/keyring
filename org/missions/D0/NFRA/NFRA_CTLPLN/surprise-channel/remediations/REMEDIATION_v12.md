# NFRA_CTLPLN -- remediations, v12

<sweep_watermark>2026-10-15T20:55Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-15 ~21:0xZ, at the round-22 close. Graduated in ADJUDICATION_v27.md C-S76. Two INERT rows, owner the danger map's owner.

```json
[
 {
  "id": "NFRA_CTLPLN-W121-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "nerves_lexical build emits a different danger-edge count for each tree it runs in: 3491 at 54e8947a06 (docs_scanned 2709), 2692 in a scratch clone without portal/, and 2703 for the committed round-22 map. Which map the reflex reads therefore depends on where it was last built.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W121-S3",
   "adjudication row NFRA_CTLPLN-C-S76"
  ],
  "remedy": "P3. The map's owner states which tree is the build input (the full tracked corpus at a named commit), and the build prints that denominator. Done when two builds of the same commit from two trees print the same edge count.",
  "owner": "1.0.0_SA_CTO",
  "round": "v27",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v27"},
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-W121-S4",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "build_refusal in org/modules/graph/nerves_lexical.py refuses a sparse tree and a missing corpus folder, but does not check portal/, whose files the resolver addresses. A build in a tree without portal/ passes the guard and drops portal edges (W121-S5).",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows W121-S4, W121-S5",
   "adjudication row NFRA_CTLPLN-C-S76"
  ],
  "remedy": "P3. The guard also refuses a tree with no portal/ checkout. Done when a build in a tree without portal/ prints a refusal.",
  "owner": "1.0.0_SA_CTO",
  "round": "v27",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v27"},
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
