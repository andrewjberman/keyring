# AMGT_HARVST task order -- `HVST-aj-6` -- ROUND 37 CELL 6 (CTO 28484; AMENDED on Andrew-direct ~13:3xZ): THE ft SIGN-IN'S hCAPTCHA SOLVED BY THE OCILAR API, UNATTENDED (THE NOPECHA TOKEN API IS DISCONTINUED)

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
comp-iam: RUN at L5 -- WORLD: ft traffic from the box's own egress through the ft profile in the main tree's runtime; Ocilar API egress (POST https://api.ocilar.com/api/v1/solve/hcaptcha) on Andrew's explicit word, 2026-10-02 ~13:3xZ ("LETS USE A NEW SOLVER", record org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261002_133xZ_USE_OCILAR_HCAPTCHA_SOLVER.md); the Ocilar key only from Secrets `ocilar/credentials` (us-east-1, field `api_key`), never printed, logged or written to a tracked file; NopeCHA, Kimi and the vision fallback NOT called (0); no Secrets write; no gold write.
comp-adversary: RUN at L5 -- the adversary is (a) a "solve" that is really a person's click (hardware_input must read none), (b) the key leaking into a committed file, a log line, an exception message or a run record, (c) a token injected into the wrong field so the form submits without it (the sign-in must yield the FTSession_s identity cookie), (d) a retry loop that burns credits. Plants pin (b) and (c) offline; the record pins (a); one attempt plus at most one retry pins (d).
</preflight>

## 0. THE CELL (row Z-W92-S18; CTO 28484; Andrew-direct ~13:3xZ)

The ft sign-in solves its hCaptcha through `nopecha.Token.solve`, in the CRO's
`org/tier1_exec/4.0.0_SA_CRO/scripts/nopecha_hcaptcha_lib.py` (called from `ft_harvest_session.py`). At 13:15Z NopeCHA
answered error 19: "This API endpoint has been discontinued". Andrew has chosen a new solver, Ocilar:

- `POST https://api.ocilar.com/api/v1/solve/hcaptcha`, header `X-API-Key: <key>`, JSON body
  `{"sitekey": "<data-sitekey>", "url": "<page url>"}`;
- response `{"token": "P1_...", "latency_ms": ..., "credits_used": 1}`; tokens are valid for 120 s; the average latency
  is 3-6 s;
- submit by setting the page's `[name="h-captcha-response"]` (and `[name="g-recaptcha-response"]` where present) to
  the token, then clicking the form's submit.

Read the CRO lib for how it finds the sitekey and injects the token, but do NOT edit it: it is the CRO's. Your
round-37 harness is `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/aj4_signin.py`, with its
record `aj4_signin.json`.

## 1. THE BUILD

1. **`lib/opal_data_harvest/ocilar_hcaptcha.py`:**
   - `extract_sitekey(page)`;
   - `solve(sitekey, url, key, http=...)`, which calls the Ocilar endpoint with stdlib `urllib` or the already
     installed `requests` (no new dependency) and a timeout, and returns the token;
   - `inject_and_submit(page, token, submit_selectors)`;
   - `read_key(secrets=...)`, which reads `ocilar/credentials` through the existing Secrets path.
   An exception message or log line never carries the key. Every call is counted for the record.
2. **The ft sign-in harness** (`aj6_signin.py`, adapted from `aj4_signin.py`) runs ONE unattended headed ft sign-in.
   When the hCaptcha appears it calls the Ocilar route; if the first token is rejected it retries ONCE. It records
   `aj6_signin.json` with:
   - started/finished;
   - `challenge_events`: challenge_presented, then challenge_passed or challenge_failed;
   - `solved_by` "ocilar", `ocilar_calls`, `ocilar_latency_ms`;
   - `nopecha_token_api_calls` 0, `kimi_vision_calls` 0, `hardware_input` "none";
   - `identity_cookie_names`, `saved_to_vault`.
   At most 2 sign-in attempts in total.
3. Plants in `lib/opal_data_harvest/test_aj6_ocilar_hcaptcha.py` (no network, no Chrome; stub HTTP and page):
   - (i) `solve` posts to the endpoint with the `X-API-Key` header and `{sitekey, url}` and returns the token;
   - (ii) a planted sentinel key appears in NO return value, log record, raised message or record file;
   - (iii) the token is written to `h-captcha-response` before submit (a mutant that skips the injection fails);
   - (iv) a non-200 or a missing token raises a solver error that names the status, not the key.

<paths>
lib/opal_data_harvest/ocilar_hcaptcha.py
lib/opal_data_harvest/test_aj6_ocilar_hcaptcha.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aj-6"><invocation>python -m pytest lib/opal_data_harvest/test_aj6_ocilar_hcaptcha.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aj-6"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/checks/aj-6.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 reads `deliverables/0.9.0_WK_AMGT_HARVST~92/aj6_signin.json` from the git root, which is your worktree.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/AMGT_HARVST.TO-HVST-aj-6.ft-signin-nopecha-extension.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aj-6.ft-signin-nopecha-extension`. The filename keeps the cell's original slug.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO 28484 YES'd the cell (WORLD, workstream ftsolver) on the NopeCHA-extension route. Andrew's
~13:3xZ word, "bETTER IDEA, LETS USE A NEW SOLVER" (Ocilar, key supplied), re-points it to the Ocilar API. The record is
@9bc0e127be and the key is in Secrets `ocilar/credentials`. The CTO lands the whitelist row. A successful aj-6 sign-in
leaves a live ft session, from which aj-4's 2 h keep-alive run (step 3) starts, re-handed to ~92. Routing the
collector's renewal through Ocilar is the composite-run (ruling 8d) step.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>37</round>
<workstream>ftsolver</workstream>
<slot>~92</slot>
<fabric>site-z</fabric>
