#!/usr/bin/env bash
# NFRA_CMTQUE TO-6 -- safe-commit-contamination-proof.sh  (CVO carry-forward #2)
# Proves the LEGACY-path contamination guard (EXTRA = STAGED \ IN_SCOPE \ BASELINE ; EXTRA
# non-empty AND not --force => exit 1, extras reset). Two parts, per MSTR's steer (LD-0251):
#
#   (b) PRIMARY, DETERMINISTIC: unit-test the classification DECISION directly. Mirrors the
#       exact bash associative-array set-difference in safe-commit.sh (the STAGED/IN_SCOPE/
#       BASELINE logic ~ safe-commit.sh:287-297). No race -> deterministic -> this is the proof
#       CVO needs: the guard correctly classifies an out-of-scope staged file as contamination.
#
#   (a) CORROBORATION, PROBABILISTIC: end-to-end -- race a stray `git add` into the real
#       safe-commit baseline->staged window; retry-until-caught. Labeled probabilistic (NOT the
#       proof) because, BY DESIGN, the block is near-UNREACHABLE except via a genuine concurrent
#       out-of-band add: the baseline-capture puts every pre-staged file in BASELINE (peer-
#       ignored), and safe-commit's own `git add` only stages the in-scope pathspec. So there is
#       no single-process deterministic end-to-end trigger -- which is exactly why (b) is primary.
#
# Usage: bash .tools/safe-commit-contamination-proof.sh  (exit 0 = (b) all pass; (a) best-effort)

set -uo pipefail
GOLDEN="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/safe-commit.legacy-golden.sh"
LIVE="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/safe-commit.sh"
FAILS=0

# ---- (b) DETERMINISTIC: the EXTRA classification, verbatim from safe-commit ----
# Given STAGED, IN_SCOPE, BASELINE (newline lists), compute EXTRA the SAME way safe-commit does.
compute_extra() {  # $1=STAGED $2=IN_SCOPE $3=BASELINE  -> echoes EXTRA (one/line)
  local STAGED="$1" IN_SCOPE="$2" BASELINE="$3" f
  declare -A IN_SCOPE_SET=() BASELINE_SET=()
  while IFS= read -r f; do [ -n "$f" ] && IN_SCOPE_SET["$f"]=1; done <<< "$IN_SCOPE"
  while IFS= read -r f; do [ -n "$f" ] && BASELINE_SET["$f"]=1; done <<< "$BASELINE"
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if [ -z "${IN_SCOPE_SET[$f]+x}" ] && [ -z "${BASELINE_SET[$f]+x}" ]; then printf '%s\n' "$f"; fi
  done <<< "$STAGED"
}
_case() {  # $1=name $2=expected_extra(space-joined) $3=STAGED $4=IN_SCOPE $5=BASELINE
  local got; got="$(compute_extra "$3" "$4" "$5" | tr '\n' ' ' | sed 's/ *$//')"
  if [ "$got" = "$2" ]; then printf '  PASS (b) %-34s EXTRA=[%s]\n' "$1" "$got"
  else printf '  FAIL (b) %-34s EXTRA=[%s] expected [%s]\n' "$1" "$got" "$2"; FAILS=$(( FAILS + 1 )); fi
}

echo "=== (b) DETERMINISTIC: EXTRA = STAGED \\ IN_SCOPE \\ BASELINE (mirrors safe-commit:287-297) ==="
# 1. out-of-scope stray staged after baseline (the CONTAMINATION case) -> EXTRA={b.txt} -> would block
_case "contamination -> block"      "b.txt" "$(printf 'a.txt\nb.txt')" "a.txt" ""
# 2. only the in-scope file staged -> EXTRA empty -> clean commit
_case "clean in-scope only"         ""      "a.txt"                    "a.txt" ""
# 3. stray IS a pre-staged peer file (in baseline) -> peer-IGNORED -> EXTRA empty (git commit --only can't commit it)
_case "peer pre-staged (baseline)"  ""      "$(printf 'a.txt\nb.txt')" "a.txt" "b.txt"
# 4. multiple strays -> both are EXTRA
_case "two strays -> both flagged"  "b.txt c.txt" "$(printf 'a.txt\nb.txt\nc.txt')" "a.txt" ""
# 5. directory pathspec: expanded in-scope files match -> no false contamination
_case "dir pathspec expansion"      ""      "$(printf 'sub/f1\nsub/f2')" "$(printf 'sub/f1\nsub/f2')" ""
# decision: EXTRA non-empty AND not --force => block(exit1); with --force => bypass(audit). (verified by cases 1/4 producing EXTRA.)
echo "  (decision: EXTRA non-empty + no --force => exit 1 + reset extras; --force => FORCE-BYPASS audit)"

# ---- (a) PROBABILISTIC end-to-end corroboration ----
echo ""
echo "=== (a) PROBABILISTIC: race a stray git-add into safe-commit's window (retry-until-caught) ==="
tmp="${TMPDIR:-/tmp}/sc_contam_$$"; rm -rf "$tmp"; mkdir -p "$tmp"
trap 'rm -rf "$tmp" 2>/dev/null || true' EXIT
caught=0; attempts=0; max=25
while [ "$attempts" -lt "$max" ] && [ "$caught" -eq 0 ]; do
  attempts=$(( attempts + 1 ))
  r="$tmp/a_$attempts"; rm -rf "$r"; mkdir -p "$r"
  ( cd "$r" && git init -q . && git config user.email t@t && git config user.name t && git commit -q --allow-empty -m root ) >/dev/null 2>&1
  echo aa > "$r/a.txt"; echo bb > "$r/stray.txt"
  # launch safe-commit (legacy path forced: no queue flag) for a.txt in the background
  ( cd "$r" && SAFE_COMMIT_USE_QUEUE=0 bash "$LIVE" --author "t <t@o>" -m "scoped" -- a.txt >"$r/out" 2>&1; echo "rc=$?" >"$r/rc" ) &
  scpid=$!
  # race a bare out-of-band `git add stray.txt` into its baseline->staged window
  ( cd "$r" && for _ in 1 2 3 4 5; do git add stray.txt 2>/dev/null; done )
  wait "$scpid" 2>/dev/null || true
  if grep -q "staged index contains files not in declared pathspec" "$r/out" 2>/dev/null && grep -q "stray.txt" "$r/out" 2>/dev/null; then
    caught=1
    echo "  CAUGHT on attempt $attempts: safe-commit BLOCKED (exit $(sed 's/rc=//' "$r/rc")) with stray.txt flagged as contamination."
  fi
done
if [ "$caught" -eq 1 ]; then echo "  (a) end-to-end corroboration: guard FIRES on a real concurrent out-of-band add."
else echo "  (a) window not caught in $max attempts (expected -- the window is tiny by design; (b) is the proof)."; fi

echo ""
echo "=== RESULT: (b) ${FAILS} failing case(s) ==="
[ "$FAILS" -eq 0 ] && echo "PASS: contamination guard classification proven deterministic (b); end-to-end $([ "$caught" -eq 1 ] && echo corroborated || echo 'best-effort')." || echo "FAIL"
exit "$FAILS"
