#!/usr/bin/env bash
# install-all-git-hooks.sh -- wire EVERY git hook this repo depends on, in one command.
#
# RUN THIS ON EVERY FRESH CLONE. Git tracks nothing under .git/, so a new clone starts
# with ZERO hooks -- no owned-paths lane enforcement, no mstr-ledger-check, no
# mass-deletion-check, no branch-content-isolation, no stitch/missions refresh.
#
#   bash .tools/install-all-git-hooks.sh          # install everything (idempotent)
#   bash .tools/install-all-git-hooks.sh --check   # report only, change nothing
#
# WHY (LD-0343, measured 2026-07-29): a second device committed to the shared CLOUD
# branch and its owned-paths gate never fired -- not because the gate was wrong, but
# because it WAS NOT THERE. The same commit was correctly refused on the gated machine.
# THE UNGATED SITE IS THE ONE THAT SUCCEEDS: it receives no refusal, so it gets no
# signal that it is unguarded. A path/config census is structurally blind to this --
# there is nothing at the ungated clone to scan. Absence is the failure mode, so the
# check has to be run FROM the tooling, not looked for in the tree.
#
# DISCOVERY, NOT A HARDCODED LIST: installers are found by glob. A hardcoded roster is
# the same staleness bug one level up -- a new installer nobody adds to the list is a
# hook nobody installs.
#
# COMPLETENESS CHECK: discovery finds installers, but it CANNOT find a hook BODY that
# has no installer at all -- which is exactly how missions-refresh came to exist on
# only one machine (hand-chained into .git/hooks/post-commit, LD-0341). So this script
# also enumerates hook bodies and reports any that no installer references, and prints
# the denominator of both sets. A count with no denominator cannot report its own
# omissions.
#
# Local-runtime bash: Git Bash 3.6.7 default-install utilities only (CLAUDE.md Rule 16).
set -u

WS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOKDIR="$WS/.tools/git-hooks"
CHECK_ONLY=0
[ "${1:-}" = "--check" ] && CHECK_ONLY=1

if [ ! -d "$HOOKDIR" ]; then
  echo "FAIL: $HOOKDIR not found -- is this a clone of ajb_workspace?" >&2
  exit 1
fi

echo "install-all-git-hooks -- repo root: $WS"
echo "======================================================================"

# ---------------------------------------------------------------------------
# PASS 1 -- run every installer (or list them under --check)
# ---------------------------------------------------------------------------
INST_N=0; OK_N=0; FAIL_N=0; FAILED=""
for inst in "$HOOKDIR"/install-*.sh; do
  [ -f "$inst" ] || continue
  INST_N=$((INST_N + 1))
  base="$(basename "$inst")"
  if [ "$CHECK_ONLY" -eq 1 ]; then
    printf '  [check] would run %s\n' "$base"
    continue
  fi
  out="$(bash "$inst" 2>&1)"; rc=$?
  # Score on OUTPUT, not rc -- harness rc capture is corrupted on this host (LD-0340).
  if [ $rc -eq 0 ] && ! printf '%s' "$out" | grep -qi '^FAIL'; then
    OK_N=$((OK_N + 1)); printf '  [ok]   %-38s %s\n' "$base" "$(printf '%s' "$out" | tail -1)"
  else
    FAIL_N=$((FAIL_N + 1)); FAILED="$FAILED $base"
    printf '  [FAIL] %-38s %s\n' "$base" "$(printf '%s' "$out" | tail -1)"
  fi
done

echo "----------------------------------------------------------------------"
if [ "$CHECK_ONLY" -eq 1 ]; then
  echo "INSTALLERS DISCOVERED: $INST_N (none run -- --check)"
else
  echo "INSTALLERS: $INST_N discovered / $OK_N ok / $FAIL_N failed"
fi

# ---------------------------------------------------------------------------
# PASS 2 -- COMPLETENESS: every hook BODY must be wired by some installer.
# Bodies are the non-installer, non-test, non-helper scripts in git-hooks/.
# ---------------------------------------------------------------------------
echo
echo "COMPLETENESS -- does every hook body have an installer?"
BODY_N=0; ORPHAN_N=0; ORPHANS=""
for body in "$HOOKDIR"/*.sh; do
  [ -f "$body" ] || continue
  b="$(basename "$body")"
  case "$b" in
    install-*) continue ;;   # an installer, not a body
    test-*)    continue ;;   # a test
    _*)        continue ;;   # a sourced helper
  esac
  BODY_N=$((BODY_N + 1))
  # Is this body's filename referenced by ANY installer?
  if grep -l -- "$b" "$HOOKDIR"/install-*.sh >/dev/null 2>&1; then
    printf '  [wired]  %s\n' "$b"
  else
    ORPHAN_N=$((ORPHAN_N + 1)); ORPHANS="$ORPHANS $b"
    printf '  [ORPHAN] %-44s no installer references this body\n' "$b"
  fi
done

echo "----------------------------------------------------------------------"
echo "HOOK BODIES: $BODY_N total / $((BODY_N - ORPHAN_N)) wired / $ORPHAN_N ORPHANED"

# ---------------------------------------------------------------------------
# PASS 3 -- what is actually live in .git/hooks right now
# ---------------------------------------------------------------------------
echo
echo "LIVE IN .git/hooks (the only thing that actually enforces anything):"
live=0
for h in applypatch-msg commit-msg post-commit post-merge pre-commit pre-push pre-rebase; do
  if [ -f "$WS/.git/hooks/$h" ]; then
    live=$((live + 1))
    n="$(grep -c '^[^#[:space:]]' "$WS/.git/hooks/$h" 2>/dev/null || echo '?')"
    printf '  %-14s present (%s active line(s))\n' "$h" "$n"
  else
    printf '  %-14s ABSENT\n' "$h"
  fi
done
echo "  -> $live hook file(s) live"

echo "======================================================================"
if [ -n "$FAILED" ]; then
  echo "RESULT: FAILURES -->$FAILED"
  echo "        Re-run individually to see full output."
  exit 1
fi
if [ "$ORPHAN_N" -gt 0 ]; then
  echo "RESULT: installers ok, but $ORPHAN_N hook body/bodies have NO INSTALLER -->$ORPHANS"
  echo "        Those hooks can only ever exist on a machine where someone wired them"
  echo "        BY HAND -- i.e. they are silently absent on every other clone."
  echo "        Write .tools/git-hooks/install-<name>.sh for each. (LD-0343)"
  exit 2
fi
if [ "$CHECK_ONLY" -eq 1 ]; then
  echo "RESULT: OK -- $INST_N installers discovered (NOT run: --check) and all $BODY_N hook bodies are wired."
  echo "        --check does NOT prove the hooks are installed, only that the WIRING IS COMPLETE."
  echo "        Read the 'LIVE IN .git/hooks' block above for what is actually enforcing."
else
  echo "RESULT: OK -- all $INST_N installers ran and all $BODY_N hook bodies are wired."
fi
