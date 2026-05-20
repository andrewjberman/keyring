# ADHC_HALTGT.002 — wire checkpoint into deploy paths

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/ADHC_HALTGT.002.ae-wire-checkpoint-into-deploy-paths.md`

---

## Current State

- **ADHC_HALTGT.002: COMPLETE.** The ADHC_HALTGT.001 checkpoint library is now sourced
  from the 3 existing deploy/push structural-enforcement points. Part of the COO~B
  batch GO; next in sequence: .003.

## What shipped

One sourced checkpoint call added to each of 3 scripts — the `.001` library is sourced,
never duplicated; existing gate logic untouched (do_not compliance):

| Script | Insertion point | Repo var |
|--------|-----------------|----------|
| `.tools/git-hooks/pre-push-safe-deploy.sh` | after the safe-deploy existence check, before the `while read` refspec loop | `$REPO_ROOT` |
| `.tools/safe-deploy.sh` | after `SCRIPT_DIR`/`PYTHON` setup, before `exec safe_deploy_core.py` | `$SCRIPT_DIR` (is `.tools/`) |
| `infra/aws/ec2/safe-ec2-deploy.sh` | after "Pre-deployment checks passed", before "Step 2/3: Running Deployment" | `$WORKSPACE_ROOT` |

The inserted block is identical in shape across all 3: `if [ -f "$HALT_GATE" ]` ->
`. "$HALT_GATE"` -> `halt_gate_check "<context>" || exit $?`. The `-f` guard means a
missing library degrades gracefully (no hard dependency). The library never reads
stdin, so the pre-push hook's git refspec on stdin is intact.

Note: `safe-ec2-deploy.sh` carries pre-existing emoji (check-marks / box-drawing /
warning glyphs in its `print_*` helpers). Left untouched — fixing them is a refactor
of existing logic, out of this TO's scope (do_not rule). My added lines are ASCII-only.

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| Phase 1 — read `.tools/halt-gate-check.sh` + the 3 insertion-point scripts | OK | `.001` exposes `halt_gate_check` with the documented exit-code contract (0/1/2/3); insertion line identified in each script before its irreversible step. `safe-ec2-deploy.sh` confirmed at `infra/aws/ec2/safe-ec2-deploy.sh` (Rule 7). comp-* N/A — `.tools/` shell + git hooks not graph-modeled (PRD section 5). |
| Phase 2 — `shellcheck` on the 3 modified scripts | **NOT RUN — shellcheck not installed** in this Git Bash env. Substitute: `bash -n` clean on all 3. The added blocks carry a `# shellcheck source=/dev/null` directive (silences SC1090 for the non-constant source). Self-audited: vars quoted, no banned utilities, sourced not duplicated. Flagged (same gap as .001). |
| Phase 3 — anchor test (`.runtmp/haltgt002_anchor_test.sh`, sandboxed inbox/context, `</dev/null`) | **10/10 PASS** | See transcript. |

## Verification — Phase 3 anchor test (10/10 PASS)

```text
=== pre-push-safe-deploy.sh ===
  PASS: STOP -> non-zero (blocked)        PASS: STOP surfaced before push
  PASS: routine(no ack) -> non-zero       PASS: routine surfaced
=== safe-deploy.sh ===
  PASS: STOP -> non-zero (blocked)        PASS: STOP surfaced before exec core.py
  PASS: core.py NOT reached (no exec)     PASS: routine(no ack) -> non-zero
=== safe-ec2-deploy.sh ===
  PASS: STOP -> checkpoint reached + blocked non-zero
  PASS: deploy step NOT reached
RESULT: 10 passed, 0 failed
```

STOP-class and routine-unacked verdicts were live-run for each script — both abort
BEFORE the irreversible step (push / `exec core.py` / "Step 2/3" deploy), so no real
deploy occurred. Empty-inbox and routine+ack pass-through were NOT live-run (they fall
through to the real irreversible step) — they are covered by the `.001` exit-code
contract (exit 0 on empty/acked, verified 7/7 in .001) plus the `|| exit $?` gate,
which only fires on a non-zero result.

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 validation; routes to CTO~B. shellcheck-absent flag carries
  over from .001.
- `[0.5.0_AE_OpalETL~B]` Proceed to ADHC_HALTGT.003 (safe-apply.sh terraform checkpoint).
