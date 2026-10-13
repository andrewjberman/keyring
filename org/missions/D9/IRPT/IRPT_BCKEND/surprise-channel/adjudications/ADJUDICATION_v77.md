# IRPT_BCKEND: CVO adjudication, round 176 (workstream ~P)

<sweep_watermark>2026-10-13T07:53Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T07:53:00Z, on msg 6857 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_176_P_DRAIN_END_20261013.md`, eb697a8338). One read-only order, no judgment criterion. The live
per-firm holdings packages are not HEAD (25 of 45 members differ in each), and 4 live members equal no historical blob. This seat agrees with
the issuer's ruling: the pair is the live bytes plus only the two merged changes. 5 rows dismissed below (one of them REMEDIATION_v52's
D2-W359-S1, whose census is done); 2 graduate ARMED in `remediations/REMEDIATION_v53.md`.

```json
[
 {
  "id": "IRPT_BCKEND-C-S360",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T07:53:00Z",
  "one_line": "Dismissed: Round 176 (~P). D2-W361-S2 (the issuer's order named holdings_inf.py for the temp-file fix; the commit touches holdings_49f.py and holdings_snapshot.py), D2-W361-S4 (the guard declares a manifest stamp; the live packages carry SHA256SUMS and S3 metadata), D2-W361-S5 (the AC2 amendment applied to the record), D2-S131 (the issuer's ruling, carried by the two graduating rows), and REMEDIATION_v52's D2-W359-S1 (ARMED; its remedy, the read-only census of the per-firm packages, is done by IB-pr-509; the hazard it fenced is carried forward by D2-W361-S1 and -S3).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W361-S2",
   "IRPT_BCKEND-D2-W361-S4",
   "IRPT_BCKEND-D2-W361-S5",
   "IRPT_BCKEND-D2-S131",
   "IRPT_BCKEND-D2-W359-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IB-pr-509 is complete (order file read); drain 024a54df28 and check amendment fea3a3c885 are on HEAD. Nothing was written to AWS. The host-bundle pair is to be a MINIMAL per-firm package (the issuer's ruling, which this seat agrees with), never a re-cut from HEAD.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W361-S2, D2-W361-S4, D2-W361-S5, D2-S131, D2-W359-S1",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_176_P_DRAIN_END_20261013.md (eb697a8338, msg 6857)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An order wording error, readings, a ruling carried by its rows, and a census remedy done."
 }
]
```
