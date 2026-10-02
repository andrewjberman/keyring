# AMGT_HARVST task order -- `HVST-ai-6` -- ROUND 36 DIRECT ACT (CTO ruling, self-drive tick 2 @bb3c328367): GRADE FWD-11 LIMB 2a PER CHALLENGE WITH A +/-2 MINUTE GUARD BAND

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ai-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code + plants; the grader reads the runtime monitor/run-record files read-only; no network, no S3, no Secrets.
comp-adversary: RUN at L5 -- the adversary is a grader that calls a challenge clean while hardware input sits inside its band (an off-by-one at the band edge, or a band measured from presentation only and not to resolution), or that lets one void challenge void its neighbours, its hour or its run. Plants pin both band edges and the one-void-voids-only-itself rule.
</preflight>

## 0. THE CELL (CTO ruling, self-drive tick 2 @bb3c328367)

`lib/opal_data_harvest/load_window_grade.py` grades FWD-11 limb 2a per MINUTE today
(`rule` "per_minute_guard_band", `GUARD_BAND_MINUTES` 1, `REQUIRED_CLEAN_MINUTES` 1440). The CTO replaced that rule:

- A challenge is CLEAN when no hardware input occurs from 2 minutes before its presentation to 2 minutes after its
  resolution. Otherwise it is VOID.
- A VOID challenge voids only itself, never its hour, its neighbours or the run.
- Limb 2a is MET for a publisher when it presented at least one challenge, at least one is non-void, and every
  non-void challenge passed.
- A publisher that presented none is MET-BY-ABSENCE.
- The 1,440-clean-minute count is dropped; no clean-minute count gates a verdict.

Read the grader's own docstring for how it reads the monitor windows (hardware input per minute; unmonitored minutes)
and how it places challenges (`challenge_presented` / `challenge_passed` / `challenge_failed` events at their `at`
minute; run-record `bot_check` attempts with no matching pass placed at the run's `finished_at`).

## 1. THE BUILD (LOCAL)

1. In `load_window_grade.py`, grade per challenge:
   - Each challenge has a presentation minute and a resolution minute. Where the events let you pair a presentation
     with its own pass or fail, use both. Otherwise presentation = resolution = the one event's minute.
   - Its band is [presentation - 2 min, resolution + 2 min], inclusive of both edge minutes.
   - A band minute with hardware input makes the challenge VOID.
   - A band minute that is UNMONITORED (no window covers it) also makes it VOID, because no input cannot be shown
     there. Say so in the docstring.
2. JSON output: top level `rule` = "per_challenge_guard_band" and `guard_band_minutes` = 2. Drop
   `required_clean_minutes`. Per publisher, emit:
   - `verdict`
   - `requests`
   - `challenges_presented`
   - `challenges_void`
   - `challenges_nonvoid`
   - `challenges_nonvoid_passed`
   Verdict order: MET-BY-ABSENCE if presented == 0; else NOT-MET if a non-void challenge did not pass; else
   INSUFFICIENT if every presented challenge is void; else MET. Keep the plain-text output in step with the JSON.
3. Plants in `lib/opal_data_harvest/test_ai6_per_challenge_grade.py`:
   - (i) input at presentation - 2 min voids the challenge, and input at presentation - 3 min does not;
   - (ii) input at resolution + 2 min voids it, and input at resolution + 3 min does not;
   - (iii) one void challenge next to a clean one leaves the clean one non-void (it voids only itself);
   - (iv) each verdict: MET, NOT-MET, INSUFFICIENT (all void) and MET-BY-ABSENCE (none presented);
   - (v) an unmonitored band minute voids the challenge.
4. Update `lib/opal_data_harvest/test_ah2_load_window_grade.py` wherever it asserts the superseded per-minute rule, so
   the collector suite stays green (`python -m pytest lib/opal_data_harvest/ -q`, base 534 passed, 3 skipped). Change
   only those assertions, and say which ones in your report.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r36-90`, branch `wk-AMGT_HARVST-90-r36f`. Run every command from
that directory. Do not touch any `.runtime` directory; AC2 reads the real windows read-only.

<paths>
lib/opal_data_harvest/load_window_grade.py
lib/opal_data_harvest/test_ai6_per_challenge_grade.py
lib/opal_data_harvest/test_ah2_load_window_grade.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ai-6"><invocation>python -m pytest lib/opal_data_harvest/test_ai6_per_challenge_grade.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ai-6"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round36/checks/ai-6.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 runs the amended grader over the REAL monitor windows, read-only, from your worktree. The runtime paths are
  absolute under `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/`, so read the grader for how it finds them.
  If it resolves them against the git root, which is your worktree, record that in the instance and the issuer
  re-runs AC2 at the base after the merge.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-ai-6.limb2a-per-challenge-grader.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ai-6.limb2a-per-challenge-grader`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ruling (self-drive tick 2 @bb3c328367; ADJUDICATION_v45 section 2): "2.0.0_SA_COO~H amends
the grader in its own order, and 3.0.0_SA_CVO~Z grades on it. No PRD half re-opens." DIRECT-ACT path (`/dispatch`): one LOCAL cell under 300 product lines; no L8-L10; its close is
the issuer's re-run of AC2 at the base after the merge. After the merge, ai-1's AC2 (which asserts the per-minute rule)
reads FAIL by supersession; that is expected and recorded in the round-36 packet. The unmonitored-band-minute VOID rule
(1.v) is the issuer's reading of "no hardware input occurs": an unmonitored minute cannot show that.

<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
<status>open</status>
<round>36</round>
<workstream>limb2a</workstream>
<slot>~90</slot>
<fabric>site-z</fabric>
