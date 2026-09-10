# AMGT_RESAPP.TO-AMGT-s-14 -- THE INPUT LEDGER: per input class, source / last run / outcome, and RE-RUN ALONE while the others stay -- a single refresh under one timestamp is a violation

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-14</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~7</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-12; manifest row S14; verb: wire)

```
AMGT-s-14. THE INPUT LEDGER -- per input class: source, last run, outcome, and RE-RUN ALONE while the
others stay. Every stage persists its own output. A single refresh under one timestamp is a violation.

FWD-12's bar, verbatim: "An analyst can see where each input came from and re-run any one alone. DONE
WHEN EXERCISED -- one input has actually been re-run by itself while the others stayed where they were.
ACCEPT: For each kind of input -- market data, filings, news, social, web -- the page shows where it
came from, when it last ran, and whether that run worked; and any one can be re-run on its own. A
single button that refreshes everything under one timestamp does not count."

C-STAGE-PERSISTS (PRD s.3): every stage persists its own output and is independently re-runnable. The
stages that exist at this cut: market_data (AMGT-s-1's pull), sa (AMGT-s-b4's fetcher); filings, news
(non-SA), social and web are registered as classes with NO stage yet, honestly.

WHAT TO PRODUCE, under lib/research/ledger/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~7/:

  (a) THE LEDGER LIBRARY  lib/research/ledger/ledger.py
      record_run(security_key, input_class, source, outcome: OK|FAILED|SKIPPED, stamp, detail) appends
      one entry to packs/<security_key>/input_ledger.json in the store (per AMGT-s-6's grammar; the
      ledger is the one artifact under packs/ that is appended rather than stamped, and the contract
      says so); read_ledger(security_key) returns the latest entry per class; the CLASSES are the closed
      set market_data|filings|news|social|web|sa, each with a `stage` callable or None.
      rerun(security_key, input_class) invokes THAT class's registered stage and nothing else, then
      records the run. There is NO function that re-runs more than one class (AC4).

  (b) THE RETROFIT, minimal: AMGT-s-1's pull (integrations/bloomberg/research/model_block_pull.py) and
      AMGT-s-b4's fetcher (integrations/seekingalpha/rest_fetch.py) CALL record_run at the end of a
      run, and are REGISTERED as the market_data and sa stages. One call added to each, nothing else
      changed; their own criteria must still pass (re-run their test invocations after the edit and
      record the results in your deliverable).

  (c) THE EXERCISE, on ONE security AMGT-s-1 already touched (no new unique security): rerun(key,
      'market_data') -- Bloomberg is called for that one name again (inside the cap AMGT-s-1 stated),
      the ledger's market_data entry moves to a new stamp, and EVERY OTHER class's entry is byte-for-byte
      unchanged. before/after copies of the ledger go in the deliverable; check_rerun.py compares them.

  (d) SPEC_SECTION_ledger.md for AMGT-s-5: per class, the three columns and the one re-run control per
      row; NO "refresh all" control anywhere on the page.
```

## DEPENDENCIES

`AMGT-s-6` (the store). Same slot (~7), third in `AMGT-s-6 -> AMGT-s-7 -> AMGT-s-14`. The retrofit
touches AMGT-s-1's and AMGT-s-b4's modules AFTER those cells have landed (sequential, never concurrent).

## BOUNDS -- what this cell may not cross

```
⛔ C-STAGE-PERSISTS: no stage's output is overwritten by another's; a re-run of one class writes a new
stamp for that class and nothing for the rest.
⛔ NO REFRESH-ALL: no function, script or page control that runs more than one class under one stamp.
AC4 refuses one by name and by test.
⛔ F2 / G-24: the exercise re-touches ONE security AMGT-s-1 already pulled; no new unique security. If
the terminal is signed out at the exercise, the market_data run records outcome FAILED with the reason
-- that IS a valid ledger entry and the exercise then re-runs a class whose stage does not need Bloomberg
(sa, if AMGT-s-b4's fetcher is registered and the parked session is alive) or records the limitation.
Never a sign-in.
⛔ THE RETROFIT IS ONE CALL PER MODULE. Do not refactor the siblings' modules; their criteria are theirs.
⛔ C-DESIGN-SPEC-FIRST: no .tsx.
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
AMGT-s-6's STORE_CONTRACT.md (landed): packs/<key>/ grammar; the ledger's append-only exception is
    stated there or in your deliverable, never assumed.
AMGT-s-1 (landed): pull_log.json records every security requested; your exercise adds one request for
    an existing key. AMGT-s-b4 (landed if in time): request_log.json likewise.
brief O12 / PART III-B: "the subtrees refresh on different clocks and a page that hides that misleads."
comp-schedule (RUN): 25 gates armed, none this project's; G-20 binds (no scheduled re-run).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/ledger/
integrations/bloomberg/research/model_block_pull.py
integrations/seekingalpha/rest_fetch.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-14.input-ledger-per-class-rerun-alone.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~7/`. The two sibling modules are granted for the
ONE-CALL retrofit only. The store is READ and WRITTEN under packs/<key>/input_ledger.json.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W7-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-14"><invocation>python -m pytest lib/research/ledger/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "4 passed" with no "failed" -- (1) record_run appends and read_ledger returns the latest per class; (2) rerun on a fixture registry with stub stages invokes exactly one stage; (3) after that rerun, every other class's entry is unchanged (the difference arm: one moved, the rest did not); (4) the CLASSES set is exactly market_data|filings|news|social|web|sa</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-14"><invocation>python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~7/check_rerun.py</invocation><expect>one line of the exact shape "RERUN market_data on &lt;key&gt;: classes moved 1 (market_data), classes unchanged &lt;n&gt;, outcome &lt;OK|FAILED&gt;" -- read from the before/after ledger copies; "classes moved" above 1 is the single-timestamp violation and is NOT met; an outcome FAILED with a recorded reason (terminal signed out) still MEETS this criterion, because the ledger recorded a real run honestly</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-14"><invocation>grep -c -E 'record_run' integrations/bloomberg/research/model_block_pull.py integrations/seekingalpha/rest_fetch.py</invocation><expect>each file listed with a count of 1 or greater -- both stages report their runs to the ledger; a file at 0 means that class cannot be re-run alone from the page and is NOT met (if AMGT-s-b4's module does not yet exist at your run, record that as a row and the sa line reads 0 honestly -- this criterion then stands NOT met until it lands, never rescued by a stub)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-14"><invocation>grep -r -c -i -E 'refresh_all|rerun_all|run_all|for .* in CLASSES.*rerun' lib/research/ledger/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE and structural: no function re-runs more than one class; "a single button that refreshes everything under one timestamp does not count" (FWD-12's own ACCEPT)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-14"><invocation>python -c "import json; l=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/pull_log.json')); print('unique securities requested across AMGT-s-1 and this exercise', len(set(l['securities'])))"</invocation><expect>"unique securities requested ... 3" or fewer -- NEGATIVE: the exercise re-touched an existing security and added no new one (F2)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-14" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the ledger's behaviour, including the one-moved-rest-unchanged arm.
- **AC2** (mechanical, read from the artifact): one real class re-run alone on a real security.
- **AC3** (mechanical): both existing stages report to the ledger.
- **AC4** (mechanical, NEGATIVE, structural): no refresh-all exists to be pressed.
- **AC5** (mechanical, NEGATIVE): no new security.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): read the ledger for the exercised security -- could an analyst tell, per input class, where it came from, when it last ran and whether it worked, and would the four classes with no stage yet read as "not wired" rather than as "fine"?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q7, third in `AMGT-s-6 -> AMGT-s-7 -> AMGT-s-14`; slot ~7 continues on the same context.
**Provenance:** the cell text is the decomposition's row verbatim. The two sibling modules in `<paths>` are a deliberate, sequential write-surface overlap: the ledger cannot be exercised without a stage that reports to it, and the stages landed before this cell runs. The grant is one call per module and the siblings' own criteria are re-run after the edit.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-20 and G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell writes one JSON per key under the store
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; the store this cell writes is created by AMGT-s-6
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a library, one call added to two scripts, JSON under a new bucket; no deployed resource changes.
