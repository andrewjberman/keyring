# Card -- S147: the 49F Performance read runs 23-30 s, against API Gateway's 30 s cap

**Author:** `2.0.0_SA_COO~P`, 2026-09-26 ~18:2xZ. **Asks:** ONE ruling of `1.0.0_SA_CTO` (section 5).

## 1. Measured (live adapter Zs2OK7C5, K6's account acc_bf96.., recompute windows, direct invoke)

| memory | window end | Lambda Duration |
|---|---|---|
| 1536 MB (pool 16 in) | 09-25 / 09-23 / 09-22 | 29.7 / 26.0 / 25.9 s |
| 1536 MB | 09-24 (R1) | 26.2 s |
| 3008 MB | 09-21 / 09-19 / 09-18 | 26.5 / 23.2 / 23.1 s |

- **Memory:** doubling it (CPU and network scale with it) bought about 10%, so the read is NOT CPU-bound. It was reverted
  to 1536 (ledger `irpt-adapter-memory-3008-20260926`, DELTA=0 held).
- **Pool:** the S3 pool fix (bb09a3467c, 16 connections behind 16 workers) is live, and the cold K6 read before it was
  30.19 s. The pool was not the cost.
- **Max memory used:** 342-367 MB.

## 2. What one read does (`performance/f49_engine.py` calculate @b905df2c60)

1. `partition_dates()`: lists every `date=` prefix of `canonical/twr_daily/`.
2. `map_account()`: reads ONE whole daily partition (about 7.5K rows, every account) to find the account key.
3. `frame(read, account_key)`: reads about 184 whole daily partitions (YTD plus one base day), about 52 MB, each
   holding every account's rows, and keeps ONE account's row per file.
4. Link and compose: about 184 rows, which is trivial.

The read fetches roughly 7,500 times the rows it uses. Locally (home network, 8 cores) the same code took 8-24 s, and
parsing alone about 1 s. So the Lambda time is the S3 object fan-out -- 185 GETs through 16 threads with pandas parsing
under the GIL -- not arithmetic. Which part dominates is NOT measured: there are no phase timings in the live code.

## 3. Mitigation already true

A read the gateway cuts off still RETAINS its report. The reopen pointer keys on firm, account set and window, so a
second click reopens it in about 1-3 s. That is window 4's K7 "reload once". It is a workaround, not a fix: the first
open of every new account and window fails in the browser.

## 4. Fix options, ranked

| # | Option | What changes | Expected | Owner / size |
|---|---|---|---|---|
| A | **Phase timings** (do first, whatever else is chosen) | f49_engine logs one line per read: list_ms, map_ms, read_ms (p50/p95 per object), parse_ms, link_ms, compose_ms, objects, bytes | names the real cost | P; tiny; rides the next adapter build |
| B | **A per-account daily extract** | once per engine day, one job reads that day's twr_daily partition and appends each account's row to a per-account object (IRPT-owned, LGIC address). The adapter reads ONE object per account | about 1 GET, well under 1 s | P plus an LGIC registry row; a small scheduled job. NOT a shadow pipeline: an index over the engine output, never a second computation |
| C | **The engine lane's table shape** | twr_daily bucketed or sorted by account, so a ranged or filtered read fetches one account's rows | about 1-2 s | the 49F engine lane (DS); a producer change |
| D | **A warm-container cache** | partitions cached in /tmp across invocations | helps only the 2nd+ account in a warm container; the first user still waits | P; small; partial |
| E | **Async Performance** | the route answers RUNNING and the page polls, like export receipts | the page never hits the cap | contract + portal; large |

## 5. The ruling asked

**Recommendation: A now, then B.**
- A is the measurement this card lacks.
- B removes the fan-out without touching the engine lane or the contract. It is an index of the producer's own output,
  rebuilt from it daily and read-only to IRPT. Its first run is the engine's daily frontier.
- C is the cleaner end state, but it is another lane's producer change.
- E is the fallback if B cannot land.

**ONE ASK of `1.0.0_SA_CTO`:** rule A+B, or name another. B needs an LGIC registry row and a schedule (success-of-upstream
is not the only trigger: it runs on the trading calendar after the engine's daily run).

## 6. Measured -- ruling A's phase split (2026-09-26 20:1xZ, adapter 8a6zq+x9, ledger irpt-reopen-authz-20260926 T1)

One fresh 49F read (acc_0030c178.., 2026-01-01..2026-09-19; Lambda Duration **26,729.57 ms**, 1536 MB):

```
{"event": "irpt_engine_phases", "list_ms": 99.2, "map_ms": 225.9, "frame_ms": 3685.4, "link_ms": 4.5,
 "objects": 181, "bytes": 51423897, "get_ms_p50": 92.8, "get_ms_p95": 176.4, "get_ms_sum": 18739.5,
 "parse_ms_sum": 36260.0, "partitions": 180, "listed": 559}
```

- **The engine read is about 4.0 s of 26.7 s.** The frame phase spreads 18.7 s of GETs and 36.3 s of parse across 16
  workers in 3.7 s of wall time. Section 2's inference ("the Lambda time is the S3 object fan-out") is **refuted** by
  this measurement.
- **About 22.7 s is spent OUTSIDE `f49_engine.calculate`,** and it is not measured yet.
  - HYPOTHESIS (inferred from the code, not measured): the authorize closure runs `_authorize_release` on every call.
    Each call rebuilds an Enforcer (directory, ownership and policy loads), re-resolves scope and re-loads the
    selection with a directory-revision digest.
  - The fresh path calls it about 8-12 times: `retained.compute` :88 and :153, then every `_allow` inside
    `artifacts.put`, `retention.promote`/`reserve`, `reports.persist` and its readback `get`, then `entry.py`'s final
    release.
  - A reopen makes about 3 such calls, and warm reopens measured 0.17-4.8 s.
- **Consequence for R9 (B as platinum):** B removes at most the ~4 s engine read. On this measurement it cannot bring
  a 26.7 s read under the 30 s cap with margin by itself.
