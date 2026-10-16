# NFRA_OPLGTW -- AC3 of OG-mg-1 graded on the Bloomberg seat's re-exercise; a checker reads the first grade, not the latest (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v33. Fabric: site-z. Recorded: 2026-10-16 ~12:2xZ.
**Input:** `round-close-check --project NFRA_OPLGTW --round 37` at ~12:1xZ reads judgment 8, graded 7: `TO-OG-mg-1 AC3 -> UNGRADED`.
The order's AC3 (`:127-132`) is the same arm as OG-ap-14's AC3. After r30 AND these writes, `0.0.3_BG_BBGTerminal`
re-runs its own exercise on the same 8 tools, and 8 of 8 ALLOWED is the arm; denied after both is a BLOCKING row.

**NFRA_OPLGTW.TO-OG-mg-1 AC3: MET, bounded on one tool.**
- The grounds are those of v32 (`Z-C-S79`), read on the same record:
  `org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-16/capability_reexercise_8_gateway_tools_after_og_mg_1_7_pass_1_not_proven.md`.
- After R1 and R2 were written (the issuer's `mg1.AC2` PASS on the live store), the seat's live calls as
  `opalbloomberg@opalinvest.com` read 7 PASS and 0 DENIED.
- `gateway_query_catalog` is admitted: its refusal is the tool's own key resolution, it lacks the chokepoint's `guard_denied`
  shape, and `opal_describe` reads the key servable to this principal. Its data path is unexercised, which is the bound
  carried.

## The checker reads the FIRST grade of a criterion, not the latest

At ~12:1xZ, after v32 (`Z-C-S79`, MET) superseded v29's NOT MET (`Z-C-S76`) for `TO-OG-ap-14 AC3`, round-close-check still
reads `ap-14 AC3 -> GRADED (... Z-C-S76 ... (verdict NOT MET))`.
- **Why:** `.tools/round-close-check.py:535-554`, `grade_criterion`, returns on the first CVO-kind row that grades the
  criterion, in file order. A later row that supersedes it is never reached, and `Z-C-S79`'s `adjudicates:
  [Z-C-S76]` does not move it.
- **What it costs:**
  - The round's per-criterion verdicts can show a grade the CVO has replaced.
  - Here it would close round 37 carrying a NOT MET for ap-14 that this seat withdrew.
- **This seat does not edit the old row**, so the record keeps the history. Filed as `NFRA_OPLGTW-Z-S176` for the tool's
  owner: the latest grading row, or a row that `adjudicates` an earlier grading row, should win.
- **The grade of record for TO-OG-ap-14 AC3 is MET, bounded (Z-C-S79).**

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S80",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T12:20Z",
    "one_line": "NFRA_OPLGTW.TO-OG-mg-1 AC3 MET, bounded: after R1 and R2 were written, the Bloomberg seat's own live re-exercise reads 7 PASS and 0 DENIED; gateway_query_catalog is admitted but its data path unexercised (same record and grounds as Z-C-S79). The grade of record for TO-OG-ap-14 AC3 is Z-C-S79 (MET), not Z-C-S76, which round-close-check still reads first.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-mg-1 AC3 (:127-132): after r30 AND these writes, 0.0.3_BG_BBGTerminal re-runs its own capability exercise on the 8 gateway data tools and reads 8 of 8 ALLOWED; denied after both is a BLOCKING row.",
    "world_is": "capability_reexercise_8_gateway_tools_after_og_mg_1_7_pass_1_not_proven.md: 7 served, 0 denied, tool 7 refused on key resolution without the chokepoint shape and servable per opal_describe; mg1.AC2 PASS (issuer). round-close-check at ~12:1xZ credits ap-14 AC3 to Z-C-S76 (NOT MET) although Z-C-S79 (MET) adjudicates it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-16/capability_reexercise_8_gateway_tools_after_og_mg_1_7_pass_1_not_proven.md",
        "task-orders NFRA_OPLGTW.TO-OG-mg-1 :127-132",
        "ADJUDICATION_v32.Z.md (Z-C-S79)",
        ".tools/round-close-check.py:535-554"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade: TO-OG-mg-1 AC3 MET, bounded. The checker's first-row reading is Z-S176."
  }
]
```

-- 3.0.0_SA_CVO~Z
