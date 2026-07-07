#!/bin/bash
# commit-gate.sh -- universal pre-commit gate for Python and shell scripts.
#
# Renamed off "ds-commit-gate.sh" (ADHC_COMMITGATE, CTO condition 3): this gate is
# universal/ANY-lane -- every agent's every .py/.sh commit runs through it, it was never
# DS-specific despite the old name.
#
# ADHC_COMMITGATE consolidation: delegates ALL files to ONE python process
# (commit_gate_runner.py), which calls the same checks the old per-file bash loop forked
# 6 separate python subprocesses for (py_compile, ds-precommit-check.py, ruff,
# comp_constants_cli.py, manifest_check_cli.py, log_open_lint.py) -- now direct in-process
# function calls, except ruff (no stable Python API, stays one subprocess per file). See
# commit_gate_runner.py's own docstring for the full parity-safety rationale + the fixture
# set that verified byte-identical output/exit-code parity vs the old per-file-fork design.
#
# Python (.py): py_compile + AST undefined-name scan + ruff + comp-constants drift +
#               comp-manifest-check + log-open-lint.
# Shell  (.sh): comp-shell scan (forbidden Git Bash 3.6.7 utility check, CLAUDE.md Rule 16)
#               + comp-manifest-check. Only in-scope local-runtime paths are comp-shell-
#               scanned (.tools/, org/mcp/, org/threads/, infra/aws/lambda/ci/,
#               infra/aws/terraform/); comp-manifest-check runs on ALL .sh regardless.
#
# Blocks (exit 1) on any failure. Silent on pass.
#
# Usage:
#   .tools/commit-gate.sh data/black_diamond/scripts/gold/B_00.py
#   .tools/commit-gate.sh $(find data/black_diamond/scripts/gold -name "*.py")
#   .tools/commit-gate.sh .tools/my-new-helper.sh
#
# Ruff: install via `pip install ruff`. Pinned version: 0.15.11 (ADHC_DSFLOW.004).
# If ruff is absent, gate exits 1 immediately (ruff is required, not optional).
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Windows-safe path form for the runner path passed to the native python.exe
# (ADHC_DSFLOW.007, carried over unchanged from ds-commit-gate.sh). Git Bash `pwd -W`
# yields mixed form (C:/Users/...) that python.exe opens correctly REGARDLESS of
# MSYS_NO_PATHCONV state; the bare POSIX form breaks when MSYS_NO_PATHCONV=1 is exported
# (mandated for every Terraform/AWS-CLI session) -- see commit_gate_runner.py's own
# import-time behavior for why this must resolve correctly before any check runs.
SCRIPT_DIR_WIN="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -W 2>/dev/null || printf '%s' "$SCRIPT_DIR")"

exec python "$SCRIPT_DIR_WIN/commit_gate_runner.py" "$@"
