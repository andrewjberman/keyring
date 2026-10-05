# AMGT_HARVST task order -- `HVST-at-1` -- ROUND 47 CHAIN A (round-46 analysis ruling 1; row Z-S86; CTO @7cd62976f1): ONE LISTING SILVER APPEND PER SOURCE PER PASS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-at-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~95</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants with a stub S3 client. NO network, NO S3 call, NO upload, NO collector run. A collection run is LIVE on this machine: never run `upload-harvest`, the collector or the backfill driver, and never touch any `.runtime` directory.
comp-adversary: RUN at L5 -- the adversary is a batch that changes a silver ROW (only the parquet object count may differ), a batch whose object name sorts BEFORE a part it supersedes (newest-wins breaks), one untableable row failing the whole pass, a per-row loop reintroduced on failure, or an outbox status that disagrees with what was written.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/uploads.py`, `HarvestUploader._run_listings`:
- Bronze stays one object per listing page.
- The silver append is grouped by `(source, run_stamp)`, with ONE `_silver_append_retrying_object_name(...)` call per group
  (around line 378). `store.silver_append` reads `silver_latest` over the WHOLE prefix on every call.
- So a pass that uploads N listing pages with distinct per-page `fetched_at` stamps reads the whole `listing_hit` prefix N times.
- Measured on site Z (row Z-S86): sa's listing upload drains about 0.6 pages a minute, and the cost grows with what is already
  stored.

The ARTICLE path in the same file was fixed for exactly this in HVST-ai-5 (row Z-S58): see the comment block around line 277
and `_land`.
- ONE silver_append per SOURCE per pass.
- Every silver row keeps its own `run_stamp` field; only the object-name stamp is shared, the greatest of the batch.
- A row that cannot be tabled (alone, or against its date group) is isolated LOCALLY first (`_isolate_bad_silver_rows`) and
  left pending, with no S3 call.
- A failure of the one append marks the whole batch pending, never a loop back to per-row calls.

## 1. THE BUILD (LOCAL; stub client only)

1. **Apply the article path's rule to `_run_listings`:** ONE `_silver_append_retrying_object_name` call per SOURCE per pass, for
   table `listing_hit`, with the same record-key fields as today, at the greatest `run_stamp` of the source's batch.
   - Isolate untableable listing rows locally first, the same way, and leave them pending with `SilverRowError`.
   - A failed append pends the whole batch, with no per-row loop.
   - Bronze puts and outbox bookkeeping are unchanged per page.
2. **Rows are identical:** for the same pending pages, the silver ROWS written (every column, including each row's own
   `run_stamp` and `record_hash`) are identical to the old path's. Only the number and names of parquet objects differ.
3. **Newest-wins holds:** the batch's object name `part-<max run_stamp>[-rN].parquet` sorts at or after every part a row in it
   supersedes, by `store.part_order_key` and `store.supersedes`.
4. **Plants** in `lib/opal_data_harvest/test_at1_batched_listing_upload.py`, with a stub S3 client and a temp sqlite outbox, no
   network:
   - (i) rows identical, old against new, on a planted set of listing pages with distinct `fetched_at` seconds;
   - (ii) `silver_latest` prefix reads = 1 per source per pass on the new path, and N on the old;
   - (iii) one untableable row is isolated and pending, while the rest upload;
   - (iv) a failing append pends the batch and makes no per-row retry;
   - (v) a mutant that restores per-group appends fails (ii).
5. **The timing control** is
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~95/at-1.timing_control.py`:
   - it drives `_run_listings` over the SAME 100 planted listing pages, old path against new, against a stub client whose
     `listing_hit` prefix already holds about 1,000 parts;
   - it prints `silver prefix reads: old <N> new <M>`, `wall seconds: old <a> new <b>`, `rows identical: <bool>`, and
     `AC2 RESULT: PASS|FAIL`;
   - PASS requires new reads == 1 per source, old > new, and rows identical.
   Keep the old path callable for the control only (for example, a private flag or a copied function in the control script), not as
   a production switch.
6. The collector suite stays green: `python -m pytest lib/opal_data_harvest -q`. Report the count.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r47-95`, branch `wk-AMGT_HARVST-95-r47a`, cut from CLOUD at the issuance commit
(sparse cone, decomposition section 50).

<paths>
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/test_at1_batched_listing_upload.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~95/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-at-1"><invocation>python -m pytest lib/opal_data_harvest/test_at1_batched_listing_upload.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-at-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/checks/at-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~95/AMGT_HARVST.TO-HVST-at-1.batched-listing-upload.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-at-1.batched-listing-upload`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-46 analysis @585391af7f ruling 1 and enrichment item 1; CTO ruling @7cd62976f1; decomposition section 60.
It lands through at-2: every leg is stopped by its stop file before the merge (no harvest code lands while a leg runs), then
each leg is resumed from its own checkpoint as the same run.

**COMPLETE 2026-10-05 ~07:2xZ (issuer):**
- **Built:** worker ~95 @7d2166a180 + @a567807afa.
- **Landed:** with at-4 through at-2 on the CTO's word @08580b1fd6 + ADDENDUM @ff4e31bcd0, merge @23baacf0e1 (11 files, dropped 0,
  foreign 0).
- **AC1 PASS:** 8 of 8.
- **AC2 PASS:** silver prefix reads, old 100 against new 1; wall time 84.04 s against 0.91 s; rows identical, 200 of 200.
- **Suites on CLOUD after the landing:** research harvest 342 passed; collector 655 passed, 3 skipped. Before the landing, the
  integration branch also passed management 142, and corpus 475 with 1 pre-existing failure identical on CLOUD.
- **Legs:** bbg and wsj stopped by their stop files and were resumed 07:25:46Z from their own checkpoints (169 and 148 pairs
  planned = 191 - 22 and 191 - 43). sa resumes when its driver exits from its old-path upload.
- **Rows:** Z-W95-S1 (column rounds); Z-W95-S2 (first-row columns), disarmed by at-4.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>47</round>
<slot>~95</slot>
<fabric>site-z</fabric>
