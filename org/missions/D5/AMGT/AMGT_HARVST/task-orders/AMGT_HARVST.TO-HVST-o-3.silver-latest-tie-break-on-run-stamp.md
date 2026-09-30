# AMGT_HARVST task order -- `HVST-o-3` -- ROUND 25 chain 3 of 4: ON EQUAL `fetched_at`, THE ROW FROM THE LATER PART'S `run_stamp` WINS -- in EVERY newest-wins silver reader (FWD-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-o-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~63</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no scheduled writer of harvest silver (the collector's Scheduled Task is Disabled, 0 triggers). This cell changes readers only and writes nothing served.
comp-iam: RUN at L5 -- S3 GET/LIST on the harvest silver prefixes for AC2's served-tie census and body check. NO PUT, NO DELETE, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a tie-break fixed in `store.silver_latest` while a SECOND reader keeps the old rule, so the page and the builder disagree on which row is current. AC2 prints the census of every newest-wins silver reader with its file:line, and AC1 plants the tie through each one.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY.**
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~63/scripts/`; outputs named `o3_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~63/AMGT_HARVST.TO-HVST-o-3.silver-latest-tie-break-on-run-stamp.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-o-3.silver-latest-tie-break-on-run-stamp`.
4. **Shared file.** `lib/research/harvest/publication_gold.py` is also named by `HVST-o-1`. In it, you own ONLY the
   silver readers: `_iter_latest_articles`, `_latest_articles_for_keys`, and their private helpers. You do NOT touch
   `publisher_coverage`, `daily_rows` or `build_daily`, which belong to `HVST-o-1`.

<paths>
lib/research/harvest/store.py
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_store.py
lib/research/harvest/tests/test_timeline_day_read_path.py
lib/research/harvest/tests/test_o3_silver_tie_break.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~63/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/CTO_RULING_ROUND24_N4_HOLD_GRAMMAR_FLAG_SILVER_TIE_20260930.md` @`5998e71f23`, ruling 3)

**Measured:**
- `store.silver_latest` (`lib/research/harvest/store.py` ~:344-364) keeps a row only when its `fetched_at` is strictly
  newer.
- Last round's `silver_from_bronze` change rebuilds 5 served sa rows that keep their bronze `fetched_at`. Appended in a
  later part, they would TIE and be read as the old rows, so a rebuild could never supersede them.
- `publication_gold._latest_articles_for_keys` (added last round for `/timeline/day`) copies the same rule: "ties go to
  the first part in listing order".

**The change:** in EVERY reader that picks the newest silver row per record key, ties on `fetched_at` go to the row from
the part with the LATER `run_stamp`, which is the `part-<run_stamp>.parquet` name `silver_append` writes. A strictly
newer `fetched_at` still wins as before.
- First find every such reader under `lib/` and print the list with file:line. It includes at least
  `store.silver_latest`, `publication_gold._iter_latest_articles` and `publication_gold._latest_articles_for_keys`.
- Change every one to the same rule. Prefer one shared comparator in `store.py` that the others call.
- A reader outside these paths is a row, not an edit.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-o-3"><invocation>python -m pytest lib/research/harvest/tests/test_o3_silver_tie_break.py -rA --tb=line</invocation><expect>all pass, with the pass count printed; for EACH newest-wins silver reader two plants: a same-fetched_at row in a LATER part is the one returned, and a same-fetched_at row in an EARLIER part is not; a strictly newer fetched_at in an earlier-stamped part still wins; a mutant reverting any one reader to first-in-listing-order fails</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-o-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~63/scripts/o3_ac2_readers_and_served_ties.py</invocation><expect>the census of newest-wins silver readers under lib/ with file:line and the pattern searched (denominator printed); over the SERVED silver of every source, the count of record keys whose newest fetched_at is tied across parts (a zero printed as a zero) and, for each tie, which row the old and new rule pick; and the /timeline/day body sha256 for AMZN_US_Equity 2026-09-07, HD_US_Equity 2026-08-18, 992_HK_Equity 2026-08-13 and 992_HK_Equity 2026-09-23 under the old and new rule, equal when no served tie touches them</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-o-3"><invocation>python -m pytest lib/research/harvest/tests/ lib/research/api/tests/test_timeline_routes.py -rA --tb=line</invocation><expect>no test that passed at the base fails (base and after pass counts printed)</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

It writes no silver. The paired served rebuild of the 5 sa rows and 6 new rows is `HVST-o-4`, which is cut after this
cell drains.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
- `ROUND_ANALYSIS.round24.md` s.4 item 3.
- The census widening, beyond `store.silver_latest` alone, is the issuer's: `n-6` copied the rule into
  `_latest_articles_for_keys`, so fixing one reader would split the page from the builder.
- `HVST-o-4` depends on this drain.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>25</round>
<slot>~63</slot>
<fabric>site-z</fabric>
