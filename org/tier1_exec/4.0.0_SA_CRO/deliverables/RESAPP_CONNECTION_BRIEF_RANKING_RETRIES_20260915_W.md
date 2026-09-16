# RESAPP connection brief: ranking reruns must replace a complete result

Seat: `4.0.0_SA_CRO~W` · 2026-09-15 06:33Z · To: `1.0.0_SA_CTO~W`  
Authority: Andrew's 60-minute COO~W/RESAPP gap review. Recommendation for the next cut; no task issuance, deployment or live mutation.

## Measured defect

`lib/research/metrics/chatter_axis.py@08b2c499235e0291668666f19f7b812b44dd942a`, lines 383–395, writes rows through `batch_writer(overwrite_by_pkeys=['axis_date','ticker'])`. It never removes prior rows absent from a new ranking. `compute_chatter_axis`, lines 429–444, calls this writer for each movement, including an empty list. The deployed-source entry point `infra/aws/terraform/harvest/lambda_src/lambda_function.py` calls this computation directly; the inspected wrapper adds no replacement operation.

A local probe ran the actual `default_write_rows` with only `boto3.resource` replaced by an in-memory table. No AWS call or table change occurred:

| Same-date run | Intended winners | Reported writes | Stored result after the call |
|---|---|---:|---|
| First | AAA #1, BBB #2 | 2 | AAA #1, BBB #2 |
| Replacement | BBB #1, CCC #2 | 2 | **AAA #1, BBB #1, CCC #2** |
| Empty result | none | 0 | **All three previous rows remain** |

The API `lib/research/api/scoped_amgt.py:295–320` queries the date partition through `axis-rank-index` and passes the rows through. Thus a same-day QA run, retry with changed input, or backfill-driven recomputation can retain a former winner, duplicate rank 1, and expose more than the intended top N. A now-empty Breakout result cannot clear an earlier nonempty one through this writer. This is a local demonstration of the writer's behavior, **not a claim that the live table currently contains these bad rows**.

## Connection to specify and exercise

The pool-reader recut should publish a **complete ranking generation** and let the reader select that committed generation. Choose the storage mechanism explicitly: immutable generation plus a current pointer is one option; a carefully bounded replacement of the old same-axis/date membership is another. The contract must cover zero winners, a changed winner set, failure during publication, and a repeat of the same completed run. Protect the other axes/dates and firm watchlist partitions in the shared metrics table.

Carry the selected generation/run ID, source coverage vintage and payload hash into the exact-input exercise (`Z-S72`); a date alone cannot distinguish two computations on the same day. Keep the existing distinction between producer/read failure and a successful empty product.

Acceptance: the three runs above yield 2, 2 and 0 visible winners respectively, unique contiguous ranks for each completed result, and no mixed generation after an interrupted write. Then exercise the API/page against that same result identity. Do not fix this by masking excess rows with a reader limit: the stale row can itself carry rank 1 and displace a current winner.

The organic 10:00Z Chatter schedule fire remains future evidence at this review's time; none was invoked here. The publisher collection cadence remains reserved to Andrew.
