# NFRA_TRNSPT -- rounds 17-19 L8 adjudication

<sweep_watermark>2026-10-09T09:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~09:4xZ. L8 inputs: org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R19_CLOSE.md @a32646d928, R18_CLOSE.md @5825d7966d, R17_CARRIED_RUNS_CLOSE.md @b85c74058c (msg 3010). 0 judgment criteria;
rounds 18 and 19 MAY-CLOSE. 3 rows dismissed below; 3 graduate OPEN in `remediations/REMEDIATION_v8.md`. ARMED: 0.

**For the analysis:**
1. **The Teams silver is not wiped** (W1-S7). C-TIERS says silver is PII-wiped, and C-READERS lets a scoped role read it; the writer
   applies no wipe. No scoped reader may be granted on Teams silver until that holds.
2. **The Teams pull cannot land a meeting** (D2-S10): its gateway transport is a stub, and pull.tf names a bearer secret that does not exist.
3. **The 365-day precedent is empty** (D2-S9): all 6 backfilled rows are held out by the wipe's residual check.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S15",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:40:06Z",
    "one_line": "Rounds 17-19 rows dismissed: D2-W1-S8 (read_meeting.py printed held_out rows; fixed in the drain @6509d14fa3), D2-W2-S4 (the grant named a test file by the wrong name; held_out added only to wiped rows, as built), D2-W3-S4 (ARMED: two test assertions broken by the listing snapshot; disarmed @1994c45467, which counts the snapshot as 8 puts and selects the run record -- measured an ancestor of HEAD).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W1-S8",
      "NFRA_TRNSPT-D2-W2-S4",
      "NFRA_TRNSPT-D2-W3-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~09:4xZ: round-close-check --round 18 and --round 19 MAY-CLOSE; 6509d14fa3 and 1994c45467 are ancestors of box/dell2 HEAD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W1-S8, D2-W2-S4, D2-W3-S4",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R19_CLOSE.md @a32646d928, R18_CLOSE.md @5825d7966d, R17_CARRIED_RUNS_CLOSE.md @b85c74058c (msg 3010)",
        "this seat's reads ~09:4xZ: round-close-check --round 18 and --round 19 MAY-CLOSE; 6509d14fa3 and 1994c45467 are ancestors of box/dell2 HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Fixed in the drain (measured), or as built."
  }
]
```
