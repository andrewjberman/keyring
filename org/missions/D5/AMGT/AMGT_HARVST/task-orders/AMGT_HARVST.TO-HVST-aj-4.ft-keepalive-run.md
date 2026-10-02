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
comp-iam: RUN at L5 -- WORLD: ft traffic from the box's own egress through the ft profile in the main tree's runtime; the sign-in is ONE headed sign-in whose hCaptcha Andrew solves by hand while present; credentials only through the existing Secrets path, never printed; NO solver vendor (Kimi, NopeCHA) -- 0 calls; no Secrets write; no gold write.
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
2. **Sign-in:** ONE headed ft sign-in through the existing path, with Andrew watching. He solves the hCaptcha by
   hand; no solver vendor is called, which the run records show as 0 calls.
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
Status: `staged` until Andrew is present.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>staged</status>
<round>37</round>
<slot>~92</slot>
<fabric>site-z</fabric>
