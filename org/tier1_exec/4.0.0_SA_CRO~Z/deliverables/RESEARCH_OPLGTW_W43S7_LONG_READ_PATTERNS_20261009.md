# NFRA_OPLGTW W43-S7: a cold 13-month availability read -- estate patterns for long reads (4.0.0_SA_CRO~Z, 2026-10-09 ~19:2xZ)

Asked by `1.0.0_SA_CTO~Z`, msg 32947 (design fork: (a) warm, (b) cap, (c) async). Sources were read at HEAD on site Z. A
line marked UNMEASURED was not run.

## 0. The fact that reframes the fork: the real service already persists each date once

`Catalog.snapshot()` (`infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py:841-870`) first reads a stored
snapshot from access_state (`_stored`, `:975`). Only when none exists does it verify the date's objects in S3 and then
`persist()` it (`:963-969`). `persist()` writes once, with `IF_ABSENT`, keyed on (master, date, closure_id). So the
expensive part, about 0.8 s per first-seen date in the row, is paid ONCE per date, EVER. Every later read of that date,
by anyone, skips the S3 verification.

The row's figure (221-235 s per master) was measured on a host harness with an in-memory store
(`r29_grant_host.py.txt`, MemStore), so every one of the 274 dates was first-seen. The row says so itself: "a warm service
may be faster. NOT measured against the real service". The harness's "0.2 s warm" for the other datasets is the
per-request `cache` dict (`availability(..., cache=)`, `:899`), not the persisted store.

So on the real service, "cold" is a one-time event per master. It happens at the first 13-month read, because the dates
beyond the old 30-day window were never snapshotted. After that, each new business date adds one first-seen date, about
0.8 s, paid by whichever read comes first.

What a WARM read still costs is UNMEASURED. Per date in the window, it is one S3 GET of the completion marker
(`_read_marker`, `:812`) plus one access_state GET. These run sequentially (`:935-937`), 274 per master.

## 1. The budget the read must fit

- **ALB idle timeout:** `infra/aws/terraform/opal-gateway/alb.tf` sets no `idle_timeout`, so the AWS default of 60 s
  applies. That is DESIRED; I did not read the live attribute. A cold read of 221-235 s per master would be cut at the ALB
  long before it finished. Whatever the MCP client's timeout is, it was not read.
- **The gateway's own read caps:** `gateway_query_catalog` is capped at 1000 rows, 4 MB and 10 s
  (its tool description; the query_v0 route).

## 2. Estate patterns for long reads, and what each cost

| # | pattern | where | what it cost | fit for W43-S7 |
|---|---|---|---|---|
| P1 | **Persist-once snapshot** (write once, read many) | this catalog, `catalog.py:842-870`, `:963` | nothing new: it exists | The cold cost becomes one-time. A one-off PRIME of the 13-month window per master makes every later read warm. It is not a standing job: the daily increment is one date |
| P2 | **Bounded fan-out**, `ThreadPoolExecutor(FETCH_THREADS=8)` | `admin_fabric.py:38,100`, `admin_fabric_gitstate.py:41,115,167` | a few lines per loop; 8 concurrent S3 reads | Applied to the per-date loop (`catalog.py:920-937`), it cuts both cold and warm time by about 8x. Cold goes from 222 s to about 28 s per master: still over 60 s for two masters in one request, so alone it is not enough |
| P3 | **Wall-clock-bounded call**: refuse or record absent on timeout, never stall | `opal_discover/integration.py:265` (`_HEAD_WALL_SECONDS = 8`, `_bounded_head`) and its GET twin | small; the answer degrades to "absent" with the claim carried | A per-request deadline on availability turns a hang into a clear refusal. This is the honest form of (b), cut by time, not by months |
| P4 | **Hard cap with refusal before the read** | `gateway_query_catalog`: 1000 rows / 4 MB / 10 s, "refused before any read" | none in code; the user meets a refusal | (b) by MONTHS conflicts with Andrew's 13-month grant word (record `116d52009d`: "13 months") and the grant model (`calendar_months` 1-13, `data_entitlement.py:80`). Capping below 13 refuses what he granted |
| P5 | **Async handle**: return an id, read the status with a second tool | data-refresh: `opal_data_refresh_upload` returns `execution_id`; `opal_data_refresh_status` reads it (`opal_portal/integration.py:74, :286-:414`) | There the durable job is the portal's Step Functions execution, so the gateway keeps only an in-process idempotency record, which "A GATEWAY RESTART CLEARS" (`:84`) | (c) has no external executor here. It would need a job record in access_state, a background worker in the gateway process that survives a restart, a status tool, and a client (the Analyst, Alyssa's MCP client) that knows to poll. It is the most code and new state of the three, and it is only as durable as its job store |

## 3. Recommendation: (d) = P1 prime + measure, then P2 if needed; hold (c)

1. **Prime once.** Run one real-service availability read per master with `calendar_months=13`, by an internal or
   operator principal, never as Alyssa. Run it in the background on the host, as the worker's SSM runs were (about 4
   minutes per master, once). It writes only write-once snapshot records in access_state, keyed by closure. These are
   runtime cache records, not served output, and nothing is overwritten.
2. **Measure the warm read** through the real service, one request per master, and record the elapsed time. That
   figure decides the rest:
   - **Warm read of a few seconds:** done. The 13-month read is interactive. Each new day costs about 0.8 s for one
     date.
   - **Warm read near or over the budget** (about 20 s or more per master): add P2's fan-out to the per-date loop.
     Re-measure.
   - **Still over after P2:** build (c), with its job record in access_state, not in process memory (P5's restart lesson).
3. **Keep P3** as the safety net: a wall-clock deadline on availability that refuses clearly, instead of the ALB cutting
   the connection mid-read.

**Against the CTO's rec (c):** both refuse nothing Alyssa needs and add no standing job. (c) also adds a job runner,
a job store, a status tool and a polling client, and it would still pay the 221-235 s cold read at least once. (d) costs
one 8-minute act and possibly a few lines of fan-out, and it makes the read synchronous. Build (c) only if the measured
warm read after the prime does not fit.

## 4. Edges this does not cover

- **A producer replay that changes a date's closure_id** makes that date first-seen again: 0.8 s for that date. This is
  rare, and P1 already handles it.
- **A grant on a third master,** or a new dataset with no shared marker: one prime per new master.
- **The live ALB idle timeout and the MCP client timeout** were not read. One `describe-load-balancer-attributes` call
  settles the first.
