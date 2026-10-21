# TO-AR-g-185 -- the Multi-Comp's portfolio line is the filed amounts bought at the common window start, not at the start of the 10-year price window (7J read, Finding 1)

<to_id>IRPT_ANLREQ.TO-AR-g-185</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~358</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL8</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-185` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** the 7J read (Finding 1) and CTO msg 11932. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~358`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-358` (branch `wk-IRPT_ANLREQ-358`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~358 <0.9.0_WK_IRPT_ANLREQ~358@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W358-S<k>` (check the channel file for `W358` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` from `infra/aws/lambda/investor-reporting` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_window_checks.py` (read it; you cannot edit it, and you cannot edit its fixture). It builds its own inputs and computes every expected value itself, independent of your code: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-185`, inlined)

**What this cell is.** The issuer's page-by-page read of run 7J's served Multi-Comp PDF (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/FWD10_READ_RUN7J_20261021.md`) found that the PORTFOLIO row of the comparison section does not reproduce (YTD 10.66 on the page against 8.83 recomputed, 1Y 13.37 against 11.12, max drawdown -15.94 against -13.60) while both Opal model rows match exactly. The cause was measured by exact reproduction: `_price_stage` in `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py` resolves every holding over a 10-year price window (`PRICE_HISTORY_YEARS = 10`) and `portfolio_series.buy_and_hold` applies the filed amounts at the START of that data (2016-10-20); `_compare_stage` then cuts that path to the common comparison window (2024-04-30 to 2026-10-19: the Opal models' first observation to their last) and rebases it to 100. By the window start the filed weights (SPY 44 percent) had drifted (SPY 60 percent), so the page's weight table says 44 and its returns, risk and chart describe a 60 percent SPY portfolio. A Multi-Comp's portfolio line must be the filed amounts bought at the COMMON WINDOW START and held, as the comparables' lines start there too.

**Do exactly this (the Overview and every run without a priced comparable stay as they are).**
1. `infra/aws/lambda/investor-reporting/ycharts/research/portfolio_series.py`: add `buy_and_hold_from(series_by_ticker, amounts, start_ms)` returning the same dict shape as `buy_and_hold` (status, pairs, coverage, used and excluded tickers), with the amounts applied at `start_ms`: each ticker's series is cut to the observations at or after `start_ms`, opened with one observation at `start_ms` that carries its last value at or before `start_ms` (a ticker with no observation at or before `start_ms` is excluded by the same rules `buy_and_hold` already applies to a bad base). `buy_and_hold` itself is unchanged.
2. `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py`: `_price_stage` already builds `series` (per-symbol pairs) and `amounts`; return them as a FOURTH value, a dict `{"series": series, "amounts": amounts}` (update its two call sites, in `produce` and `produce_package`, and nothing else that unpacks it; `kept`, `prices` and `named` are unchanged, so run.json is unchanged). `_compare_stage` takes that dict as a new last parameter: after the comparison `items` are built and BEFORE `portfolio = {...}`, let `start` be the largest first timestamp among the items that carry a series; if `start` exists and the dict is not None, call `portfolio_series.buy_and_hold_from(series, amounts, start)` and, when its status is `OK` with at least two pairs, use its pairs as the portfolio's series; otherwise keep the existing pairs. Nothing else changes (the allocation, the risk-free and benchmark inputs, the gap sentences).
3. Tests, each of which FAILS before your code change (run it first and say so in your report): in `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_portfolio_series.py` add unit tests of `buy_and_hold_from` (a series that begins before `start_ms` is cut and opened at its value there; two tickers that drift apart before `start_ms` start from the filed weights at `start_ms`; a ticker with no observation at or before `start_ms` is excluded and named); in `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_producer.py` add one test that a Multi-Comp whose holdings were priced over a history that starts years before the models' first observation, with strong drift before that date, serves a "Your portfolio" chart line whose last level equals the amounts bought at the window start (compute the expected value in the test with its own arithmetic, not by calling the code under test). Keep every existing test passing.
4. Run the two acceptance invocations; write the proof instance; commit; flip the order to complete only on both PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR185-g-AC1" cell_refs="AR-g-185"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_window_checks.py portfolio</invocation><expect>^AR-WINDOW-portfolio-OK$</expect></criterion>

<criterion id="AR185-g-AC2" cell_refs="AR-g-185"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_window_checks.py tests</invocation><expect>^AR-WINDOW-tests-OK passed=[0-9]+$</expect></criterion>

<expected_criteria>AR185-g-AC1,AR185-g-AC2</expected_criteria>

- AC1: the REAL producer on a Multi-Comp whose holdings were priced over a history that starts 60 months before the models' first observation, with strong drift before it: the served 'Your portfolio' chart line ends at the level the filed amounts bought at the window start give (this file's own arithmetic), starts at 100, and the ETF line is unchanged. At base it FAILs (157.44 against 151.61).
- AC2: the five owned producer test files pass (63 at the base) and at least 65 ran. At base it FAILs (63 ran).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/portfolio_series.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_portfolio_series.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_compare_producer.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~358/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-185.multicomp-portfolio-path-from-the-common-window-start-not-the-price-window-start.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-185`.
<owned_cells>AR-g-185</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR185-g-AC1,AR185-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~358/IRPT_ANLREQ.TO-AR-g-185.multicomp-portfolio-path-from-the-common-window-start-not-the-price-window-start.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-185`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR185-g-AC1,AR185-g-AC2` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two lambda-tree source files and two test files edited in the worker's worktree; nothing is deployed, no AWS call, no network; the change reaches the host only through a later resident release under a never-widen pair. The Overview and runs without a priced comparable are unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: both criteria FAIL at base; the checker was calibrated by the issuer against a reference fix in a scratch worktree (OK) and three mutants (window start ignored, start at the wrong date, amounts ignored), each of which fails. Traps: re-cutting the path instead of re-applying the amounts at the window start, changing run.json by widening `prices` or `kept`, changing the Overview, using the first timestamp of the PORTFOLIO instead of the largest first timestamp of the comparables, editing the checker. NOT seen (blind): the live price tiers (the next filing reads them).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 and AC2 FAIL.
