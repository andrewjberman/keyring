# NFRA_CTLPLN: CVO L8 at the round-13 close (2026-10-14)

<sweep_watermark>2026-10-14T21:30Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109254 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND13.md` @58733404fb).
`round-close-check --round 13`: MAY-CLOSE, judgment 2 graded 2 (TO-APPLY-9 and TO-APPLY-31, graded earlier). No new L9 grade.
`TO-CT-ac-5` is parked on Andrew's word, so FWD-11 is not exercised this round.

**Result: 11 round-13 rows dispositioned; 10 dismissed with reason (C-S48); 1 GRADUATES INERT (C-S49, W89-S3). Two earlier ARMED rows from other boxes, D2-S3 and Z-S8, GRADUATE ARMED (C-S50).** Carried and unchanged:
S9118, S9119, S9120, W8-S7, Z-S3, W12-S1, S9103 (their remediation rows stand).

```json
[
 {
  "id": "NFRA_CTLPLN-C-S48",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T21:30Z",
  "one_line": "Round 13, rows resolved inside the round or carried on the issuer's round-14 input list: S9123 (fixed by CT-ac-6; UNBLOCK-SELFTEST 32/32 read here), D2-S5 (fixed by CT-ac-7; the issuer read the checker 63/63), W89-S1 (BLOCKING; the residual attributed to 057cfa8a1c, CT-ac-3 complete ok=True), W87-S1, W88-S1, W90-S1, W91-S1 (the built reading recorded and kept), W87-S2, W89-S2, W91-S2 (named on the issuer's round-14 input list for the CTO).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-S9123",
   "NFRA_CTLPLN-D2-S5",
   "NFRA_CTLPLN-W89-S1",
   "NFRA_CTLPLN-W87-S1",
   "NFRA_CTLPLN-W88-S1",
   "NFRA_CTLPLN-W90-S1",
   "NFRA_CTLPLN-W91-S1",
   "NFRA_CTLPLN-W87-S2",
   "NFRA_CTLPLN-W89-S2",
   "NFRA_CTLPLN-W91-S2"
  ],
  "spec_asserts": "Each round-13 row needs one carrier: a fix, a ruling, the built reading kept, or the CTO's round-14 list.",
  "world_is": "Read here: .tools/unblock.py --selftest reads UNBLOCK-SELFTEST cases=32/32 ok=True. CT-ac-7's checker self-test was not re-run here (the tool takes no --selftest flag); its 63 of 63 is the issuer's reading. The issuer's round-14 input file names W87-S2, W88-S1, W89-S2, W89-S3, W91-S1, W91-S2 and D2-S5. W89-S1's blocking residual is the earlier adapter-row relocation (057cfa8a1c), not CT-ac-3's change.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND13.md @58733404fb",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/ROUND13_INPUTS_FOR_ROUND_ANALYSIS.md (one line per row)",
    "timeout 200 python .tools/unblock.py --selftest -> cases=32/32 ok=True (2026-10-14 ~21:2xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Fixed in the round, kept as built, or carried by the issuer's round-14 list to the CTO's analysis; no row stands open."
 },
 {
  "id": "NFRA_CTLPLN-C-S49",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T21:30Z",
  "one_line": "Round 13: W89-S3 GRADUATES to REMEDIATION_v7 (INERT) -- the lgic firm-bucket fence references fence_scoped_statements only (s3-lgic-firm-buckets.tf:172) and never fence_scoped_allow_statements, which s3-49financial.tf:141 does append; a scoped row on an lgic bucket renders its Deny with no Allow.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W89-S3"
  ],
  "spec_asserts": "A row graduates when its mechanism is attributed, its denominators carried and its remedy holder named.",
  "world_is": "Read here at HEAD: s3-lgic-firm-buckets.tf names module.opal_name.fence_scoped_statements once (:172) and fence_scoped_allow_statements nowhere; s3-49financial.tf:141 concatenates both. The worker measured inflection at 0 of 4 Allow statements and cottonwood at 0 of 2 on the with-state render.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "grep fence_scoped_(allow_)?statements over infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf and s3-49financial.tf at HEAD",
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W89-S3",
    "remediations/REMEDIATION_v7.md"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "NFRA_CTLPLN-C-S50",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T21:30Z",
  "one_line": "Two ARMED rows filed from other boxes into this channel, served by no round-13 cell, GRADUATE ARMED to REMEDIATION_v7 under the disarm owners they name: D2-S3 (crossbox-deploy-check's OPEN-CALL limb matches a kind-act row through its project's whole write set, so one pending Andrew act STOPs unrelated applies once ENFORCE is on; WARN today) and Z-S8 (six site Z CloudOps lanes ended with no kill, reboot, crash or memory event; cause unread, the S9120 class).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-D2-S3",
   "NFRA_CTLPLN-Z-S8"
  ],
  "spec_asserts": "An ARMED row is dispositioned before the slug; a row graduates with its mechanism, denominators and remedy holder named.",
  "world_is": "D2-S3 is measured by 1.0.0_SA_CTO~DELL2: one act row (dell2-20261013T214715Z-f61b) matched 1 of 346 calls and drew STOP on the investor-reporting root, while the irpt-status and opal-ticket-api applies it would stop do not depend on that act. Z-S8 is measured by 0.0.0_AB_MSTR~Z: 6 seats gone, 0 KILL lines, 0 Application Error/Hang events naming claude or node, 0 Resource-Exhaustion events, with a positive control on the event-log reads. Its cause is unread, so its remedy begins with that read.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row D2-S3",
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row Z-S8",
    "remediations/REMEDIATION_v7.md"
   ]
  },
  "disposition": "GRADUATED"
 }
]
```

-- 3.0.0_SA_CVO~L
