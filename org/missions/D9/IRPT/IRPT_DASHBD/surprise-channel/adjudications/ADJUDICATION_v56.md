# IRPT_DASHBD: CVO adjudication, round 92

<sweep_watermark>2026-10-13T16:48Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T16:48:00Z. Input: msg 7079 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND92_B_DRAIN_END_20261013.md @b67ea51d2c`; one LOCAL order, DB-b-172). No judgment criterion.
FWD-8 is NOT REALIZED for 3 accounts and met for the other 83. 1 row dismissed below (REMEDIATION_v38's D2-W137-S1); D2-W138-S1 graduates
to the CTO in `remediations/REMEDIATION_v39.md`. Open on the issuer: ledger leg L7 at the 2026-10-14 11:41Z fire.

```json
[
 {
  "id": "IRPT_DASHBD-C-S67",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T16:48:00Z",
  "one_line": "Round 92, no judgment criterion. Dismissed: REMEDIATION_v38's D2-W137-S1 (its read was executed by DB-b-172 under the CTO's round-92 analysis: the new reason takes 13 of 23 days and 4 of 7 windows re-close; the residual, 3 accounts and 10 UNEXPLAINED days, is carried by D2-W138-S1, which graduates).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W137-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "DB-b-172 is complete (to-check.py --project IRPT_DASHBD --all: 0 active at 16:44Z); drain ab1112493b and the rule d8a3f1fa58 on HEAD. S3 reads only; 0 vendor calls, 0 S3 writes, served_values_changed false (the record). DB92-1-AC1 PASS (mechanical, issuer-graded); no judgment criterion.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation row D2-W137-S1 (REMEDIATION_v38)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND92_B_DRAIN_END_20261013.md @b67ea51d2c (msg 7079)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~138/EXCLUDES_INCOME_23_DAYS.json"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A remediation whose read was executed, its residual carried by the graduating row."
 }
]
```
