# AMGT_HARVST task order -- `HVST-ah-3` -- ROUND 35: ft -- 91% OF FETCHED BODIES COME BACK LOCKED; FIND WHY AND UNLOCK THEM (FWD-14 depth)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ah-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~92</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- WORLD: ft traffic from the box's own egress through the existing ft session/profile; no Secrets write; no gold write; the stored ft session is re-minted only through the existing renewal path.
comp-adversary: RUN at L5 -- the adversary is a "fix" that just stops fetching locked pages (fewer fetches, same coverage) or one that counts a teaser as a body. AC2 grades the locked share over at least 40 real body fetches with stored articles.
</preflight>

## 0. THE CELL (decomposition section 48, `HVST-ah-3`; PRD FWD-14; round-34 analysis item 3)

**The measurement.** The ft driver's job 1 (ASML, 12:34-15:01Z) ran 2 h 27 min for 61 accepted articles out of 418 body
fetches. Its run record is
`.runtime/opal-data-harvest/runs/20261001T123436Z-ft-a76fabb550.json`, under the main tree
`C:/Users/Opal Bloomberg/Desktop/ajb_workspace`.
- Of the 357 rejected, 324 carry `publisher_did_not_unlock_body` + `short_or_partial_body` + `missing_metadata` +
  `invalid_publication_date` + `company_not_mentioned`: the body came back as the paywall/barrier page.
- Only 27 are a plain `company_not_mentioned`.
- So the problem is ft ACCESS, not relevance: the in-tab fetch unlocks about 1 article in 10.

**What exists.** ft uses the in-tab transport (`lib/opal_data_harvest/tab_transport.py` `TabSession`, persistent Chrome
profile under the main tree's `.runtime/opal-data-harvest`). It is wired by `lib/opal_data_harvest/publishers.py`
(`TAB_ORIGINS`, `seed_cookies`) and `lib/opal_data_harvest/contracts.json` (`transport`, `body_format`,
`seed_from_bundle`).

**The issuer stopped the ft driver for you (`STOP_FT`).** The ft profile and the main runtime are yours this round. Never
touch the bbg/wsj runtimes (`.runtime/opal-data-harvest-bbg`, `-wsj`) or the sa runtime under `wk-hvst-r32-92`.

## 1. THE ACT

1. **DIAGNOSE (at most 20 ft requests).** Take 5 locked and 5 unlocked `fetch_key`s from the run record above (their
   URLs are in `rejected` and `accepted`) and compare them. Candidates:
   - a content-type or tier the subscription does not cover (FT Premium, Lex, Alphaville, a podcast/video page);
   - a session that is not attached to the in-tab `fetch()` (credentials mode, a cross-origin redirect to
     `accounts.ft.com`, a stale cookie);
   - a barrier served to `fetch()` but not to a navigated page.

   Record each sample's observed barrier signature, the request mode and the answer, as
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/ah3_diagnosis.md`.
2. **FIX** at the root you found, in `publishers.py` / `tab_transport.py` / `contracts.json`, with plants in
   `lib/opal_data_harvest/test_ah3_ft_unlock.py`:
   - the barrier page is classified as locked;
   - the fixed request path is used for ft.

   If the root is a tier the account does not hold, the fix is to skip those URLs BEFORE the body fetch, by URL or
   listing metadata. Say so in the diagnosis: that is a coverage limit, not an unlock.
3. **RUN** the real collector on 2 ft names from the universe, chosen by the most ft listing hits, in the main runtime.
   Write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/ah3_ft_runs.json` =
   `{"before": "<the run record path above>", "after": [<each job's run record, verbatim>]}`.

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/tab_transport.py
lib/opal_data_harvest/contracts.json
lib/opal_data_harvest/test_ah3_ft_unlock.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ah-3"><invocation>python -m pytest lib/opal_data_harvest/test_ah3_ft_unlock.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ah-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round35/checks/ah-3.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- The collector suite (`python -m pytest lib/opal_data_harvest/ -q`, base 468 passed, 1 skipped) stays green.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/AMGT_HARVST.TO-HVST-ah-3.ft-body-unlock.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ah-3.ft-body-unlock`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-34 analysis @`6cbef26707` item 3 ("ft pre-filtering or a dated source"). The measurement
re-points it from relevance to access: 324 of 357 rejections are locked bodies. Authority R-21.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>35</round>
<slot>~92</slot>
<fabric>site-z</fabric>
