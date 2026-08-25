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
    # jq unavailable -> FAIL CLOSED, LOUD. This gate is CLAUDE.md's "only
    # detector" for a silent rebase on a shared branch; a gate that cannot run
    # must deny, not silently pass (exercised 2026-07-29: with jq hidden, a
    # `git rebase origin/CLOUD` returned rc=0 with NO OUTPUT at site Z).
    # Remedy is one step and stated below; jq.exe is also tracked in-repo now
    # (.gitignore negation), so a current clone should never hit this branch.
    echo "BLOCKED: never-rules-gate cannot run -- jq not found at .tools/jq.exe or on PATH." >&2
    echo "This security gate FAILS CLOSED. Fix: git checkout .tools/jq.exe (tracked) or install jq, then retry." >&2
    exit 2
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
# GATE 0 -- bare-path inbox-watch launch (MERGED IN from block-bare-inbox-watch.sh,
# Andrew cleanup 2026-07-30 / MSTR low-level audit: both hooks matched Bash|PowerShell and
# each cost one MSYS bash spawn per tool call; the check is one grep, so it rides this gate
# and settings.json drops the separate entry. The standalone script is left on disk,
# unchanged, for in-flight sessions still carrying the old hook config -- remove it only
# after those sessions cycle.) Semantics preserved verbatim from the original: raw-command
# grep (no heredoc/quote stripping -- a relative launch is the hazard wherever it appears),
# same deny reason, same derived-not-hardcoded remedy path. One deliberate strengthening:
# the original passed silently when jq was missing; this file FAILS CLOSED on missing jq
# for every gate, which is strictly safer and jq.exe is tracked in-repo.
# =========================================================================================
if printf '%s' "$CMD" | grep -qE '(^|[[:space:];|&(])([a-z0-9_./-]*/)?(bash|sh)[[:space:]]+org/mcp/inbox-watch\.sh'; then
    deny "BLOCKED: relative-path inbox-watch.sh invocation. Use the canonical PATH wrapper \"inbox-watch <serial>\" or absolute path \"bash ${WS:-<your-clone-root>}/org/mcp/inbox-watch.sh <serial>\". Relative-path launches propagate bare-path \$0 into auto-respawn children, creating PPID=1 zombies that survive session death and short-circuit future tracked launches via the single-watcher guard (Claude Code surfaces guard-exit-0 as misleading exit 143). See org/XXX.md Step 1b / org/mcp/INBOX_WATCH_DESIGN.md."
fi

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
# ALSO honour a leading `cd <path> && git ...` -- the SUBMODULE shape (MSTR/DT finding 2026-08-11:
# `cd portal && git push origin DEV` resolved $BRANCH from the OUTER repo's HEAD, so the denial text
# named the wrong branch. Harmless that night because BOTH branches were shared -- but the INVERSE is
# the hazard: outer on a SCRATCH branch + a shared-branch push from inside the submodule would not
# have fired at all. A gate that reads the wrong repo is silently absent exactly where LD-0367 needs it.
elif printf '%s' "$CMD" | grep -qE '(^|[[:space:];|&(])cd[[:space:]]+[^[:space:]]+[[:space:]]*(&&|;)'; then
    _c=$(printf '%s' "$CMD" | sed -n 's/.*[^[:alnum:]_-]\?cd[[:space:]]\+\([^[:space:];&|]\+\).*/\1/p' | head -1)
    case "$_c" in
        /*) [ -d "$_c/.git" ] || [ -f "$_c/.git" ] && REPO="$_c" ;;
        "") : ;;
        *)  { [ -d "$WS/$_c/.git" ] || [ -f "$WS/$_c/.git" ]; } && REPO="$WS/$_c" ;;
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
# F-XXX (2026-08-05): the option-consumer must handle EVERY git global option that takes its
# value as a SEPARATE ARGV TOKEN -- not just `-C <path>`. A two-token option whose value is not
# consumed strands the regex before the verb, so the WHOLE COMMAND becomes invisible to all five
# gates built on _GIT (rebase, bare-pull-under-pull.rebase=true, stash, clean, integrator push/pull).
# Found by 2.0.0_SA_COO, who hit the `-c` cell live and self-disclosed; CTO re-derived at source and
# WIDENED it -- `-c` was 1 of 5 cells. Measured: `--git-dir`, `--work-tree`, `--namespace`,
# `--config-env` all accept a space-separated value too, and `git --git-dir .git rebase` evaded the
# `-c`-only fix. THE LIST IS A PREDICATE OVER GIT'S OWN `git --help` USAGE LINE, not a hand-drawn
# roster -- re-derive it against that usage on any git-version bump (see tests, DERIVATION CHECK).
# `--exec-path` is DELIBERATELY EXCLUDED: its value is optional, and the valueless form is TERMINAL
# (prints the path, never runs a verb) -- listing it here would let it SWALLOW a real verb and turn
# this fix into a false-negative.
# TWO DIFFERENT EXCLUSIONS ON TWO DIFFERENT GROUNDS -- kept apart deliberately (CVO L7, 2026-08-05:
# folded into one sentence, the solid half lends its credibility to the half that is merely asserted):
#   (a) ATTACHED SHORT `-cKEY=VAL` -- excluded because GIT ITSELF REFUSES IT (rc=129, "unknown
#       option"), an EXTERNAL oracle. Re-exercised independently by CVO on git 2.55.0.windows.2.
#       VERSION-SCOPED: rc=129 is that git's behaviour and re-opens on a git bump, which is why the
#       probe rides the DERIVATION CHECK's trigger in the fixture rather than being tracked apart.
#   (b) ATTACHED LONG `--git-dir=.git` -- git ACCEPTS this (rc=0); it is a real, reachable command.
#       It is excluded from _O2 ONLY because _O1 catches it. Ground = THIS REGEX, not git's
#       behaviour -- an assertion, so it is TESTED (fixture arm "F-XXX --git-dir= single-token").
_O2='[[:space:]]+(-c|-C|--git-dir|--work-tree|--namespace|--config-env|--super-prefix)[[:space:]]+[^[:space:]]+'
_O1='[[:space:]]+-[^[:space:]]+'
_GIT="${_LEAD}"'git('"${_O2}"'|'"${_O1}"')*[[:space:]]+'
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
        deny "BLOCKED (CLAUDE.md NEVER#7): 'git pull' on shared branch '$BRANCH' with pull.rebase=true SILENTLY REBASES -- this is the cell nobody types and nobody gated (headmove-guard.sh carries 'pull' x0, and the remedy for a rejected push sends you straight here). Use: git pull --no-rebase. Or fix the config by running 'git config pull.rebase false' AS ITS OWN SEPARATE COMMAND -- do NOT inline it as 'git -c pull.rebase=false pull' (F-XXX: the inline one-shot was the shape that EVADED this gate until 2026-08-05; it is gated now, but the standalone form is the one to reach for). Audited override: '# never-override: <reason>'."
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

        # TOKEN ATTRIBUTION (CTO gate-shape repair 2026-08-25, on COO 67279's false-positive
        # report: a record ABOUT the hazard was denied for DESCRIBING it, and the deny named
        # nothing -- the seat had to guess which prose token tripped which regex). The MATCHER
        # IS DELIBERATELY UNCHANGED: the in-file F-021 record above forbids the per-command
        # "fix" (it executed a real commit message), and the error-direction trade stands.
        # What changes is that the deny now NAMES the first line matching each of the three
        # co-occurring tokens, so a false positive costs seconds to restructure, not minutes
        # to diagnose -- a gate that explains itself is a gate that gets obeyed, not routed
        # around.
        _g3_a="$(printf '%s
' "$_CMD_NOHEREDOC" | grep -nE -- "$_RE_COMMIT" | head -1 | cut -c1-160)"
        _g3_b="$(printf '%s
' "$_CMD_NOHEREDOC" | grep -nE -- "$_RE_DASH_M" | head -1 | cut -c1-160)"
        _g3_c="$(printf '%s
' "$_CMD_NOHEREDOC" | grep -nE -- "$_RE_META"   | head -1 | cut -c1-160)"
        echo "  [gate3] co-occurring tokens (line:text, heredocs already stripped):" >&2
        echo "  [gate3]   commit-token -> ${_g3_a:-<none>}" >&2
        echo "  [gate3]   -m token     -> ${_g3_b:-<none>}" >&2
        echo "  [gate3]   metachar     -> ${_g3_c:-<none>}" >&2
        if true; then
            deny "BLOCKED (CLAUDE.md Git / LD-0276): 'git commit -m' carrying a backtick or \$( -- A COMMIT MESSAGE IS AN EXECUTION VECTOR. The substitution is performed by the SHELL before git or safe-commit ever sees the argument, so it RUNS with your permissions and splices its stdout into the immutable record -- and a safe-commit lint structurally cannot catch it. Use -F instead: write the body to a file (heredoc -> file), then: safe-commit.sh --author \"...\" -F <file> -- <paths>. -F routes the body into a file the shell never parses, so the safe path needs no backtick in the command at all. (Yes, -m \"\$(cat <<'EOF'...)\" is technically inert -- it is still deprecated, because verifying it requires shell parsing and mandating -F makes the gate parse-free.) Audited override: '# never-override: <reason>'. Incident: MSTR corrupted 11c44632b writing the finding about this very hazard."
        fi
    fi
fi

# =========================================================================================
# GATE 5 -- LD-0367 rule 2 / LD-0368: INTEGRATOR-ONLY push+pull on a SHARED branch.
# Only 0.0.0_AB_MSTR (base) and 0.0.0_AB_MSTR~Z (site-Z) -- the two integration-window
# integrators -- may `git push` or `git pull` a shared branch. Every other seat commits to a
# SEAM and lets the hourly window (LD-0367) move it.
#
# WHY (proven, integration-window #1, 2026-07-31, measured not confessed): a seat that pushes
# early PUBLISHES EVERY OTHER SEAT'S LOCAL COMMITS with its own -- CTO~Z's push carried MSTR~Z's
# held commit (MSTR~Z's 380192d3d was an ancestor of CTO~Z's HEAD). Neither party chooses it and
# the pusher cannot see what it carried. "just this one push" is therefore never local. A gate,
# not a convention, because the violation is INVISIBLE to the violator.
#
# SCOPE, deliberately narrow, three ways:
#   - `git fetch` is NOT blocked (LD-0367 rule 4: everyone fetches-by-hash mid-hour).
#   - SHARED branches only (CLOUD/DEV/PROD/main/master); a scratch branch is the worker's own.
#   - rebase-pull is already denied for EVERYONE by GATE 1 above (it runs first and exits).
#
# IDENTITY, fail-closed: the caller's serial comes from THIS call's own session_id (hook input
# JSON -> LD-0290's per-session serial file, the reliable source; the SHARED .agent_context is
# not), then $OPAL_AGENT_SERIAL. If it does not POSITIVELY resolve to an integrator MSTR, the
# push/pull is DENIED. A false-deny is loud and the integrator fixes it in one step; a false-allow
# silently republishes the whole tree -- so UNRESOLVED FAILS TO DENY, never to allow.
# =========================================================================================
# TWO TRIGGERS, NOT ONE (CTO 2026-08-11, closing the wrong-repo/explicit-refspec hole):
#   (a) HEAD is a shared branch (the original), now resolved against the TARGET repo; and
#   (b) THE COMMAND ITSELF NAMES A SHARED BRANCH -- `git push origin DEV` / `HEAD:CLOUD` /
#       `refs/heads/main` -- regardless of what HEAD is.
# (b) is the structural half: HEAD is an INFERENCE about what the command will move, the refspec
# is the command SAYING IT. It closes two silent-absence cases (a) alone cannot see: a shared-branch
# push from inside a submodule while the outer repo sits on a scratch branch, and the plainer
# `git push origin CLOUD` issued from any scratch branch in the workspace itself.
_RE_PUSHPULL="${_GIT}"'(push|pull)([[:space:]]|$)'
_PUSHPULL_HIT="$(scan PUSHPULL_AUTHORITY '' "$_RE_PUSHPULL")"
_REF_NAMES_SHARED=""
if [ -n "$_PUSHPULL_HIT" ]; then
    # A COMMENT IS NOT A REFSPEC -- strip it first, exactly as `scan` does for matching
    # (`git push origin scratch  # rebase onto DEV later` must not read as a DEV push).
    # Then tokenise; strip refs/heads/, origin/, and the src: half of a src:dst refspec.
    _REF_NAMES_SHARED="$(printf '%s' "$_PUSHPULL_HIT" | sed -E 's/#.*$//' | tr ' \t' '\n\n' \
        | sed -e 's#^refs/heads/##' -e 's#^.*:##' -e 's#^origin/##' \
        | grep -E -- "$SHARED_BRANCHES" | head -1)"
fi
if [ -n "$_PUSHPULL_HIT" ] \
   && { printf '%s' "$BRANCH" | grep -qE -- "$SHARED_BRANCHES" || [ -n "$_REF_NAMES_SHARED" ]; }; then
    [ -n "$_REF_NAMES_SHARED" ] && BRANCH="${_REF_NAMES_SHARED}"
    _SID=$(printf '%s' "$INPUT" | "$JQ" -r '.session_id // empty' 2>/dev/null)
    _CALLER=""
    [ -n "$_SID" ] && _CALLER=$(tr -d '[:space:]' < "$WS/org/mcp/sessions/${_SID}.serial" 2>/dev/null || true)
    [ -z "$_CALLER" ] && _CALLER="${OPAL_AGENT_SERIAL:-}"
    if ! printf '%s' "$_CALLER" | grep -qE -- '^0\.0\.0_AB_MSTR(~[A-Za-z0-9]+)?$'; then
        deny "BLOCKED (LD-0367 rule 2 / LD-0368 -- INTEGRATOR-ONLY push/pull on shared branch '$BRANCH'): only 0.0.0_AB_MSTR (base) / 0.0.0_AB_MSTR~Z (site-Z) may push or pull the shared branch; you are '${_CALLER:-UNRESOLVED}'. WHY: a push from any other seat PUBLISHES EVERY OTHER SEAT'S LOCAL COMMITS along with yours -- neither of you chooses it and you cannot see what you carried (proven integration-window #1, 2026-07-31: a seat's push carried the site-Z integrator's held commit). Commit your work to a SEAM; the hourly INTEGRATION WINDOW (LD-0367) moves it -- the integrator MSTR runs the pull+push. 'git fetch' (incl. fetch-by-hash, LD-0367 rule 4) is NOT blocked. A scratch branch is your own business (this fired because HEAD is the shared '$BRANCH'). Audited override (rare -- coordinate with the integrator FIRST, because it still republishes the tree): append '# never-override: <reason>' to the SAME simple command."
    fi
fi

exit 0
