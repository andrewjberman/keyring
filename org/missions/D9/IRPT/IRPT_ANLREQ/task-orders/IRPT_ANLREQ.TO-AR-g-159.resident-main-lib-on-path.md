# TO-AR-g-159 -- the resident's entry module puts the package's lib directory on sys.path with the others (r34j's V2 found the door's checker failing in the service: trading_calendar was not importable; CTO msgs 10166 and 10172)

<to_id>IRPT_ANLREQ.TO-AR-g-159</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~281</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>55</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-159` (`decompositions/IRPT_ANLREQ_DECOMP_R55_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none (AR-g-157 is merged on the trunk). Order: CTO msgs 10166 and 10172. The failure: `intake/yfinance_check.py` (since AR-g-157) does `import trading_calendar`; `lib/trading_calendar.py` is a member of the resident package, but `ycharts/generate/resident_main.py:20-23` does not put `lib` on `sys.path`, so in the service every symbol reads CHECK_FAILED.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~281`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-281` (branch `wk-IRPT_ANLREQ-281`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~281 <0.9.0_WK_IRPT_ANLREQ~281@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W281-S<k>` (take the next free `<k>`; check the channel file for `W281` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-159`, inlined)

File: `infra/aws/lambda/investor-reporting/ycharts/generate/resident_main.py`. Lines 18-23 read:

    # Works with either the source layout or P's flattened deployment package.
    _root = Path(__file__).resolve().parents[2]
    for _relative in ("intake", "ops", "reports", "_keys", "_authz", "_gate", "ycharts/session", "ycharts/extract"):
        _path = _root / _relative
        if _path.is_dir():
            sys.path.insert(0, str(_path))

1. Add `"lib"` to that tuple, between `"_gate"` and `"ycharts/session"`: `("intake", "ops", "reports", "_keys", "_authz", "_gate", "lib", "ycharts/session", "ycharts/extract")`. In the flattened deployment package `lib/` holds `trading_calendar.py` (and `opal_naming.py`); in the source layout `lib` under `infra/aws/lambda/investor-reporting/` does not exist, so the existing `is_dir()` test skips it there. Change nothing else in the module (the other entries keep their order and spelling; the comment above the loop gains one clause naming `lib`).
2. Two tests, added to `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_main.py` (offline: no network, no AWS; leave the existing test as it is):
   - **the tuple:** parse `resident_main.py` with `ast` (the module file next to the tests' parent), find the `for _relative in (...)` loop and assert `"lib"` is among its entries and the entries without `"lib"` equal `["intake", "ops", "reports", "_keys", "_authz", "_gate", "ycharts/session", "ycharts/extract"]`, in that order.
   - **the layout run (`python -I`):** build a temporary tree holding copies of `intake/yfinance_check.py` (from `infra/aws/lambda/investor-reporting/intake/yfinance_check.py`), `lib/trading_calendar.py` (from the repository's top-level `lib/trading_calendar.py`) and `ycharts/generate/resident_main.py`. Run, with `subprocess` and the current interpreter, `python -I -c <code> <tree>` where the code sets `sys.path` from the tuple parsed in the previous test (for each entry, if `tree/<entry>` is a directory `sys.path.insert(0, ...)`, exactly as `resident_main` does), imports `yfinance_check`, and prints the state, last close and reason of `YfinanceChecker(history=<fake returning rows 2026-10-14 100.0, 2026-10-15 101.0, 2026-10-16 102.0>, sleep=<noop>, now=<a callable returning 2026-10-17 00:50 UTC, aware>).check(["SPY"])["SPY"]`. Assert it prints `KEPT 101.0 HISTORY_ROWS`. Then run the same code with `lib` removed from the entries and assert it prints `CHECK_FAILED` (the control: this is the defect the service had). The file must contain the strings `lib`, `-I` and `trading_calendar`.
3. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
4. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR159-g-AC1" cell_refs="AR-g-159"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g159_checks.py build</invocation><expect>^AR-G159-OK</expect></criterion>

<criterion id="AR159-g-AC2" cell_refs="AR-g-159"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g159_checks.py guard</invocation><expect>^AR-G159-OK</expect></criterion>

<criterion id="AR159-g-AC3" cell_refs="AR-g-159"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g159_checks.py regress</invocation><expect>^AR-G159-REGRESS-OK</expect></criterion>

<expected_criteria>AR159-g-AC1,AR159-g-AC2,AR159-g-AC3</expected_criteria>

- AC1 reads the tuple from `resident_main.py` itself and runs the shipped checker in a fresh `python -I` interpreter over a package-layout tree with that tuple: it must read KEPT on Thursday's close for a Saturday run; with `lib` removed it must read CHECK_FAILED; and the test file holds the strings. At base it FAILs (the tuple has no `lib`: the run reads CHECK_FAILED, which is the defect).
- AC2 holds what must not move: the other entries of the tuple in order, and `resident_main.py` differing from its base only in the tuple line. At base it PASSes.
- AC3 runs `test_resident_main.py` and `test_package_poll.py` on their own, then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. The factory import, the loop, the worker and every file not listed are not yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_main.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_main.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~281/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-159.resident-main-lib-on-path.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R55_G.md</decomp_doc> round 55, workstream ~G, cell `AR-g-159`.
<owned_cells>AR-g-159</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR159-g-AC1, AR159-g-AC2, AR159-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~281/IRPT_ANLREQ.TO-AR-g-159.resident-main-lib-on-path.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-159`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR159-g-AC1,AR159-g-AC2,AR159-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 4.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one entry-module line and one test file; no deploy, no AWS call, no network. The change reaches production only through the r34k resident release under its own never-widen pair. In the service it adds one directory (`lib`: trading_calendar.py, opal_naming.py) at the head of sys.path ahead of `ycharts/session`; no module in the package has the same name as a member of `lib`.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the issuer's check `ar_g159_checks.py` was dry-run at the base (build FAIL showing the defect itself: the shipped checker over a package-layout tree with resident_main's own path list reads CHECK_FAILED; guard PASS; regress PASS) and against a scratch copy with the reference fix (build OK) and three mutants (lib misspelled, lib absent, another entry dropped); the first two fail build and the third fails guard. Traps: the offline V2 test passed on r34j because the repository held the OLD checker when it ran (it ran before AR-g-157 merged); a test that finds the calendar through the repository's own path or PYTHONPATH (hence python -I and a copied tree); the static reachability walk models lib as on the path, which the service does not. NOT seen (blind): the live service's sys.path (the V2 script of r34k sets its own from the same tuple); denominator: 4 build arms, 2 guard arms.
</preflight>

- Cut on the CTO's rulings (msgs 10166 and 10172) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR159-g-AC1 FAILs, AR159-g-AC2 PASSes, AR159-g-AC3 PASSes (in the worker's worktree).
