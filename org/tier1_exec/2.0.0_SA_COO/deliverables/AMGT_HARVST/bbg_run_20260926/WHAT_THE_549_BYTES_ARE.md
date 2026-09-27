# The 549-byte HTTP 200 is a SESSION CHECK THAT SUCCEEDED, and bbg's real failure is an INTERMITTENT 403 nobody has retried

**Measured 2026-09-27 from `.runtime/opal-data-harvest/events.jsonl`** -- 67 bbg http events, on disk, **no
vendor call made to produce this file.**

---

## 1. TWO THINGS I SAID ABOUT THE 549 BYTES, BOTH WRONG

I wrote: *"A signed-in search response is not 549 bytes -- that is an interstitial. Reading that body costs
one read and answers 'is this token working'."*

**It was never a search response, and 549 bytes is the RIGHT size for what it actually is.**

| what the ledger says | |
|---|---|
| host | `login.bloomberg.com` |
| path | **`/user-info`** |
| status | **200**, on **6 of 6** calls |
| bytes | **549**, on 6 of 6 |
| dates | 2026-09-15 (x3), 09-23, 09-26 20:32, 09-26 22:27 |

`/user-info` is the **SESSION IDENTITY CHECK**. A small JSON payload is exactly what it should return, and a
200 on it is the producer confirming **we are signed in**. Calling it an interstitial inverted its meaning:
the line I read as evidence of failure was the one piece of evidence that the token WORKS.

⭐ **So this is a THIRD independent instrument agreeing with Andrew's rule** -- *"if you have a long term
cookie that is working, then you do not need to do the crawl"*. The first two were the discriminating pair
(a 5-day-old and a 20-minute-old envelope failing identically) and `auth_refreshes: 0`. This is the
endpoint whose entire job is to answer that question, answering 200 six times out of six.

⛔ **AND THE BODY IS NOT RECOVERABLE, WHICH IS BY DESIGN.** `transport.py:100-103` holds bodies in memory and
records only status/path/bytes: *"No cookies, headers, query values, or response bodies in the event
ledger."* So "read that body" was never a free check -- it would have needed a fresh vendor call. The path
and size in the ledger were the free check, and they are enough.

## 2. THE REAL FAILURE, AND IT IS A DIFFERENT ENDPOINT

**`/nemo-next/api/search/query` -> HTTP 403, 535 bytes.** Every bbg failure this month is that one line.

## 3. THE HISTORY IS THE FINDING: THAT 403 IS INTERMITTENT, AND BBG GENUINELY WORKED

All 15 search calls in the ledger:

| when | status | bytes |
|---|---|---|
| 2026-09-15 03:31:31 | **403** | 535 |
| 2026-09-15 03:44:24 | **200** | 8846 |
| 2026-09-15 03:47:44 | **403** | 535 |
| 2026-09-15 03:55:14 | **200** | 8846 |
| 2026-09-15 04:00:07 | 200 | 7823 |
| 2026-09-15 04:06:05 | 200 | 8175 |
| 2026-09-15 04:40:10 | **403** | 535 |
| 2026-09-15 04:41:22 | **200** | 8175 |
| 2026-09-15 04:44:22 | 200 | 8366 |
| 2026-09-15 04:45:36 | 200 | 10448 |
| 2026-09-15 04:46:33 | 200 | 8631 |
| 2026-09-15 04:47:32 | 200 | 8987 |
| 2026-09-23 00:27:26 | **403** | 535 |
| 2026-09-26 20:32:01 | **403** | 535 |
| 2026-09-26 22:26:44 | **403** | 535 |

⭐ **ON 2026-09-15 A 403 WAS FOLLOWED BY A 200 THIRTEEN MINUTES LATER -- TWICE (03:31 -> 03:44, and 04:40 ->
04:41, that one after SEVENTY SECONDS).** Nine of twelve calls that night succeeded, and the run pulled
**46 article fetches up to 40,687 bytes**, last success 04:48:50. **bbg is not a publisher we cannot reach.
It is a publisher we reached for over an hour, eleven days ago.**

## 4. SO "WALLED" IS NOT ESTABLISHED. "NEVER RETRIED" IS

Since 09-15 there have been exactly **THREE** search attempts -- 09-23, and two on 09-26. **Each was a
SINGLE SHOT**: the first 403 raised, the publisher went on cooldown, and the batch's remaining jobs returned
`cooldown` with zero attempts. **We have never once retried bbg's search within a window**, which is the only
thing that separated success from failure on 09-15.

⚠ **AND THE BOUND THAT PREVENTS THE RETRY IS MINE.** `HVST-v-2`'s BOUNDS say *"ONE capture invocation ... No
retry loop. If a call fails, that IS the result."* That was the right bound for a cell spending a scarce
vendor grant on a publisher believed to need re-auth. Against an endpoint whose 403 is measurably
intermittent, **it guarantees the failure it then records.**

## 5. WHAT THIS RECLASSIFIES

`Z-S14` classified bbg as **"a verification challenge"** -- the one movable of three, which is why Andrew's
troubleshooting offer was carded against it. **The measurement says bbg's live blocker is now an
INTERMITTENT 403 ON THE SEARCH PATH with a VALID session** -- which is the class `Z-S14` assigned to **ft**
(*"ft is a 403 from its search endpoint"*). bbg has moved into ft's class, and the two may share a cause.

⛔ **NOT PROPOSED HERE, BECAUSE IT NEEDS A WORD, NOT A GUESS:** a paced bbg retry, on the cadence that
worked for sa tonight. It is a vendor act on a publisher whose remedy was carded to Andrew, and the honest
next step is to say what the evidence now supports -- not to spend another grant discovering it.
