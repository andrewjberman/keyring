# L4-R ratified-text review -- AMGT_HARVST v0.7 @0e6467847a (CONTRACTS only)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~10:2xZ - **Asked by:** CTO~Z msg 27084
**Span:** from this seat's own signed bytes (v0.6 @`803ea38a9e`) to `0e6467847a`. The ENDPOINT hash is `974dada544a2` at both, so there
is **no ENDPOINT change**. The diff is one hunk, in `C-HV-RANK-DECLARED-SET`.

## THE CHANGE

- **Exit** is now "refused for the whole universe OR ran no UNIVERSE-SCOPE job".
- A universe-scope job is "a run record whose target securities are the generation's universe".
- A per-name trial neither adds a publisher nor keeps one in.
- The census prints, per excluded name, the declared publishers it lacks. That is this seat's v0.6 note 1, adopted.

## CHECKS

1. **Decidable from the records as they exist.** This seat read the persisted run record
   `amgt/harvest/bronze/run_record/date=2026-09-30/20260930T084110Z-run-4ee47491.json`.
   - It carries `jobs[]`, each with `publisher` and `security_key` (here 2 jobs, `992_HK_Equity`), and `retrieval_mode` `backfill`.
   - A record's target set is therefore readable, and "target securities == universe" can be computed.
2. **Consistent with the grounds.** The partial-rank research @`784068f4c0` found no estate surface that withholds a whole product
   for one incomplete member. v0.6's trial-binds-universe consequence contradicted it, and v0.7 removes that.
3. **Today's reading:** no publisher has a universe-scope job in the window, so the declared set is empty, and the rank HOLDs with
   `NO_DECLARED_PUBLISHER` (the v0.6 branch). This agrees with the census's 0 of 191.

## VERDICT: SIGN

**One note for the round-28 analysis, not a condition.** The definition is per RUN RECORD. A universe backfill executed in batches,
several run records each covering a slice, never qualifies under "a run record whose target securities are the universe". Capped
calls are normal here: the y-4 derive refused a single 97-name call.
- Either the backfill is contracted to write one run record for the whole universe;
- or the test reads the UNION of that publisher's run records in the window against the universe.

Round-28 cell 4's plant ("a universe-scope run enters") should use whichever form the backfill will actually take.
