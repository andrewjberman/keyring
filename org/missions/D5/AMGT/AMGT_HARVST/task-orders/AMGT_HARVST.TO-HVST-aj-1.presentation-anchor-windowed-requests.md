# AMGT_HARVST task order -- `HVST-aj-1` -- ROUND 37: ANCHOR EACH LIMB-2a BAND ON THE CHALLENGE'S PRESENTATION, AND COUNT REQUESTS INSIDE THE MONITOR WINDOWS ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code + plants; the grader reads runtime monitor/run-record files read-only; the transport emission writes only the collector's own run-record event list; no network in tests, no S3, no Secrets.
comp-adversary: RUN at L5 -- the adversary is a band anchored on the PASS minute (so input between the 403 and the pass is missed), or a request count that still includes traffic outside every monitor window (so an unmonitored publisher reads MET-BY-ABSENCE instead of NOT_EVALUATED). Plants: a presentation 3 min before its pass with input inside the band reads VOID; a publisher with requests only outside the windows reads NOT_EVALUATED.
</preflight>

## 0. THE CELL (round-36 analysis ruling 1; `ledger/ROUND_ANALYSIS.round36.md` @e38e50aa55)

`lib/opal_data_harvest/load_window_grade.py` (rule `per_challenge_guard_band`, +/-2 min) needs two corrections.

1. **The band starts too late.** Today it starts at the challenge's own event minute. bbg does not emit
   `challenge_presented`, so a band is anchored near the PASS. The ruling: anchor each band on the PRESENTATION as the
   run records it. bbg must emit `challenge_presented` from its path, at the moment the bot-check response is classed.
   Until a record carries it, the grader anchors on the HTTP 403 (the bot_check-class request attempt) that precedes
   each pass in the same run.
2. **The `requests` count is unwindowed.** `requests` counts every request, so barrons (52 requests on 2026-09-15,
   outside every window) reads MET-BY-ABSENCE. The ruling: count requests inside the monitor windows only. A
   publisher with 0 windowed requests reads NOT_EVALUATED, never MET-BY-ABSENCE.

`lib/opal_data_harvest/transport.py` records `challenge_passed` around line 305 (`PacedSession`). The bot_check
classification happens in `PacedSession.get`.

## 1. THE BUILD (LOCAL)

1. In `transport.py`, at the point a response is classed `bot_check`, record ONE
   `{"event": "challenge_presented", "publisher": ..., "at": <utc iso>}` through the same `self.record` that writes
   `challenge_passed`. Add nothing else to the live path.
2. In `load_window_grade.py`:
   - a challenge's presentation is its `challenge_presented` event when the run carries one;
   - otherwise it is the timestamp of the preceding bot_check/403 request attempt in the same run (read the run
     record's request attempts);
   - otherwise it is the pass or fail minute, as today, and the docstring says so;
   - count `requests` only where the request's minute is inside a monitor window;
   - verdict order: NOT_EVALUATED when windowed requests == 0, before MET-BY-ABSENCE;
   - emit top level `"requests_counted": "inside_monitor_windows"`.
   Keep `--runtimes` working, and keep the plain-text output in step.
3. Plants in `lib/opal_data_harvest/test_aj1_presentation_anchor.py`:
   - (i) a presentation 3 min before its pass, with hardware input 1 min after the presentation (inside the band, more
     than 2 min before the pass), reads VOID;
   - (ii) a run with only a 403 attempt and a later pass, no `challenge_presented`, anchors on the 403 time;
   - (iii) a publisher whose requests all fall outside the windows reads NOT_EVALUATED with requests 0;
   - (iv) the transport records `challenge_presented` when a response is classed bot_check (stubbed response, no
     network).
4. Update only the assertions the change supersedes in `test_ai6_per_challenge_grade.py` and
   `test_ah2_load_window_grade.py`, and name them. The collector suite stays green:
   `python -m pytest lib/opal_data_harvest/ -q` (base 541 passed, 3 skipped).

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r36-90`, branch `wk-AMGT_HARVST-90-r37a`, sparse cone per
decomposition section 50. Run every command from that directory. Do not touch any `.runtime` directory.

<paths>
lib/opal_data_harvest/load_window_grade.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/test_aj1_presentation_anchor.py
lib/opal_data_harvest/test_ai6_per_challenge_grade.py
lib/opal_data_harvest/test_ah2_load_window_grade.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aj-1"><invocation>python -m pytest lib/opal_data_harvest/test_aj1_presentation_anchor.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aj-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/checks/aj-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 re-grades ROUND 36's windows over the real run records. The pinned file
  `deliverables/2.0.0_SA_COO_H/round37/runtimes.round36_windows.json` lists windows 1 and 2. AC2 expects bbg 9
  non-void and 9 passed, barrons NOT_EVALUATED with requests 0, and `requests_counted` set. The runtime paths resolve
  against the git root, so in your worktree AC2 cannot read the real windows. Mark it "issuer re-runs at the base after
  merge"; do not copy or link `.runtime` data.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-aj-1.presentation-anchor-windowed-requests.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aj-1.presentation-anchor-windowed-requests`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-36 analysis ruling 1 and enrichment item 1. The CVO's true-band re-derivation
(ADJUDICATION_v47 s.2(a), s.5) gives bbg 9/9 on round 36's windows. If the worker's anchor gives a different number,
that is a row, not a re-pin. The transport emission is the live-path half: the bbg, wsj and sa drivers spawn a fresh
collector per job, so the merge reaches them at their next job.

**COMPLETE 2026-10-02 ~07:1xZ (issuer).** AC1 PASS (5 passed; suite 546). Merged @fdd7442696. AC2 PASS at the base over
round 36's pinned windows (`deliverables/2.0.0_SA_COO_H/round37/aj-1.AC2.output.txt`):
- `requests_counted` is inside_monitor_windows;
- bbg MET, 27 presented, 18 void, **9 non-void, 9 passed**, reproducing the CVO's true-band 9/9 on the 403 anchor;
- barrons **NOT_EVALUATED, 0 windowed requests**;
- wsj, ft and sa MET-BY-ABSENCE.

The worker's row Z-W90-S12: run-record attempts carry no timestamp, so the anchor is the http-ledger 403 inside the
run span. Only test_ai6's `test_all_four_verdicts` changed.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>37</round>
<slot>~90</slot>
<fabric>site-z</fabric>
