# IRPT_DASHBD: CVO adjudication, round 109 (the first Inflection render)

<sweep_watermark>2026-10-14T18:43Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO~DELL2`, 2026-10-14T18:43Z, on msg 7801 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND109_B_DRAIN_END_20261014.md`, blob 9de51f92ce). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_109_L9_GRADE_20261014.md`): DB109-2-J1 FAIL. Four counts: the account 'Since 2026-06-15' benchmark column prints the household's since-2024-07-30 figures; the gain/loss Ending Value reads unavailable while the account pages print it; benchmark YTD/L12M say 'needs more history' while p.4 prints them; the p.5 split-column cells get two reasons. Plumbing and layout are met. DB109-1..3-AC1 re-run here: 3 of 3 PASS. 12 rows dismissed below. Held: D2-W173-S2 (ARMED; likely seat of count 1), D2-W173-S9 (ARMED; the ordinal relabel reads as an account number, so the disarm in D2-S36 is not accepted for a client render), D2-W173-S10 (the ending-value blanking, count 2's family), D2-W174-S2 (BLOCKING; two missing Orion days, the next enrichment), D2-W174-S4, -S5 (data facts for the CTO). No remediation row while round 98 runs.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S6",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T18:43:00Z",
  "one_line": "Round 109. L9: DB109-2-J1 FAIL on 4 counts, all 20 pages read (see the grade file). Met: no plumbing visible, the 49 Financial layout, lots absent in words. Dismissed (12): D2-W173-S1 (BLOCKING; the household-return fill the contract sources ABSENT, amended by the issuer), D2-W173-S8 (BLOCKING; the issuer's checker clauses assumed a 49F-shaped sample, amended), D2-W173-S3 (125 Orion asset labels, no granted class table: allocation absent in words), -S4 (as_of moved to the last positions date, amended), -S5 (ending values from positions, the build followed the TO), -S6 (Orion account id used as the key, read), -S7 (membership read after the as_of move), -S11 (page estimate for wrapped rows, fixed), D2-W174-S1 (account id not zero-padded, read), -S3 (calendar-daily partitions, one repair with S2), D2-S35 (the issuer's dispositions of W174), D2-S36 (the issuer's rulings of W173-S8..S11, recorded; this seat does not accept its disarm of W173-S9 for a client render, so W173-S9 stays ARMED). Held: D2-W173-S2, -S9, -S10, D2-W174-S2, -S4, -S5.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W173-S1",
   "IRPT_DASHBD-D2-W173-S8",
   "IRPT_DASHBD-D2-W173-S3",
   "IRPT_DASHBD-D2-W173-S4",
   "IRPT_DASHBD-D2-W173-S5",
   "IRPT_DASHBD-D2-W173-S6",
   "IRPT_DASHBD-D2-W173-S7",
   "IRPT_DASHBD-D2-W173-S11",
   "IRPT_DASHBD-D2-W174-S1",
   "IRPT_DASHBD-D2-W174-S3",
   "IRPT_DASHBD-D2-S35",
   "IRPT_DASHBD-D2-S36"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): judgment criteria are graded at L9, never self-graded; every BLOCKING row is dispositioned before the slug; an ARMED row leaves ARMED only on a disarm whose read holds.",
  "world_is": "All three round-109 orders complete; merges on origin box/dell2; nothing served or written to AWS. Inflection renders one household through the same components, but a benchmark window mislabelled at account grain and an ending value hidden in one section misinform. The issuer's whole-document and note-level rules (0 conflicts) do not reach either pair.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's read of 20 of 20 pages, fwd21_sample_r109/pages/run5/ (private; no client figure copied)",
    "this seat's re-run 2026-10-14T18:4xZ: DB109-1-AC1, DB109-2-AC1, DB109-3-AC1 PASS",
    "investigation rows D2-W173-S1..S11, D2-W174-S1..S5, D2-S35, D2-S36",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_109_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two BLOCKING rows closed by the issuer's amendments, build readings followed or fixed in the round, and the issuer's two disposition records. Rows tied to this grade's counts, the label condition, the next enrichment and the CTO's data facts are held."
 }
]
```
