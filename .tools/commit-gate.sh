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
# Shell  (.sh): bash -n (syntax) on EVERY .sh whatever its path + comp-shell scan
#               (forbidden Git Bash 3.6.7 utility check, CLAUDE.md Rule 16) + comp-manifest-
#               check. Only in-scope local-runtime paths are comp-shell-SCANNED (.tools/,
#               org/mcp/, org/threads/, infra/aws/lambda/ci/, infra/aws/terraform/) -- an EC2
#               script is not a Git Bash 3.6.7 subject, so that scope is deliberate and is
#               NOT widened; bash -n and comp-manifest-check run on ALL .sh regardless.
#
# EXIT CODES -- what each one means, and none of them promises a check this gate does not run:
#   0  every DISPATCHED file was checked and is clean; or nothing was dispatched at all
#      (a commit of only .md/.ts/.json-outside-org/projects is a legitimate no-op and prints
#      the WARN below).
#   1  a check FAILED on some file. Blocking.
#   2  REFUSAL, and it is neither a pass nor a check failure: a file whose suffix this gate
#      DECLARES it reads (.py / .sh / .tf / org/projects/*.json) reached ZERO checks. That is
#      a GATE DEFECT -- the gate did not do the job this header advertises -- and rc=2 exists
#      so it can never be read as a clean commit. Do not re-run for a 0; fix the gate.
#      (ADHC_COMMITGATE.TO-ZEROCHECK-REFUSE. Before it, that state exited 0: measured on a
#      .sh with a planted syntax error and a clean .sh in the same out-of-scope directory --
#      byte-identical output, rc=0 for both, so the exit code carried no information at all.)
#
# Silent on pass, with one exception: each .sh prints "OK: bash -n syntax-checked <file>", so
# the "N of N file(s)" summary names its instrument per file instead of asserting a number.
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
