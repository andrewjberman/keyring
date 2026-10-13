# merged-checker.sh -- the project-tree checker THE MERGE carries, for grading that merge (NFRA_CTLPLN.TO-CT-ab-13).
#
# Sourced by .tools/box-sync.sh and .tools/safe-merge.sh. Defines one function:
#
#   merged_checker_path <git-dir> <fallback-root>
#
# Prints the path of a runnable missions-tree-index.py to call with `check --staged`:
#   - the merge carries the file at stage 0 in the private index at <git-dir>: a fresh COPY of the merge's bytes is
#     written under <git-dir>/merged-checker.XXXXXX/.tools/, and its path is printed. The caller's existing cleanup of
#     <git-dir> removes the copy.
#   - the merge does not carry the file: prints <fallback-root>/.tools/missions-tree-index.py and says
#     `merged-checker: FALLBACK` on stderr.
# Returns 1, printing nothing on stdout, when the merge carries the file but it cannot be read or copied.
#
# WHY: the working tree's checker grades the merge's staged bytes. A checker that its own previous version cannot read
# (CT-ab-8: FABRIC_ENUM = tuple(_fabric_values()) is not a literal) then refuses the merge. The copy is the merge's own.
#
# ROOT DISCOVERY (chosen: the copy sits beside its own `.tools/` under <git-dir>). The checker sets _WS from its own
# location (parent of parent), so _WS becomes <git-dir>/merged-checker.XXXXXX, not the worktree. This is harmless for the
# grade: `check --staged` reads every input through the index named by GIT_DIR (materialise_index writes them into a
# scratch dir) and never reads _WS. The checker has no root option, and the alternative (copying into the worktree's
# .tools/) would leave an untracked file in the working tree.

merged_checker_path() {
  local gd="$1" fb="$2" listing tmpd
  if [ -z "$gd" ] || [ -z "$fb" ]; then
    echo "merged-checker: ERROR -- merged_checker_path needs <git-dir> <fallback-root>" >&2
    return 1
  fi
  listing="$(GIT_DIR="$gd" GIT_WORK_TREE="$fb" git ls-files -s -- ':(top).tools/missions-tree-index.py')" \
    || { echo "merged-checker: ERROR -- cannot list the merge's index under $gd" >&2; return 1; }
  if [ -z "$listing" ]; then
    echo "merged-checker: FALLBACK -- the merge does not carry .tools/missions-tree-index.py; using the working-tree copy $fb/.tools/missions-tree-index.py" >&2
    printf '%s\n' "$fb/.tools/missions-tree-index.py"
    return 0
  fi
  case "$listing" in
    *$'\n'*) echo "merged-checker: ERROR -- .tools/missions-tree-index.py is listed more than once in the merge's index" >&2; return 1 ;;
    *" 0"$'\t'*) ;;
    *) echo "merged-checker: ERROR -- .tools/missions-tree-index.py is unmerged in the merge's index ($listing)" >&2; return 1 ;;
  esac
  tmpd="$(mktemp -d "$gd/merged-checker.XXXXXX")" || { echo "merged-checker: ERROR -- cannot make a scratch dir under $gd" >&2; return 1; }
  mkdir -p "$tmpd/.tools" || { rm -rf "$tmpd"; return 1; }
  if ! GIT_DIR="$gd" GIT_WORK_TREE="$fb" git show ":.tools/missions-tree-index.py" > "$tmpd/.tools/missions-tree-index.py"; then
    echo "merged-checker: ERROR -- cannot read the merge's missions-tree-index.py from $gd" >&2
    rm -rf "$tmpd"
    return 1
  fi
  printf '%s\n' "$tmpd/.tools/missions-tree-index.py"
}
