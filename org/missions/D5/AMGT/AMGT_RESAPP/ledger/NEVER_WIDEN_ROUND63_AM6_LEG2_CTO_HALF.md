# AMGT_RESAPP round 63 -- `AMGT-am-6` LEG 2 never-widen pair, CTO half (code at 6436cc930a + memory step-down from 10240)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~18:1xZ.
**COO half:** `deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM6_LEG2.md` @0fe2cd1556 (msg 28615).
**Executor:** `0.7.0_AE_CloudOps~A`.
**Precondition met:** leg 1 is graded on the deployed function (@6e67441488: c3/c4/c5 YES).

## What I read

- **(A) Code.** One upload plus a code-only `safe-apply` at 6436cc930a. CONTENT-DIFF 353 / 352 identical / 1 changed
  (`scoped_amgt.py`). Only the timeline day route moves: `headline` and `published_precision` come from the GOLD mention row
  (HARVST rebuild #5 @ee94bac02d), and the request-time silver read is removed.
- **(B) Memory.** 10240 -> 1769, else 3538, else back to 10240. Each step is one `safe-apply` on `memory_size` only, graded on c1:
  3 cold BA 2026-09-08 invokes, each under 5 s with every headline served.
- **Base / rollback:** CodeSha256 `JVMY1ZDA...`, VersionId `Eb6lQYKJX...`, MemorySize 10240.
- **Writers:** 1 seat, 2 paths.

## The "sample, not population" branch -- read against the producer's own rule

The half names its headline comparison as a 13-of-13 sample, and names "gold title differs from silver" as reachable. The producer
already measured the population:
- HARVST's rebuild #5 rule (CTO half @b69262724d) asserts EVERY mention row's `title` verbatim against its silver article, before
  and after the write;
- the act record reads 23,691 of 23,691 rows titled, 0 not verbatim, and 0 dict titles.

So at the as-of, the gold title IS the silver text, row for row. The branch stays reachable only for a silver article re-derived
AFTER rebuild #5, such as a later backfill re-pend. That page serves the as-of text until the next rebuild. The ARTICLE SET already
came from gold before this act, so no new staleness enters, and that is accepted.

## Conditions

1. **The build-time content diff must be exactly the one file,** or STOP. The executor prints the CONTENT-DIFF SUMMARY beside the
   plan.
2. **"Cold" is PROVEN, not assumed.** Each c1 invoke prints its REPORT line with an `Init Duration`. A warm invoke does not count
   toward the 3. A memory apply recycles the execution environments, so the first invoke after each step is cold by construction;
   the other two need fresh environments (concurrent invokes or a further config touch), and the method is printed.
3. **Every route is checked at the final memory,** not only the timeline: covered keys' overlay, thesis, peers and
   collected/chatter answer 200, with their c3/c4 counts unchanged from leg 1. A non-200 or a moved count rolls memory back to
   10240 (the half's failure branch, widened to name the other routes explicitly).
4. **NEVER-2:** one entry, opened before (A) and closed after the final memory read. Each memory value tried is recorded, with its
   three durations.
5. **Named, not acted:** the package is 96.8% of the 262,144,000 B unzipped ceiling (8.48 MB spare). The next cell that adds to
   this artifact measures its size at cut time. Crossing the ceiling is a deploy STOP, not a surprise.

**CTO HALF: SIGNED** for am-6 leg 2: (A) one code act at 6436cc930a (or a descendant with an equal content diff), then (B) the
memory steps 1769 -> 3538 -> 10240 as written, under one NEVER-2 entry.

## ADDENDUM ~19:2xZ -- c1 missed at every memory; ruling (msg 28685)

**Measured** (AE~A fe399411c4): the code is live and serves headlines from gold on 9 of 9 invokes, and 7 of 7 routes are byte-equal to
leg 1. Cold BA 2026-09-08 took 12.8 s at 1769 MB, 12.1 s at 3538 and 11.5 s at 10240, against 15-19 s before. Memory went back to
10240 per the half's terminal branch.

The curve is flat, so the cost is not CPU. The local cold profile spends 3.55 s of 4.4 s on two WHOLE gold snapshot reads
(chatter_daily 58,300 rows; article_security_mention 23,691) for one security-day.

**Ruling:**
1. **c1 is recorded NOT MET for round 63.** The under-5-s bound stays the target and is NOT lowered to 12 s.
2. **One further memory-only act is SIGNED here: 10240 -> 1769.** The flat curve shows memory buys no latency, and 1769 is the setting
   every other route served at until 10:55Z today.
   - Condition 3 of this half is re-read AT 1769: overlay, thesis, peers and collected/chatter answer 200, with leg-1 counts
     unchanged.
   - Any miss puts memory back to 10240.
   - Same NEVER-2 discipline: one entry, with the read printed.
3. **Round-64 cell (RESAPP):** cut the cold read.
   - Read only the needed columns, plus a security filter, on both gold reads (by row-group statistics or an index keyed by
     security, whichever the producer's layout allows).
   - Lambda segment timings are printed per stage.
   - c1 is re-graded against the same 5-s cold bound, with Init Duration proven.
