# P0 INGESTION CENSUS -- THE ACCEPTANCE RE-RUN (2026-07-16 ~14:25Z, 1.0.0_SA_CTO)

**Verdict: THE BAR IS MET -- 18/18 channel-layer rows PASS, zero fails.** Same instrument as the
baseline (P0_INGESTION_CENSUS_BASELINE_20260716T0450Z.md); bar = Andrew verbatim ("at least July 14
if not July 15 in every single bronze and silver bucket at parity ... backfill first and incremental
pulls scheduled henceforth").

| channel | layer | max_date | 07-14 | 07-15 | verdict (baseline -> now) |
|---|---|---|---|---|---|
| blackdiamond/49f | bronze+silver | 07-15 | YES | YES | PASS (silver lagged -> caught up WP3) |
| blackdiamond/cottonwood | both | 07-16 | YES | YES | PASS (unchanged) |
| eclipse/inflection | both | **07-16** | holes* | holes* | **PASS (was DEAD at 07-10)** |
| orion/inflection | both | 07-16 | YES | YES | **PASS (was a 5-day hole)** |
| pathfinder + trueshares (ETF) | both | 07-15 | n/a (born 07-15) | YES | PASS (daily 22:00Z live) |
| schwab 0824 + 0833 | both | 07-15 | YES | YES | PASS (T-1 delivery converting in seconds, event-driven) |
| smartx | both | 07-15/16 | YES | YES | PASS (scheduler was ALWAYS live; retry 185->2 fixed) |

*eclipse 07-11..15: 07-11/12 = weekend (Andrew's calendar correction, vendor-stamp-proven); 07-13..15
= documented holes with practical loss ~NIL PROVEN from the vendor's own editedOn fields (model layer
100% static; 21 changed portfolios named, final states held). Manifest @ 074e2530b.

**Schedulers henceforth (the second half of the directive), all live:** eclipse box 13:30Z (FATAL
fixed, full natural cycle proven today) · orion Lambdas 13:17-13:47Z · schwab delivery + guarded
puller (daily, self-verifying) · smartx 13:30Z ET (retry 185->2) · 49F feeders 03:30Z x2 (new,
battery 14/14) · bd49f D1 converter 03:05Z (new, battery 9/9, first fire tomorrow) · cot nightly
02:03Z · ETF 22:00Z (cloud-only; laptop retired). Absence twins armed per producer.

**Named residuals, all owned:** WP4 500-ing smartx feed = producer defect (0.5.0 artifact swap at CTO
gate) -- not an ingestion gap · WP6 ETF laptop-era history (P1, approved shape) · WP7 converter
re-point (PROMOTED: holding cost = one manual bridge/day, L5 next at ~A) · rps staleness backstop
(one-line alarm, routed to 0.7.0's batch, retires with WP7) · ~~PutMetricData grant~~ **CORRECTED-RETRACTED 15:19Z (0.7.0's own re-simulate): the grant EXISTS
(namespace-conditioned, inf-bronze-runner.tf:154); the original simulate omitted --context-entries against a
conditioned statement = 22a false-deny mode (2), re-demonstrated live under 0.7.0's authorship. The empty-metrics
fact STANDS with mechanism UNKNOWN-not-IAM (discriminators queued to next natural box-up)** · 17a monolith
deny gate (parquet-under-bronze; 0.7.0's batch; the inf-tree dual-writer instance dies with the
re-point).

**Lesson set (the wave's own):** trading-calendar-first hole counting · a vendor-capability claim
cites the VENDOR SURFACE · a render-layer claim verifies at the RENDER layer · a grep-pattern
negative is about the pattern · real-bytes-or-stated-holes, never labels · census call sites, not
files · a retracted prohibition is only as dead as its last-surviving copy.
