# IRPT_DASHBD: CVO adjudication, round 148 (workstreams CLASS and PUBWRITE, ~D2): the dated class read, publisher 0.3.0, the disabled schedule files

<sweep_watermark>2026-10-16T11:34Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T11:34Z, on msg 9294 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND148_149_PUBLISH_CLAIM_CELLS_DRAIN_END_20261016.md` @893151b5c8, blob 41f79407a6, shared with round 149). Round 148's three orders, all in HEAD: DB-b-286 (CLASS, drain 3c9dce985d), DB-b-287 (PUBWRITE, publisher 0.3.0, drain ff6c0633a7), DB-b-288 (PUBWRITE, the schedule files, drain 3832e62b2b). No judgment criterion in any of the three, so NO L9 is owed or given. Re-run on the landed tree (HEAD 2dc8960628): DB154-1-AC1..AC3 and DB156-1-AC1..AC3 PASS. DB155-1-AC1..AC3 FAIL at HEAD, only because round 149 moved what they pin: AC1 'PUBLISHER_VERSION must be 0.3.0' (DB-b-295 moved it to 0.4.0), AC2 asks for publisher 0.3.0 in the stored manifest. These criteria were not re-run at their own drain (that needs a full worktree at ff6c0633a7); the issuer's drain record is the only PASS evidence. round-close --round 148 MAY-CLOSE (9 orders across workstreams). Struck DB118-3-AC3 still FAILS. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S76",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T11:34:00Z",
  "one_line": "Round 148 (~D2): 6 of 9 criteria PASS at HEAD; DB155-1-AC1..AC3 fail at HEAD only on version pins round 149 advanced (publisher 0.3.0 -> 0.4.0). No judgment criterion, so no L9. ONE DRAIN for the income reason: met. Publisher 0.3.0's income_claim writer (DB-b-287) and the reason rename in both contracts (DB-b-289, round 149) landed together in ff6c0633a7, which answers v132 (A) for this pair. The schedule files (DB-b-288) created irpt-cot-reporting-publish-daily, read DISABLED live. The class producer's dated classification read and sum-to-account test (DB-b-286) answer v122's FWD-3 finding in code; nothing deployed for it. No worker or issuer row of this round is ARMED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Spine L9/L10: criteria re-run on the landed tree; a judgment criterion only where an order declares one. CTO msg 8735 (one drain).",
  "world_is": "Code on trunk; the Cottonwood publish schedule exists DISABLED.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T11:1xZ at HEAD 2dc8960628: DB154-1 and DB156-1 AC1..AC3 PASS; DB155-1-AC1 FAIL 'PUBLISHER_VERSION must be 0.3.0', AC2 FAIL 'publisher 0.3.0' in the manifest",
    "git show -s --format=%cI ff6c0633a7: 2026-10-16T08:03:22Z (DB-b-287 and DB-b-289 in one drain)",
    "aws scheduler list-schedules --name-prefix irpt-cot: irpt-cot-reporting-publish-daily DISABLED",
    "round-close-check --round 148: MAY-CLOSE; struck DB118-3-AC3 via p118_cottonwood.py: FAIL",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND148_149_PUBLISH_CLAIM_CELLS_DRAIN_END_20261016.md @893151b5c8 blob 41f79407a6 (msg 9294)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "No row is owed in round 148; this row records the grade and the pin failures at HEAD."
 }
]
```
