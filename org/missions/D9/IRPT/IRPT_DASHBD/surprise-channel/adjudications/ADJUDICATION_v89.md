# IRPT_DASHBD: CVO adjudication, round 125 (workstream B-49F, ~D2)

<sweep_watermark>2026-10-15T12:01Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T12:01Z, on msg 8258 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND125_B49F_DRAIN_END_20261015.md` @90b7f8b23a, blob a12c9bfeb1). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Three orders (DB-b-254..256), LOCAL repo edits and read-only probes. No judgment criterion. The orders declare six criteria. Re-run here on the landed tree: 6 of 6 PASS (rc 0). The struck DB118-3-AC3 still FAILS (rc 1), unmet. Three proof instances VALID; `round-close-check --round 125 --workstream B-49F` MAY-CLOSE (3 orders). Round 124 (TO-DB-b-253, the hop-1 apply) is not graded here. One row HELD ARMED (W209-S3, owner the CTO). No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S26",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T12:01:00Z",
  "one_line": "Round 125 B-49F (~D2): the Cottonwood write guard and start floor (DB-b-254), the Cottonwood function memory from a measurement (DB-b-255: peak 654 MB, 1024 MB chosen), and the dim_return_method claims read (DB-b-256). 6 of 6 PASS re-run. Struck DB118-3-AC3: still unmet. DISCLOSURE 1, the transaction keying error (reads keyed without tran_srcde, so the 04-21 event read as in-kind receipts and not as a 6-for-1 VUG split): it affected three READ records and their verdicts: RD_QTY_CHANGE_0421_R121 (DB-b-244, IC|RO read as in-kind), RD_CONVERSION_READ_R122 (DB-b-248, CONVERSION_LEG_ABSENT) and RD_INKIND_FLOW_READ_R123 (DB-b-251, IN_KIND_RECONCILES 913 of 920). It also affected the checkers that recount them on the same keying, the CTO analyses of rounds 122-124, and this seat's v87 and v88 rows, whose 04-21 readings are superseded by the CTO and CRO split ruling. NO LANDED OUTPUT is built on the wrong key: a repo-wide search for CONVERSION_LEG_ABSENT, IN_KIND_RECONCILES and SPLIT_UNADJUSTED_COMPARISON finds 25 files, none under data/, infra/, lib/ or org/standards/. All are records, checkers, analyses, decompositions, drive logs or adjudications. No producer, contract, guard or served flag adopted the reason. The split adjustment is ~P2's (IRPT_BCKEND IB-pr-572) under its own pair. DISCLOSURE 2, the moving-newest-day checker defect (repair @2cdacfd136): negative controls run here on the repaired p125_cotmem.check_record, with the real listed partitions (145, newest 2026-10-14) and the landed record. The record as landed PASSES. A second day not listed (2026-10-31) FAILS. A second day before the first FAILS. A held day FAILS. A chosen memory of 512 FAILS ('recomputed 1024'). The repair can still fail. The issuer also discloses that DB122-1-AC1 now fails on the landed tree (its record says 3008 MB, lambda.tf 8192): a criterion superseded by DB123-1 and not edited. DISCLOSURE 3, round 124: THE HOP-1 APPLY HAPPENED. At 2026-10-15T11:59:21Z the live irpt-49f-reporting-gold-lambda reads LastModified 2026-10-15T11:49:38Z, CodeSha256 jz6fRzL5..., MemorySize 8192, where v88 read 2026-10-13, J6M/92Mh... and 3008. Its inline policy now holds 11 sids, adding ReadTheServedModelSeriesObjectOnly, ListExactlyTheHouseholdCrosswalkPrefix, ReadTheHouseholdCrosswalkOnly and InvokeOwnFunctionOnly. The apply's commits (29d9e71933 ledger open .. e9f08ad76f complete, author 0.7.0_AE_CloudOps~DB2) sit on the AE worktree branch C:/dev/wk-irpt-dashbd-db2-b253, where the ledger irpt-dashbd-hop1-filled-report-values-20261015.json is OPEN (read across 26 worktrees). On box/dell2 the order still reads pending and no packet has come. Round 125 does NOT depend on it: its three orders touch the Cottonwood adapter and handler and read the method row. DB-b-256's 'reporting-gold write list lacks dim_return_method' still holds after the apply, since the four new sids add no method prefix. Rows: D2-S79 (BLOCKING, ARMED, owner ~D2; filed after v88 named the hazard) is DISARMED by D2-S81, grounded: DB125-1-AC1 and AC2 PASS here (write_day LISTs the exact day and refuses with no put, including a 2026-06-22 history day; owed_days floors at 2026-07-10 and refuses earlier events). D2-W207-S1 (BLOCKING, ARMED, owner ~D2; the floor contradicted one pinned handler example) is resolved by the owner's Amendment 1 @1bec1bfc83 (the one example changed, 16 of 16 pass), recorded in W207-S3 with no owner-filed disarm row. D2-W209-S3 (ARMED, owner 1.0.0_SA_CTO~DELL2; no scheduled writer of the claim columns) is HELD for the CTO's A/B/C choice. W207-S2, W208-S1, S2, W209-S1, S2 and D2-S80 (the AE seat's odd finds) are INERT.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S79",
   "IRPT_DASHBD-D2-S81",
   "IRPT_DASHBD-D2-W207-S1",
   "IRPT_DASHBD-D2-W207-S2",
   "IRPT_DASHBD-D2-W207-S3",
   "IRPT_DASHBD-D2-W208-S1",
   "IRPT_DASHBD-D2-W208-S2",
   "IRPT_DASHBD-D2-W209-S1",
   "IRPT_DASHBD-D2-W209-S2",
   "IRPT_DASHBD-D2-S80"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned or held with a live owner before the slug; a repaired checker must still fail a known-bad input; no landed output may rest on a withdrawn method.",
  "world_is": "Three orders complete (merges 4200e3415b, a59a25fefd, 68a4438870); nothing written to AWS by them. The Cottonwood overwrite and stall hazard is closed in code; the root is unapplied and the schedule DISABLED. Hop 1 is LIVE in its function as of 11:49:38Z (code, 8192 MB, four new grants). Its proof is the next scheduled fire, and its ledger is open on the AE branch, not yet drained to box/dell2. The 04-21 event is a stock split per the CTO and CRO; the earlier in-kind readings are withdrawn and nothing served used them. The packet is stale on D2-W195-S1 (disarmed by D2-S71, v85). FWD-2, FWD-11 and FWD-21 are not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T12:0xZ: DB125-1-AC1..AC3, DB125-2-AC1, AC2, DB125-3-AC1 PASS rc 0; DB118-3-AC3 FAIL rc 1",
    "negative controls on p125_cotmem.check_record (scratchpad negctl_p125.py): landed record PASS; unlisted day, pre-floor day, held day and memory 512 each FAIL",
    "Grep of the workspace for CONVERSION_LEG_ABSENT|IN_KIND_RECONCILES|SPLIT_UNADJUSTED_COMPARISON: 25 files, none under data/, infra/, lib/, org/standards/",
    "aws lambda get-function-configuration irpt-49f-reporting-gold-lambda at 2026-10-15T11:59:21Z: LastModified 2026-10-15T11:49:38Z, CodeSha256 jz6fRzL52EaI..., MemorySize 8192; aws iam get-role-policy: 11 sids",
    "git log --all --author 0.7.0_AE_CloudOps~DB2: 29d9e71933 .. e9f08ad76f; open ledger on C:/dev/wk-irpt-dashbd-db2-b253 (26 worktrees read); TO-DB-b-253 <status>pending on box/dell2",
    "proof-of-spec-check VALID rc 0 on ~207, ~208, ~209; round-close-check --round 125 --workstream B-49F verdict=MAY-CLOSE orders=3",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_ICRO_VUG_STOCK_SPLIT_NONFLOW_SPLIT_ADJUST_HOLDINGS_RETURN_20261015.md",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND125_B49F_DRAIN_END_20261015.md blob a12c9bfeb1 (msg 8258)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two ARMED rows resolved by their owner's code and amendment, re-graded green here, and inert observations. W209-S3 stays ARMED with the CTO. The withdrawn in-kind readings touched no landed output."
 }
]
```
