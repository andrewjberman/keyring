# NFRA_GRAPHUNI cause-1 build + thread resolution — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch NFRA_GRAPHUNI HARNESS-AUDIT, second half (cause-1 build, "AFTER the audit
lands")
**Status:** COMPLETE

---

## Objective

Build the additive lambda-bridge extraction pass per this lane's own wiring spec (`GRAPHUNI_CHAIN_TRACE.md`),
code + tests only, nothing wired into live ingestion — the forward motion available regardless of the
harness-audit outcome.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `python3 -m py_compile` | `extract_gold_compute.py` | PASS | |
| `python3 extract_gold_compute.py --lambda-bridge-self-test` | first run | **FAIL** (caught a real bug) | positive control `lambda:bd-price-update` absent -- the code assumed a GOLD_SCRIPT<->LAMBDA shape; the real fixture edges are LAMBDA<->S3 directly, no gold endpoint at all |
| same, after fix | PASS | 610 edges, both positive controls + mutant clean |
| `python3 extract_gold_compute.py --stats` (default path, no new flags) | regression check | PASS | byte-identical behavior to pre-change (1366 nodes / 3467 edges Phase-A, unresolved=0) |

**What worked:** anchoring the self-test's positive controls to findings THIS SESSION had already
independently verified (the 2 deterministic lambda members from CVO~Z's cross-tab) rather than inventing
new fixtures — meant the test was grounded before it was even run once.

**What failed:** the first implementation of `build_lambda_bridge()` had a real design gap (assumed the
wrong edge shape) — caught by the self-test itself, before any review, exactly the discipline this whole
program is built on.

**Gap found:** none remaining; the one found was fixed in this same pass.

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

### 1. Cause-1 build

Added `build_lambda_bridge()`, `_lambda_bridge_self_test()`, and three new CLI flags to
`infra/aws/globgrph/extract_gold_compute.py` (this lane's own ownpath) — fully additive, the existing
`build()`/default `main()` path untouched and regression-checked. First self-test run failed on one of two
positive controls; root-caused directly (the real fixture edges for `lambda:bd-price-update` are
`LAMBDA`↔`S3` with zero `GOLD_SCRIPT` endpoint, not the `GOLD_SCRIPT`↔`LAMBDA` shape the first draft
assumed) and fixed. Re-run: clean, 610 edges (`READS_S3` 197, `WRITES_S3` 160, `FETCHES` 96, `TRIGGERS`
157).

### 2. Thread resolution — the harness-audit dispute closed

CVO~Z resolved the 16-vs-18-writer disagreement from the prior HARNESS-AUDIT deliverable: their count came
from `NFRA_GRAPHUNI.P1-D.gold_compute_producer.json` — the **month-old committed artifact CVO~Z had
themselves flagged as stale earlier in this same thread** — not the fresh `--full` artifact my harness
actually reads. Re-verified against the correct file: matches my audit exactly (16 writers, zero
`WRITES_S3` from the disputed id). CVO~Z retracted the 18-writer count, the firm-qualification-split
mechanism claim, and the "harness demonstrably misreports" characterization. **Ruling fired per the
pre-commitment: audit clean → 19 is real → the producer is ruled NON-VIABLE as a fixture-equivalent
source. Chain terminates; wire-in is closed, not deferred.** Cause 1 (this build) is unaffected and
proceeds as scoped, independent of that ruling.

Delivered `GRAPHUNI_CAUSE1_BUILD.md` to the census dir.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Keep the lambda-bridge slice fully additive (separate function, separate CLI flag, separate output file) | Matches the wiring spec's own "distinct marker, additive join" design and the dispatch's explicit boundary — nothing should change for any existing consumer of `build()`'s default output. |
| Fix the self-test's caught bug immediately rather than report it as a known gap | The fix was small, direct, and fully grounded in the fixture's own real edges — no reason to ship a known-broken positive control when the correct fix was available in the same pass. |
| Fold the thread-resolution news into this same log/deliverable rather than a separate one | It directly frames what "cause 1 proceeds, cause 2 is closed" means for this build; separating them would lose that context. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/globgrph/extract_gold_compute.py` | Additive: `build_lambda_bridge()`, `_lambda_bridge_self_test()`, 3 new CLI flags | Yes — this lane's own ownpath |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_CAUSE1_BUILD.md` | New — build memo | No — CTO~Z's BASE_EXEC lane |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_graphuni_cause1_build_and_thread_close.md` | This log | Yes — own lane |

---

## Blockers

None. Ingestion stays hard-gated for the cause-2/wire-in path (now permanently, per the non-viability
ruling) — cause 1's own eventual ingestion join remains a separately-gated future step, not built here.

---

## Current State

Cause-1 build complete and self-test-verified. The GRAPHUNI thread's central question (wire-in the
gold-compute producer as a comp-blast/trace/xref re-point source) is now RULED CLOSED — the producer is
non-viable as a fixture-equivalent source, chain terminated. This build is the one piece of forward motion
that survives that ruling, since it never depended on cause 2. Reported to CTO~Z + CVO~Z this turn.

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit `GRAPHUNI_CAUSE1_BUILD.md`; decide whether/when the (still separately-gated)
   lambda-bridge ingestion join becomes its own scoped TO.
2. **[3.0.0_SA_CVO~Z]** Verify the self-test + regression check if useful; the thread's own ruling is
   already recorded in their own message, not re-litigated here.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by. No further GRAPHUNI passes expected on the closed
   cause-2 path.
