# AMGT_HARVST task order -- `HVST-ae-5` -- ROUND 32 chain B: THE CHALLENGE PATH FOR bbg, wsj AND barrons ON THE ONE BROWSER IDENTITY, DATE-ORDERED DISCOVERY FOR bbg AND wsj, AND A STALE SESSION THAT RENEWS ITSELF (FWD-11, the closing condition)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ae-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- phase A is LOCAL (code + tests, fake pages). Phase B sends bbg, wsj and barrons traffic from the site Z box's own egress (no residential arm: placement R7), writes run records and that run's articles, and writes the renewed session through the browser only -- under the signed never-widen pair.
comp-adversary: RUN at L5 -- the adversary is a "pass" that a human produced (operator input during the solve) or a renewal written by a Python client. AC2 requires operator_input_detected false per publisher (verification.last_operator_input); AC3 requires renewed_by browser and a changed stored hash.
</preflight>

## 0. THE CELL (decomposition section 45, cell `HVST-ae-5`; PRD v0.13 FWD-11 and the amended `C-HV-TRUST-TOKEN`)

**FWD-11, verbatim (the closing condition):** collection beats the publishers' bot checks and runs on a robust auth
solution, on all five publishers, and this project is not over until it does. DONE WHEN, EXERCISED: one unattended run
on the site Z box, with no human hand at any point, meets each publisher's live challenge (DataDome on wsj and barrons,
bbg's press-and-hold, FT's Security Verification, sa's checks) and passes it, then collects the validation security's
articles. In the same run, a session made deliberately stale is renewed without Andrew and written back to its store.
The run record names, per publisher, the challenge met, the path that passed it, and the session source.
RULE: BLOCKED is never the final state; licensed bulk access is not a route.

**The amended rule (`C-HV-TRUST-TOKEN`, v0.13):** a `bot_check` routes the leg to the CHALLENGE PATH
(`lib/opal_data_harvest/verification.py`, extended to every publisher) inside the SAME browser identity that met it. A
blind retry against a check stays forbidden; the challenge path is the only retry. If it does not pass, the leg stops and
the run record writes `bot_check` + `challenge_failed` with the signature -- a result to work on, never a final state.
Solving a challenge is not a sign-in.

**What exists:** `verification.py` `repair()` solves Bloomberg's press-and-hold (`press_and_hold_adaptive`, from the CRO
scripts dir) and Barron's slider ("Slide right to secure your access"), in a FRESH non-persistent context, and measures
human input with `last_operator_input()`. `HVST-ae-2` (drained before this order is handed to you) adds
`lib/opal_data_harvest/tab_transport.py` `TabSession`: one persistent per-publisher Chrome profile, requests in-tab.
The issuer's first-light grade (09:00Z, cell `HVST-ae-3`) names, per publisher, the challenge met and whether the
production launch settings changed it; it is added to this order as an amendment before hand-over.

## 1. PHASE A (LOCAL)

1. **`verification.py`: the challenge path on the identity.** A `solve(tab_session, publisher, signature)` that runs
   the solver INSIDE the `TabSession`'s own page (never a fresh context, never copied cookies): bbg press-and-hold,
   barrons slider, and wsj DataDome (the same Dow Jones slider family as barrons; locate it the way barrons does, by its
   visible instruction text inside the DataDome frame). Returns `{"challenge_met", "path", "passed",
   "operator_input_detected"}`; `passed` requires a same-origin in-tab fetch of the blocked route returning 200 after the
   solve. Keep `repair()` working for its existing callers.
2. **Routing:** a leg whose request is classed `bot_check` calls `solve` ONCE on the same `TabSession`, then retries the
   blocked request ONCE; on failure the job ends `bot_check` + `challenge_failed` with the signature.
3. **Date-ordered discovery for bbg and wsj** (FWD-15 e): a listing that walks each publisher's newest-first,
   date-filtered route back to 2026-01-01 (not relevance search). Find the route in the existing harvester and CRO
   scripts; if none is measured, implement it against the route the TabSession can open in-tab and name it in your
   report.
4. **Renewal:** `renew(tab_session, publisher)`: when the profile's session is stale (the account check reads logged
   out), the harvester's existing sign-in runs INSIDE the persistent profile, unattended; the browser's jar is the
   store; return before/after SHA-256 of the stored session.
5. **`lib/opal_data_harvest/test_ae5_challenge_path.py` (new), plants with fake pages** (each fails on the base):
   (i) a `bot_check` on a tab leg calls `solve` once on the SAME session object, never a new context; (ii) a second
   `bot_check` after the solve ends `challenge_failed` with no further request; (iii) wsj's DataDome slider is located
   and dragged in the fake frame; (iv) bbg/wsj discovery requests are date-ordered and stop at 2026-01-01; (v) `renew`
   writes nothing from Python (the stored session changes only through the browser fake).

## 2. PHASE B (WORLD) -- only when the issuer hands it to you, under the signed pair

One unattended run (no human at the keyboard; `last_operator_input` measured before and after) for bbg, wsj and
barrons, validation security **BA** (Boeing), each publisher in its own persistent profile: meet the live challenge,
solve it, collect BA's articles. Then stale ONE session deliberately (delete that profile's session cookie for the
publisher the issuer names) and renew it. Write
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/ae5_unattended_run.json` and `ae5_renewal.json`
in the shapes `ae-5.AC2.py` and `ae-5.AC3.py` read (open those two files: they are the record interface). A publisher
whose challenge is NOT passed is recorded honestly (`passed: false`, the signature) and is NOT a final state.

<paths>
lib/opal_data_harvest/verification.py
lib/opal_data_harvest/test_ae5_challenge_path.py
lib/opal_data_harvest/discovery.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

**Reads you may need (no write):** `lib/opal_data_harvest/tab_transport.py`, `publishers.py`, `worker.py`,
`bot_check.py`, `contracts.json`, `org/tier1_exec/4.0.0_SA_CRO/scripts/` (press_and_hold_lib and the REST clients),
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/scripts/harvest_first_light.py`, and the issuer's checks in
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/`.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ae-5"><invocation>python -m pytest lib/opal_data_harvest/test_ae5_challenge_path.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ae-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae-5.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ae-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae-5.AC3.py</invocation><expect>AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC1 passes at the end of phase A; AC2 and AC3 FAIL until phase B -- record them FAIL with `status_reason: phase B
  pending`, never PASS.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-ae-5.challenge-path-and-renewal.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ae-5.challenge-path-and-renewal`.

## AMENDMENT 1 -- 2026-10-01 ~06:0xZ, the issuer: phase A dispatched ahead of the first-light grade

1. **Phase A is dispatched now** (slot ~91 is free; `ae-2` drained @594d7be519 with `TabSession` on CLOUD). Phase A's code
   does not depend on the first-light result; the grade (cell `HVST-ae-3`, after 09:00Z) only sets each publisher's path
   for phase B and is added as AMENDMENT 2 before phase B is handed over.
2. **Date-ordered discovery** (section 1 item 3) goes in a new module `lib/opal_data_harvest/discovery.py` (path added),
   not in `verification.py`.
3. **Routing hookup is the issuer's:** the call from a leg's `bot_check` classification into `solve` sits in
   `publishers.py` / `worker.py` (other cells' files). Export `solve(tab_session, publisher, signature)` and
   `renew(tab_session, publisher)`; name in your report the exact call site and arguments the issuer should add. Section
   1 item 2's plants (i)-(ii) test `solve`'s contract through a small `route_bot_check(tab_session, publisher,
   signature, retry)` helper you export from `verification.py`.
4. Execute PHASE A only, then report and stop.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Analysis `ROUND_ANALYSIS.round31.md` @`309b2da963` section 4 item 5 (after items 2 and 3); PRD v0.13 FWD-11, FWD-15 (e).
- QUEUED on slot ~91 behind `ae-2`; handed over after `ae-2` drains and the issuer's first-light grade (cell `HVST-ae-3`)
  is folded in as an amendment. ft and sa's live challenges are in FWD-11 too; they are graded in a later cell once the
  three DataDome/press-and-hold publishers pass (ft passes after a warm-up today; sa runs on its R7 route).
- Phase B pair: CTO + COO halves name the three publishers, the validation security, the run's writes and the one
  session staled.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>32</round>
<slot>~91</slot>
<fabric>site-z</fabric>
