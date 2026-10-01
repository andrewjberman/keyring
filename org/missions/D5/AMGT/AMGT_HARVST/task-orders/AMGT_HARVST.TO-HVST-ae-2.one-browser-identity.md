# AMGT_HARVST task order -- `HVST-ae-2` -- ROUND 32 chain B: ONE BROWSER IDENTITY PER PUBLISHER -- A PERSISTENT PER-PUBLISHER CHROME PROFILE, REQUESTS MADE IN-TAB, NO REST COOKIES WRITTEN BACK OVER THE BROWSER SESSION, NO TLS / USER-AGENT SPLIT (FWD-13)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ae-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL: repo code and tests, and a headed Chrome against a 127.0.0.1 fixture. NO publisher request, NO AWS write, NO Secrets write.
comp-adversary: RUN at L5 -- the adversary is a transport that still sends from Python (a curl client wearing the browser's cookies) or a browser launched with the automation flag on. AC2 is the issuer's seam probe against a real Chrome: the server reports the User-Agent and cookie it actually received, and the tab reports navigator.webdriver.
</preflight>

## 0. THE CELL (decomposition section 45, cell `HVST-ae-2`; PRD v0.13 FWD-13, `C-HV-ONE-IDENTITY`)

**FWD-13, verbatim:** each publisher is reached by ONE browser identity: the session is used by the browser that earned
it. DONE WHEN, EXERCISED, per publisher: (a) one persistent per-publisher browser profile on the site Z box is the only
session source; (b) every request that carries that session presents the earning browser's TLS fingerprint and
User-Agent, or runs inside that browser's own tab; (c) no client writes cookies back over the browser session (a
before/after hash of the stored session reads unchanged except by the browser itself). This order builds the mechanism
(LOCAL); the per-publisher live exercise is graded in a later cell.

**What is wrong today (measured):**
- The REST clients present curl_cffi's Chrome TLS fingerprint (`impersonate="chrome"`) while sending the stored
  browser's Chrome 154 User-Agent: `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py` (the `impersonate` kwargs and
  the `bundle["user_agent"]` header update), `bloomberg_rest_fetch.py:64-69`; ft hard-codes a Chrome/126 User-Agent
  (`ft_rest_fetch.py:111`).
- `lib/opal_data_harvest/auth.py` `persist_http_cookies` (lines ~26-45) writes the REST client's cookie jar back over the
  stored browser envelope (`self.vault.save(publisher, envelope)`).
- The estate already makes requests inside a browser tab: `lib/opal_data_harvest/verification.py:164`,
  `page.evaluate("async url => {const r = await fetch(url, {credentials:'include'}); return {status:r.status,text:await r.text()};}", url)`,
  launched with `channel="chrome"`, `headless=False`, `args=["--no-first-run", "--disable-blink-features=AutomationControlled"]`.

## 1. THE BUILD (LOCAL)

1. **`lib/opal_data_harvest/tab_transport.py` (new): `TabSession(publisher, profile_root, origin, headless=False)`.**
   - Launches `playwright.sync_api` `chromium.launch_persistent_context(user_data_dir=<profile_root>/<publisher>,
     channel="chrome", headless=headless, args=["--no-first-run", "--disable-blink-features=AutomationControlled"])`.
     NO `user_agent` override, no extra headers: the browser presents its own TLS and User-Agent.
   - Opens ONE page and navigates it to `origin` (requests are same-origin from that tab).
   - `get(url, params=None, headers=None, **_ignored)` runs the request IN THE TAB with
     `fetch(url, {credentials:'include'})` (append `params` as a query string; pass no Python-side cookie or UA) and
     returns a response object with `status_code`, `text`, `content` (bytes, UTF-8 of text), `headers` (dict), `url`, and
     `json()`. It never touches Python-side cookies.
   - `evaluate(expression)` passes through to the page; `close()` closes the context; the profile directory persists.
   - `seed(cookies)`: imports cookies into the profile ONCE, only when the context holds no cookie for the origin's
     domain (the first-use bridge from the stored bundle, e.g. ad-1's `dowjones/{wsj,barrons}/session` secrets read by
     the caller). After seeding, the browser's own jar is the only session source.
   - A `default_profile_root()` that derives the site Z root from the existing runtime root (never a hard-coded drive or
     user path; CLAUDE.md: derive, don't hardcode).
2. **`lib/opal_data_harvest/auth.py`: no write-back.** `persist_http_cookies` stops writing over the browser envelope:
   it returns the envelope unchanged and records nothing to the vault (keep the signature; callers stay valid).
3. **`lib/opal_data_harvest/contracts.json`:** add `"transport": "tab"` to bbg, wsj, barrons and ft; sa stays
   `"transport": "rest"` (placement R7: sa keeps its route).
4. **The REST clients that remain (sa):** in `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py`, remove the
   `User-Agent` override from the bundle, so curl_cffi presents the User-Agent of the fingerprint it impersonates. In
   `ft_rest_fetch.py` and `bloomberg_rest_fetch.py`, remove the hard-coded / bundle User-Agent the same way (they are no
   longer the session's transport, but no client may present a split identity).
5. **`lib/opal_data_harvest/test_ae2_one_identity.py` (new), the plants** (each fails on the base behaviour): (i) with a
   fake page, `TabSession.get` issues exactly one `page.evaluate` fetch with `credentials:'include'` and sets no
   Python-side cookie or User-Agent; (ii) `persist_http_cookies` leaves the vault's stored bytes unchanged (SHA-256
   before == after); (iii) contracts.json reads `tab` for bbg, wsj, barrons, ft and `rest` for sa; (iv) no
   `User-Agent` literal or `bundle["user_agent"]` header assignment remains in the three CRO REST clients (read the
   files' text); (v) `default_profile_root()` contains no drive letter or user-name literal.
6. **The hookup is NOT yours:** `lib/opal_data_harvest/publishers.py` (another cell's file) will select `TabSession`
   for `"transport": "tab"` at the issuer's merge. Name in your report the constructor call it should make.

<paths>
lib/opal_data_harvest/tab_transport.py
lib/opal_data_harvest/auth.py
lib/opal_data_harvest/contracts.json
lib/opal_data_harvest/test_ae2_one_identity.py
org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py
org/tier1_exec/4.0.0_SA_CRO/scripts/ft_rest_fetch.py
org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

**Reads you may need (no write):** `lib/opal_data_harvest/verification.py`, `lib/opal_data_harvest/publishers.py`,
`lib/opal_data_harvest/conftest.py`, the issuer's probe
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae-2.AC2.py` (read it: it is the interface).
**Never:** a request to any publisher or proxy; a Secrets write; an edit to `publishers.py`.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ae-2"><invocation>python -m pytest lib/opal_data_harvest/test_ae2_one_identity.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ae-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 opens a headed Chrome window on this box against a 127.0.0.1 fixture; it sends nothing off the box.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-ae-2.one-browser-identity.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ae-2.one-browser-identity`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Analysis `ROUND_ANALYSIS.round31.md` @`309b2da963` section 4 item 2; brief IV.4 (the chrome146/Chrome 154 split, ft
  Chrome/126, `auth.py:24-41`), IV.5 (cookie bound to fingerprint).
- The CRO scripts are the collector's REST modules (loaded as `self._module`); the order is their grant for this cell.
- `ae-5` (the challenge path on this identity) is queued on the same slot after this drains and first light is graded.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>32</round>
<slot>~91</slot>
<fabric>site-z</fabric>
