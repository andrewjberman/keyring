# AE 0.7.0 Session Log — ADHC_DSFLOW.005 safe-deploy gate
**Date:** 2026-05-11
**Agent:** 0.7.0_AE_CloudOps
**TO:** ADHC_DSFLOW.005

## Objective
Atomic deploy wrapper: close CLAUDE.md rule 13 cultural->structural gap.
DS commit -> push -> S3 cp -> SHA verify -> comp-pipescript confirm, in one indivisible call.
Fold INF silver coverage gap in comp-pipescript deployed.

## Trigger
COO GO received 2026-05-11T184747Z. ID-DTYPE-ENFORCEMENT complete (DS~B commit `7b6c0523d`).
CTO clearance via inbox: "You're cleared to execute ADHC_DSFLOW.005 on DS~B's RAVC2 close signal."

## Design Decision — Option C (hybrid)

Pre-push hook calls safe-deploy.sh internally. Best of both Option A (named discoverable script) and Option B (invisible structural enforcement). Matches existing pattern: safe-commit.sh (ADHC_OWNPTH.007) + owned-paths hook (ADHC_OWNPTH.003).

## Files Delivered

| File | Description |
|------|-------------|
| `.tools/safe_deploy_core.py` | Core logic: file->S3 mapping, detect changed scripts, deploy_file, pipescript verify, bypass audit |
| `.tools/safe-deploy.sh` | Thin bash entry point; delegates to safe_deploy_core.py |
| `.tools/git-hooks/pre-push-safe-deploy.sh` | Pre-push hook; reads push refspec, calls safe-deploy.sh |
| `.tools/git-hooks/install-safe-deploy-hook.sh` | Idempotent hook installer (chains if pre-push already exists) |
| `.tools/test_safe_deploy.py` | 6-fixture test suite (no real AWS required; subprocess mocked) |
| `org/modules/graph/pipeline_cli.py` | INF silver local dir fix: SILVER_LOCAL_DIR now table-driven per pipeline |

## Pipeline->S3 Mapping (baked into safe_deploy_core.py)
- `data/black_diamond/scripts/{gold,silver,bronze}[/lib]/*.py` → `s3://opal-data-bd/code/{layer}/`
- `data/orion/scripts/{gold,silver,bronze}[/lib]/*.py` → `s3://opal-data-inf/code/{layer}/`

## INF Coverage Fix (pipeline_cli.py cmd_deployed)

Bug: `SILVER_LOCAL_DIR` hardcoded to BD silver path for all pipelines.

Fix: table-driven dict `_PIPELINE_SILVER_DIRS` keyed by pipeline arg:
- `bd-gold` / `bd-silver` → `data/black_diamond/scripts/silver/`
- `inf-gold` / `inf-silver` → `data/orion/scripts/silver/`

Eliminates DS~B's manual hashlib workaround for INF silver verification.

## Compiler Tools Run

| Tool | Command | Result |
|------|---------|--------|
| py_compile | python -m py_compile .tools/safe_deploy_core.py | OK |
| py_compile | python -m py_compile .tools/test_safe_deploy.py | OK |
| ruff | ruff check --target-version py39 .tools/safe_deploy_core.py .tools/test_safe_deploy.py | 3 unused imports fixed; re-run PASS |
| py_compile | python -m py_compile org/modules/graph/pipeline_cli.py | OK |
| ds-commit-gate | .tools/ds-commit-gate.sh .tools/safe_deploy_core.py .tools/test_safe_deploy.py | PASS (2 files) |
| comp-shell | .tools/ds-commit-gate.sh *.sh hook files | PASS (3 files) |
| hook install | bash .tools/git-hooks/install-safe-deploy-hook.sh | OK: installed at .git/hooks/pre-push |
| test suite | python .tools/test_safe_deploy.py | 6/6 PASS |

## Test Results

| Case | Description | Result |
|------|-------------|--------|
| PASS | gold script upload OK, ETag matches local MD5 | PASS |
| FAIL-NODEPLOY | stale ETag detected (simulates no-S3-deploy push) | PASS |
| FAIL-PARTIAL | first file OK, second upload fails, fast-fail | PASS |
| FAIL-MISMATCH | ETag corrupted post-upload, SHA guard fires | PASS |
| BYPASS | --allow-stale writes audit entry with author+files+sha+reason | PASS |
| INF-PATH | data/orion/* maps to opal-data-inf, bd → opal-data-bd | PASS |

## Acceptance Criteria Status

| AC | Status |
|----|--------|
| AC1: Design decision documented | DONE (Option C, rationale above) |
| AC2: Diff detection for data/*/scripts/*.py | DONE (file_to_s3_target + detect_script_files) |
| AC3: S3 deploy phase idempotent, fail-safe | DONE (fast-fail on error, no partial guarantee noted in output) |
| AC4: comp-pipescript verify integrated | DONE (run_pipescript_verify, STALE/MISSING = fail) |
| AC5: INF coverage fix PASS | DONE (SILVER_LOCAL_DIR table-driven; py_compile PASS) |
| AC6: --allow-stale bypass audit-logged | DONE (org/safe-deploy-bypass-audit.log, author+pathspec+sha+reason) |
| AC7: 6 synthetic fixtures all PASS | DONE (6/6) |
| AC8: 100% PASS post-incident state | N/A (DS~A `c2a7a5967` gap would now be caught; can't retroactively test) |
| AC9: CLAUDE.md rules 13+14 | PENDING — draft sent to CTO for co-sign (20260511T190002Z) |
| AC10: Memory entry | DONE (memory/feedback_safe_deploy_gate.md) |
| AC11: RAVC delivered | PENDING (sending post-commit) |

## Pending
- CTO co-sign on CLAUDE.md rules 13+14 wording
- Commit + push (all files except CLAUDE.md now; CLAUDE.md after CTO ACK)
- RAVC2 to COO + CTO on full close

## Blockers
- ADHC_INFRUNNERPARITY: unblocked by this TO close. Next TO.
