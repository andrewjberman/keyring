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
# NEVER_GATE_AUDIT lets the TEST SUITE route its override records to a scratch file. Without it the
# suite appends to the governance log on every run -- and OVERRIDE_REVIEW (the instrument MSTR is
# required to walk every review) then reads its own test fixtures as real overrides. An instrument
# whose test suite poisons its evidence base, append-only, cannot be audited. (RV-0048 F-020.)
AUDIT="${NEVER_GATE_AUDIT:-$WS/org/git-author-override-audit.log}"
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

# =========================================================================================
# *** RV-0048 F-019: THE OVERRIDE MARKER WAS A UNIVERSAL DISARM. ***
# The marker used to be grepped against the WHOLE COMMAND, ahead of every rule, with an
# unconditional `exit 0`. So ONE occurrence of that text ANYWHERE -- a comment on an unrelated
# line, a quoted string inside an echo, a commit message -- waived rebase AND pull AND stash AND
# clean AND terraform AND commit-msg. All of them. Exercised by MSTR with an isolated control:
#   CONTROL  `terraform apply` + `git stash push`, no marker                      -> DENY
#   BROKEN   the SAME two hazards + `# never-override: scratch cleanup` on a
#            DIFFERENT line (authorizing a scratch REBASE, not these)             -> PASS
#   BROKEN   a real `git stash push`, marker merely QUOTED INSIDE AN ECHO         -> PASS
# An agent legitimately overriding ONE thing silently waived the terraform and stash gates.
#
# >> IT IS THIS FILE'S OWN RULE, ONE LEVEL UP. << The comment 40 lines above says: "AN EXCLUSION
# EVALUATED OVER A WIDER SCOPE THAN THE MATCH IT EXCUSES IS A DISARM VECTOR -- scope the excuse to
# the same unit as the match; the unit is the SIMPLE COMMAND." I applied that to the stash/clean
# ALLOWLIST and did not apply it to the MARKER -- which is the maximal exclusion in the file, the
# one that excuses EVERY match. *** KNOWING A FAILURE MODE BY NAME DOES NOT IMMUNIZE YOU AGAINST
# WRITING IT *** (CLAUDE.md Rule 22a, landed by me, hours before I shipped this).
#
# THE FIX: the marker is now evaluated PER SIMPLE COMMAND, exactly like every other excuse.
# A marker on the `git rebase` line excuses THAT rebase and NOTHING ELSE; a `terraform apply` on
# the next line still denies. There is no whole-command pre-emptive exit.
#
# AND F-020: the audit log now records an override ONLY when the marker actually SUPPRESSED A REAL
# MATCH. It used to write a NEVER-OVERRIDE record on every MENTION -- census-by-mention wearing an
# audit trail's clothes, on the append-only log that OVERRIDE_REVIEW reads as its evidence base.
# =========================================================================================
OVERRIDE_RE='#[[:space:]]*never-override:'

# Simple commands with COMMENTS PRESERVED -- the marker lives in a comment, so it must survive the
# split. (Comments are stripped per-command below, AFTER the marker is read off the raw text.)
# *** A QUOTED STRING IS DATA, NOT COMMANDS. *** The command-form gates (rebase / terraform / stash /
# clean) must not see inside one -- and, crucially, must not SPLIT inside one.
#   grep -oE 'rebase|terraform apply|git stash' CLAUDE.md
# The `|` characters are INSIDE A QUOTED REGEX. Splitting on them tore the command into fragments,
# and `terraform apply` became a FRAGMENT WHOSE FIRST TOKEN IS `terraform` -- a command that never
# existed. The gate DENIED A CENSUS OF ITSELF. Same root as `echo "...terraform apply; use
# safe-apply"`, where the `;` inside the quotes split the MATCH away from its EXCUSE.
# So: blank the CONTENTS of quoted strings before splitting. The quotes and the surrounding command
# structure survive; only the data inside them is neutralised.
# NOTE: GATE 3 (commit -m + metachar) does NOT use this -- it must see INSIDE the `-m` body, because
# the body is exactly what the shell will evaluate. Different question, different scope.
# ACCEPTED RESIDUAL: `bash -c "git rebase"` evades this. It is a deliberate trade -- the alternative
# is a gate that blocks every brief, census and echo discussing the hazard, and CLAUDE.md is explicit
# that such a gate SHIPS OFF. A gate nobody can work next to gets disabled, and then protects nothing.
_strip_quoted() {
    sed -E "s/'[^']*'/'Q'/g; s/\"[^\"]*\"/\"Q\"/g"
}
_simple_commands_raw() {
    printf '%s\n' "$CMD" \
      | _strip_heredocs \
      | _strip_quoted \
      | sed -E 's/(\|\||&&|;|\|)/\n/g'
}

audit_override() {   # <rule> <the simple command that carried the marker>
    local reason
    reason=$(printf '%s' "$2" | sed -n 's/.*#[[:space:]]*never-override:[[:space:]]*\(.*\)/\1/p' | head -1)
    {
        printf '%s NEVER-OVERRIDE serial=%s rule=%s reason=%s cmd=%s\n' \
            "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "${OPAL_AGENT_SERIAL:-UNKNOWN}" \
            "$1" "${reason:-<none>}" "$2"
    } >> "$AUDIT" 2>/dev/null || true
}

# scan <rule> <excuse-re|""> <match-re>...
#   Prints the SIMPLE COMMANDS where EVERY <match-re> matches (all on that one command), which are
#   not excused by <excuse-re>, and which do not carry the override marker.
#   A marker on the SAME simple command suppresses THAT command only, and is AUDITED as a real
#   override. Empty output => nothing to block.
#   Requiring all match-res to hit ONE simple command is what stops three independent whole-command
#   greps ("git commit" here, "-m" there, "$(" in an unrelated echo) from conspiring into a verdict.
scan() {
    local rule="$1" excuse="$2"; shift 2
    local sc code re ok
    while IFS= read -r sc; do
        printf '%s' "$sc" | grep -qE -- '[^[:space:]]' || continue
        code=$(printf '%s' "$sc" | sed -E 's/#.*$//')     # a comment is not a command
        ok=1
        for re in "$@"; do
            printf '%s' "$code" | grep -qE -- "$re" || { ok=0; break; }
        done
        [ "$ok" -eq 1 ] || continue
        if [ -n "$excuse" ] && printf '%s' "$code" | grep -qE -- "$excuse"; then continue; fi
        if printf '%s' "$sc" | grep -qE -- "$OVERRIDE_RE"; then
            audit_override "$rule" "$sc"
            continue
        fi
        printf '%s\n' "$sc"
    done < <(_simple_commands_raw)
}

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
# =========================================================================================
# *** COMMAND POSITION, NOT "ANYWHERE IN THE TEXT". THE NEGATIVE CONTROL WAS RED AND CLAUDE.md
#     SAYS A RED NEGATIVE CONTROL SHIPS THE GATE OFF. (COO, exercised, 2026-07-13.) ***
#
#     echo "the rule forbids bare terraform apply; use safe-apply"   -> WAS DENIED
#     echo "NEVER#7 forbids git rebase on shared branches"           -> WAS DENIED
#     grep -oE 'rebase|terraform apply'   (a CENSUS OF THE GATE)     -> WAS DENIED
#   The command is `echo`. There is NO terraform and NO git invocation in any of them.
#   *** THE GATE WAS BLOCKING THE BRIEF THAT REPORTS THE HAZARD *** -- the one thing CLAUDE.md
#   refuses outright ("a gate that blocks the brief reporting the hazard is worse than no gate").
#
# TWO CAUSES, ONE ROOT -- I MATCHED THE WORD, NOT THE COMMAND:
#   (a) `_GIT` matched `git ... rebase` ANYWHERE in the text, INCLUDING INSIDE A QUOTED STRING.
#   (b) `_simple_commands()` splits on `;` -- INCLUDING A `;` INSIDE QUOTES -- so
#       `echo "... terraform apply; use safe-apply"` tore into a fragment holding the MATCH and a
#       fragment holding the EXCUSE. The match survived; its excuse did not.
#   CLAUDE.md said, from the beginning: *"match the SUBCOMMAND POSITION, NEVER THE WORD."*
#   I wrote a rule about command position and then implemented a substring search.
#
# THE FIX: the command must be the FIRST TOKEN of its simple command. `echo "git rebase"` has
# first token `echo` -> no match. `git rebase -i` has first token `git` -> match. `cd x && git
# rebase` splits, and fragment 2's first token is `git` -> match. Leading env-assignments, an
# interpreter (`bash`/`sh`/`env`/`command`), and shell keywords (`then`/`do`/`else`/`{`) are
# skipped so `if ...; then git rebase; fi` still catches.
# =========================================================================================
_LEAD='^[[:space:]]*(([A-Za-z_][A-Za-z0-9_]*=[^[:space:]]*|bash|sh|env|command|then|do|else|elif|\{|\()[[:space:]]+)*'
_GIT="${_LEAD}"'git([[:space:]]+-[^[:space:]]+|[[:space:]]+-C[[:space:]]+[^[:space:]]+)*[[:space:]]+'
# `git rebase`, or `git pull ... --rebase` (any flag order, up to the next command separator).
_RE_REBASE="${_GIT}"'(rebase([[:space:]]|$)|pull[^;|&]*--rebase)'
_RE_PULL="${_GIT}"'pull([[:space:]]|$)'

# *** NO EARLY `exit 0` HERE. IT WAS A SECOND DISARM VECTOR, AND NOBODY NAMED IT (CTO, self-found
# while fixing F-019). The old code did:
#       if IS_REBASE; then  (deny if shared);  exit 0  # "a scratch rebase is your own business"
# -- and that `exit 0` returned from THE WHOLE HOOK, skipping the stash, clean, terraform and
# commit-msg gates. So on a scratch branch, `git rebase -i HEAD~1 && terraform apply` sailed
# straight past the terraform gate. The rebase verdict is a verdict about the REBASE; it must never
# be a verdict about the rest of the command. Same class as F-019 through a different door:
# A CONTROL-FLOW SHORTCUT IS AN EXCLUSION TOO, AND IT WAS SCOPED TO THE WHOLE COMMAND. ***
if printf '%s' "$BRANCH" | grep -qE -- "$SHARED_BRANCHES"; then
    if [ -n "$(scan REBASE '' "$_RE_REBASE")" ]; then
        deny "BLOCKED (CLAUDE.md NEVER#7): rebase on the SHARED branch '$BRANCH' ($REPO). Rebase REWRITES multi-agent history -- a non-conflicting result is luck, not correctness, and a silent non-conflicting rebase is INDISTINGUISHABLE from an honest merge, so this gate is the only detector. Rejected push? Use: git pull (merge), then re-push. Legitimate local-only rebase on a scratch branch is NOT blocked (this fired because HEAD is '$BRANCH'). Audited override: append '# never-override: <reason>' to the SAME simple command."
    fi

    # `git pull` BARE while pull.rebase=true silently rebases (NEVER#7; headmove-guard has pull x0).
    PR=$(git -C "$REPO" config --get pull.rebase 2>/dev/null || echo "")
    if [ "$PR" = "true" ] && [ -n "$(scan PULL_REBASE_CFG '--no-rebase' "$_RE_PULL")" ]; then
        deny "BLOCKED (CLAUDE.md NEVER#7): 'git pull' on shared branch '$BRANCH' with pull.rebase=true SILENTLY REBASES -- this is the cell nobody types and nobody gated (headmove-guard.sh carries 'pull' x0, and the remedy for a rejected push sends you straight here). Use: git pull --no-rebase. Or fix the config: git config pull.rebase false. Audited override: '# never-override: <reason>'."
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
if [ -n "$(scan STASH 'stash[[:space:]]+(list|show|pop|apply|drop|branch|clear)' "${_GIT}"'stash([[:space:]]|$)')" ]; then
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
if [ -n "$(scan CLEAN '(^|[[:space:]])(-[a-zA-Z]*n[a-zA-Z]*|--dry-run)([[:space:]]|$)' "${_GIT}"'clean([[:space:]]|$)')" ]; then
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
# COMMAND-POSITION anchored, same as the git gates and for the same reason: the unanchored version
# DENIED `echo "the rule forbids bare terraform apply; use safe-apply"` and even a `grep -oE
# 'terraform apply'` CENSUS OF THE GATE ITSELF. The `;` inside the quoted string also split the
# MATCH away from its EXCUSE. A leading path is allowed (`./.tools/terraform.exe apply`).
_RE_TF="${_LEAD}"'([^[:space:]]*[/\\])?(terraform(\.exe)?)[[:space:]]+(apply|destroy)([[:space:]]|$)'
if [ -n "$(scan TERRAFORM 'safe-apply|safe-destroy' "$_RE_TF")" ]; then
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
# RV-0048 F-021: these three conditions used to be THREE INDEPENDENT WHOLE-COMMAND GREPS, so they
# did not have to co-occur on the same command to convict. A perfectly safe `-F` commit sitting next
# to an unrelated `echo "the id is $(id)"` supplied `git commit` from one line, `-m`... from wherever,
# and `$(` from the echo -- and got DENIED. It fails CLOSED, so it was never a hole; but it blocks the
# brief reporting the hazard, which is the ONE thing CLAUDE.md refuses ("the matcher fires on MENTIONS
# ... including the one reporting this"), and it made the cell inline-untestable.
# Now all three must hit ONE simple command -- which is exactly what a real `git commit -m "... $(id)"`
# does, and what prose about it does not.
_RE_COMMIT='(^|[[:space:];|&(/\\])(git([[:space:]]+-[^[:space:]]+|[[:space:]]+-C[[:space:]]+[^[:space:]]+)*[[:space:]]+commit|safe-commit(\.sh)?)([[:space:]]|$)'
_RE_DASH_M='(^|[[:space:]])-m([[:space:]]|=)'
_RE_META='`|\$\('
# =========================================================================================
# *** GATE 3 IS DELIBERATELY **WHOLE-COMMAND** SCOPED. DO NOT "FIX" IT TO PER-SIMPLE-COMMAND. ***
#
# It WAS per-simple-command for ~6 hours on 2026-07-13 (my own F-021 change) and THAT CREATED A
# HOLE THAT EXECUTED A REAL COMMIT MESSAGE. `_simple_commands()` splits on NEWLINES -- and a `-m`
# body is a SINGLE SHELL ARGUMENT THAT SPANS NEWLINES. So a multi-line message is torn apart:
#     git commit -m "fix: the selector          <- fragment 1: has `commit` + `-m`, NO metachar
#     `any(t in src ...)` was the bug"          <- fragment 2: has the metachar, NO `commit`
# Neither fragment carries all three, so the gate PASSED IT. Exercised:
#     single-line -m + backtick   -> DENY      (the only case I tested when I made the change)
#     multi-line  -m + backtick   -> PASS      *** THE HOLE ***
# 0.4.0_DS_ClientPlatform~A then executed his own commit message (49fe7b0e4): the shell evaluated
# the backticks BEFORE git or safe-commit saw the string, the substitution failed, and bash spliced
# its EMPTY output in -- DELETING A CLAUSE FROM THE IMMUTABLE RECORD. He had read the rule that
# morning and followed it four times. The gate was the only thing that could have caught the fifth,
# and I had broken it.
#
# >> I TRADED A FALSE POSITIVE FOR A FALSE NEGATIVE, AND THE FALSE NEGATIVE IS THE DIRECTION THAT
#    EXECUTES CODE. <<  The F-021 false positive (a SAFE `-m` commit denied because an UNRELATED
# `echo "$(id)"` sits elsewhere in the command) is ANNOYING and FAILS CLOSED. This hole is SILENT
# and RUNS ARBITRARY CODE with the agent's permissions, into a record that cannot be corrected.
# *** WHEN THE TWO ERROR DIRECTIONS ARE "ANNOYING" AND "EXECUTES CODE", YOU CHOOSE ANNOYING. ***
# And the remedy for the false positive costs nothing: USE `-F`. That is the mandated path anyway
# (LD-0276), and a `-F` body is not shell-parsed, so it needs no metachar in the command at all.
#
# HEREDOC BODIES ARE STILL STRIPPED (see _strip_heredocs), so the mandated
# `cat > msg <<'EOF' ... EOF; safe-commit -F msg` pattern -- even when the message DOCUMENTS this
# very hazard and contains backticks -- still PASSES. That is the case that must never break.
# =========================================================================================
_CMD_NOHEREDOC=$(printf '%s\n' "$CMD" | _strip_heredocs)
if printf '%s' "$_CMD_NOHEREDOC" | grep -qE -- "$_RE_COMMIT" \
   && printf '%s' "$_CMD_NOHEREDOC" | grep -qE -- "$_RE_DASH_M" \
   && printf '%s' "$_CMD_NOHEREDOC" | grep -qE -- "$_RE_META"; then
    if ! printf '%s' "$CMD" | grep -qE -- "$OVERRIDE_RE"; then
        if true; then
            deny "BLOCKED (CLAUDE.md Git / LD-0276): 'git commit -m' carrying a backtick or \$( -- A COMMIT MESSAGE IS AN EXECUTION VECTOR. The substitution is performed by the SHELL before git or safe-commit ever sees the argument, so it RUNS with your permissions and splices its stdout into the immutable record -- and a safe-commit lint structurally cannot catch it. Use -F instead: write the body to a file (heredoc -> file), then: safe-commit.sh --author \"...\" -F <file> -- <paths>. -F routes the body into a file the shell never parses, so the safe path needs no backtick in the command at all. (Yes, -m \"\$(cat <<'EOF'...)\" is technically inert -- it is still deprecated, because verifying it requires shell parsing and mandating -F makes the gate parse-free.) Audited override: '# never-override: <reason>'. Incident: MSTR corrupted 11c44632b writing the finding about this very hazard."
        fi
    fi
fi

exit 0
