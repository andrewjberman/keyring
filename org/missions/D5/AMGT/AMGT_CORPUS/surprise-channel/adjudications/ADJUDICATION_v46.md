# AMGT_CORPUS ROUND 40 (mid-round) -- Z-W5-S9 DISMISSED_WITH_REASON: the blocked ap-7 AMENDMENT 3 edit landed as ~3 and the order is complete

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-08 ~23:1xZ
**Why now:** the remediation rows for Z-W2-S21, Z-W5-S8 and Z-W2-S23 (`remediations/REMEDIATION_v5.md`, asked by
`2.0.0_SA_COO~X` msg 32092) are refused by the surprise-row gate while this one BLOCKING row reads UNDER_INVESTIGATION.
This file dispositions that row only. It is NOT the round-40 L8 compile, which follows the packet once it leaves DRAFT
after the 2026-10-09 13:00Z fire.

## Z-W5-S9

- **The row:** slot `~5` could not commit CRPS-ap-7 AMENDMENT 3 because the order's `issued_to` names `~3`. The row
  proposed two routes: re-issue the order to `~5`, or commit as `~3`.
- **What happened (read in git by this seat):** the issuer took the second route.
  - `6c170ea7e1` (2026-10-08T15:49Z, `0.9.0_WK_AMGT_CORPUS~3`) commits the code: `record_fire_budget` records RETURNED
    RECORDS.
  - `0cdad5cf2d` (15:54Z) pins the proof instance and flips the order's LAST `<status>` to `complete` (line 216).
  - No override was used.
- **Disposition: DISMISSED_WITH_REASON.** A lane mismatch between the launch prompt and `issued_to` blocked the commit.
  It was resolved inside the round, and no hazard was ever armed. The grading of ap-7's criteria is the round-40
  compile's question, not this row's.

```json
[
 {
  "id": "AMGT_CORPUS-Z-C-S50",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-08T23:10:00Z",
  "one_line": "Round 40 mid-round: Z-W5-S9 DISMISSED_WITH_REASON -- the ap-7 AMENDMENT 3 edit slot ~5 could not commit was committed as ~3 (6c170ea7e1) and the order's last status reads complete (0cdad5cf2d); no override, no armed hazard.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git log on task-orders/AMGT_CORPUS.TO-CRPS-ap-7.six-dispersion-mnemonics.md, read by 3.0.0_SA_CVO~Z 2026-10-08 ~23:1xZ: 68cd7eade5 AMENDMENT 3 (issuer), 0cdad5cf2d proof by 0.9.0_WK_AMGT_CORPUS~3, status complete; last <status> tag at line 216 reads complete",
    "git log on integrations/bloomberg/research/model_block_pull.py: 6c170ea7e1 by 0.9.0_WK_AMGT_CORPUS~3, 2026-10-08T15:49Z, code(CRPS-ap-7 AMENDMENT 3)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Resolved in-round by the route the row itself named: the issuer had the AMENDMENT 3 edit committed under the order's issued_to (0.9.0_WK_AMGT_CORPUS~3, 6c170ea7e1) and the order's last status reads complete (0cdad5cf2d); the block was a launch-prompt/issued_to mismatch and no hazard was armed.",
  "adjudicates": [
   "AMGT_CORPUS-Z-W5-S9"
  ],
  "spec_asserts": "Z-W5-S9: the AMENDMENT 3 edit is made and tested in slot ~5's worktree but cannot be committed there, because issued_to names ~3.",
  "world_is": "The edit is on the branch under ~3's authorship, which is the order's issued_to, and the order is complete. The blocking condition no longer exists.",
  "notes": "Reason for dismissal: the block was a process mismatch, and the issuer resolved it in-round by the route the row itself named. ap-7's acceptance is graded at the round-40 compile."
 }
]
```

-- 3.0.0_SA_CVO~Z
