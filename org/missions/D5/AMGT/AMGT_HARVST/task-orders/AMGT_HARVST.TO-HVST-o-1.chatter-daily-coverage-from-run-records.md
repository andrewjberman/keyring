# AMGT_HARVST task order -- `HVST-o-1` -- ROUND 25 chain 1 of 4: `chatter_daily` COVERAGE FROM THE COLLECTOR'S RUN RECORDS -- a name-day searched reads SEARCHED, a name-day never searched reads DENIED (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-o-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~61</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the harvest collector's Scheduled Task is Disabled with 0 triggers (read 2026-09-30 03:3xZ); `build_daily` has no scheduled writer. This cell runs no collection and writes nothing served.
comp-iam: RUN at L5 -- S3 GET/LIST on the harvest prefixes for the in-memory before/after only. NO PUT, NO DELETE, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is coverage that turns "not searched" into SEARCHED: a span invented for a job that reports no reach, a failed job counted as a search, or a run record from one security crediting another. AC1 plants each of those and requires DENIED.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL, NO COLLECTION RUN, NO S3 WRITE OR DELETE, NO DEPLOY.** Every proof runs over recorded fixtures, a
   temp-dir runtime root, or an in-memory store stub. The real S3 read in AC2 is GET and LIST only.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~61/scripts/`; outputs named `o1_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~61/AMGT_HARVST.TO-HVST-o-1.chatter-daily-coverage-from-run-records.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-o-1.chatter-daily-coverage-from-run-records`.
4. **Shared file.** `lib/research/harvest/publication_gold.py` is also named by `HVST-o-3`. In it, you own ONLY
   `publisher_coverage`, `daily_rows`'s coverage handling, `build_daily`, and any new helper you add ABOVE
   `publisher_coverage`. You do NOT touch `_iter_latest_articles`, `_latest_articles_for_keys` or
   `_latest_gold_snapshot_rows*`, which belong to `HVST-o-3`.

<paths>
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/test_o1_run_record_reach.py
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_publication_gold_daily.py
lib/research/harvest/tests/test_o1_run_record_coverage.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~61/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/CTO_RULING_ROUND24_N4_HOLD_GRAMMAR_FLAG_SILVER_TIE_20260930.md` @`5998e71f23`, ruling 1)

**Measured last round:**
- The chatter producer's `gold` branch fails with `INCOMPLETE_GOLD_INPUT` and resolves 0 of 191 security windows.
- Gold `chatter_daily` reads `no_coverage` on 5,675 of 5,730 day-reads, and all 191 names read `DENIED` on 09-29.
- Today coverage comes ONLY from listing hits (`publication_gold.publisher_coverage`, ~:554). So a name that was searched
  and returned nothing reads exactly like a name never searched.
- The guard is right and is NOT changed. The fix is in the coverage the gold table records.

**The change:**
1. **The run record says what each job searched.**
   - Today the collector writes one run record per collection (`worker.py` `write_run_record`, ~:406), to
     `<runtime root>/run_records/<run_id>.json`.
   - Extend it, going forward: each job entry gains the security, the publisher, its status, and the date span its
     listings REACHED. The span runs from the oldest date reached to the fetch date. When no dated listing is reached,
     the span is the bound the job stopped at, recorded as such.
   - The run record is also persisted beside bronze, when a harvest client is present, through the harvest store's
     EXISTING key builder (`lib/research/harvest/store.py`: `table_prefix` and its siblings). No hand-typed prefix.
     Write it never-overwrite, as bronze is written.
   - You own `worker.py`'s run-record code only. `store.py` is read, not edited. If a builder you need is missing, file a
     row and use the nearest existing one.
2. **`build_daily`'s coverage reads the run records** as well as the listing hits:
   - a name-day inside a SUCCESSFUL job's reached span reads SEARCHED, with that publisher in its covered set, even with
     zero articles;
   - a job that failed, was challenged or was denied covers nothing;
   - a name-day no job reached stays DENIED;
   - a run record without the new span field (written before this change) contributes nothing new. The listing-hit
     spans still apply.

   The `data_status` class names and the schema's columns are unchanged. Only which days count as covered moves.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-o-1"><invocation>python -m pytest lib/opal_data_harvest/test_o1_run_record_reach.py lib/research/harvest/tests/test_o1_run_record_coverage.py lib/research/harvest/tests/test_publication_gold_daily.py -rA --tb=line</invocation><expect>all pass, with the pass count printed; the new tests plant (a) a successful job with zero articles whose days read SEARCHED, (b) a failed job and a challenged job whose days stay DENIED, (c) a run record for security A that leaves security B DENIED, (d) a pre-change run record with no span field that adds no coverage; a mutant counting a failed job as SEARCHED fails at least one test</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-o-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~61/scripts/o1_ac2_coverage_before_after.py</invocation><expect>over the 191 covered names (denominator printed) and the served window, the coverage distribution (COMPLETE / PARTIAL / DENIED name-days, and per publisher) BEFORE (the merged-base rule) and AFTER (this rule) side by side, built in memory from the served mention snapshot, listing hits and every run record found in S3 and in the local runtime root (counts printed, a zero named as a zero); and the chatter producer's gold branch RESOLVED count on the same window before and after, run in memory with no write</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-o-1"><invocation>python -m pytest lib/opal_data_harvest/ lib/research/harvest/tests/ -rA --tb=line</invocation><expect>no test that passed at the base fails (base and after pass counts printed)</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

It does not relax the guard, does not flip `CHATTER_AXIS_SOURCE`, writes no gold snapshot, and runs no collection. A
served `chatter_daily` rebuild on this rule is a later paired order.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
- From `ROUND_ANALYSIS.round24.md` @`6c5b4339a1` s.4 item 1, and ruling 1 @`5998e71f23`.
- **AC2 is expected to move little or nothing on real data.** No collection has run since `n-1` merged: the Scheduled
  Task is Disabled, and run records are local-only until this cell persists them. The number that moves is the one
  `HVST-o-5`'s Lenovo run feeds.
- Stating a zero is correct here; the served rebuild is cut after `o-5` lands.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>25</round>
<slot>~61</slot>
<fabric>site-z</fabric>
