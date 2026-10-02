# AMGT_HARVST task order -- `HVST-aj-5` -- ROUND 37 CELL 5 (CTO 28278; addendum ruling 8): EVERY bbg BOT_CHECK REACHES THE IN-TAB SOLVE; A FAILED SOLVE WRITES A CAPTURE BUNDLE AND RETRIES ONCE; LIMB 2a GRADED PER RUN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aj-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code + plants (stub tab, stub clock, stub response; no network, no Chrome); the capture bundle writes under the publisher runtime's existing challenge-capture root; no S3, no Secrets.
comp-adversary: RUN at L5 -- the adversary is (a) a bbg bot_check that still exits through VerificationRequired with no solve and no event (the 06:59:52Z run), (b) a "retry" fired immediately or twice (a hammer, not a backoff), (c) a capture bundle missing a part, or one that contains cookies, tokens or credentials, (d) a per-run grade that lets one passing run hide a run that was never in a window. Plants pin each.
</preflight>

## 0. THE CELL (row Z-S64; CTO 28278; `ledger/ROUND_ANALYSIS.round36.md` addendum ruling 8)

At 06:59:52Z, inside a monitor window with 0 hardware events, a bbg article fetch got a 403 with signature
`bloomberg_press_and_hold`. The job (`20261002T065754Z-bbg-4f3bfa12bd`) ended `bot_check`. Its run record and the bbg
`events.jsonl` hold NO solve or challenge event, and no capture exists: the ah-1 hook in `verification.solve()`
captures at most once per publisher per hour, and that hour's capture had already been taken at 06:38Z.

Read first:
- `lib/opal_data_harvest/transport.py`: `PacedSession.get`, the bot_check classing, `VerificationRequired` around
  line 432, the CHALLENGE_PUBLISHERS checks around lines 377-386, and the `challenge_passed` record around line 305.
- `lib/opal_data_harvest/verification.py`: `solve()` at line 342; `CHALLENGE_PUBLISHERS` = bbg, wsj, barrons.
- `lib/opal_data_harvest/challenge_capture.py`.
- `lib/opal_data_harvest/load_window_grade.py`: per-challenge bands, the 403 anchor, windowed requests.

## 1. THE BUILD (LOCAL)

1. **Find the path.** From the code, establish which path a bbg article-fetch 403 takes when the job runs in the
   driver's per-name shape: the run record shows `request_kind` "listing" and `signed_in` false. Establish why it
   reached no `solve()`. Write the finding with file:line to
   `deliverables/0.9.0_WK_AMGT_HARVST~90/aj5_path_finding.md`.
2. **Route every bbg bot_check to the in-tab solve,** and record the challenge events:
   - `challenge_presented` already exists, from aj-1;
   - add a solve attempt and its outcome: `challenge_passed` or `challenge_failed` with the signature.
3. **On a failed solve, write a capture bundle before giving up,** regardless of the hourly cap:
   - a DOM snapshot;
   - a screenshot;
   - the HTTP status and the response headers of the challenge exchange, with cookie and token values redacted.
   It goes under the existing capture root, and the event names the bundle path.
4. **ONE bounded retry** 60-120 s after the failure (a jittered sleep through an injectable clock), recorded as a
   second challenge event. No second retry. If the retry fails, capture again and end the leg `bot_check`, as today.
5. **Grader (ruling 8a)** in `load_window_grade.py`:
   - top level `"grain": "per_run"`;
   - per publisher, `runs` = [{run_id, in_window, challenges_presented, challenges_void, challenges_nonvoid,
     challenges_nonvoid_passed, run_verdict}];
   - per publisher, `window_pass_rate` = non-void passed / non-void presented over the windows, or null when none;
   - verdict NOT_EVALUATED when there is no windowed request; else MET-BY-ABSENCE when no challenge was presented in
     any windowed run; else MET when at least one in-window run has every presented challenge non-void and passed;
     else NOT-MET;
   - each retry attempt counts as its own challenge;
   - keep `requests_counted` and `--runtimes`, and keep the plain-text output in step.
6. Plants in `lib/opal_data_harvest/test_aj5_bbg_failure_capture_retry.py` (stub tab, stub clock, stub response, no
   network):
   - (i) a bbg article 403 classed bot_check reaches `solve()` and records `challenge_presented` plus the outcome;
   - (ii) a planted solve failure writes a bundle with all three parts, and no cookie or token value appears in it;
   - (iii) the retry fires once, 60-120 s later on the stub clock, as a second challenge event, and never a third;
   - (iv) per-run grading: one in-window run with all challenges passed plus one failed run gives MET, with
     window_pass_rate < 1; an all-failed window gives NOT-MET.
   Update only the superseded assertions in the existing grader tests, and name them. The suite stays green:
   `python -m pytest lib/opal_data_harvest/ -q` (base 546 passed, 3 skipped).

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r36-90`, branch `wk-AMGT_HARVST-90-r37c`, sparse cone per
decomposition section 50. Do not touch any `.runtime` directory.

<paths>
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/verification.py
lib/opal_data_harvest/challenge_capture.py
lib/opal_data_harvest/load_window_grade.py
lib/opal_data_harvest/test_aj5_bbg_failure_capture_retry.py
lib/opal_data_harvest/test_aj1_presentation_anchor.py
lib/opal_data_harvest/test_ai6_per_challenge_grade.py
lib/opal_data_harvest/test_ah2_load_window_grade.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aj-5"><invocation>python -m pytest lib/opal_data_harvest/test_aj5_bbg_failure_capture_retry.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aj-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/checks/aj-5.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 reads the real windows from the git root. In your worktree it cannot read them, so mark it "issuer re-runs at
  the base after merge".
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-aj-5.bbg-failure-capture-retry-per-run.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aj-5.bbg-failure-capture-retry-per-run`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO 28278 (YES; folded with addendum ruling 8, @1c693565e7). This is cell 5 of round 37 as an issuer
amendment. The ONE REAL RUN at close: the bbg driver restarts after the merge, under the monitor, and the next real
challenge either passes or leaves a capture bundle. Run 065754Z stays UNCLASSIFIED (8c). STOP_BBG is set until the
merge.

**COMPLETE 2026-10-02 ~08:0xZ (issuer).** AC1 PASS: 13 passed. Suite 561 at the base. Merged @7b3800219d. AC2 PASS at
the base over live windows 1-3 (`deliverables/2.0.0_SA_COO_H/round37/aj-5.AC2.output.txt`):
- `grain` per_run;
- bbg **MET** per run, with **window_pass_rate 0.9** (9 of 10 non-void; 63 of 157 runs in a window);
- wsj, barrons, ft and sa MET-BY-ABSENCE.

ONE REAL RUN: the bbg driver restarted at 08:06:20Z with `--clear-stop bbg` under monitor window3 (pid 37260). Its next
real challenge either passes or writes a capture bundle with one retry.

Issuer rulings on the worker's rows:
- **Z-W90-S13:** the path finding shows the 06:59 job DID reach `verification.solve()`. The failed solve emitted no
  event, and its capture is hour-capped and fires only once the control is located. Z-S64's "no solve event" stands;
  "reached no solve" was never claimed as established.
- **Z-W90-S15 ACCEPTED as narrowed:** the retry fires after a solve that did not pass. A solve that passed but whose
  re-sent request was challenged again gets the bundle and events but no retry, because retrying it breaks
  `test_ae5_hookup.py`, which is outside this cell's paths. That branch is carried to the round-37 analysis.
- **Z-W90-S16:** the grader's definitions (in-window = run span overlaps a window; unattributed challenges become their
  own run; counters over in-window runs only) are accepted.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>37</round>
<workstream>bbgcapture</workstream>
<slot>~90</slot>
<fabric>site-z</fabric>
