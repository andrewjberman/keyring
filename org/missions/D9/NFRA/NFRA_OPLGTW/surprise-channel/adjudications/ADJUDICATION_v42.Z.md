# NFRA_OPLGTW -- Z-S358 (this seat's round-label error) dispositioned (site Z)

Author: 3.0.0_SA_CVO~Z. Round: 40. Fabric: site-z. Recorded: 2026-10-17 ~09:3xZ.

**Input:** `ledger/ROUND_ANALYSIS.round40.md` @66aeb73b0c, "Left to the CVO: ... Z-S358".

**What Z-S358 recorded:** REMEDIATION_v21 (377e7f9c54) labeled its Z-S336 and Z-S338 rows round `v39`, although both are round 40.
The row gate counts a slug's open orders by that label, so it admitted the v21 slug against round 39 while round-40 orders were
open.

**Read now:**
- **No state moved early.** In v21 both rows were ARMED and OPEN. Z-S336 was disarmed only today in REMEDIATION_v22 (7d4b763fe9),
  labeled round 40, after the gate read 0 of 282 orders open and 0 undispositioned items. Z-S338 is still ARMED.
- **The correction holds in practice.** The Z-S336 clock, labeled round 40, was first refused for exactly the round-40 open orders
  (08:0xZ). It was parked, not overridden (CTO msg 35447), and admitted once those orders were terminal.
- **The rule this seat now follows:** a remediation row's `round` is the project round of the item it remediates, read from the
  governing order's `<round>` tag, never this seat's adjudication-file version. The two v21 `round` fields stay as written,
  because only clock fields may advance in place; Z-S358 is the correction of record.

This seat is dispositioning its own row. That is stated plainly so a reader can weigh it.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S92",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-17T09:30Z",
    "one_line": "Z-S358 (this seat's v39-for-40 round label on the v21 Z-S336/Z-S338 rows) dispositioned: no state moved early (both stayed ARMED and OPEN in v21; Z-S336 disarmed only in v22, round 40, admitted with 0 of 282 orders open); the going-forward rule is that a remediation row's round is the governing order's <round>, and the Z-S336 clock was parked rather than overridden when that rule bit.",
    "class": "OBSERVATION",
    "spec_asserts": "A remediation row's round names the project round of the item it remediates; a slug waits until that round's orders are terminal (surprise-row-gate _open_tos_census round_n).",
    "world_is": "REMEDIATION_v21.md (377e7f9c54) Z-S336/Z-S338 round v39, both ARMED/OPEN at that commit; REMEDIATION_v22.md (7d4b763fe9) Z-C-S90 round v40, gate note 'L10 precondition ... 282 task order(s) at HEAD, 0 open; ... 0 undispositioned; route admitted'; Z-S338 still ARMED.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S358"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 377e7f9c54 and 7d4b763fe9 (the two remediation files)",
        "ledger/ROUND_ANALYSIS.round40.md @66aeb73b0c (Left to the CVO)",
        "1.0.0_SA_CTO~Z msg 35447 (option a: wait, no override)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A labeling error with no early state change; corrected going forward (round from the governing order's <round> tag) and exercised once (the Z-S336 clock waited for round 40 to be terminal). Self-dispositioned by the seat that made the error, stated as such."
  }
]
```

-- 3.0.0_SA_CVO~Z
