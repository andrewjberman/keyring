#!/usr/bin/env bash
# =============================================================================
# test_safe_apply_scoped_gates.sh -- self-test: safe-apply's TAG-AUTHZ and TOMBSTONE stages grade the plan the apply
# RUNS (cell MS-s-2, NFRA_MCPMSP round 3, E1; row NFRA_MCPMSP-Z-W7-S1).
#
# Runs the script named by env SAFE_APPLY_UNDER_TEST (default: .tools/safe-apply.sh next to this test's repo) as a COPY
# placed in a SCRATCH ROOT: <root>/.tools/safe-apply.sh, a fake <root>/.tools/comp-tagauthz, a fake
# <root>/.tools/tombstone-gate.py, a pass-through <root>/.tools/naming-apply-gate.py, a copy of halt-gate-check.sh,
# <root>/infra/aws/terraform/tombstones.json, and a tree whose main.tf carries a provider default_tags block.
# SAFE_APPLY_TERRAFORM is a FAKE terraform that records its argv. A plan is a list of resource addresses: a whole-tree
# plan (no -target) lists TRIP and OTHER, a targeted plan lists only the targeted addresses, a planfile is whatever the
# arm wrote into it; `show -json` renders those addresses as resource_changes. Both fake gates refuse (rc 2) exactly
# when the JSON handed to them contains TRIP; FAKE_TAG_OFF=1 / FAKE_TS_OFF=1 make one fake pass so an arm can isolate
# the other stage. Every other gate is isolated by the scratch root's own files and env (no org/mcp/*.enforce file
# exists in the scratch root; the main tree's org/mcp is never read), never by editing the script under test.
#
# One line per arm, PASS: <arm> or FAIL: <arm>, then RESULT: PASS only when all six pass. Bounded to 50 seconds.
# Git Bash safe, ASCII only.
# =============================================================================
set -u
if [ -z "${SA_SCOPED_TEST_INNER:-}" ]; then
  out="$(SA_SCOPED_TEST_INNER=1 timeout 48 bash "${BASH_SOURCE[0]}" "$@" 2>&1)"; rc=$?
  printf '%s\n' "$out"
  if [ "$rc" -eq 124 ]; then echo "RESULT: FAIL (timed out inside the 48 second bound)"; exit 1; fi
  exit "$rc"
fi

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
UNDER="${SAFE_APPLY_UNDER_TEST:-$REPO/.tools/safe-apply.sh}"
[ -f "$UNDER" ] || { echo "ERROR: script under test absent: $UNDER"; echo "RESULT: FAIL"; exit 1; }

SB="$(mktemp -d "${TMPDIR:-/tmp}/safe_apply_scoped.XXXXXX")" || { echo "ERROR: no temp dir"; echo "RESULT: FAIL"; exit 1; }
trap 'rm -rf "$SB"' EXIT

mkdir -p "$SB/.tools" "$SB/org/mcp/sessions" "$SB/org/tier1_exec/1.0.0_SA_CTO" "$SB/infra/aws/terraform" "$SB/tree" "$SB/fakebin"
cp "$UNDER" "$SB/.tools/safe-apply.sh"
cp "$REPO/.tools/halt-gate-check.sh" "$SB/.tools/halt-gate-check.sh"
printf '%s\n' '1.0.0_SA_CTO' > "$SB/org/mcp/sessions/sa-test.serial"
printf '%s\n' '{}' > "$SB/infra/aws/terraform/tombstones.json"
cat > "$SB/tree/main.tf" <<'TFEOF'
provider "aws" {
  default_tags {
    tags = { Project = "x" }
  }
}
TFEOF

# the naming gate: a pass-through (the naming stages are not under test here)
printf '%s\n' 'import sys' 'sys.exit(0)' > "$SB/.tools/naming-apply-gate.py"

cat > "$SB/.tools/comp-tagauthz" <<'FAKEEOF'
#!/usr/bin/env bash
# FAKE comp-tagauthz: check --default-tags-tree T --from-plan J ; rc 2 exactly when J contains TRIP
j=""; prev=""
for a in "$@"; do [ "$prev" = "--from-plan" ] && j="$a"; prev="$a"; done
echo "FAKE-TAGAUTHZ read $j" >> "$FAKE_LOG"
[ "${FAKE_TAG_OFF:-0}" = "1" ] && exit 0
[ -f "$j" ] || exit 1
grep -q TRIP "$j" && exit 2
exit 0
FAKEEOF
chmod +x "$SB/.tools/comp-tagauthz"

cat > "$SB/.tools/tombstone-gate.py" <<'FAKEEOF'
import os, sys
a = sys.argv[1:]
j = a[a.index("--plan-json") + 1] if "--plan-json" in a else ""
with open(os.environ["FAKE_LOG"], "a") as f:
    f.write("FAKE-TOMBSTONE read %s\n" % j)
if os.environ.get("FAKE_TS_OFF") == "1":
    sys.exit(0)
try:
    txt = open(j).read()
except Exception:
    sys.exit(3)
sys.exit(2 if "TRIP" in txt else 0)
FAKEEOF

cat > "$SB/fakebin/terraform" <<'FAKEEOF'
#!/usr/bin/env bash
# FAKE terraform: record argv; a plan is a list of addresses written to -out; `show -json` renders them.
sub=""; out=""; last=""; tg=()
for a in "$@"; do
  case "$a" in
    -out=*) out="${a#-out=}" ;;
    -target=*) tg+=("${a#-target=}") ;;
  esac
  [ -z "$sub" ] && case "$a" in -*) ;; *) sub="$a" ;; esac
  last="$a"
done
printf 'SUB=%s ARGS=%s\n' "$sub" "$*" >> "$FAKE_LOG"
case "$sub" in
  plan)
    if [ "${#tg[@]}" -gt 0 ]; then printf '%s\n' "${tg[@]}" > "$out"; else printf 'TRIP\nOTHER\n' > "$out"; fi
    exit 0 ;;
  show)
    [ -f "$last" ] || { echo "Error: no such plan file: $last" >&2; exit 1; }
    printf '{"resource_changes":['
    first=1
    while IFS= read -r addr; do
      [ -z "$addr" ] && continue
      [ "$first" = 1 ] || printf ','
      first=0
      printf '{"address":"%s","mode":"managed","type":"aws_instance","change":{"actions":["create"]}}' "$addr"
    done < "$last"
    printf ']}\n'
    exit 0 ;;
  apply) exit 0 ;;
esac
exit 0
FAKEEOF
chmod +x "$SB/fakebin/terraform"

# The six arms are independent (each has its own log and output file under the scratch root), so they run in
# parallel: process spawn dominates the cost on this device and a serial run came within seconds of the bound.
LAST_RC=0
# run_sa <extra-env-assignment-or-:> <args...> : fresh log, run the sandboxed script, capture rc into LAST_RC
run_sa() {
  : > "$FAKE_LOG"
  local envset="$1"; shift
  ( [ "$envset" != ":" ] && export "$envset"
    export FAKE_LOG SAFE_APPLY_TERRAFORM="$SB/fakebin/terraform" OPAL_SEAT_GATES_ENFORCE_DIR="$SB/org/mcp" \
           CLAUDE_CODE_SESSION_ID=sa-test HALT_GATE_SHARED_ROOT="$SB" HALT_GATE_REPO_ROOT="$SB" TMPDIR="$SB"
    unset TAGAUTHZ_OVERRIDE TOMBSTONE_OVERRIDE HALT_OVERRIDE SEAT_GATES_OVERRIDE NAMING_GATE_ENFORCE DEPLOY_COMMIT
    bash "$SB/.tools/safe-apply.sh" "$@" > "$RUN_OUT" 2>&1 )
  LAST_RC=$?
}
n_sub() { grep -c "^SUB=$1 " "$FAKE_LOG"; }
said() { grep -q "$1" "$RUN_OUT"; }

# arm <name> <0|1 ok> : writes the arm's verdict lines to $SB/res.<arm number>
arm() {
  if [ "$2" = 1 ]; then echo "PASS: $1" > "$SB/res.$ARMNO"
  else { echo "FAIL: $1 (rc=$LAST_RC)"; sed 's/^/  | /' "$RUN_OUT" | tail -n 12; sed 's/^/  | log: /' "$FAKE_LOG"; } > "$SB/res.$ARMNO"; fi
}
# begin_arm <number> : per-arm log and output file
begin_arm() { ARMNO="$1"; FAKE_LOG="$SB/fake.$1.log"; RUN_OUT="$SB/run.$1.out"; }

TREE="$SB/tree"
printf 'aws_instance.a\n' > "$SB/plan.bin"

# --- arm 1: a targeted apply whose OWN plan is clean passes the tag-authz stage although the whole tree's plan has TRIP
arm1() {
  begin_arm 1
  run_sa FAKE_TS_OFF=1 "-chdir=$TREE" apply -target=aws_instance.a -auto-approve
  ok=1
  [ "$LAST_RC" = 0 ] && [ "$(n_sub apply)" = 1 ] || ok=0
  grep -q '^FAKE-TAGAUTHZ read ' "$FAKE_LOG" || ok=0
  said 'comp-tagauthz gate PASSED' || ok=0
  arm tagauthz_targeted_grades_own_plan "$ok"
}

# --- arm 2: a targeted apply whose own plan carries TRIP is blocked by the tag-authz stage, nothing applied
arm2() {
  begin_arm 2
  run_sa FAKE_TS_OFF=1 "-chdir=$TREE" apply -target=TRIP -auto-approve
  ok=1
  [ "$LAST_RC" = 2 ] && [ "$(n_sub apply)" = 0 ] || ok=0
  said 'BLOCKED by comp-tagauthz' || ok=0
  arm tagauthz_targeted_refuses_own_plan "$ok"
}

# --- arm 3: as arm 1, for the tombstone stage
arm3() {
  begin_arm 3
  run_sa FAKE_TAG_OFF=1 "-chdir=$TREE" apply -target=aws_instance.a -auto-approve
  ok=1
  [ "$LAST_RC" = 0 ] && [ "$(n_sub apply)" = 1 ] || ok=0
  grep -q '^FAKE-TOMBSTONE read ' "$FAKE_LOG" || ok=0
  arm tombstone_targeted_grades_own_plan "$ok"
}

# --- arm 4: as arm 2, for the tombstone stage
arm4() {
  begin_arm 4
  run_sa FAKE_TAG_OFF=1 "-chdir=$TREE" apply -target=TRIP -auto-approve
  ok=1
  [ "$LAST_RC" = 2 ] && [ "$(n_sub apply)" = 0 ] || ok=0
  said 'TOMBSTONE GATE BLOCKED' || ok=0
  arm tombstone_targeted_refuses_own_plan "$ok"
}

# --- arm 5: a planfile apply: both stages read the GIVEN planfile (show -json, no re-plan by either stage)
arm5() {
  begin_arm 5
  run_sa : "-chdir=$TREE" apply "$SB/plan.bin"
  ok=1
  [ "$LAST_RC" = 0 ] && [ "$(n_sub apply)" = 1 ] || ok=0
  grep -qE "^SUB=show ARGS=.* show -json $SB/plan\.bin\$" "$FAKE_LOG" || ok=0
  [ "$(n_sub plan)" = 0 ] || ok=0
  grep -q '^FAKE-TAGAUTHZ read ' "$FAKE_LOG" && grep -q '^FAKE-TOMBSTONE read ' "$FAKE_LOG" || ok=0
  arm planfile_stages_read_given_planfile "$ok"
}

# --- arm 6: an UNSCOPED apply is unchanged: the whole tree's plan (TRIP) is graded and blocks, nothing applied
arm6() {
  begin_arm 6
  run_sa FAKE_TS_OFF=1 "-chdir=$TREE" apply -auto-approve
  ok=1
  [ "$LAST_RC" = 2 ] && [ "$(n_sub apply)" = 0 ] || ok=0
  [ "$(n_sub plan)" -ge 1 ] || ok=0
  said 'BLOCKED by comp-tagauthz' || ok=0
  arm unscoped_apply_unchanged "$ok"
}

for n in 1 2 3 4 5 6; do ( arm$n ) & done
wait
pass=0
for n in 1 2 3 4 5 6; do
  if [ -f "$SB/res.$n" ]; then cat "$SB/res.$n"; head -n 1 "$SB/res.$n" | grep -q '^PASS: ' && pass=$((pass+1)); else echo "FAIL: arm$n (no result: the arm did not finish)"; fi
done
if [ "$pass" = 6 ]; then echo "RESULT: PASS"; exit 0; fi
echo "RESULT: FAIL ($pass of 6 arms passed)"; exit 1
