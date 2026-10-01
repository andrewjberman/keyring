# AMGT_HARVST task order -- `HVST-p-2` -- ROUND 26 chain 2 of 4: FWD-3's TWO OWED ROWS -- why `bbg:NM5NLQ6K50XZ01` was fetched and never stored, and why wsj keys an article by URL in the run record and by UUID in the outbox (FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-p-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~67</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector's Scheduled Task is Disabled with 0 triggers; this cell runs no collection.
comp-iam: RUN at L5 -- local reads of the collector's runtime root (read-only) and S3 GET/LIST. NO vendor call, NO S3 write, NO collection run, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a cause guessed from code without the recorded evidence, or a "fix" that makes the ledgers agree by dropping the key that disagrees. AC1 replays each case from the recorded run artifacts through the real code path; AC2's fix is proved on a fixture reproducing the recorded shape, with a mutant.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL, NO COLLECTION RUN, NO S3 WRITE, NO DEPLOY.**
   - The runtime root `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest` is READ-ONLY for you. Copy
     what you need into your deliverables.
   - Recorded files you may read: `progress.sqlite3`, `events.jsonl`, `runs/*.json` and `run_records/*.json`.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~67/scripts/`; outputs named `p2_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~67/AMGT_HARVST.TO-HVST-p-2.fwd3-never-stored-fetch-and-wsj-key-split.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-p-2.fwd3-never-stored-fetch-and-wsj-key-split`.

<paths>
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/storage.py
lib/opal_data_harvest/test_p2_fetched_and_stored_keys.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~67/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE TWO QUESTIONS (`ledger/ROUND_ANALYSIS.round25.md` @`300ea99310`, ruling 3; `o-5` CTO half AMENDMENT 2)

**Recorded (HVST-o-5, 2026-09-30):**
- **(a) The never-stored fetch.** Run 1 `20260930T044003Z-run-b75f9299` lists `bbg:NM5NLQ6K50XZ01` among `keys_fetched`. It has
  NO row in `harvest_raw_outbox`, and run 2 `20260930T045332Z-run-75d4c464` fetched it again.
  - The other 10 of run 1's 11 bbg keys were stored.
  - The run record writer is `worker.py` `write_run_record` (~:406); the outbox writer is `_write_harvest_raw` (~:147).
- **(b) The key split.** Run 1's run record keys wsj articles by URL (`wsj:https://www.wsj.com/...`). The outbox keys the same
  articles by UUID (`wsj:0ec5b5a0-...`). So the two ledgers cannot be joined by key for wsj, although they can for bbg.

**For each question, measure and then act:**
1. **The cause**, traced from the recorded artifacts through the code path, with file:line.
2. **The fix, or an accepted limit with its reason.**
   - A SILENT loss on the collection path is FIXED, not accepted. If the fetch was rejected on purpose (a non-article, a failed
     body check), the fix is that the run record says so: the key is counted as rejected, not as fetched.
   - For the key split, one key space across both ledgers, or a recorded join the next reader can use. Choose the smaller
     change and say why.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-p-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~67/scripts/p2_ac1_causes.py</invocation><expect>for (a) and (b), the recorded evidence printed (the run-record entries, the outbox rows or their absence, the events.jsonl lines for the key, with counts and denominators: run 1's 22 fetched keys each classified stored / not stored) and the cause named by file:line on the code path those artifacts went through</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-p-2"><invocation>python -m pytest lib/opal_data_harvest/test_p2_fetched_and_stored_keys.py -rA --tb=line</invocation><expect>all pass, with the pass count printed; a fixture reproducing (a)'s recorded shape shows the run record no longer counts a never-stored key as fetched (or the stated accepted limit is asserted instead), and a fixture reproducing (b)'s shape shows a wsj article's run-record key and outbox key join; a mutant restoring either base behaviour fails at least one test</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-p-2"><invocation>python -m pytest lib/opal_data_harvest/ -rA --tb=line</invocation><expect>no test that passed at the base fails (base and after pass counts printed; the base is commit b635dadc66, pinned at cut -- never merge-base)</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

It runs no collection, calls no vendor and changes no S3 object. The next collection run on the merged code exercises the fix.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
- `ROUND_ANALYSIS.round25.md` s.4 item 2.
- **Ruling 2 (check base pinned at cut) is applied:** the base is pinned to `b635dadc66`, whose lib/ equals the issuance commit.
- **Write set.** `worker.py` is also read by `HVST-p-3`'s act. `p-3`'s pair pins its code at signing, so this cell's merge
  does NOT reach `p-3`'s run unless `p-3` is re-signed after it. The issuer orders `p-3`'s run on the signed pin.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>26</round>
<slot>~67</slot>
<fabric>site-z</fabric>
