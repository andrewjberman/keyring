# AMGT_HARVST task order -- `HVST-aw-2` -- ROUND 50 (round-49 analysis ADDENDUM 1 item 1; CTO @3bf4e2ea1e; Andrew-direct ~19:2xZ): SEEKING ALPHA ON THE TAB PATTERN, NO PROXY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aw-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~100</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants, plus ONE live probe of seekingalpha.com (Andrew-direct ~19:2xZ worded SA collection on this pattern), at most 4 requests, made in-tab from the signed-in profile named below. No other publisher host, no proxy, no collector or backfill_driver run, no S3 call. The only `.runtime` path touched is the sa profile through the env var below; never any other profile or runtime file.
comp-adversary: RUN at L5 -- the adversary is a path that still reaches `sa_rest_fetch.build_session` (the curl + residential-proxy session), a proxy left in the path, a check that reads the user id from anywhere but the profile's own jar, or a probe that prints a cookie value.
</preflight>

## 0. THE CELL

Seeking Alpha is collected today through `sa_rest_fetch.build_session`: a curl session, cookies replayed from a stored bundle,
egress through a Bright Data residential proxy (`lib/opal_data_harvest/contracts.json` sa `"egress": "existing-residential-proxy"`,
`"transport": "rest"`). Since 2026-10-06 01:12Z, the proxy refuses the site (HTTP 402, "no KYC" access mode). Andrew's word moves
SA to the pattern the other publishers use: its own persistent Chrome profile, signed in by hand once (Google), and the SA REST
endpoints called INSIDE that tab.

Measured at the cut (issuer probe, 19:3xZ): in profile `browser-profiles/sa`, after Andrew's Google sign-in, an in-tab
`fetch` with `credentials: 'include'` and a `Referer` header answered:
- `GET /api/v3/account/<id>/info` -> 200 (4,774 B);
- `GET /api/v3/symbols/aapl/news?...&page[size]=5` -> 200, 5 items.

Where the code is (`lib/opal_data_harvest/publishers.py`):
- `TAB_ORIGINS` (line ~25) holds ft, wsj, bbg, barrons.
- `Publisher._ensure_session` (line ~352): a contract with `"transport": "tab"` builds
  `TabSession(pub, str(default_profile_root()), TAB_ORIGINS[pub])` and loads `self._module = legacy(...)` only for ft and bbg;
  the `elif pub in {"sa", "ft", "bbg"}` branch (line ~375) is today's sa path (`build_session(bundle=bundle)`, then `inner[0]`).
- `check_auth` (line ~560) calls `self.module.check(self.session)`; `seeking_alpha()` calls `self.module.news(...)` and
  `self.module.get_json(...)`. These helpers live in `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py` (READ ONLY here): each
  calls `s.get(BASE + path, headers={Accept, Accept-Language, Referer})`, which `TabSession.get(url, headers=...)` already serves
  in-tab. `check(s)` reads `s.sa_user_id` and requires it to match `USER_ID_SHAPE`; the user id is the value of the cookie named
  `IDENTITY_COOKIE` (`"user_id"`) on seekingalpha.com.
- `TabSession` (`lib/opal_data_harvest/tab_transport.py`, READ ONLY here -- another cell owns it this round) exposes
  `self.context.cookies([origin])`.

## 1. THE BUILD (LOCAL)

1. `contracts.json`, sa: `"transport": "tab"`, `"egress": "native in-tab (persistent profile browser-profiles/sa; no proxy;
   Andrew-direct 2026-10-06 ~19:2xZ)"`, and `"seed_from_bundle": false`. Change no other key and no other publisher.
2. `publishers.py`:
   - `TAB_ORIGINS["sa"] = "https://seekingalpha.com"`;
   - in the tab branch of `_ensure_session`, load `legacy("sa_rest_fetch")` for sa as well (as for ft and bbg), and for sa set
     `inner.sa_user_id` to the `user_id` cookie's value read from `inner.context.cookies([TAB_ORIGINS["sa"]])` (None if absent,
     so `check` raises its own `NotAuthorized`). No cookie value is logged or printed.
   - The sa path never calls `sa_rest_fetch.build_session` any more; remove sa from the `elif` set (it is reached only by ft and
     bbg if their contracts ever leave `tab`). Name `HVST-aw-2` in a comment at each change.
3. **Plants** in `lib/opal_data_harvest/test_aw2_sa_tab.py` (no network; monkeypatch `lib.opal_data_harvest.tab_transport.TabSession`
   with a fake whose `context.cookies()` returns a planted `user_id` and whose `get()` returns planted responses):
   - (i) the sa contract reads `transport` `tab` and its egress names no proxy; `TAB_ORIGINS["sa"]` is the SA origin;
   - (ii) building an sa `Publisher`'s session constructs the fake `TabSession` with origin `https://seekingalpha.com`, sets
     `sa_user_id` from the planted cookie, and NEVER calls `sa_rest_fetch.build_session` (patch it to raise);
   - (iii) `check_auth` on a planted 200 account body with `data.type == "authorizedUser"` passes, and on a planted
     `data.type == "anonymousUser"` raises `AuthExpired`;
   - (iv) the mutant: restore the old sa route (call `build_session`) and (ii) fails.
4. **Existing tests** that pin the OLD sa route (curl session / proxy / `transport: rest`) may be updated to the new route, and
   only for that reason; list each file and the assertion you changed in your report. Leave every other assertion unchanged.
5. **The live probe** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~100/aw-2.live_probe.py`:
   - run it with `OPAL_HARVEST_PROFILE_ROOT="C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/browser-profiles"`
     so it opens the SIGNED-IN sa profile (the profile root otherwise follows your worktree, which has none);
   - build an sa `Publisher` session through the real `_ensure_session` (the same path the collector uses), then make exactly
     these calls through it, at least 15 s apart: `module.check(session)`; `module.news(session, "AAPL", limit=5)`; and
     `module.article(session, <the first news item's id>)`;
   - print one line per endpoint class: `account <status>`, `listing <status> items=<n>`, `article <status> body_chars=<n>`,
     then `ALL 200` only if all three were 200. Never print a cookie, header or token. Close the session in a `finally`.
   - Write its output beside it as `aw-2.live_probe.out`.
   - Run it ONCE. If a call answers non-200, do not retry: record the status, file a surprise row, and report.
6. The harvest suite stays green: `python -m pytest lib/opal_data_harvest -q -p no:cacheprovider`. Report the count.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/contracts.json
lib/opal_data_harvest/test_aw2_sa_tab.py
lib/opal_data_harvest/test_ai3_capture_all.py
lib/opal_data_harvest/test_ae2_hookup.py
lib/opal_data_harvest/test_ae1_sa_listing_body.py
lib/opal_data_harvest/test_ae2_one_identity.py
lib/opal_data_harvest/test_n1_received_bytes_and_run_record.py
lib/opal_data_harvest/test_retrieval_provenance.py
lib/opal_data_harvest/test_check_as_received.py
lib/opal_data_harvest/test_harvest_grammar.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~100/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aw-2"><invocation>python -m pytest lib/opal_data_harvest/test_aw2_sa_tab.py -rA --tb=line -p no:cacheprovider</invocation><expect>4 passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aw-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~100/aw-2.live_probe.out</invocation><expect>ALL 200</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-aw-2"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~100/AMGT_HARVST.TO-HVST-aw-2.sa-tab-pattern.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aw-2.sa-tab-pattern`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Round-49 analysis ADDENDUM 1 item 1 @3bf4e2ea1e; decomposition section 63. Cut on the probe's 200 (issuer probe 19:3xZ,
  scratchpad `sa_tab_probe.py`: account 200 / 4,774 B; listing 200 / 5 items; RESULT OK), Andrew signed in by hand ~19:3xZ.
- Write set disjoint from `aw-1` (which owns `tab_transport.py` and its own test).
- The close run is the issuer's: after the merge, the sa leg resumes from `r47_sa_checkpoint.json` (root
  `.runtime/opal-data-harvest-sa`, `--clear-stop sa`) and its account check must answer 200.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>50</round>
<slot>~100</slot>
<fabric>site-z</fabric>
