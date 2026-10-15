# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PJ, the served DELTAs of the ~PH builds, measured)

<sweep_watermark>2026-10-15T15:47Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T15:47Z, on msg 8408 (the combined packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_1_PJ_PK_DRAIN_END_20261015.md` @a245739457; this file grades the ~PJ lane, ADJUDICATION_v122 grades ~PK). Two orders: IB-pr-580 (the exemption alone, risk SERVED) merged @d1ba413cec, and IB-pr-581 (the split alone, risk SERVED) merged @2f69e24932. Both were issued @9b74f17beb and are complete. The merges change records and harness scripts under the worker folders only; no product file. Re-run here at HEAD: IB218-1-AC1..AC3 and IB218-2-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 1 --workstream "~PJ"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**(1) The exemption alone does not unblock 49 Financial: what still refuses it, and who owns the next step.** Record `IB218-1_exemption_delta.json`, firm 49financial, candidate 2026-10-14 against served 2026-10-12. WITHOUT arm: REFUSED on `classified_security_lost` and `account_lost`, 7,664 accounts, 156,074 nodes. WITH arm: REFUSED on the SAME two conditions. It exempts 1 account, but `account_lost` stands for the other lost accounts, so `run_firm` applies no listing and the exemption alone adds 0 nodes. Two conditions refuse 49F: (a) `classified_security_lost`, untouched by the exemption, and (b) the further lost accounts. Neither is counted or classed in this record. Owner: `D2-S203` (ARMED, `2.0.0_SA_COO~P2`) carries it, and the packet names the next act, a READ of the refusal's anatomy (the lost accounts by class and count, and what `classified_security_lost` names). No task order for it exists yet. Cottonwood (served 2026-10-08) already PUBLISHES at HEAD without the exemption (four lost accounts listed as not refused). With it, the four become zero-value listed nodes (17,927 to 17,931, 0 other node changed, 0 USD). The live refusal is the deployed-gate difference (v118, D2-S199), removed by the IB-pr-549 mint.

**(2) How the DELTAs were measured, and that nothing was written.** Method (the record's `method`): a READ-ONLY dry run in one process of the HEAD code over the live pinned inputs (`HoldingsPublication.begin()` read, `VersionedInputs`, one `build_snapshot`, then `served_publication`), with the gate evaluated WITH and WITHOUT the provider on deep copies of the one build. The difference is taken node by node. Counters: aws_writes_made 0, rows_written 0, figures_written 0. The split arm (`IB218-2_split_delta.json`) ran the producer's own read path over 49 Financial's 47 split days. Denominator: **266,455 account-days**. 1,293 hold a split security at t-1, **1,291 change** (0.48 percent), 63 security-days adjusted, 13 ratio-absent. It was determinism-checked by two full runs (diff rc 0). **Served output unmoved, read live here:** the served holdings indexes `irpt/<firm>/platinum/holdings/current/manifest.json` read Cottonwood VersionId lQMhNnIm... (2026-10-09T14:18:11Z, latest_date 2026-10-08) and 49 Financial daFZJt6f... (2026-10-13T14:20:49Z, latest_date 2026-10-12). Both are the versions packet V3 recorded, so neither moved. Inflection's index moved at 2026-10-15T14:18:33Z (latest 2026-10-14). That is the scheduled 14:15Z fire on the live bundle, not these runs, which read 49 Financial and Cottonwood only. Never-widen holds: nothing was written to served output; the two pairs are the next act.

**(3) The 21 failures, by name, against v120's set.** `data/assets/scripts/gold/investor_reporting/tests` was run here at HEAD 5aefc342bf (which contains all four drains) in a clean detached worktree, since removed: 21 failed, 465 passed. The failing ids are IDENTICAL to v120's HEAD set (0 new, 0 gone). `irpt_holdings_performance/tests`: 83 passed, 0 failed.

The 2026-04-21 count: this run's 985 changed account-days equal the READ's 985 holders (v115). The ruling's 920 does not reproduce; D2-W423-S2 (ARMED, `~P2`) carries it. Per v115, the 920 is a graded-set count, a different population, not shown contradicted.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S29",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T15:47:00Z",
  "one_line": "Round 1 ~PJ. The exemption alone leaves 49 Financial REFUSED both ways (classified_security_lost and account_lost for further lost accounts; 1 exempted, 0 nodes added); the next step, an anatomy READ, is carried by D2-S203 (ARMED, ~P2) with no order cut yet. Cottonwood already publishes at HEAD; the exemption adds its 4 listed zero-value nodes, 0 USD. Split alone on 49F: 1,291 of 266,455 account-days change (47 days, 63 adjusted, 13 ratio-absent), determinism-checked. Both measured by a read-only in-process dry run of HEAD over live pinned inputs; served indexes for Cottonwood (lQMhNnIm, 10-08) and 49F (daFZJt6f, 10-12) unchanged, read live. Same 21 failing test ids as v120. 6 of 6 criteria PASS. Dismissed (5): D2-W422-S1, -S2 (BLOCKING; the issuer's AC2 premise, amended and re-run), D2-W422-S3, D2-W423-S1, -S3 (readings). Held: D2-S203, D2-W423-S2 (~P2).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W422-S1",
   "IRPT_BCKEND-D2-W422-S2",
   "IRPT_BCKEND-D2-W422-S3",
   "IRPT_BCKEND-D2-W423-S1",
   "IRPT_BCKEND-D2-W423-S3"
  ],
  "spec_asserts": "CTO msg 8359: each change measured ALONE on the same candidate; never-widen (CLAUDE.md section 5): a DELTA read writes nothing served; a 'same failures' claim is graded by test id.",
  "world_is": "49 Financial stays served at 2026-10-12, refused on two conditions the exemption does not touch; its unblock needs the anatomy READ. Cottonwood publishes at HEAD and is blocked only by the deployed gate until the IB-pr-549 mint. The 49F split moves 1,291 account-days when released. Nothing served moved.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T15:3xZ of the invocations in IB-pr-580 and IB-pr-581: IB218-1-AC1..3, IB218-2-AC1..3 PASS, exit 0 each; round-close-check ~PJ round 1 MAY-CLOSE",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~422/IB218-1_exemption_delta.json: method, 49financial with/without both REFUSED on classified_security_lost and account_lost, exempted_accounts 1, listing_applied false, node_count 156074 both; aws_writes_made 0",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~423/IB218-2_split_delta.json and proof instance: 47 days, 266,455 account-days, 1,291 changed, 1,293 holding, determinism diff rc 0",
    "aws s3api head-object + get-object of irpt/<firm>/platinum/holdings/current/manifest.json 2026-10-15T15:4xZ: cottonwood lQMhNnIm 2026-10-09T14:18:11Z latest 2026-10-08; 49financial daFZJt6f 2026-10-13T14:20:49Z latest 2026-10-12; inflection G0vUKUOQ 2026-10-15T14:18:33Z latest 2026-10-14",
    "pytest at 5aefc342bf (detached worktree): investor_reporting/tests 21 failed, 465 passed; failing ids equal to v120's HEAD set (comm: 0 new, 0 gone); irpt_holdings_performance/tests 83 passed",
    "investigation rows D2-W422-S1..S3, D2-W423-S1..S3, D2-S203",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_1_PJ_PK_DRAIN_END_20261015.md @a245739457 (msg 8408)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two issuer check premises the measurements disproved (amended and re-run) and three readings. 49 Financial's remaining refusal and the 920 count stay held with ~P2."
 }
]
```
