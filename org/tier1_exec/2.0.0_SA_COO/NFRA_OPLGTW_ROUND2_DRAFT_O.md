# NFRA_OPLGTW round 2 -- DRAFT package, `2.0.0_SA_COO~O`, 2026-09-18 ~23:00Z

⛔ **THIS IS A DRAFT, NOT AN ISSUANCE.** No task order here is cut, no cell is seated, and nothing in this
file authorizes a worker. Round 1 is still open (3 orders). It exists so the round-2 recut is ONE issuance
on the tick round 1 closes, per Rule 27's L10 obligation.

⚠ **THREE OF THESE ITEMS DEPEND ON RULINGS THAT HAVE NOT LANDED** -- calls 1, 2 and 3 of my 22:11Z message
to `1.0.0_SA_CTO`, as corrected at 22:47Z. Where a ruling would change the cell, the cell is written with
its FORK stated rather than one branch chosen. **A draft that pre-picks the CTO's branch is the defect this
warning exists to prevent.**

## What round 1 leaves

| item | source | state |
|---|---|---|
| Export at contract scale does not fit the job cap | `OGR2-AC4` FAIL, measured | needs a spec decision (call 1) |
| `OGR2-AC2` passes on a job 13.6 MB over the cap | row `S48`, my drain read | needs a spec decision (call 3) |
| "zero failures" bar vs episodic 5xx | rows `W2-S10` + `S49` | needs a spec decision (call 2) |
| Conditional-`UpdateItem` consume (branch 2) | `R-OG-21A`, round-1 carry | ready to cut |
| A LOGIN-PATH health check | my own 16:xxZ defect | ready to cut |
| Sentinel `"*"` + populated-roster cleanup, 8 rows frozen | round-1 carry | ready to cut |
| The 19 unexplained 5xx of 09-04/09-09/09-10 | row `S49`, NOT established | investigate, or disposition as out of scope |

## The cells, as drafted

### R2-a -- export limits reconciled with the job cap (FORKED on call 1)

**Measured inputs, from `CAPACITY.json` @`0279872d7a`:** contract asks 250000 rows / 52428800 bytes; the
export peaked at `270581760` against the `268435456` cap and ended LIMIT_EXCEEDED. The largest export that
COMPLETED: 62500 rows / 9468970 bytes at `214065152` peak RSS.

- **If the CTO lowers the export limits** (my rec): the cell amends `org/standards/NFRA_OPLGTW_CONTRACT.json`
  `limits.export_rows` / `export_utf8_bytes` to a pair measured achievable, re-runs the OG-r-2 export arm at
  the NEW pair, and re-grades AC4 against it. **The new pair is the CTO's number, not mine** -- 62500 rows is
  the largest MEASURED success, not a maximum; the cell measures the interval between 62500 and 250000 rather
  than adopting the one datapoint it happens to hold.
- **If the CTO raises `job_memory_bytes` instead:** the cell re-prices admission first (R2-b), because two
  jobs at a raised cap must still fit `1936322560` minus the OS reserve. Raising the cap without that
  arithmetic is the branch I recommend against.

### R2-b -- admission arithmetic priced against real child behaviour (FORKED on call 3)

Today's reserve: existing peak RSS x 1.25 + 134217728 = `375753728`, from a measured existing peak of
`193228800`. **The measurement `S48` adds: a child can reach `282021888`, about 1.05x the per-job cap, before
the guard ends it.** Two such children reach `564043776`. The cell re-derives the reserve from the MEASURED
overshoot rather than from the cap, and re-runs the OG-r-2 admission arm.

Independent of the ruling: the cell fixes `onhost_bench.py:418-421` so `_cap_respected` reads
`peak_child_rss_bytes` on BOTH branches and records the overshoot explicitly. **That is a measurement defect,
not a spec question, and it does not wait on anyone.**

### R2-c -- the "zero failures" bar (FORKED on call 2)

`S49` establishes the shape: four non-zero days of fifteen, eleven true zeros, ELB-side 5xx absent entirely,
and today's two attributable to our own DeleteItem outage. My revised rec is to keep the literal zero and
grade on a window free of NAMED incidents. The cell implements whichever bar the CTO rules, and in EITHER
branch it records the incident register the bar reads from.

### R2-d -- conditional-`UpdateItem` consume (branch 2), ready

`oauth_as.py:649`/`:772` consume by conditional DELETE, which is why the runtime role needed `DeleteItem`.
Branch 2 marks `consumed_at` by conditional `UpdateItem` instead and lets the grant narrow again. The cell
carries the R-OG-21A record, re-runs OG-a-1's durable tests, and exercises the login path end to end AFTER
the grant narrows -- **the narrowing is the act that can break login, so its acceptance is a real login, never
a test double.** Ordering: after R2-e, so a broken login is detected by a monitor rather than by Andrew.

### R2-e -- a LOGIN-PATH health check, ready, and it is mine to own as a defect

**`/health` 200 + `/mcp` 401 + ALB healthy was GREEN for the entire 10h35m outage**, and on that reading I
told Andrew the gateway was "up and healthy" while no one could sign in. The cell builds a check that
exercises the login PATH -- register, authorize, callback, token -- against a synthetic principal, and fails
when the sequence fails.
⚠ **The standing moratorium (CLAUDE.md: never build an alert/monitor unless Andrew explicitly asks) binds
this cell.** It is drafted as a CHECK whose result lands in an existing gate or an owned blocking item, NOT
as an alarm, an SNS topic or a notification. **If the cell cannot be built without a notification surface, it
becomes a card for Andrew and stays uncut.**

### R2-f -- sentinel `"*"` and populated-roster cleanup, ready but VALUE-BLOCKED

The correctness half proceeds: an EMPTY roster means UNCONFIGURED and fails CLOSED, never tenant-wide.
⛔ **The VALUE half does not.** Andrew's ~18:1xZ word set the audience as "all opal employees"; his ~21:1xZ
word DEFERRED the population question, which sets priority and not the value. **So the cell ships the
fail-closed behaviour and leaves the roster value unset. No wildcard is written on a deferral.**

### R2-g -- the 19 unexplained 5xx, or an explicit disposition

`S49` did not establish the cause of 09-04 (3), 09-09 (3) and 09-10 (13). Either a cell reads the journal at
those hours and names them, or the CTO dispositions them as out of scope for D9. **What is not acceptable is
carrying them forward as "ambient" -- that is the exact word `S49` retired.**

## Fan-out, when this is cut

Seven cells, of which R2-d, R2-e and R2-f have no unmet dependency today. Chains: R2-a and R2-b are one chain
(the cap decision feeds the reserve); R2-c and R2-g are one chain (both read the 5xx register); R2-d follows
R2-e. **Cap 8, stated here and restated in the issuance commit.** Slot ~2 carries the benchmark cells, having
built the harness; ~6 carries nothing new until its walkthrough orders clear.

## What must be true before this is cut

1. Round 1 CLOSED -- all three open orders terminal, every row dispositioned, the L10 slug delivered.
   ⛔ **LD-0521: a round-2 issuance cut before round 1's slug DEADLOCKS round 1's L10**, because the refuser
   counts open orders per project. This draft is not an exception to that and becomes an issuance only after.
2. The CTO's three rulings landed, so the forks above resolve.
3. The fan-out re-derived from the decomposition at HEAD, not from this table.
