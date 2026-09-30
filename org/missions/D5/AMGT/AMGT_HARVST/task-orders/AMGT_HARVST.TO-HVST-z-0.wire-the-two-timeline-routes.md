# AMGT_HARVST task order -- `HVST-z-0` -- ROUND 11 cell 0 of 4: WIRE the two timeline routes. Nothing is served today

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-z-0</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~31</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/research/api/scoped_amgt.py; this cell deploys nothing and pushes nothing.
comp-iam: RUN at L5 on the DESIRED plane -- the loaders need S3 GET on the newest chatter_daily / chatter_event / article_security_mention gold snapshots. NO PUT. A refusal is a BLOCKING row.
comp-adversary: RUN at L5 -- the adversary is a route that returns an EMPTY ARRAY where the load FAILED. AC2 is that adversary's test.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO S3 WRITE OR DELETE. NO PROD PUSH, and no push at all.**
2. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~31/scripts/` -- **never `.scratch/`.**
3. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~31/AMGT_HARVST.TO-HVST-z-0.wire-the-two-timeline-routes.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-z-0.wire-the-two-timeline-routes`.

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~31/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. WHY THIS CELL EXISTS -- and it is an issuer defect that created it

`HVST-w-3` built `lib/research/harvest/timeline_api.py` and `HVST-y-3` built the portal panel. ⛔ **NEITHER IS
REACHABLE: `lib/research/api/scoped_amgt.py` has ZERO occurrences of `timeline`** (measured: 0 hits over 1 file),
and every `get_timeline*` reference in the estate is its own definition or a test/proof script. **So `y-3`
rendered against STUBS and my AC1 could not tell** -- a render criterion that does not name its data source
certifies the component and not the path. Decomp `s.23.2`.

**You are wiring the missing path.** The panel calls:
- `GET /api/scoped/amgt/security/<security_key>/timeline?from=&to=`
- `GET /api/scoped/amgt/security/<security_key>/timeline/day/<date>`

## 2. WHAT TO BUILD

**Register both routes in `scoped_amgt.py`, following that file's OWN existing per-security route pattern** --
read it first; do not invent a new shape.

Each route delegates to the ALREADY-BUILT, PURE server module `lib/research/harvest/timeline_api.py`
(`get_timeline`, `get_timeline_day`). ⛔ **DO NOT MODIFY `timeline_api.py` -- it is not in your `<paths>`.** Your
job is the loaders and the wiring:

- **`daily_loader(security_key)`** and **`event_loader(security_key)`** read the **NEWEST** landed gold snapshot
  (`chatter_daily`, `chatter_event`), and an **`article_loader`** for the day route.
- ⭐ **USE THE PRODUCER'S OWN NEWEST-SNAPSHOT READER, not a hand-rolled S3 sweep.**
  `publication_gold._latest_gold_snapshot_rows` reads the ONE newest part by `(date, key)`, never a union -- **that
  property is what the signed never-widen pair rests on** (`ledger/NEVER_WIDEN_CTO_HALF_chatter_event_rebuild_20260928.md`
  @`9fddce21db`). A loader that unions parts would break it.

## 3. BOUNDS

1. **Three mechanical criteria, no fourth.** The round's JUDGMENT criterion is on `HVST-z-1`.
2. **Two routes only.** The event route (`/timeline/event/<first_day>`) is NOT in scope this cell -- `get_timeline_event`
   exists and stays unwired; say so rather than adding it.
3. **No schema change, no gold write, no producer change.**
4. **Do not touch the portal.** The push waits on Andrew and on this cell landing.

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-z-0"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~31/scripts/ac1_routes_serve_real_gold.py</invocation><expect>BOTH ROUTES SERVE REAL LANDED GOLD, not fixtures, and the proof is that the numbers match an independent read. Call each route in-process for the validation security and print: the route path, the field names returned against the spec's enumerated list with the set difference in BOTH directions, and the dense day count with its days-in-range denominator (equal, no gap). THEN prove the data is REAL: print the same day count and the same event count read directly via publication_gold._latest_gold_snapshot_rows, and show the two agree. A route that returns correct-shaped data from a fixture FAILS this criterion -- the independent read is what separates wired from stubbed, and that distinction is the whole reason this cell exists</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-z-0"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~31/scripts/ac2_route_failure_is_not_empty.py</invocation><expect>A FAILED LOAD IS UNREACHABLE TO THE EMPTY-ARRAY ENCODING, at the ROUTE layer. Inject a loader failure (raise, timeout, and malformed rows) into each of the two routes -- 6 cases -- and print for each the HTTP status and body, showing it carries `error: true` with a non-empty stable `error_code` and NO `series`/`events`/`articles` key. Then the CONTRAST: a SUCCESSFUL call over a range with no data, returning an empty array and NO error key. Print the exact predicate a caller uses to tell them apart. 6 of 6 failure cases plus the honest-empty control, or the criterion FAILS. timeline_api already proved this server-side over constructed rows (HVST-w-3 AC2); this proves the ROUTE does not undo it</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-z-0"><invocation>python -m pytest lib/research/api/tests/ -rA --tb=line</invocation><expect>the api suite passes with the new route tests NAMED in the -rA output, and the pass count printed BEFORE and AFTER so nothing elsewhere went red. ⛔ If any pre-existing test in this suite fails, report it with its error text and DO NOT repair it -- lib/research/api/ is AMGT_RESAPP's surface and a pre-existing failure there is a surprise ROW, not this cell's work</expect></criterion>
</proof_of_spec>

## 5. WHAT THIS CELL DOES NOT DO

It serves no new table, writes no gold, changes no schema, touches no portal file and pushes nothing. It does not
wire the event route. It does not grade FWD-5 -- that walk needs Andrew's word for the portal push and the deploy.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **AC1's independent-read clause is the lesson from `y-3` turned into a criterion.** "Renders correctly" and
   "renders correctly from the real path" were indistinguishable in round 10; comparing the route's numbers to a
   direct `_latest_gold_snapshot_rows` read is what separates them.
2. **The loader instruction is load-bearing, not stylistic.** The signed never-widen pair depends on newest-part
   semantics; a unioning loader would silently invalidate a signed rollback.
3. **AC3 forbids repairing a neighbour's red test.** `lib/research/api/` is AMGT_RESAPP's; round 10's `y-3` showed
   how easily a worker tidies someone else's component.

<risk>LOCAL</risk>
<status>complete</status>
<round>11</round>
<slot>~31</slot>
<fabric>site-z</fabric>
