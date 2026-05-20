#!/usr/bin/env bash
# =============================================================================
# safe-apply.sh -- HALTGT-gated `terraform apply` wrapper (ADHC_HALTGT.003)
# =============================================================================
# The PRIMARY HALTGT net. `terraform apply` is the irreversible step and it
# precedes the git push, so a pre-push-only checkpoint (ADHC_HALTGT.002) lets
# the apply happen before a STOP is seen. safe-apply fires the ADHC_HALTGT.001
# checkpoint immediately before the apply -- the last reversible moment.
#
# Behaviour:
#   - Runs the .001 checkpoint (.tools/halt-gate-check.sh) FIRST.
#   - Checkpoint blocks (STOP-class, or routine without HALT_ACK=1) -> safe-apply
#     exits non-zero and terraform is NEVER invoked.
#   - Checkpoint passes -> delegates via exec to the real terraform binary with
#     every argument passed through unchanged; terraform's exit code propagates.
#   - Gates `apply` ONLY. `plan` and other subcommands are non-destructive --
#     call terraform.exe directly for those.
#
# Usage (pass args exactly as to terraform.exe, INCLUDING the `apply` word):
#   .tools/safe-apply.sh [-chdir=DIR] apply [apply-args...]
#   HALT_ACK=1 .tools/safe-apply.sh ... apply ...     # re-run after a routine surface
#
# Env:
#   SAFE_APPLY_TERRAFORM  Override the terraform binary (default: sibling terraform.exe).
#
# Git Bash 3.6.7-safe (CLAUDE.md Rule 16). ASCII only -- no emoji.
# =============================================================================
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TERRAFORM="${SAFE_APPLY_TERRAFORM:-$SCRIPT_DIR/terraform.exe}"
HALT_GATE="$SCRIPT_DIR/halt-gate-check.sh"

# Gate `apply` only -- refuse if no `apply` subcommand is present.
has_apply=0
for arg in "$@"; do
  if [ "$arg" = "apply" ]; then
    has_apply=1
    break
  fi
done
if [ "$has_apply" -ne 1 ]; then
  echo "safe-apply: ERROR -- no 'apply' subcommand in the arguments." >&2
  echo "safe-apply: this wrapper gates 'terraform apply' only. For 'plan' or any" >&2
  echo "            other subcommand call the terraform binary directly." >&2
  echo "safe-apply: usage -- safe-apply.sh [-chdir=DIR] apply [apply-args...]" >&2
  exit 2
fi

# HALTGT checkpoint -- fired immediately before the irreversible apply.
if [ -f "$HALT_GATE" ]; then
  # shellcheck source=/dev/null
  . "$HALT_GATE"
  halt_gate_check "safe-apply" || exit $?
else
  echo "safe-apply: ERROR -- halt-gate-check.sh not found at $HALT_GATE; refusing to apply ungated." >&2
  echo "safe-apply: the primary HALTGT net cannot run without its checkpoint library." >&2
  exit 3
fi

# Checkpoint passed (empty inbox, or routine acked, or audited STOP override).
# Delegate to terraform; exec propagates its exit code transparently.
exec "$TERRAFORM" "$@"
