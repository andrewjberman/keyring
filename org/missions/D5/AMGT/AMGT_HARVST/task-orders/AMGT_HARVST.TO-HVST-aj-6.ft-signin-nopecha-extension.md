# AMGT_HARVST task order -- `HVST-aj-6` -- ROUND 37 CELL 6 (CTO 28484; RE-POINTED on Andrew-direct ~16:47Z, option A): THE ft SIGN-IN'S hCAPTCHA SOLVED BY THE NOPECHA BROWSER EXTENSION, UNATTENDED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aj-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- WORLD: NopeCHA egress under VEW-1 (org/ref/VENDOR_EGRESS_WHITELIST.yaml; Andrew-direct 2026-10-02 ~13:08Z "nopeCHA is permanently whitelisted for egress"): the extension download from NopeCHA's own published source, and the extension's own solve calls; the NopeCHA key only from Secrets, never printed or written to a tracked file; Ocilar, Kimi and the vision fallback NOT called (0); no Secrets write; no gold write. THIS STAGE (build) makes no ft request: the live sign-in is a later stage, after aj-4's 2 h run releases the ft profile.
comp-adversary: RUN at L5 -- the adversary is (a) an extension "solve" that is really the discontinued Token API (0 Token API calls must hold), (b) a sign-in that only looks unattended because a person clicked (hardware_input none), (c) the key leaking into a committed file or a log line, (d) an extension pulled from an unofficial source. Plants pin (a) and (c); the source record pins (d); the live record pins (b).
</preflight>

## 0. THE CELL

The ft sign-in solves its hCaptcha through `nopecha.Token.solve`, in the CRO's
`org/tier1_exec/4.0.0_SA_CRO/scripts/nopecha_hcaptcha_lib.py`. At 13:15Z NopeCHA answered error 19, "This API
endpoint has been discontinued" (row Z-W92-S18).

The Ocilar route (built and merged, `lib/opal_data_harvest/ocilar_hcaptcha.py`) waits on Ocilar's hcaptcha service,
which is not live (row Z-W92-S19). Andrew chose option A: NopeCHA's BROWSER EXTENSION, which solves an hCaptcha in the
page with the account key. VEW-1 covers it, and CTO 28484 said YES.

## 1. THE BUILD -- STAGE 1 (now; no ft request)

1. **Source the extension** from NopeCHA's own published release (their official GitHub releases, or the Chrome Web
   Store CRX). Record the URL, version and sha256 in
   `deliverables/0.9.0_WK_AMGT_HARVST~90/aj6_extension_source.md`. Do NOT commit the binary: cache it under
   `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/extensions/nopecha/`, which is gitignored.
   Writing that one cache directory is the only main-tree write.
2. **`lib/opal_data_harvest/nopecha_extension.py`:**
   - prepares the unpacked extension with the key set through the extension's own configuration mechanism;
   - takes the key from Secrets through the existing credentials path (read how `nopecha_hcaptcha_lib.py` gets its
     key), never printed or written to a tracked file;
   - returns the Chrome launch arguments that load it (`--load-extension`, `--disable-extensions-except`);
   - lets a test substitute the Secrets read and the filesystem.
3. **The sign-in harness** `deliverables/0.9.0_WK_AMGT_HARVST~92/aj6_signin_ext.py` (adapt the ~92 harness
   `aj6_signin.py`; you may write into the ~92 deliverables folder for this file only):
   - launches the ft profile headed, with the extension loaded;
   - lets the extension solve;
   - records `aj6_signin_ext.json` with `challenge_events`, `solved_by` "nopecha_extension",
     `nopecha_token_api_calls` 0, `kimi_vision_calls` 0, `hardware_input` "none", `identity_cookie_names`,
     `saved_to_vault`, and whitelist "VEW-1".
   Build and plant it; do NOT run it live in this stage.
4. Plants in `lib/opal_data_harvest/test_aj6_nopecha_extension.py` (no network, no Chrome):
   - (i) the launch arguments load exactly the prepared directory;
   - (ii) a planted sentinel key appears in no return value, log or file outside the runtime cache;
   - (iii) the module never imports or calls `nopecha.Token` (a mutant that calls it fails).
5. Do NOT edit `org/tier1_exec/4.0.0_SA_CRO/scripts/*`. The collector suite stays green:
   `python -m pytest lib/opal_data_harvest/ -q`.

**STAGE 2 (later, the issuer's GO):** after aj-4's 2 h run releases the ft profile, ONE live unattended ft sign-in with
`aj6_signin_ext.py`, under the same rules as above. At most 2 attempts in total.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r36-90`, branch `wk-AMGT_HARVST-90-r37h`.

<paths>
lib/opal_data_harvest/nopecha_extension.py
lib/opal_data_harvest/test_aj6_nopecha_extension.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/aj6_signin_ext.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/aj6_signin_ext.json
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aj-6"><invocation>python -m pytest lib/opal_data_harvest/test_aj6_nopecha_extension.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aj-6"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/checks/aj-6.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 reads `deliverables/0.9.0_WK_AMGT_HARVST~92/aj6_signin_ext.json`, written in stage 2. In stage 1, mark it
  "stage 2 (live sign-in) pending the issuer's GO".
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-aj-6.ft-signin-nopecha-extension.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aj-6.ft-signin-nopecha-extension`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** History of this cell:
- CTO 28484 YES'd it on the NopeCHA-extension route.
- Andrew ~13:3xZ re-pointed it to Ocilar; that attempt hit HTTP 503 (hcaptcha "coming"), row Z-W92-S19, and its code
  was merged @67cc4ecbcc.
- Andrew ~16:47Z approved open-calls option A+B (record
  `ANDREW_DIRECT_20261002_164xZ_OPEN_CALLS_RECS_APPROVED_FT_SOLVER_AB_OCILAR_RECHECK_30D.md`). This re-points the cell
  back to the extension.

It is re-issued to slot ~90 for the build, because ~92 holds aj-4's live 2 h ft run on the same profile. Stage 2
follows aj-4. The Ocilar route is kept; it is re-checked on 2026-11-01 (`scheduled_checks` HVST-RECHECK-OCILAR-1).

**CANCELLED 2026-10-02 ~18:3xZ (issuer flip; precedent ai-2):**
- Stage 1 (worker branch 5ff819a79f): AC1 PASS 15/15.
- Stage 2 (issuer GO ~18:05Z; branch a7b574e513 and 030b99819b): extension 0.6.1 loaded on the ft profile through CDP
  loadUnpacked. The hCaptcha was presented at 18:07:12Z and was NOT cleared in 150 s; no identity cookie; FTSession_s
  not saved; 1 of 2 attempts used, because the failure came after the challenge was presented.
- AC2 FAIL, 4 failures: solved_by nopecha_extension_failed; hardware_input detected:7042 (the machine was not
  input-quiet); no FTSession_s; challenge presented then failed.
- Token API, Kimi and vision calls were all 0.
Row Z-W90-S21 agrees with Z-S66: NopeCHA's current product documents no hCaptcha.

Option A is closed by measurement. The unattended ft sign-in has no working solver today: the NopeCHA Token API is
discontinued, the NopeCHA extension fails, and Ocilar's hCaptcha is "coming" (re-check 2026-11-01). Hand-solved
sessions die at 24-75 min.

Residue: the unpacked extension persisted in the ft profile's Secure Preferences. It is INERT, because both ft launchers
(`tab_transport.py:89` and the CRO `ft_harvest_session.py:285`) keep Playwright's default `--disable-extensions`.

ft stays OFF (STOP_FT). The round-37 drain-end packet carries FWD-11's ft limb.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>cancelled</status>
<round>37</round>
<workstream>ftsolver</workstream>
<slot>~90</slot>
<fabric>site-z</fabric>
