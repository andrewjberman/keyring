# AMGT_HARVST task order -- `HVST-aj-4` -- ROUND 37: THE ft KEEP-ALIVE RUN -- 2 HOURS FROM A SIGN-IN ANDREW SOLVES BY HAND, ONE KEEP-ALIVE EVENT PER PAGE LOAD (STAGED ON ANDREW)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aj-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~92</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 (AMENDED 13:1xZ) -- WORLD: ft traffic from the box's own egress through the ft profile in the main tree's runtime; the sign-in's hCaptcha is solved through the existing NopeCHA path, which Andrew permanently whitelisted for egress at 2026-10-02 ~13:08Z (record org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261002_130xZ_VENDOR_EGRESS_WHITELIST_NOPECHA_PERMANENT.md); Kimi and the vision fallback stay barred (0 calls); credentials and the NopeCHA key only through the existing Secrets path, never printed; no Secrets write; no gold write.
comp-adversary: RUN at L5 -- the adversary is a "2-hour session" that renews silently, a keep-alive that is configured but never fires (round 36: no keep-alive load appears in any run record), or a span padded by cooldown. AC2 requires one keepalive_page_load event per load at the contract cadence, 0 renewals and no auth-failure status across >= 120 min.
</preflight>

## 0. THE CELL (round-36 analysis ruling 5; CTO 28235)

Round 36, ai-2 attempt 3 (records `deliverables/0.9.0_WK_AMGT_HARVST~92/ai2_attempt3_summary.md`):
- the sign-in at 02:38:37Z met an hCaptcha, solved by hand;
- 74m45s later, job 3 ended `sign_in_refused` (401 under `--no-sign-in`);
- NO keep-alive page load appears in the run records, so `TabSession.keepalive` (`tab_transport.py`; the ft contract
  sets `session_keepalive_seconds` to 300) was never shown to fire in the real collector.

## 1. THE ACT -- BEGINS ONLY WHEN THE ISSUER HANDS THE GO (Andrew present)

1. **Instrument (no network):** every keep-alive page load records
   `{"event": "keepalive_page_load", "publisher": "ft", "at": <utc iso>, "url_kind": <home|article>, "logged_in": <bool>}`
   into the job's run record `events`. Plant it in `lib/opal_data_harvest/test_aj4_keepalive_event.py` with a stub
   tab and no network. A mutant that skips the record fails the plant.
2. **Sign-in (RE-AMENDED 16:4xZ, Andrew-direct ~16:47Z, option B):** ONE HEADED ft sign-in through the existing
   path, with ANDREW at the site-Z terminal solving the hCaptcha BY HAND. The NopeCHA Token API is discontinued (row
   Z-W92-S18), so there are 0 solver calls of any vendor. Wait up to 15 min for his solve, and record it as human-hand
   in the sign-in record (`solved_by` "andrew_hand"). The unattended route is option A, cell aj-6.
3. **Run at least 120 minutes:** the real collector on ft names in driver order, from your worktree, with
   `--runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`, mirroring the driver's
   job invocation. Use Bash `run_in_background` per job and commit progress at least every 30 minutes. Write
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/aj4_ft_keepalive.json`
   = `{"run_records": [<each job's run record, verbatim>]}`. Hard cap: 180 minutes.
4. If the session dies, stop and file a row with the time from sign-in and the last keep-alive event before the
   death. Do not sign in again.

<paths>
lib/opal_data_harvest/tab_transport.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/test_aj4_keepalive_event.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aj-4"><invocation>python -m pytest lib/opal_data_harvest/test_aj4_keepalive_event.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aj-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/checks/aj-4.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/AMGT_HARVST.TO-HVST-aj-4.ft-keepalive-run.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aj-4.ft-keepalive-run`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Ruling 5 and CTO 28235. This cell is a qualified wait: Andrew's own hand on the hCaptcha (analysis
section 4, act 1). A solver is a vendor use, and no word of Andrew's names one. The card goes to 0.0.0_AB_MSTR~Z for
Andrew. The instrument step (1) may be cut to a worker ahead of the GO; the sign-in and run wait on the GO.
Status: `staged` until Andrew is present. AMENDED 13:1xZ: Andrew permanently whitelisted NopeCHA for egress (record
above), so the sign-in no longer waits on his hand. The order goes `pending` and runs now.

**CANCELLED 2026-10-02 ~18:1xZ (issuer flip; precedent ai-2):** step 2 was re-amended to Andrew's hand-solved sign-in
(option B, Andrew-direct ~16:47Z). FTSession_s was saved 17:01Z and the run started 17:02Z.
- AC1 PASS.
- AC2 FAIL: the session got a 401 (sign_in_refused) at 17:25:05Z, 24m04s after the sign-in, despite 6 keepalive_page_load
  events about 3.3 min apart, all logged_in.
Row Z-W92-S20 carries it; the records were merged @1e6610290e.

The keep-alive does NOT hold an ft session: two hand-solved sessions died at about 75 min and at 24 min. FWD-11's ft
limb therefore needs an unattended re-sign-in, which depends on a working hCaptcha solver (aj-6 stage 2; row Z-S66). The
round-37 drain-end packet carries it. ft stays OFF (STOP_FT).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>cancelled</status>
<round>37</round>
<slot>~92</slot>
<fabric>site-z</fabric>
