# IRPT_BCKEND: CVO adjudication, round 179 (workstream ~P)

<sweep_watermark>2026-10-13T15:14Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T15:14:00Z, on msg 7014 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_179_P_DRAIN_END_20261013.md`, f970b40f11). One read-only order, no judgment criterion.
**D2-W345-S3 is closed:** the 49 Financial builder's client-bearing temp file is no longer left on the host after a real build. 3 rows dismissed
below; nothing graduates. Still ARMED where they stand: D2-W361-S1 (v53) and D2-W348-S2 (v48).
For the issuer's note: PRD v0.53's ratified half is already signed and current (review @d08f9f408e); the directory-search apply waits on its own pair only.

```json
[
 {
  "id": "IRPT_BCKEND-C-S363",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T15:14:00Z",
  "one_line": "Round 179 (~P). Dismissed: D2-S135 (the first control could not be obtained and the first AC2 could not pass; answered by the CTO's control, the build's own vintage receipt, amendment @f18974e127, and the check repair @8c4bde24a8), D2-S136 (the disarm evidence), and REMEDIATION_v47's D2-W345-S3 (ARMED; DISARMED on the CTO's PASS definition: 0 and 0 leftover snapshot temp files at 14:47:12Z after the named real 49financial build 4f958436, whose own manifest shows the S3 snapshot path, so the 0 is not vacuous). Caveats kept on the record: the package VersionId the build ran is inferred (the latest since 13:35Z, which this seat read at round 178); the Inflection build's vintage was not read; no pre-fix host count exists.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S135",
   "IRPT_BCKEND-D2-S136",
   "IRPT_BCKEND-D2-W345-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "TO-IB-pr-513 is complete (order file read; close ac5c8dfba7, amendment f18974e127 and check repair 8c4bde24a8 on HEAD). The temp-file leak's fix is on the host and a real build left nothing behind. PRD v0.53's ratified half is already SIGNED and current (prd-signoff status, this seat's read), so the irpt-directory-search apply waits on no re-sign of this seat.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S135, D2-S136, D2-W345-S3",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_179_P_DRAIN_END_20261013.md (f970b40f11, msg 7014)",
    "this seat's reads 2026-10-13T15:1xZ: prd-signoff status IRPT_BCKEND v0.53 ratified-text SIGNED current; merge-base --is-ancestor HEAD yes for ac5c8dfba7, f18974e127, 8c4bde24a8; round 178 head-object of the 49financial package VersionId UHOCIkWj (13:35:24Z)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A control replaced by the CTO's, its evidence, and an armed hazard disarmed on a non-vacuous live count."
 }
]
```
