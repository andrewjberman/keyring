#!/usr/bin/env bash
# never-rules-gate.sh -- PreToolUse hook. THE GATE FOR THREE UNGATED "NEVER" RULES.
#
# Built 2026-07-13 by 1.0.0_SA_CTO against MSTR RV-0047 F-009/F-010 ("every gate RV-0046
# declared a blocker was RULED AND NEVER BUILT ... 581 commits happened in between").
#
# ===========================================================================================
# WHY A HOOK AND NOT A PATH SHIM -- RV-0047's PREMISE IS FALSE, MEASURED:
#   RV-0047 says: "No `git` PATH shim -- and the `terraform` shim it was modeled on EXISTS at
#   .tools/terraform. The mechanism is proven; it simply was not applied to git."
#   IT DOES NOT EXIST.  `file .tools/terraform` -> PE32+ executable (the real Go binary).
#   Same for .tools/terraform.exe. THERE IS NO TERRAFORM SHIM. A shim was inferred from a
#   filename and then cited as a proven mechanism -- by RV-0047, and by CLAUDE.md NEVER#7
#   itself ("same mechanism as the bare-`terraform apply` shim: one shim, two NEVER rules").
#   *** A COMMENT IS A CLAIM WITH NO VINTAGE AND NO TEST. *** (This file's own doctrine,
#   landed in Rule 22a hours before it caught RV-0047.)
#
#   AND IT HAS A SECOND CONSEQUENCE NOBODY DREW: .tools/ is on PATH and .tools/terraform IS
#   the real binary -- so a bare `terraform apply` (NEVER#3) runs STRAIGHT THROUGH, ungated.
#   Two NEVER rules, both unenforced, and the doc cited a shim for one as the model for the
#   other. Neither existed.
#
#   The mechanism that IS proven in this repo is the PreToolUse hook (block-bare-inbox-watch,
#   comp-tool-hud -- both live). It fires on `Bash|PowerShell`, which is exactly what a PATH
#   shim could never fix: CLAUDE.md notes the bash `git()` shadow is useless because
#   "PowerShell never sources ~/.bashrc, so BOTH forms are ungated there." A hook has no shell.
# ===========================================================================================
#
# GATES (each = an existing NEVER rule with no enforcement):
#   1. NEVER#7  rebase on a SHARED branch (CLOUD/DEV/PROD/main/master) -- incl. `git pull --rebase`,
#               and a BARE `git pull` when pull.rebase=true (CLAUDE.md: "pull.rebase=true makes a
#               *bare* git pull rebase"; headmove-guard.sh has `pull` x0).
#   2. NEVER#3  bare `terraform apply` / `destroy` (must go through safe-apply / safe-destroy).
#   3. LD-0276  `git commit`/`safe-commit` with `-m` AND a backtick or `$(` -- a commit message is
#               an EXECUTION VECTOR; the substitution happens BEFORE git sees it, so a safe-commit
#               lint structurally CANNOT catch it. Only a raw-.tool_input.command hook can.
#
# *** THE TRAP THIS HOOK MUST NOT FALL INTO (CLAUDE.md says so explicitly, LD-0274): ***
#   "A text `deny` rule is REFUSED: the matcher fires on MENTIONS, so it would forbid every brief
#    and commit message discussing rebase -- including the one reporting this."
#   So: we match the COMMAND FORM (rebase in git's SUBCOMMAND position), never the WORD.
#   `git commit -m "we must never rebase"` MUST PASS. There is a negative control for exactly
#   this in tests/test_never_rules_gate.sh, and it is the most important assertion in the file.
#   For gate 3 text-matching IS correct -- and ONLY there -- precisely because `-F` moves the
#   body OUT of the shell-parsed argument, so the safe path needs no backtick in the command.
#
# OVERRIDE: append an inline marker to the command (audited, like the comp-rail's `# rail-checked:`)
#     # never-override: <reason>
# Bypasses are logged to org/git-author-override-audit.log with the full command.
#
# Block mechanism: JSON on stdout, permissionDecision="deny", exit 0. (Bare exit-2 is treated as
# a hook ERROR, not a block, on current Claude Code -- see block-bare-inbox-watch.sh:19.)

set -uo pipefail

INPUT=$(cat 2>/dev/null || true)
[ -z "$INPUT" ] && exit 0

SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
if [ -x "$SCRIPT_DIR/../jq.exe" ]; then
    JQ="$SCRIPT_DIR/../jq.exe"
elif command -v jq >/dev/null 2>&1; then
    JQ="jq"
else
    exit 0   # jq unavailable -> fail-open pass-through (same posture as the sibling hook)
fi

CMD=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_input.command // empty' 2>/dev/null) || exit 0
[ -z "$CMD" ] && exit 0

WS="${CLAUDE_PROJECT_DIR:-$(cd "$SCRIPT_DIR/../.." 2>/dev/null && pwd)}"
AUDIT="$WS/org/git-author-override-audit.log"
SHARED_BRANCHES='^(CLOUD|DEV|PROD|main|master)$'

deny() {
    "$JQ" -nc --arg r "$1" \
      '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
    exit 0
}

# =========================================================================================
# offending_lines <match-re> <excuse-re>
#   Prints the lines that MATCH <match-re> and are NOT excused by <excuse-re>.
#   Empty output => nothing to block.
#
# *** WHY THIS EXISTS. THE GATE DISARMED ITSELF, AND IT NEARLY COST A LIVE RELEASE. ***
# 2026-07-13: the CTO ran a live probe of the new stash gate. The probe was a multi-line Bash
# command whose ECHO line read:
#     echo "(probe chosen so a DEAD gate is harmless: 'git stash list' would just print ...)"
# The gate matched `git stash push` correctly -- and then evaluated its ALLOWLIST
# (`stash list|show|pop|...`) against the WHOLE COMMAND, found "stash list" INSIDE THE ECHO
# STRING, concluded the call was a read-only form, and PASSED IT.
# `git stash push` then EXECUTED and parked the working tree of EIGHT LIVE AGENTS -- the exact
# incident the gate had been written, minutes earlier, to prevent. (Recovered: 0 files lost.)
#
# >> AN EXCLUSION EVALUATED OVER A WIDER SCOPE THAN THE MATCH IT EXCUSES IS A DISARM VECTOR. <<
# Any text anywhere in the command -- a comment, an echo, a commit message -- could switch the
# gate off. It is the census-by-mention defect (CLAUDE.md Rule 22a) wearing a safety-check's
# clothes: THE MATCH was scoped to the command form, but THE EXCUSE was scoped to the prose.
# The excuse must be scoped to the SAME UNIT as the match. Hence: per-line.
# =========================================================================================
# THE UNIT IS THE SIMPLE COMMAND, NOT THE LINE. Line-scoping was my SECOND wrong answer:
# `git stash push  # we can git stash pop it back` still disarmed the gate, because the excuse
# (`stash pop`) sat on the same LINE -- in a COMMENT. And `git stash push && git stash list`
# would have done the same. So we normalise to one SIMPLE COMMAND per line (split on newline,
# `;`, `&&`, `||`, `|`) and STRIP COMMENTS before evaluating the excuse.
# (The `# never-override:` marker is matched earlier against the RAW command and exits, so
#  comment-stripping here cannot eat it.)
#   >> SCOPE THE EXCUSE TO THE SAME UNIT AS THE MATCH. A wider scope is a disarm vector;
#      "the same line" is still wider than "the same command." <<
# *** AND A HEREDOC BODY IS DATA, NOT COMMANDS. ***
# The gate BLOCKED ITS OWN COMMIT: the commit message -- written via `cat > /tmp/msg <<'EOF' ... EOF`,
# the mandated -F pattern (LD-0276) -- DOCUMENTS the gate, so it contains the words `git clean` and
# `git stash`. A line-based matcher cannot tell a heredoc BODY from a COMMAND, so it fired on the
# prose describing itself.
# That is EXACTLY the failure CLAUDE.md predicted and refused: "the matcher fires on MENTIONS, so it
# would forbid every brief and commit message discussing rebase -- INCLUDING THE ONE REPORTING THIS."
# I avoided it for `rebase` (subcommand-position matching) and walked straight into it for stash/clean.
# So: strip heredoc bodies before matching. Everything between `<<[-]['"]?TAG` and the closing TAG is
# DATA the shell never executes -- and a gate that blocks the documentation of itself gets turned off.
_strip_heredocs() {
    awk '
      { line = $0 }
      inhd {
        if (line ~ ("^[[:space:]]*" tag "[[:space:]]*$")) { inhd = 0 }
        next                      # drop the heredoc BODY and its terminator
      }
      {
        if (match(line, /<<-?[[:space:]]*[\x27"]?[A-Za-z_][A-Za-z0-9_]*[\x27"]?/)) {
          t = substr(line, RSTART, RLENGTH)
          gsub(/^<<-?[[:space:]]*/, "", t); gsub(/[\x27"]/, "", t)
          tag = t; inhd = 1
        }
        print line                # keep the line that OPENS the heredoc (it is a real command)
      }
    '
}
_simple_commands() {
    printf '%s\n' "$CMD" \
      | _strip_heredocs \
      | sed -E 's/#.*$//' \
      | sed -E 's/(\|\||&&|;|\|)/\n/g'
}
offending_lines() {
    _simple_commands | grep -E "$1" | grep -vE "$2"
}

# --- audited override -------------------------------------------------------------------
if printf '%s' "$CMD" | grep -qE '#[[:space:]]*never-override:'; then
    REASON=$(printf '%s' "$CMD" | sed -n 's/.*#[[:space:]]*never-override:[[:space:]]*\(.*\)/\1/p' | head -1)
    {
        printf '%s NEVER-OVERRIDE serial=%s reason=%s cmd=%s\n' \
            "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "${OPAL_AGENT_SERIAL:-UNKNOWN}" "${REASON:-<none>}" "$CMD"
    } >> "$AUDIT" 2>/dev/null || true
    exit 0
fi

# --- resolve the target repo's branch ----------------------------------------------------
# Honour `git -C <path>` so a portal command is judged against portal's branch, not the parent's.
REPO="$WS"
if printf '%s' "$CMD" | grep -qE '(^|[[:space:];|&(])git[[:space:]]+-C[[:space:]]+[^[:space:]]+'; then
    _c=$(printf '%s' "$CMD" | sed -n 's/.*git[[:space:]]\+-C[[:space:]]\+\([^[:space:]]\+\).*/\1/p' | head -1)
    case "$_c" in
        /*) REPO="$_c" ;;
        *)  REPO="$WS/$_c" ;;
    esac
fi
BRANCH=$(git -C "$REPO" rev-parse --abbrev-ref HEAD 2>/dev/null || echo UNKNOWN)

# =========================================================================================
# GATE 1 -- NEVER#7: rebase on a shared branch.
# Match the SUBCOMMAND POSITION, never the word. `git [opts] rebase` / `git [opts] -C x rebase`.
# `git commit -m "...rebase..."` cannot match: the token after git (modulo -flags) is `commit`.
# =========================================================================================
IS_REBASE=0
printf '%s' "$CMD" | grep -qE '(^|[[:space:];|&(])git([[:space:]]+-[^[:space:]]+|[[:space:]]+-C[[:space:]]+[^[:space:]]+)*[[:space:]]+rebase([[:space:]]|$)' && IS_REBASE=1
# `git pull --rebase` (any flag order, up to the next command separator)
printf '%s' "$CMD" | grep -qE '(^|[[:space:];|&(])git([[:space:]]+-[^[:space:]]+|[[:space:]]+-C[[:space:]]+[^[:space:]]+)*[[:space:]]+pull[^;|&]*--rebase' && IS_REBASE=1

if [ "$IS_REBASE" -eq 1 ]; then
    if printf '%s' "$BRANCH" | grep -qE "$SHARED_BRANCHES"; then
        deny "BLOCKED (CLAUDE.md NEVER#7): rebase on the SHARED branch '$BRANCH' ($REPO). Rebase REWRITES multi-agent history -- a non-conflicting result is luck, not correctness, and a silent non-conflicting rebase is INDISTINGUISHABLE from an honest merge, so this gate is the only detector. Rejected push? Use: git pull (merge), then re-push. Legitimate local-only rebase on a scratch branch is NOT blocked (this fired because HEAD is '$BRANCH'). Audited override: append '# never-override: <reason>' to the command."
    fi
    exit 0   # non-shared branch -> a rebase is the author's own business
fi

# `git pull` BARE while pull.rebase=true silently rebases (CLAUDE.md NEVER#7; headmove-guard has pull x0).
if printf '%s' "$CMD" | grep -qE '(^|[[:space:];|&(])git([[:space:]]+-[^[:space:]]+|[[:space:]]+-C[[:space:]]+[^[:space:]]+)*[[:space:]]+pull([[:space:]]|$)'; then
    if ! printf '%s' "$CMD" | grep -qE -- '--no-rebase'; then
        PR=$(git -C "$REPO" config --get pull.rebase 2>/dev/null || echo "")
        if [ "$PR" = "true" ] && printf '%s' "$BRANCH" | grep -qE "$SHARED_BRANCHES"; then
            deny "BLOCKED (CLAUDE.md NEVER#7): 'git pull' on shared branch '$BRANCH' with pull.rebase=true SILENTLY REBASES -- this is the cell nobody types and nobody gated (headmove-guard.sh carries 'pull' x0, and the remedy for a rejected push sends you straight here). Use: git pull --no-rebase. Or fix the config: git config pull.rebase false. Audited override: '# never-override: <reason>'."
        fi
    fi
fi

# =========================================================================================
# GATE 4 -- THE SHARED-WORKTREE BLAST RULE: `git stash` (and `git clean`) park/delete EVERY
# dirty file in the repo -- INCLUDING OTHER AGENTS' UNSAVED WORK.
#
# INCIDENT (2026-07-13, self-reported by 2.0.0_SA_COO -- disclosed before anyone found it):
# to check whether a ruff failure on `.tools/operator.py` was HIS or pre-existing, he ran
# `git stash` to see the file unmodified. It parked **38 FILES**, across DS / AE / CTO lanes,
# during a live release with eight agents writing -- including CTO~B's live gate-1 verdict,
# 0.8.0's emitter test, and 0.7.0's open deploy ledger. (Zero data loss: he measured it
# file-by-file, retained the stash, and correctly refused to restore from it because live
# agents had written NEWER content since.)
#
# *** `stash` IS THE SHARPEST OF THE DESTRUCTIVE VERBS BECAUSE IT *LOOKS* READ-ONLY AND
#     REVERSIBLE, AND IT IS NEITHER. *** `reset`/`rebase` only rewrite YOUR history.
# `stash` silently widens its blast radius to EVERY dirty file in the repo, and its `pop`
# is not guaranteed clean. It is the only one that will happily park another agent's work.
#
# THE CLASS (COO's own framing, and it is the same one that bit six instruments tonight):
#   >> IN A SHARED WORKTREE, ANY COMMAND THAT MUTATES GLOBAL STATE TO ANSWER A LOCAL
#      QUESTION IS A HAZARD. He reached for a MUTATING instrument to answer a READ-ONLY
#      question -- "he used a tool that changes the subject in order to observe the subject."
#
# THE RIGHT INSTRUMENT, and it is what this gate tells you: `git show HEAD:<path>` reads the
# committed vintage WITHOUT TOUCHING THE WORKING TREE AT ALL.
#
# ALLOWED: `git stash list` / `show` (read-only), and `pop` / `apply` / `drop` (the RECOVERY
# path -- never block recovery; same rule as NFRA_IDENTITY G-A direction-2).
# =========================================================================================
_GIT='(^|[[:space:];|&(])git([[:space:]]+-[^[:space:]]+|[[:space:]]+-C[[:space:]]+[^[:space:]]+)*[[:space:]]+'
if [ -n "$(offending_lines "${_GIT}stash([[:space:]]|$)" 'stash[[:space:]]+(list|show|pop|apply|drop|branch|clear)')" ]; then
    if true; then
        deny "BLOCKED (shared-worktree blast rule): 'git stash' PARKS EVERY DIRTY FILE IN THE REPO -- including other agents' UNSAVED WORK. This is a multi-agent tree; on 2026-07-13 one 'git stash' parked 38 files across DS/AE/CTO lanes during a live release (a gate-1 verdict, a test, an OPEN deploy ledger). It LOOKS read-only and reversible and it is NEITHER -- and its 'pop' is not guaranteed clean. IF YOU WANT TO SEE A FILE'S COMMITTED STATE, DO NOT TOUCH THE WORKING TREE: use 'git show HEAD:<path>' (pipe it: git show HEAD:.tools/x.py | ruff check -). IN A SHARED WORKTREE, ANY COMMAND THAT MUTATES GLOBAL STATE TO ANSWER A LOCAL QUESTION IS A HAZARD. (stash list/show/pop/apply/drop are NOT blocked -- read + recovery are fine.) Audited override: '# never-override: <reason>'."
    fi
fi

# `git clean` DELETES untracked files -- i.e. another agent's not-yet-committed new work.
# Strictly worse than stash: there is no stash to pop it back from.
# Dry-run detection must accept a COMBINED short-flag cluster (`-nd`, `-dn`), not just a standalone
# `-n`. My first version matched only `-n` and therefore DENIED `git clean -nd` -- i.e. it blocked
# "LOOK BEFORE YOU DELETE", the exact safe behaviour this gate wants to encourage. A guard that
# punishes the cautious form pushes people to the destructive one. (Caught by the test's PASS arm;
# every DENY arm was green and it would have shipped.) Excuse is LINE-SCOPED, per offending_lines.
if [ -n "$(offending_lines "${_GIT}clean([[:space:]]|$)" '(^|[[:space:]])(-[a-zA-Z]*n[a-zA-Z]*|--dry-run)([[:space:]]|$)')" ]; then
    if true; then
        deny "BLOCKED (shared-worktree blast rule): 'git clean' DELETES UNTRACKED FILES -- in a multi-agent tree that is another agent's not-yet-committed NEW work, and unlike 'git stash' there is NO stash to pop it back from. It is unrecoverable. Dry-run ('git clean -n') is NOT blocked -- look first. If you must delete specific files, name them explicitly with rm. Audited override: '# never-override: <reason>'."
    fi
fi

# =========================================================================================
# GATE 2 -- NEVER#3: bare `terraform apply` / `terraform destroy`.
# There is NO terraform PATH shim (.tools/terraform is the real PE binary) and .tools/ is on
# PATH -- so this has been running straight through. safe-apply / safe-destroy carry the
# HALTGT checkpoint; a bare apply skips it entirely.
# =========================================================================================
# LINE-SCOPED excuse (see offending_lines): a bare `terraform apply` on one line was previously
# excused by the string "safe-apply" appearing ANYWHERE else in the command -- a comment, an echo,
# even a message explaining why the apply was unsafe. Same disarm vector as the stash gate.
if [ -n "$(offending_lines '(^|[[:space:];|&(/\\])(terraform(\.exe)?)[[:space:]]+(apply|destroy)([[:space:]]|$)' 'safe-apply|safe-destroy')" ]; then
    if true; then
        deny "BLOCKED (CLAUDE.md NEVER#3): bare 'terraform apply/destroy'. Use .tools/safe-apply.sh (or safe-destroy.sh) -- it carries the HALTGT inbox checkpoint at the last reversible moment, plus the pre-apply drift-plan check and the write-without-read paired-permission lint (Rule 22a). A bare apply skips ALL of it. NOTE: there is no terraform PATH shim -- .tools/terraform is the real binary on PATH, so nothing else stops this. Audited override: '# never-override: <reason>'."
    fi
fi

# =========================================================================================
# GATE 3 -- LD-0276: a commit message is an EXECUTION VECTOR.
# A double-quoted -m "..." is shell-evaluated BEFORE git or safe-commit sees it, so a backtick
# or $( in the body RUNS with your permissions and splices its stdout into the immutable record.
# A safe-commit lint CANNOT catch this (the substitution already happened). Only a raw-command
# hook can. Text-matching is correct HERE and nowhere else, precisely because -F moves the body
# OUT of the shell-parsed argument -- so the safe path needs no backtick in the command at all.
# =========================================================================================
if printf '%s' "$CMD" | grep -qE '(^|[[:space:];|&(/\\])(git([[:space:]]+-[^[:space:]]+|[[:space:]]+-C[[:space:]]+[^[:space:]]+)*[[:space:]]+commit|safe-commit(\.sh)?)([[:space:]]|$)'; then
    if printf '%s' "$CMD" | grep -qE -- '(^|[[:space:]])-m([[:space:]]|=)'; then
        if printf '%s' "$CMD" | grep -qE '`|\$\('; then
            deny "BLOCKED (CLAUDE.md Git / LD-0276): 'git commit -m' carrying a backtick or \$( -- A COMMIT MESSAGE IS AN EXECUTION VECTOR. The substitution is performed by the SHELL before git or safe-commit ever sees the argument, so it RUNS with your permissions and splices its stdout into the immutable record -- and a safe-commit lint structurally cannot catch it. Use -F instead: write the body to a file (heredoc -> file), then: safe-commit.sh --author \"...\" -F <file> -- <paths>. -F routes the body into a file the shell never parses, so the safe path needs no backtick in the command at all. (Yes, -m \"\$(cat <<'EOF'...)\" is technically inert -- it is still deprecated, because verifying it requires shell parsing and mandating -F makes the gate parse-free.) Audited override: '# never-override: <reason>'. Incident: MSTR corrupted 11c44632b writing the finding about this very hazard."
        fi
    fi
fi

exit 0
