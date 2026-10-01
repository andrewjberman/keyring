#!/usr/bin/env bash
# =============================================================================
# test_safe_apply_targeted.sh -- self-test of the safe-apply naming plan stage for a TARGETED or PLANFILE apply
# (cell MS-s-1, NFRA_MCPMSP round 2; the gate owner's ruling).
#
# Runs the script named by env SAFE_APPLY_UNDER_TEST (default: .tools/safe-apply.sh next to this test's repo) in a
# SANDBOX: a temp tree holding a COPY of that script, a copy of halt-gate-check.sh, and a stub naming-apply-gate.py
# that runs the REAL .tools/naming-apply-gate.py (so the grader is real; only its location is the sandbox's). The
# other gates are isolated by fixtures, not edited out: the halt checkpoint reads an empty inbox for a serial file the
# sandbox provides; the tag-authz gate skips (the tree has no default_tags); the tombstone gate skips (the sandbox has
# no register). terraform is a FAKE (SAFE_APPLY_TERRAFORM): it records every argv, writes a fixture for `show -json`,
# and fails `plan` when FAKE_PLAN_FAIL=1. A plan carrying `-target=aws_s3_bucket.bad` (or a planfile that says bad)
# renders an out-of-pattern bucket addition; any other plan renders clean -- so a script that re-plans WITHOUT the
# caller's -target grades the wrong plan and the arms see it. NAMING_GATE_ENFORCE=1 throughout.
#
# One line per arm, PASS: <arm> or FAIL: <arm>, then RESULT: PASS only when all five pass (else RESULT: FAIL).
# Git Bash safe, ASCII only.
# =============================================================================
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
UNDER="${SAFE_APPLY_UNDER_TEST:-$REPO/.tools/safe-apply.sh}"
[ -f "$UNDER" ] || { echo "ERROR: script under test absent: $UNDER"; echo "RESULT: FAIL"; exit 1; }

SB="$(mktemp -d "${TMPDIR:-/tmp}/safe_apply_targeted.XXXXXX")" || { echo "ERROR: no temp dir"; echo "RESULT: FAIL"; exit 1; }
trap 'rm -rf "$SB"' EXIT

mkdir -p "$SB/.tools" "$SB/org/mcp/sessions" "$SB/org/tier1_exec/1.0.0_SA_CTO" "$SB/tree" "$SB/fakebin"
cp "$UNDER" "$SB/.tools/safe-apply.sh"
cp "$REPO/.tools/halt-gate-check.sh" "$SB/.tools/halt-gate-check.sh"
printf '%s\n' '# a tree with no resources and no default_tags' > "$SB/tree/main.tf"
printf '%s\n' '1.0.0_SA_CTO' > "$SB/org/mcp/sessions/sa-test.serial"

REAL_GATE="$(cd "$REPO/.tools" && { pwd -W 2>/dev/null || pwd; })/naming-apply-gate.py"
cat > "$SB/.tools/naming-apply-gate.py" <<PYEOF
import runpy
runpy.run_path(r"$REAL_GATE", run_name="__main__")
PYEOF

cat > "$SB/fakebin/terraform" <<'FAKEEOF'
#!/usr/bin/env bash
# FAKE terraform: record argv, write fixtures, optionally fail plan.
sub=""; out=""; bad=0; last=""
for a in "$@"; do
  case "$a" in
    -chdir=*) ;;
    -out=*) out="${a#-out=}" ;;
    -target=aws_s3_bucket.bad) bad=1 ;;
  esac
  [ -z "$sub" ] && case "$a" in -*) ;; *) sub="$a" ;; esac
  last="$a"
done
printf 'SUB=%s ARGS=%s\n' "$sub" "$*" >> "$FAKE_LOG"
case "$sub" in
  plan)
    if [ "${FAKE_PLAN_FAIL:-0}" = "1" ]; then echo "Error: fake plan failure" >&2; exit 1; fi
    if [ "$bad" = 1 ]; then echo bad > "$out"; else echo clean > "$out"; fi
    exit 0 ;;
  show)
    [ -f "$last" ] || { echo "Error: no such plan file: $last" >&2; exit 1; }
    if grep -q bad "$last"; then
      echo '{"resource_changes":[{"address":"aws_s3_bucket.bad","mode":"managed","type":"aws_s3_bucket","change":{"actions":["create"],"before":null,"after":{"bucket":"x-bad-name"}}}]}'
    else
      echo '{"resource_changes":[]}'
    fi
    exit 0 ;;
  apply) exit 0 ;;
esac
exit 0
FAKEEOF
chmod +x "$SB/fakebin/terraform"

FAKE_LOG="$SB/fake.log"; export FAKE_LOG
LAST_RC=0
# run_sa <extra-env-assignment-or-:> <args...> : fresh log, run the sandboxed script, capture rc into LAST_RC
run_sa() {
  : > "$FAKE_LOG"
  local envset="$1"; shift
  ( [ "$envset" != ":" ] && export "$envset"
    export SAFE_APPLY_TERRAFORM="$SB/fakebin/terraform" NAMING_GATE_ENFORCE=1 \
           CLAUDE_CODE_SESSION_ID=sa-test HALT_GATE_SHARED_ROOT="$SB" HALT_GATE_REPO_ROOT="$SB"
    unset TAGAUTHZ_OVERRIDE TOMBSTONE_OVERRIDE HALT_OVERRIDE
    bash "$SB/.tools/safe-apply.sh" "$@" > "$SB/run.out" 2>&1 )
  LAST_RC=$?
}
n_sub() { grep -c "^SUB=$1 " "$FAKE_LOG"; }

# Fail unless every listed condition held; each arm prints its own reasons on failure.
pass=0
arm() { # arm <name> <0|1 ok>
  if [ "$2" = 1 ]; then echo "PASS: $1"; pass=$((pass+1)); else echo "FAIL: $1"; sed 's/^/  | /' "$SB/run.out" | tail -n 12; sed 's/^/  | log: /' "$FAKE_LOG"; fi
}

TREE="$SB/tree"; MISSING="$SB/no-such-tree"

# --- arm 1: the plan stage carries the caller's -target and -var; a pre-plan error does not block a targeted apply
run_sa : "-chdir=$MISSING" apply -target=aws_s3_bucket.good -var x=y -auto-approve
ok=1
grep -qE '^SUB=plan ARGS=.* -target=aws_s3_bucket\.good( |$)' "$FAKE_LOG" || ok=0
grep -qE '^SUB=plan ARGS=.* -var x=y( |$)' "$FAKE_LOG" || ok=0
[ "$LAST_RC" = 0 ] && [ "$(n_sub apply)" = 1 ] || ok=0
arm targeted_plan_carries_caller_args "$ok"

# --- arm 2: a targeted apply whose rendered plan adds an out-of-pattern name is refused in ENFORCE, nothing applied
run_sa : "-chdir=$TREE" apply -target=aws_s3_bucket.bad -auto-approve
ok=1
[ "$LAST_RC" = 7 ] || ok=0
[ "$(n_sub apply)" = 0 ] || ok=0
arm targeted_out_of_pattern_refuses_enforce "$ok"

# --- arm 3: a planfile apply grades the GIVEN planfile (show -json, no re-plan); here it is a bad one, so it refuses
echo bad > "$SB/plan.bin"
run_sa : "-chdir=$TREE" apply "$SB/plan.bin"
ok=1
grep -qE "^SUB=show ARGS=.* show -json $SB/plan\.bin\$" "$FAKE_LOG" || ok=0
[ "$(n_sub plan)" = 0 ] || ok=0
[ "$LAST_RC" = 7 ] && [ "$(n_sub apply)" = 0 ] || ok=0
arm planfile_apply_grades_given_planfile "$ok"

# --- arm 4: an UNTARGETED apply is unchanged: its plan carries none of the caller's args, and the pre-plan stage binds
run_sa : "-chdir=$TREE" apply -var x=y -auto-approve
ok=1
[ "$(n_sub plan)" = 1 ] || ok=0
grep -qE "^SUB=plan ARGS=-chdir=$TREE plan -input=false -lock=false -out=[^ ]+\$" "$FAKE_LOG" || ok=0
[ "$LAST_RC" = 0 ] && [ "$(n_sub apply)" = 1 ] || ok=0
run_sa : "-chdir=$MISSING" apply -var x=y -auto-approve
[ "$LAST_RC" = 6 ] || ok=0
[ "$(n_sub plan)" = 0 ] && [ "$(n_sub apply)" = 0 ] || ok=0
arm untargeted_apply_unchanged "$ok"

# --- arm 5: a targeted apply whose plan cannot render is refused in ENFORCE, nothing applied
run_sa FAKE_PLAN_FAIL=1 "-chdir=$TREE" apply -target=aws_s3_bucket.good -auto-approve
ok=1
[ "$(n_sub plan)" -ge 1 ] || ok=0
[ "$LAST_RC" = 7 ] && [ "$(n_sub apply)" = 0 ] || ok=0
arm targeted_unrenderable_refuses_enforce "$ok"

if [ "$pass" = 5 ]; then echo "RESULT: PASS"; exit 0; fi
echo "RESULT: FAIL ($pass of 5 arms passed)"; exit 1
