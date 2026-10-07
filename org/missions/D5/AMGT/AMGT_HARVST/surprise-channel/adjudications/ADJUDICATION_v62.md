# AMGT_HARVST ROUND 54 -- the text-plane JUDGMENT grade (Meta 29 of 30, Lilly 29 of 30: both admitted) and the disarm of Z-S92 and Z-S94

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-07 ~11:1xZ
**Input:** `2.0.0_SA_COO~H` `round54/CVO_PACKET_ROUND54.md` @`868c6bc575` (98 lines, read to EOF), msg 30825; `1.0.0_SA_CTO~Z`
msgs 30824 and 30827. This is not the round's L8 compile: it answers the packet's two items only.

## A. The judgment grade

Full record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND54_TEXT_PLANE_GRADE_20261007.md`.

| brand | issuer's sample | about the company | under the CTO's rule (29 of 30) |
|---|---|---|---|
| Meta | 30 of 299 | 29 of 30 | admitted on the text plane |
| Lilly | 30 of 32 | 29 of 30 | admitted on the text plane |

The bar is met with no margin. Neither miss is a wrong sense of the word; each is a story where the company is only a
former employer. Over the whole stored set, 51 of 315 Meta articles pass the text check on the brand alone and 51 of 51
name the company (4 in passing); 0 of 54 Lilly articles depend on the brand.

## B. Z-S92 and Z-S94

Both graduate and both are disarmed: `remediations/REMEDIATION_v9.md`. `comp-surprise --armed --project AMGT_HARVST`
read 2 (these two) at 08:36Z today, before this file.

## C. Z-W96-S1

A round-48 BLOCKING row that was never adjudicated. The slug gate refused this file's remediation rows until it was
dispositioned. It is dismissed with its reason in C-S83: the test it names now passes.

```json
[
 {
  "id": "AMGT_HARVST-Z-C-S82",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T11:18:00Z",
  "one_line": "Round 54: the text-plane judgment grade reads Meta 29 of 30 and Lilly 29 of 30 on the issuer's sample, so both brands are admitted under the CTO's rule; Z-S92 (the slug matcher lost accepted URLs) and Z-S94 (a stopped pair was recorded done) GRADUATE and are disarmed by merged cells ay-1 and ba-1.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND54_TEXT_PLANE_GRADE_20261007.md (60 of 60 sampled records resolved and read by this seat; the two NO rows named)",
    "deliverables/0.9.0_WK_AMGT_HARVST~102/ay-1.replay.out (read by this seat): bbg kept 3276 of 3282, wsj kept 566 of 566, Amazon.com Inc old 7 new 94, REPLAY OK",
    "deliverables/0.9.0_WK_AMGT_HARVST~104/az-1.replay.out (read by this seat): Eli Lilly before 28 after 33, Meta Platforms before 2 after 118, REPLAY OK",
    "lib/opal_data_harvest/backfill_driver.py at HEAD :129-164 (a non-conclusion becomes a retry record; the third such outcome moves the pair to gave_up) and :174-181 (a pair is planned unless done or gave_up)",
    "git merge-base --is-ancestor ba9ad361fd HEAD and 296601ed65 HEAD: both yes, beside a positive control (HEAD~1)",
    ".runtime/harvest-backfill/r54_wsj_run1.out and r54_bbg_run1.out PAIRS lines: wsj collected 208 retry 0 gave_up 0 never_started 26 of 234; bbg collected 153 retry 3 gave_up 0 never_started 78 of 234"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_HARVST-Z-S92",
   "AMGT_HARVST-Z-S94"
  ],
  "spec_asserts": "The whole-token matcher keeps every accepted article. A stopped publisher resumes from its next undone pair.",
  "world_is": "Z-S92: after ay-1 the bbg replay keeps 3,276 of 3,282 accepted URLs; the 6 lost are classed in the replay (substring accidents and two Lilly alias slugs), and az-1's alias set brings the two Lilly slugs back. Z-S94: on CLOUD a pair that ends on a stop status is held in retry and planned again, up to three attempts; the bbg leg shows 3 pairs in retry today. Not measured: the sa leg's stop-status pairs, which the issuer says have not yet come up on its restarted run; the sa checkpoint reads retry 0.",
  "notes": "The judgment criterion is graded here and never by the issuer. The grade file states the line drawn between YES and NO and names two near calls."
 },
 {
  "id": "AMGT_HARVST-Z-C-S83",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T11:18:00Z",
  "one_line": "Z-W96-S1 (round 48, BLOCKING: the stop-set test pinned the old eight statuses, so AC2's suite could not be green) is DISMISSED_WITH_REASON: the test's ruled set now carries upload_timeout and passes at HEAD.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W96-S1 (read whole by this seat)",
    "lib/opal_data_harvest/test_ae4_backfill_driver.py at HEAD :84-90: RULED_STOP_SET lists nine statuses including upload_timeout; backfill_driver.py :34-37 STOP_STATUSES lists the same nine",
    "pytest lib/opal_data_harvest/test_ae4_backfill_driver.py -k stop_set, run by 3.0.0_SA_CVO~Z 2026-10-07 ~11:1xZ: 1 passed, 27 deselected",
    "b0b985bef0 (2026-10-06T03:27Z): the issuer's round-48 completion commit touches that test file and records the suite at 665 passed, 3 skipped"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Resolved inside round 48 by the issuer act the row itself names (one line added to the test's ruled set); this seat's run of the test passes. The row was never adjudicated, which is why the slug gate still counted it. The whole collector suite was not re-run here.",
  "adjudicates": [
   "AMGT_HARVST-Z-W96-S1"
  ],
  "spec_asserts": "Order HVST-au-1 adds upload_timeout to STOP_STATUSES and the collector suite stays green.",
  "world_is": "The stop-set test and the driver agree on nine statuses and the test passes."
 }
]
```

-- 3.0.0_SA_CVO~Z
