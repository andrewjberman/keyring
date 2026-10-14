# IRPT_DASHBD: CVO adjudication, round 107

<sweep_watermark>2026-10-14T15:55Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO~DELL2`, 2026-10-14T15:55Z, on msg 7720 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND107_B_DRAIN_END_20261014.md`, blob 78683c7421). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_107_L9_GRADE_20261014.md`): DB107-1-J1 PASS. The p.5 pointer now names p.4, which prints the household period totals; the p.6 foot note is class-only; the p.2 pointer is unmoved. DB107-1-AC1 and the five earlier live criteria re-run here: 6 of 6 PASS. 3 rows dismissed below. The disclosure release gate (Andrew's call a252) still holds every client render.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S4",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T15:55:00Z",
  "one_line": "Round 107. L9: DB107-1-J1 PASS. Pages 2, 4, 5 and 6 read: the p.5 chart note points to 'the table on page 4', which prints the household's Net Additions, Net Gain and Ending Value for four windows; the p.6 foot note names the class figures only and matches the class rows; the split-column line prints once; the p.2 pointer to p.6 is unmoved (14 pages, as in round 106). Dismissed (3): D2-W170-S1 (the note-level rule does not key the per-account 'chart: not available yet.' sentences; ruled in D2-S33, nothing contradicted today, keyed next render round), D2-W170-S2 (no committer identity in the portal worktree, set per command), and D2-S33.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W170-S1",
   "IRPT_DASHBD-D2-W170-S2",
   "IRPT_DASHBD-D2-S33"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): judgment criteria are graded at L9, never self-graded; every round row is dispositioned before the slug.",
  "world_is": "DB-b-209 is merged LOCAL (19370b057a); the portal commits are LOCAL and unpushed; nothing served moved. J1 is met on the 49financial sample. What still stands between this render and a client: the disclosure page (a252) and the candidate's route through the portal approval rows.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's read of pages 2, 4, 5, 6 of fwd21_sample_r107/pages/final/ (private; no figure copied)",
    "this seat's re-run 2026-10-14T15:5xZ: DB107-1-AC1, DB105-1-AC1, DB105-2-AC1, DB105-3-AC1, DB106-1-AC1, DB106-2-AC1 PASS",
    "investigation rows D2-W170-S1, D2-W170-S2, D2-S33",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_107_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A ruled checker blind spot with no contradicted figure today, a worktree identity note, and the ruling row."
 }
]
```
