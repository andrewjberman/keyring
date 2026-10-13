#!/usr/bin/env bash
# OPAL_BBGTML Z6 repair 5 -- check, two legs, both on the SHARED-TREE bytes:
#  ARM leg:    one --once pass of teams-watch.py with the BG seat's exact pin and channels, run against a
#              THROWAWAY TMPDIR (its own cursors, seeded at now -- it never touches the live BG watcher's
#              cursor files), must print EXACTLY ONE stdout line beginning "[TEAMS-ARMED]".
#  RUNNER leg: the intake runner's own import path (runner._load_teams_watch) must write ZERO bytes to
#              stdout -- the runner imports the module every 5 minutes and must be unchanged.
# Usage (repo root): bash org/tier1_exec/2.0.0_SA_COO~ZB/deliverables/z6_checks/r5_teams_armed_check.sh
set -u
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT" || exit 3
PY="${R5_PYTHON:-python}"
T="$(mktemp -d)"
TMPDIR="$(cygpath -w "$T")" timeout 90 "$PY" .claude/skills/teams-assist/teams-watch.py \
  --server opal-gateway-bbg --identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f \
  --channels .claude/skills/teams-assist/channels.json --once >"$T/out" 2>"$T/err"
arc=$?
armed="$(grep -c '^\[TEAMS-ARMED\]' "$T/out" | tr -d '\r')"
echo "ARM leg: rc=$arc stdout_lines=$(wc -l <"$T/out" | tr -d ' ') TEAMS-ARMED_lines=$armed"
grep '^\[TEAMS-ARMED\]' "$T/out" | head -3
echo "stderr tail:"; tail -3 "$T/err"
rbytes="$("$PY" - <<'EOF'
import contextlib, io, sys
sys.path.insert(0, ".")
from integrations.ticketing.intake import runner
b = io.StringIO()
with contextlib.redirect_stdout(b):
    runner._load_teams_watch()
print(len(b.getvalue()))
EOF
)"
rbytes="$(echo "$rbytes" | tr -d '\r' | tail -1)"
echo "RUNNER leg: stdout bytes on the runner's import path = $rbytes"
rm -rf "$T"
ok=0
[ "$arc" -eq 0 ] && [ "$armed" = "1" ] && echo "ARM leg: PASS" || { echo "ARM leg: FAIL"; ok=1; }
[ "$rbytes" = "0" ] && echo "RUNNER leg: PASS" || { echo "RUNNER leg: FAIL"; ok=1; }
[ $ok -eq 0 ] && echo "R5: PASS" || echo "R5: FAIL"
exit $ok
