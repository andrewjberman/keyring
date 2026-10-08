# IRPT_DASHBD -- round 25 (workstream B) L8/L9 adjudication

<sweep_watermark>2026-10-07T19:4xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~20:3xZ. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND25_B_DRAIN_END_20261007.md @7cadad7a87` (msg 1059). 3 of 3 orders terminal, merged and VALID
@5ffd7b740d; 0 judgment criteria; LOCAL. 5 rows: 3 dismissed below, 2 graduated OPEN in `remediations/REMEDIATION_v11.md`. Clocks in
REMEDIATION_v10: W21-S4 and W21-S5 REMEDIATED and closed; W21-S6 REMEDIATED, not closed until it ships tested on the served pandas. ARMED: 0.

```json
[
 {
  "id": "IRPT_DASHBD-C-S21",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T20:30Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "W22-S1 (the lag bound governs only in-kind legs), W22-S2 (a lot event id repeats after a wash sale re-dates it; fixed by the acquired-date tie-break) and W22-S4 (round 24's regrade script no longer runs) are dismissed; W21-S4 and W21-S5 are closed in place, W21-S6 advanced.",
  "adjudicates": [
   "IRPT_DASHBD-W22-S1",
   "IRPT_DASHBD-W22-S2",
   "IRPT_DASHBD-W22-S4"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "W22-S1 and W22-S2 are measured notes on the lag rule and the sale link, each settled by DB-b-38/39. W22-S4: identity_regrade_e2.py is a round-24 deliverable that read served_runtime(), now removed; its record stays the round-24 evidence, and round 25's re-run is the current one. Clocks in REMEDIATION_v10: W21-S4 REMEDIATED and closed (all 4 non-rounding windows named as rule causes, wash-sale basis and in-kind re-selection, fixed through the rule; 91-window re-run 58 tie, 33 miss, all within 0.05; with both rules off the 4 return round 24's gaps exactly). W21-S5 REMEDIATED and closed (887 of 887 trades matched to their lot row, max 1 trading day; LEG_LAG_DAYS 3 -> 1). W21-S6 REMEDIATED, not closed: the option is set once per process and classify_and_sum is hardened in source, but the hardening is unmeasured on the served layer's pandas 2.2.3 and ships only with the next reporting-gold release.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows IRPT_DASHBD-W22-S1, IRPT_DASHBD-W22-S2, IRPT_DASHBD-W22-S4",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND25_B_DRAIN_END_20261007.md @7cadad7a87",
    "pytest -q data/assets/scripts/gold/irpt_reporting/tests: 88 passed (this compile's read, dell2 CLOUD, 2026-10-07 ~20:2xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Measured notes settled by the round, and a superseded deliverable."
 }
]
```
