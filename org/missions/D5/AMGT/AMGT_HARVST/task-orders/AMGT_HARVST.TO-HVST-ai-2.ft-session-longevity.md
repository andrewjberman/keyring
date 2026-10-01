# AMGT_HARVST task order -- `HVST-ai-2` -- ROUND 36: ft SESSION LONGEVITY -- THE SESSION DIES ~20-30 MIN AFTER EACH RENEWAL; MAKE IT LAST A 2-HOUR RUN WITH NO LOGOUT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ai-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~92</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- WORLD: ft traffic from the box's own egress through the ft profile in the main tree's runtime; credentials only through the existing renewal path, never printed; no Secrets write; no gold write.
comp-adversary: RUN at L5 -- the adversary is a "2-hour run" that renews silently (a logout hidden by a renewal), or one whose span is padded by cooldown. AC2 requires 0 renewals and no auth-failure status across at least 120 minutes of jobs.
</preflight>

## 0. THE CELL (decomposition section 49; CTO round-35 ruling 4)

Round 35 (`HVST-ah-3`, merged @a78b06d3e6 / @9b14622a78) fixed the dead-session read and skips Premium teasers. Two
rows remain:

- **Z-W92-S12:** after a renewal, the ft session dies again ~20-30 minutes later. The worker renews once per job, so the
  job ends `auth_failed_after_refresh` and ft cools down for 60 minutes.
- **Z-W92-S11:** the backfill driver passes `--no-sign-in`, which refuses a dead saved session at the first fetch.

The ft backfill driver is OFF until a 2-hour run shows no logout. Code:
- `lib/opal_data_harvest/publishers.py`: `ft_page_state`, `AuthExpired`.
- `lib/opal_data_harvest/tab_transport.py`: `logged_in`, `seed`.
- `lib/opal_data_harvest/worker.py`: the renewal path.
- `lib/opal_data_harvest/contracts.json`.
- `lib/opal_data_harvest/backfill_driver.py`: read-only for you.

Your round-35 diagnosis: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/ah3_diagnosis.md`.

## 1. THE ACT

1. **DIAGNOSE (at most 30 ft requests).** Find what kills the session about 20-30 minutes after a renewal. Look at:
   - cookie expiry and refresh: which cookie lapses, and whether ft refreshes it on navigation but not on an in-tab
     `fetch()`;
   - a second session displacing the first (a concurrent login elsewhere, a re-seed overwriting a fresh cookie with the
     stale bundle copy);
   - an idle or keep-alive rule.

   Record the evidence in `ai2_diagnosis.md`.
2. **FIX** at the root, with plants in `lib/opal_data_harvest/test_ai2_ft_session.py`. Examples: refresh the session
   by navigation on a cadence, never re-seed a stale cookie over a live one, or persist the renewed cookies back to the
   bundle. Do NOT change `backfill_driver.py`. If the driver's `--no-sign-in` must change for ft, write a row (the
   issuer rules on the driver).
3. **RUN at least 120 minutes:** the real collector on ft names in driver order, cwd = your worktree,
   `--runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`, mirroring the
   driver's job invocation. Use Bash `run_in_background` per job and commit progress at least every 30 minutes. Write
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/ai2_ft_longevity.json` =
   `{"run_records": [<each job's run record, verbatim>]}`. Hard cap: 180 minutes of run.

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/tab_transport.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/contracts.json
lib/opal_data_harvest/test_ai2_ft_session.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ai-2"><invocation>python -m pytest lib/opal_data_harvest/test_ai2_ft_session.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ai-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round36/checks/ai-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- The collector suite (`python -m pytest lib/opal_data_harvest/ -q`, base 494 passed, 1 skipped) stays green.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/AMGT_HARVST.TO-HVST-ai-2.ft-session-longevity.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ai-2.ft-session-longevity`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-35 ruling 4. Rows Z-W92-S11/S12, disposed by Z-S55 (the driver stays OFF).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>36</round>
<slot>~92</slot>
<fabric>site-z</fabric>
