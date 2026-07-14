#!/usr/bin/env bash
# test-safe-commit-deletion-staging.sh -- the pure-deletion + pycache-exclusion suite
# (safe-commit-pure-deletion-staging TO, CTO fix shape 081918Z + COO AMENDMENT-1).
#
# NEW FILE by design: the compat matrix (safe-commit-compat-matrix.sh) asserts
# golden-EQUIVALENCE, and this fix DELIBERATELY diverges from golden for deletion
# shapes -- so deletion classes live here, and deletion-free behavior stays pinned
# by the untouched golden matrix.
#
# Classes (TO + AMENDMENT-1):
#   (a) pure deletion  a1 unstaged (rm), a2 already-staged (git rm) -> both commit
#   (b) mixed add+delete in one commit
#   (c) untracked+missing pathspec entry -> still FAILS loud (caller typo)
#   (d) staged RENAME (git mv), pathspec naming both sides -> both sides commit
#   (e) pycache: dir pathspec sweeping __pycache__/*.pyc -> commits WITHOUT them,
#       SKIP line printed; positive control SEPARATELY (same shape, legit .py lands);
#       MUTANT kill: a filter-neutered lib copy stages the .pyc and the class-(e)
#       assertion FAILS on it (an exclusion that cannot fail is not a control).
#
# Each case runs in its OWN fresh temp repo against the REAL wrapper. Git Bash
# 3.6.7 default utilities only (Rule 16).

set -uo pipefail

WS="/c/Users/AndrewBerman/Desktop/ajb_workspace"
SC="$WS/.tools/safe-commit.sh"
LIB="$WS/.tools/commit_gate_lib.sh"
AUTHOR='0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>'
TMPROOT="${TMPDIR:-/tmp}/scdel_$$"
mkdir -p "$TMPROOT"
PASSES=0
FAILS=0

say()  { printf '%s\n' "$*"; }
pass() { PASSES=$((PASSES+1)); say "  PASS  $1"; }
fail() { FAILS=$((FAILS+1));  say "  FAIL  $1"; }

mkrepo() {
  local d="$TMPROOT/repo_$1"
  rm -rf "$d"; mkdir -p "$d"
  ( cd "$d" && git init -q . && git config user.email w@o && git config user.name w \
      && git commit -q --allow-empty -m root ) >/dev/null 2>&1
  echo "$d"
}

# run_wrapper <repo> <msg> <path>... -> globals RC, ERR (stderr), LANDED (yes/no)
run_wrapper() {
  local d="$1" msg="$2"; shift 2
  local before after
  before="$(cd "$d" && git rev-parse HEAD)"
  ERR="$( cd "$d" && SAFE_COMMIT_AUDIT_LOG="$d/audit.log" bash "$SC" --author "$AUTHOR" -m "$msg" -- "$@" </dev/null 2>&1 >/dev/null )"
  RC=$?
  after="$(cd "$d" && git rev-parse HEAD)"
  LANDED=no; [ "$before" != "$after" ] && LANDED=yes
}

in_head()  { ( cd "$1" && git ls-tree -r --name-only HEAD ) | grep -qxF "$2"; }

say "== (a) pure deletion =="
D="$(mkrepo a1)"; ( cd "$D" && echo x > f.txt && git add -A . && git commit -qm add ) >/dev/null 2>&1
( cd "$D" && rm f.txt )
run_wrapper "$D" "del f unstaged" f.txt
if [ "$RC" -eq 0 ] && [ "$LANDED" = yes ] && ! in_head "$D" f.txt; then pass "a1 unstaged deletion commits"; else fail "a1 unstaged deletion (rc=$RC landed=$LANDED)"; fi

D="$(mkrepo a2)"; ( cd "$D" && echo x > f.txt && git add -A . && git commit -qm add ) >/dev/null 2>&1
( cd "$D" && git rm -q f.txt )
run_wrapper "$D" "del f staged" f.txt
if [ "$RC" -eq 0 ] && [ "$LANDED" = yes ] && ! in_head "$D" f.txt; then pass "a2 already-staged deletion commits (the rc=128 incident shape)"; else fail "a2 staged deletion (rc=$RC landed=$LANDED err=${ERR:0:160})"; fi

say "== (b) mixed add+delete in one commit =="
D="$(mkrepo b)"; ( cd "$D" && echo x > del.txt && git add -A . && git commit -qm add ) >/dev/null 2>&1
( cd "$D" && git rm -q del.txt && echo y > new.txt )
run_wrapper "$D" "mixed" del.txt new.txt
if [ "$RC" -eq 0 ] && [ "$LANDED" = yes ] && ! in_head "$D" del.txt && in_head "$D" new.txt; then pass "b mixed add+delete"; else fail "b mixed (rc=$RC landed=$LANDED)"; fi

say "== (c) untracked+missing still fails loud =="
D="$(mkrepo c)"
run_wrapper "$D" "ghost" ghost.txt
if [ "$RC" -ne 0 ] && [ "$LANDED" = no ]; then pass "c untracked+missing refused (rc=$RC, no commit)"; else fail "c ghost (rc=$RC landed=$LANDED)"; fi

say "== (d) staged rename, pathspec both sides =="
D="$(mkrepo d)"; ( cd "$D" && echo x > old.txt && git add -A . && git commit -qm add ) >/dev/null 2>&1
( cd "$D" && git mv old.txt new.txt )
run_wrapper "$D" "rename" old.txt new.txt
if [ "$RC" -eq 0 ] && [ "$LANDED" = yes ] && ! in_head "$D" old.txt && in_head "$D" new.txt; then pass "d staged rename commits both sides"; else fail "d rename (rc=$RC landed=$LANDED err=${ERR:0:160})"; fi

say "== (e) pycache exclusion =="
# Payloads are .txt: the universal commit-gate's ruff step is WORKSPACE-anchored and
# E902s on any .py inside a scratch temp repo (pre-existing wrapper behavior, not
# this TO's subject). The gate-creates-the-.pyc-mid-run aspect is exercised by the
# phase-3-amendment REPLAYS in the real repo; here the suite pins the sweep
# mechanics (staging filter + SKIP loudness + commit-time belt).
D="$(mkrepo e)"; ( cd "$D" && mkdir -p pkg/__pycache__ \
  && printf 'payload\n' > pkg/data.txt \
  && printf 'fakebytecode' > pkg/__pycache__/mod.cpython-312.pyc \
  && printf 'fakebytecode' > pkg/stray.pyc )
run_wrapper "$D" "pkg with pycache" pkg/
E_TREE="$(cd "$D" && git ls-tree -r --name-only HEAD)"
if [ "$RC" -eq 0 ] && [ "$LANDED" = yes ] \
   && printf '%s\n' "$E_TREE" | grep -qxF pkg/data.txt \
   && ! printf '%s\n' "$E_TREE" | grep -qE '\.pyc$|__pycache__'; then
  pass "e1 dir pathspec commits payload WITHOUT pycache artifacts"
else fail "e1 pycache excluded (rc=$RC landed=$LANDED tree=[$E_TREE])"; fi
if printf '%s\n' "$ERR" | grep -q 'SKIP: pycache-artifact'; then
  pass "e2 SKIP line printed per artifact (never silent)"
else fail "e2 no SKIP line in stderr: ${ERR:0:200}"; fi

# positive control, SEPARATE run in a SEPARATE repo (same pathspec shape, no pycache).
D="$(mkrepo e_pos)"; ( cd "$D" && mkdir -p pkg && printf 'clean\n' > pkg/real.txt )
run_wrapper "$D" "pkg clean" pkg/
if [ "$RC" -eq 0 ] && in_head "$D" pkg/real.txt; then pass "e3 positive control: same shape, legit payload lands"; else fail "e3 positive control (rc=$RC)"; fi

# e6: the COMMIT-TIME BELT, unit level -- a .pyc created AFTER staging (the
# mid-gate py_compile window) must still be excluded by cg_commit_exclude_pathspec.
D="$(mkrepo e_belt)"; ( cd "$D" && mkdir -p pkg && printf 'belt\n' > pkg/data.txt )
BELT_TREE="$( cd "$D" && bash -c "
  source '$LIB'
  cg_stage_pathspec pkg/ >/dev/null 2>&1
  mkdir -p pkg/__pycache__ && printf 'latebytecode' > pkg/__pycache__/late.cpython-312.pyc
  ex=()
  while IFS= read -r x; do ex+=(\"\$x\"); done < <(cg_commit_exclude_pathspec)
  git -c gc.auto=0 commit -q --only -m belt -- pkg/ \"\${ex[@]}\" </dev/null >/dev/null 2>&1
  git ls-tree -r --name-only HEAD" )"
if printf '%s\n' "$BELT_TREE" | grep -qxF pkg/data.txt \
   && ! printf '%s\n' "$BELT_TREE" | grep -qE '\.pyc$'; then
  pass "e6 commit-time belt: post-staging .pyc excluded from the committed tree"
else fail "e6 belt (tree=[$BELT_TREE])"; fi

say "== (e) MUTANT kill (unit level, mutated COPY of the lib -- live file untouched) =="
MUT="$TMPROOT/commit_gate_lib.mutant.sh"
# Neuter the filter: point the pycache regex at a token that can never match.
sed 's|^CG_PYCACHE_RE=.*|CG_PYCACHE_RE="A_PATTERN_THAT_NEVER_MATCHES_ANYTHING_9f3"|' "$LIB" > "$MUT"
D="$(mkrepo e_mut)"; ( cd "$D" && mkdir -p pkg/__pycache__ \
  && printf 'Z = 3\n' > pkg/mod.py \
  && printf 'fakebytecode' > pkg/__pycache__/mod.cpython-312.pyc )
MUT_STAGED="$( cd "$D" && bash -c "source '$MUT'; cg_stage_pathspec pkg/ >/dev/null 2>&1; git diff --cached --name-only" )"
if printf '%s\n' "$MUT_STAGED" | grep -qE '\.pyc$'; then
  pass "e4 MUTANT KILL: neutered filter stages the .pyc -> the class-(e) assertion catches it (the control can fail)"
else fail "e4 mutant did not stage the .pyc -- the exclusion cannot fail = not a control (staged=[$MUT_STAGED])"; fi
# and the REAL lib on the same shape must NOT stage it (paired half of the kill):
D="$(mkrepo e_real)"; ( cd "$D" && mkdir -p pkg/__pycache__ \
  && printf 'W = 4\n' > pkg/mod.py \
  && printf 'fakebytecode' > pkg/__pycache__/mod.cpython-312.pyc )
REAL_STAGED="$( cd "$D" && bash -c "source '$LIB'; cg_stage_pathspec pkg/ >/dev/null 2>&1; git diff --cached --name-only" )"
if ! printf '%s\n' "$REAL_STAGED" | grep -qE '\.pyc$'; then
  pass "e5 real lib on the identical shape stages zero .pyc"
else fail "e5 real lib staged a .pyc: [$REAL_STAGED]"; fi

rm -rf "$TMPROOT" 2>/dev/null || true
say ""
say "================================================================"
say "PASS: $PASSES   FAIL: $FAILS"
[ "$FAILS" -eq 0 ] && say "ALL CHECKS PASS -- deletion staging + pycache exclusion." || say "SUITE RED."
[ "$FAILS" -eq 0 ]
