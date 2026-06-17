#!/usr/bin/env bash
# =============================================================================
# safe-destroy.sh -- HALTGT-gated wrapper for ANY destructive operation
#                    (path-independent HALTGT; deploy-tooling hardening 2026-06-17)
# =============================================================================
# safe-apply.sh gates `terraform apply` ONLY. A destructive op expressed as a
# bare `aws ... delete-*` CLI call, a boto3 teardown script, or `terraform
# destroy` bypasses the HALTGT checkpoint entirely -- the gate was
# PATH-DEPENDENT (CLI/boto3/TF each a different surface; only one was gated).
# The 2026-06-16 causality teardown ran its boto3 delete leg gated only by author
# discipline + a human GO, never hitting the checkpoint -- the residual exposure
# COO flagged ("the gate must not depend on path/representation").
#
# safe-destroy fires the SAME ADHC_HALTGT.001 checkpoint (halt-gate-check.sh)
# immediately before the irreversible command -- the last reversible moment --
# then execs the command unchanged. CLI / boto3-script / terraform-destroy all
# hit ONE gate. Same fail-closed + same env-var ack/override contract as
# safe-apply (HALT_ACK / HALT_OVERRIDE are read inside the checkpoint).
#
# Behaviour (mirrors safe-apply.sh):
#   - Runs the .001 checkpoint FIRST against the running agent's MCP inbox.
#   - Checkpoint blocks (STOP-class -> exit 2, or routine without HALT_ACK=1 ->
#     exit 1) -> safe-destroy exits with that code and the command is NEVER run.
#   - Checkpoint passes (empty inbox / routine acked / audited STOP override) ->
#     delegates via exec to the command, passing every argument through unchanged;
#     the command's exit code propagates.
#   - Fails CLOSED (exit 3) if the checkpoint library is missing -- a destructive
#     op must NEVER run ungated.
#
# Usage:
#   .tools/safe-destroy.sh <command> [args...]
#   .tools/safe-destroy.sh aws dynamodb delete-table --table-name foo
#   .tools/safe-destroy.sh python teardown_causality.py --go      # gates the whole
#                                                                 # boto3 teardown
#   .tools/safe-destroy.sh -- .tools/terraform.exe -chdir=DIR destroy -auto-approve
#   HALT_ACK=1       .tools/safe-destroy.sh ...   # re-run after a routine surface
#   HALT_OVERRIDE="reason" .tools/safe-destroy.sh ...   # audited STOP bypass
#
# An optional leading `--` separates safe-destroy from the command (useful when
# the command itself starts with a dash).
#
# Env:
#   SAFE_DESTROY_LABEL  context label shown in the checkpoint banner
#                       (default: "safe-destroy:<argv0>").
#
# Git Bash 3.6.7-safe (CLAUDE.md Rule 16): no pgrep/pkill/flock/pidof/setsid/wget.
# ASCII only -- no emoji.
# =============================================================================
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HALT_GATE="$SCRIPT_DIR/halt-gate-check.sh"

# Optional `--` separator before the command.
if [ "${1:-}" = "--" ]; then
  shift
fi

if [ "$#" -eq 0 ]; then
  echo "safe-destroy: ERROR -- no command given." >&2
  echo "safe-destroy: usage -- safe-destroy.sh <command> [args...]" >&2
  echo "safe-destroy: gates ANY destructive op (CLI / boto3 script / terraform" >&2
  echo "              destroy) behind the HALTGT checkpoint." >&2
  exit 2
fi

LABEL="${SAFE_DESTROY_LABEL:-safe-destroy:$1}"

# HALTGT checkpoint -- fired immediately before the irreversible command.
if [ -f "$HALT_GATE" ]; then
  # shellcheck source=/dev/null
  . "$HALT_GATE"
  halt_gate_check "$LABEL" || exit $?
else
  echo "safe-destroy: ERROR -- halt-gate-check.sh not found at $HALT_GATE;" >&2
  echo "              refusing to run a destructive op ungated." >&2
  echo "safe-destroy: the HALTGT net cannot run without its checkpoint library." >&2
  exit 3
fi

# Checkpoint passed -- exec the destructive command; exec propagates its exit code.
exec "$@"
