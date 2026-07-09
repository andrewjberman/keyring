#!/usr/bin/env bash
# =============================================================================
# mass-deletion-check.sh -- ATTRIBUTION gate for mass deletion of tracked files.
#
# CTO ruling 2026-07-09T192324Z (reversing his own WARN-only call on new
# empirical evidence, per his standard: a ruling reverses on evidence, never on
# a re-read):
#
#     "A mass deletion of tracked files is LEGAL. An UNATTRIBUTED one is not."
#
# The discriminator is ATTRIBUTION, not COUNT. Andrew's deliberate 903-file
# logs/ cleanup is legitimate and must pass. A bare `git commit -a` silently
# carrying 932 deletions off a shared index must not.
#
# WHY THIS IS A commit-msg HOOK AND NOT pre-commit / safe-commit:
#
#   1. safe-commit.sh STRUCTURALLY CANNOT catch this. It BASELINEs everything
#      already staged at lock-entry (safe-commit.sh:260-261, comment: "foreign +
#      any caller pre-add") and excludes baselined files from its contamination
#      check (:321). An armed mass-deletion is, by definition, baseline. It is
#      never contamination, never printed, never blocked. Two commits landed
#      cleanly on 2026-07-09 with 167 deletions armed (e23a9b965, bfbf89ba7).
#      safe-commit is nonetheless SAFE by construction -- :421 commits
#      `--only -- PATHSPEC`, so foreign staged content is excluded regardless of
#      --force. It does not need this gate. The paths that bypass it do.
#
#   2. pre-commit cannot see the commit message, so it cannot read the
#      Authorized-Deletion trailer. commit-msg receives the message file AND an
#      index view that honors $GIT_INDEX_FILE. Both are required here.
#
# EXERCISED before being written (not inferred -- the failure this gate exists
# to catch is silent, so an unexercised gate would be worthless):
#
#   git commit -a       + 12 worktree deletions -> hook sees 12   (CATCHES)
#   bare git commit     + 12 armed deletions    -> hook sees 12   (CATCHES; and
#                                                   bare commit DID commit them)
#   git commit --only   + 12 foreign deletions  -> hook sees 0    (NO false pos;
#                        GIT_INDEX_FILE = .git/next-index-NNNN.lock, a temp index
#                        holding only the pathspec)
#   pure `git mv` move (12 files)               -> D=0, R=12      (SILENT)
#   move + CRLF perturbation                    -> D=0, R=12      (SILENT)
#   true deletion (12 files)                    -> D=12           (FIRES)
#
# RENAME DETECTION IS LOAD-BEARING. `git diff --cached --diff-filter=D` has
# rename detection ON by default, so a MOVE is classified R, not D. This is
# precisely what makes CTO's "it does not fire on Andrew" true: his infra/aws
# archive move (byte-identical modulo CRLF) scores R and is invisible here.
# NEVER add --no-renames: it reports that same move as 12 deletions.
#
# Ramp (CTO): WARN for 48h with attribution printed, then flip to BLOCK.
# Flip is DATE-DRIVEN (BLOCK_AFTER_EPOCH below) so it happens whether or not
# anyone remembers. Override either way with MASS_DELETE_MODE=warn|block.
# Self-check the ramp state at any time:  bash .tools/git-hooks/mass-deletion-check.sh --mode
#
# Bypass (audited): FORCE_DELETE=1 git commit ...
# Attribute (the intended path): add a trailer to the commit message --
#   Authorized-Deletion: LD-0262
#   Authorized-Deletion: org/critical_paths/change_management/<ledger>.md
#
# Rule 16: Git Bash 3.6.7 default utilities only (git, wc, grep, sed, date).
# CLAUDE.md Code Quality: ASCII only -- no emoji, no non-ASCII.
# =============================================================================
set -e

MSG_FILE="${1:-}"
THRESHOLD="${MASS_DELETE_THRESHOLD:-25}"

# End of the 48h WARN ramp. SINGLE SOURCE OF TRUTH: the human-readable date is
# DERIVED from this epoch at runtime, never hardcoded alongside it.
#
# INCIDENT (mine, 2026-07-09T19:47Z, caught 7 min after push): I first shipped
# 1783452600 here and a hardcoded "2026-07-11T19:30Z" in the messages. That epoch
# is 2026-07-07T19:30Z -- two days in the PAST -- so the gate went live BLOCKING
# on a shared worktree, against CTO's explicit WARN ramp, while the printed string
# cheerfully said WARN. Two sources of truth, and the one humans read was the one
# that lied.
#
# The deeper error: my test matrix passed 10/10 because every ramp case forced
# MASS_DELETE_MODE=warn|block explicitly. I exercised the OVERRIDE and never the
# DEFAULT. A test that only drives the path you control cannot fail on the path
# everyone else takes. Same class as the negative-control error CVO caught me in
# the same hour: rigor of form, wrong instrument.
BLOCK_AFTER_EPOCH=1783798200   # verified: date -u -d @1783798200 -> 2026-07-11T19:30:00Z
BLOCK_AFTER_ISO="$(date -u -d "@$BLOCK_AFTER_EPOCH" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo "epoch $BLOCK_AFTER_EPOCH")"

AUDIT_LOG="org/mass-deletion-audit.log"

# Resolve the effective mode. Extracted as a function precisely BECAUSE the
# date-driven default is the path nobody exercises -- `--mode` makes it
# assertable without constructing a commit. (The bug above shipped because the
# only ramp tests forced MASS_DELETE_MODE explicitly.)
_effective_mode() {
  local now; now="$(date -u +%s 2>/dev/null || echo 0)"
  case "${MASS_DELETE_MODE:-}" in
    block) echo block; return ;;
    warn)  echo warn;  return ;;
  esac
  if [ "$now" -gt "$BLOCK_AFTER_EPOCH" ] 2>/dev/null; then echo block; else echo warn; fi
}

# Self-check surface: `bash mass-deletion-check.sh --mode`
if [ "${1:-}" = "--mode" ]; then
  echo "mass-deletion gate"
  echo "  now              : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "  ramp flips at    : $BLOCK_AFTER_ISO"
  echo "  MASS_DELETE_MODE : ${MASS_DELETE_MODE:-<unset, date-driven>}"
  echo "  effective mode   : $(_effective_mode)"
  echo "  threshold        : $THRESHOLD deleted tracked files"
  exit 0
fi

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[ -n "$ROOT" ] || exit 0

# A merge commit's deletions come from the merged branch, not from this
# committer. `git pull` (merge) after a legitimate cleanup lands would otherwise
# false-positive on every lane. NEVER rebase (CLAUDE.md), so merges are the
# normal integration path and must stay silent here.
if [ -f "$ROOT/.git/MERGE_HEAD" ] || [ -f "$ROOT/.git/CHERRY_PICK_HEAD" ]; then
  exit 0
fi

# Rename detection ON (default). A move is R, not D. See header.
DELETED="$(git diff --cached --diff-filter=D --name-only 2>/dev/null || true)"
if [ -z "$DELETED" ]; then
  exit 0
fi
N_DEL="$(printf '%s\n' "$DELETED" | grep -c . || true)"
[ "$N_DEL" -gt "$THRESHOLD" ] || exit 0

# ---- Attribution: the Authorized-Deletion trailer -------------------------
TRAILER=""
if [ -n "$MSG_FILE" ] && [ -f "$MSG_FILE" ]; then
  # Strip comment lines; match the trailer key case-insensitively.
  TRAILER="$(grep -v '^#' "$MSG_FILE" 2>/dev/null \
             | grep -iE '^[[:space:]]*Authorized-Deletion:[[:space:]]*' \
             | sed -E 's/^[[:space:]]*[Aa]uthorized-[Dd]eletion:[[:space:]]*//' \
             | sed -E 's/[[:space:]]+$//' \
             | grep -v '^$' | head -1 || true)"
fi

# An attribution must REFER to something. A magic word is not attribution:
# accept an LD-#### id, or a path to a real ledger file under org/critical_paths/.
ATTRIBUTED=0
ATTR_REASON=""
if [ -n "$TRAILER" ]; then
  if printf '%s' "$TRAILER" | grep -qE '^LD-[0-9]{3,}$'; then
    ATTRIBUTED=1; ATTR_REASON="ledger-id $TRAILER"
  elif [ -f "$ROOT/$TRAILER" ]; then
    ATTRIBUTED=1; ATTR_REASON="ledger-file $TRAILER"
  else
    ATTR_REASON="UNRESOLVABLE trailer '$TRAILER' (not an LD-#### id; not an existing file)"
  fi
fi

ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown)"
AGENT="$(git config user.name 2>/dev/null || echo unknown)"
MODE="$(_effective_mode)"

_audit() {  # $1 = verdict
  mkdir -p "$(dirname "$ROOT/$AUDIT_LOG")" 2>/dev/null || true
  printf '%s  %-9s  agent=%s  deletions=%s  threshold=%s  mode=%s  attribution=%s\n' \
    "$ISO" "$1" "$AGENT" "$N_DEL" "$THRESHOLD" "$MODE" \
    "${ATTR_REASON:-<none>}" >> "$ROOT/$AUDIT_LOG" 2>/dev/null || true
}

_show() {
  echo "" >&2
  echo "MASS-DELETION GATE -- $N_DEL tracked file(s) deleted in this commit (threshold $THRESHOLD)." >&2
  echo "  A mass deletion of tracked files is LEGAL. An UNATTRIBUTED one is not." >&2
  echo "" >&2
  echo "  Deleting (first 10):" >&2
  printf '%s\n' "$DELETED" | head -10 | sed 's/^/    /' >&2
  if [ "$N_DEL" -gt 10 ]; then echo "    ...and $((N_DEL - 10)) more" >&2; fi
  echo "" >&2
  echo "  NOTE: a MOVE is not a deletion here (rename detection is on). If you" >&2
  echo "  intended to move these, use 'git mv' or stage both sides together." >&2
  echo "" >&2
}

# ---- Verdict --------------------------------------------------------------
if [ "$ATTRIBUTED" -eq 1 ]; then
  _audit "ATTRIBUTED"
  echo "OK: mass-deletion gate -- $N_DEL deletion(s) ATTRIBUTED ($ATTR_REASON)." >&2
  exit 0
fi

if [ -n "${FORCE_DELETE:-}" ]; then
  _audit "FORCE-BYPASS"
  _show
  echo "WARN: FORCE_DELETE override -- $N_DEL deletion(s) committed WITHOUT attribution." >&2
  echo "      Audited to $AUDIT_LOG" >&2
  exit 0
fi

_show
if [ -n "$ATTR_REASON" ]; then
  echo "  $ATTR_REASON" >&2
  echo "" >&2
fi
echo "  To ATTRIBUTE (the intended path) add a trailer to the commit message:" >&2
echo "      Authorized-Deletion: LD-0262" >&2
echo "      Authorized-Deletion: org/critical_paths/change_management/<ledger>.md" >&2
echo "" >&2
echo "  To bypass (audited):  FORCE_DELETE=1 git commit ..." >&2
echo "" >&2

if [ "$MODE" = "block" ]; then
  _audit "BLOCKED"
  echo "ERROR: BLOCKED -- unattributed mass deletion. Commit aborted." >&2
  echo "" >&2
  exit 1
fi

_audit "WARNED"
echo "WARN: mass-deletion gate is in WARN mode (ramp ends $BLOCK_AFTER_ISO, then BLOCKS)." >&2
echo "      This commit PROCEEDS. Attribute it now and the flip is a no-op for you." >&2
echo "" >&2
exit 0
