# IRPT_BCKEND: CVO adjudication, round 191 (workstream ~P)

<sweep_watermark>2026-10-14T05:29:59Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-14T05:29:59Z, on msg 7548 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_191_P_DRAIN_END_20261014.md`). One order, 3 of 3 PASS, no judgment
criterion; nothing applied. 5 rows dismissed below; nothing graduates while IB-pr-497 is parked. For the CTO half: the release must state
each firm's published business date (select_business_date() returned 2026-10-14 pre-session; this seat saw the same from the calendar), and
49financial's 2026-10-08 gap is named, not hidden.

```json
[
 {
  "id": "IRPT_BCKEND-C-S375",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T05:29:59Z",
  "one_line": "Round 191 (~P), no judgment criterion. Dismissed: D2-S164 (the cause of 49financial's failed 2026-10-09 fire: the SSM command timed out and was killed, exit 137); D2-W379-S1 and -S2 (the canonical/fallback split read by building twice over the same inputs; Cottonwood's fallback 211 at the newer candidate against 215 at the older); D2-W379-S3 (select_business_date() returned 2026-10-14 pre-session while the candidates carry 2026-10-12: this seat saw the same forward date from trading_calendar at 02:27Z, so the release's re-measure must state which business date each firm's mint publishes, and a fire before the session must not stamp the current day); D2-S166. HELD with their owners: D2-S158 (ARMED, the CTO, until the release's after-read) and D2-W374-S1 (ARMED, the box manager). Stay open with the issuer: D2-S165 (49financial's served series has a gap at 2026-10-08; a one-date backfill is a separate act), D2-S152, D2-S155, D2-S156, D2-S145 to -S147, D2-S150, D2-S153.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S164",
   "IRPT_BCKEND-D2-W379-S1",
   "IRPT_BCKEND-D2-W379-S2",
   "IRPT_BCKEND-D2-W379-S3",
   "IRPT_BCKEND-D2-S166"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "The one release's movers are counted per firm by the producer's own rules: cash rule 32 (49F), 38 + 211 (COT), 774 + 67 (INF); Cottonwood's refused candidate publishes with its one lost account listed. The COO half is SIGNED with seven conditions; the CTO half is UNSIGNED; the apply is round 192. The counting harness was scratch and is deleted, so the release re-runs the method. Nothing applied. IB-pr-497 parked; IB-pr-456 waits on Andrew's PROD execution ID.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S164, D2-W379-S1, D2-W379-S2, D2-W379-S3, D2-S166",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_191_P_DRAIN_END_20261014.md (msg 7548)",
    "TO-IB-pr-532 complete (order file read); merge a33cb9b030 on HEAD. This seat's own read at 2026-10-14T02:27Z: lib/trading_calendar expected_last_trading_day(now) returned 2026-10-14 while it was 2026-10-13 in New York, the same pre-session forward date W379-S3 records for select_business_date()"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A cause read, the movers' measured split, and a date-selection reading carried as a release condition."
 }
]
```
