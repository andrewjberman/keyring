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
HOOK="$(cd "$(dirname "$0")/.." && pwd)/never-rules-gate.sh"
PASS=0; FAIL=0

# verdict: prints DENY or PASS for a given command string
verdict() {
    local out
    out=$(printf '{"tool_input":{"command":%s}}' "$(printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g; s/^/"/; s/$/"/')" \
          | bash "$HOOK" 2>/dev/null)
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
check "N5 the REMEDY: git pull (merge)"   'git pull origin CLOUD'                              PASS
check "N6 git pull --no-rebase"           'git pull --no-rebase origin CLOUD'                  PASS
check "N7 safe-apply (the sanctioned path)" 'bash .tools/safe-apply.sh -chdir=infra/aws'       PASS
check "N8 terraform plan"                 'terraform plan'                                     PASS
check "N9 git commit -m, no metachar"     'git commit -m "plain message"'                      PASS
check "N10 git status"                    'git status --short'                                 PASS
check "N11 rebase in a PATH-ish word"     'echo "see docs/rebase-policy.md"'                   PASS

echo ""
echo "OVERRIDE -- audited bypass must PASS:"
check "never-override marker"             'git rebase -i HEAD~2  # never-override: scratch branch cleanup, CTO' PASS

echo ""
echo "================================================================"
echo "PASS: $PASS   FAIL: $FAIL"
[ "$FAIL" -eq 0 ] && { echo "ALL CHECKS PASS -- denies the command, never the mention."; exit 0; }
echo "FAILURES PRESENT -- do NOT wire this hook."; exit 1
