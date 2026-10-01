# AMGT_HARVST task order -- `HVST-ai-1` -- ROUND 36: GRADE FWD-11 LIMB 2a PER MINUTE WITH A +/-1 MINUTE GUARD BAND (1,440 CLEAN MINUTES; EVERY CLEAN-MINUTE CHALLENGE PASSES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ai-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL, read-only over runtime files; no network.
comp-adversary: RUN at L5 -- the adversary is a challenge solved within a minute of human input counted as unattended. The guard band voids the challenge's own minute and its two neighbours.
</preflight>

## 0. THE CELL (decomposition section 49; CTO round-35 ruling 1)

`lib/opal_data_harvest/load_window_grade.py` currently grades by clock hour: an hour is clean only if none of its
minutes is void. People use this box in every clock hour, so the limb could never be reached. The new rule:

- **Clean minute:** a monitored minute with no hardware input. A minute outside every monitor window is unmonitored and
  is never clean. A window with hardware input and no per-minute buckets voids every one of its minutes.
- **Clean-minute challenge:** a challenge whose own minute AND the minute before AND the minute after all have no
  hardware input (the +/-1 guard band).
- **`clean_minutes`:** clean minutes in which the publisher made at least 1 request.
- **Verdict:**
  - INSUFFICIENT if `clean_minutes` < 1440;
  - else NOT-MET if any clean-minute challenge did not pass;
  - else MET-BY-ABSENCE if no challenge was presented in a clean minute;
  - else MET.

## 1. THE BUILD (LOCAL)

1. Re-shape the grader to the rule above. Keep the existing inputs (`runtimes.json`, monitor windows, events,
   `runs/*.json`) and the existing challenge-presented rule.
2. `--json` adds at the top level: `rule: "per_minute_guard_band"`, `guard_band_minutes: 1`,
   `required_clean_minutes: 1440`. Per publisher it adds `clean_minutes`, `clean_minute_challenges_presented` and
   `clean_minute_challenges_passed`. Keep `requests`, `challenges_presented` and `verdict`.
3. Human output prints the request count and the denominators.
4. Re-write the plants in `lib/opal_data_harvest/test_ah2_load_window_grade.py` for the new rule:
   - a challenge with hardware input in the minute before is not clean;
   - 1,439 clean minutes reads INSUFFICIENT;
   - 1,440 clean minutes with no clean challenge reads MET-BY-ABSENCE;
   - a failed clean challenge reads NOT-MET;
   - an unmonitored minute is not clean;
   - a window with no buckets voids every minute.

<paths>
lib/opal_data_harvest/load_window_grade.py
lib/opal_data_harvest/test_ah2_load_window_grade.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ai-1"><invocation>python -m pytest lib/opal_data_harvest/test_ah2_load_window_grade.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ai-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round36/checks/ai-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 is graded over the live data, so it MUST run with cwd = the main tree after the drain (the issuer re-runs it). In
  your worktree, record its output and say which tree it ran in.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-ai-1.per-minute-guard-band-grade.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ai-1.per-minute-guard-band-grade`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-35 ruling 1 (`ledger/ROUND_ANALYSIS.round35.md` @89539ccbc2). The CTO reports the reading to
Andrew; his word overrides it.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>open</status>
<round>36</round>
<slot>~90</slot>
<fabric>site-z</fabric>
