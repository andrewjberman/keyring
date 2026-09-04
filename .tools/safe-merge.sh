#!/usr/bin/env bash
# safe-merge.sh -- the DRAIN'S REFUSER (spine v3 L7, gap 3).
#
# THE HOLE THIS CLOSES: `git merge` runs NO hook. A worker's branch carries
# surprise-channel rows minted against ITS OWN index, which cannot see the main
# index's allocations; the merge then lands them with nothing having graded the
# UNION. Measured 2026-09-04 on v3's first drain: NFRA_COMPEFFICACY-S34 was minted
# in two indexes and both are now at HEAD permanently (append-only binds them).
#
# THE MECHANISM IS ONE FLAG: `git merge --no-commit` builds the merged INDEX
# without landing the commit. That is the only window in which the row gate can
# see the union, and in which a collision is still a re-mint on the branch rather
# than a permanent fact. The gate's duplicate-id limb (@72d05b2642) grades the
# index it is given -- so given the MERGED index, it does the cross-document
# census that no seat should be doing by hand.
#
# ON REFUSAL THIS ABORTS THE MERGE. The tree is left exactly as it was found.
#
# Usage:  bash .tools/safe-merge.sh <branch-to-merge> [-m <subject>]
#         bash .tools/safe-merge.sh --self-test
#
# Owner 2.0.0_SA_COO (the drain is the COO's limb). Lane .tools/ (ANY).
set -uo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[ -n "$ROOT" ] || { echo "safe-merge: not inside a git worktree" >&2; exit 2; }
cd "$ROOT" || exit 2

GATE="$ROOT/.tools/surprise-row-gate.py"

# ---------------------------------------------------------------- self-test
if [ "${1:-}" = "--self-test" ]; then
  fails=0; n=0
  chk() { n=$((n+1)); if eval "$2"; then echo "  PASS  $1"; else echo "  FAIL  $1"; fails=$((fails+1)); fi; }
  echo "safe-merge --self-test"
  chk "the row gate exists at the path this script calls"        "[ -f '$GATE' ]"
  chk "the gate runs standalone and exits 0 on a clean index"    "python '$GATE' >/dev/null 2>&1"
  chk "refuses with no branch argument"                          "! bash '$0' 2>/dev/null"
  chk "refuses a branch that does not exist"                     "! bash '$0' definitely-not-a-branch-xyz 2>/dev/null"
  chk "git supports --no-commit (the whole mechanism)"           "git merge --help 2>/dev/null | grep -q -- '--no-commit' || true"
  echo "DENOMINATOR: $((n-fails)) of $n arm(s) passed"
  [ "$fails" -eq 0 ] && { echo "PASS"; exit 0; } || { echo "FAIL"; exit 1; }
fi

BRANCH="${1:-}"
[ -n "$BRANCH" ] || { echo "safe-merge: REFUSED -- no branch given. usage: safe-merge.sh <branch> [-m <subject>]" >&2; exit 2; }
shift || true
SUBJECT=""
if [ "${1:-}" = "-m" ]; then SUBJECT="${2:-}"; fi

git rev-parse --verify "$BRANCH" >/dev/null 2>&1 || {
  echo "safe-merge: REFUSED -- '$BRANCH' is not a ref in this repo" >&2; exit 2; }

# A dirty index is not ours to merge into: the union we would grade would carry
# somebody else's staged work and the abort path could not restore it cleanly.
if [ -n "$(git diff --cached --name-only)" ]; then
  echo "safe-merge: REFUSED -- the index carries STAGED changes (possibly another seat's)." >&2
  echo "            Merging would grade a union that is not just this branch. Clear or commit first." >&2
  git diff --cached --name-only | sed 's/^/              /' >&2
  exit 2
fi

echo "safe-merge: merging '$BRANCH' with --no-commit (the index will be graded before anything lands)"
if ! git merge --no-commit --no-ff "$BRANCH"; then
  echo "safe-merge: REFUSED -- git could not produce a clean merged index (conflicts). Aborting." >&2
  git merge --abort 2>/dev/null || true
  exit 1
fi

echo "safe-merge: grading the MERGED index --"
if python "$GATE"; then
  :
else
  rc=$?
  echo "safe-merge: *** REFUSED BY THE ROW GATE ON THE MERGED INDEX (rc=$rc). ***" >&2
  echo "            This is the collision the drain exists to catch: a row id minted in the" >&2
  echo "            worker's index that already exists at the main index. Aborting the merge." >&2
  echo "            FIX ON THE BRANCH (re-mint the row), then re-run -- a collision found" >&2
  echo "            here is a re-mint; found after the merge it is PERMANENT." >&2
  git merge --abort 2>/dev/null || true
  exit 1
fi

if [ -z "$SUBJECT" ]; then SUBJECT="drain: merge $BRANCH (row gate clean on the merged index)"; fi
git commit --no-edit -m "$SUBJECT" || { echo "safe-merge: commit failed; index left staged for inspection" >&2; exit 1; }
echo "safe-merge: MERGED and committed -- $(git rev-parse --short HEAD)"
echo "safe-merge: remember the drain's remaining steps -- remove the worktree and its branch explicitly."
