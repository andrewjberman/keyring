#!/usr/bin/env bash
# Exercise .tools/hooks/never-rules-gate.sh directly with WELL-FORMED JSON.
# Runs as `bash <path>`, so the hook sees only that -- it cannot block its own test.
#
# THE ORACLE, CORRECTED (v2). The hook ALWAYS exits 0 -- never-rules-gate.sh:51:
#   "Block mechanism: JSON on stdout, permissionDecision=\"deny\", exit 0."
# v1 of this harness keyed the verdict on rc, so DENY WAS NOT A REACHABLE OUTPUT. Every arm scored
# PASS -- including `git rebase origin/CLOUD`, which I had watched this same gate BLOCK minutes
# earlier. Ten arms read "ok" and measured NOTHING. It was RIGGED, NOT PASSED. Read STDOUT, which is
# where the gate actually speaks.
cd /c/Users/AndrewBerman/Desktop/ajb_workspace || exit 2
GATE=.tools/hooks/never-rules-gate.sh
pass=0; fail=0

probe() {
  local desc="$1" cmd="$2" expect="$3" tool="${4:-Bash}"
  local json out verdict mark
  json=$(python -c "import json,sys; print(json.dumps({'tool_name':sys.argv[2],'tool_input':{'command':sys.argv[1]}}))" "$cmd" "$tool")
  out=$(printf '%s' "$json" | bash "$GATE" 2>/dev/null)
  case "$out" in
    *'"permissionDecision":"deny"'*) verdict=DENY ;;
    *)                               verdict=PASS ;;
  esac
  if [ "$verdict" = "$expect" ]; then mark="ok  "; pass=$((pass+1)); else mark="FAIL"; fail=$((fail+1)); fi
  printf '  %s %-4s (want %-4s) %s\n' "$mark" "$verdict" "$expect" "$desc"
}

echo "=== P: POSITIVE CONTROLS -- can the gate DENY? (a gate never seen to fire has not been shown to) ==="
probe "git rebase on CLOUD"              'git rebase origin/CLOUD'                       DENY
probe "git pull --rebase"                'git pull --rebase origin CLOUD'                DENY
probe "bare terraform apply"             'terraform apply -auto-approve'                 DENY
probe "git stash push"                   'git stash push -m wip'                         DENY
probe "git clean -fd"                    'git clean -fd'                                 DENY
probe "PowerShell surface too"           'git rebase origin/CLOUD'                       DENY PowerShell
probe "F-010: commit -m with \$( "        'git commit -m "fix $(whoami) thing"'           DENY
probe "F-010: commit -m with backtick"   'git commit -m "fix `whoami` thing"'            DENY

echo
echo "=== N: NEGATIVE CONTROLS -- the load-bearing half. A gate that blocks the brief is worse than no gate ==="
probe "commit msg MENTIONS rebase"       'git commit -m "doctrine: never rebase a shared branch"'  PASS
probe "stash list (READ path)"           'git stash list'                                PASS
probe "stash pop (RECOVERY path)"        'git stash pop'                                 PASS
probe "git clean -n (dry run)"           'git clean -n'                                  PASS
probe "safe-apply (sanctioned)"          'bash .tools/safe-apply.sh'                     PASS
probe "git pull merge (the remedy)"      'git pull origin CLOUD'                         PASS
probe "terraform plan"                   'terraform plan'                                PASS
probe "commit -F (the mandated path)"    'safe-commit.sh --author "x" -F /tmp/m.txt -- a.py'  PASS

echo
echo "=== D: THE DISARM VECTOR (CTO 0332d5d55: 'one string, anywhere, waived EVERY rule') ==="
probe "override marker in an ECHO + real rebase" 'echo "# never-override: safe" && git rebase origin/CLOUD' DENY
probe "allowlist word in ECHO + real stash push" 'echo "we can git stash pop it back" && git stash push'    DENY
probe "legit override on the SAME simple cmd"    'git rebase origin/CLOUD # never-override: scratch recovery, CVO' PASS

echo
echo "=== X: OVER-FIRE -- does a banned verb as DATA get blocked? (the false-positive axis) ==="
probe "grep for the string in a doc"     'grep -n "git rebase" CLAUDE.md'                PASS
probe "echo the string"                  'echo "git rebase is banned"'                   PASS

echo
echo "=== TOTAL: pass=$pass fail=$fail (denominator $((pass+fail))) ==="
if [ $fail -eq 0 ]; then echo "GATE SOUND on every arm."; else echo ">>> $fail ARM(S) DISAGREE -- read them above."; fi
