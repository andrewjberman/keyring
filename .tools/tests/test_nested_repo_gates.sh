#!/usr/bin/env bash
# test_nested_repo_gates.sh -- OA-w-2 battery for the nested-repo (submodule) commit
# gates. Builds a SCRATCH superproject with a nested repo in a temp dir (never the
# shared opal_ai -- see .tools/git-hooks/install-owned-paths.sh's own bound), copies
# THIS worktree's hooks/tools + a minimal lane file into it, and exercises four arms:
#
#   nested-granted-pass         a commit inside the nested repo, on a path the parent
#                                lane file grants, PASSes the hook (block mode).
#   nested-violation-block      the same commit shape on a path the lane file does NOT
#                                grant is BLOCKed.
#   safe-commit-nested-landed   .tools/safe-commit.sh run from inside the nested repo
#                                lands a commit (rc 0, the commit shows in its git log).
#   parent-unchanged            in the fixture's OWN parent (a plain, non-nested
#                                commit), a granted commit PASSes and a violation
#                                BLOCKs, exactly as before this cell's changes.
#
# Prints one "ok   [<arm>]" / "FAIL [<arm>] <reason>" line per arm, then
# "ARMS: <k> of 4 PASS". Exit 0 only when all four pass.
#
# Nothing here touches the real opal_ai or its worktree(s): every git repo this script
# creates lives under a fresh `mktemp -d`, torn down at exit.

set -uo pipefail

SRC_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HOOK_SRC="$SRC_ROOT/.tools/git-hooks/owned-paths-check.sh"
INSTALL_SRC="$SRC_ROOT/.tools/git-hooks/install-owned-paths.sh"
VALIDATE_SRC="$SRC_ROOT/.tools/owned-paths-validate.py"
SAFE_COMMIT_SRC="$SRC_ROOT/.tools/safe-commit.sh"
GATE_LIB_SRC="$SRC_ROOT/.tools/commit_gate_lib.sh"
QUEUE_LIB_SRC="$SRC_ROOT/.tools/commit_queue_lib.sh"
# safe-commit.sh's universal commit-gate call (Rule 14: EVERY commit, not just .py, is
# dispatched to commit-gate.sh -- the per-suffix skip lives INSIDE the runner) needs its
# own closure to import cleanly: commit_gate_runner.py's top-level imports reach
# ds-precommit-check.py beside it and comp_constants_cli.py/friends under
# org/modules/graph, and comp_constants_cli's own default config path is the WORKSPACE
# ROOT's comp-constants.config.yaml (computed from ITS OWN copied file location, so it
# resolves correctly once these are copied into a like-shaped fixture tree).
COMMIT_GATE_SH_SRC="$SRC_ROOT/.tools/commit-gate.sh"
GATE_RUNNER_SRC="$SRC_ROOT/.tools/commit_gate_runner.py"
DS_PRECOMMIT_SRC="$SRC_ROOT/.tools/ds-precommit-check.py"
GIT_BASH_RESOLVER_SRC="$SRC_ROOT/.tools/git_bash_resolver.py"
MSYS_ARGV_GUARD_SRC="$SRC_ROOT/.tools/msys_argv_guard.py"
MSG_VERIFY_SRC="$SRC_ROOT/.tools/safe_commit_msg_verify.py"
GRAPH_DIR_SRC="$SRC_ROOT/org/modules/graph"
CC_CONFIG_SRC="$SRC_ROOT/comp-constants.config.yaml"

for f in "$HOOK_SRC" "$INSTALL_SRC" "$VALIDATE_SRC" "$SAFE_COMMIT_SRC" "$GATE_LIB_SRC" "$QUEUE_LIB_SRC" \
         "$COMMIT_GATE_SH_SRC" "$GATE_RUNNER_SRC" "$DS_PRECOMMIT_SRC" "$GIT_BASH_RESOLVER_SRC" \
         "$MSYS_ARGV_GUARD_SRC" "$MSG_VERIFY_SRC" "$CC_CONFIG_SRC"; do
  if [ ! -f "$f" ]; then
    echo "ERROR: fixture source missing: $f"
    echo "ARMS: 0 of 4 PASS"
    exit 1
  fi
done
if [ ! -d "$GRAPH_DIR_SRC" ]; then
  echo "ERROR: fixture source missing: $GRAPH_DIR_SRC"
  echo "ARMS: 0 of 4 PASS"
  exit 1
fi

SCRATCH="$(mktemp -d "${TMPDIR:-/tmp}/oa-w2-nested-gates.XXXXXX")"
cleanup() { rm -rf "$SCRATCH" 2>/dev/null || true; }
trap cleanup EXIT

PARENT="$SCRATCH/parent"
UPSTREAM="$SCRATCH/opal_ai_upstream"

PASS_N=0
FAIL_LOG=()

record() {
  # record <arm> <ok:0|1> [reason]
  local arm="$1" ok="$2" reason="${3:-}"
  if [ "$ok" -eq 0 ]; then
    echo "ok   [$arm]"
    PASS_N=$((PASS_N + 1))
  else
    echo "FAIL [$arm] $reason"
    FAIL_LOG+=("$arm: $reason")
  fi
}

copy_tools() {
  # copy_tools <root> -- lays THIS worktree's hooks/tools into <root>/.tools/**, plus the
  # small closure safe-commit.sh's UNIVERSAL commit-gate call needs to import (org/modules/
  # graph + the workspace-root comp-constants config it reads by computed path).
  local root="$1"
  mkdir -p "$root/.tools/git-hooks" "$root/org/modules"
  cp "$HOOK_SRC" "$root/.tools/git-hooks/owned-paths-check.sh"
  cp "$INSTALL_SRC" "$root/.tools/git-hooks/install-owned-paths.sh"
  cp "$VALIDATE_SRC" "$root/.tools/owned-paths-validate.py"
  cp "$SAFE_COMMIT_SRC" "$root/.tools/safe-commit.sh"
  cp "$GATE_LIB_SRC" "$root/.tools/commit_gate_lib.sh"
  cp "$QUEUE_LIB_SRC" "$root/.tools/commit_queue_lib.sh"
  cp "$COMMIT_GATE_SH_SRC" "$root/.tools/commit-gate.sh"
  cp "$GATE_RUNNER_SRC" "$root/.tools/commit_gate_runner.py"
  cp "$DS_PRECOMMIT_SRC" "$root/.tools/ds-precommit-check.py"
  cp "$GIT_BASH_RESOLVER_SRC" "$root/.tools/git_bash_resolver.py"
  cp "$MSYS_ARGV_GUARD_SRC" "$root/.tools/msys_argv_guard.py"
  cp "$MSG_VERIFY_SRC" "$root/.tools/safe_commit_msg_verify.py"
  cp -r "$GRAPH_DIR_SRC" "$root/org/modules/graph"
  cp "$CC_CONFIG_SRC" "$root/comp-constants.config.yaml"
  chmod +x "$root/.tools/git-hooks/owned-paths-check.sh" "$root/.tools/git-hooks/install-owned-paths.sh" \
    "$root/.tools/safe-commit.sh" "$root/.tools/commit-gate.sh"
}

write_lane_file() {
  # write_lane_file <root> -- a MINIMAL lane file, both entries present from the START
  # (never appended mid-test -- appending after the first commit would itself require
  # committing an edit to a file the lane file grants nobody, its own UNDEFINED
  # violation): one lane grants opal_ai/granted/** AND parent-granted/** to TEST_AGENT;
  # opal_ai/other/** and parent-other/** match no rule (UNDEFINED -> a violation).
  local root="$1"
  cat > "$root/.owned-paths.yaml" <<'YAML'
rollout_phase: 2
lanes:
  TEST_LANE:
    permitted_agents:
      - TEST_AGENT
    description: "OA-w-2 fixture lane -- opal_ai/granted/** and parent-granted/** only."
paths:
  "opal_ai/granted/**":
    lane: TEST_LANE
  "parent-granted/**":
    lane: TEST_LANE
YAML
}

# ---------------------------------------------------------------------------
# BUILD: parent superproject + nested repo (a real submodule, added by local path --
# no network) + hooks/tools/lane-file copied in.
# ---------------------------------------------------------------------------
mkdir -p "$UPSTREAM"
git init -q "$UPSTREAM"
git -C "$UPSTREAM" config user.email "upstream@test.local"
git -C "$UPSTREAM" config user.name "upstream"
echo "seed" > "$UPSTREAM/README.md"
git -C "$UPSTREAM" add README.md
git -C "$UPSTREAM" commit -q -m "seed"

mkdir -p "$PARENT"
git init -q "$PARENT"
git -C "$PARENT" config user.email "test@test.local"
git -C "$PARENT" config user.name "test"
git -C "$PARENT" config protocol.file.allow always
copy_tools "$PARENT"
write_lane_file "$PARENT"
git -C "$PARENT" add .tools .owned-paths.yaml
git -C "$PARENT" commit -q -m "fixture: hooks + tools + lane file"

SUBMODULE_ADD_ERR="$(git -C "$PARENT" -c protocol.file.allow=always submodule add -q "$UPSTREAM" opal_ai 2>&1)"
if [ ! -e "$PARENT/opal_ai/.git" ]; then
  echo "ERROR: submodule add failed: $SUBMODULE_ADD_ERR"
  echo "ARMS: 0 of 4 PASS"
  exit 1
fi
git -C "$PARENT" commit -q -m "add opal_ai submodule"
# COMMITTER identity (distinct from --author, which the fixture's own commits set
# per-call): a fresh submodule checkout carries no user.[name|email] of its own, and
# a real device always has one at the global level -- set it here so the fixture's
# git-commit calls need nothing beyond what a real device already provides.
git -C "$PARENT/opal_ai" config user.email "test@test.local"
git -C "$PARENT/opal_ai" config user.name "test"

# Install the pre-commit hook into the NESTED repo's OWN hooks dir (the round's
# issuer's act, exercised here only against the SCRATCH nested repo -- never the
# real opal_ai; see install-owned-paths.sh's --submodule bound).
INSTALL_OUT="$(cd "$PARENT" && bash .tools/git-hooks/install-owned-paths.sh --submodule opal_ai 2>&1)"
INSTALL_RC=$?
NESTED_GITDIR="$(git -C "$PARENT/opal_ai" rev-parse --absolute-git-dir 2>/dev/null || true)"

# ---------------------------------------------------------------------------
# ARM 1: nested-granted-pass
# ---------------------------------------------------------------------------
if [ "$INSTALL_RC" -eq 0 ] && [ -n "$NESTED_GITDIR" ] && [ -f "$NESTED_GITDIR/hooks/pre-commit" ]; then
  mkdir -p "$PARENT/opal_ai/granted"
  echo "ok content" > "$PARENT/opal_ai/granted/file1.txt"
  ( cd "$PARENT/opal_ai" && git add granted/file1.txt \
      && GIT_AUTHOR_NAME="TEST_AGENT <t@t>" GIT_COMMITTER_NAME="TEST_AGENT" GIT_COMMITTER_EMAIL="t@t" \
         git -c user.email=t@t -c user.name=TEST_AGENT commit -q --author "TEST_AGENT <t@t>" -m "granted path" )
  RC1=$?
  if [ "$RC1" -eq 0 ]; then
    record nested-granted-pass 0
  else
    record nested-granted-pass 1 "commit on a granted nested path was refused (rc=$RC1)"
  fi
else
  record nested-granted-pass 1 "hook not installed at $NESTED_GITDIR/hooks/pre-commit (install rc=$INSTALL_RC: $INSTALL_OUT)"
fi

# ---------------------------------------------------------------------------
# ARM 2: nested-violation-block
# ---------------------------------------------------------------------------
mkdir -p "$PARENT/opal_ai/other"
echo "ungranted content" > "$PARENT/opal_ai/other/file2.txt"
VIOLATION_OUT="$(cd "$PARENT/opal_ai" && git add other/file2.txt \
    && git -c user.email=t@t -c user.name=TEST_AGENT commit --author "TEST_AGENT <t@t>" -m "ungranted path" 2>&1)"
RC2=$?
( cd "$PARENT/opal_ai" && git reset -q HEAD -- other/file2.txt 2>/dev/null || true )
if [ "$RC2" -ne 0 ] && printf '%s\n' "$VIOLATION_OUT" | grep -q "lane violation"; then
  record nested-violation-block 0
else
  record nested-violation-block 1 "expected a lane-violation BLOCK (rc!=0); got rc=$RC2: $(printf '%s' "$VIOLATION_OUT" | tr '\n' ' ' | head -c 200)"
fi

# ---------------------------------------------------------------------------
# ARM 3: safe-commit-nested-landed
# ---------------------------------------------------------------------------
mkdir -p "$SCRATCH/msg"
MSGFILE="$SCRATCH/msg/nested.msg"
printf 'chore(fixture): nested safe-commit landing\n' > "$MSGFILE"
echo "safe-commit content" > "$PARENT/opal_ai/granted/file3.txt"
SC_OUT="$(cd "$PARENT/opal_ai" \
    && bash "$PARENT/.tools/safe-commit.sh" --author "TEST_AGENT <t@t>" -F "$MSGFILE" -- granted/file3.txt 2>&1)"
SC_RC=$?
LOG_HAS_IT="$(git -C "$PARENT/opal_ai" log --oneline --all -- granted/file3.txt 2>/dev/null)"
if [ "$SC_RC" -eq 0 ] && [ -n "$LOG_HAS_IT" ]; then
  record safe-commit-nested-landed 0
else
  record safe-commit-nested-landed 1 "safe-commit rc=$SC_RC; git log for granted/file3.txt: '${LOG_HAS_IT:-<empty>}'; output: $(printf '%s' "$SC_OUT" | tr '\n' ' ' | head -c 300)"
fi

# ---------------------------------------------------------------------------
# ARM 4: parent-unchanged -- in the fixture's OWN parent (a plain, non-nested
# worktree), a granted commit PASSes and a violation BLOCKs, exactly as before.
# The lane file already carries parent-granted/** (write_lane_file, above) --
# never appended mid-test, which would itself be an edit to a file nothing grants.
# ---------------------------------------------------------------------------
( cd "$PARENT" && bash .tools/git-hooks/install-owned-paths.sh >/dev/null 2>&1 )
mkdir -p "$PARENT/parent-granted" "$PARENT/parent-other"
echo "granted" > "$PARENT/parent-granted/a.txt"
echo "other" > "$PARENT/parent-other/b.txt"
( cd "$PARENT" && git add parent-granted/a.txt )
PARENT_PASS_OUT="$(cd "$PARENT" && git -c user.email=t@t -c user.name=TEST_AGENT commit --author "TEST_AGENT <t@t>" -m "parent granted path" 2>&1)"
PARENT_PASS_RC=$?
( cd "$PARENT" && git add parent-other/b.txt )
PARENT_BLOCK_OUT="$(cd "$PARENT" && git -c user.email=t@t -c user.name=TEST_AGENT commit --author "TEST_AGENT <t@t>" -m "parent ungranted path" 2>&1)"
PARENT_BLOCK_RC=$?
( cd "$PARENT" && git reset -q HEAD -- parent-other/b.txt 2>/dev/null || true )
if [ "$PARENT_PASS_RC" -eq 0 ] && [ "$PARENT_BLOCK_RC" -ne 0 ] && printf '%s\n' "$PARENT_BLOCK_OUT" | grep -q "lane violation"; then
  record parent-unchanged 0
else
  record parent-unchanged 1 "pass_rc=$PARENT_PASS_RC block_rc=$PARENT_BLOCK_RC block_out=$(printf '%s' "$PARENT_BLOCK_OUT" | tr '\n' ' ' | head -c 200)"
fi

echo "ARMS: $PASS_N of 4 PASS"
[ "$PASS_N" -eq 4 ] && exit 0 || exit 1
