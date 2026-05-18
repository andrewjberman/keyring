#!/usr/bin/env bash
# ADHC_OWNPTH.010 -- Unified destructive-HEAD-move guard (git() shadow function).
#
# SOURCEABLE LIBRARY -- meant to be `source`d, not executed; not a git hook.
# (The shebang documents the intended interpreter; the file defines functions
# only and is wired into ~/.bashrc by install-headmove-guard.sh.) `~/.bashrc` sources
# this file (wired idempotently by install-headmove-guard.sh); it defines a
# `git()` shell function that SHADOWS the git command and gates operations that
# discard or rewrite local-only commits: `git reset <divergent-ref>`,
# `git rebase`, and `git commit --amend`.
#
# WHY A SHADOW FUNCTION, NOT A HOOK (ADHC_OWNPTH.010 Phase-4 finding,
# CTO re-ruling 2026-05-18 -- Option A):
#   - git has NO `pre-reset` hook at any version.
#   - The `reference-transaction` hook is the only hook that fires on `git
#     reset`, BUT installing ANY reference-transaction hook -- even a no-op
#     `exit 0` -- DETERMINISTICALLY hangs `git rebase` (7/7) and flakily hangs
#     `git merge --ff` on Windows Git Bash (git 2.54.0.windows.1). The hang is
#     the hook's PRESENCE, not its content.
#   - A `~/.bashrc`-autoloaded `git()` function is structural (every shell that
#     sources the profile gets it -- zero per-invocation agent action) and
#     hangs nothing.
#
# COVERAGE BOUNDARY (honest -- CTO constraint 4):
#   - COVERS: `git ...` typed in any bash shell that sources ~/.bashrc -- which
#     includes Claude Code Bash-tool shells (profile-initialized per call).
#   - DOES NOT COVER: PowerShell, cmd.exe, GUI git clients, `command git ...`,
#     `/usr/bin/git ...` (absolute path), or git invoked by tools that don't go
#     through an interactive-profile bash. The escape hatch (`command git`) is
#     also, deliberately, the recursion guard -- so the bypass is intrinsic.
#   - This matches the incident class: AE 0.7's 2026-05-08 reset was a typed
#     `git reset` in a bash shell. The guard catches the human/agent-typed path.
#
# Escape hatch: FORCE_HEADMOVE=1 (alias RESET_FORCE=1) allows the move and
# appends a FORCE-HEADMOVE line to org/git-author-override-audit.log.
#
# FAIL-OPEN by design (CTO ruling 2026-05-18): any parse/resolve ambiguity
# falls through to real git. A `git()` shadow that blocks or hangs legitimate
# operations is far worse than one that misses an edge case. Only a CONFIRMED
# destructive move is ever gated. Per the CTO addition, the guard "fails open
# LOUDLY IN THE LOG" -- every error-driven fail-open writes a HEADMOVE-FAILOPEN
# line to the same audit log, so a chronically degraded guard is detectable.
# (Determined-non-destructive passes are silent -- that is the guard working.)
#
# HYGIENE: this file is SOURCED into interactive shells. It MUST NOT change
# shell options (no `set -e`/`set -u`), MUST NOT leak variables (all `local`),
# and every internal git call uses `command git` (recursion guard + bypass).
#
# Windows Git Bash 3.6.7 compatible -- only default-install utilities
# (CLAUDE.md Rule 16): bash, git, date, grep, sed, printf.

# ---------------------------------------------------------------------------
# __headmove_serial <repo-root> -- resolve the acting agent serial.
# ---------------------------------------------------------------------------
__headmove_serial() {
    local root="$1" serial=""
    if [ -f "$root/.comp-graph/.agent_context" ]; then
        serial="$(grep -m1 '^SERIAL=' "$root/.comp-graph/.agent_context" 2>/dev/null \
            | sed 's/^SERIAL=//' | tr -d '\r')"
    fi
    [ -z "$serial" ] && serial="${GIT_AUTHOR_NAME%% <*}"
    [ -z "$serial" ] && serial="UNKNOWN"
    printf '%s' "$serial"
}

# ---------------------------------------------------------------------------
# __headmove_audit <token> <tail> -- append one timestamped line to the audit
# log (org/git-author-override-audit.log, shared with safe-commit.sh).
#   line: {ISO8601-basic} {token} {serial} {tail}
# ---------------------------------------------------------------------------
__headmove_audit() {
    local root audit
    root="$(command git rev-parse --show-toplevel 2>/dev/null)"
    [ -z "$root" ] && root="."
    audit="${HEADMOVE_AUDIT_LOG:-$root/org/git-author-override-audit.log}"
    echo "$(date -u +%Y-%m-%dT%H%M%SZ) $1 $(__headmove_serial "$root") $2" \
        >> "$audit" 2>/dev/null || true
}

# ---------------------------------------------------------------------------
# __headmove_guard <subcommand> <args-after-subcommand...>
#   exit 0 -> allow (non-destructive, forced, or error fail-open)
#   exit 1 -> block (destructive, not forced)
# Never blocks unless a destructive move is positively confirmed.
# ---------------------------------------------------------------------------
__headmove_guard() {
    local sub="$1"; shift

    local old
    old="$(command git rev-parse --verify --quiet HEAD 2>/dev/null)"
    [ -z "$old" ] && return 0   # no HEAD yet -- nothing can be discarded

    local range="" target_desc="" verb="" a
    case "$sub" in
        reset)
            # Path-mode resets never move HEAD -- pass straight through.
            for a in "$@"; do
                case "$a" in
                    --) return 0 ;;
                    -p|--patch) return 0 ;;
                    --pathspec-from-file|--pathspec-from-file=*) return 0 ;;
                esac
            done
            # Collect non-flag args.
            local nonflag_count=0 first_nonflag=""
            for a in "$@"; do
                case "$a" in
                    -*) ;;
                    *)  nonflag_count=$((nonflag_count + 1))
                        [ -z "$first_nonflag" ] && first_nonflag="$a" ;;
                esac
            done
            # 0 non-flag args  -> reset to HEAD (no move).
            # 2+ non-flag args -> `git reset <commit> <pathspec...>` (no move).
            [ "$nonflag_count" -ne 1 ] && return 0
            local t
            t="$(command git rev-parse --verify --quiet "${first_nonflag}^{commit}" 2>/dev/null)"
            # Not a commit-ish -> it is a pathspec -> path-mode reset, no move.
            [ -z "$t" ] && return 0
            [ "$t" = "$old" ] && return 0    # no move
            # Destructive iff old is NOT an ancestor of the target.
            command git merge-base --is-ancestor "$old" "$t" 2>/dev/null
            local mbrc=$?
            [ "$mbrc" -eq 0 ] && return 0    # forward move -- non-destructive
            if [ "$mbrc" -ne 1 ]; then
                __headmove_audit "HEADMOVE-FAILOPEN" "reset (merge-base errored rc=$mbrc)"
                return 0                     # fail-open, logged
            fi
            range="$t..$old"
            target_desc="$t"
            verb="reset"
            ;;
        rebase)
            # In-progress rebase control verbs never start a new rewrite.
            case "${1:-}" in
                --continue|--abort|--skip|--quit|--edit-todo|--show-current-patch)
                    return 0 ;;
            esac
            # Upstream = first non-flag arg; fall back to the configured upstream.
            local up=""
            for a in "$@"; do
                case "$a" in -*) ;; *) up="$a"; break ;; esac
            done
            [ -z "$up" ] && up="@{upstream}"
            local upsha
            upsha="$(command git rev-parse --verify --quiet "${up}^{commit}" 2>/dev/null)"
            if [ -z "$upsha" ]; then
                __headmove_audit "HEADMOVE-FAILOPEN" "rebase (upstream '$up' unresolvable)"
                return 0                     # fail-open, logged
            fi
            local cnt
            cnt="$(command git rev-list --count "${upsha}..HEAD" 2>/dev/null)"
            case "$cnt" in
                ''|*[!0-9]*)
                    __headmove_audit "HEADMOVE-FAILOPEN" "rebase (rev-list count failed)"
                    return 0 ;;              # fail-open, logged
            esac
            [ "$cnt" -eq 0 ] && return 0     # nothing to rewrite (ff / no-op)
            range="${upsha}..HEAD"
            target_desc="$upsha"
            verb="rebase"
            ;;
        commit)
            # Only `--amend` rewrites a commit; a plain commit moves forward.
            local is_amend=""
            for a in "$@"; do
                case "$a" in --amend) is_amend=1; break ;; esac
            done
            [ -z "$is_amend" ] && return 0
            if command git rev-parse --verify --quiet HEAD~1 >/dev/null 2>&1; then
                range="HEAD~1..HEAD"
            else
                range="HEAD"                 # amending a root commit
            fi
            target_desc="amended"
            verb="commit --amend"
            ;;
        *)
            return 0
            ;;
    esac

    # --- A destructive move is confirmed -------------------------------------
    local discarded n
    discarded="$(command git log --format='  %h  %an  (%ar)  %s' $range 2>/dev/null)"
    n="$(printf '%s\n' "$discarded" | grep -c . 2>/dev/null)"
    [ -z "$n" ] && n=0

    if [ -n "${FORCE_HEADMOVE:-${RESET_FORCE:-}}" ]; then
        __headmove_audit "FORCE-HEADMOVE" "${old} -> ${target_desc} (${n} discarded)"
        echo "WARN: destructive ${verb} ALLOWED via FORCE_HEADMOVE -- ${n} commit(s) discarded/rewritten; logged to org/git-author-override-audit.log" >&2
        return 0
    fi

    {
        echo "================================================================"
        echo "ABORTED: destructive ${verb} would discard/rewrite ${n} local commit(s)"
        echo "================================================================"
        printf '%s\n' "$discarded"
        echo "----------------------------------------------------------------"
        echo "If this is intentional, re-run with:"
        echo "    FORCE_HEADMOVE=1 git ${verb} ..."
        echo "The forced move will be logged to org/git-author-override-audit.log"
        echo "================================================================"
    } >&2
    return 1
}

# ---------------------------------------------------------------------------
# git() -- shadow function. Finds the real subcommand past any global options,
# routes reset/rebase/commit through the guard, passes everything else through.
# Every internal git call uses `command git` (recursion guard).
# ---------------------------------------------------------------------------
git() {
    local args=("$@")
    local n=${#args[@]}
    local i=0 sub="" subidx=-1 tok

    # Skip leading `git` global options to locate the real subcommand.
    while [ "$i" -lt "$n" ]; do
        tok="${args[$i]}"
        case "$tok" in
            -c|-C|--git-dir|--work-tree|--namespace|--super-prefix|--config-env|--attr-source|--exec-path)
                i=$((i + 2)); continue ;;          # option takes a separate value
            -*)
                i=$((i + 1)); continue ;;          # valueless / `--opt=val` global option
            *)
                sub="$tok"; subidx=$i; break ;;
        esac
    done

    case "$sub" in
        reset|rebase|commit)
            __headmove_guard "$sub" "${args[@]:$((subidx + 1))}"
            local grc=$?
            if [ "$grc" -ne 0 ]; then
                return "$grc"
            fi
            command git "$@"
            ;;
        *)
            command git "$@"
            ;;
    esac
}
