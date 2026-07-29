#!/usr/bin/env bash
# verify-device.sh -- prove THIS DEVICE's shell/git infrastructure actually works.
#
#   bash .tools/verify-device.sh          # verify; exit 1 on any FAIL
#   bash .tools/verify-device.sh --quiet  # only FAIL/UNVERIFIED lines + the summary
#
# RUN IT: on every fresh clone, after any reboot, and after provisioning anything.
#
# ============================================================================
# WHY THIS EXISTS -- it is not a nicety, it is the lesson of 2026-07-28/29
# ============================================================================
# A second device came online and every guarantee this fabric describes as
# "gated" turned out to be per-clone and UNVERIFIED. Measured that night:
#   * 8 PreToolUse hooks -- including never-rules-gate, which CLAUDE.md calls
#     "the only detector" for a silent rebase on a shared branch -- were
#     COMPLETELY INERT at site Z because a gitignored jq.exe never propagated.
#     `git rebase origin/CLOUD` passed SILENTLY on a device committing to CLOUD.
#   * A reboot killed ALL 186 ~/bin forwarders at once; the comp rail was dead
#     at the entrypoint and safe-commit's own hooks printed
#     "No such file or directory" and LET COMMITS THROUGH.
#   * The startup probe reported "93 of 93 comp-tools resolve bare". ZERO ran.
#
# >> THE UNIFYING DEFECT: EVERY ONE OF THOSE CHECKS TESTED A TEXTUAL PROXY
#    (a name resolves, a file exists, a config says so) INSTEAD OF THE
#    SEMANTIC FACT (the thing RUNS, the gate DENIES). A probe aimed at a proxy
#    reads healthy precisely when the breakage is total and single-caused --
#    all N resolve BECAUSE the provisioner ran, all N are dead BECAUSE they
#    share one broken prefix. THE CLEANER THE PASS, THE MORE COMPLETE THE
#    FAILURE. <<
#
# RULES THIS FILE OBEYS, because it is the thing that catches the others:
#   1. EXERCISE, never resolve. Run the tool; grep its OUTPUT.
#   2. NEVER score on rc alone -- harness rc is corrupted (LD-0340), and some
#      healthy tools exit nonzero (comp-which's rc tracks match/no-match).
#   3. PRINT THE DENOMINATOR. Never a bare boolean.
#   4. Where a gate is under test, prove it can DENY, not just that it ran.
#   5. THREE OUTCOMES, never two: PASS / FAIL / UNVERIFIABLE. Collapsing
#      "cannot tell" into "fine" is how every one of the above survived.
#   6. Derive every path at run time. No device literal, ever.
# ============================================================================
set -u
QUIET=0; [ "${1:-}" = "--quiet" ] && QUIET=1

WS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$WS" || { echo "verify-device: cannot cd to repo root"; exit 1; }

P=0; F=0; U=0; FAILS=""
say(){ [ "$QUIET" -eq 1 ] || printf '%s\n' "$*"; }
ok(){   P=$((P+1)); say "  [PASS]  $1"; [ -n "${2:-}" ] && say "          $2"; }
bad(){  F=$((F+1)); printf '  [FAIL]  %s\n' "$1"; [ -n "${2:-}" ] && printf '          %s\n' "$2"; [ -n "${3:-}" ] && printf '          FIX: %s\n' "$3"; FAILS="$FAILS
  - $1"; }
unv(){  U=$((U+1)); printf '  [UNVER] %s\n' "$1"; [ -n "${2:-}" ] && printf '          %s\n' "$2"; }

say "=============================================================="
say " verify-device -- $WS"
say " EXERCISES the infrastructure. A passing NAME is not a passing TOOL."
say "=============================================================="

# ---------------------------------------------------------------- 1. jq
say ""; say "-- 1. jq (8 hooks fail-closed without it) --------------------"
JQ=""
[ -x "$WS/.tools/jq.exe" ] && JQ="$WS/.tools/jq.exe"
[ -z "$JQ" ] && command -v jq >/dev/null 2>&1 && JQ="jq"
if [ -n "$JQ" ] && printf '{"a":1}' | "$JQ" -r '.a' 2>/dev/null | grep -q '^1$'; then
  ok "jq present AND parses" "$JQ"
else
  bad "jq missing or broken" "8 hooks depend on it; they now FAIL CLOSED and will refuse your commits" \
      "git checkout .tools/jq.exe   (it is tracked)   or install jq"
fi

# ------------------------------------------------------- 2. forwarders
say ""; say "-- 2. ~/bin forwarders: RESOLVE *and* EXECUTE ----------------"
TOT=0; RES=0
for t in "$WS"/.tools/comp-*; do
  b="$(basename "$t")"; case "$b" in *.py|*.sh) continue;; esac
  TOT=$((TOT+1)); command -v "$b" >/dev/null 2>&1 && RES=$((RES+1))
done
say "  denominator: $RES of $TOT comp-tools RESOLVE by name"
if command -v comp-which >/dev/null 2>&1; then
  if comp-which "how do I grep the repo" 2>&1 | grep -q "comp-which --"; then
    ok "a forwarder EXECUTES" "comp-which produced its own banner"
  else
    bad "forwarders RESOLVE BUT DO NOT RUN" \
        "This is the 2026-07-29 failure exactly: names resolve, targets are gone. \`command -v\` cannot see it." \
        "bash .tools/provision-path-shims.sh"
  fi
else
  bad "comp-which does not resolve" "the Rule 21 comp-rail entrypoint is absent" "bash .tools/provision-path-shims.sh"
fi
if command -v comp-which >/dev/null 2>&1; then
  fw="$(command -v comp-which)"
  if grep -q '_alt=' "$fw" 2>/dev/null; then
    ok "forwarder reboot-fallback present" "tries both /c and /cygdrive/c"
  else
    bad "forwarder has NO prefix fallback" \
        "It bakes one MSYS flavor. If that mount goes (reboot), EVERY forwarder dies at once -- 186 did at site Z." \
        "bash .tools/provision-path-shims.sh"
  fi
fi

# ------------------------------------------------------------ 3. hooks
say ""; say "-- 3. git hooks: INSTALLED, and able to DENY ------------------"
LIVE=0
for h in pre-commit post-commit pre-push commit-msg; do [ -f "$WS/.git/hooks/$h" ] && LIVE=$((LIVE+1)); done
say "  denominator: $LIVE of 4 core hook files present in .git/hooks/"
[ "$LIVE" -ge 3 ] && ok "git hooks installed" "$LIVE/4" \
  || bad "git hooks missing" "$LIVE/4 -- a fresh clone gets ZERO; git tracks nothing under .git/" "bash .tools/install-all-git-hooks.sh"

NRG="$WS/.tools/hooks/never-rules-gate.sh"
if [ -f "$NRG" ]; then
  out="$(printf '%s' '{"tool_name":"Bash","tool_input":{"command":"git rebase origin/CLOUD"}}' | bash "$NRG" 2>&1)"
  case "$out" in
    *'"deny"'*) ok "never-rules-gate DENIES a rebase" "the only detector for a silent history rewrite" ;;
    *BLOCKED*)  bad "never-rules-gate cannot run" "it fails closed (correct) but is not protecting you" "install jq -- see check 1" ;;
    *)          bad "never-rules-gate did NOT deny a rebase on a shared branch" \
                    "It returned no deny verdict. A silent non-conflicting rebase is indistinguishable from an honest merge." \
                    "inspect .tools/hooks/never-rules-gate.sh and settings.json wiring" ;;
  esac
else
  bad "never-rules-gate.sh absent" "" "restore from the repo"
fi

if [ -f "$WS/.tools/install-all-git-hooks.sh" ]; then
  o="$(bash "$WS/.tools/install-all-git-hooks.sh" --check 2>&1)"
  case "$o" in
    *"0 ORPHANED"*) ok "hook bodies all wired" "$(printf '%s' "$o" | grep -o 'HOOK BODIES: .*' | head -1)" ;;
    *) bad "hook body has NO installer" "$(printf '%s' "$o" | grep -o '[0-9]* ORPHANED' | head -1) -- can only exist where someone wired it BY HAND" \
           "write .tools/git-hooks/install-<name>.sh for each orphan" ;;
  esac
fi

# ---------------------------------------------------------- 4. post-commit order
say ""; say "-- 4. post-commit: every invocation ABOVE 'exit 0' -----------"
PC="$WS/.git/hooks/post-commit"
if [ -f "$PC" ] && grep -q '^exit 0[[:space:]]*$' "$PC"; then
  L="$(grep -n '^exit 0[[:space:]]*$' "$PC" | tail -1 | cut -d: -f1)"
  T="$(grep -c '^_ws=' "$PC")"; A="$(awk -v l="$L" 'NR<l && /^_ws=/' "$PC" | wc -l | tr -d ' ')"
  [ "$A" = "$T" ] && ok "post-commit ordering" "$A/$T above exit 0" \
    || bad "post-commit lines BELOW 'exit 0'" "$A/$T above -- the rest NEVER RUN while printing nothing" \
           "move them above exit 0 (see install-closeout-comp-state.sh)"
else
  [ -f "$PC" ] && ok "post-commit ordering" "no trailing exit 0" || unv "post-commit" "hook absent"
fi

# ------------------------------------------------------------- 5. fstab
say ""; say "-- 5. fstab / mount (THREE outcomes, not two) ----------------"
MT="$(mount 2>&1)"; ERR="$(printf '%s' "$MT" | grep -i 'invalid fstab option' || true)"
CL="$(printf '%s' "$MT" | grep ' /c ' || true)"
if [ -n "$ERR" ]; then
  bad "fstab is PARSED and REJECTED" "$ERR" "fix the named option -- ONE invalid option voids the WHOLE line, so /c never mounts"
elif printf '%s' "$CL" | grep -q 'noumount\|posix=0'; then
  ok "/c mounted from fstab" "$CL"
elif [ -n "$CL" ]; then
  unv "/c mounted, but NOT from fstab" "[$CL] -- these are volatile 'mount -f' flags; it will VANISH on reboot. LD-0340 open."
else
  unv "/c absent, no parse error in this shell" "AMBIGUOUS: unread fstab and rejected fstab look identical from the mount table alone. Re-check from a fresh table (reboot)."
fi

# --------------------------------------------------------------- 6. aws
say ""; say "-- 6. aws shim (executes, not just resolves) -----------------"
if command -v aws >/dev/null 2>&1; then
  a="$(aws sts get-caller-identity --query Arn --output text 2>&1 | tr -d '\r')"
  case "$a" in
    arn:aws:*) ok "aws shim executes" "$a" ;;
    *SyntaxError*|*Traceback*) bad "aws shim mis-dispatches" "$(printf '%s' "$a" | head -1)" "the shim must dispatch on MAGIC BYTES (MZ), not the .exe suffix" ;;
    *nable*locate*credential*|*Unable*) unv "aws resolves; NO CREDENTIALS on this device" "shim is fine; ~/.aws is not configured" ;;
    *) unv "aws returned something unexpected" "$(printf '%s' "$a" | head -1 | cut -c1-70)" ;;
  esac
else
  bad "aws does not resolve" "" "bash .tools/provision-path-shims.sh"
fi

# -------------------------------------------------------- 7. gitattributes
say ""; say "-- 7. append-only log merge driver ---------------------------"
m="$(git check-attr merge -- org/compiler-tools-log.md 2>/dev/null)"
case "$m" in
  *union*) if git check-attr merge -- README.md 2>/dev/null | grep -q unspecified; then
             ok "merge=union live AND scoped" "README.md unaffected"
           else bad "merge=union LEAKED to a glob" "union silently keeps a STALE line beside its correction" "scope it to the one path"; fi ;;
  *) unv "merge=union not set" "concurrent appends to the tools log will 3-way conflict; hand-resolution corrupted it 4x on 2026-07-29" ;;
esac

# ------------------------------------------------------------ 8. launchers
say ""; say "-- 8. launchers derive their own root -----------------------"
for f in .tools/ajb.ps1 .tools/spawn-agent.ps1; do
  if [ -f "$WS/$f" ]; then
    n="$(grep -c 'Users\\\\[A-Za-z]*\\\\Desktop\|Users/[A-Za-z]*/Desktop' "$WS/$f" 2>/dev/null || echo 0)"
    c="$(grep -c '^#' "$WS/$f" 2>/dev/null || echo 0)"
    if grep -qE 'PSScriptRoot|OPAL_WS_ROOT' "$WS/$f"; then ok "$f derives its root" "PSScriptRoot / OPAL_WS_ROOT present"
    else bad "$f has NO run-time root derivation" "it will fail on any clone at a different path" "derive from \$PSScriptRoot"; fi
  fi
done

say ""
say "=============================================================="
printf ' PASS=%d  FAIL=%d  UNVERIFIABLE=%d\n' "$P" "$F" "$U"
if [ "$F" -gt 0 ]; then
  printf ' RESULT: FAIL -- this device is NOT fully protected.%s\n' "$FAILS"
  say "=============================================================="
  exit 1
fi
if [ "$U" -gt 0 ]; then
  printf ' RESULT: PASS with %d UNVERIFIABLE -- read them. "Cannot tell" is NOT "fine".\n' "$U"
else
  printf ' RESULT: PASS -- every check EXERCISED, none inferred.\n'
fi
say "=============================================================="
exit 0
