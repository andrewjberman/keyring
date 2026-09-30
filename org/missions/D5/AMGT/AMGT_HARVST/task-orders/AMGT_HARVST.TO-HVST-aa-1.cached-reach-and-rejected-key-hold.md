# AMGT_HARVST task order -- `HVST-aa-1` -- ROUND 28 chain 1: A CACHED LISTING PAGE STILL RECORDS REACH (`from_cache`), AND A KEY REJECTED FOR ITS BODY IS HELD FOR THE REST OF THE UTC DAY (FWD-7, FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aa-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~76</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; no run in this cell.
comp-iam: RUN at L5 -- no network: sockets blocked in every test and script; the runtime root is read-only. NO vendor call, NO S3 write.
comp-adversary: RUN at L5 -- the adversary is a cached page credited with reach it never showed (a span invented beyond the page's own dates), or a hold that also swallows a key rejected for a transient reason. AC1 plants both: reach comes only from the cached page's own date bounds; only short_or_partial_body is held.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO REQUEST TO ANY PUBLISHER, NO S3 WRITE, NO COLLECTION RUN.** Sockets are blocked in every test and script (assert
   it). The runtime root `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest` is READ-ONLY.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~76/scripts/`; outputs named `aa1_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~76/AMGT_HARVST.TO-HVST-aa-1.cached-reach-and-rejected-key-hold.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-aa-1.cached-reach-and-rejected-key-hold`.

<paths>
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/test_aa1_cached_reach_and_hold.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~76/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULINGS (`ledger/ROUND_ANALYSIS.round27.md`, rulings 2 and 3)

**Measured (HVST-q-1, run `20260930T084110Z-run-4ee47491`):**
- **wsj:** the Lenovo listing pages 1-3 were served from same-day cached listing bronze (written 05:12Z), so the job recorded
  `reached_span` NULL. The code is `publishers.py` ~:650-661 and `worker.py` ~:56-85.
- **bbg:** the job made no listing request (also cached). Its only live request re-fetched `bbg:NM5NLQ6K50XZ01`, which `p-2`
  records as rejected `short_or_partial_body` and re-fetches every run. That request got a 403, then a failed press-and-hold
  repair, then `request_rejected` (row `Z-S45`).

**The changes:**
1. **Reach from cache.** A listing page served from same-day cache is evidence of the span it covered. The job's
   `reached_span` is written from the cached page's own date bounds, marked `from_cache: true`. It is never widened beyond
   those bounds.
2. **Hold a body-rejected key.**
   - A key rejected `short_or_partial_body` is HELD for the rest of that UTC day: not fetched again. It is retried on a later
     day.
   - After 3 failed days it is recorded `rejected_final`, with its reason, and never re-fetched.
   - The run record names each hold.
   - A key rejected for any OTHER reason (a transient failure) is not held.
   - This replaces `p-2`'s "re-fetch rejected keys every run".

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aa-1"><invocation>python -m pytest lib/opal_data_harvest/test_aa1_cached_reach_and_hold.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-aa-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~76/scripts/aa1_ac2_replay_q1.py</invocation><expect>NETWORK CALLS MADE: 0</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-aa-1"><invocation>python -m pytest lib/opal_data_harvest/ -rA --tb=line</invocation><expect>passed</expect></criterion>
</proof_of_spec>

**What each criterion must prove or print:**
- **AC1** (plants, each asserted):
  - (a) a cached wsj listing page yields a `reached_span` equal to the page's own date bounds, with `from_cache` true;
  - (b) a cached page with no dates yields no span;
  - (c) a `short_or_partial_body` key is not fetched again the same UTC day, and is fetched on the next day;
  - (d) after 3 failed days it is `rejected_final`;
  - (e) a transient rejection is NOT held.

  Mutants restoring each base behaviour fail.
- **AC2:** replay `q-1`'s recorded job shapes from the runtime root (read-only; `events.jsonl`, `runs/20260930T084110Z-*.json`,
  the cached listing bronze metadata) through the new code on stubs. Print:
  - wsj's `reached_span` with `from_cache`;
  - that `bbg:NM5NLQ6K50XZ01` is HELD (not fetched);
  - the line `NETWORK CALLS MADE: 0`.
- **AC3:** the base is commit `699fb78c93`, pinned. Print the base and after pass counts. No test that passed at the base
  fails.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round27.md` @`8c0b34526b` s.4 item 1.
- `HVST-aa-2`'s pair is signed against this cell's merged code.
- The `<expect>`s are plain printed tokens (ruling 6).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<slot>~76</slot>
<fabric>site-z</fabric>
