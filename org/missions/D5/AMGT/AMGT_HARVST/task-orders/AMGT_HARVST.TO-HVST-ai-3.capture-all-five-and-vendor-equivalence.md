# AMGT_HARVST task order -- `HVST-ai-3` -- ROUND 36: CAPTURE-AT-LOAD ARMED ON ALL FIVE PUBLISHERS + SAME-VENDOR FIXTURE EQUIVALENCE FOR wsj/barrons (FWD-11 limb 2b)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ai-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code; captures land under the live runtimes after the drain; no network; no Secrets write.
comp-adversary: RUN at L5 -- the adversary is a publisher graded as passing limb 2b with no real sample. Status may read PASS-FIXTURE, SAMPLE-CAPTURED, VENDOR-EQUIVALENT or OPEN (NO SAMPLE), never MET-BY-ABSENCE.
</preflight>

## 0. THE CELL (decomposition section 49; CTO round-35 ruling 3)

Round 35 (`HVST-ah-1`) hooked `lib/opal_data_harvest/challenge_capture.py` into `lib/opal_data_harvest/verification.py`
`solve()`, just before the control is operated. Only bbg, wsj and barrons reach `solve()`
(`verification.CHALLENGE_PUBLISHERS`). ft and sa challenges are detected in `lib/opal_data_harvest/transport.py`
(`PacedSession.get` -> `_routes_challenges` / `route_bot_check`, signatures from `bot_check.signature_of`) and never
reach the hook. The live drivers have captured 3 bbg DOMs (`<runtime>/challenge_dom/`); bbg has a planted fixture
(`lib/opal_data_harvest/fixtures/challenges/bbg.*`, test `test_ah1_fixture_solve.py`). wsj and barrons share Dow Jones's
DataDome slider.

## 1. THE BUILD (LOCAL)

1. **Arm all five.** A detected challenge for ANY publisher is captured, sanitized and capped exactly as today:
   - where the page is the challenge (the tab), the rendered DOM;
   - for a REST refusal (sa), the response body, sanitized.

   Hook at the ONE detection point in `transport.py` for publishers that do not reach `solve()`. A capture failure never
   alters the request outcome. Plants in `lib/opal_data_harvest/test_ai3_capture_all.py`: one test per publisher, with
   the publisher in the test id, proving a planted challenge for that publisher writes one sanitized capture with
   provenance.
2. **Status CLI.** `python -m lib.opal_data_harvest.challenge_capture --status [--json]` reads the runtimes in
   `.runtime/harvest-backfill/runtimes.json` (repo root derived) and the fixtures directory. Per publisher it prints
   `captures` (count + newest), `vendor` (bbg/sa PerimeterX, wsj/barrons DataDome, ft its own) and `limb_2b`:
   - PASS-FIXTURE: a committed fixture whose solve test exists;
   - SAMPLE-CAPTURED: a live capture with no fixture yet;
   - VENDOR-EQUIVALENT: no own sample, but a same-vendor fixture passes through THIS publisher's solver path;
   - OPEN (NO SAMPLE): none of the above.
3. **Vendor equivalence (wsj/barrons).** `lib/opal_data_harvest/test_ai3_vendor_equivalence.py` takes any DataDome
   capture (wsj or barrons, from a fixture or a runtime `challenge_dom/`) and runs it through EACH of the wsj and
   barrons solver paths in the collector's own headless TabSession, as `test_ah1_fixture_solve.py` does. With no
   DataDome sample it SKIPS with the reason "OPEN (NO SAMPLE)" and never passes.

<paths>
lib/opal_data_harvest/challenge_capture.py
lib/opal_data_harvest/verification.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/test_ai3_capture_all.py
lib/opal_data_harvest/test_ai3_vendor_equivalence.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ai-3"><invocation>python -m pytest lib/opal_data_harvest/test_ai3_vendor_equivalence.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ai-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round36/checks/ai-3.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC1 reads "passed" or "skipped" with the OPEN (NO SAMPLE) reason; it never reads "failed".
- The collector suite (`python -m pytest lib/opal_data_harvest/ -q`, base 494 passed, 1 skipped) stays green.
- The changes go live in the running drivers after the drain: keep the hook minimal and defensive.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-ai-3.capture-all-five-and-vendor-equivalence.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ai-3.capture-all-five-and-vendor-equivalence`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-35 ruling 3. AC1's expect is "passed", but a SKIP carrying the OPEN (NO SAMPLE) reason is the
honest state until a DataDome capture exists. The issuer grades AC1 by reading the reason.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>36</round>
<slot>~91</slot>
<fabric>site-z</fabric>
