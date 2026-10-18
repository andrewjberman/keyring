# NFRA_OPLGTW task order -- `OG-pr-5` -- the probe listener's server must not touch the process-wide `uvicorn` loggers (round 43 repair; row `Z-S395`, the CTO's ruling msg 35769)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pr-5</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pr-5</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~156</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling on the applier's row `Z-S395` (msg 35769).
EGRESS CLASS, declared: NONE (the listener binds the loopback interface only).
</preflight>

## 1. THE CELL -- `OG-pr-5` (decomposition addendum R3-T.120 amendment A1, round 43, workstream ENRICH-R43-B)

THE DEFECT. `infra/aws/ec2/opal-gateway/app/probe_listener.py` builds its server with `uvicorn.Config(probe_app, host=PROBE_HOST, port=port, log_level="warning", access_log=False, lifespan="off", ...)` in `make_server` (about line 359). A `uvicorn.Config` constructor calls `configure_logging()`, which is PROCESS-WIDE: it applies `LOGGING_CONFIG` (`logging.config.dictConfig`), sets the levels of the `uvicorn.error`, `uvicorn.access` and `uvicorn.asgi` loggers to the config's `log_level` (here `warning`), and, for `access_log=False`, sets `logging.getLogger("uvicorn.access").handlers = []` and `.propagate = False`. The listener's Config is the first one built after the gateway service's own, so since the `OG-ap-40` deploy the service's OWN access log (`POST /mcp ...` lines in the journal, 157 to 171 per 30 minutes before) is silent (0 per window after) while the audit lake shows traffic continuing. The applier measured it; the CTO signed past it and rules this repair.

THE REPAIR (you write only `app/probe_listener.py` and the new `tests/test_og_pr5.py`; `server.py`, `audit.py` and every other file are read-only for you):
1. In `make_server`, BEFORE constructing the `uvicorn.Config`, snapshot the state of the four process-wide loggers `uvicorn`, `uvicorn.error`, `uvicorn.access` and `uvicorn.asgi`: for each, `level`, a COPY of `handlers` (the list, shallow-copied), `propagate`, `disabled`, and the list of `filters`. Build the Config inside a `try`, and in a `finally` RESTORE every one of those attributes to the snapshot (assign `logger.handlers[:]` from the copy, so the logger object is the same object). The restore runs also when the Config constructor raises. Keep the listener's own settings (`access_log=False`, `log_level="warning"`, `lifespan="off"`, no server or date header): the listener itself still writes no access line; it is audited by its own labelled records.
2. Add a short comment naming the cause (uvicorn's `Config` configures process-wide loggers) and this order. No other behaviour changes. If `start`, `_run_guarded` or any other function builds a second `uvicorn.Config` or `uvicorn.Server`, route it through the same snapshot and restore (read the file in full first; there is one `uvicorn.Config` call today).

NEW TESTS in `tests/test_og_pr5.py` (a new file; import the module as `tests/test_og_pr1.py` does, `from app import probe_listener as pl`; no socket may be opened: build the server object with `pl.make_server(port=0)` and do NOT call `serve()`):
- `test_ogpr5_ac01` THE SERVICE'S ACCESS LOGGER SURVIVES THE LISTENER: first build a stand-in for the service's own Config (`uvicorn.Config(lambda scope, receive, send: None, log_level="info")`, which applies the same default logging as the service), attach a capturing `logging.Handler` to `logging.getLogger("uvicorn.access")`, record the state of the four loggers (level, handlers as a list of objects, propagate, disabled, filters), then call `pl.make_server(port=0)`; assert the state of all four loggers is IDENTICAL to the snapshot (same level, the same handler objects in the same order including your capturing handler, same propagate, disabled and filters), and that an INFO record emitted on `uvicorn.access` after the call reaches your capturing handler.
- `test_ogpr5_ac02` THE RESTORE RUNS ON ERROR: monkeypatch `uvicorn.Config` in the module under test to a function that first mutates the four loggers (set the `uvicorn.access` level to WARNING, empty its handlers, set `propagate` False) and then raises; assert `pl.make_server(port=0)` raises and the loggers read their pre-call state afterwards.
- `test_ogpr5_ac03` THE LISTENER ITSELF STAYS QUIET: the object `pl.make_server(port=0)` returns has `config.access_log is False` and `config.log_level` equal to the WARNING level, so it writes no access line of its own.
Restore the logger state at the end of each test (a fixture that snapshots and restores, so the tests do not leak into the other files).

Mutant control to run and report (restore the file byte-equal afterwards): deleting the `finally` restore makes `ac01` and `ac02` fail.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no SSM write, no env key, no Terraform, no change to `server.py`, `audit.py`, `tools.py` or any other app file; do not edit `tests/test_og_pr1.py` (it must pass unchanged).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret, an account number or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/probe_listener.py
infra/aws/ec2/opal-gateway/tests/test_og_pr5.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/probe_listener.py` and `tests/test_og_pr5.py`; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~156/`. Rows: id `NFRA_OPLGTW-Z-W156-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pr-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_pr5.py test_ogpr5_ac01 test_ogpr5_ac02 test_ogpr5_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pr-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~156 '^infra/aws/ec2/opal-gateway/(app/probe_listener\.py|tests/test_og_pr5\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~156: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-pr-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh pr5set tests/test_og_pr5.py tests/test_og_pr1.py tests/test_og_en21.py tests/test_og_cl2.py tests/test_og_en9.py; echo "exit=$?"</invocation><expect>(?s)pr5set forward: passed (\d+); failed 0.*pr5set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three new tests pass. `AC2`: your commits touch only the module and the new test file. `AC3`: the new tests, the thirteen existing `test_og_pr1.py` tests (unchanged) and three more gateway test files pass together in both orders with the same count. Run `AC1` and `AC3` THREE times each and report the three results.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pr-5.round-43-listener-leaves-the-service-access-log-alone.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines and the three-run results, the mutant control). Commits can take several minutes: give `safe-commit` a generous bound.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-B (a second issuance in round 43: the gate allows one issuance per workstream; decomposition addendum R3-T.120 amendment A1). The CTO's ruling (msg 35769): "the listener must not touch `uvicorn.access`; give its server its own logger or leave access logging on for it"; the issuer reads the first alternative as stronger: leave ALL process-wide uvicorn loggers exactly as they were, which also covers the `uvicorn.error` and `uvicorn.asgi` levels that the same `Config` call sets to `warning` and the dictConfig the constructor re-applies.
- The CTO's criterion (journal lines under traffic, counted against the audit lake, listener lines distinguishable) is the release order's (`OG-ap-44`, `ap44.AC2`); this order proves the mechanism offline. The listener still writes no access line, so there are no listener lines to confuse with the service's.
- Mechanism cited from uvicorn's `Config.configure_logging` (read it in the installed package to confirm the four attributes before editing; if the installed version differs from this description, say so in a row and cover what you read).
- Chain: `OG-pr-5` then `OG-ap-44` (the tenth release), ahead of `OG-ev-7`. Slot `~156`.
- Pre-cut: `AC1` base FAIL as expected (the test file is absent).

<status>complete</status>
<round>43</round>
<workstream>ENRICH-R43-B</workstream>
<slot>~156</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
