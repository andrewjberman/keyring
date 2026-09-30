# AMGT_HARVST task order -- `HVST-ab-1` -- ROUND 29 chain 1: THE LIVE wsj PATH READS A HIT'S `timestamp`, `p-2`'s TEST DESCRIBES THE HOLD, AND `bbg:NM5NLQ6K50XZ01` IS SEEDED INTO THE HOLD (FWD-7, FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ab-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~81</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; no collection run in this cell.
comp-iam: RUN at L5 -- no network: sockets blocked in every test and script. NO vendor call, NO S3 write. ONE local write: the seed row in the runtime progress.sqlite3 rejected_hold table.
comp-adversary: RUN at L5 -- the adversary is a date read that widens reach beyond what the page showed, or a paging change nobody named. AC1 plants the live span from the hits' own dates and the backfill bound-stop on dated wsj hits, each with a mutant.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO REQUEST TO ANY PUBLISHER, NO S3 WRITE, NO COLLECTION RUN.** Sockets are blocked in every test and script (assert it).
2. The runtime root `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest` is READ-ONLY except for ONE
   act: the seed in section 1 change 3. It writes one row to the `rejected_hold` table in `progress.sqlite3` and nothing else.
3. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~81/scripts/`; outputs named `ab1_*`.
4. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~81/AMGT_HARVST.TO-HVST-ab-1.live-wsj-reach-and-hold-seed.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-ab-1.live-wsj-reach-and-hold-seed`.

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/test_p2_fetched_and_stored_keys.py
lib/opal_data_harvest/test_ab1_live_reach_and_seed.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~81/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CHANGES (`ledger/ROUND_ANALYSIS.round28.md` section 4 item 1, ruling 4)

**Measured:** the recorded wsj listing pages carry 30 hits. All 30 have `timestamp` (e.g. `2026-09-23T09:30:00Z`) and
`printPublicationDate`. `publishers._hit_date` (`_HIT_DATE_KEYS`, ~:145) reads neither, so it dates 0 of the 30, and a
LIVE wsj job's `reached_span` is only a `stop_bound` (row `Z-W76-S1`). `worker._cached_hit_date` (~:62) reads both, but
only for cached pages.

1. **The live wsj date read.**
   - `_hit_date` also reads `timestamp`, then `printPublicationDate`, after its current keys.
   - A live wsj job's `reached_span` then comes from its hits' own dates, basis `listing_dates`.
   - **The named paging change (issuer ruling):** `_stop_paging` reads `_hit_date` too. A wsj backfill now stops
     `older_than_bound` on a page whose hits all predate the floor. Before, an undated wsj page paged to `max_pages`.
     This change is intended: it spends fewer pages.
   - Nothing else changes for any other publisher's hits.
2. **`p-2`'s test describes the hold.** In `test_p2_fetched_and_stored_keys.py`, the case that asserts a rejected key is
   re-fetched every run (`test_p2a_the_rejected_key_is_still_refetched_each_run...`, ~:78-98) is re-pointed. It keeps the
   legacy no-client arm as it stands, and adds the harvest-mode arm: two same-day runs fetch the rejected key ONCE. Its
   "ACCEPTED LIMIT" docstring is corrected (row `Z-W76-S2`).
3. **The seed.** `bbg:NM5NLQ6K50XZ01` was rejected before `rejected_hold` existed. It is seeded through the hold's OWN
   rule, not a hand-typed row:
   - `failed_days` and `last_failed_day` are derived from its recorded body rejections in the runtime `events.jsonl`;
   - `state` follows `HOLD_FINAL_AFTER_DAYS`;
   - a seed script runs it ONCE and prints the table row before and after;
   - a second run is a no-op that prints the same row.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ab-1"><invocation>python -m pytest lib/opal_data_harvest/test_ab1_live_reach_and_seed.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-ab-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~81/scripts/ab1_ac2_seed_and_replay.py</invocation><expect>NETWORK CALLS MADE: 0</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-ab-1"><invocation>python -m pytest lib/opal_data_harvest/ -rA --tb=line</invocation><expect>passed</expect></criterion>
</proof_of_spec>

**What each criterion must prove or print:**
- **AC1** asserts each of these; a mutant restoring each base behaviour fails:
  - (a) a LIVE wsj listing page's hits (the recorded pages' shape) yield `reached_span` equal to their own date bounds,
    with basis `listing_dates`;
  - (b) a wsj backfill with floor `2026-01-01` stops `older_than_bound` on a page whose hits all carry a `timestamp` before
    the floor;
  - (c) a page mixing dated and undated hits does NOT bound-stop;
  - (d) a bbg harvest-mode job with the seeded hold makes no request for that key.
- **AC2:** the seed (section 1 change 3) against the runtime root, then a replay of `q-1`'s recorded bbg and wsj job shapes
  through the new code on stubs. Print:
  - the seed row before and after;
  - the live-shaped wsj `reached_span`;
  - that `bbg:NM5NLQ6K50XZ01` is HELD (not fetched);
  - the line `NETWORK CALLS MADE: 0`.
- **AC3:** the base is commit `6caac02338`, pinned. Print the base and after pass counts. No test that passed at the base
  fails.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round28.md` @`c907537920` section 4 item 1, ruling 4.
- **The paging change is the issuer's ruling on row `Z-W76-S1`'s note** ("a decision, not a rider"). A wsj backfill that
  stops at the floor serves Andrew's quota word. `HVST-ab-3`'s pre-run print is measured on this code.
- **The seed's reach, stated plainly:** the runtime `events.jsonl` records the key's body rejection on 2026-09-30 only (2
  fetches with status 200, then 1 with status 403). By the hold's own rule, a seed with that history holds it on that day
  and retries it on a later day.
  - Batch 1 (`HVST-ab-3`) has no Lenovo job, so its listings cannot name this key.
  - A later Lenovo bbg job re-meets it; that is the hold's designed retry, not a defect.
- The `<expect>`s are plain printed tokens.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>29</round>
<slot>~81</slot>
<fabric>site-z</fabric>
