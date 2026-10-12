# ETFS_RIVALS task order -- `RIV-xb-1` -- THE LOOKUP'S SEARCH RETRIES A VENDOR 5xx OR A TRANSPORT FAILURE, AT MOST TWICE, NEVER A 4xx

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~35</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file(s) (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-xb-1` -- the lookup's search retries a vendor 5xx or a transport failure, at most twice with backoff, never a 4xx (round 28 analysis section 2.2) -- APPENDED 2026-10-12, revision 1.29
- Placement: `ledger/ROUND_ANALYSIS.round28.md` section 2.2 and section 3 item 2 (msg 4558).
- Measured (2026-10-12, zone `serp_opal`, this seat's `WI1_SCRATCH_WALK_20261012.md`): 5 of 9 Bright Data searches failed (4
  `VENDOR`: HTTP 200 with `x-brd-status-code` 502, `brd_error_code` `expect_element`; 1 `TRANSPORT`); the same query failed
  once and succeeded once. `serp.classify_serp_attempt` classes a failure `VENDOR` (5xx or a vendor-error header),
  `TRANSPORT` (no HTTP status or a connection error) or `CONFIG` (a 4xx). `dramatic_move.serp_search` (about line 341) makes
  ONE call and raises `RuntimeError("SERP FAILED: <kind>")`; `run_for_day` counts that as `failed` and the candidate waits for
  the next walk.
- Interface: `dramatic_move.serp_search(query, *, _call=None, _sleep=None) -> list[dict]`. `_call(query)` defaults to the
  current body (key lookup, the staged `serp` import, `serp_module.serp_brightdata_records(query, max_pages=1, gl="us",
  hl="en")` returning its dict); `_sleep` defaults to `time.sleep`. With `_call` given the key lookup and the import are
  skipped. Policy: a result with `status` `FAILED` and `failure.kind` in (`VENDOR`, `TRANSPORT`) is retried, at most 2
  retries (3 attempts), sleeping 1.0 then 2.0 seconds between attempts; a `CONFIG` or any other kind is raised at once;
  the first OK result is returned in the same `[{title, url, snippet}]` shape as today. The final failure raises
  `RuntimeError` whose message names the class, the attempts and the vendor's own words, in the form
  `SERP FAILED: <kind> after <n> attempts: <brd_error_code> <brd_error>` (`1 attempt` for a CONFIG).
- Out of bounds: `serp.py` (the staged vendor client), `lookup`, `detect`, the cap, `write_rows`, `sweep.py`, any key or
  environment change; no live search.
- Checks: `round29/checks/xb1_retry_check.py` (AC1; base FAIL 6 -- the call has no `_call`) and the existing lookup tests
  (AC2: must stay green). J1 is not set: a retry is read in the next sweep's `failed` count when a candidate exists.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xb1_retry_check.py`. It FAILS at the base (6 failed: the call has no `_call`)
  and is your target; do not edit it. `Plan` returns the next planned raw result of `serp_brightdata_records`.
- `dramatic_move.serp_search` (about line 341) today: key from `BRIGHT_DATA_API_KEY` else `_secret_key()`; puts `_serp_dir()` on
  `sys.path`, imports `serp`, sets `serp_module._bd_key_cache` and `_bd_serp_zone_cache`, calls
  `serp_module.serp_brightdata_records(query, max_pages=1, gl="us", hl="en")`, raises `RuntimeError` on `status == "FAILED"`,
  and returns `[{title, url (the record's `link`), snippet}]`. Keep all of that as the default `_call`; add the retry around it.
- The failure dict is `{"kind", "http_status", "brd_status", "brd_error_code", "brd_error"}`; read `data/find/dualbiz/scripts/serp.py`
  `classify_serp_attempt` for the kinds, do not edit it. A real `time.sleep` must never run in a test: `_sleep` is injected.
- Your queue has a second order after this one (RIV-xd-1, same file): the issuer continues you on it.
## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~35/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search -- inject `search` or the client), any Secrets Manager call, any
environment gate flip outside a test. A row you file goes in the investigation file below with id
`ETFS_RIVALS-D1-W35-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/dramatic_move.py
data/etfs/scripts/rivalfunds/tests/test_riv_xb1_search_retry.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- the check file: retry on a planted VENDOR then success, two retries at most with sleeps 1.0 and 2.0, a persistent
  502 raises with the class, `3 attempts` and the vendor's words, a CONFIG (4xx) is not retried, a first-try success sleeps
  nothing, and `run_for_day` counts a persistent failure once.
- **AC2** -- the existing lookup tests are unchanged and green (the seam with the real neighbour `run_for_day`).
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xb-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xb1_retry_check.py</invocation><expect>6 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xb-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider rivalfunds/tests/test_ws2_wb1_dramatic_move.py rivalfunds/tests/test_riv_wi1_sweep_lookup.py</invocation><expect>all passed, 0 failed</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~35/ETFS_RIVALS.TO-RIV-xb-1.bounded-search-retry.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xb-1.bounded-search-retry`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 29 of ETFS_RIVALS, ONE issuance on `ledger/ROUND_ANALYSIS.round28.md` section 3
(msg 4558). Decomposition revision 1.29. Check file(s) dry-run at the base before the cut. Chain A, first order (slot ~35); RIV-xd-1 follows on the same slot (one file, `dramatic_move.py`: a write-set serialization).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>29</round>
<workstream>4</workstream>
<slot>~35</slot>
<fabric>dell1</fabric>
