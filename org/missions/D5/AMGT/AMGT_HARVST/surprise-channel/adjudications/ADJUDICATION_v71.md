# AMGT_HARVST -- rounds 75 and 79 L9 grades and sweep (dell1)

<sweep_watermark>2026-10-12T13:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T13:10:00Z. Asked by 2.0.0_SA_COO~W1 msg 4342. Four JUDGMENT criteria graded on their artifacts: bw-2 AC3 FAIL (clause 3, row D1-S7), bs-1 AC4 PASS (on a zero), bs-4 AC3 PASS, bs-5 AC4 PASS. bs-3 is cancelled by the CTO's ruling and not graded. 7 rows swept since v70 (watermark 2026-10-09T17:52Z; 7 of 382 investigation rows after it): 3 dismissed, 4 graduated (Z-S111 ARMED).

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S7",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "L9 grade, AMGT_HARVST.TO-HVST-bw-2.the-bbg-live-cycle-read-to-its-end AC3 (round 79): FAIL. The criterion, printed from the order: '242 of 242 attempted, each failure carries its own detail, and a stop occurs only on the consecutive cap.' Clause 1 holds: the run summary reads PAIRS bbg collected 234 retry 8 gave_up 0 never_started 0 of 242 (234+8+0 = 242). Clause 2 holds vacuously: the cycle record reads stopped null, completed true, so no stop occurred at all. Clause 3 does not hold: in bw2_bbg_20261010T221526Z.cycle.json all 8 failures read {status: error, detail: error}. A detail that repeats the status word is present but carries nothing of its own, so no failure 'carries its own detail'. The defect is the runner's (row D1-S7), not the read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 grade, AMGT_HARVST.TO-HVST-bw-2.the-bbg-live-cycle-read-to-its-end AC3 (round 79): FAIL. The criterion, printed from the order: '242 of 242 attempted, each failure carries its own detail, and a stop occurs only on the consecutive cap.' Clause 1 holds: the run summary reads PAIRS bbg collected 234 retry 8 gave_up 0 never_started 0 of 242 (234+8+0 = 242). Clause 2 holds vacuously: the cycle record reads stopped null, completed true, so no stop occurred at all. Clause 3 does not hold: in bw2_bbg_20261010T221526Z.cycle.json all 8 failures read {status: error, detail: error}. A detail that repeats the status word is present but carries nothing of its own, so no failure 'carries its own detail'. The defect is the runner's (row D1-S7), not the read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "order AMGT_HARVST.TO-HVST-bw-2 criterion AC3 text (judgment block)",
        "deliverables/0.7.0_AE_CloudOps~ZW/round79/bw2_bbg_cycle.out lines 6-7, 287 and the 8 FAILURE lines",
        "deliverables/0.7.0_AE_CloudOps~ZW/round79/bw2_bbg_20261010T221526Z.cycle.json failures[0..7]"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "HVSTbw2-AC3",
        "instance": "deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bw-2.the-bbg-live-cycle-read-to-its-end.proof_of_spec.json@625de3ec4f",
        "verdict": "FAIL",
        "reason": "Clauses 1 (242 of 242 attempted) and 2 (no stop) hold; clause 3 fails: 8 of 8 failure details equal the status word 'error', so none carries its own detail (row D1-S7)."
      }
    ]
  },
  {
    "id": "AMGT_HARVST-D1-C-S8",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "L9 grade, AMGT_HARVST.TO-HVST-bs-1.rebuild11-dry-run-the-list-move AC4 (round 75): PASS, on a zero. The judgment is R28's ten titles per list-moved security. gold_rebuild11.signing.out reads AIG_US_Equity served 16 built 16 gone 0 added 0, OMAB_MM_Equity 5/5/0/0 and OMAB_US_Equity 5/5/0/0, with the LIST FILE equal to build() at HEAD and PUTS SENT 0. REBUILD11_TITLES.md lists no gone and no added pairs, by construction. This seat's run of gold_rebuild11_rule.py: SELFTEST OK (holds on a list-moved loss; negative controls break). The list move moves no pair, so there are no titles to judge, and the zero is what the move should produce: the alias edits add forms the matcher already caught.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 grade, AMGT_HARVST.TO-HVST-bs-1.rebuild11-dry-run-the-list-move AC4 (round 75): PASS, on a zero. The judgment is R28's ten titles per list-moved security. gold_rebuild11.signing.out reads AIG_US_Equity served 16 built 16 gone 0 added 0, OMAB_MM_Equity 5/5/0/0 and OMAB_US_Equity 5/5/0/0, with the LIST FILE equal to build() at HEAD and PUTS SENT 0. REBUILD11_TITLES.md lists no gone and no added pairs, by construction. This seat's run of gold_rebuild11_rule.py: SELFTEST OK (holds on a list-moved loss; negative controls break). The list move moves no pair, so there are no titles to judge, and the zero is what the move should produce: the alias edits add forms the matcher already caught.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_AMGT_HARVST~129/gold_rebuild11.signing.out",
        "deliverables/0.9.0_WK_AMGT_HARVST~129/REBUILD11_TITLES.md",
        "3.0.0_SA_CVO ran gold_rebuild11_rule.py: SELFTEST OK"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "HVSTbs1-AC4",
        "instance": "deliverables/0.9.0_WK_AMGT_HARVST~129/AMGT_HARVST.TO-HVST-bs-1.rebuild11-dry-run-the-list-move.proof_of_spec.json@2ba8e449f5",
        "verdict": "PASS",
        "reason": "No pair moves on any of the three list-moved securities (16/16, 5/5, 5/5, gone 0 added 0); there are no titles to judge, and a zero is the right result of an alias edit the matcher already covered."
      }
    ]
  },
  {
    "id": "AMGT_HARVST-D1-C-S9",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "L9 grade, AMGT_HARVST.TO-HVST-bs-4.the-r47-seeking-alpha-backfill-resumed AC3 (round 75): PASS. Clause 1, resumed from its checkpoint: the second relaunch (2026-10-11T04:01:39Z, declared dj-20261011T040137Z-1679536) ran pairs_run_this_session 107 = 242 - 135 already done; the first resume read 'Checkpoint done=133'; neither started from 0. Clause 2, a completion and not a stop: the run's own terminal fields read stopped null, interrupted false, never_started 0, collected 237 + retry 4 + gave_up 1 = 242, the checkpoint stopped map {}, and JOB-EXIT rc 0. The 4 retries are contract_unavailable at retry 1 of 3, recorded with a status. Read from the site-Z records on box/dell1, not re-run (a site-Z process).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 grade, AMGT_HARVST.TO-HVST-bs-4.the-r47-seeking-alpha-backfill-resumed AC3 (round 75): PASS. Clause 1, resumed from its checkpoint: the second relaunch (2026-10-11T04:01:39Z, declared dj-20261011T040137Z-1679536) ran pairs_run_this_session 107 = 242 - 135 already done; the first resume read 'Checkpoint done=133'; neither started from 0. Clause 2, a completion and not a stop: the run's own terminal fields read stopped null, interrupted false, never_started 0, collected 237 + retry 4 + gave_up 1 = 242, the checkpoint stopped map {}, and JOB-EXIT rc 0. The 4 retries are contract_unavailable at retry 1 of 3, recorded with a status. Read from the site-Z records on box/dell1, not re-run (a site-Z process).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~ZW/r47/bs4_resumed.out, bs4_resumed_2.out, bs4_completed.out (terminal fields verbatim)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "HVSTbs4-AC3",
        "instance": "deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bs-4.the-r47-seeking-alpha-backfill-resumed.proof_of_spec.json@11270dbfe6",
        "verdict": "PASS",
        "reason": "Resumed from the checkpoint (107 pairs run this session = 242 - 135), and completed without a stop (stopped null, never_started 0, rc 0)."
      }
    ]
  },
  {
    "id": "AMGT_HARVST-D1-C-S10",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "L9 grade, AMGT_HARVST.TO-HVST-bs-5.rebuild12-dry-run-r30-served AC4 (round 75): PASS. REBUILD12_REMOVED_SAMPLE.md (30 of 285 R30 removals, every 9th by security and article key): each is a lower-case common-word hit on a company alias in an unrelated story ('booking', 'cadence', 'monster', 'orange', 'visas', 'apple', 'global payments'), which R30 rightly drops. The 22 count-down rows read from gold_rebuild12.signing.json outside_rows (of 113) are kept pairs whose mention_count falls but not to 0 (Visa 8->3 and 4->1; Booking 3->1; Orange 5->1; Monster 5->1): the capitalised company mention stays and the lower-case ones go. That is the 'R30-partial count-down' class the CTO admitted (ADDENDUM 2, msg 2181). Lost 0, added 0, daily OTHER 0. AC2 and AC3 read FAIL in the instance as results (OUTSIDE R30 CLASS 113), resolved by that ruling, not by this grade.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 grade, AMGT_HARVST.TO-HVST-bs-5.rebuild12-dry-run-r30-served AC4 (round 75): PASS. REBUILD12_REMOVED_SAMPLE.md (30 of 285 R30 removals, every 9th by security and article key): each is a lower-case common-word hit on a company alias in an unrelated story ('booking', 'cadence', 'monster', 'orange', 'visas', 'apple', 'global payments'), which R30 rightly drops. The 22 count-down rows read from gold_rebuild12.signing.json outside_rows (of 113) are kept pairs whose mention_count falls but not to 0 (Visa 8->3 and 4->1; Booking 3->1; Orange 5->1; Monster 5->1): the capitalised company mention stays and the lower-case ones go. That is the 'R30-partial count-down' class the CTO admitted (ADDENDUM 2, msg 2181). Lost 0, added 0, daily OTHER 0. AC2 and AC3 read FAIL in the instance as results (OUTSIDE R30 CLASS 113), resolved by that ruling, not by this grade.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_AMGT_HARVST~131/REBUILD12_REMOVED_SAMPLE.md (30 rows read)",
        "deliverables/0.9.0_WK_AMGT_HARVST~131/gold_rebuild12.signing.json outside_rows[0..21]",
        "1.0.0_SA_CTO~DELL1 ADDENDUM 2 (msg 2181): R30-partial count-down admitted as a second class"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "HVSTbs5-AC4",
        "instance": "deliverables/0.9.0_WK_AMGT_HARVST~131/AMGT_HARVST.TO-HVST-bs-5.rebuild12-dry-run-r30-served.proof_of_spec.json@4bdcef8666",
        "verdict": "PASS",
        "reason": "The sampled removals are lower-case common-word false hits; the count-downs keep the capitalised company mention and drop the lower-case ones, the class the CTO admitted."
      }
    ]
  },
  {
    "id": "AMGT_HARVST-D1-C-S11",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "Z-S112 dismissed and bs-3 not graded: AMGT_HARVST.TO-HVST-bs-3.the-runner-activated-on-bbg-wsj-barrons reads cancelled at HEAD, by ledger/CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md section 2 (carried once bs-4 completes; a round-80 successor waits on Andrew's vendor sign-in). Its AC3 is unmet and not claimed; a cancelled order is outside the round's verdict.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-Z-S112"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Z-S112 dismissed and bs-3 not graded: AMGT_HARVST.TO-HVST-bs-3.the-runner-activated-on-bbg-wsj-barrons reads cancelled at HEAD, by ledger/CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md section 2 (carried once bs-4 completes; a round-80 successor waits on Andrew's vendor sign-in). Its AC3 is unmet and not claimed; a cancelled order is outside the round's verdict.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ledger/CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md s.2",
        "order bs-3 <status>cancelled</status> at HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S112 dismissed and bs-3 not graded: AMGT_HARVST.TO-HVST-bs-3.the-runner-activated-on-bbg-wsj-barrons reads cancelled at HEAD, by ledger/CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md section 2 (carried once bs-4 completes; a round-80 successor waits on Andrew's vendor sign-in). Its AC3 is unmet and not claimed; a cancelled order is outside the round's verdict."
  },
  {
    "id": "AMGT_HARVST-D1-C-S12",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "D1-S5 dismissed: bw-2 AMENDMENT 1's process-tree read answers it. RUNNERS 1, PID 21512 at both reads, and PID 37816 (the old pin) absent at both, so there is one runner, not two.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S5 dismissed: bw-2 AMENDMENT 1's process-tree read answers it. RUNNERS 1, PID 21512 at both reads, and PID 37816 (the old pin) absent at both, so there is one runner, not two.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_HARVST-D1-S5",
        "deliverables/0.7.0_AE_CloudOps~ZW/round79/bw2_bbg_cycle.out PROCESS TREE / RUNNERS 1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S5 dismissed: bw-2 AMENDMENT 1's process-tree read answers it. RUNNERS 1, PID 21512 at both reads, and PID 37816 (the old pin) absent at both, so there is one runner, not two."
  },
  {
    "id": "AMGT_HARVST-D1-C-S13",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "D1-S6 dismissed: the quiet runner it measured at 20:37Z on 10-09 is explained by Z-S111 (its worktrees force-removed at 22:01Z) and superseded by the re-pinned runner's completed cycle 20261010T221526Z (242 of 242 attempted).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S6 dismissed: the quiet runner it measured at 20:37Z on 10-09 is explained by Z-S111 (its worktrees force-removed at 22:01Z) and superseded by the re-pinned runner's completed cycle 20261010T221526Z (242 of 242 attempted).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_HARVST-D1-S6, AMGT_HARVST-Z-S111",
        "bw2_bbg_cycle.out line 6"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S6 dismissed: the quiet runner it measured at 20:37Z on 10-09 is explained by Z-S111 (its worktrees force-removed at 22:01Z) and superseded by the re-pinned runner's completed cycle 20261010T221526Z (242 of 242 attempted)."
  },
  {
    "id": "AMGT_HARVST-D1-C-S14",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "D1-S7 graduated INERT to REMEDIATION_v14 (owner 2.0.0_SA_COO~W1): it is the cause of bw-2 AC3's FAIL (C-S7).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S7 graduated INERT to REMEDIATION_v14 (owner 2.0.0_SA_COO~W1): it is the cause of bw-2 AC3's FAIL (C-S7).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_HARVST-D1-S7",
        "row AMGT_HARVST-D1-C-S7"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v14.md."
  },
  {
    "id": "AMGT_HARVST-D1-C-S15",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "Z-S110 graduated INERT to REMEDIATION_v14 (owner 2.0.0_SA_COO~W1): the live runner's --stop-file points into the b5a7a3a4b6 code worktree while its --state-dir and --runtime-root sit under the c1be67f53c pin (bw2 process tree, PID 21512).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-Z-S110"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Z-S110 graduated INERT to REMEDIATION_v14 (owner 2.0.0_SA_COO~W1): the live runner's --stop-file points into the b5a7a3a4b6 code worktree while its --state-dir and --runtime-root sit under the c1be67f53c pin (bw2 process tree, PID 21512).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_HARVST-Z-S110",
        "bw2_bbg_cycle.out PID 21512 command line"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v14.md."
  },
  {
    "id": "AMGT_HARVST-D1-C-S16",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "Z-S111 graduated ARMED to REMEDIATION_v14 (owner and disarm owner 0.0.0_AB_MSTR~Z): worktree GC judges idleness by git activity only and force-removed two worktrees a live scheduled runner executed from. This seat finds no protection for the pin worktrees in .tools (comp-find 'harvest-runner-pin|wk-harvest-runner' 0 hits over 515 files), so the next /govern GC pass can repeat it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-Z-S111"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Z-S111 graduated ARMED to REMEDIATION_v14 (owner and disarm owner 0.0.0_AB_MSTR~Z): worktree GC judges idleness by git activity only and force-removed two worktrees a live scheduled runner executed from. This seat finds no protection for the pin worktrees in .tools (comp-find 'harvest-runner-pin|wk-harvest-runner' 0 hits over 515 files), so the next /govern GC pass can repeat it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_HARVST-Z-S111",
        "3.0.0_SA_CVO comp-find over .tools: 0 hits / 515 files"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v14.md."
  },
  {
    "id": "AMGT_HARVST-D1-C-S17",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T13:10:00Z",
    "one_line": "Z-S113 graduated INERT to REMEDIATION_v14 (owner 2.0.0_SA_COO~W1): the backfill driver labels a local launch failure (rc 0xC0000142) transport-class and retries it; carried to round 80 by the bs-4 record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-Z-S113"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Z-S113 graduated INERT to REMEDIATION_v14 (owner 2.0.0_SA_COO~W1): the backfill driver labels a local launch failure (rc 0xC0000142) transport-class and retries it; carried to round 80 by the bs-4 record.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_HARVST-Z-S113",
        "order bs-4 COMPLETE record, 'Carried, round 80'"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v14.md."
  }
]
```
