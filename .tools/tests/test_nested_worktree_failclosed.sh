#!/usr/bin/env bash
# OA-e-11 regression test (row NFRA_OPALAI-Z-S17): a commit in a LINKED worktree of a submodule placed OUTSIDE every
# parent worktree must be graded against the superproject's lane file (fail CLOSED), not skip the lane check.
# Builds its own scratch superproject + submodule `opal_ai` under mktemp -d (local file protocol, no network), copies the
# lane file, validator and both hook scripts from THIS tree, installs the hook, and runs the arms. opal_ai/** is lane
# ANY_EXEC_OR_AE: 0.4.0_DS_ClientPlatform is out of it, 1.0.0_SA_CTO is in it.
# Prints one line per arm and ends with `RESULT: N passed, M failed`; exit 0 only when M is 0.
# Never writes the real org/git-author-override-audit.log (OWNED_PATHS_AUDIT_LOG is a scratch file).
_HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
_ROOT="$(git -C "$_HERE" rev-parse --show-toplevel)"
FX="$(mktemp -d)"; trap 'rm -rf "$FX" 2>/dev/null' EXIT
SUPER="$FX/super"; NESTED="$SUPER/opal_ai"; OUTSIDE="$FX/outside"
export OWNED_PATHS_AUDIT_LOG="$FX/audit.log"
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR OWNED_PATHS_STAGED_FILES GIT_COMMIT_AUTHOR_OVERRIDE OWNED_PATHS_MODE
_g() { git -c user.name=fixture -c user.email=fixture@opal.agent -c protocol.file.allow=always "$@"; }
PASS=0; FAIL=0
ok()  { echo "ok   $1"; PASS=$((PASS+1)); }
bad() { echo "FAIL $1"; FAIL=$((FAIL+1)); }
die() { echo "FAIL fixture: $1"; echo "RESULT: $PASS passed, $((FAIL+1)) failed"; exit 1; }

_g init -q -b main "$FX/subsrc" || die "init subsrc"
_g -C "$FX/subsrc" commit -q --allow-empty -m init || die "subsrc commit"
_g init -q -b main "$SUPER" || die "init super"
mkdir -p "$SUPER/.tools/git-hooks"
for f in .owned-paths.yaml .tools/owned-paths-validate.py .tools/git-hooks/owned-paths-check.sh .tools/git-hooks/install-owned-paths.sh; do
    cp "$_ROOT/$f" "$SUPER/$f" || die "copy $f"
done
( cd "$SUPER" && _g submodule add -q "$FX/subsrc" opal_ai >/dev/null 2>&1 ) || die "submodule add"
_g -C "$SUPER" add -A >/dev/null 2>&1; _g -C "$SUPER" commit -q --no-verify -m fixture || die "super commit"
_g -C "$NESTED" worktree add -q "$OUTSIDE" -b wk-fixture-outside >/dev/null 2>&1 || die "nested worktree add"
( cd "$SUPER" && bash .tools/git-hooks/install-owned-paths.sh --submodule opal_ai >/dev/null 2>&1 ) || die "install --submodule"
( cd "$SUPER" && bash .tools/git-hooks/install-owned-paths.sh >/dev/null 2>&1 ) || die "install parent"

# fx_commit <dir> <author-serial> <new-file> -> "landed" | "refused rc=<n>"; stderr of the commit in $FX/last.out
fx_commit() {
    local d="$1" a="$2" f="$3" before after rc
    before=$(git -C "$d" rev-parse HEAD 2>/dev/null)
    mkdir -p "$(dirname "$d/$f")"; printf 'planted by test\n' > "$d/$f"
    git -C "$d" add -- "$f" >/dev/null 2>&1
    GIT_AUTHOR_NAME="$a" GIT_AUTHOR_EMAIL="$a@opal.agent" timeout 60 \
        git -C "$d" -c user.name=fixture -c user.email=fixture@opal.agent commit -q --author "$a <$a@opal.agent>" -m planted -- "$f" >"$FX/last.out" 2>&1
    rc=$?
    after=$(git -C "$d" rev-parse HEAD 2>/dev/null)
    if [ "$before" != "$after" ]; then echo "landed"; else echo "refused rc=$rc"; fi
}
expect() { # expect <label> <want: landed|refused> <got>
    case "$3" in
        landed) [ "$2" = landed ] && ok "$1: landed" || bad "$1: wanted refused, got landed" ;;
        refused*) [ "$2" = refused ] && ok "$1: $3" || bad "$1: wanted landed, got $3 ($(tr '\n' ' ' < "$FX/last.out" | cut -c1-200))" ;;
    esac
}

expect "arm1 outside-worktree out-of-lane" refused "$(fx_commit "$OUTSIDE" 0.4.0_DS_ClientPlatform planted_outside.md)"
grep -q 'VIOLATION' "$FX/last.out" && ok "arm1 refusal names a lane VIOLATION (graded, not skipped)" || bad "arm1 refusal has no VIOLATION line: $(tr '\n' ' ' < "$FX/last.out" | cut -c1-200)"
expect "arm1b outside-worktree in-lane (positive control)" landed "$(fx_commit "$OUTSIDE" 1.0.0_SA_CTO planted_outside_in.md)"
expect "arm2 main-nested out-of-lane" refused "$(fx_commit "$NESTED" 0.4.0_DS_ClientPlatform planted_nested_out.md)"
expect "arm3 main-nested in-lane" landed "$(fx_commit "$NESTED" 1.0.0_SA_CTO planted_nested_in.md)"
expect "arm4 parent out-of-lane" refused "$(fx_commit "$SUPER" 0.4.0_DS_ClientPlatform docs/architecture/ZZPLANT_OUT.md)"
expect "arm5 parent in-lane" landed "$(fx_commit "$SUPER" 1.0.0_SA_CTO docs/architecture/ZZPLANT_IN.md)"

# arm6: a submodule whose superproject cannot resolve is REFUSED loud (never skipped), even for an in-lane author.
_GD="$(git -C "$NESTED" rev-parse --absolute-git-dir)"
git config --file "$_GD/config" --unset core.worktree
r=$(fx_commit "$OUTSIDE" 1.0.0_SA_CTO planted_unresolved.md)
expect "arm6 submodule with unresolvable superproject" refused "$r"
grep -q 'superproject could not be resolved' "$FX/last.out" && ok "arm6 message names the reason" || bad "arm6 message missing reason: $(tr '\n' ' ' < "$FX/last.out" | cut -c1-200)"

echo "RESULT: $PASS passed, $FAIL failed"
[ "$FAIL" = 0 ]
