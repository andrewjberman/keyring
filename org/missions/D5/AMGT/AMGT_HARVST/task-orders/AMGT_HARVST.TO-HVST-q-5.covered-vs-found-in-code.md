# AMGT_HARVST task order -- `HVST-q-5` -- ROUND 27 chain 5: `C-HV-COVERED-VS-FOUND` IN CODE -- the daily builder emits `publishers_found_codes`, the timeline route serves it (FWD-3, FWD-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-q-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~74</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- build_daily has no scheduled writer; this cell writes no gold (the serving rebuild rides a later pair).
comp-iam: RUN at L5 -- S3 GET/LIST for an in-memory local build over current gold inputs. NO PUT, NO deploy, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a found set that silently feeds data_status (a found-only day turning SEARCHED). AC1 plants a found-only day and requires data_status unchanged and covered/found kept apart.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE, NO DEPLOY, NO VENDOR CALL.**
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~74/scripts/`; outputs named `q5_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~74/AMGT_HARVST.TO-HVST-q-5.covered-vs-found-in-code.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-q-5.covered-vs-found-in-code`.
4. **Shared file.** In `lib/research/harvest/publication_gold.py` you own ONLY `daily_rows`'s emitted fields and
   `GOLD_DAILY_SCHEMA`. Coverage computation is not yours.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/timeline_api.py
lib/research/harvest/tests/test_q5_covered_vs_found.py
lib/research/harvest/tests/test_publication_gold_daily.py
lib/research/harvest/tests/test_timeline_api.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~74/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CONTRACT (`prd/AMGT_HARVST_PRD.md` v0.4 `C-HV-COVERED-VS-FOUND`)

- `publishers_covered_codes`: the publishers whose listing for that name ran over that day (SEARCHED).
- `publishers_found_codes`: the publishers whose articles that day serves, by whatever path found them.
- A publisher in the found set but not the covered set reads as "found, listing not run", never "not searched".
- Coverage marks (`data_status`, FWD-7 eligibility) read the COVERED set only. A found-only article never makes a day
  SEARCHED.

**The change:**
- `daily_rows` emits `publishers_found_codes` per row, appended to `GOLD_DAILY_SCHEMA` as an added column. No existing column
  changes.
- The timeline route (`timeline_api.py`, series rows) serves it beside `publishers_covered_codes`.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-q-5"><invocation>python -m pytest lib/research/harvest/tests/test_q5_covered_vs_found.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-q-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~74/scripts/q5_ac2_lenovo_2026_02_12.py</invocation><expect>992_HK_Equity 2026-02-12 covered=</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-q-5"><invocation>python -m pytest lib/research/harvest/tests/ lib/research/api/tests/test_timeline_routes.py -rA --tb=line</invocation><expect>0 failed</expect></criterion>
</proof_of_spec>

**What each criterion must prove or print:**
- **AC1:**
  - a found-only day keeps `data_status` and `publishers_covered_codes` unchanged and lists the publisher in
    `publishers_found_codes`;
  - the route serves both fields;
  - a mutant folding found into covered fails.
- **AC2:** a LOCAL in-memory `build_daily` over the current gold inputs (no put) prints the line
  `992_HK_Equity 2026-02-12 covered=[...] found=[...]`.
  - The CVO measured covered `[bbg]` with sa and wsj articles on that day. Print what the build gives.
  - Print a total: the days where found is not a subset of covered.
- **AC3:** the base is commit `ff4405d3d5`, pinned. It prints the base and after counts, and `0 failed`.

## 3. MERGE ORDER

This cell merges only after `HVST-q-1` drains (ruling 6). The serving rebuild rides `q-7`'s pair or round 28's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round26.md` s.4 item 5, and ruling 2.
- DSGN_AMGTV1 round-11 `n-3` renders the page half (`2.0.0_SA_COO~D`).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>27</round>
<slot>~74</slot>
<fabric>site-z</fabric>
