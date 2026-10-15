# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PO, the Orion Inflection raw feed)

<sweep_watermark>2026-10-15T03:57Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T03:57Z, on msg 8015 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PO_DRAIN_END_20261015.md` @136f730225; the file is untracked in the shared tree and was read at its pin). One order, IB-pr-552 (READ of the Orion raw producer, the dropped days, the re-pull cost and the 6 AM fold), complete, merged @62d5757800, issued on the CTO's msg 7980. No judgment criterion; nothing pulled, written to AWS, signed or invoked; no Orion request. Re-run here on the landed tree: IB199-4-AC1..AC3 PASS. `round-close-check --round 1 --workstream "~PO"`: verdict=MAY-CLOSE. 8 rows dismissed below. One thing the packet's summary line does not carry and the CTO should weigh before cutting the re-pull pair: row D2-W396-S4 measures trading days with NO key in EITHER format for transactions (7, among them 2026-07-01 and 2026-09-28) and performance (22); the re-pull is costed for parquet-only positions days only, so it does not close the two known gap days for transactions or performance, and no artifact read says why the producers wrote nothing on those 29 feed-days. HELD, carried and owned: D2-W394-S2 and D2-S180 (ARMED, owner `~P2`, from the IB-pr-550 read), D2-W392-S2, W349-S1, W361-S1, W348-S2, W368-S2 (owner `~P2`), D2-S158 (owner the CTO).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S9",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T03:57:00Z",
  "one_line": "Round 1 ~PO. The flat .jsonl.gz positions key the mirror needs is written only by a manual CLI pull (data/inf/manual_api/pull_inflection_positions_daily.py:445, --upload-bronze, no schedule); the deployed inf-api-positions lambda writes parquet only. 7 positions days landed parquet-only and were dropped by the mirror by design (ruling 16), so the defect is the unscheduled raw producer, not the mirror. Positions re-pull: 7 days, 2,240 requests, about 19 minutes at the 2 req/s floor (inferred from the limiter). Fold: one 06:00 America/New_York scheduler schedule on the trading-day frontier, names from opal_naming. IB199-4-AC1..AC3 PASS re-run. Dismissed (8): D2-W396-S1..S7 (writer location, an unscheduled key write, the mirror header's stop account, source-absent transactions/performance days, a stale limiter docstring, stale clock text, a 2,259-object bulk write date; all INERT readings) and D2-S182 (the issuer's dispositions). W396-S4 is dismissed as a row but carried into world_is for the CTO: transactions 7 and performance 22 trading days have no key in either format, cause unread.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W396-S1",
   "IRPT_BCKEND-D2-W396-S2",
   "IRPT_BCKEND-D2-W396-S3",
   "IRPT_BCKEND-D2-W396-S4",
   "IRPT_BCKEND-D2-W396-S5",
   "IRPT_BCKEND-D2-W396-S6",
   "IRPT_BCKEND-D2-W396-S7",
   "IRPT_BCKEND-D2-S182"
  ],
  "spec_asserts": "CTO msg 7980: locate the raw producer, read which days landed parquet-only and were dropped, cost the re-pull PER FEED, and fold the producer into the 6 AM ET schedule. Spine L9/L10: every BLOCKING or ARMED row dispositioned before the slug.",
  "world_is": "Answered for positions. Per feed, the re-pull cost covers parquet-only days only: transactions (7 trading days, including 2026-07-01 and 2026-09-28) and performance (22) have no object in either format between May and 2026-10-14, so a positions-only re-pull leaves the two known gap days absent in those two feeds, and the cause of those 29 feed-days is not read. The two next pairs (the 7-day positions re-pull; the scheduled producer in the fold) are not cut and wait on the CTO's word on shape. ~I2's round-116 feed is not yet written.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T03:5xZ of org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py: IB199-4-AC1..3 PASS",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 1 --workstream ~PO: orders=1 judgment=0 verdict=MAY-CLOSE",
    "investigation row D2-W396-S4 world_is: transactions 7 trading days with no key in either format 2026-05-12..2026-10-14 (07-01, 07-13, 07-14, 07-15, 08-06, 09-28, 09-29); performance 22 in 2026-05-03..2026-10-14",
    "investigation rows D2-W396-S1..S7, D2-S182, D2-W394-S2, D2-S180",
    "git show 136f730225:org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PO_DRAIN_END_20261015.md (msg 8015)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Seven INERT readings and the disposition record. The source-absent transactions/performance days are carried to the CTO in world_is, not as an armed hazard: nothing is served or moved by this READ."
 }
]
```
