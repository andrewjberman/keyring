# IRPT_BCKEND: remediations, round 166 (workstream ~P)

<sweep_watermark>2026-10-12T19:58Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T19:58:00Z. Follows ADJUDICATION_v67. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_166_P_DRAIN_END_20261012.md` (blob 6f7a87658e, msgs 6511, 6513). No judgment criterion.
Graduated, round label v167: 3 rows, OPEN; BLOCKING 2; ARMED 0.
- D2-W334-S2 (BLOCKING, owner `1.0.0_SA_CTO~DELL2`): a frozen v1 contract artifact was edited on v0.50's order. This seat signed v0.50 and missed it.
- D2-W331-S2 (BLOCKING, owner `2.0.0_SA_COO~P2`): the release pair prints the claim MOVES (orion SI 750, YTD 76, 1Y 106), not the reach.
- D2-W333-S1 (owner `2.0.0_SA_COO~P2`): the resident package does not stage ycharts/research.
Still OPEN from REMEDIATION_v41: D2-W321-S1 (C-VALUEFACTS step 1 done: the portal tiles read the market-value names at `adapt.ts:839-840`;
the reader's move and the bd_adapter rename are later cuts, reader first).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W331-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The reader's new rule fires on exactly the CTO's v0.49 counts in all 8 cells, but the accounts whose claim MOVES from measured to inferred (base reader vs built reader, same partitions) are fewer in 3 orion cells: SI 750 of 894, YTD 76 of 200, 1Y 106 of 240, because 144, 124 and 134 accounts were already inferred at base for a missing trading day.",
  "evidence": [
   "investigation row D2-W331-S2",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_166_P_DRAIN_END_20261012.md"
  ],
  "remedy": "The C-CHAINCLAIM release pair's packet prints the accounts whose claim MOVES, with the reach beside them: 49F SI 23, YTD 19, QTD 2, 1Y 20; orion SI 750 (reach 894), YTD 76 (200), QTD 7 (7), 1Y 106 (240). Correction to this seat's v0.49 review, which named the reach as the moves. The never-widen half is signed against the moves.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v167",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v167"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W334-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "infra/aws/lambda/ci/lambda-source-map.json and infra/aws/lambda/layers/irpt-common/BUILD_MANIFEST.json pin the two schema copies by sha256, and PATH_MANIFEST.json calls the docs copy IMMUTABLE once IB-rt-1 completes; the order edits both copies and none of those files is in its paths.",
  "evidence": [
   "investigation row D2-W334-S2",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_166_P_DRAIN_END_20261012.md",
   "infra/aws/lambda/investor-reporting/PATH_MANIFEST.json:5726-5730 ('IMMUTABLE once IB-rt-1 flips complete')",
   "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-1.the-seam-one-versioned-contract-artifact.md <status> 'complete ... v1 IS FROZEN AT THIS FLIP'",
   "git show --stat c16bf9d7bb: docs/contracts/investor-reporting/v1/PerformanceReport.schema.json 18 lines changed"
  ],
  "remedy": "docs/contracts/investor-reporting/v1/PerformanceReport.schema.json is IMMUTABLE since IB-rt-1 flipped complete ('v1 IS FROZEN AT THIS FLIP'; PATH_MANIFEST.json:5730). IB-pr-479 (@c16bf9d7bb) changed it, as v0.50 ordered ('both copies'). This seat signed v0.50 without catching it. The change is additive inside an open object, so existing instances still validate, but the published v1 bytes moved under the same $id, and three manifests pin them by sha256. The CTO rules one of two: revert the v1 docs copy and publish the two members in a new contract version, or record a deliberate exception to the freeze with its reason. No release re-pins the docs copy before that ruling.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v167",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v167"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W333-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "No package list in the repo carries ycharts/research/opal_packager.py: lambda-source-map.json names it in no function, and build_resident_package.py stages ycharts/{generate,session,extract} but not ycharts/research, though resident_installed.build_resident_runtime imports opal_packager when the bindings carry commentary_ready_queue_url.",
  "evidence": [
   "investigation row D2-W333-S1",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_166_P_DRAIN_END_20261012.md"
  ],
  "remedy": "build_resident_package.py stages ycharts/{generate,session,extract} and not ycharts/research, though build_resident_runtime imports opal_packager when commentary_ready_queue_url is bound. Add ycharts/research to the staged dirs, or prove no resident binds the queue, before a resident release that carries IB-pr-478.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v167",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v167"
  },
  "closed": false
 }
]
```
