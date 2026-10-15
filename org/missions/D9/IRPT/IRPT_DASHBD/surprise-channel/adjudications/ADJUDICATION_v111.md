# IRPT_DASHBD: CVO adjudication, round 126 (workstream B-IN, ~I2): the series-ended cause read

<sweep_watermark>2026-10-15T22:28Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T22:28Z, on msg 8722 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND126_BIN_DRAIN_END_20261015.md` @628efedb47, blob 3a51ce3277). Not B-49F's round 126, which is ADJUDICATION_v90. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-i-13 (LOCAL read; worker ~313; merged @3e9df877fd). No judgment criterion. Re-run on the landed tree: DBI126-1-AC1 PASS (rc 0); proof VALID; round-close MAY-CLOSE. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S48",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T22:28:00Z",
  "one_line": "Round 126 B-IN (~I2): the two early-ending Orion series (95 and 120 days) read against Opal's Orion fact_positions silver. 1 of 1 PASS re-run. (1) CAUSE CLASS. 'Not held on the newest partition, therefore CLOSED_OR_TRANSFERRED' is an INFERENCE FROM ABSENCE, the same shape as a 'closed' read elsewhere. The record (SERIES_ENDED_CAUSE_R126.json) carries no claim field. The verdict is a bare word; only the free-text basis_words says 'consistent with a close or transfer', so a consumer cannot reject it as inferred. COMPLETENESS, checked here before absence can mean anything: the newest in-window partition (date=2026-10-13) holds 36,931 rows and 980 distinct accountId, against neighbours 2026-10-12 (36,931 / 980), 2026-10-14 (37,008 / 980) and 2026-10-09/10 (36,916-36,930 / 979). So the partition is complete and no partition-level feed drop explains the absence. What would still separate a close from a single-account drop is an account-status source: Orion's own account record (isActive or a close date) or a custodian close or transfer event. Neither was read. n = 2 accounts in 2 households. Account 2's one held day after its series end is a single partition, not a holding. Read it as 'consistent with closed or transferred, inferred, n = 2', not as a cause established. (2) VALUES: CLOSED_OR_TRANSFERRED, STALE_AT_SOURCE and NOT_DETERMINED are verdict words minted in ~I2's read script (series_ended_cause.py:7-8, :95-98). They are in neither contract 0.4.1 nor contract 0.4.2 (HEAD is now 0.4.2), nor in the 0.4.2 order TO-DB-b-275. They are record vocabulary, not table values, so they owe no contract entry today. If any becomes a reason_class or a served word, it needs ~D2's contract and a rule-24 record first. (3) NUMBERING: this round 126 is the cause read, not the TWR flip the CTO's msg 8696 placed in 'round 126'. The flip is still owed, and it is now TO-DB-i-14, B-IN ROUND 127 ('Orion PRESENT rows write return_basis TWR, provenance stays in source', on contract 0.4.2), which reads complete and has not yet been slugged to this seat. D2-W221-S3 stays ARMED until that round is graded. D2-S91 (ARMED, owner ~P2; SERIES_ENDED_AT_SOURCE) may cite this read as consistent-with-closed for 2 of 2, not as its disarm. Rows: D2-W313-S1 (BLOCKING, INERT: the checker scanned the exempt private path; amended @47c68a361a) and D2-W313-S2 (its reconciliation) are accepted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W313-S1",
   "IRPT_DASHBD-D2-W313-S2"
  ],
  "spec_asserts": "A_VALUE_MUST_CARRY_ITS_CLAIM (an inference from absence carries 'inferred' in a field a consumer can reject on); CLAUDE.md rule 24 (i) (an absence is read only after the population is shown complete); rule 24 for any new value enum.",
  "world_is": "Both early-ending Orion series belong to accounts absent from a complete newest positions partition: consistent with closed or transferred, inferred, n = 2, cause unread. The TWR flip is owed under B-IN round 127 (TO-DB-i-14). Nothing is deployed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T22:2xZ: DBI126-1-AC1 PASS rc 0; proof-of-spec-check VALID rc 0 on ~313",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~313/SERIES_ENDED_CAUSE_R126.json (no claim field; verdict_counts CLOSED_OR_TRANSFERRED 2); series_ended_cause.py:7-8, :95-98",
    "this seat's GET of s3://opal-data-assets/orion/inflection/silver/fact_positions/date=2026-10-09, -10, -12, -13, -14: rows 36916, 36930, 36931, 36931, 37008; distinct accountId 979, 979, 980, 980, 980 (counts only)",
    "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json at HEAD: 0.4.2, no CLOSED_OR_TRANSFERRED or STALE_AT_SOURCE; TO-DB-b-275: 0 occurrences",
    "TO-DB-i-14 <round>127 <status>complete (the 0.4.2 TWR flip)",
    "investigation rows D2-W313-S1, D2-W313-S2, D2-S91, D2-W221-S3",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND126_BIN_DRAIN_END_20261015.md blob 3a51ce3277 (msg 8722)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A BLOCKING checker fault ruled by its amendment, and its reconciliation. The read's verdict is graded as inferred at n = 2 on a complete partition, and the owed TWR flip is placed in round 127."
 }
]
```
