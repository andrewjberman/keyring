# AMGT_HARVST task order -- `HVST-n-1` -- ROUND 24 chain 1 of 5: THE COLLECTOR KEEPS THE RECEIVED BYTES, LINKS THE LISTING OBJECT, RECORDS RANK AND PAGE FOR EVERY PUBLISHER, AND WRITES A RUN RECORD (FWD-1, FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-n-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~56</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on lib/opal_data_harvest/ or the harvest prefixes; this cell runs no collection and deploys nothing.
comp-iam: RUN at L5 -- no new AWS call at run time in this cell; every proof runs over RECORDED FIXTURES and an in-memory or temp-dir store. NO PUT to S3, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a "no re-fetch" proof that counts nothing (a stub whose counter never increments passes every zero), or a stored "as received" body that is really the rebuilt record. AC2 plants a NEW key that must fetch exactly 1; AC1 requires the stored received body to be byte-equal to the fixture's raw response, not to the rebuild.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL, NO S3 WRITE OR DELETE, NO COLLECTION RUN, NO DEPLOY.** Recorded fixtures stand in for every
   publisher. Use the ones under the collector's tests where they exist, and add small recorded fixtures of your own
   under the tests path where they don't.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~56/scripts/`; outputs named `n1_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~56/AMGT_HARVST.TO-HVST-n-1.collector-keeps-received-bytes-and-provenance.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-n-1.collector-keeps-received-bytes-and-provenance`.

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/storage.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/__main__.py
lib/opal_data_harvest/test_bronze_capture.py
lib/opal_data_harvest/test_retrieval_provenance.py
lib/opal_data_harvest/test_worker.py
lib/opal_data_harvest/test_n1_received_bytes_and_run_record.py
lib/research/harvest/store.py
lib/research/harvest/tests/test_store.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~56/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULINGS (`ledger/ROUND_ANALYSIS.round23.md` @`d1ec6f4118`, s.2 rulings 1 and 3)

**Measured last round:**
- 104 of 126 bronze objects are `normalised_record` rebuilds, so the publisher's original bytes are not stored.
- No article records the listing object that found it (0 of 120).
- Search rank and page are recorded only for sa and wsj.
- No run record exists, so "a second run the same day fetches no article we already hold" cannot be exercised.

**The change, going forward only** (the 104 existing rebuilds stay, labelled for what they are; no re-fetch):
1. The collector (`lib/opal_data_harvest/`: `publishers.py`, `worker.py`, `storage.py`, `transport.py`, `uploads.py`, `__main__.py`; NOT `silver_from_bronze.py`, which is `HVST-n-2`'s; bronze metadata in
   `lib/research/harvest/store.py`) stores each response body **AS RECEIVED**, beside its rebuild, with its own recorded
   hash.
2. Every stored article **links the listing object that found it** (a field naming that listing object's key).
3. **Result rank and page** are recorded for every publisher's discovery, not only sa and wsj.
4. Each collection **writes a run record**: run id, start, keys fetched, keys skipped as already held.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-n-1"><invocation>python -m pytest lib/opal_data_harvest/ lib/research/harvest/tests/test_store.py -rA --tb=line</invocation><expect>the suites pass with new tests NAMED in the -rA output: for each of the five publishers, a recorded fixture response is stored AS RECEIVED byte-equal to the fixture's raw bytes (not to the rebuild) with its recorded hash, beside the rebuild; every stored article carries the key of the listing object that found it; rank and page are recorded for every publisher's discovery; the pass count BEFORE and AFTER printed and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-n-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~56/scripts/n1_ac2_counting_stub.py</invocation><expect>TWO SAME-DAY RUNS through the collector with a COUNTING stub transport over recorded fixtures and a temp-dir store: run 1 fetches every fixture article (count printed); run 2 fetches 0 for already-held keys; a planted NEW key in run 2 fetches exactly 1; each run writes a run record with keys fetched and keys skipped, both printed. PASS only if held = 0 and new = 1</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-n-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~56/scripts/n1_ac3_existing_objects_unchanged.py</invocation><expect>the change is going-forward only: reading the served bronze objects' metadata (S3 GET/LIST only) through the NEW store code classifies the 126 existing objects exactly as before (104 normalised_record, 16 as_received, 6 unlabelled at the round-23 reading, or the current counts with any difference explained), and no existing object is re-labelled as received bytes</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No live collection, no re-fetch of the 104 originals, no vendor call, no S3 write, no deploy, no silver rebuild.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **From `ROUND_ANALYSIS.round23.md` @`d1ec6f4118` s.3 item 1.**
2. **FWD-1's DONE WHEN ("one run on the validation security, every article from each of the five publishers") is
   exercised on the next LIVE collection.** That is a vendor act under the harvester's scripted grant, and Seeking
   Alpha's leg waits on the renewal. It is not this cell.
3. **`lib/opal_data_harvest/` is in the scoped API's build closure** (the build script names it). A later scoped-API HEAD
   build carries these files, and that deploy's pair must trace them, as for `j-1`/`k-1`/`l-1`
   (`CTO_RULING_YY5_CLOSURE_HARVST_INERT_20260930.md`).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>24</round>
<slot>~56</slot>
<fabric>site-z</fabric>
