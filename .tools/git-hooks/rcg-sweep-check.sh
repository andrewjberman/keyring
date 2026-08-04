#!/usr/bin/env bash
# =============================================================================
# rcg-sweep-check.sh -- pre-commit enforcement of ruling CTOB-RCG-001.
#
# Constrains the RCG sweep-executor identity to doing exactly one thing: executing
# a ratified, pre-committed, content-bound ARCHIVE batch, and nothing else.
#
#     AUTHORITY ATTACHES TO THE BATCH, NOT TO THE SEAT.
#
# FIRES ON AUTHOR IDENTITY, NOT ON A DECLARED TRAILER. This is the load-bearing
# choice. A gate that only fires when the committer declares "this is a sweep" is
# evaded by not declaring one; keying on identity means every commit that identity
# ever makes is checked, so no un-gated commit shape exists for that seat. It is
# also what makes the seat's broad delete lane safe: the lane is wide, and this
# gate is what makes it unusable for anything but an exact ratified batch.
#
# WHY PRE-COMMIT AND NOT commit-msg: its sibling mass-deletion-check.sh lives in
# commit-msg BECAUSE it must read the Authorized-Deletion trailer. This gate reads
# the index and the ledger, both available earlier, and pre-commit runs in the same
# invocation as owned-paths. mass-deletion-check STILL APPLIES to sweep commits --
# batches carry their trailer, the estate-wide deletion audit stays complete, and
# neither gate blinds the other.
#
# BATCH ID comes from RCG_BATCH_ID in the environment:
#     RCG_BATCH_ID=B-0001 git commit ...
# Absent, this DENIES. That is not a bypass -- omitting it blocks the commit, it
# does not permit one. There is deliberately no file-based "active batch" pointer:
# a mutable pointer read at execution is exactly the indirection this ruling exists
# to remove.
#
# rc: 0 permit | 1 DENY. The engine's rc=2 (deny) and rc=3 (cannot-evaluate) BOTH
# become 1 -- a property that cannot be established is never a pass.
#
# Ruling: org/tier1_exec/1.0.0_SA_CTO/deliverables/RCG_SWEEP_MECHANICS_RULING_20260804.md
# Rule 16: Git Bash 3.6.7 default utilities only. ASCII only.
# Author: 1.0.0_SA_CTO~B, 2026-08-04 (D-0001 item 5 / D-0004 / R-0021).
# =============================================================================
set -e

ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
[ -n "$ROOT" ] || exit 0

# The sweep-executor identity. A commit by any other author is none of this
# gate's business and exits silently -- zero cost on every ordinary commit.
SWEEP_IDENTITY="${RCG_SWEEP_IDENTITY:-4.0.0_SA_CRO~SWEEP}"

RAW_AUTHOR="$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//' || true)"
[ "$RAW_AUTHOR" = "$SWEEP_IDENTITY" ] || exit 0

ENGINE="$ROOT/.tools/rcg_sweep_verify.py"
AUDIT="$ROOT/org/rcg-sweep-audit.log"
ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown)"

_audit() {  # $1 verdict  $2 detail
  printf '%s  %-14s  batch=%s  %s\n' "$ISO" "$1" "${RCG_BATCH_ID:-<unset>}" "$2" \
    >> "$AUDIT" 2>/dev/null || true
}

_deny() {  # $1 message
  echo "" >&2
  echo "BLOCKED: RCG sweep gate -- $1" >&2
  echo "  Ruling CTOB-RCG-001. The sweep identity may commit NOTHING except an exact" >&2
  echo "  ratified batch: deletion-only, set-equal to the batch, every property" >&2
  echo "  re-derived at HEAD." >&2
  echo "" >&2
  _audit "DENIED" "$1"
  exit 1
}

if [ ! -f "$ENGINE" ]; then
    _deny "the verifier is MISSING at $ENGINE -- the lane this identity holds is only safe because this gate constrains it, so an absent gate is a DENY"
fi
if ! command -v python >/dev/null 2>&1; then
    _deny "'python' is not on PATH -- the gate cannot evaluate, which is a DENY"
fi
if [ -z "${RCG_BATCH_ID:-}" ]; then
    _deny "RCG_BATCH_ID is not set. Run: RCG_BATCH_ID=B-000N git commit ..."
fi

# Ramp cap (ruling s.7): 100 until batch 1's REVERT has been exercised, then
# 500, then uncapped -- each step gated on the prior batch's CVO verify closing
# clean. Deliberately an env override rather than a date-driven flip: this ramp
# advances on an EXERCISED revert, which no clock can observe. (Its sibling
# mass-deletion-check ramps on a date and its author's own header records that
# shipping a wrong epoch put the gate live two days early while the printed
# string still said WARN.)
CAP="${RCG_SWEEP_CAP:-100}"

# MODE. Default 'execute' (the deletion batch). 'revert' is the s.7 restore leg:
# addition-only, set-equal to the batch, and every blob hash-identical to the
# pre-deletion tree -- so revert mode can restore exactly what was deleted and
# nothing else. It exists because the restore leg was otherwise UNAUTHORABLE: the
# sweep identity is the only one holding those lanes (granting them is what made
# it so -- measured 93/93 vs 0/93 for every exec seat), and C1 forbade it from
# committing additions. A safety case that cannot be executed is not a safety case.
MODE="${RCG_SWEEP_MODE:-execute}"
case "$MODE" in
  execute|revert) ;;
  *) _deny "RCG_SWEEP_MODE='$MODE' is not a mode (expected 'execute' or 'revert')" ;;
esac

if ! python "$ENGINE" --batch-id "$RCG_BATCH_ID" --cap "$CAP" --mode "$MODE"; then
    _deny "batch $RCG_BATCH_ID failed $MODE verification (see the check output above)"
fi

_audit "PERMITTED" "mode=$MODE cap=$CAP"
exit 0
