# AMGT_HARVST task order -- `HVST-aw-1` -- ROUND 50 (round-49 analysis ADDENDUM 1 item 2; CTO @3bf4e2ea1e): THE TAB OPENS ITS ORIGIN ON THE DOCUMENT, NOT THE FULL PAGE LOAD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~99</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants against a LOCAL http server on 127.0.0.1 only. NO publisher host (ft.com, wsj.com, barrons.com, bloomberg.com, seekingalpha.com) is contacted, no collector or backfill_driver is run, no S3 call, and never touch any `.runtime` directory (three live collection legs use the profiles there).
comp-adversary: RUN at L5 -- the adversary is a fix that only raises the timeout (the wait is still `load`), a named error that is swallowed into a bare TimeoutError, a context left open on failure, or a plant that contacts a real host.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/tab_transport.py`, `TabSession.__init__` (around line 81-96):
- It launches a persistent Chrome context on the publisher's profile, then runs `self.page.goto(origin)` (line 92) with NO
  `wait_until` and NO `timeout`, so Playwright waits for the full `load` event (every image, ad and script) for 30 s.
- On any exception it calls `self.close()` and re-raises; the collector records the job as `status: error` with
  `error_type: TimeoutError` (`lib/opal_data_harvest/worker.py:770-772`).
- Measured at the cut: since 18:39Z, 5 of 15 live jobs (bbg, wsj, barrons) ended `TimeoutError` with ZERO request attempts,
  right after the stored token was read. The tab needs only the origin's document and its cookies, never the full page load.

## 1. THE BUILD (LOCAL)

1. In `tab_transport.py`:
   - add a module constant `ORIGIN_TIMEOUT_MS = 60000`;
   - add `class OriginLoadTimeout(RuntimeError)`;
   - in `TabSession.__init__`, open the origin with `self.page.goto(origin, wait_until="domcontentloaded",
     timeout=ORIGIN_TIMEOUT_MS)`;
   - catch Playwright's `TimeoutError` (`playwright.sync_api.TimeoutError`) from that call ONLY and raise
     `OriginLoadTimeout("origin %s did not deliver its document within %d ms (publisher %s)" % (origin, ORIGIN_TIMEOUT_MS,
     publisher))` from it. The existing `except Exception: self.close(); raise` still closes the context on every failure.
   - Name `HVST-aw-1` in a comment at the change. Change nothing else in the file.
2. **Plants** in `lib/opal_data_harvest/test_aw1_origin_load_wait.py`. Each plant serves pages from a `http.server` bound to
   `127.0.0.1` on a free port in a background thread, and opens `TabSession(publisher, <tmp_path profile root>, origin,
   headless=True)`; no other host is contacted. Close every session in a `finally`.
   - (i) **load never fires:** the origin's HTML holds `<img src="/hang">`, and `/hang` sends headers then never finishes its
     body. `TabSession` opens and `session.page.url` starts with the origin. Set `ORIGIN_TIMEOUT_MS` (monkeypatch) to 5000 so
     the plant is bounded.
   - (ii) **document never arrives:** the origin path itself never answers; with `ORIGIN_TIMEOUT_MS` = 3000, the constructor
     raises `OriginLoadTimeout` (assert the type and that the message names the origin), and it is NOT a bare
     `playwright.sync_api.TimeoutError`.
   - (iii) **the mutant:** monkeypatch the page's `goto` so it waits for `load` with the same 5000 ms bound (wrap the original
     and force `wait_until="load"`); plant (i)'s origin then raises. This proves (i) tests the wait mode, not the timeout.
   - Keep the whole file under 60 s wall time.
3. The harvest suite stays green: `python -m pytest lib/opal_data_harvest -q -p no:cacheprovider`. Report the count.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/tab_transport.py
lib/opal_data_harvest/test_aw1_origin_load_wait.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~99/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aw-1"><invocation>python -m pytest lib/opal_data_harvest/test_aw1_origin_load_wait.py -rA --tb=line -p no:cacheprovider</invocation><expect>3 passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aw-1"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~99/AMGT_HARVST.TO-HVST-aw-1.origin-load-wait.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aw-1.origin-load-wait`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Round-49 analysis ADDENDUM 1 item 2 @3bf4e2ea1e; decomposition section 63.
- The close run is the issuer's: after the merge, the live legs' next jobs build tabs from the merged code, and the 5
  `TimeoutError` pairs are re-run with `--names`, each reaching its first request (ADDENDUM 1's proof).
- The five pairs: barrons `security-6c77e5f2f3cc198f`; wsj `security-6e124400d00ba71b`, `security-bbd3ca12bae63fd7`;
  bbg `security-0c64ed19785afcdf`, `security-0654d797b0d7a678`.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>50</round>
<slot>~99</slot>
<fabric>site-z</fabric>
