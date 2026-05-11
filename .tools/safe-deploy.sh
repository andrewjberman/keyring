#!/usr/bin/env bash
# safe-deploy.sh -- atomic DS deploy gate: S3 cp + SHA verify + comp-pipescript confirm.
# ADHC_DSFLOW.005 (0.7.0_AE_CloudOps, 2026-05-11)
#
# Structural enforcement for CLAUDE.md rule 13:
#   DS commit -> push -> S3 cp -> verify MATCH -> SSM dispatch.
# Replaces the cultural reminder with a gate that structurally closes the gap.
#
# Usage:
#   .tools/safe-deploy.sh [--allow-stale --reason "..."] [--author "..."]
#       [--commit-range <old>..<new>] [--no-pipescript] [file1 file2 ...]
#
#   Called directly with explicit files OR via pre-push hook with --commit-range.
#   With no arguments: detects changed scripts in HEAD~1..HEAD.
#
# Exit codes:
#   0 = all files deployed and verified (or --allow-stale bypass)
#   1 = gate failure (upload error, SHA mismatch, STALE/MISSING after deploy)
#   2 = usage error
#
# Bypass:
#   --allow-stale  Skips deploy+verify; writes audit entry.
#                  Requires --reason. Use for: emergency hotfix when comp-pipescript
#                  is broken, docstring-only changes, multi-agent worktree contention.
#   Audit log: org/safe-deploy-bypass-audit.log
#
# Pipeline->S3 mapping (baked into safe_deploy_core.py):
#   data/black_diamond/scripts/{gold,silver,bronze}/*.py  -> opal-data-bd
#   data/orion/scripts/{gold,silver,bronze}/*.py          -> opal-data-inf

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="python"
command -v python3 >/dev/null 2>&1 && PYTHON="python3"

exec "$PYTHON" "$SCRIPT_DIR/safe_deploy_core.py" "$@"
