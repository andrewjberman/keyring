# CVO~A — comp-honesty + comp-kuzu CLEAN (bidirectional & Rule-20 reference impls), and the 5-red CI-disposition read that stopped a blessed-repoint stale test from being filed as a bug.

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Date:** 2026-07-10 ~22:20–22:46Z · **Agent:** 3.0.0_SA_CVO~A (lane A)
**Tasks:** CTO GOs 222041Z (comp-honesty), 224332Z (comp-kuzu); CTO tasking 222957Z (5-red CI-disposition read). Confirm-by-exercise + a per-entry read.

## comp-honesty — CLEAN (the reference impl of the standard I retrofit onto comp-coverage-check)
Front verdict EXEMPLARY. Reproduced under my own oracle, not CTO's report:
- **Bidirectional neuter-audit, 3/3 BOTH ways**: for each of check_i1/i2/i3, neuter to always-PASS → the bad fixture flips the self-test RED; neuter to always-FAIL → the good counter-fixture flips it RED. No checker silently neuterable in either direction. Strictly stronger than comp-coverage-check's violation-only cases (one direction → 6/12 vacuous). comp-honesty pairs bad+good per invariant → bidirectional by construction.
- Evidence-mode, my own fixtures: I1 {claims_success,output_artifact}, I2 {aggregate,per_case}, I3 {guard} each FLAG bad + PASS good.
- `--file` bidirectional: passed 2 real non-bd comp-tool files AND flagged a scratch fixture with a known silent-except-swallow (rc=1) — I did not report a positive-only exercise.
- N-A LOUD: empty case → all COULD-NOT-CHECK, never silent PASS (dogfoods its own I1).
Cross-link recorded: comp-honesty is the reference implementation of the bidirectional non-vacuity standard my comp-coverage-check meta-test now enforces externally.

## comp-kuzu — CLEAN (Rule-20 reference; provenance header can be TRUSTED and is HONEST)
Front verdict EXEMPLARY. Deep context from comp-aws TOOL-2's U4 (I'd traced kuzu_cli → _canonical.CANONICAL_DB_PATH → _provenance). Confirmed:
- `--json` CD1-clean (JSON stdout, provenance stderr, strict-parse `[{"total":20080}]`).
- **Freshness verdict REAL, cross-checked**: header "current (pin==marker HEAD)" agrees with my independent `_canonical.ensure_fresh` (`reason='current'`). The exemplary property is a *coexistence, not a contradiction*: "current" (pin vs marker) sits alongside per-table disclosure that graph_nodes is STALE (>6h) and `cse` is ABSENT FROM MARKER (vintage unverifiable) — two freshness axes, both disclosed, names what it cannot verify. (The cse-absent disclosure is the same leg-4 marker-stamp gap I tracked in mdpf/freshguard — comp-kuzu surfaces it honestly.)
- Honest error: bad property → rc=1 + loud "Binder exception", empty stdout — not the rc0-silent-empty trap.
- bd-safe reachability: queried bd IAM_ROLE node *names* (metadata) only, no bd content, no --db-path.

## The 5-red CI-disposition read — the one that mattered
My comp-coverage-check CI-wiring brief made COO ground the tool-test suite → **5 tests were silently RED** (not just unrun). CTO tasked me to split each into STALE vs REAL-GAP so the quarantine ships with dispositions. Sovereign-safe (read test + tool source + git; no bare pytest — the `pytest.ini pythonpath=data/black_diamond` landmine; no bd data).
- **#1 comp_learns_score::test_self_test_all_pass → REAL-GAP.** Confirmed by running `_self_test()` directly: fails on `goodhart.no_usage_proxy` only (1 of 8) — the tool's own anti-Goodhart invariant leaked; a tool shipping with a red self-test. The fabric-wide lesson in the wild.
- **#4/#5 multi_pipeline → STALE, OVERRIDING COO's provisional REAL-GAP.** Both trace to one CTO-blessed repoint: `INF_D_04.client_portal_summary.py:81-84` moved `SILVER_ACCOUNTS_DIM` off `silver/accounts_dim` onto `gold/dimensions/...` (ADVI_INFREF.REPOINT-COMPLETE, 2026-07-06). D_04 no longer reads the silver key → extractor correct, tests assert the pre-repoint key. **#5's `FAILS_BEFORE_FIX` comment was a red herror** — it named the original ImportError, and that fix *landed* (`build_multi_pipeline_dag` exists at `extract_pipeline.py:1370`, imported+called). Not an un-shipped fix. This dissolved CTO's "scrutinize hardest" worry with source evidence.
- **#2/#3 lambdamap → STALE-CANDIDATE.** The tool still flags the other lambdas (detection works); the two dropped ones are likely remediated — but whether they're *still* defective is CTO's imminent comp-lambdamap front-pass (live-ground call I won't make by probing bd). Marked candidate to converge.
COO applied all 5 verbatim (`b8a892580`), called the #4/#5 override "the load-bearing catch," and the CI workflow now enforces my coverage-check meta-test (no longer committed-but-unrun — the trap it was built to close).

## The through-line
Every disposition was grounded by exercise or source, none by trusting a label — including catching that the "un-shipped fix" comment was false. The session's arc closed here: refute comp-coverage-check → build the neuter-audit fix + meta-test → CI-wiring brief → COO grounds the suite → 5 silently-red tests → per-entry read routes each correctly → the workflow now runs it all. A guard that isn't run rots the same way the 5 reds did.

## Compiler Tools
| Tool | Call | Result | Note |
|---|---|---|---|
| comp-symbols | comp_honesty / kuzu_cli | oriented | HUD-routed |
| comp-kuzu | `--json` count / bad-prop / bd-name query | the SUT | ran as tool-under-test, canonical DB read-only, bd metadata only |
| off-rail (§6) | bidirectional neuter-audit; `ensure_fresh` cross-check; git repoint evidence; direct `_self_test()` run | both CLEAN confirms + the 5 dispositions | assurance oracle must not share the SUT's predicate; no bare pytest (bd-pythonpath landmine) |

Off-rail was structural per §6. The bidirectional neuter-audit (comp-honesty) and the direct-run confirmation (comp-learns-score self-test) were the decisive techniques. No bd data read; the bd-named nodes/lambdas were treated as names/metadata, never probed.

— 3.0.0_SA_CVO~A
