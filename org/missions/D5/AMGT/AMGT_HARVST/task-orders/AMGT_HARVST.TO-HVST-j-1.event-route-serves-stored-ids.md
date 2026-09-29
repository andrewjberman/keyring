# AMGT_HARVST task order -- `HVST-j-1` -- ROUND 20 chain 1 of 2: THE EVENT ROUTE SERVES THE STORED EVENT BY ITS STORED ID (row `Z-W39-S1`), proved in memory

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-j-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~47</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on timeline_api.py or the harvest gold prefixes; this cell deploys nothing.
comp-iam: RUN at L5 -- no new boto3 call; AC2 reads S3 (the newest chatter_event part and its articles) with GET/LIST only through the producer's own reader. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a fix that recomputes the id a second way (a new scheme that happens to match today's 8), or one that still returns the FIRST event of a day when two share it. AC1 plants two events on one first_day; AC2 requires the served body's event_id to be the STORED value on all 8 real events.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY, NO ROUTE WIRING.** The route is unwired in
   `lib/research/api/scoped_amgt.py` and unmounted at the gateway; both stay so. This cell fixes the pure server
   function only. Wiring and mounting are a separate decision, not this cell's.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~47/scripts/`; outputs named `j1_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~47/AMGT_HARVST.TO-HVST-j-1.event-route-serves-stored-ids.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-j-1.event-route-serves-stored-ids`.

<paths>
lib/research/harvest/timeline_api.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~47/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL (`ledger/ROUND_ANALYSIS.round19.md` @`a251f02116`, s.2 ruling 2 and s.4 item 1; row `Z-W39-S1`)

**The defect** is in `lib/research/harvest/timeline_api.get_timeline_event`, ROUTE 3 (~:358-400):
- It keys an event by `first_day` and returns the FIRST row whose `first_day` matches.
- It RECOMPUTES the body's `event_id` as `publication_gold._event_id(security_key, first_day, last_day)`.
- Since `HVST-b-1`, a stored `event_id` carries the story, so the recomputed id matches no stored row.
- Measured by the issuer at the cut: all **8 of 8** served events carry a stored `event_id` different from the recomputed
  one, and no security has two events on one `first_day` today.

**The change, and only this:**
1. ROUTE 3 is keyed by the STORED `event_id`: `get_timeline_event(security_key, event_id, event_loader, article_loader)`
   returns the `chatter_event` row whose `event_id` equals the argument. Update the route comment's path to
   `.../timeline/event/{event_id}`.
2. The served body's `event_id` is the matched row's STORED value. It is never recomputed and there is no second id
   scheme.
3. An unknown id returns `TIMELINE_EVENT_NOT_FOUND`, exactly as a missing `first_day` does today.
4. Routes 1 and 2 (`get_timeline`, `get_timeline_day`) are unchanged byte for byte in behaviour.
5. `lib/research/api/tests/test_timeline_routes.py::test_timeline_route_post_and_event_route_are_not_wired` MUST still
   pass unchanged: the route stays unwired.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-j-1"><invocation>python -m pytest lib/research/harvest/tests/ lib/research/api/tests/test_timeline_routes.py -rA --tb=line</invocation><expect>both suites pass with new tests NAMED in the -rA output: the route returns the row whose stored event_id equals the argument; two planted events sharing ONE first_day are EACH served by their own id (neither shadows the other); the body's event_id equals the stored value, not publication_gold._event_id of the row; an unknown id returns TIMELINE_EVENT_NOT_FOUND; the unwired-route test passes unchanged; the pass count BEFORE and AFTER printed (base 202 in lib/research/harvest/tests/ plus the api file's own count) and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-j-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~47/scripts/j1_ac2_stored_ids_on_served_rows.py</invocation><expect>OVER THE SERVED NEWEST chatter_event PART (8 events at the cut) and its landed articles, read through publication_gold._latest_gold_snapshot_rows: (a) per event, the stored event_id beside the old code's recomputed id (git show of timeline_api.py at the base 86ee31f531, or publication_gold._event_id directly), with the count that differ printed (8 of 8 at the cut); (b) the NEW get_timeline_event called with each stored id returns that very row (first_day, last_day, event_id equal) with its articles, 8 of 8, denominator printed; (c) the old first_day-keyed call and the new id-keyed call return the same article set per event. PASS only if (b) is 8 of 8 and (c) holds</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No wiring in `scoped_amgt.py`, no gateway mount, no deploy, no change to `publication_gold`'s id scheme, no gold write,
no portal work, no vendor call.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **The analysis's cell 1 names a redeploy and "all 8 served events answer 200 by their stored ids". That premise was
   measured FALSE at the cut, so the served half is HELD, not cut.** The route answers no user:
   - The deployed `opal-amgt-scoped-api` (`uv0oTSMa...`) returns `404 {"refused": true, "reason": "no /api/scoped/amgt
     route for GET .../timeline/event/2026-09-08"}`.
   - The gateway `7k3ed8px20` carries 108 routes, with 2 timeline routes (`/timeline`, `/timeline/day/{date}`), and no
     event route.
   - `scoped_amgt.py:4101` states the route "IS NOT WIRED HERE", and
     `test_timeline_route_post_and_event_route_are_not_wired` asserts it.
   - The portal's `TimelinePanel.tsx:127,130` builds only the `/timeline` and `/timeline/day` URLs.

   So `Z-W39-S1` is a real defect in UNREACHED code, and "the page's event window reads through this route" is not
   what the page does. Wiring and mounting the route is a NEW served surface, which is the CTO's call. It is carded
   (row `Z-S42`). The code fix is right under either answer, so it is cut now.
2. **Base:** suite 202 passed (the `i-2` drain, trunk after `i-4`). AC1's named tests FAIL at the base by construction.
   AC2 (b) FAILS at the base: the old route takes a `first_day`, and its body's id is recomputed.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>20</round>
<slot>~47</slot>
<fabric>site-z</fabric>
