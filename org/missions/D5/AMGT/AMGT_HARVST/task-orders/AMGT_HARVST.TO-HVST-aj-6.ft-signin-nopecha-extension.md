# AMGT_HARVST task order -- `HVST-aj-6` -- ROUND 37 CELL 6 (CTO 28484; VEW-1): THE ft SIGN-IN'S hCAPTCHA SOLVED BY THE NOPECHA BROWSER EXTENSION, UNATTENDED (THE TOKEN API IS DISCONTINUED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aj-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~92</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- WORLD: ft traffic from the box's own egress through the ft profile in the main tree's runtime; NopeCHA egress (extension download from NopeCHA's own published source + the extension's own solve calls) under VEW-1 (org/ref/VENDOR_EGRESS_WHITELIST.yaml; Andrew-direct 2026-10-02 ~13:08Z, "nopeCHA is permanently whitelisted for egress"); the NopeCHA key only from Secrets, never printed or written to a file in the repo; Kimi and the vision-API fallback BARRED (0 calls); no Secrets write; no gold write.
comp-adversary: RUN at L5 -- the adversary is (a) an extension "solve" that is really the discontinued Token API (the record must show 0 Token API calls), (b) a sign-in that only looks unattended because a person clicked (hardware_input must read none from the input-source monitor or the harness's own instrument), (c) the key leaking into a committed file or a log line, (d) an extension pulled from an unofficial source. Plants pin (a) and (c); the record pins (b); the finding pins (d).
</preflight>

## 0. THE CELL (row Z-W92-S18; CTO 28484)

The ft sign-in solves its hCaptcha through `nopecha.Token.solve`, in the CRO's
`org/tier1_exec/4.0.0_SA_CRO/scripts/nopecha_hcaptcha_lib.py` (called from `ft_harvest_session.py`). At 13:15Z NopeCHA
answered error 19: "This API endpoint has been discontinued". NopeCHA still ships a browser extension that solves an
hCaptcha in the page with the account key. The account was on the Starter plan (2,000 credits) at 2026-09-15.

Your round-37 harness: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/aj4_signin.py`, and
its record `aj4_signin.json`.

## 1. THE BUILD

1. **Source the extension** from NopeCHA's own published release (their official GitHub releases or the Chrome Web
   Store CRX). Record the URL, version and sha256 in `aj6_extension_source.md`. Do NOT commit the extension binary:
   it is cached under the main-tree runtime, which is gitignored.
2. **`lib/opal_data_harvest/nopecha_extension.py`:**
   - prepares the unpacked extension with the key set through the extension's own configuration mechanism;
   - takes the key from Secrets through the existing credentials path, never printed or written to a tracked file;
   - returns the Chrome launch arguments that load it (`--load-extension`, `--disable-extensions-except`);
   - lets a test substitute the Secrets read and the filesystem.
3. **The ft sign-in harness** (your `aj6_signin.py`, adapted from `aj4_signin.py`) launches the ft profile headed,
   with the extension loaded, and lets the extension solve the hCaptcha. It records:
   - a `challenge_events` list, with challenge_presented when the hCaptcha appears and challenge_passed or
     challenge_failed when the sign-in completes or fails;
   - `nopecha_token_api_calls` (must be 0: the harness must not call `nopecha.Token`);
   - `kimi_vision_calls` 0;
   - `hardware_input` "none", read by the input-source instrument the harness already uses;
   - `identity_cookie_names`, `saved_to_vault`, `solved_by` "nopecha_extension".
   If the extension cannot solve it, record why and try the Recognition API fallback ONCE, under VEW-1. Never loop.
   At most 2 sign-in attempts in total.
4. Plants in `lib/opal_data_harvest/test_aj6_nopecha_extension.py` (no network, no Chrome):
   - (i) the launch arguments load exactly the prepared extension directory;
   - (ii) the key is set in the extension's configuration and appears in NO return value, log record or file outside
     the runtime cache (planted sentinel key);
   - (iii) the module never imports or calls `nopecha.Token` (a mutant that calls it fails).
5. Do NOT edit `org/tier1_exec/4.0.0_SA_CRO/scripts/*`, which is the CRO's. If the collector's own renewal must route
   through the extension, file a row naming the call site.

<paths>
lib/opal_data_harvest/nopecha_extension.py
lib/opal_data_harvest/test_aj6_nopecha_extension.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aj-6"><invocation>python -m pytest lib/opal_data_harvest/test_aj6_nopecha_extension.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aj-6"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/checks/aj-6.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 reads `deliverables/0.9.0_WK_AMGT_HARVST~92/aj6_signin.json` from the git root, which is your worktree.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/AMGT_HARVST.TO-HVST-aj-6.ft-signin-nopecha-extension.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aj-6.ft-signin-nopecha-extension`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO 28484 (YES; WORLD; workstream ftsolver), under VEW-1. A successful aj-6 sign-in leaves a live
ft session. aj-4's 2 h keep-alive run then starts from it, as aj-4 step 3, re-handed to ~92. Collector-renewal routing
through the extension is the composite-run (ruling 8d) step; it is not this cell.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>37</round>
<workstream>ftsolver</workstream>
<slot>~92</slot>
<fabric>site-z</fabric>
