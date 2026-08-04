# F9 build window: the comp-pipescript suite commit-gate (dial F9) -- 0.8.0_AE_CloudComp~D

**archetype:** IMPLEMENT

Window: 2026-08-04 ~1320Z -> ~1500Z. TO: `ADHOC.comp-pipescript-suite-commit-gate-f9`
(COO GO 20260804T132102Z, both TOs flipped pending @dbf3d7a7d; sequence F9 -> F1 per the GO
so F1's engine edit becomes this gate's first REAL fire).

NOTE: this log file is itself the F9 Phase-2 UNRELATED-COMMIT exercise vehicle -- the commit
that lands it stages only this .md and must produce ZERO suite invocations (probe instrumented
in the working-tree gate at commit time; result recorded in the follow-up deliverables commit).

---

## What landed this window (working tree; deliverables commit follows)

1. `.tools/git-hooks/pipescript-suite-check.sh` -- pre-commit stage 7. Scoped-stage: pure-bash
   staged-path predicate first; non-matching commits exit silently with zero python spawn.
   On match: runs the suite, PERMIT on green (audited, denominator printed), DENY loud on red
   (failing tests + trigger paths + full-output path). Audited bypass
   `PIPESCRIPT_SUITE_SKIP="<reason>"`, never silent. Fail-closed: python missing or zero suite
   files resolving = DENY.
2. `.tools/git-hooks/install-pipescript-suite.sh` -- idempotent installer appending stage 7 to
   the composed pre-commit hook (rcg-sweep install pattern; EXTENDS, never replaces; verified
   twice-run = no-op second time).
3. Audit log at `org/pipescript-suite-gate-audit.log` (runtime artifact; NOT tracked by me --
   owned-paths exercised: my lane returns False on that path; tracked-or-not routed to CTO as
   a GOVERNANCE_AUDIT-lane call, rcg-sweep-audit precedent).

## Suite membership -- source-confirmed, and the TO's candidate 4th was WRONG (as the TO anticipated)

The dial's "4 files / 41 tests" (P6 @a35ac7af8) is:
`test_multi_pipeline.py` (21) + `test_pipeline_gaps.py` (16) + `test_pipescript_deployed_bd_hold.py` (2)
+ `test_pipescript_io_discrimination.py` (2) = 41. Settled by arithmetic + imports (both extra
files exercise `extract_pipeline`); the TO's candidate `test_sovereign_held_no_drift.py` (5)
was NOT in the dial suite. It is ADDED to the gate suite on its own merits (comp-pydeps: INVOKEs
pipeline_cli; it is the engine's predicate-import no-drift guard). **Gate suite = 5 files / 46
tests, baseline 46/46 green observed pre-build (rc=0, pipe-free).**

Watch list (single derivation point inside the gate script, commented with TO + dial):
engine = `pipeline_cli.py` + its direct engine imports `extract_pipeline.py` + `sovereign_held.py`
+ INVOKE consumer `.tools/safe_deploy_core.py` + shim `.tools/comp-pipescript`; suite files via
globs so F1 fixtures auto-enroll (`test_pipescript_*.py`). Deliberately NOT watched: the
no-drift census's wider tool set (trace_graph, comp-secrets, ...) -- their lanes carry their own
tests; taxing every tool commit breaks the zero-cost-to-unrelated property the TO names
load-bearing. Stated here so the bounded denominator is a DECLARED exclusion, not a blind spot.

## Phase-2 exercises

- **MUTANT (PASS, captured):** ruff-clean semantic mutant in `_build_dag` -- inf-gold ask
  silently returns the bd DAG (the exact D2X wrong-tree false-clean class). First attempt was
  instructive: commit-gate's ruff intercepted a cruder mutant (unused-import) BEFORE stage 7 --
  the chain's earlier gates screen some mutant classes, so the exercise must use a
  lint-invisible one. Second attempt reached stage 7: gate FIRED, suite invoked (probe line
  observed), REFUSED rc=1 naming
  `test_pipescript_io_discrimination.py::test_target_io_surfaces_all_discriminating_terms`
  + trigger path `org/modules/graph/pipeline_cli.py`. Audit line DENIED written. Mutant
  reverted (`git restore --staged --worktree`), file verified byte-clean vs HEAD.
- **UNRELATED-COMMIT (this commit):** result recorded in the deliverables commit message +
  final report: expectation = no probe line, no gate banner, no new audit line, commit passes.

## Smoke exercises (env seam, pre-commit-context)

- Negative: `PIPESCRIPT_SUITE_STAGED_FILES="docs/references/foo.md"` -> silent rc=0, zero output.
- Positive: `...="org/modules/graph/pipeline_cli.py"` -> suite ran, 46 passed, PERMITTED audit
  line (author resolves to the repo default identity outside a real commit -- expected; real
  commits carry the commit author).
- Defect found+fixed in the same window: pytest ANSI color codes leaked into the audit log;
  now `--color=no` + escape-strip on the summary line.

## Compiler Tools (window running record; full table in the F9 report)

| Tool | Invocation | Result |
|---|---|---|
| comp-pydeps | `consumers pipeline_cli` | 5 consumers (3 test files + safe_deploy_core INVOKE + extract_s3 IMPORT) -- membership evidence |
| comp-which | A.3 exercise probe | forwarder RAN (banner) |
| pytest | 4-file candidate suite | 30 passed -- exposed the 41-vs-30 membership question |
| pytest | 5-file gate suite | **46 passed** baseline green |
| owned-paths validator | check_agent x4 paths + neg control | ~D True on all build paths; False on audit log; control discriminates |

## Open at this window's close

- Deliverables commit (gate + installer, probe removed) -- next action.
- First REAL fire = F1's engine commit (sibling TO, same seat, next work item).
- SURFACED, not mine: `org/modules/graph/tests/test_adapter_audit.py` is COLLECTION-BROKEN at
  HEAD (imports `adapter_audit_cli.py` which does not exist -- likely mass-deletion residue).
  Any whole-dir pytest run of `org/modules/graph/tests/` now dies at collection. Routing to COO
  with the F9 Phase-3 report.

-- 0.8.0_AE_CloudComp~D
