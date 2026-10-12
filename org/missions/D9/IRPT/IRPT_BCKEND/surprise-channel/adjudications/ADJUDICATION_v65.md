# IRPT_BCKEND: CVO adjudication, the ~P slug (rounds 117 to 164)

<sweep_watermark>2026-10-12T17:40Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T17:40:00Z, on msgs 6436 and 6445 (rounds 163 and 164, packet blob 081cb2b959) and the
uncompiled rounds 161 and 162 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_161_162_P_DRAIN_END_20261012.md`). Every IRPT_BCKEND order is terminal, so the
rows held since round 117 in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md` land now. No judgment criterion in rounds 161 to 164.
100 open rows: 72 dismissed below (plus this seat's read row D2-S108); 28 graduate OPEN in `remediations/REMEDIATION_v41.md`.
Both ARMED rows are disarmed on this seat's reads (D2-S108): D2-S60 graduates INERT with a residual; D2-W317-S1 is dismissed. ARMED after: 0.

```json
[
 {
  "id": "IRPT_BCKEND-C-S341",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T17:40:00Z",
  "one_line": "~P slug, rounds 117 to 164. Dismissed: Contract text repaired or superseded by signed PRD versions, or a contract input consumed by them: D2-S82 (met by v0.35/v0.36, signed), D2-S92 (met by v0.38, signed), D2-W297-S1 (v0.38's sizing, superseded), D2-W313-S3, D2-W319-S1, S2, S3 and D2-W322-S1 (consumed by C-CHAINCLAIM, PRD v0.48, and round 164's counts), D2-W301-S2 (the last-day question answered by rounds 161 and 164).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S82",
   "IRPT_BCKEND-D2-S92",
   "IRPT_BCKEND-D2-W297-S1",
   "IRPT_BCKEND-D2-W313-S3",
   "IRPT_BCKEND-D2-W319-S1",
   "IRPT_BCKEND-D2-W319-S2",
   "IRPT_BCKEND-D2-W319-S3",
   "IRPT_BCKEND-D2-W322-S1",
   "IRPT_BCKEND-D2-W301-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "Every IRPT_BCKEND order is terminal at this compile (0 active, to-check.py --all). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S82, D2-S92, D2-W297-S1, D2-W313-S3, D2-W319-S1, D2-W319-S2, D2-W319-S3, D2-W322-S1, D2-W301-S2",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md (the held compiles of rounds 117 to 160)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_161_162_P_DRAIN_END_20261012.md",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_163_164_P_DRAIN_END_20261012.md (blob 081cb2b959, msg 6436)",
    "row D2-S108"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Repaired, superseded, or consumed by signed contract text."
 },
 {
  "id": "IRPT_BCKEND-C-S342",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T17:40:00Z",
  "one_line": "~P slug, rounds 117 to 164. Dismissed: Hazards disarmed and read live, and their records: D2-W317-S1 (ARMED: site Z removed the four stale sentinels at 8c85a65a1e; 0 of 4 at origin/box/sitez bb49ae1cad, this seat's read), D2-S102 (the disarm evidence for S60 and W317-S1), D2-W278-S3 and D2-W278-S5 (irpt-status and irpt-narrative released again 2026-10-12 ~14:1xZ; 0 TypeError in 24 hours).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W317-S1",
   "IRPT_BCKEND-D2-S102",
   "IRPT_BCKEND-D2-W278-S3",
   "IRPT_BCKEND-D2-W278-S5"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "Every IRPT_BCKEND order is terminal at this compile (0 active, to-check.py --all). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W317-S1, D2-S102, D2-W278-S3, D2-W278-S5",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md (the held compiles of rounds 117 to 160)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_161_162_P_DRAIN_END_20261012.md",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_163_164_P_DRAIN_END_20261012.md (blob 081cb2b959, msg 6436)",
    "row D2-S108"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarmed or closed on live reads, and the disarm record."
 },
 {
  "id": "IRPT_BCKEND-C-S343",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T17:40:00Z",
  "one_line": "~P slug, rounds 117 to 164. Dismissed: Check defects on terminal orders: the checks were amended and the proofs read VALID (D2-W315-S1 on IB-pr-459 @ad00251c0c; D2-S106 and D2-S107 on IB-pr-413 and IB-pr-404 @e2073040ab), or the order was withdrawn unexecuted (D2-S96 and D2-S97, IB-pr-451 superseded on CTO msg 5770; the explicit deny is a control and was honoured). D2-W317-S2 and D2-W293-S3 are the same class; the class graduates as D2-S101.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W315-S1",
   "IRPT_BCKEND-D2-S106",
   "IRPT_BCKEND-D2-S107",
   "IRPT_BCKEND-D2-S96",
   "IRPT_BCKEND-D2-S97",
   "IRPT_BCKEND-D2-W317-S2",
   "IRPT_BCKEND-D2-W293-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "Every IRPT_BCKEND order is terminal at this compile (0 active, to-check.py --all). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W315-S1, D2-S106, D2-S107, D2-S96, D2-S97, D2-W317-S2, D2-W293-S3",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md (the held compiles of rounds 117 to 160)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_161_162_P_DRAIN_END_20261012.md",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_163_164_P_DRAIN_END_20261012.md (blob 081cb2b959, msg 6436)",
    "row D2-S108"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Check defects on terminal orders; the class carried by D2-S101."
 },
 {
  "id": "IRPT_BCKEND-C-S344",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T17:40:00Z",
  "one_line": "~P slug, rounds 117 to 164. Dismissed: Worker disclosures, face readings and method notes, each stated in its cell's record and consumed by the round that followed: wording and window notes, rebuilt inputs that reproduced, worktree limits (an empty portal checkout, no PyMuPDF), a refused scratch request that read nothing, and forensic notes of the capture rounds.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W278-S4",
   "IRPT_BCKEND-D2-W285-S2",
   "IRPT_BCKEND-D2-W285-S3",
   "IRPT_BCKEND-D2-W286-S1",
   "IRPT_BCKEND-D2-W288-S2",
   "IRPT_BCKEND-D2-W292-S1",
   "IRPT_BCKEND-D2-W293-S1",
   "IRPT_BCKEND-D2-W293-S2",
   "IRPT_BCKEND-D2-W294-S1",
   "IRPT_BCKEND-D2-W297-S2",
   "IRPT_BCKEND-D2-W298-S1",
   "IRPT_BCKEND-D2-W299-S1",
   "IRPT_BCKEND-D2-W299-S2",
   "IRPT_BCKEND-D2-W300-S1",
   "IRPT_BCKEND-D2-W300-S2",
   "IRPT_BCKEND-D2-W300-S3",
   "IRPT_BCKEND-D2-W301-S1",
   "IRPT_BCKEND-D2-W301-S3",
   "IRPT_BCKEND-D2-W303-S1",
   "IRPT_BCKEND-D2-W303-S2",
   "IRPT_BCKEND-D2-W304-S1",
   "IRPT_BCKEND-D2-W304-S2",
   "IRPT_BCKEND-D2-W304-S3",
   "IRPT_BCKEND-D2-W304-S4",
   "IRPT_BCKEND-D2-W305-S1",
   "IRPT_BCKEND-D2-W305-S2",
   "IRPT_BCKEND-D2-W306-S1",
   "IRPT_BCKEND-D2-W308-S1",
   "IRPT_BCKEND-D2-W309-S3",
   "IRPT_BCKEND-D2-W310-S1",
   "IRPT_BCKEND-D2-W310-S2",
   "IRPT_BCKEND-D2-W312-S2",
   "IRPT_BCKEND-D2-W313-S1",
   "IRPT_BCKEND-D2-W315-S2",
   "IRPT_BCKEND-D2-W315-S4",
   "IRPT_BCKEND-D2-W316-S1",
   "IRPT_BCKEND-D2-W318-S1",
   "IRPT_BCKEND-D2-W320-S1",
   "IRPT_BCKEND-D2-W323-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "Every IRPT_BCKEND order is terminal at this compile (0 active, to-check.py --all). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W278-S4, D2-W285-S2, D2-W285-S3, D2-W286-S1, D2-W288-S2, D2-W292-S1, D2-W293-S1, D2-W293-S2, D2-W294-S1, D2-W297-S2, D2-W298-S1, D2-W299-S1, D2-W299-S2, D2-W300-S1, D2-W300-S2, D2-W300-S3, D2-W301-S1, D2-W301-S3, D2-W303-S1, D2-W303-S2, D2-W304-S1, D2-W304-S2, D2-W304-S3, D2-W304-S4, D2-W305-S1, D2-W305-S2, D2-W306-S1, D2-W308-S1, D2-W309-S3, D2-W310-S1, D2-W310-S2, D2-W312-S2, D2-W313-S1, D2-W315-S2, D2-W315-S4, D2-W316-S1, D2-W318-S1, D2-W320-S1, D2-W323-S1",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md (the held compiles of rounds 117 to 160)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_161_162_P_DRAIN_END_20261012.md",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_163_164_P_DRAIN_END_20261012.md (blob 081cb2b959, msg 6436)",
    "row D2-S108"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disclosures and readings recorded in their cells; nothing left to act on."
 },
 {
  "id": "IRPT_BCKEND-C-S345",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T17:40:00Z",
  "one_line": "~P slug, rounds 117 to 164. Dismissed: Records, relays and rows folded into a graduating row: D2-S62 (dismissed on Andrew's word of 2026-10-09, relayed in CTO msg 4327), D2-S71 (two grants applied from dell2 under the signed IB-pr-423), D2-S78 (this seat's row; the vendor release was rolled back at round 122), D2-S79 (a pair's post-promote check that could not discriminate; the act closed), D2-S86 (an SSM trap: an empty command reads Success), D2-S95 (the rollback target on record), D2-S99 and D2-W309-S1 (S99 shows W309-S1 is a vintage artifact), D2-S103 (folded into D2-S98), D2-W312-S1 (folded into D2-W318-S2), D2-S88, D2-W317-S3 and D2-S100 (folded into D2-W324-S1), and this seat's read row D2-S108.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S62",
   "IRPT_BCKEND-D2-S71",
   "IRPT_BCKEND-D2-S78",
   "IRPT_BCKEND-D2-S79",
   "IRPT_BCKEND-D2-S86",
   "IRPT_BCKEND-D2-S95",
   "IRPT_BCKEND-D2-S99",
   "IRPT_BCKEND-D2-W309-S1",
   "IRPT_BCKEND-D2-S103",
   "IRPT_BCKEND-D2-W312-S1",
   "IRPT_BCKEND-D2-S88",
   "IRPT_BCKEND-D2-W317-S3",
   "IRPT_BCKEND-D2-S100",
   "IRPT_BCKEND-D2-S108"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "Every IRPT_BCKEND order is terminal at this compile (0 active, to-check.py --all). ARMED after this compile: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S62, D2-S71, D2-S78, D2-S79, D2-S86, D2-S95, D2-S99, D2-W309-S1, D2-S103, D2-W312-S1, D2-S88, D2-W317-S3, D2-S100, D2-S108",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md (the held compiles of rounds 117 to 160)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_161_162_P_DRAIN_END_20261012.md",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_163_164_P_DRAIN_END_20261012.md (blob 081cb2b959, msg 6436)",
    "row D2-S108"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Records and relays, and rows carried by a graduating row."
 }
]
```
