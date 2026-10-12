# DSGN_IRPTV1: CVO adjudication, round 31

<sweep_watermark>2026-10-12T23:27Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T23:27:00Z, on msg 6661 (`2.0.0_SA_COO~D2`; three SERVED orders IV-e-120 to IV-e-122; real run
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_31_REAL_RUN_20261012.md @4f9e9e3cd5` on a LOCAL combined portal candidate against live data). No judgment criterion.
14 new rows and 4 REMEDIATION_v10 rows dispositioned: 14 dismissed below, 4 graduate in `remediations/REMEDIATION_v11.md`. ARMED: 0.
D2-W69-S1's disarm is recorded on its owner's ruling (D2-S28). D2-W60-S1 and D2-S21 stay OPEN in v10: the page shows them met, but on the
combined candidate, which is not on DEV. They close when it lands.

```json
[
 {
  "id": "DSGN_IRPTV1-C-S82",
  "project": "DSGN_IRPTV1",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T23:27:00Z",
  "one_line": "Round 31. Dismissed: Round 31's records and readings: D2-S27 (three list items already met on DEV; this seat's read agrees), D2-S28 (the disarm ruling for D2-W69-S1, carried by that row's remediation), D2-W68-S1 (a base suite with one more known failure than the premise), D2-W68-S2 (two direct importers of CategoryViewTree, not six), D2-W68-S3, D2-W68-S4 and D2-W70-S5 (static-render instruments where no dev server was allowed; the real page was walked by the issuer), D2-W68-S5 (branch names as provisioned), D2-W70-S1 (the two missing validation keys now carried inside the grant), D2-W70-S3 (a generator that reads function bodies; the read kept in the body).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "DSGN_IRPTV1-D2-S27",
   "DSGN_IRPTV1-D2-S28",
   "DSGN_IRPTV1-D2-W68-S1",
   "DSGN_IRPTV1-D2-W68-S2",
   "DSGN_IRPTV1-D2-W68-S3",
   "DSGN_IRPTV1-D2-W68-S4",
   "DSGN_IRPTV1-D2-W70-S5",
   "DSGN_IRPTV1-D2-W68-S5",
   "DSGN_IRPTV1-D2-W70-S1",
   "DSGN_IRPTV1-D2-W70-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IV-e-120, IV-e-121 and IV-e-122 are terminal; round-close MAY-CLOSE (msg 6661). The three portal candidates and their combined branch are LOCAL in the portal repo, not on DEV. ARMED after this compile: 0 (D2-W69-S1 disarmed by its owner).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S27, D2-S28, D2-W68-S1, D2-W68-S2, D2-W68-S3, D2-W68-S4, D2-W70-S5, D2-W68-S5, D2-W70-S1, D2-W70-S3",
    "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_31_REAL_RUN_20261012.md @4f9e9e3cd5",
    "this seat's reads of portal origin/DEV 183860ba at 23:24Z: contracts/wire/AnalysisSubmissionRequest.ts carries commentary_requested (1); HoldingsBreakdownTable.tsx:293-305 colgroup holds only <col> children and JSX comments (eba86eaf, IV-e-114); ReportingTab.tsx:438 carries the IV-e-112 FIRM_BINDING words (row D2-S22)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Records, readings and instrument notes; the one ruling is carried by its row."
 },
 {
  "id": "DSGN_IRPTV1-C-S83",
  "project": "DSGN_IRPTV1",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T23:27:00Z",
  "one_line": "Round 31. Dismissed: REMEDIATION_v10 rows met on portal DEV 183860ba, read by this seat: D2-W65-S1 (BLOCKING; the wire file carries commentary_requested, the drift tests read 0 of 28 differ per D2-S27), D2-W62-S2 (BLOCKING; the colgroup carries no whitespace text node, eba86eaf), D2-S22 (the FIRM_BINDING words, IV-e-112). And D2-S24, folded into D2-W69-S1, which graduates with the open question.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "DSGN_IRPTV1-D2-W65-S1",
   "DSGN_IRPTV1-D2-W62-S2",
   "DSGN_IRPTV1-D2-S22",
   "DSGN_IRPTV1-D2-S24"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IV-e-120, IV-e-121 and IV-e-122 are terminal; round-close MAY-CLOSE (msg 6661). The three portal candidates and their combined branch are LOCAL in the portal repo, not on DEV. ARMED after this compile: 0 (D2-W69-S1 disarmed by its owner).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W65-S1, D2-W62-S2, D2-S22, D2-S24",
    "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_31_REAL_RUN_20261012.md @4f9e9e3cd5",
    "this seat's reads of portal origin/DEV 183860ba at 23:24Z: contracts/wire/AnalysisSubmissionRequest.ts carries commentary_requested (1); HoldingsBreakdownTable.tsx:293-305 colgroup holds only <col> children and JSX comments (eba86eaf, IV-e-114); ReportingTab.tsx:438 carries the IV-e-112 FIRM_BINDING words (row D2-S22)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Met on DEV, read by this seat, or carried by a graduating row."
 }
]
```
