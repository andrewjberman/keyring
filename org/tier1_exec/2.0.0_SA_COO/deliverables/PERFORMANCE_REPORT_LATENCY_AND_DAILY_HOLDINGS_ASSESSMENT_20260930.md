# Where the slowness in a Performance report comes from, and what exists for daily holdings-based performance

**For:** Andrew. **By:** `2.0.0_SA_COO~P`, 2026-09-30 ~05:1xZ (about 01:1x ET). **Read-only investigation.** Nothing deployed or changed.
Claim tags: MEASURED (read from a log or S3 this session), CODE (read from source), INFERRED (my reasoning, not tested).

## Conclusion

1. **The slowness is the serving layout, not the daily computation.** The daily holdings math already runs nightly and is stored
   (MEASURED, CODE). But the store is one file per DATE holding EVERY account, so one account's report has to fetch, parse and
   filter one whole file per day in its window. Since Inception on 49 Financial reads 558 files (128 MB) to keep about 558 rows.
2. **Your suspicion is right in direction.** Serve from a per-ACCOUNT series so a report is one small read.
3. **"At the asset level" is a separate question.** The producer already computes at the asset level, then keeps only the account's
   daily return and value. Store asset-level rows only if the report must show contributors or holdings drill-down. I don't know
   that requirement.

## The measured latency (the Lambda `irpt-performance-adapter`, last 2 days, 600 invocations, 1,536 MB, 16-thread reads)

| path | n | median | p90 | max |
|---|---|---|---|---|
| a report computed fresh | 59 | **6.7 s** | 15.2 s | 16.7 s |
| a report reopened from the retained copy | 123 | **0.52 s** | 0.76 s | 0.88 s |
| everything else (refusals by name) | 418 | 0.2-0.4 s | | |

- Of 600 calls, only 182 (30%) returned a report. The rest were refusals (see "State by firm").
- On a fresh compute, **the holdings read is 84% of the time** (median 5.7 s of 6.7 s). The rest is about 0.35 s of request
  preparation, and about 0.6 s to store the report (evidence 0.24 s, persist 0.24 s, read-back 0.08 s).
- **It grows with the window, roughly 24-28 ms per date file:** about 4.9 s for 150-199 files (YTD), 6.7 s for 250-299 (1Y),
  13.6 s for 550-599 (Since Inception).
- One S3 GET is small: p50 59 ms, p95 143 ms, 16 at a time, about 2 s of the 13.6 s. **So most of the time is parsing and
  filtering in Python** (INFERRED: a 1,536 MB Lambda has under one vCPU and threads share the interpreter lock. I did not profile CPU).
- 94 of 600 calls (16%) were cold starts adding about 0.44 s.
- A reopen only hits when firm, accounts, start date, end date and basis all match. The end date moves every day, so the first view
  of each day, per account and period, is a fresh compute.

**Why the layout hurts, in numbers (MEASURED):**

| firm | partitions | size per file | history |
|---|---|---|---|
| 49 Financial | 558 | median 227 KB, 128 MB total | 2024-07-09 to 2026-09-28 |
| Inflection | **1,609** | median 27 KB | 2020-04-27 to 2026-09-25 |
| Cottonwood | 75 | median 36 KB | 2026-06-10 to 2026-09-25 |

At about 25 ms a file, a Since Inception read for Inflection would be about 40 s, near the adapter's 48 s bound, before any
other cost (INFERRED from the 49 Financial rate). That read is not being served today (below).

## What has been built for daily holdings-based performance

- **Decision:** your calls of 2026-09-28 ~22:2x and ~22:4x, "holdings-based performance, all firms, silver to one gold" (PRD
  addenda v0.19 and v0.20).
- **The producer (CODE):** `C:\Users\AndrewBerman\Desktop\ajb_workspace\data\assets\scripts\gold\irpt_holdings_performance\holdings_performance.py`
  (1,065 lines). Method: end-of-day return over the long holdings, cash earning zero, no flow term, one row per account per day.
  Sources are declared as data in `sources.json`: Schwab for 49 Financial, Orion, Black Diamond.
- **The daily schedule (CODE, MEASURED):** Lambda `irpt-holdings-performance-lambda`, 07:30 ET Monday to Friday, ENABLED. **Its input
  pins ONE source, the 49 Financial one.**
- **The reader (CODE):** `...\infra\aws\lambda\investor-reporting\performance\holdings_gold.py` chains the account's daily returns.
  49 Financial switched to it on 2026-09-29 (ledger `irpt-adapter-holdings-gold-49f-r3-20260929`, leg D1).

## State by firm (MEASURED unless tagged)

| firm | gold in S3 | scheduled daily | served |
|---|---|---|---|
| 49 Financial | 558 days, last 09-28 | **yes** | yes, from the gold |
| Inflection | 1,609 days, last 09-25, written once 09-29 09:24Z | **no** | wired in code; **requests refused** (63 `InflectionMappingRefused`, and 51 `ModuleNotFoundError`, cause not diagnosed, firm not confirmed) |
| Cottonwood | 75 days, last 09-25, written once 09-29 ~10:5x Z | **no** | still the vendor path in code; **195 `VendorEgressRefused`** (INFERRED: those are Cottonwood) |

So daily systemization exists for 49 Financial only. Inflection is one trading day behind 49 Financial's last partition; I did not
resolve Inflection's own landing lag, so I do not call it stale.

## Options, in the order I would take them (all ESTIMATES, none built)

1. **Serve from a per-account series.** One object per account holding its whole series (date, daily return, value, status),
   gzipped JSON or parquet, tens of KB. A report is then one GET (about 60 ms) plus a short chain, so the holdings read should
   fall from 5-14 s to well under a second, for every window from one read. The dated gold stays as the record; the daily
   producer also refreshes the account objects. This is what you described, minus the asset detail.
2. **Asset-level rows per account per day** (gzipped JSON), only if the report shows contributors or holdings. It is a much
   larger store (about 106,000 position rows a day for 49 Financial) and a separate product.
3. **Cheap first steps that keep the linear cost:** more Lambda memory (more vCPU), and reading only the needed columns. Likely
   about 2x, and Inflection's history would still be slow.
4. **Warm the retained reports nightly.** The reopen path is 0.5 s, but every day's key changes, so it means precomputing every
   account and period, which is option 1 done the heavy way.

## What I did not measure

- **End-to-end user latency.** I measured only the adapter. I did not measure browser to CloudFront to API to authorization, or how
  the page fans out its period calls.
- **The traffic is walk windows** (a few accounts pressed repeatedly), not real users.
- **CPU profile** of the parse step (inferred above), and the vendor-path latency for Cottonwood.
- **The refusal counts** by firm beyond what the labels say.
