# IRPT_DASHBD: CVO adjudication, round 96

<sweep_watermark>2026-10-14T01:02:18Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-14T01:02:18Z. Input: msg 7395 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND96_B_DRAIN_END_20261014.md @32070ec5e1`; two LOCAL orders, DB-b-180 and DB-b-181).
No judgment criterion. This seat re-ran DB96-1-AC1: PASS. 5 rows dismissed below. **Before round 98 applies the FDRXX rule:** D2-W147-S3
(ARMED) says a synthetic CASH_USD position still serves fixed_income while Cash-typed rows will serve cash; resolve it or name it in the pair.

```json
[
 {
  "id": "IRPT_DASHBD-C-S71",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T01:02:18Z",
  "one_line": "Round 96, no judgment criterion. Dismissed: D2-W146-S1 (BLOCKING, ARMED: the components could not render the real sample; after round 97's shape fix the render ran, and this seat re-ran DB96-1-AC1: PASS, so the hazard no longer holds); D2-W146-S2 (two absent counts, 73 by the build record and 62 top-level markers: two definitions, both stated); D2-W146-S3 (the criterion's eight-digit rule against a dated private folder name: the folder is outside the repository); D2-W147-S1 and -S2 (the served class sits in platinum advisor positions with no account key; the 178 accounts are read from the holdings, stated). HELD, not adjudicated: D2-W147-S3 (ARMED: a synthetic CASH_USD position still serves fixed_income while a canonical Cash-typed row will serve cash; the two cash paths disagree. This must be resolved, or named in the signed pair, BEFORE round 98's DB-b-183 applies the FDRXX rule). Stay open with the issuer for Andrew's read and the next round: D2-W146-S4 (18 PDF pages footed 'Page n of 12') and -S5 (no chart draws).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W146-S1",
   "IRPT_DASHBD-D2-W146-S2",
   "IRPT_DASHBD-D2-W146-S3",
   "IRPT_DASHBD-D2-W147-S1",
   "IRPT_DASHBD-D2-W147-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "DB-b-180 and DB-b-181 are complete. The real sample is rendered privately (tab HTML, export HTML, export PDF), outside the repo. The FDRXX-to-CASH rule is committed (e340e07f4e) and its never-widen packet is signed on both halves (CTO half d3b576bb67); the apply is round 98's DB-b-183, which is issued and active, so no remediation row is written this compile. No served byte moved.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W146-S1, D2-W146-S2, D2-W146-S3, D2-W147-S1, D2-W147-S2",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND96_B_DRAIN_END_20261014.md @32070ec5e1 (msg 7395)",
    "this seat's run 2026-10-14T01:02 of DB96-1-AC1 from TO-DB-b-180: PASS (the real sample rendered to an 18-page PDF and two HTML files in the private folder; 117 member ids; the record holds paths and hashes only); drains 66e73a39e5 and 89f747e70f on HEAD"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An ARMED render failure re-run to PASS by this seat, two counting definitions, and readings; one ARMED row held before the apply."
 }
]
```
