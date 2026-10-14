# ADVI_COTBKF: CVO adjudication, rounds 83 and 84

<sweep_watermark>2026-10-13T23:52</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T23:52:38Z, on msg 7358 (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_83_84_DRAIN_END_20261014.md @14ee4128f1`). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_83_84_L9_GRADE_20261014.md`): CB83ce1-AC3 FAIL on one
clause (derivation not checked; the salt is lost), CB83ce2-AC3, CB83ce3-AC3 and CB84cf1-AC3 PASS with notes. 13 rows dismissed below;
D2-W164-S1 to -S3 (ARMED) are held to round 85's compile. Recommended for round 85: one key space for the whole set (raw ids, which
Andrew's 2026-10-09 word allows here, or a token whose derivation is committed).

```json
[
 {
  "id": "ADVI_COTBKF-C-S67",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T23:52:38Z",
  "one_line": "Rounds 83 and 84. L9: CB83ce1-AC3 FAIL on one clause (the derivation was not checked: the round-82 salt is lost), CB83ce2-AC3 PASS (note: 10 month_grades Year/ITD columns unchanged by code reading only; measure them before the label's apply), CB83ce3-AC3 PASS (price-conditional key accepted: 0 disagreeing days merged), CB84cf1-AC3 PASS (NEW_CLIENT run on the active-set windows, disclosed). Dismissed: D2-S135 (the CTO's disarm record of D2-W155-S1: route_not_live); D2-W165-S2 and -S4 (BLOCKING; the unmeasured month_grades columns, carried in the ce-2 grade as a precondition of any apply); D2-W165-S5 and D2-W166-S1 (BLOCKING; the status flip outside <paths>, flipped by the issuer, and the AC1 invocation's collection error, present at HEAD and amended); D2-W166-S2 (graded in CB83ce3-AC3); D2-W166-S4 (the W158-S2 id carries two subjects; its disarm is the CTO's); readings D2-W164-S4, D2-W165-S1, -S3, D2-W166-S3, D2-W167-S1, -S2. HELD to round 85's compile, not adjudicated here: D2-W164-S1, -S2, -S3 (ARMED: the lost salt, the four identifiers under the old definition, the mixed key space), which the issuer disarms on round 85's rebuilt files; no remediation row can be written while TO-CB-cg-1 runs.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "ADVI_COTBKF-D2-S135",
   "ADVI_COTBKF-D2-W164-S4",
   "ADVI_COTBKF-D2-W165-S1",
   "ADVI_COTBKF-D2-W165-S2",
   "ADVI_COTBKF-D2-W165-S3",
   "ADVI_COTBKF-D2-W165-S4",
   "ADVI_COTBKF-D2-W165-S5",
   "ADVI_COTBKF-D2-W166-S1",
   "ADVI_COTBKF-D2-W166-S2",
   "ADVI_COTBKF-D2-W166-S3",
   "ADVI_COTBKF-D2-W166-S4",
   "ADVI_COTBKF-D2-W167-S1",
   "ADVI_COTBKF-D2-W167-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "All 4 orders of rounds 83 and 84 are complete (order files read); round 85 (TO-CB-cg-1) is active. Code edits on four price-store readers and three serve scripts; nothing applied, minted, served or fetched from a vendor. The porting-verdict pair's COO half is a DRAFT, unsigned. REVERSE_MATCH_V2.csv sits outside the repository, superseded by round 85.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S135, D2-W164-S4, D2-W165-S1, D2-W165-S2, D2-W165-S3, D2-W165-S4, D2-W165-S5, D2-W166-S1, D2-W166-S2, D2-W166-S3, D2-W166-S4, D2-W167-S1, D2-W167-S2",
    "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_83_84_DRAIN_END_20261014.md @14ee4128f1 (msg 7358)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_83_84_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A disarm record, graded deviations, amended or issuer-resolved process rows, and readings; three ARMED rows held to round 85."
 }
]
```
