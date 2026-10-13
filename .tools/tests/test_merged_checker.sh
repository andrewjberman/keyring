#!/usr/bin/env bash
# test_merged_checker.sh -- NFRA_CTLPLN.TO-CT-ab-13: the project-tree check at a merge runs the MERGE's checker.
#
# Arms, each in a temporary git repository (mktemp -d, removed on exit); the real worktree is only READ:
#   1  a merge whose staged missions-tree-index.py is the CURRENT one, with the OLD checker in the working tree and the
#      merged gate (FABRIC_ENUM = tuple(_fabric_values())): helper's copy of the merge's checker passes the check.
#   2  CONTROL: the same merge checked with the working-tree OLD checker (the pre-fix call) is REFUSED with ValueError.
#      The arm passes when the control refuses; it is there so arm 1 cannot pass by accident.
#   3  a merge that does not carry the file: the helper falls back to the working-tree path and says FALLBACK on stderr.
#   4  the helper's copy exists during the grade and is gone after the private git dir is removed.
#
# Git Bash 3.6.7 default utilities only. Final line: MERGED-CHECKER-TEST cases=<k>/<n> ok=<True|False>
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"      # the .tools directory of the worktree
REAL="$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null)" || { echo "test: not inside a git worktree" >&2; exit 2; }
OLD_REF="a71a0b4f68"                                          # the checker before CT-ab-8
N=4; K=0
. "$HERE/merged-checker.sh" || { echo "test: cannot source merged-checker.sh" >&2; exit 2; }

T="$(mktemp -d)" || { echo "test: cannot make a temporary directory" >&2; exit 2; }
trap 'rm -rf "$T"' EXIT

pass() { K=$((K + 1)); echo "  PASS  $1"; }
fail() { echo "  FAIL  $1"; }
final() { echo "MERGED-CHECKER-TEST cases=${K}/${N} ok=$([ "$K" -eq "$N" ] && echo True || echo False)"; [ "$K" -eq "$N" ]; }

# The OLD and CURRENT checkers, read from git (never from a file the arms could edit).
git -C "$REAL" show "${OLD_REF}:.tools/missions-tree-index.py" > "$T/old.py" || { echo "test: cannot read ${OLD_REF}:.tools/missions-tree-index.py" >&2; final; exit 1; }
cp "$HERE/missions-tree-index.py" "$T/cur.py" || { echo "test: cannot read the current checker" >&2; final; exit 1; }
[ -s "$T/old.py" ] && [ -s "$T/cur.py" ] || { echo "test: a checker copy is empty" >&2; final; exit 1; }

# mk_tree <repo> <checker-file-or-empty>: the MERGE's tree, staged in <repo>'s index. The inputs are the real
# contract, the completion schema, the registers and the merged gate; the tree itself holds no projects.
mk_tree() {
  local repo="$1" chk="$2"
  mkdir -p "$repo/.tools" "$repo/org/standards" "$repo/org/missions" "$repo/org/devices" "$repo/lib" || return 1
  git init -q "$repo" || return 1
  cp "$REAL/org/standards/PROJECT_TREE.contract.json" "$REAL/org/standards/COMPLETION_REPORT.schema.json" "$repo/org/standards/" || return 1
  cp "$REAL/org/missions/DIRECTIVES.yaml" "$REAL/org/missions/MACROS.yaml" "$repo/org/missions/" || return 1
  cp "$REAL/org/devices/DEVICES.json" "$repo/org/devices/" || return 1
  cp "$REAL/lib/devices.py" "$repo/lib/" || return 1
  cp "$REAL/.tools/to-pipeline-gate.py" "$repo/.tools/" || return 1
  if [ -n "$chk" ]; then cp "$chk" "$repo/.tools/missions-tree-index.py" || return 1; fi
  git -C "$repo" -c core.autocrlf=false add -A -- . || return 1
}

# private_gitdir <gd> <repo>: a private git dir pinned to the merge the way box-sync makes one (HEAD + commondir).
private_gitdir() {
  mkdir -p "$1" || return 1
  printf '%s
' "ref: refs/heads/merge-under-test" > "$1/HEAD" || return 1
  git -C "$2" rev-parse --path-format=absolute --git-common-dir > "$1/commondir" || return 1
}

# ---- arms 1, 2, 4: the merge carries the CURRENT checker; the working tree holds the OLD one.
R1="$T/r1"
mk_tree "$R1" "$T/cur.py" || { echo "test: fixture 1 could not be built" >&2; final; exit 1; }
TREE1="$(git -C "$R1" write-tree)" || { echo "test: fixture 1 write-tree failed" >&2; final; exit 1; }
cp "$T/old.py" "$R1/.tools/missions-tree-index.py"              # the working tree is the OLD checker
GD1="$R1/.git/box-sync-test"; private_gitdir "$GD1" "$R1" || { echo "test: private git dir 1 failed" >&2; final; exit 1; }
GIT_DIR="$GD1" GIT_WORK_TREE="$R1" git read-tree "$TREE1" || { echo "test: read-tree of the merge failed" >&2; final; exit 1; }

# arm 1: the helper's copy of the merge's checker, run as the grade runs it.
CHK1="$(merged_checker_path "$GD1" "$R1")" || CHK1=""
OUT1=""; RC1=0
if [ -n "$CHK1" ]; then
  OUT1="$(GRADE_ACT=".tools/box-sync.sh" GIT_DIR="$GD1" GIT_WORK_TREE="$R1" python "$CHK1" check --staged --act-from-env GRADE_ACT 2>&1)" || RC1=$?
fi
echo "$OUT1" | tail -n 3 | sed 's/^/        | /'
if [ -n "$CHK1" ] && [ "$RC1" -eq 0 ] && echo "$OUT1" | grep -q "RESULT: 0 violation(s)"; then
  pass "arm 1: the merge's own checker passes the project-tree check (rc=0, RESULT: 0 violation(s))"
else
  fail "arm 1: the merge's own checker did not pass (rc=${RC1}, helper path='${CHK1}')"
fi

# arm 2 (CONTROL): the same merge with the working-tree OLD checker, the way the call sites ran before this change.
OUT2=""; RC2=0
OUT2="$(GRADE_ACT=".tools/box-sync.sh" GIT_DIR="$GD1" GIT_WORK_TREE="$R1" python "$R1/.tools/missions-tree-index.py" check --staged --act-from-env GRADE_ACT 2>&1)" || RC2=$?
echo "$OUT2" | tail -n 1 | sed 's/^/        | /'
if [ "$RC2" -ne 0 ] && echo "$OUT2" | grep -q "ValueError"; then
  pass "arm 2 (control): the working-tree OLD checker is REFUSED on the merge (rc=${RC2}, ValueError)"
else
  fail "arm 2 (control): the OLD checker was not refused by ValueError (rc=${RC2})"
fi

# arm 4: the copy exists during the grade and is gone once the private git dir is removed (the call sites' cleanup).
if [ -n "$CHK1" ] && [ -f "$CHK1" ]; then
  rm -rf "$GD1"
  if [ ! -e "$CHK1" ] && [ ! -e "$GD1" ]; then
    pass "arm 4: the helper's copy existed during the grade and is gone after the private git dir is removed"
  else
    fail "arm 4: the helper's copy survived the cleanup (${CHK1})"
  fi
else
  fail "arm 4: no helper copy existed to clean up (path='${CHK1}')"
fi

# ---- arm 3: a merge that does not carry the file falls back to the working-tree path, and says so.
R3="$T/r3"
mk_tree "$R3" "" || { echo "test: fixture 3 could not be built" >&2; final; exit 1; }
TREE3="$(git -C "$R3" write-tree)" || { echo "test: fixture 3 write-tree failed" >&2; final; exit 1; }
cp "$T/old.py" "$R3/.tools/missions-tree-index.py"              # present on disk only, not in the merge
GD3="$R3/.git/box-sync-test"; private_gitdir "$GD3" "$R3" || { echo "test: private git dir 3 failed" >&2; final; exit 1; }
GIT_DIR="$GD3" GIT_WORK_TREE="$R3" git read-tree "$TREE3" || { echo "test: read-tree of fixture 3 failed" >&2; final; exit 1; }
merged_checker_path "$GD3" "$R3" > "$T/p3" 2> "$T/e3"; RC3=$?
P3="$(cat "$T/p3")"
echo "$(cat "$T/e3")" | sed 's/^/        | /'
if [ "$RC3" -eq 0 ] && [ "$P3" = "$R3/.tools/missions-tree-index.py" ] && [ -f "$P3" ] && grep -q "merged-checker: FALLBACK" "$T/e3"; then
  pass "arm 3: a merge without the file falls back to the working-tree checker and says FALLBACK"
else
  fail "arm 3: fallback not taken (rc=${RC3}, printed='${P3}')"
fi

final
