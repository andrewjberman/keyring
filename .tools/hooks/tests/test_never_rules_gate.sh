#!/usr/bin/env bash
# Exercise never-rules-gate.sh. Rule 22a: acceptance rests on the gate FIRING/PASSING, not on
# reading it. Feeds real PreToolUse JSON on stdin and asserts DENY vs PASS.
#
# THE MOST IMPORTANT ASSERTIONS IN THIS FILE ARE THE NEGATIVE CONTROLS.
# CLAUDE.md refuses a text `deny` rule for rebase precisely because "the matcher fires on
# MENTIONS, so it would forbid every brief and commit message discussing rebase -- including
# the one reporting this." A gate that blocks `git commit -m "...never rebase..."` is WORSE
# than no gate: it is unusable, it will be disabled, and it will have blocked the person
# documenting the hazard. If N2/N3 ever go red, the gate ships OFF.

set -uo pipefail
# NRG_HOOK lets us drive the suite at a DIFFERENT build of the hook -- specifically the PREVIOUS
# committed one -- to prove the new arms are PROVEN-RED. A test that has never been observed to fail
# has not been shown it CAN fail. (CLAUDE.md: "a census never observed to say RED has not been shown
# to be able to." Run it as: NRG_HOOK=/tmp/old-hook.sh bash tests/test_never_rules_gate.sh)
HOOK="${NRG_HOOK:-$(cd "$(dirname "$0")/.." && pwd)/never-rules-gate.sh}"

# JQ resolution LADDER (Andrew finish-out 2026-07-30, MSTR): the suite built its JSON
# payloads with `${JQ:-jq}` and NEVER RESOLVED JQ -- in a profile-less harness shell
# (no PATH jq, the measured norm on this box) the encode failed, the hook received
# EMPTY stdin, exited 0 by design, and EVERY DENY ARM RENDERED "PASS (want DENY)":
# 32 PASS / 35 FAIL with the failures tracking the ENVIRONMENT, not the gate. A
# suite whose encoder can silently die reports the encoder's health, not the
# subject's. Same ladder as the gate itself (tests/ -> ../../jq.exe = .tools/jq.exe).
if [ -z "${JQ:-}" ]; then
    _TD="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || _TD="."
    if [ -x "${_TD}/../../jq.exe" ]; then JQ="${_TD}/../../jq.exe"
    elif command -v jq >/dev/null 2>&1; then JQ="jq"
    else
        echo "FATAL: no jq resolvable (tests/../../jq.exe absent, none on PATH) -- the suite" >&2
        echo "cannot encode payloads and every verdict would be meaningless. Refusing to run." >&2
        exit 2
    fi
fi
export JQ
PASS=0; FAIL=0

# *** RV-0048 F-020: THIS SUITE USED TO POISON THE EVIDENCE BASE IT IS AUDITED BY. ***
# The hook appends every override to org/git-author-override-audit.log -- the append-only log that
# OVERRIDE_REVIEW (MSTR's governance instrument) reads. This suite exercises overrides, so every run
# wrote fixtures into it as if they were real bypasses. 6 such records existed; ALL were phantoms.
# Route ours to a scratch file, and assert on it at the end.
export NEVER_GATE_AUDIT="$(mktemp 2>/dev/null || echo "/tmp/nrg_audit_$$")"
# *** THE SUITE WAS NOT HERMETIC: ITS TOTALS DEPENDED ON WHO RAN IT. ***
# Measured 2026-09-01 -- 1.0.0_SA_CTO~Z read 76 PASS/15 FAIL and 0.0.0_AB_MSTR~Z read 79/12 on the
# SAME commit, same device, same file. Both totals summed to 91, so no arm appeared or vanished:
# THREE ARMS FLIPPED. Reproduced by changing exactly one variable, the caller identity:
#     env -u OPAL_AGENT_SERIAL            -> 79 PASS / 12 FAIL
#     OPAL_AGENT_SERIAL=0.0.0_AB_MSTR~Z   -> 76 PASS / 15 FAIL
# The three are the `git pull`-based rebase arms (git pull --rebase, -c pull.rebase one-shot,
# generic-flag-before--c). GATE 5 resolves the caller from OPAL_AGENT_SERIAL when the payload
# carries no session_id, and for a NON-INTEGRATOR it DENIES those pulls on IDENTITY -- so the arm
# observed DENY and scored PASS WITHOUT GATE 1 EVER FIRING. Green for the wrong gate: a rebase arm
# certifying the rebase gate while the push/pull gate did the denying.
# PINNING the caller to the integrator makes GATE 5 transparent, so a GATE 1 arm measures GATE 1
# and nothing else. It RAISES the failure count from 12 to 15 -- those three were always broken and
# were being masked. A per-arm identity (check_as, below) overrides this for GATE 5's own arms.
export OPAL_AGENT_SERIAL="0.0.0_AB_MSTR~Z"

: > "$NEVER_GATE_AUDIT"

# verdict: prints DENY or PASS for a given command string.
#
# *** THE HARNESS ITSELF COULD NOT EXPRESS THE INPUT THAT BROKE THE GATE. ***
# The original built its JSON with `sed 's/^/"/; s/$/"/'` -- which applies PER LINE. A MULTI-LINE
# command therefore produced INVALID JSON, jq failed, the hook exited 0, and the harness reported
# **PASS**. So every multi-line arm was green for a reason that had nothing to do with the gate:
# a test that cannot encode the failing input reports PASS no matter what the gate does.
# That is exactly the class this gate exists for -- and it was in the instrument verifying it.
# Now: jq -Rs does a real JSON encode (newlines -> \n), so a multi-line command reaches the hook
# the way Claude Code actually delivers it.
verdict() {
    local out
    out=$(printf '%s' "$1" | "${JQ:-jq}" -Rs '{tool_input:{command:.}}' | bash "$HOOK" 2>/dev/null)
    if printf '%s' "$out" | grep -q '"permissionDecision":"deny"'; then echo DENY; else echo PASS; fi
}

check() { # name, cmd, expected
    local got; got=$(verdict "$2")
    if [ "$got" = "$3" ]; then PASS=$((PASS+1)); printf '  PASS  %-58s -> %s\n' "$1" "$got"
    else FAIL=$((FAIL+1)); printf '  FAIL  %-58s -> %s (want %s)\n' "$1" "$got" "$3"; fi
}

echo "never-rules-gate -- EXERCISED (branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null))"
echo ""
echo "POSITIVE -- must DENY (these are the NEVER rules, on a shared branch):"
check "git rebase -i"                     'git rebase -i HEAD~3'                              DENY
check "git rebase (bare)"                 'git rebase origin/CLOUD'                           DENY
check "git pull --rebase"                 'git pull --rebase origin CLOUD'                    DENY
check "git -C portal rebase"              'git -C portal rebase origin/DEV'                   DENY

# --- F-XXX (2026-08-05): TWO-TOKEN GIT GLOBAL OPTIONS STRAND THE _GIT OPTION-CONSUMER ---
# Found by 2.0.0_SA_COO (hit the `-c` cell live, self-disclosed before anyone found it); CTO
# re-derived at source and WIDENED it: `-c` was 1 of 5 cells. Every option whose value is a
# SEPARATE argv token strands the regex before the verb, making the command invisible to ALL
# FIVE _GIT-built gates. These arms are PROVEN-RED against the pre-fix hook:
#     NRG_HOOK=<pre-fix build> bash tests/test_never_rules_gate.sh
# -> the `-c` arms and the --git-dir/--work-tree/--namespace arms all render PASS(want DENY).
# DO NOT collapse these to one representative case: they are five independent cells and a future
# _GIT edit can reopen any one of them alone.
check "F-XXX -c evades rebase"            'git -c core.pager=cat rebase origin/CLOUD'         DENY
check "F-XXX -c pull.rebase one-shot"     'git -c pull.rebase=true pull origin CLOUD'         DENY
check "F-XXX --git-dir two-token"         'git --git-dir .git rebase origin/CLOUD'            DENY
check "F-XXX --work-tree two-token"       'git --work-tree . rebase origin/CLOUD'             DENY
check "F-XXX --namespace two-token"       'git --namespace ns rebase origin/CLOUD'            DENY
check "F-XXX -c repeated"                 'git -c a=1 -c b=2 rebase origin/CLOUD'             DENY
check "F-XXX -C and -c combined"          'git -C portal -c a=1 rebase origin/DEV'            DENY
check "F-XXX generic flag before -c"      'git --no-pager -c pull.rebase=true pull origin CLOUD' DENY
check "F-XXX --git-dir= single-token"     'git --git-dir=.git rebase origin/CLOUD'            DENY
# NEGATIVE CONTROLS for the widened consumer -- the fix must not start eating verbs. If the
# option list ever gains an OPTIONAL-value flag (e.g. --exec-path, deliberately excluded), the
# consumer swallows the verb and these go red. That is the whole reason they are here.
check "F-XXX neg: plain rebase still denies" 'git rebase origin/CLOUD'                        DENY
check "F-XXX neg: --exec-path not eaten"  'git --exec-path rebase origin/CLOUD'               DENY
check "F-XXX neg: log is not a verb match" 'git log --oneline -1'                             PASS
check "F-XXX neg: -c on a benign verb"    'git -c core.pager=cat log --oneline -1'            PASS
check "F-XXX neg: MENTION not matched"    'git commit -m "F-XXX: do not rebase, see gate"'    PASS
check "bare terraform apply"              'terraform apply -auto-approve'                     DENY
check "bare terraform destroy"            'terraform destroy'                                 DENY
check ".tools/terraform.exe apply"        './.tools/terraform.exe apply'                      DENY
check "git commit -m w/ backtick"         'git commit -m "fix `whoami` thing"'                DENY
check "git commit -m w/ \$("              'git commit -m "fix $(id -u) thing"'                DENY
check "safe-commit -m w/ \$("             'bash .tools/safe-commit.sh -m "x $(date) y" -- a'  DENY

echo ""
echo "NEGATIVE CONTROLS -- must PASS. *** THESE ARE THE ONES THAT MATTER. ***"
echo "  (a gate that fires on a MENTION of rebase blocks the brief reporting the hazard --"
echo "   CLAUDE.md refuses a text-deny rule for exactly this reason. If these go red, ship OFF.)"
check "N1 commit msg MENTIONING rebase"   'git commit -m "doc: we must never rebase on CLOUD"' PASS
check "N2 commit -F w/ rebase in file"    'safe-commit.sh --author "x" -F /tmp/msg.txt -- a'   PASS
check "N3 grep for the word rebase"       'grep -rn "rebase" CLAUDE.md'                        PASS
check "N4 echo mentioning terraform apply" 'echo "never run bare terraform apply"'             PASS
# N5/N6 REPAIRED 2026-08-05 (CTO, found while landing F-XXX). These asserted PASS and had been
# RED on every run since LD-0367/0368 added GATE 5 (integrator-only push/pull) -- which denies any
# `git pull` from a NON-INTEGRATOR seat, entirely correctly. The arms were never updated, so the
# suite printed "FAILURES PRESENT -- do NOT wire this hook" on every green build.
# THAT IS THE REAL HAZARD HERE, not the two red lines: a permanently-red suite is a DEAD suite --
# it trains its readers to discount the verdict, and the next genuine red arrives into an audience
# that has already learned to ignore it. Discriminator run before repairing: these two deny
# IDENTICALLY on the pre-F-XXX and post-F-XXX hook, so the cause is GATE 5, not the option-consumer.
# The ORIGINAL INTENT of these arms is still worth asserting and is preserved: the sanctioned merge
# remedy must not be denied BY THE REBASE GATE. So assert the GATE, not the bare verdict -- a
# verdict-only assertion cannot tell "denied for the right reason" from "denied for the wrong one".
# CVO N5/N6 residual (2320Z, adjudicated): the prior form echoed PASS on a NON-DENY, but an ERRORED
# hook ALSO produces a non-deny (empty stdout), so a gate that CRASHED read as PASS. That was live at
# 1323Z when never-rules-gate.sh threw a parse error under an in-place edit. Fixed per CRO's vacuity
# rule (DENOMINATOR_ERRORS/DERIVED_UNIVERSE §2): an instrument that did not run reports UNRUN, NEVER pass.
# DISCRIMINATOR, exercised: a genuine ALLOW is rc=0 + empty stdout; an errored hook is rc!=0 + empty
# stdout. The exit code is the only signal that separates them, so verdict_gate keys on it.
verdict_gate() { # command -> BLOCKED(...) tag if denied | "ALLOW" if cleanly allowed | "UNRUN" if the hook errored
    local out rc
    out=$(printf '%s' "$1" | "${JQ:-jq}" -Rs '{tool_input:{command:.}}' | bash "$HOOK" 2>/dev/null)
    rc=$?
    if printf '%s' "$out" | grep -q '"permissionDecision":"deny"'; then
        printf '%s' "$out" | grep -oE 'BLOCKED \(([^)]*)\)' | head -1
    elif [ "$rc" -ne 0 ]; then echo UNRUN     # hook crashed/parse-errored -> NOT a pass
    else echo ALLOW; fi
}
check_not_rebase_gate() { # name, cmd -- must NOT be denied by the NEVER#7 rebase gate
    local g; g=$(verdict_gate "$2")
    case "$g" in
        UNRUN)     FAIL=$((FAIL+1)); printf '  FAIL  %-58s -> %s\n' "$1" "UNRUN -- hook produced no verdict (crash/parse-error), NOT a pass" ;;
        *NEVER#7*) FAIL=$((FAIL+1)); printf '  FAIL  %-58s -> %s\n' "$1" "denied by the REBASE gate" ;;
        *)         PASS=$((PASS+1)); printf '  PASS  %-58s -> %s\n' "$1" "$g (not the rebase gate)" ;;
    esac
}
check_not_rebase_gate "N5 the REMEDY: git pull (merge) not rebase-gated" 'git pull origin CLOUD'
check_not_rebase_gate "N6 git pull --no-rebase not rebase-gated"        'git pull --no-rebase origin CLOUD'
check "N7 safe-apply (the sanctioned path)" 'bash .tools/safe-apply.sh -chdir=infra/aws'       PASS
check "N8 terraform plan"                 'terraform plan'                                     PASS
check "N9 git commit -m, no metachar"     'git commit -m "plain message"'                      PASS
check "N10 git status"                    'git status --short'                                 PASS
check "N11 rebase in a PATH-ish word"     'echo "see docs/rebase-policy.md"'                   PASS

echo ""
echo "SHARED-WORKTREE BLAST RULE -- must DENY (stash/clean park or delete OTHER agents' work):"
check "git stash (bare)"                  'git stash'                                          DENY
check "git stash push"                    'git stash push -m "wip"'                            DENY
check "git stash save"                    'git stash save'                                     DENY
check "git clean -fd"                     'git clean -fd'                                      DENY

echo ""
echo "...but READ + RECOVERY must stay OPEN (never block the recovery path):"
check "git stash list (read-only)"        'git stash list'                                     PASS
check "git stash show"                    'git stash show -p stash@{0}'                        PASS
check "git stash pop (RECOVERY)"          'git stash pop'                                      PASS
check "git stash apply (RECOVERY)"        'git stash apply stash@{0}'                          PASS
check "git clean -n (dry-run: look first)" 'git clean -nd'                                     PASS
check "THE RIGHT INSTRUMENT (no mutation)" 'git show HEAD:.tools/operator_tool.py | ruff check -'   PASS

echo ""
echo "*** DISARM VECTOR -- THE BUG THAT LET A LIVE 'git stash' THROUGH. ***"
echo "  A multi-line command whose ECHO merely MENTIONS an allowlisted form must STILL be DENIED."
echo "  (The real probe said: echo \"...'git stash list' would just print...\" then ran 'git stash push'."
echo "   The whole-command allowlist matched 'stash list' IN THE ECHO and PASSED the push. It executed.)"
echo "  AN EXCLUSION EVALUATED OVER A WIDER SCOPE THAN THE MATCH IT EXCUSES IS A DISARM VECTOR."
check "stash push + 'stash list' in an echo"  'echo "safe because git stash list is read-only"
git stash push -m wip'                                                                            DENY
check "stash push + 'stash pop' in a comment" 'git stash push  # we can git stash pop it back'    DENY
check "terraform apply + 'safe-apply' in echo" 'echo "should use safe-apply"
terraform apply'                                                                                   DENY
check "git clean + '-n' mentioned in an echo" 'echo "you could use -n to dry-run"
git clean -fd'                                                                                     DENY

echo ""
echo "...and the excuse must STILL work when it is on the SAME line as the command:"
check "same-line: git stash list"             'git stash list'                                     PASS
check "same-line: safe-apply"                 'bash .tools/safe-apply.sh -chdir=infra/aws apply'   PASS
check "same-line: git clean -nd"              'git clean -nd'                                      PASS

echo ""
echo "*** HEREDOC BODY = DATA, NOT COMMANDS. The gate BLOCKED ITS OWN COMMIT on this. ***"
echo "  CLAUDE.md refuses a matcher that 'would forbid every brief and commit message discussing"
echo "  rebase -- INCLUDING THE ONE REPORTING THIS.' A -F commit message (LD-0276) documenting the"
echo "  gate necessarily CONTAINS 'git stash' / 'git clean'. It must PASS."
check "heredoc commit msg documenting the gate" 'cat > /tmp/m.txt <<'"'"'EOF'"'"'
doc: the gate denies git stash and git clean
git stash parks every dirty file; git clean -fd deletes untracked work
EOF
bash .tools/safe-commit.sh -F /tmp/m.txt -- CLAUDE.md'                                            PASS
check "heredoc mentioning terraform apply"      'cat > /tmp/m.txt <<'"'"'EOF'"'"'
never run bare terraform apply
EOF
git status'                                                                                       PASS
echo "  ...but a REAL command AFTER a heredoc must still be caught:"
check "heredoc + a real git stash after it"     'cat > /tmp/m.txt <<'"'"'EOF'"'"'
some message
EOF
git stash push -m wip'                                                                            DENY

echo ""
echo "OVERRIDE -- audited bypass must PASS:"
check "never-override marker"             'git rebase -i HEAD~2  # never-override: scratch branch cleanup, CTO' PASS

echo ""
echo "*** RV-0048 F-019: THE OVERRIDE MARKER IS AN EXCLUSION. IT MUST BE SCOPED TO ITS OWN"
echo "    SIMPLE COMMAND -- OR IT IS A UNIVERSAL DISARM: one string waives EVERY rule. ***"
echo "  Found by 0.0.0_AB_MSTR by EXERCISING the gate, not by it biting. These arms are PROVEN-RED:"
echo "  every one of them PASSED (fail-open) against the gate as shipped 2026-07-13."
echo "  D and E are the disarms. G is the control that proves the override still WORKS -- without G,"
echo "  a gate that simply ignored the marker entirely would score a perfect green here."
check "F-019 D: marker QUOTED in an echo + a real stash" 'echo "append # never-override: reason to bypass the gate"
git stash push -m wip'                                                                             DENY
check "F-019 E: marker authorizes the REBASE, not the terraform" 'git rebase -i HEAD~2  # never-override: scratch cleanup
terraform apply -auto-approve'                                                                     DENY
check "F-019 E2: marker authorizes the REBASE, not the stash"    'git rebase -i HEAD~2  # never-override: scratch cleanup
git stash push -m wip'                                                                             DENY
check "F-019 F: CONTROL -- same two hazards, NO marker at all"   'terraform apply -auto-approve
git stash push -m wip'                                                                             DENY
check "F-019 G: CONTROL -- marker ON the hazard's OWN command"   'terraform apply  # never-override: DR drill, CTO'  PASS

echo ""
echo "*** F-022 (CTO, self-found while fixing F-019): THE REBASE GATE'S EARLY `exit 0` WAS A"
echo "    SECOND UNIVERSAL DISARM. A rebase on a SCRATCH branch returned from the WHOLE HOOK,"
echo "    skipping the stash / clean / terraform / commit-msg gates. ***"
echo "  Cannot be observed on a shared branch (the rebase denies first), so these arms drive the"
echo "  hook at a REAL scratch repo via 'git -C' -- the branch the hook itself resolves."
SCRATCH=$(mktemp -d 2>/dev/null || echo "/tmp/nrg_scratch_$$")
mkdir -p "$SCRATCH"
git -C "$SCRATCH" init -q >/dev/null 2>&1
git -C "$SCRATCH" checkout -q -b scratch >/dev/null 2>&1
# An UNBORN HEAD makes `rev-parse --abbrev-ref HEAD` fail -- the hook then reads BRANCH=UNKNOWN,
# which is not shared, so the arms would still work by ACCIDENT. Give it a real commit so the
# scratch branch is a real branch and the arms test what they claim to test.
git -C "$SCRATCH" -c user.email=t@t -c user.name=t commit -q --allow-empty --allow-empty-message -F /dev/null >/dev/null 2>&1
if [ "$(git -C "$SCRATCH" rev-parse --abbrev-ref HEAD 2>/dev/null)" = "scratch" ]; then
    check "F-022 scratch rebase alone -> allowed (your own business)" \
        "git -C $SCRATCH rebase -i HEAD~1"                                                         PASS
    check "F-022 scratch rebase must NOT disarm the terraform gate" \
        "git -C $SCRATCH rebase -i HEAD~1
terraform apply -auto-approve"                                                                     DENY
    check "F-022 scratch rebase must NOT disarm the stash gate" \
        "git -C $SCRATCH rebase -i HEAD~1
git stash push -m wip"                                                                             DENY
    rm -rf "$SCRATCH" 2>/dev/null || true
else
    FAIL=$((FAIL+1)); echo "  FAIL  F-022 setup: could not create a scratch repo -- ARMS NOT RUN (not a pass)"
fi

echo ""
echo "*** RV-0048 F-021: the commit-msg gate's three conditions must CO-OCCUR on ONE simple"
echo "    command. Three independent whole-command greps convicted a SAFE -F commit. ***"
echo ""
echo "*** F-023 -- THE HOLE MY OWN F-021 FIX CREATED, AND IT EXECUTED A REAL COMMIT MESSAGE. ***"
echo "  A `-m` BODY IS ONE SHELL ARGUMENT THAT SPANS NEWLINES. Per-simple-command scoping SPLITS IT:"
echo "     line 1 gets `commit` + `-m` and NO metachar; line 2 gets the metachar and NO `commit`."
echo "  Neither fragment carries all three -> the gate PASSED IT. 0.4.0_DS_ClientPlatform~A then"
echo "  executed his own commit message (49fe7b0e4) and a clause was DELETED from the immutable record."
echo "  >> GATE 3 IS WHOLE-COMMAND SCOPED ON PURPOSE. Do NOT 'fix' it to per-simple-command. <<"
check "F-023 MULTI-LINE -m, backtick on line 2 (DS~A's shape)" 'git commit -m "fix: the selector
`any(t in src for t in ROSTER_TOKENS)` was the bug"'                                               DENY
check "F-023 MULTI-LINE -m, \$( on line 2"                 'git commit -m "header
body with $(id) in it"'                                                                            DENY
check "F-023 single-line -m + backtick (was already green)" 'git commit -m "fix `whoami` thing"'   DENY

echo ""
echo "  ...and the FALSE POSITIVE we DELIBERATELY ACCEPT. It fails CLOSED, and the remedy is -F."
echo "  *** WHEN THE TWO ERROR DIRECTIONS ARE 'ANNOYING' AND 'EXECUTES CODE', YOU CHOOSE ANNOYING. ***"
check "F-021 safe -m + unrelated \$( elsewhere -> DENIED (accepted)" 'safe-commit.sh --author "x" -m "plain message" -- a
echo "the id is $(id)"'                                                                            DENY
check "F-021 a REAL commit -m with \$( still denies"  'safe-commit.sh --author "x" -m "fix $(id)" -- a'  DENY

echo ""
echo "  ...but the MANDATED -F PATH MUST STILL PASS -- even when the message DOCUMENTS this hazard:"
check "the -F heredoc pattern, message full of backticks" 'cat > /tmp/m.txt <<'"'"'EOF'"'"'
doc: a commit message is an EXECUTION VECTOR -- `whoami` and $(id) run BEFORE git sees them
EOF
bash .tools/safe-commit.sh --author "x" -F /tmp/m.txt -- CLAUDE.md'                                PASS
check "-F with no -m at all"                          'safe-commit.sh --author "x" -F /tmp/m.txt -- a'  PASS

echo ""
echo "*** F-024: THE NEGATIVE CONTROL WENT RED, ON BOTH ARMS. CLAUDE.md: A RED HERE SHIPS THE GATE OFF. ***"
echo "  Exercised by COO. The gate DENIED an `echo` that merely MENTIONED the banned commands -- and"
echo "  DENIED A CENSUS OF ITSELF. *** IT WAS BLOCKING THE BRIEF THAT REPORTS THE HAZARD. ***"
echo "  ROOT (one, three symptoms): I matched THE WORD, not THE COMMAND -- and split on ; and | INSIDE"
echo "  QUOTED STRINGS, which tore the MATCH away from its EXCUSE and manufactured fragments whose"
echo "  first token looked like a command that never existed."
echo "  FIX: command-POSITION anchoring + a quoted string is DATA (blank its contents before splitting)."
check "COO-1 echo mentioning terraform apply + safe-apply" 'echo "the rule forbids bare terraform apply; use safe-apply"'  PASS
check "COO-2 echo mentioning the rebase rule"              'echo "NEVER#7 forbids git rebase on shared branches"'          PASS
check "COO-3 a CENSUS OF THE GATE ITSELF"                  "grep -oE 'rebase|terraform apply|git stash' CLAUDE.md"         PASS
check "N echo mentioning git stash"                        'echo "git stash parks every dirty file"'                       PASS
echo "  ...and it must STILL BITE (a gate that denies nothing is not a gate):"
check "REAL rebase still denies"                           'git rebase -i HEAD~3'                                          DENY
check "REAL bare terraform apply still denies"             'terraform apply -auto-approve'                                 DENY
check "REAL stash push still denies"                       'git stash push -m wip'                                         DENY
check "rebase inside if/then (leading keyword)"            'if true; then git rebase origin/CLOUD; fi'                     DENY

echo ""
echo "*** RV-0048 F-020: THE AUDIT LOG MUST RECORD A REAL SUPPRESSION, NEVER A MENTION. ***"
echo "  It is the evidence base for OVERRIDE_REVIEW. Census-by-mention on an append-only"
echo "  governance log is not a bug in a report -- it is a permanently corrupted record."
# `grep -c` PRINTS 0 AND EXITS 1 on no-match, so `|| echo 0` emitted "0\n0" and the arithmetic blew
# up. It is the banked retrieval defect (CLAUDE.md Git: "grep -c prints 0 -- grep counted zero
# matches IN AN ERROR MESSAGE"). Swallow the exit status, do not add a second value.
# ============================================================================================
# F-XXX CLASS-LEVEL CONTROLS. The two above these lines are special cases; these two are the
# assertions that would have caught F-XXX WITHOUT ANYONE THINKING OF `-c`. Proposed by
# 2.0.0_SA_COO in the finding routing; adopted by CTO as the durable half of the fix.
#
# (1) DERIVATION CHECK -- the two-token option list is a PREDICATE OVER GIT'S OWN USAGE LINE,
#     not a hand-drawn roster ("a predicate is not a roster"). git's `-c <name>=<value>` and
#     `-C <path>` appear in `git --help` usage; if a git-version bump adds a value-taking global
#     option, this goes RED and the list gets re-derived. It cannot tell us about options git
#     omits from its usage line -- stated, not papered over.
_gitusage="$(git --help 2>&1 | head -4)"
_missing=""
for _o in '-c <name>=<value>' '-C <path>'; do
    case "$_gitusage" in *"$_o"*) ;; *) _missing="${_missing} ${_o}";; esac
done
if [ -z "$_missing" ]; then
    PASS=$((PASS+1)); printf '  PASS  %-58s -> %s\n' "F-XXX derivation: git usage still declares -c/-C" "in sync"
else
    FAIL=$((FAIL+1)); printf '  FAIL  %-58s -> %s\n' "F-XXX derivation: git usage drifted" "missing:${_missing} -- RE-DERIVE _O2"
fi

# (2) DENY-TEXT/MATCHER COHERENCE -- a gate's suggested remedy is part of its SURFACE. F-XXX's
#     root was that the deny-text taught `git config pull.rebase false`, whose natural one-shot
#     form (`git -c pull.rebase=false pull`) evaded the matcher: the guidance funnelled careful
#     agents INTO the gap. Assert no deny-text recommends an inline `-c` one-shot.
if grep -nE 'deny "' "$HOOK" | grep -qE "Use: git -c|try git -c|run git -c"; then
    FAIL=$((FAIL+1)); printf '  FAIL  %-58s -> %s\n' "F-XXX deny-text recommends an inline -c one-shot" "funnel into the gap"
else
    PASS=$((PASS+1)); printf '  PASS  %-58s -> %s\n' "F-XXX no deny-text recommends an inline -c one-shot" "coherent"
fi

_n_audit=$(grep -c 'NEVER-OVERRIDE' "$NEVER_GATE_AUDIT" 2>/dev/null || true)
[ -z "$_n_audit" ] && _n_audit=0
# The ONLY arms that legitimately override (marker on the SAME simple command as a real match):
#   'never-override marker' (rebase on CLOUD) and 'F-019 G' (terraform) -- and F-019 E/E2 each
#   legitimately override THEIR rebase limb (the terraform/stash limb is what still denies).
# What must NEVER appear: an override record from F-019 D, where the marker is only QUOTED in an echo.
if [ "$_n_audit" -gt 0 ]; then
    PASS=$((PASS+1)); printf '  PASS  %-58s -> %s\n' "audit log records real overrides" "$_n_audit record(s)"
else
    FAIL=$((FAIL+1)); printf '  FAIL  %-58s -> %s\n' "audit log records real overrides" "0 (the override path never fired -- instrument break, not a pass)"
fi
if grep -q 'reason=reason to bypass the gate' "$NEVER_GATE_AUDIT" 2>/dev/null; then
    FAIL=$((FAIL+1)); printf '  FAIL  %-58s -> %s\n' "F-020 a MENTION was audited as an override" "census-by-mention"
else
    PASS=$((PASS+1)); printf '  PASS  %-58s -> %s\n' "F-020 no mention audited as an override" "clean"
fi
# =========================================================================================
# DT PORTAL-PROD CARVE-OUT (Andrew-direct 2026-09-01 at the 1.0.0_SA_CTO~Z terminal:
# "fix the gate so DT can push portal prod").
#
# THE POSITIVE ARM IS ONE LINE. THE SIX NEGATIVES ARE THE POINT -- the failure mode for a
# carve-out is not that it fails to open, it is that it opens WIDER THAN ITS WORD, and a
# too-wide gate passes its own positive test perfectly. Each negative is an independent cell
# of the three-way scope (caller is DT / branch is PROD / repo is portal) plus the verb.
#
# PROVEN-RED: the positive arm renders DENY against the pre-carve-out hook --
#     NRG_HOOK=<pre-carve-out build> bash tests/test_never_rules_gate.sh
# An arm never observed to fail has not been shown it CAN fail.
#
# check_as drives the caller identity the way the gate actually resolves it: the payload
# carries no session_id, so $_CALLER falls through to OPAL_AGENT_SERIAL.
check_as() { # serial, name, cmd, expected
    local got
    export OPAL_AGENT_SERIAL="$1"
    got=$(verdict "$3")
    unset OPAL_AGENT_SERIAL
    if [ "$got" = "$4" ]; then PASS=$((PASS+1)); printf '  PASS  %-58s -> %s
' "$2" "$got"
    else FAIL=$((FAIL+1)); printf '  FAIL  %-58s -> %s (want %s)
' "$2" "$got" "$4"; fi
}

echo ""
echo "DT PORTAL CARVE-OUT (PROD 09-01, DEV 09-02) -- positives + negatives (over-widening is the failure mode):"
check_as '0.4.0_DT_ClientPlatform~Z' "DT pushes portal PROD (the carve-out)"       'git -C portal push origin PROD' PASS
check_as '0.4.0_DT_ClientPlatform~Z' "DT pushes portal DEV (Andrew 2026-09-02)"    'git -C portal push origin DEV'  PASS
check_as '0.4.0_DT_ClientPlatform~Z' "neg: DT PULLing portal DEV still DENIED"     'git -C portal pull origin DEV'  DENY
check_as '0.4.0_DT_ClientPlatform~Z' "neg: DT pushing workspace CLOUD still DENIED" 'git push origin CLOUD'         DENY
check_as '0.4.0_DT_ClientPlatform~Z' "neg: DT PULLing portal PROD still DENIED"    'git -C portal pull origin PROD' DENY
check_as '1.0.0_SA_CTO~Z'            "neg: non-DT (CTO) on portal PROD DENIED"     'git -C portal push origin PROD' DENY
check_as '0.4.0_DS_ClientPlatform~Z' "neg: DS is not DT, portal PROD DENIED"       'git -C portal push origin PROD' DENY
check_as ''                          "neg: UNRESOLVED caller fails CLOSED on PROD" 'git -C portal push origin PROD' DENY
check_as '0.0.0_AB_MSTR~Z'           "integrator unaffected: MSTR workspace CLOUD" 'git push origin CLOUD'          PASS

# SITEZ IN SHARED_BRANCHES (Andrew-direct 2026-09-02, "all recs approved"). Before this, on the site-Z
# device the working branch read as NOT shared, so GATE 1 and GATE 5 never fired there -- every rebase
# arm above was red on that device for that reason alone. PROVEN-RED: the three DENY arms render
# PASS (want DENY) against the pre-09-02 hook when run from a SITEZ checkout.
echo ""
echo "SITEZ IS A SHARED BRANCH (Andrew 2026-09-02):"
check    "SITEZ: rebase onto origin/SITEZ DENIED (NEVER#7 fires here now)" 'git rebase origin/SITEZ'  DENY
check_as '0.4.0_DT_ClientPlatform~Z' "SITEZ: non-integrator push DENIED (LD-0367 mechanical)" 'git push origin SITEZ' DENY
check_as '0.4.0_DT_ClientPlatform~Z' "SITEZ: non-integrator pull DENIED"              'git pull origin SITEZ' DENY
check_as '0.0.0_AB_MSTR~Z'           "SITEZ: integrator push still PASS"              'git push origin SITEZ' PASS

rm -f "$NEVER_GATE_AUDIT" 2>/dev/null || true

echo ""
echo "================================================================"
echo "PASS: $PASS   FAIL: $FAIL"
[ "$FAIL" -eq 0 ] && { echo "ALL CHECKS PASS -- denies the command, never the mention."; exit 0; }
echo "FAILURES PRESENT -- do NOT wire this hook."; exit 1
