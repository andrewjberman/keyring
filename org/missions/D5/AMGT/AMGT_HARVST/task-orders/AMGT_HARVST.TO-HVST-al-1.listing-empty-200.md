# AMGT_HARVST task order -- `HVST-al-1` -- ROUND 39 CHAIN A (row Z-W91-S10, placed by Z-S79): A DOW JONES LISTING THAT ANSWERS 200 WITH 0 PARSEABLE HITS IS TOLD APART FROM "NO ARTICLES"

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-al-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants only, with a stub session: no network, no publisher request, no S3. Collection is unchanged and held on the publisher-terms card; this cell runs NO live listing.
comp-adversary: RUN at L5 -- the adversary is a flag set from the body alone (a 403 or 5xx reading as an empty 200), a flag that sticks across calls, or a status change that ends a backfill run (the new status must NOT join the driver's STOP set).
</preflight>

## 0. THE CELL

Row Z-W91-S10: on one call, barrons search returned HTTP 200 with 0 parseable hits (a probable soft block); every other
call returned 16 hits. Today `lib/opal_data_harvest/publishers.py` reads a 200 with no hits as "no articles":
- `DowJones.discover`, around line 1155;
- the listing loop that calls it, around lines 1000-1016, which sets `urls` and `listing_ref`.
So the run record cannot tell a soft-blocked page from a genuinely empty search. barrons still searches through
`/search`; `discovery.py`'s sitemap routes cover only wsj and bbg.

## 1. THE BUILD (LOCAL)

1. Add the module constant `LISTING_EMPTY_200 = "listing_empty_200"` to `publishers.py`.
2. In `DowJones.discover`, set `self.listing_empty_200 = True` when the response status is 200 and the parse returns 0
   URLs. Otherwise set it to False. Reset it on every call, and decide it from the status as well as the body.
3. In the listing loop that calls `discover`, a job whose page-1 listing is an empty 200 records a run-record event
   `listing_empty_200` (query, page). That job's status is `listing_empty_200`, not `no_new_articles`.
   - Do NOT add the new status to `backfill_driver.STOP_STATUSES`. A backfill moves on to the next pair, as it does for
     no_new_articles.
   - Any other job outcome is unchanged.
4. Plants in `lib/opal_data_harvest/test_al1_listing_empty_200.py`, with no network and a stub session:
   - (i) an empty 200 sets the flag, records the event and sets the job status;
   - (ii) a 200 with hits does not set the flag;
   - (iii) a 403 does not set the flag, and existing behaviour is unchanged;
   - (iv) the flag resets: an empty 200 followed by a 403 reads False;
   - (v) wsj and barrons both, through the same class;
   - (vi) `listing_empty_200` is not in `backfill_driver.STOP_STATUSES`.
5. Both suites stay green: `python -m pytest lib/opal_data_harvest -q` and `python -m pytest lib/research/harvest -q`.
   Report the counts before and after. At the cut the base read 597 passed with 3 skipped, and 334 passed.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r39-91`, branch `wk-AMGT_HARVST-91-r39a`, cut from CLOUD at the issuance
commit (sparse cone per decomposition section 50). Do not touch any `.runtime` directory.

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/test_al1_listing_empty_200.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-al-1"><invocation>python -m pytest lib/opal_data_harvest/test_al1_listing_empty_200.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-al-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round39/checks/al-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 drives the real `DowJones.discover` for wsj and barrons through a stub session, with no network.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-al-1.listing-empty-200.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-al-1.listing-empty-200`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-38 analysis @3da5563fd8, enrichment item 1. Placed by row Z-S79; the CTO accepted the placement
(msg 28796). Live proof against a real soft block needs barrons collection, which is held on the publisher-terms card
@8d20bc24c8. This cell proves the status on planted pages only.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>39</round>
<slot>~91</slot>
<fabric>site-z</fabric>
