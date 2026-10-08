# AMGT_HARVST task order -- `HVST-bk-1` -- ROUND 66 (`1.0.0_SA_CTO~Z` msg 31613, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 3 @f7ad546af4): ARTICLES COLLECTED PER SOURCE PER DAY OVER 90 DAYS, FROM WHAT IS ALREADY HELD -- AND THE DAY EACH SOURCE THINNED; NO PUBLISHER IS CALLED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~116</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL scripts and records, plus a READ-ONLY census (S3 GET of the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a census with no printed denominator, a sample the script grades, a source substituted for a refused read, or a gold build.
</preflight>

## 0. THE CELL

The Security Analysis page shows a covered company its last 30 days of harvested articles. A reviewer read the served
silver (19,159 latest articles): only 714 were PUBLISHED from 2026-09-09 to 2026-10-08 (bbg 288, sa 207, barrons 162, wsj
52, ft 5), and none names Caterpillar, CSL or AIG, so three covered companies show an empty panel
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND65_FEED_WALK_GRADE_20261008.md` @96206b0d29; row AMGT_HARVST-Z-S103). The panels are faithful to what is held; what is held is thin. Nobody has
measured WHEN it thinned, per source.

The ruling: read it first, from what is ALREADY HELD only -- bronze, silver and the collector's own run records. **No
publisher, vendor or search host is called to find out what was missed.**

Where to read (all S3 GET or list, no put): silver articles through `lib/research/harvest/publication_gold.py`
`_iter_latest_articles()` (each row carries its publisher, `published_utc` and the stored fetch fields; print which fields
you used); the collector's run records through `publication_gold._iter_run_records()` (each run's `started_at`,
`finished_at` and `jobs[]` with `publisher`, `status`, `keys_fetched`); bronze through `lib/research/harvest/store.py`
(read the module for how bronze article objects are addressed and list them; count objects per source per day of the stamp
in the key). The five sources are bbg, wsj, barrons, sa, ft.

## 1. THE BUILD (read-only)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~116/bk1_per_source_per_day.py`. The window is the 90 days ending today UTC. Print a progress line every 2,000 rows.
2. It prints `DENOMINATOR: silver articles <N>, run records <R>, bronze objects listed <B>, window <start> to <end>` and
   which field gave each day (with the count of rows that lacked it).
3. Three tables, each source by day, written to `BK1_PER_SOURCE_PER_DAY.md` and `.json` beside the script and summarised in
   the output by WEEK (13 rows per source, Monday-start, so the output stays readable):
   - (A) silver articles by PUBLISHED day;
   - (B) silver articles by the day they were FETCHED (collected);
   - (C) run records by the day they finished: runs, jobs, jobs by status, and keys fetched;
   - (D) bronze objects by the day in their key, if bronze is addressable by day; if it is not, say so and why.
4. Per source, ONE mechanical line for table (A) and one for table (B):
   `<source> (A): 90-day total <t>, median per day over days 31 to 90 <m>, per day over the last 30 days <l>, THINNED ON
   <the first day after which the trailing 7-day mean stayed below half of <m> to the end of the window, or NEVER>`.
   State that rule in the md. It is a description of the counts, not a verdict on the cause.
5. Per source, from table (C): the first and last day a run for it finished in the window, and the days with no finished
   run. The collector has been run as a per-security backfill (one job per security per source), not as a daily sweep:
   say for each source whether its run records show a daily sweep, a backfill pass, or both, quoting the fields you read.
6. `IN-WINDOW ARTICLES NAMING: Caterpillar <a>, CSL <b>, AIG <c>, Nokia <d>` over silver published in the last 30 days (a
   case-insensitive name search of title and blocks; `CSL` counted as `CSL Limited`, `CSL Ltd`, `CSL Behring`, `Seqirus`),
   as a check against the reviewer's 0, 0, 0 and 7.
7. Last line: `CENSUS OK` only if N > 0, R > 0, tables (A), (B) and (C) each printed five sources, and every source printed
   its THINNED lines. Otherwise `CENSUS FAIL` and the failing condition. Write the output as `bk1_per_source_per_day.out`.
8. A read that is refused or returns 0 rows is a FINDING: print it whole, file a row, do not substitute a source. Change no
   product file. Do not read `.runtime`.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/store.py
lib/opal_data_harvest/harvest_grammar.py
org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND65_FEED_WALK_GRADE_20261008.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~116/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bk-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~116/bk1_per_source_per_day.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bk-1" judgment="true"/>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W116-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~116/AMGT_HARVST.TO-HVST-bk-1.articles-collected-per-source-per-day.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bk-1.articles-collected-per-source-per-day`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31613, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 3 @f7ad546af4. Decomposition section 80.
- R14: "Round 66's first cell reads, from bronze, silver and the collector's own run logs only, the articles collected per
  source per day over 90 days, and names the day each source thinned. No publisher is called to find out what was missed: that
  is a vendor use with no word of Andrew's." Row Z-S103.
- **Issuer rulings inside the decomposition** (no gate limb graded them): "thinned" is given one mechanical definition (the
  trailing 7-day mean staying below half the earlier median) so two readers get one day; the run logs are read from the run
  records the collector uploads, not from `.runtime`, which a worktree does not carry. AC2 is the reviewer's read of whether
  the thinning is a collection gap.
- Chain of one, slot ~116. **Checks dry-run at the base:** AC1 base FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>66</round>
<slot>~116</slot>
<fabric>site-z</fabric>
