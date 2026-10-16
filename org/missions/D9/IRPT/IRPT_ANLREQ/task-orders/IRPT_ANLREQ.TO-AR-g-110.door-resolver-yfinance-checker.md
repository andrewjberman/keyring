# TO-AR-g-110 -- the upload door's resolver is built with the yfinance checker, so a symbol YCharts omits and yfinance knows is KEPT (C-SWAP step 2)

<to_id>IRPT_ANLREQ.TO-AR-g-110</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~250</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-110` (`decompositions/IRPT_ANLREQ_DECOMP_R28_G.md`) |
**outcome_ref:** FWD-1 run 3 (C-SWAP step 2, C-FILING-HINT) | **depends_on:** `AR-y-292` (`intake/yfinance_check.py`, merged), `AR-y-293` (the KEPT state in `SecurityResolver`, merged). Order: CTO msg 8968 (ruling on Y2 msg 8965).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~250`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-250` (branch `wk-IRPT_ANLREQ-250`), provisioned by the issuer with `infra/`, `docs/`, `data/`, `lib/`, `org/standards` and the project folder on disk. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~250 <0.9.0_WK_IRPT_ANLREQ~250@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. (A provisioner error about a portal sub-worktree does not concern you.)
- A row id has the form `IRPT_ANLREQ-D2-W250-S<k>` (take the next free `<k>`; check the channel file for `W250` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network (the yfinance library is never imported or called by your tests), no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`). The checker is run WITHOUT `-I`.

### Read first (under `C:/dev/wk-irpt-anlreq-250/infra/aws/lambda/investor-reporting/`)

- `ycharts/session/resident_session.py` (`template_resolver`, the only place the door builds a `SecurityResolver`) and `ycharts/session/tests/test_resident_session.py` (`test_resident_factory_uses_canonical_secret_and_durable_lookup_boundary` is the fixture pattern: `Dynamo`, `Secrets`, `ResidentSession(...)`, and `monkeypatch.setattr(deadline_transport, '_run_child', offline_child)` to answer the provider lookup).
- `intake/security_resolution.py` (`SecurityResolver.__init__(..., checker=None)` and `_check_unknown`: what a KEPT / NOT_KEPT / CHECK_FAILED verdict does to a symbol's result) and `intake/yfinance_check.py` (`YfinanceChecker(history=None, sleep=..., cap=10, pace_seconds=1.0)`, `check(symbols)`, `CheckerUnavailable`, `default_history`).

### THE CELL (`AR-g-110`, inlined)

`SecurityResolver` already sends every symbol the provider answers NOT_FOUND to a `checker`, but the resident builds it with none (`checker=None`), so a real symbol that YCharts omits and yfinance knows is filed TICKER_NOT_FOUND with Replace and No offered, on every upload. This cell wires the real checker.

**`ycharts/session/resident_session.py`, exactly this, and nothing else in the file:**
1. `ResidentSession.template_resolver` gains the keyword `checker=None` (after `cache=None`). Its docstring (add one) says: the upload door's resolver; C-SWAP step 2: a symbol the provider omits goes to the yfinance checker, so one yfinance knows is KEPT; `checker` is an offline control (an object with `check(symbols)`), and `None` builds the real `YfinanceChecker()`.
2. Inside it, import `YfinanceChecker` from `yfinance_check` (a function-level import, next to the existing two) and pass `checker=checker if checker is not None else YfinanceChecker()` to `SecurityResolver(...)`. The other arguments stay exactly as they are.
3. No other file changes: not `intake/yfinance_check.py`, not `security_resolution.py`, not `resident_worker.py` (it calls `template_resolver(identity=..., source_revision=...)`, which keeps working).

**Tests.** A NEW file `ycharts/session/tests/test_resident_session_checker.py`, offline, with these exact test function names (the checker looks for each by name), built on the fixture pattern above (the provider lookup is stubbed; the history port is a fake set with `monkeypatch.setattr(yfinance_check, "default_history", fake)` and `monkeypatch.setattr(yfinance_check.time, "sleep", lambda s: None)`; yfinance itself is never imported):
`test_the_door_resolver_keeps_a_yfinance_known_symbol` (two symbols in one call: one the stubbed provider finds, one it omits that the fake history gives two rows; assert the found one is `FOUND`, the other is `KEPT` with `resolution_action` `NONE` and `price_source` `yfinance`, and the fake history was asked only for the omitted symbol), `test_a_missing_library_is_a_failed_check` (the fake history raises `yfinance_check.CheckerUnavailable`; the symbol reads `UNAVAILABLE` with `reason` `YFINANCE_CHECK_FAILED`, never a clean absence).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR110-g-AC1" cell_refs="AR-g-110"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g109_checks.py g110</invocation><expect>^AR-G110-OK</expect></criterion>

<criterion id="AR110-g-AC2" cell_refs="AR-g-110"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g109_checks.py regress110</invocation><expect>^AR-G110-REGRESS-OK</expect></criterion>

<expected_criteria>AR110-g-AC1,AR110-g-AC2</expected_criteria>

- AC1 runs the issuer's 5 tests against your tree (a yfinance-known symbol the provider omits is KEPT and the found symbol never reaches the checker; a symbol neither knows stays NOT_FOUND; a missing library and a 429 pushback read as failed checks, never absence; an injected checker wins over the default), then checks your two named tests exist and pass. At base it FAILs.
- AC2 runs four existing test files one at a time (71 tests: the session, the checker, the KEPT holding, the resolve upload) and needs all of them to pass, and needs your branch (against the merge-base with `box/dell2`) to change only your two files, your folder, your order and the channel file. At base it PASSes. Run it under `timeout` 590000 ms.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/session/resident_session.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/test_resident_session_checker.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~250/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-110.door-resolver-yfinance-checker.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R28_G.md</decomp_doc> round 28, workstream ~G, cell `AR-g-110`.
<owned_cells>AR-g-110</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR110-g-AC1, AR110-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~250/IRPT_ANLREQ.TO-AR-g-110.door-resolver-yfinance-checker.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-110`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR110-g-AC1,AR110-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed in `resident_session.py` with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `ycharts/session/resident_session.py` is a member of the resident package (r32 and the r34 draft carry the PRE-wiring bytes; the next resident release carries this) and is staged into no Lambda (it is in neither source-map function's files). Behaviour change at the door: a symbol the provider omits (NOT_FOUND, registry-unresolved) now goes to `YfinanceChecker.check` in ONE batch, at most `cap` (10) symbols per upload, paced 1 second apart, each a `yf.Ticker(symbol).history(period="1mo")` call (a Yahoo read, not Bloomberg: no per-use word, CLAUDE.md Agent Autonomy). A KEPT symbol is no longer offered Replace or No. A raised checker, a missing library or a Yahoo pushback reads UNAVAILABLE `YFINANCE_CHECK_FAILED`, never absence. The only constructor of `SecurityResolver` outside tests is this one call (measured: the repository holds exactly one non-test `SecurityResolver(` and one non-test `template_resolver(` caller, `resident_worker.py:676`); no Lambda path builds a resolver.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; the checker reads Yahoo only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's reference build in a scratch tree (5 issuer tests pass; at base 4 of 5 fail) and the CTO's ruling (msg 8968). Traps: the checker built per call but never passed (the default stays None); the found symbols sent to the checker (the history asked for AAPL); a missing library read as a clean "not a symbol"; the injected checker ignored, so a test would call the real library; `intake/yfinance_check.py` not shipped in the resident package (the release tooling adds it; this cell cannot); a second constructor of the resolver left unwired.
</preflight>

- Cut on CTO msg 8968 (ruling on `2.0.0_SA_COO~Y2` msg 8965, row `IRPT_ANLREQ-D2-W165-S2`). Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR110-g-AC1` FAILs and `AR110-g-AC2` PASSes (71), as expected.
- NOT claimed: that the resident host has `yfinance` installed (a missing library reads as a failed check, never a wrong answer; the r34 apply's V2 reads one ticker through the host's interpreter); that Yahoo answers from this host; that the package carries `intake/yfinance_check.py` (the release tooling adds it).
