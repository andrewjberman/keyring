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
# FIXED 2026-07-13 (RV-0046 F-001 sibling / RV-0047). THIS FUNCTION WAS A FALSE WITNESS.
#
# It read `^SERIAL=` from `$root/.comp-graph/.agent_context` -- a SHARED, repo-root file that
# EVERY agent's startup Step E TRUNCATES AND REWRITES. So it named whoever ran Step E most
# recently, not the actor. And because org/XXX.md Step E guarantees the file always EXISTS,
# the GIT_AUTHOR_NAME fallback was UNREACHABLE -- and GIT_AUTHOR_NAME is unset in an agent
# Bash-tool shell anyway. THE FUNCTION HAD NO BRANCH THAT COULD EVER NAME THE TRUE ACTOR:
#   file present -> whoever last ran Step E;  file absent -> UNKNOWN.
#
# Exercised live 2026-07-10 (CVO, real function, real root): it named `1.0.0_SA_CTO` while
# `3.0.0_SA_CVO` was the actor -- and `$OPAL_AGENT_SERIAL` held the correct answer, unread.
#
# *** An absent field is a gap. A confident WRONG field is a false witness. ***
# And this one is ANTI-CORRELATED: it names the most-recently-STARTED agent, who by construction
# has the FEWEST local commits worth force-discarding. ON A DESTRUCTIVE HEAD MOVE, IT NAMED THE
# INNOCENT -- which is worse than logging nothing at all.
#
# Now delegates to the one sound resolver (env -> per-session file -> git author -> UNKNOWN).
# .comp-graph/.agent_context is NEVER consulted: it answers "what TO", never "who am I".
__headmove_serial() {
    local root="$1" here
    here="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd)" || here=""
    if [ -n "$here" ] && [ -f "$here/../lib/resolve-actor.sh" ]; then
        . "$here/../lib/resolve-actor.sh"
        resolve_actor
        return 0
    fi
    # Resolver missing -> replicate its precedence inline. Still NEVER the shared file.
    local serial="${OPAL_AGENT_SERIAL:-}"
    if [ -z "$serial" ] && [ -n "${CLAUDE_CODE_SESSION_ID:-}" ] \
       && [ -f "$root/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial" ]; then
        serial="$(tr -d '\r\n' < "$root/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial" 2>/dev/null)"
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
    local root audit ws here foreign
    root="$(command git rev-parse --show-toplevel 2>/dev/null)"
    # *** THE AUDIT LOG IS GOVERNANCE EVIDENCE AND IT LIVES IN ajb_workspace, ALWAYS. ***
    # Until 2026-08-30 this resolved the log from the CURRENT repo's toplevel, so a FORCE_HEADMOVE in
    # any other clone wrote a NEW org/git-author-override-audit.log INTO THAT TREE. Measured by
    # 1.1.0_SA_KJ~Y the same day: the foreign repo's own compiler then refused the file it had just been
    # given ("forbidden org runtime/history extension") and its suites went 11 failed / 362 passed --
    # SAME COMMIT, NO CODE CHANGE. A seat that did not diff its own tree would read those failures as a
    # defect in its work. That is the worst shape a guard can have: its own audit act damages a
    # repository it does not own, and the damage is indistinguishable from the seat's work being broken.
    # Two consequences beyond the mess: the governance log SPLITS (OVERRIDE_REVIEW walks ajb_workspace's
    # copy and would never see the foreign one), and __headmove_serial loses org/mcp/sessions/ -- so the
    # serial silently degrades to GIT_AUTHOR_NAME or UNKNOWN on exactly the entries that matter most.
    # Resolved from THIS FILE's own location instead, which is cwd-independent by construction.
    here="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." 2>/dev/null && pwd)" || here=""
    ws="${HEADMOVE_WS:-$here}"
    audit="${HEADMOVE_AUDIT_LOG:-$ws/org/git-author-override-audit.log}"
    # The marker binds $ws to the tree THIS FILE lives in. Belt-and-braces: the installer wires an
    # ABSOLUTE source path into ~/.bashrc, so BASH_SOURCE is absolute and $ws is already cwd-independent --
    # but a hand-edited RELATIVE source line would resolve $ws against the cwd, and "does it have org/"
    # alone would then happily accept a foreign repo that happens to have one (the tree that reported this
    # defect HAS an org/). Under that shape this fails to the loud WARN instead of writing into it.
    if [ -z "$ws" ] || [ ! -d "$ws/org" ] || [ ! -f "$ws/.tools/git-hooks/headmove-guard.sh" ]; then
        # FAIL OPEN, LOUDLY -- per the CTO ruling in this file's header. The move still proceeds; what
        # is lost is the record, and a silently unrecorded override is the thing worth shouting about.
        echo "WARN: headmove-guard cannot resolve the ajb_workspace audit log -- THIS OVERRIDE IS NOT RECORDED." >&2
        return 0
    fi
    # Name the foreign tree when there is one. Same-repo lines keep their exact historical shape, so
    # nothing that reads this log has to change; a foreign override stops being indistinguishable.
    foreign=""
    [ -n "$root" ] && [ "$root" != "$ws" ] && foreign=" [repo: $root]"
    echo "$(date -u +%Y-%m-%dT%H%M%SZ) $1 $(__headmove_serial "$ws") $2$foreign" \
        >> "$audit" || echo "WARN: headmove-guard failed to append to $audit -- override NOT recorded." >&2
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
