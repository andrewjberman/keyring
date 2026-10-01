# AMGT_HARVST task order -- `HVST-ah-1` -- ROUND 35: CAPTURE A REAL CHALLENGE DOM AT LOAD, THEN PROVE THE REAL SOLVER PASSES IT AS A PLANTED FIXTURE (FWD-11 limb 2b)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ah-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code + a local fixture server on 127.0.0.1; the capture runs inside the issuer's live drivers after the drain; no Secrets write, no gold write.
comp-adversary: RUN at L5 -- the adversary is a fixture that is NOT a real challenge (hand-written, or a normal page), or a "pass" that never operated the control. AC2 accepts only `source: captured_at_load` with provenance, and the fixture page records the control's operation.
</preflight>

## 0. THE CELL (decomposition section 48, `HVST-ah-1`; CTO ruling msg 27860 limb 2b; round-34 analysis item 1)

FWD-11 limb 2b: the solver passes a planted challenge fixture for each publisher, and the fixture must be a REAL
challenge DOM captured at load. Nothing captures a challenge DOM today: in round 34 the count of real bbg PerimeterX
DOMs on disk was 0. The live drivers do meet challenges. The bbg runtime logged `challenge_passed` events, the latest at
15:11:30Z. Challenges are routed in `lib/opal_data_harvest/transport.py` (`PacedSession.get`, `_routes_challenges` ->
`route_bot_check`) and solved in-tab by `lib/opal_data_harvest/verification.py` `solve()` (the bbg press-and-hold, the
wsj/barrons DataDome slider).

## 1. PHASE A (LOCAL) -- the capture hook

1. New `lib/opal_data_harvest/challenge_capture.py`. `capture(publisher, request_path, html, runtime_root)` writes
   `<runtime_root>/challenge_dom/<pub>-<UTC stamp>.html` plus a `.provenance.json` holding `source` "captured_at_load",
   `captured_at`, `runtime_root`, `request_path`, `signature` and `sanitizer` (a version string).
2. The sanitizer strips every `<input>` value, every cookie- or token-shaped attribute or string (`_px*`, `datadome`, any
   `value=`, any 20+ char base64/hex run inside an attribute) and every inline `<script>` body, and keeps the markup and
   visible text. Never write a cookie header.
3. Hook it at the ONE point where the live page is the challenge, just before `solve()` operates the control (the
   rendered DOM in the tab, not the raw 403 body). A capture failure is logged and NEVER fails the job. Write at most
   one capture per publisher per hour.
4. Plants in `lib/opal_data_harvest/test_ah1_capture.py`:
   - a fake challenge page is written and sanitized, with no planted cookie or value surviving;
   - a capture raising inside the hook leaves `solve()`'s result unchanged;
   - the hourly cap holds.
5. Commit, then REPORT (phase A ends here). The issuer drains A so the live drivers start capturing, and hands you
   phase B in a second order turn.

## 2. PHASE B (LOCAL, after the issuer's word) -- the planted fixture

1. Copy each captured DOM (the issuer names the files) to `lib/opal_data_harvest/fixtures/challenges/<pub>.html` with its
   `<pub>.provenance.json`.
2. `lib/opal_data_harvest/test_ah1_fixture_solve.py`: serve the fixture from a local `http.server` on 127.0.0.1. Add a
   recorder script that the TEST injects, not the fixture, which logs the press duration or the slider travel on the
   control. Open the fixture in a real Chrome through the same Playwright launch the collector uses, call
   `verification.solve()` on that page, and assert the control was operated as a pass requires (a hold for at least the
   challenge's stated time, or the slider reaching its end). One test per captured publisher, with the publisher's name
   in the test id.

<paths>
lib/opal_data_harvest/challenge_capture.py
lib/opal_data_harvest/verification.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/test_ah1_capture.py
lib/opal_data_harvest/test_ah1_fixture_solve.py
lib/opal_data_harvest/fixtures/challenges/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ah-1"><invocation>python -m pytest lib/opal_data_harvest/test_ah1_capture.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ah-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round35/checks/ah-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- The collector suite (`python -m pytest lib/opal_data_harvest/ -q`, base 468 passed, 1 skipped) stays green.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-ah-1.challenge-capture-and-planted-fixture.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ah-1.challenge-capture-and-planted-fixture`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-34 analysis @`6cbef26707` item 1. The phase-A drain changes live driver code: each driver job
re-imports the main tree, so phase A ships with the suite green.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>35</round>
<slot>~91</slot>
<fabric>site-z</fabric>
