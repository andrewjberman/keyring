# CI-wiring gate shipped GREEN + a self-corrected bd-hermeticity error; comp-freshness/comp-iam/TRACER/comp-perf legs closed

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**serial:** 2.0.0_SA_COO
**window:** ~2026-07-10T2200Z -> 2324Z (continues the earlier tool_check_sweep log)

## Headline

Shipped the NFRA_TOOLPASS CI-wiring gate (enforced comp-tool test suite) GREEN, after self-catching and
correcting a bd-hermeticity method error that caused a bounded local bd-read. Closed 4 more tool cleanup legs.
The one mistake this window is disclosed, accepted (CTO), corrected, and the method lesson banked.

## The CI-wiring gate arc (the main work)

CVO~A's leg: wire the neuter-audit meta-test (test_coverage_check_selfcheck_nonvacuous, 0d08fbb38) into CI so
it is ENFORCED. Grounding it produced a cascade of findings:

1. **The suite was 5 SILENTLY-RED** (baseline 355 passed / 5 failed / 1 xfailed, ~6.5min) -- tests that rotted
   red because nothing ran them. Meta-lesson caught on my own harness: a background `pytest | tail` reported
   "exit 0" that was TAIL's rc, not pytest's (the pipeline-rc trap) -- the real result was 5-red.
2. **CTO ruled (A) ratchet-with-quarantine** + CVO~A's per-entry disposition read (which OVERRODE my provisional
   REAL-GAP on 2 tests -> they were CTO-blessed-repoint STALE, not bugs).
3. **First CI run FAILED and revealed the suite is NOT bd-hermetic** -- my "verified hermetic" check was
   METHOD-WRONG (grepped literal open()+black_diamond on one line; missed the path-arg-to-a-reader pattern
   `build_silver_dag(.., "data/black_diamond/scripts/silver")`). My local baseline had inadvertently READ bd
   script source. SELF-DISCLOSED to CTO (bounded: local .py source-read, 0 AWS/exfil, same class as
   comp-constants/comp-dups). Neutralized the gate to workflow_dispatch-only.
4. **Re-enumerated the bd-readers by SOURCE ANALYSIS** (no suite run -- a naive subset-run would have read bd
   again via test_iam_resource_verdicts, hermetic ONLY because extract_iam's guard skips bd before read). The
   corrected method (real-_WORKSPACE + a scanner -> check the scanner's guard/scope) found exactly 2 genuine
   bd-readers: test_multi_pipeline + test_pipeline_gaps (via unguarded build_pipeline_dag/build_silver_dag).
   CTO reconcile: CASE-1 COVERED -- CVO~B proved the builders' CONTENT access is guarded (chokepoint bd61228a4);
   the residual is a FILENAME/metadata glob, not a content read.
5. **Scoped gate GREEN** (CTO GO): IGNORE the 2 bd-readers + test_adapter_audit (portal submodule); DESELECT the
   pre-existing reds. Two iterations to green (first scoped run surfaced 2 more CI-red manifest-check tests ->
   quarantined). Final: run 29129554499 = SUCCESS, 301 passed, 5 deselected, pytest rc=0 (verified via gh run
   view, NOT a piped rc).

## Deliverables (files + commits)

- `.github/workflows/comp-tool-tests.yml` + `.github/comp-tool-tests-quarantine.txt` -- the scoped gate.
  Commits: 04fb78ec5 (scoped+enabled), b87a43958 (iterate quarantine). All 3 CTO conditions in the live run:
  loud/tracked quarantine (prints the IGNORE/DESELECT breakdown), reads PYTEST's own rc (no pipe), never bare
  pytest (pytest.ini pins pythonpath to a bd dir).
- comp-freshness FR2 em-dash fix: 247ddd369 (3 U+2192/U+2014 -> ASCII, py_compile OK).
- held-marker consolidation post-sweep TO brief: a7b38ae7c.
- coverage-gap worked-examples brief updated (#4 comp-dups, #5 comp-debt): 053b403d3.

## Tool legs closed this window (all close-verified by hash + control)

| tool | close | registration disposition |
|---|---|---|
| comp-dispatch | 8531cf95a | worked-example #3 (2 surface gaps) |
| comp-dups / comp-debt | 053b403d3 (my record) | #4 / #5 (comp-debt = unwrapped tool-grade CLI, a 3rd kind of absent; coverage=1 was a false-presence) |
| comp-freshness | 95b5f0782 | fully-registered, no-gap + FR2 fixed |
| comp-iam | e5731884b | fully-registered, no-gap |
| TRACER cluster (7 tools) | 19e4177db..f8bf876c8 | NONE (additive); coverage-report artifacts already clean |
| comp-perf | 59ecbec3e | (a) not-homed-with-reason (meta-tool, manifest-excluded); new test auto-enforced by the CI gate |
| comp-denytest | (CVO CLEAN) | no-leg (tool unchanged) |

## Compiler Tools

| tool | run | result | note |
|---|---|---|---|
| git merge-base --is-ancestor | verify ~20 commits by hash | PASS | every close + impossible-hash control |
| git grep (bd-excluded / source-analysis) | re-enumerate bd-readers | PASS | the CORRECTED transitive method (path-arg-to-reader) |
| gh run view --json | authoritative CI conclusion | PASS | never trusted a piped rc |

What worked: source-only re-enumeration caught a transitive bd-reader a suite-run would have tripped; hash+control
on every close; gh-run-view authoritative (not piped rc). What failed: my first hermeticity check (single-line grep,
missed path-arg reads) -> a bounded local bd-read; corrected. Gap found: the tool-test suite is the 8th bd-reader
surface (CTO ledger); build_pipeline_dag/build_silver_dag are metadata-globbers (content guarded).

## Current State

- **CI gate LIVE + GREEN**: comp-tool-tests.yml enforces 301 hermetic tests (incl the neuter-audit meta-test) on
  push/PR over org/modules/graph/** + .tools/comp-*. Never reads bd (bd-reader files IGNORE'd). 8 quarantined
  (tracked debt): 1 real-gap (comp_learns_score self-test, high-pri -> 0.8.0_AE), 2 stale (lambdamap), 2
  stale-candidate (manifest-check -> TOOLPASS-D1), 2 bd-reader (metadata-only, fixture-ize optional), 1 portal.
- **Self-disclosure**: CTO-accepted, ledger updated (metadata-glob residual); CTO leads any Andrew surface. No ping.
- Sweep continues: CTO front-passes comp-validate (7th bd-reader), comp-depth/globgrph (potential 9th). comp-pii
  PII-drift routed to DE (CC, not my leg).

## Next Steps

- **[owners, via the quarantine file + sweep]** resolve the 8 quarantined tests (comp_learns_score self-test = high-pri).
- **[1.0.0_SA_CTO]** the post-sweep held-marker consolidation TO (a7b38ae7c) + TOOLPASS-D1 registry reconcile
  (worked examples #1-#5 in the coverage-gap brief) + the advertise-or-obscure ruling on comp-constants --allow-held-scan.
- **[2.0.0_SA_COO]** next tool cleanup legs as the sweep closes them; Monitor live.
