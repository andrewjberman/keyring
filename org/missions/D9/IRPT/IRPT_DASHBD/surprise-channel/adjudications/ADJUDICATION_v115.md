# IRPT_DASHBD: CVO adjudication, round 129 (workstream B-IN, ~I2): the first-real-row run script

<sweep_watermark>2026-10-15T23:58Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T23:58Z, on msg 8776 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND129_BIN_DRAIN_END_20261015.md` @f94a84d4a7, blob b1e7b4ce2f). Not B-49F's round 129, which is ADJUDICATION_v92. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-i-16 (LOCAL; worker ~316; merged @0350741d4c). No judgment criterion. Re-run on the landed tree (HEAD feb0a37a46): DBI129-1-AC1..AC3, 3 of 3 PASS (rc 0); proof VALID. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S52",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T23:58:00Z",
  "one_line": "Round 129 B-IN (~I2): run_scope_feed_real.py, which lists the feed silver, runs the round-127 wrapper and returns counts only. 3 of 3 PASS re-run. Not exercised on real data. Its chain check compares chained rows with the silver's own factors, not with Orion's reported period return, as the issuer states. GRADING GAP, THIS SEAT'S: v110 graded round 125 MAY-CLOSE on fixtures that were not feed-shaped. The real feed writes one partition per calendar day and stamps every row of a pull with the pull date, so a backfill's rows carry a pull_date later than their partition. The round-125 wrapper (still at HEAD, inflection_scope_feed_run.py @b80bd23364) refuses that shape. REPRODUCED HERE: the round-130 checker's backfill-shaped feed (p130_run_partition.py silver_backfill) against the wrapper at HEAD gives 'ValueError: partition keys refused: 48 row(s) name another pull date', DBI130-1-AC1 FAIL. v110 dismissed W311-S5 ('a partition key that disagrees with its rows') on the wrapper's refusal at run.py:112 without asking what the real feed's partition key means. That is a grading gap of this seat, not only the issuer's defect: a criterion that passes on a fixture shaped by the rule it tests proves the rule, not the rule's fit to the world. The issuer found it first and disclosed it. Round 130 (TO-DB-i-17) re-keys the refusal on the row's day. The first real run must not start before that merges. ROUND 130's FORM: issued as a task order, not done outside the issuance. issue commit f71ea6eefc (~I2), drained into the shared tree @d9e8307c5d with its checker p130_run_partition.py and decomposition entry, issued_to worker ~317, status pending. Its <direct_act>true marks an order cut on the issuer's own finding, not on a CTO analysis cell. A worker executes it, so rule 27 (the COO issues, workers execute) holds. ROUND 128 EXISTS: TO-DB-i-15 (the series-ended record's cause_claim line, <direct_act>true, worker ~315), issued @d5d026244d, complete, drained @b421b07328. No ROUND128_BIN drain-end packet exists in ~I2's folder, so A PACKET IS OWED for round 128 (or a stated fold into another). Rows: D2-W316-S1..S6 are inert observations, accepted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W316-S1",
   "IRPT_DASHBD-D2-W316-S2",
   "IRPT_DASHBD-D2-W316-S3",
   "IRPT_DASHBD-D2-W316-S4",
   "IRPT_DASHBD-D2-W316-S5",
   "IRPT_DASHBD-D2-W316-S6"
  ],
  "spec_asserts": "Spine L9: the CVO grades against the world the code will meet, not only against fixtures shaped by the rule under test; rule 27: the COO issues, workers execute; every terminal round sends one packet.",
  "world_is": "The run script exists and passes on fixtures. The wrapper it calls refuses the real feed's backfill shape (48 rows on the feed-shaped fixture) until round 130 merges. Round 128 drained with no packet. Nothing has run on real data. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T23:5xZ (HEAD feb0a37a46): DBI129-1-AC1..AC3 PASS rc 0; proof-of-spec-check VALID rc 0 on ~316",
    "python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r130/p130_run_partition.py . DBI130-1-AC1 at HEAD: FAIL, 'partition keys refused: 48 row(s) name another pull date'",
    "data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py last changed @b80bd23364; ADJUDICATION_v110 (W311-S5 dismissed on run.py:112)",
    "TO-DB-i-15 <round>128 <direct_act>true complete (issue d5d026244d, drain b421b07328); TO-DB-i-17 <round>130 <direct_act>true pending, issued_to ~317 (issue f71ea6eefc, drain d9e8307c5d); no ROUND128_BIN packet in 2.0.0_SA_COO~I2/",
    "investigation rows D2-W316-S1..S6",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND129_BIN_DRAIN_END_20261015.md blob b1e7b4ce2f (msg 8776)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Six inert worker rows. The wrapper defect, this seat's v110 grading gap and the missing round-128 packet are named for the CTO and the issuer, not repaired here."
 }
]
```
