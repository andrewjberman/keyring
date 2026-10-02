# AMGT_HARVST task order -- `HVST-ai-5` -- ROUND 36 REPAIR (CTO msg 28222): ONE silver_append PER SOURCE PER UPLOAD PASS SO THE bbg OUTBOX DRAINS IN MINUTES, NOT HOURS (row Z-S58)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ai-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code + plants on a stub S3 client; the drain is the issuer's upload-harvest pass after the merge; no Secrets write; no gold write.
comp-adversary: RUN at L5 -- the adversary is a batch that writes a DIFFERENT row set than the per-row path (a row dropped, a value changed, a record_hash or run_stamp field rewritten), or one bad row that strands its whole batch. Plant 1 compares the two row sets key by key and value by value; plant 2 plants a type-conflict row.
</preflight>

## 0. THE CELL (CTO ruling msg 28222; row Z-S58)

The bbg outbox drain is too slow. `lib/opal_data_harvest/uploads.py` `HarvestUploader._run_articles` (lines ~172-260)
groups the due rows by `(source, run_stamp)`. A bbg `run_stamp` is the per-second `fetched_at`, so every group holds
ONE row, and every group makes its own `_silver_append_retrying_object_name` -> `store.silver_append` call.
`lib/research/harvest/store.py` `silver_append` calls `silver_latest`, which lists and reads EVERY part under the
source's silver article prefix (bbg: 576 parts, 69 MB). Each row therefore costs about 90 s and adds one more part.

`silver_append` already writes one part per fetch-date partition, and every silver row carries its own `run_stamp`
field, so grouping the rows by SOURCE keeps the row content.

## 1. THE BUILD (LOCAL), bounded by the ruling

1. In `_run_articles`, make ONE `_silver_append_retrying_object_name` call per SOURCE for the pass, not one per
   `(source, run_stamp)`. The object-name stamp for the batch is the greatest `run_stamp` in the batch. Each row keeps
   its own `run_stamp` value. The bronze put stays one object per article, unchanged. The outbox status updates and
   the result records stay per row, as now.
2. When the batched call raises `store.SilverRowError`, fall back to one call per row for that source's rows. The good
   rows land; the bad row stays pending with its error code, exactly as today.
3. Change nothing else: not `store.py`, not `silver_from_bronze.py`, not `LegacyUploader`, not `_run_listings`.
4. Plants in `lib/opal_data_harvest/test_ai5_batched_silver_append.py`, on the stub S3 client the suite already uses
   (see `lib/opal_data_harvest/test_retrieval_provenance.py` section 13 for a HarvestUploader on a stub):
   - (i) CONDITION: on ONE fixture of at least 5 rows of one publisher with distinct `fetched_at` seconds across at
     least 2 dates, the batched pass and the per-row path (the old grouping, run on a fresh stub) write the SAME row
     set. Compare every written silver row by `article_key`, and compare every column value, `record_hash` and
     `run_stamp` included. The part layout may differ; the rows may not.
   - (ii) the batched pass reads the silver prefix ONCE per source (count the stub's `list_objects_v2` pages or the
     `silver_latest` calls), where the per-row path reads it once per row;
   - (iii) one row whose nested field mixes int and str (the W91-S19 shape) does not stop the others: every other row
     is `uploaded`, and that row is `pending` with `SilverRowError`;
   - (iv) a mutant that restores the per-row grouping fails (ii).
5. The collector suite stays green: `python -m pytest lib/opal_data_harvest/ -q` (base 529 passed). That includes
   `test_retrieval_provenance.py::test_harvest_uploader_same_second_siblings_both_land`.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r36-90`, branch `wk-AMGT_HARVST-90-r36e`. Run every command from
that directory. Do NOT drain: the issuer merges, then runs the upload pass on the live bbg runtime in the main tree.

<paths>
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/test_ai5_batched_silver_append.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ai-5"><invocation>python -m pytest lib/opal_data_harvest/test_ai5_batched_silver_append.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ai-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round36/checks/ai-5.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 is graded by the ISSUER after the merge and the drain (the live outbox is in the main tree). Write the proof
  instance with AC1 run and AC2 marked "issuer-graded after drain", and leave `<status>` open.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-ai-5.batched-silver-append-per-source.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ai-5.batched-silver-append-per-source`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 28222 (YES, bounded, one condition: identical row set, plant 1). Carried as workstream
`bbgdrain` of round 36 (its own scope: the uploader's article grouping; disjoint from ai-2's ft files and ai-4's
silver_from_bronze.py). The one real run at close is the live drain reaching 0 pending (bar the W91-S19 row) with
gold-readable silver. Gold #4 stays on ruling 28084: before 13:00Z, and without the rest of the drain from 10:00Z.
Row Z-S58 is disarmed at the merge.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>36</round>
<workstream>bbgdrain</workstream>
<slot>~90</slot>
<fabric>site-z</fabric>
