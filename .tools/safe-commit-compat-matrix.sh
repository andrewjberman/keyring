#!/usr/bin/env bash
# NFRA_CMTQUE TO-2 -- safe-commit compat matrix.
# Proves safe-commit.v2.sh is interface-compatible with the current safe-commit.sh:
#   PHASE A (LEGACY equivalence): v2 with the queue flag OFF must match the CURRENT
#           safe-commit.sh byte-for-byte on {exit code, commit-landed, author, subject}
#           across every arg-shape (the AC2 matrix). This is what makes v2 safe to LAND
#           flag-off (zero behavior change for the ~1338 callers).
#   PHASE B (QUEUE path): v2 with the flag ON + a live worker must produce the SAME
#           {exit code, commit-landed} verdict as legacy for the same inputs.
#
# Each case runs in its OWN fresh temp repo (identical setup per binary) so the
# comparison is clean. git-commit-free where possible; bounded.
#
# Usage: bash .tools/safe-commit-compat-matrix.sh   (exit 0 = all cases matched)

set -uo pipefail

# CUR = the frozen pre-queue golden (byte-exact reference of the behavior we must preserve);
# V2  = the LANDED safe-commit.sh (queue-client; flag-off must == golden). Durable regression:
# re-run any time to prove the landed client's legacy path never drifts from the golden.
CUR="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/safe-commit.legacy-golden.sh"
V2="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/safe-commit.sh"
GATE_LIB_OK=1
AUTHOR='0.7.0_AE_CloudOps~B <0.7.0_AE_CloudOps@opal.agent>'
FAILS=0
PASSES=0
TMPROOT="${TMPDIR:-/tmp}/sccompat_$$"
mkdir -p "$TMPROOT"

# make a fresh repo with a root commit + an isolated audit log; echo its path
mkrepo() {
  local d="$TMPROOT/repo_$1"
  rm -rf "$d"; mkdir -p "$d"
  ( cd "$d" && git init -q . && git config user.email w@o && git config user.name w \
      && git commit -q --allow-empty -m root ) >/dev/null 2>&1
  echo "$d"
}

# run a binary in $1 with args ${@:3}; $2 = extra env (e.g. "SAFE_COMMIT_USE_QUEUE=1").
# echoes: "<exit>|<landed yes/no>|<author>|<subject>"
run_bin() {
  local dir="$1" env="$2" bin="$3"; shift 3
  local before after rc landed author subject
  before="$(cd "$dir" && git rev-parse HEAD 2>/dev/null || echo NONE)"
  ( cd "$dir" && env $env SAFE_COMMIT_AUDIT_LOG="$dir/audit.log" bash "$bin" "$@" ) \
    >/dev/null 2>&1 </dev/null
  rc=$?
  after="$(cd "$dir" && git rev-parse HEAD 2>/dev/null || echo NONE)"
  landed=no; [ "$before" != "$after" ] && landed=yes
  author="$(cd "$dir" && git log -1 --format='%an <%ae>' 2>/dev/null || echo -)"
  subject="$(cd "$dir" && git log -1 --format='%s' 2>/dev/null || echo -)"
  [ "$landed" = no ] && { author="-"; subject="-"; }
  echo "${rc}|${landed}|${author}|${subject}"
}

# compare current vs v2-flag-off for one case. setup_fn stages the working tree.
# args after the 2 names are passed to BOTH binaries.
cmp_legacy() {
  local name="$1" setup_fn="$2"; shift 2
  local da db ra rb
  da="$(mkrepo "a_${name}")"; db="$(mkrepo "b_${name}")"
  "$setup_fn" "$da"; "$setup_fn" "$db"
  ra="$(run_bin "$da" "" "$CUR" "$@")"
  rb="$(run_bin "$db" "" "$V2" "$@")"
  if [ "$ra" = "$rb" ]; then
    PASSES=$((PASSES + 1)); printf '  PASS  %-28s cur=[%s] == v2=[%s]\n' "$name" "$ra" "$rb"
  else
    FAILS=$((FAILS + 1)); printf '  FAIL  %-28s cur=[%s] != v2=[%s]\n' "$name" "$ra" "$rb"
  fi
}

# ---- setup functions (each stages the working tree of $1) ----
s_basic()   { echo hi > "$1/a.txt"; }
s_parens()  { echo hi > "$1/a.txt"; }
s_dir()     { mkdir -p "$1/sub"; echo x > "$1/sub/f1.json"; echo y > "$1/sub/f2.json"; }
s_gitign()  { printf '.tools/\n' > "$1/.gitignore"; ( cd "$1" && git add -f .gitignore >/dev/null 2>&1 ); mkdir -p "$1/.tools"; echo t > "$1/.tools/newtool.sh"; }
s_sens()    { printf 'evil/\n' > "$1/.gitignore"; ( cd "$1" && git add -f .gitignore >/dev/null 2>&1 ); mkdir -p "$1/evil"; printf 'AWS_SECRET_ACCESS_KEY=x\n' > "$1/evil/.env"; }
s_contam()  { echo hi > "$1/a.txt"; echo stray > "$1/stray.txt"; ( cd "$1" && git add stray.txt >/dev/null 2>&1 ); }  # peer-staged extra
s_empty()   { : ; }
s_nofile()  { : ; }
s_nothing() { : ; }  # nothing staged/changed -> git "nothing to commit"

echo "=== PHASE A: LEGACY equivalence (current safe-commit.sh vs safe-commit.v2.sh flag-off) ==="
cmp_legacy "basic-commit"        s_basic   --author "$AUTHOR" -m "basic commit"          -- a.txt
cmp_legacy "parens-in-message"   s_parens  --author "$AUTHOR" -m 'fn() [pure] $V `c`'    -- a.txt
cmp_legacy "directory-pathspec"  s_dir     --author "$AUTHOR" -m "dir commit"            -- sub/
cmp_legacy "newfile-gitignored"  s_gitign  --author "$AUTHOR" -m "new tool"              -- .tools/newtool.sh
cmp_legacy "sensitive-block"     s_sens    --author "$AUTHOR" -m "leak"                  -- evil/.env
cmp_legacy "contamination-abort" s_contam  --author "$AUTHOR" -m "scoped"                -- a.txt
cmp_legacy "contamination-force" s_contam  --force --author "$AUTHOR" -m "scoped"        -- a.txt
cmp_legacy "no-doubledash"       s_nofile  --author "$AUTHOR" -m "x"
cmp_legacy "help-flag"           s_empty   --help
cmp_legacy "nothing-to-commit"   s_nothing --author "$AUTHOR" -m "empty"                 -- nonexistent.txt

echo ""
echo "=== PHASE B: QUEUE path (v2 flag-on + live worker) matches the legacy verdict ==="
WORKER="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/commit-worker.sh"
# For a shape: get the legacy verdict (flag-off) in one repo, then run v2 flag-on with a
# LIVE daemon in an identical repo; the {exit|landed} verdict must match.
phase_b_case() {
  local name="$1" setup_fn="$2"; shift 2
  local dl dq legacy queue wpid c
  # legacy verdict (flag-off)
  dl="$(mkrepo "bl_${name}")"; "$setup_fn" "$dl"
  legacy="$(run_bin "$dl" "" "$V2" "$@")"
  legacy="$(echo "$legacy" | cut -d'|' -f1-2)"   # exit|landed
  # queue path: start a persistent daemon for dq, confirm it's up, run v2 flag-on
  dq="$(mkrepo "bq_${name}")"; "$setup_fn" "$dq"
  ( cd "$dq" && bash "$WORKER" --daemon </dev/null >/dev/null 2>&1 ) &
  wpid=$!
  c=0
  while [ ! -f "$dq/.git/commit-queue/worker.pid" ] && [ "$c" -lt 12 ]; do sleep 1; c=$((c + 1)); done
  queue="$(run_bin "$dq" "SAFE_COMMIT_USE_QUEUE=1" "$V2" "$@")"
  queue="$(echo "$queue" | cut -d'|' -f1-2)"
  kill "$wpid" 2>/dev/null || true; wait "$wpid" 2>/dev/null || true
  if [ "$legacy" = "$queue" ]; then
    PASSES=$((PASSES + 1)); printf '  PASS  %-28s legacy=[%s] == queue=[%s]\n' "$name" "$legacy" "$queue"
  else
    FAILS=$((FAILS + 1)); printf '  FAIL  %-28s legacy=[%s] != queue=[%s]\n' "$name" "$legacy" "$queue"
  fi
}
phase_b_case "queue-basic-commit"  s_basic --author "$AUTHOR" -m "basic via queue" -- a.txt
phase_b_case "queue-sensitive"     s_sens  --author "$AUTHOR" -m "leak via queue"  -- evil/.env

rm -rf "$TMPROOT" 2>/dev/null || true
echo ""
echo "=== RESULT: ${PASSES} passed, ${FAILS} failed ==="
[ "$FAILS" -eq 0 ] && echo "PASS: safe-commit v2 is interface-compatible (legacy byte-for-byte + queue-equivalent)."
exit "$FAILS"
