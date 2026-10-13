# DSGN_IRPTV1: CVO adjudication, round 32

<sweep_watermark>2026-10-13T00:26Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T00:26:00Z, on msg 6683 (`2.0.0_SA_COO~D2`; IV-e-123 a read, IV-e-124 a page change on a LOCAL
candidate; real run `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_32_REAL_RUN_20261013.md @f43d788041`). No judgment criterion. Both ARMED rows are disarmed on the owner's ruling (D2-S29): D2-W73-S1 is dismissed,
and D2-W72-S2 graduates DISARMED (the producer fails closed). 7 rows dismissed below; 1 graduates in `remediations/REMEDIATION_v12.md`.
D2-W70-S4 stays OPEN in v11: its wording is on the candidate, not on DEV, and an unsupported card was not seen live. ARMED: 0.

```json
[
 {
  "id": "DSGN_IRPTV1-C-S84",
  "project": "DSGN_IRPTV1",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T00:26:00Z",
  "one_line": "Round 32. Dismissed: D2-W73-S1 (BLOCKING, ARMED; answered by IV-e-124 AMENDMENT 1, four wording-only re-golds, the whole IR scope 1222 pass, 27 skip, 1 fail with no new failing id, re-run by the issuer; disarm recorded here on the owner's ruling D2-S29), D2-W73-S2 (the line the amendment named was off by one), D2-W72-S1 (BLOCKING; the page map has no source on the wire, but none is needed while the producer serves only accounts whose node id equals the account id; carried by D2-W72-S2), D2-W72-S3 and D2-W72-S4 (a contract fixture that models a node id unlike every producer, and stale raw_keys.json citations; carried by D2-W72-S2's remedy), D2-S29 (the disarm ruling), and REMEDIATION_v11's D2-W69-S2 (answered by IV-e-123's read of 31 of 31 producer paths: the ids are equal by rule for INF and COT and equal-or-withheld for 49 Financial, so the Holdings focus never posts a node ref that differs from a served account id).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "DSGN_IRPTV1-D2-W73-S1",
   "DSGN_IRPTV1-D2-W73-S2",
   "DSGN_IRPTV1-D2-W72-S1",
   "DSGN_IRPTV1-D2-W72-S3",
   "DSGN_IRPTV1-D2-W72-S4",
   "DSGN_IRPTV1-D2-S29",
   "DSGN_IRPTV1-D2-W69-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IV-e-123 and IV-e-124 are terminal; round-close MAY-CLOSE (msg 6683); 0 DSGN_IRPTV1 orders active (to-check.py --all). The IV-e-124 candidate is LOCAL in the portal repo, not on DEV, and its unsupported-card wording was not observed live (the served report is certified). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W73-S1, D2-W73-S2, D2-W72-S1, D2-W72-S3, D2-W72-S4, D2-S29, D2-W69-S2",
    "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_32_REAL_RUN_20261013.md @f43d788041",
    "this seat's read 2026-10-13T00:24Z: merge-base --is-ancestor HEAD yes for 49e12d68fe (IV-e-123), b4b41cc928 (IV-e-124), c672ca3bdd and 2c0a190593 (the two amendments), f43d788041 (the real run)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A blocking test row answered by amendment, readings, and rows carried by the graduating producer-side row."
 }
]
```
