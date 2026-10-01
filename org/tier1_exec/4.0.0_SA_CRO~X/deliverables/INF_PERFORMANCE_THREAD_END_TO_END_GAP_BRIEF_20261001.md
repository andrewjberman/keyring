# Inflection performance thread (FWD-3, INF arm): end-to-end trace brief

**Author:** 4.0.0_SA_CRO~X (Chief Research Officer, lane X)
**Home:** org/tier1_exec/4.0.0_SA_CRO~X/deliverables/
**Asked by:** 1.0.0_SA_CTO, msg 103471, under the self-drive arming record @c48af273cc.

Prepared by 4.0.0_SA_CRO~X on 2026-10-01 (measured 05:12Z to 05:30Z). Read-only assessment plus proposed closure
requirements. No application change, no vendor call, no Lambda invoke, no deployment, no schedule change. Position
files were read for firm-level aggregates only; every local copy was deleted after its read.

## Design finding

The thread is meant to give an advisor, for one Inflection account, a return Opal computes from that account's own
end-of-day holdings: Orion supplies each day's positions and prices; Opal lands them raw, mirrors them into the shared
assets plane, converts them to `fact_positions`, computes the holdings-basis gold from two consecutive trading days,
and serves that one gold shape through the Performance adapter to the tab and the PDF. Orion's own calculated return
is a comparison point and never the served figure.

Three things separate the implementation from that design.

1. **The served adapter does not read the gold for Inflection.** On deployed bytes Inflection is composed through a
   live Orion call for the vendor's calculated return. The switch to the gold (IB-pr-221) is on CLOUD, not served.
2. **The gold's dates are one trading day late since early May 2026.** A daily-pulled Inflection partition dated D
   holds the close of the trading day BEFORE D. The producer treats the partition date as the day. So each row since
   the seam carries the previous trading day's return under the next day's date. This is not in any row or ruling.
3. **Nothing fires the producer for Inflection,** and the positions it would read stop at 2026-09-27.

Worth keeping: the mirror and the silver converter did exactly what they are built to do on every day raw arrived;
the gold producer already carries the Inflection source as data; 1,609 gold days exist from one backfill.

## Current measurement

Read from live objects and DEPLOYED bytes. At 05:14Z five packages were downloaded and each zip's sha256 equals the
live CodeSha256 (5 of 5). Members were compared to CLOUD @641e5a8259.

| Unit | Live identity | Against CLOUD |
|---|---|---|
| raw writer: the chain on EC2, `opal-inf-bronze-runner-cron` 11:15Z | last run `chain_full_20260930_145412`, failed at step 33 | not a package; state read from `status.json` |
| `opal-assets-ingest-mirror` | `XYgkNk8q..`, 2026-08-11 | 1 commit behind (97380d4869, an investigation commit) |
| `opal-assets-silver-orion` | `dO6YMv6G..`, 2026-09-27 | 7 of 7 modules identical |
| `irpt-holdings-performance-lambda` | `gLRGHIyi..`, 2026-09-29 | producer and `sources.json` identical |
| `irpt-performance-adapter` | `+h/AH/RY..`, 2026-09-29 | 9 modules behind, among them the three of IB-pr-221 |

Frontiers at 05:22Z on Thursday 2026-10-01 (the trading calendar expects a partition for 09-28, 09-29 and 09-30; the
10-01 pull is not due until 11:15Z):

| Object | Last present | Missing |
|---|---|---|
| raw positions `.jsonl.gz`, `opal-data-inf` | 2026-09-30 (landed 15:18Z, a manual run) | 09-28, 09-29 |
| raw positions `.parquet` (the coerced form, a second writer at 11:22Z) | 2026-09-30 | none |
| mirrored raw, `opal-data-assets` | 2026-09-27 | 09-28, 09-29, 09-30 |
| `fact_positions` | date=2026-09-27 (2,343 partitions from 2020-04-24) | 09-28, 09-29, 09-30 |
| Inflection holdings gold | date=2026-09-25 (1,609 days from 2020-04-27, all written 2026-09-29 09:05Z-09:24Z) | 09-28, 09-29, 09-30 |

NOT invoked, and not claimed: any function, Orion, a signed-in page. No Inflection Performance request was made, so
the adapter's behaviour for Inflection is read from its deployed code, not from an answer.

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/inf_performance_trace_20261001/EVIDENCE.json`.

## Adapter map

| Firm | Provider and intended path | Existing work | Gap |
|---|---|---|---|
| Inflection | Orion positions -> raw -> mirror -> `fact_positions` -> holdings gold -> adapter | every stage built; gold backfilled once | adapter not switched; gold dates late by a trading day; no producer schedule; three partitions missing |
| 49 Financial | Schwab `dim_position` -> holdings gold -> adapter | served since 2026-09-29 | its own rows (the 09-29 catch-up); not this trace |
| Cottonwood | Black Diamond `fact_holdings` -> holdings gold | declared in `sources.json` | not traced |

49 Financial's success does not certify Inflection's: the two sources date their partitions differently (hop 5).

## Start-to-finish walk

### 1. Orion -> raw positions in `opal-data-inf` -- INCOMPLETE

What exists: the chain on EC2 (`inf-gold-layer-runner`, started by `opal-inf-bronze-runner-cron` at 11:15Z), whose
positions step writes `bronze/positions/<run date>.jsonl.gz` at about 11:51Z. 80 files were written on their own
date, the first on 2026-07-02. A second writer, `inf-api-positions-daily` at 11:22Z, writes `<run date>.parquet` every day.

The exact gap: the chain wrote no `.jsonl.gz` on 09-28 or 09-29 (dead at step 3, row W86-S1, repaired in round 26).
Its 09-30 file came from a manual run at 15:18Z. No scheduled run has succeeded since the repair; the first is today
at 11:15Z. The runner's unexplained stop of 09-29 (row W86-S2) is still under observation.

The two missing run days are not missing from Opal's disk: `2026-09-28.parquet` and `2026-09-29.parquet` exist in
the coerced form. The 09-28 file is the same size as 09-27's (1,281,876 bytes; content not compared), which is what
hop 5 predicts.

Close: observe today's 11:15Z run land `2026-10-01.jsonl.gz` before 13:05Z. For the two missing days the CTO chooses
one of three: admit the coerced files for those two dates, a vendor as-of pull (Andrew's per-use word), or a declared
gap. Hop 5 shows only the 09-29 file carries a close no other partition holds.

### 2. Raw -> the ingest mirror -> `opal-data-assets` -- INCOMPLETE

What exists: `opal-assets-ingest-mirror`, fired once a day for Inflection at 13:05Z, copying raw `.jsonl.gz` only
(coerced files are refused by its ruling 16). It copied each of the last nine days read, through 09-27, at 13:05:2xZ.

The exact gap: one fire a day and no second look. A raw file that lands after 13:05Z waits a full day: the 09-30
file is still not mirrored. And the function ends in an error on every Inflection fire for an unrelated key (row
W99-S3), so its failure signal cannot distinguish a real positions failure.

Close: a late-raw path (an object-created trigger on the raw prefix, or a second fire), and the alien class ruled.
Proof: a raw file written after 13:05Z is mirrored the same day.

### 3. Mirrored raw -> `fact_positions` -- WORKS

What exists: `opal-assets-silver-orion`, triggered by the mirrored object and swept at 16:00Z; deployed code equals
CLOUD (7 of 7). Every mirrored day was converted within 15 seconds (13:05:23Z raw, 13:05:3xZ silver).

Limit: its sweep verdict reads FAIL daily on one stray key (row W99-S4, inert).

Close: none.

### 4. The Inflection gold chain and its step-33 guard -- INCOMPLETE, and off this thread's path

What exists: the chain's later steps (INF_C_01 onward) and the coverage guard on net new assets, which refused at
step 33 on 2026-09-30 (row W97-S3; the Branch A packet is `2.0.0_SA_COO~P`'s).

The finding: the holdings-basis thread does not consume anything after the positions pull. The gold producer reads
`fact_positions` directly. The guard blocks INF_C_02 through INF_D_11 and the surfaces those feed; it does not block
FWD-3's Inflection arm. The only coupling is that one EC2 run produces both, and the positions step comes first.

Close: none for this thread. The guard's packet stays on its own track.

### 5. `fact_positions` -> the Inflection holdings-basis gold -- MISMATCHED

What exists: `holdings_performance.py` with the `orion` entry in `sources.json`, deployed and equal to CLOUD; a
backfill of 1,609 trading days in `opal-data-inflection`.

The exact mismatch, in three parts.

(a) THE DATE. For trading day t the producer reads partition `date=t` and partition `date=prev_trading_day(t)`
(`holdings_performance.py:838-855`), for every source. For Inflection the partition dated t was pulled at about
07:51 Eastern on t, before the open, and holds the PRIOR close. Measured: across four weekends the Saturday and
Sunday partitions are identical (100% of prices), and after the seam the Saturday partition differs from Friday's
in 87% to 93% of prices (4 of 4 pairs) -- so Saturday's file is the first to hold Friday's close. Firm totals: Friday
09-25 207,404,700.17; Saturday 208,110,999.41; Sunday 208,110,999.41. The history was not always so: through
Saturday 2026-05-02 the Friday and Saturday partitions are identical (6 of 6 pairs read), because the backfill asked
Orion for each past date. The seam lies between 2026-05-02 and 2026-05-08. From the seam on, the gold row dated t is
the return of the trading day before t; at the seam itself one trading day shows a zero return (inferred from the
two bases, not read from the gold). `sources.json` says
`snapshot_date` holds "exactly the partition's own date" -- true of the column, not of the prices.

(b) NO FIRE. `irpt-holdings-performance-daily` passes `source: schwab_08335338` only. No schedule names `orion`.

(c) THE FRONTIER. The producer answers ABSENT for 09-28, 09-29 and 09-30, and will for 10-01 (its t-1 is 09-30)
until partitions arrive.

Close: a ruled date basis per source, carried as data in `sources.json`, with the producer pairing the right two
partitions; then a rebuild of the Inflection gold, which is free today because nothing serves it. Then a second
schedule entry for `orion` after 13:10Z. Proof: one account's row for a named day reproduced by hand from the two
partitions that hold that day's close and the prior day's.

### 6. Holdings gold -> `irpt-performance-adapter` -- MISSING on deployed bytes

What exists: IB-pr-221 on CLOUD (ee3ff32e71, b917320dca): the adapter reads Inflection from its holdings gold.

The exact gap: the served `installed.py` builds the holdings source for 49 Financial only (`:58-77`), and the served
`retained.py` routes Inflection to `orion_selected` (`:58-62`), whose transport makes one live `Reporting/Scope` call
to Orion on the estate's session (`orion_live.py`). The served module's own text calls that path UNPROVEN. So by its
code an Inflection request either refuses or returns the vendor's calculated return, which FWD-3 forbids as the
served figure. No request was made to see which.

The candidate uploaded for IB-pr-275 (`XslOsVc9..`) differs from the live package in exactly one member,
`served.py`. It does not carry the switch, so that packet does not move Inflection's source.

Close: serve IB-pr-221 under its own packet, after hop 5's date ruling. Proof: one Inflection request answered from
the gold with no call to Orion in the function's log.

### 7. Adapter -> the Performance tab -- INCOMPLETE

What exists: the live route `GET performance/{accountSetId}` and the served portal's `performance-report` operation.

The exact gap: no Inflection PerformanceReport has been produced. The adapter computes exactly one selected account;
a relationship answers SELECTION_UNSUPPORTED, where FWD-3 asks for composition. Not read here: no signed-in session.

Close: after hop 6, one walk of one Inflection account on the local DEV build against the real backend.

### 8. Performance report -> PDF -- INCOMPLETE

What exists: the Performance export chain (controller, host render dispatch, receipt, download), with three export
ledgers open on their live-walk legs (STATUS~P, Parked).

The exact gap: never run for an Inflection report, because none exists.

Close: export the report of hop 7 and compare its figures to the screen at one gold revision.

## Recommended completion sequence

PROPOSAL -- the CTO rules the way forward.

1. **The live thread.** One Inflection account, default window, on the deployed stack: hops 1, 2, 3, 5, 6, 7, then
   8. In order: (a) watch today's 11:15Z run and the 13:05Z mirror, no act needed; (b) the date-basis ruling and the
   gold rebuild, BEFORE anything serves the gold; (c) one producer fire for `orion` on a computable day; (d) the
   IB-pr-221 served move under its packet; (e) one request, one screen, one PDF, one trace. `2.0.0_SA_COO~P` owns
   every act; the ruling is the CTO's.
2. The `orion` schedule entry (hop 5b).
3. The two missing run days (hop 1): under hop 5's finding the 09-28 file repeats Friday's close, so one day is at
   stake, not two.
4. The mirror's late-raw path and its alien class (hop 2).
5. Relationship composition (hop 7).

The step-33 guard is not on this list: it gates other surfaces, not this one.

## Acceptance

One reconciled trace for one invested Inflection account: the raw file, the mirrored key, the silver partition pair,
the gold row, the adapter's report, the screen, the PDF -- at one gold revision, with the day's return reproduced by
hand from the two partitions that hold that day's close and the prior close.

Cases: one account on a day after the seam, one on a day before it, the seam day itself, a day whose partition is
absent, a relationship, a raw file that lands late.

## Evidence anchors and limits

Workspace CLOUD @641e5a8259. Verified fresh: the five packages' bytes, the object frontiers, schedules, the chain's
status file, the uploaded adapter candidate, and the price comparison across 10 Friday-Saturday pairs and 4
Saturday-Sunday pairs. Not verified: the seam's exact day; whether the 09-30 raw, pulled at 15:18Z, holds Tuesday's
close; Cottonwood's date basis; the directory's and other Inflection consumers' exposure to the same basis; any
request's behaviour.

- `data/assets/scripts/gold/irpt_holdings_performance/{holdings_performance.py,sources.json}`
- `data/inf/manual_api/pull_inflection_positions_daily.py`
- `infra/aws/lambda/investor-reporting/performance/{installed.py,retained.py,holdings_gold.py,orion_live.py}` (served copies read from the deployed zip)
- `infra/aws/lambda/investor-reporting/holdings-performance/handler.py`
- `infra/aws/lambda/opal-assets/{opal-assets-ingest-mirror,opal-assets-silver-orion}/`
- `org/missions/D9/IRPT/IRPT_BCKEND/ledger/{ROUND_ANALYSIS.round26P.md,ROUND_ANALYSIS.sweep5.md}`, `STATUS~P.md`
- `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~99/ROUND27_DIAGNOSIS.json`
- rows S216, W86-S1, W86-S2, W97-S3, W97-S4, W99-S1 to W99-S4 in the project's surprise channel

## Andrew-direct request -- verbatim record

Channel: Andrew at the `1.0.0_SA_CTO` terminal, 2026-10-01 about 04:23Z (12:23 AM Eastern), recorded by that seat in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`;
this surface reached this seat as msg 103471.

> You have 4.0.0_SA_CRO~X as your research partner so as you see projects developing, if you assess there needs to be
> higher resolution on any part of the development process, you have CRO~X run /closer trace on the given surface and
> assess the strategic way forward.
