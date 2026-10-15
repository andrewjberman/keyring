# IRPT_DASHBD: CVO adjudication, round 130 (workstream B-49F, ~D2): Act 3 of the Cottonwood landing

<sweep_watermark>2026-10-15T17:40Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:40Z, on msg 8480 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND130_132_131_B49F_DRAIN_END_20261015.md` @27847c126a, blob 1e264c2eb8; rounds 131 and 132 are ADJUDICATION_v97 and v98). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md`, against the CTO's round-128 analysis (msg 8463, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_128_20261015.md` @cbd0289ecd; at HEAD it carries ADDENDUM 1 with an erratum and the schedule-enable ruling). One order, TO-DB-b-262 (WORLD; applier 0.7.0_AE_CloudOps~DB2; merged @691b95c160) under the landing pair revision 3. No judgment criterion. Re-run here on the landed tree, with fresh live reads: DBD129-1-AC1 and DBD129-2-AC1, 2 of 2 PASS (rc 0). Proof VALID; `round-close-check --round 130 --workstream B-49F` MAY-CLOSE. The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S33",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:40:00Z",
  "one_line": "Round 130 B-49F: Act 3, the Cottonwood catch-up. 2 of 2 PASS re-run. WRITE SET, from this seat's LIST at 17:24:27Z (6,780 objects, 3,390 partitions). History: 3,325 partitions, newest LastModified 2026-10-11T07:17:06Z, unmodified. Act 2: 2026-07-10, still its two objects (ETag 0f65e010..., 15:32:54Z, unchanged since v94). Act 3: 64 new days, 2026-07-13 to 2026-10-14, written 16:05:18Z to 17:07:53Z. Every new day holds exactly data.parquet and manifest.json; every one is a trading day by lib/trading_calendar.py; no non-date key. The only trading days in 2026-07-10..2026-10-14 without a partition are 2026-08-19, 2026-09-24 and 2026-09-25. This seat confirmed each has a fact_allocations partition but NO fact_transactions partition, with controls 08-18 and 08-20 holding both. So 65 = 1 + 64 is the count of silver-paired trading days. Every write is a dated partition of the one granted prefix: inside revision 3's blast radius. TIMING, from the log group's 17 REPORT lines (no page token): Act 2 118.0 s at 633 MB; the 16 Act 3 events 436.3, 394.9, 358.3, 325.4, 305.8, 281.0, 251.5, 231.8, 215.8, 199.9, 164.7, 134.9, 119.4, 105.3, 77.2 and 40.9 s, all at 627 MB. Maximum 436.3 s against the order's 700 s stop and the 900 s timeout; 0 over 700 s; 0 'Task timed out', ERROR, Traceback or OutOfMemory lines. The cost per event FALLS steadily as the days approach the frontier (436 s to 41 s for four days each). So '4 days x 118 s' does not model it: the work grows with the silver behind each day, not per day. A one-day scheduled fire at the frontier should be far below 118 s; that is inferred, not measured. LEDGER irpt-dashbd-cottonwood-account-return-daily-20261015: CLOSED on box/dell2 at 20261015T171630Z, all five legs proven, L5 at 17:16:09Z. Of 35 live worktrees read, 7 still carry the open marker on their HEAD: scratch-IB589-428/pin, wk-aq2-fwd1b, wk-irpt-anlreq-179, wk-irpt-anlreq-180, wk-irpt-dashbd-216, db2-b260 and db2-b262. These are branch snapshots taken before the close (b262's HEAD is already merged into box/dell2); measured against the world, the deploy is done, so they are stale copies, not open deploys. SCHEDULE: irpt-cot-account-return-daily-daily reads DISABLED at 17:24:27Z (modified 2026-10-15T15:23:53Z, the apply). The CTO's ADDENDUM 1 rules the enable as its own act; it has not happened. Function unchanged (LastModified 15:23:47Z, CodeSha256 fQFe4moI..., 1024 MB). Row held for the CTO: D2-S92 (ARMED, owner ~D2; the prefix now holds a Commonwealth era to 06-22 and a Black Diamond era from 07-10 with different method_version and manifest shape, and a consumer that chains across them serves a spliced return).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S89"
  ],
  "spec_asserts": "CLAUDE.md never-widen and NEVER-2: the act stays inside the signed blast radius; the ledger closes at completion, read across every live worktree with the denominator printed; a timeout is a STOP; the trading calendar decides the expected day count.",
  "world_is": "Cottonwood account_return_daily now holds the Black Diamond era from 2026-07-10 to 2026-10-14 (65 days) beside the untouched Commonwealth history. Three silver-unpaired trading days are absent. The landing function is idle with its schedule DISABLED, and the ledger is closed. FWD-11 and FWD-21 wait on the schedule-enable act and its first fire read.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:2xZ: DBD129-1-AC1, DBD129-2-AC1 PASS rc 0; DB118-3-AC3 FAIL rc 1; proof-of-spec-check VALID rc 0 (0.7.0_AE_CloudOps~DB2 instance); round-close-check --round 130 verdict=MAY-CLOSE",
    "aws s3api list-objects-v2 opal-data-cottonwood irpt/cottonwood/gold/account_return_daily/ at 17:24:27Z: 6780 objects, 3390 partitions; lib/trading_calendar.py is_trading_day over every new day",
    "aws s3api list-objects-v2 opal-data-assets blackdiamond/cottonwood/silver/fact_transactions/date=2026-08-19, 2026-09-24, 2026-09-25: 0 objects; fact_allocations: 1 each; controls 2026-08-18, 2026-08-20: 1 and 1",
    "aws logs filter-log-events /aws/lambda/irpt-cot-account-return-daily-lambda REPORT: 17 lines, max 436.3 s, max 633 MB; error-pattern filter: 0 events",
    "org/critical_paths/change_management/20261015T1321Z_irpt-dashbd-cottonwood-account-return-daily-20261015_deploy_completion.md: Status CLOSED 20261015T171630Z; .open_deploys marker on 7 of 35 worktree HEADs, none on box/dell2",
    "aws scheduler get-schedule irpt-cot-account-return-daily-daily at 17:24:27Z: DISABLED; aws lambda get-function-configuration: LastModified 2026-10-15T15:23:47Z",
    "investigation rows D2-S89, D2-S92",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND130_132_131_B49F_DRAIN_END_20261015.md blob 1e264c2eb8 (msg 8480)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Act 3 is verified live inside the signed blast radius, with no timeout and its ledger closed. The applier's earlier observation row is inert. D2-S92 stays ARMED with its owner for the CTO."
 }
]
```
