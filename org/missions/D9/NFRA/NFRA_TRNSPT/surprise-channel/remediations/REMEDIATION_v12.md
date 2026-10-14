# NFRA_TRNSPT: remediations, round 24

<sweep_watermark>2026-10-14T11:52Z</sweep_watermark>

Round 24 slug by `3.0.0_SA_CVO~DELL2`, 2026-10-14T11:52Z. L8 input: `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R24_CLOSE.md`
@c8a91bd6eb (msg 7564). No judgment criterion. Follows ADJUDICATION_v16.
Graduated, round label v25: 0 new rows. One disarm-clock row: D2-S22, ARMED in REMEDIATION_v10, is DISARMED and REMEDIATED here.
ARMED after this file: 0. Still OPEN where it stands: D2-S15 (BLOCKING, REMEDIATION_v10, owner `1.0.0_SA_CTO~DELL2`), on the
FWD-3 ruling for the 4 Monday meetings, which R24_CLOSE carries as one ask to the CTO.

```json
[
 {
  "id": "NFRA_TRNSPT-D2-C-S1",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "D2-S22: one dist zip path feeds every function of the transcripts Terraform root, so an untargeted apply from a tree without fd74f984ac, 5ae3b3ddd9 and 7bca11ddee reverts the Teams pull. Its REMEDIATION_v10 row was written ARMED and append-only, so the disarm its owner measured (D2-S28) never reached the ARMED read.",
  "evidence": [
   "adjudications/ADJUDICATION_v16.md#NFRA_TRNSPT-D2-C-S1",
   "investigations/INVESTIGATION_v1.md#NFRA_TRNSPT-D2-S28 (1.0.0_SA_CTO~DELL2, 2026-10-11T07:51:01Z: one digest on 3 of 3 functions; the four fix commits ancestors of origin CLOUD)",
   "this seat's live read 2026-10-14T11:45:39Z: the three functions read CodeSha256 xC1GDXXpuO5vNk2lGqRr2S6rH041rzdQnbCD91KQodE=, distinct digests 1"
  ],
  "remedy": "The REMEDIATION_v10 remedy is met: every function of the root reads one live CodeSha256, built from a tree holding the three fix commits. An apply of this root still prints its tree's dist zip digest beside the live one (D2-S28's standing condition).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v25",
  "disarms": [
   "NFRA_TRNSPT-D2-S22"
  ],
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "at": "2026-10-11T07:51:01Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v25"
  },
  "closed": true
 }
]
```
