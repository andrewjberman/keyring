# AMGT_HARVST task order -- `HVST-ac-1` -- ROUND 30 chain 1: THE `bot_check` ATTEMPT CLASS (PRD v0.10 `C-HV-TRUST-TOKEN`) -- A BOT CHECK IS NEVER TOKEN EXPIRY, NEVER STARTS A SIGN-IN, STOPS THE LEG, AND IS WRITTEN TO THE DURABLE RUN RECORD (FWD-7, FWD-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ac-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~84</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; no collection run in this cell.
comp-iam: RUN at L5 -- no network: sockets blocked in every test and script; the runtime root is READ-ONLY. NO vendor call, NO S3 write.
comp-adversary: RUN at L5 -- the adversary is a classifier that reads a real expiry as a bot check (so a dead token is never refreshed), or a bot check as expiry (the crawl Andrew forbade). AC1 plants both: a session-invalid 401 still marks expiry; each kept bot-check body classifies bot_check and marks nothing expired.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO REQUEST TO ANY PUBLISHER, NO S3 WRITE, NO COLLECTION RUN.** Sockets are blocked in every test and script (assert it).
   The runtime root `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest` is READ-ONLY.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~84/scripts/`; outputs named `ac1_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~84/AMGT_HARVST.TO-HVST-ac-1.bot-check-attempt-class.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-ac-1.bot-check-attempt-class`.

<paths>
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/verification.py
lib/opal_data_harvest/bot_check.py
lib/opal_data_harvest/test_ac1_bot_check_class.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~84/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CONTRACT (PRD v0.10 `C-HV-TRUST-TOKEN`, `ROUND_ANALYSIS.round29.md` ruling 1)

**Measured at CLOUD `d0bc0a79f0`, from the runtime root:**
- Batch 1's four refusals were recorded in the run records with attempt class `other`: bbg `listing` 403, wsj `listing` 401,
  barrons `listing` 401, ft `listing` 403.
- Only TWO kept a body in `rejected_bodies/`:
  - `20260930T163418Z-wsj-241953e39e.body` (652 B): a DataDome page, `geo.captcha-delivery.com`, "Please enable JS and
    disable any ad blocker";
  - `20260930T164017Z-ft-feffdb1b13.body` (65,536 of 270,934 B): an FT "Security Verification" interstitial.
- bbg and barrons ended through `verification.py` ~:21, `RequestRejected("Browser verification repair did not restore HTTP
  access (...)")`. That path raises WITHOUT the response, so no body was kept.
- Under v0.9 a 401 that persists after backoff reads as expiry. So a reader of the record alone could mark a valid token
  expired.

**The changes:**
1. **A `bot_check` attempt class, decided by a SIGNATURE rule over the kept body.**
   - A small named-signature table: at least DataDome (`captcha-delivery.com`), FT Security Verification, bbg's press-and-hold
     page, and the PerimeterX / Cloudflare challenge families.
   - The attempt row writes `class: bot_check` and `signature: <name>`.
   - No signature means the class is unchanged.
2. **A bot check is never expiry.** A `bot_check` attempt never marks a token expired, never calls a sign-in or `refresh`,
   and ends that publisher's leg in the job with status `bot_check`.
3. **The repair-failed path keeps its body.** `verification.py` ~:21 raises carrying the refused response (status, url,
   content_type, the capped and redacted body), exactly as `transport` does for a rejection. So the next bbg and barrons refusal
   is classifiable.
4. **(AMENDMENT 1, PRD v0.11) Every refusal keeps a bounded body; a body-less refusal is `unclassified`, never expiry.**
   Every refusal path keeps its capped, redacted body. A refusal that still has NO body classes `unclassified`: it never marks
   a token expired and never starts a sign-in.
5. **The expiry branch still fires.** A 401 or 403 whose kept body says the session is invalid (not a bot signature),
   persisting after backoff, still marks expiry as in v0.9.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ac-1"><invocation>python -m pytest lib/opal_data_harvest/test_ac1_bot_check_class.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-ac-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~84/scripts/ac1_ac2_replay_kept_bodies.py</invocation><expect>NETWORK CALLS MADE: 0</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-ac-1"><invocation>python -m pytest lib/opal_data_harvest/ -rA --tb=line</invocation><expect>passed</expect></criterion>
</proof_of_spec>

**What each criterion must prove or print:**
- **AC1** asserts each of these; a mutant restoring each base behaviour fails:
  - (a) each signature classifies `bot_check` with its name;
  - (b) a `bot_check` attempt marks no token expired and makes 0 sign-in or `refresh` calls, and the job ends `bot_check`;
  - (c) a planted session-invalid 401 persisting after backoff STILL marks expiry (the positive arm);
  - (d) the repair-failed path keeps its body;
  - (e) a body with no signature keeps its prior class;
  - (f) (AMENDMENT 1) a planted body-less persistent 403 classes `unclassified`, marks no token expired, and makes 0 sign-in
    calls.
- **AC2:** replay the two kept batch-1 bodies (read-only) through the classifier. Print, per body:
  - the class and signature as DERIVED from the rule, never typed from the file name;
  - the record shape the new code writes.

  Then print, for bbg and barrons: `no body kept at batch 1 -- unclassifiable until the next refusal (change 3 keeps it)`.
  End with `NETWORK CALLS MADE: 0`.
- **AC3:** the base is commit `d0bc0a79f0`, pinned. Print the base and after pass counts. No test that passed at the base
  fails.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round29.md` @`d0bc0a79f0` section 4 item 1, ruling 1.
- **Premise corrected by measurement:** the analysis's criterion reads "the four batch-1 kept bodies". Only TWO exist; bbg's
  and barrons' refusals went through `verification.py`'s raise, which keeps none. Change 3 closes that, and AC2 names the two
  unclassifiable refusals instead of predicting them.
- The `<expect>`s are plain printed tokens.

**AMENDMENT 1 (issuer, 2026-09-30 ~17:3xZ, before dispatch) -- PRD v0.11 criterion (CTO msg, @`bb49eb7e76`).**
- Change 4 (every refusal keeps a bounded body; a body-less refusal is `unclassified`, never expiry) is added. The old change 4 is
  renumbered 5.
- AC1 adds plant (f): a body-less persistent 403.
- **Paths and invocations:** unchanged.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>30</round>
<slot>~84</slot>
<fabric>site-z</fabric>
