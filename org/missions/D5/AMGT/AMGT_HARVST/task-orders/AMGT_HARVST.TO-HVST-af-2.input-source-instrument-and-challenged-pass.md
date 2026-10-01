# AMGT_HARVST task order -- `HVST-af-2` -- ROUND 33: AN INPUT-SOURCE INSTRUMENT THAT TELLS A HUMAN HAND FROM INJECTED INPUT, THEN A CHALLENGED PASS RECORDED UNDER IT (FWD-11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-af-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- phase A LOCAL (a Windows low-level input hook, tests); phase B sends wsj/barrons/bbg traffic from the box's own egress (no residential arm), sign-ins inside the main-tree profiles, no Secrets write, no gold write.
comp-adversary: RUN at L5 -- the adversary is an instrument that cannot see the difference (GetLastInputInfo ticks for harness input too: row W91-S8) or a "challenged pass" in which no challenge was actually met. AC2 requires hardware events 0 from a hook that classes each event, and a met-and-passed challenge inside the window.
</preflight>

## 0. THE CELL (decomposition section 46, `HVST-af-2`; PRD v0.13 FWD-11; round-32 analysis item 2; row W91-S8)

**FWD-11 (the closing condition):** one unattended run on site Z, with NO HUMAN HAND at any point, meets each publisher's
live challenge and passes it. Round 32 passed bbg's press-and-hold unattended, but its evidence of "no human hand" was
`verification.last_operator_input()` (GetLastInputInfo), which ticks every 2-3 minutes with no human present -- it
cannot tell a human from injected input (row W91-S8). wsj and barrons were re-minted in clean profiles in round 32 and
met NO challenge, so no challenged pass exists for them yet.

## 1. PHASE A (LOCAL)

1. **`lib/opal_data_harvest/input_source.py` (new): `InputSourceMonitor`**, a context manager that installs Windows
   low-level hooks (`SetWindowsHookExW` with `WH_MOUSE_LL` and `WH_KEYBOARD_LL`, via `ctypes`, on its own thread with a
   message loop) and counts every OS input event as HARDWARE or INJECTED from the hook's flags (`LLMHF_INJECTED` /
   `LLKHF_INJECTED`, plus `LLMHF_LOWER_IL_INJECTED` / `LLKHF_LOWER_IL_INJECTED`). It records `window_start`,
   `window_end`, `hardware_input_events`, `injected_input_events` and the instrument name. Unhook on exit, always.
   Note: Playwright/CDP mouse input never reaches the OS hook at all; that is fine and is stated in the record.
2. **`verification.py`:** `solve()` and `renew()` accept an optional monitor and stamp `solved_at` (UTC ISO) on their
   outcome. No other change.
3. **`lib/opal_data_harvest/test_af2_input_source.py` (new)**, plants with a fake hook callback (no real hook in tests):
   (i) an event with the injected flag is counted injected, not hardware; (ii) an event without it is counted hardware;
   (iii) the monitor unhooks on exception; (iv) `solve()` stamps `solved_at` inside the monitor's window.
4. **A local seam run (no network):** with the monitor active, send ONE `SendInput` mouse move from Python; the record
   must read `injected_input_events >= 1` and `hardware_input_events == 0`. Keep its output (`af2_seam.out`).

## 2. PHASE B (WORLD) -- the challenged pass, under the monitor

1. With `InputSourceMonitor` active for the whole run: in the MAIN-tree profiles
   (`C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/browser-profiles/<pub>`), drive bbg's
   blocked route until its PRESS & HOLD challenge appears (the press-and-hold is met on bbg routes; round 32 met it) and
   solve it; for wsj and barrons, open the sign-in route in-profile and solve a DataDome slider if one is met (the
   re-minted sessions may meet none: record "none" honestly). Never more than 10 requests per publisher; never search.
2. Write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/af2_challenged_pass.json` in the shape
   the issuer's AC2 reads (open `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round33/checks/af-2.AC2.py`).
3. A publisher that meets no challenge is recorded `challenge_met: "none"`; a challenge met and not passed is recorded
   `passed: false` with the signature -- never a final state.

<paths>
lib/opal_data_harvest/input_source.py
lib/opal_data_harvest/test_af2_input_source.py
lib/opal_data_harvest/verification.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

**Reads you may need (no write):** `lib/opal_data_harvest/tab_transport.py`, `discovery.py`, `publishers.py`,
`org/tier1_exec/4.0.0_SA_CRO/scripts/press_and_hold_lib.py`, the round-32 record
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/ae5_unattended_run.json`. **Never:** the ft or sa
profiles or traffic (the issuer's running backfills), a residential proxy, a Secrets write, any vision/AI API.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-af-2"><invocation>python -m pytest lib/opal_data_harvest/test_af2_input_source.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-af-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round33/checks/af-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-af-2.input-source-instrument-and-challenged-pass.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-af-2.input-source-instrument-and-challenged-pass`.

## AMENDMENT 1 -- 2026-10-01 ~12:2xZ, the issuer, on the phase-B report (rows Z-W91-S11, S12, S13)

1. **Z-W91-S11 RULED:** the press-and-hold WAS met (run 1, a 403 on the in-tab sitemap fetch) but the run driver had no
   solve step, and the 10-request cap was spent. The challenged pass is now taken through the REAL collector path, where
   `PacedSession` routes a tab leg's bot check to `verification.route_bot_check` once (wired @a7dbc71874): run ONE bbg
   collector job for BA from the MAIN tree's runtime (`--runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`,
   `--publishers bbg --max-jobs 1`, backfill, floor 2026-01-01, `--new-only --no-sign-in`) with `InputSourceMonitor`
   active for the whole job. Fresh budget: at most 15 bbg requests (stop the job past that). Record the job's
   `challenge_passed` / `bot_check` events and the run record; build `af2_challenged_pass.json` from them (bbg's
   `challenge_met` = the signature, `path` = the solver, `passed`, `solved_at`).
2. **Z-W91-S12 RULED:** in `solve()`, a "Frame was detached" while locating the control re-locates ONCE on the page's
   current frames (no new request); a second detach ends the solve `passed: false`. Plant it in
   `test_af2_input_source.py`.
3. **Z-W91-S13 RULED INERT:** 12 injected events in a 2-minute window with no hardware events is the harness's own
   synthetic input -- exactly what the monitor exists to separate; it does not weaken the "no human hand" reading.
4. **Sequencing:** bbg is ONE seat at a time. This re-run starts only after `HVST-af-4`'s live bbg job has ended (the
   issuer hands it over then). wsj and barrons are not re-run (no challenge was met; recorded "none").

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-32 analysis @`749ec2c72e` item 2; row W91-S8 (ruled in Z-S52). Authority: R-21; placement R7.
No never-widen pair: no served gold moves.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>33</round>
<slot>~91</slot>
<fabric>site-z</fabric>
