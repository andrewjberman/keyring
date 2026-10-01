# AMGT_HARVST task order -- `HVST-af-4` -- ROUND 33: THE COLLECTOR LISTS bbg AND wsj THROUGH THE DATE-ORDERED MONTHLY SITEMAPS, NEVER SEARCH; ONE LIVE bbg JOB

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-af-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~92</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- phase A LOCAL (code + tests); phase B is ONE live bbg collector job from the box's own egress in the main-tree bbg profile (no residential arm), writing its run record and, if the upload runs, bronze/silver for that one name; no gold write.
comp-adversary: RUN at L5 -- the adversary is a listing that silently falls back to search when the sitemap fails. AC2 requires 0 /search requests in the job's own attempt rows.
</preflight>

## 0. THE CELL (decomposition section 46, `HVST-af-4`; PRD v0.13 FWD-15 (e); CTO rulings 27695 item 3 and 27700)

**FWD-15 (e):** for bbg and wsj, discover articles in DATE ORDER back to 2026-01-01 rather than by search relevance.
**CTO ruling:** bbg discovery stays OFF search (first light: bbg search 403 PerimeterX). **Measured in round 32 (`ae-5`
census, `deliverables/0.9.0_WK_AMGT_HARVST~91/ae5_discovery_census.json`):** wsj
`/sitemaps/web/wsj/en/sitemap_wsj_en_m{month}_{year}.xml` (200, dated newest-first, reaches 2026-01) and bbg
`/sitemaps/news/{year}-{month}.xml` (200 after the press-and-hold solve, ~6,900 items per month, reaches 2026-01; order
within a month mixed, so it is sorted). `lib/opal_data_harvest/discovery.py` `discover(tab_session, publisher, query)`
already walks them (ROUTES set to the measured routes). The collector's own `bloomberg()` leg in `publishers.py` STILL
lists by `/nemo-next/api/search/query` -- nothing calls `discovery` yet.

## 1. PHASE A (LOCAL)

1. In `lib/opal_data_harvest/publishers.py`, the `bloomberg` leg (and the Dow Jones `wsj` listing) list through
   `discovery.discover(self._session.inner, pub, <company query>, floor=<the bound/floor>)` whenever the inner session
   is a `TabSession` (`getattr(inner, "solves_challenges", False)`); the sitemap item's URL and date replace the search
   hit; relevance is decided by the existing body check after the article fetch (as today). The old search path stays
   only for a non-tab session (tests and any REST fallback); a tab session NEVER requests `/search`.
2. `lib/opal_data_harvest/test_af4_discovery_hookup.py` (new), plants with a fake TabSession (no network): (i) a tab bbg
   leg requests `/sitemaps/news/` and never `/search`; (ii) items before the floor are not fetched; (iii) a wsj tab leg
   lists through its monthly sitemap; (iv) a non-tab session keeps the base search path.

## 2. PHASE B (WORLD) -- one live bbg job

Run ONE collector job: `python -m lib.opal_data_harvest run --harvest-grammar --retrieval-mode backfill --floor
2026-01-01 --new-only --no-sign-in --security-json <BA's universe row as a file under your deliverables> --publishers
bbg --max-jobs 1` from the MAIN tree's runtime (`--runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`)
so the main-tree bbg profile (earned in round 32) is used. If a PRESS & HOLD challenge is met, the transport's challenge
path solves it once (wired). Copy the job's run record verbatim to
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/af4_bbg_run.json` (add `"run_record_path"`).
At most ~40 requests (pacing applies); stop the job if it exceeds that.

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/discovery.py
lib/opal_data_harvest/test_af4_discovery_hookup.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

**Reads (no write):** `tab_transport.py`, `transport.py`, `verification.py`, `worker.py`, the `ae5_discovery_census.json`
above, `contracts.json`. **Never:** sa or ft traffic or profiles (the issuer's running backfills), wsj live traffic in
this order (phase A only for wsj), search on bbg, a residential proxy, any vision/AI API.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-af-4"><invocation>python -m pytest lib/opal_data_harvest/test_af4_discovery_hookup.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-af-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round33/checks/af-4.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/AMGT_HARVST.TO-HVST-af-4.bbg-wsj-sitemap-discovery-in-the-collector.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-af-4.bbg-wsj-sitemap-discovery-in-the-collector`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-32 analysis @`749ec2c72e` item 4 (the census half was measured in `ae-5`; this cell wires it).
Authority R-21; R7. No pair: no served gold moves.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>33</round>
<slot>~92</slot>
<fabric>site-z</fabric>
