set -u
# Ledger irpt-resident-r34d-20261016, leg V2 (READ ONLY on the host; TWO Yahoo calls): run the door's real checker INSIDE THE RESIDENT SERVICE'S OWN ENVIRONMENT.
# Not a shell run: the user, the working directory and every Environment= entry are READ from the unit (systemctl show) and handed to a transient unit
# (systemd-run) that runs the same interpreter over the same root, so the process has the service's identity, cwd and import path, not the operator's.
# The code under test is the root's own intake/yfinance_check.py, loaded by path (the file the door imports), with the DEFAULT history port (the real yfinance call).
# Expected: SPY KEPT (HISTORY_ROWS) and ZQXWVK NOT_KEPT (NO_ROWS). Prints V2S OK only when both hold. Writes nothing on the host except the transient unit's own journal lines.
# Written for IRPT_ANLREQ round 37 (issuer 2.0.0_SA_COO~G2). NOT RUN: a CloudOps applier runs it under a signed never-widen pair, as root (systemd-run needs it).
U=irpt-analysis-resident.service
echo "V2S unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U)"
USR=$(systemctl show -p User --value $U)
WD=$(systemctl show -p WorkingDirectory --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
EXEC=$(systemctl show -p ExecStart --value $U)
WANT_ROOT=${V2S_WANT_ROOT:-/opt/irpt-resident/0485393f3a-r34d}
ROOT=$WD
echo "V2S user=$USR workdir=$WD interpreter=$PY"
echo "V2S environment entries: $(echo "$ENVS" | wc -w)"
if [ -z "$USR" ] || [ -z "$WD" ] || [ -z "$PY" ]; then echo "V2S FAIL a unit property is empty (user, workdir or interpreter)"; exit 61; fi
if [ "$ROOT" != "$WANT_ROOT" ]; then echo "V2S FAIL the working directory (the running root) is $ROOT, want $WANT_ROOT"; exit 62; fi
if ! echo "$EXEC" | grep -q "$ROOT/ycharts/generate/resident_main.py"; then echo "V2S FAIL ExecStart does not run resident_main.py from $ROOT"; exit 63; fi
SETENV=""
for e in $ENVS; do SETENV="$SETENV --setenv=$e"; done
PYF=${V2S_PYFILE:-/tmp/v2s_r34d.py}
cat > "$PYF" <<'PYEOF'
import importlib.util
import json
import os
import sys

root = os.getcwd()
path = root + "/intake/yfinance_check.py"
spec = importlib.util.spec_from_file_location("yfinance_check", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
import yfinance  # noqa: E402  (the service's own import path)
print("V2S process: uid=%d cwd=%s file=%s yfinance=%s from=%s" % (getattr(os, "getuid", lambda: -1)(), root, path, yfinance.__version__, os.path.dirname(yfinance.__file__)))
fixed = "_is_ticker_missing" in open(path, encoding="utf-8").read()
print("V2S the shipped checker carries the ticker-missing fix: %s" % ("yes" if fixed else "NO"))
out = mod.YfinanceChecker().check(["SPY", "ZQXWVK"])
print("V2S RESULT " + json.dumps(out, sort_keys=True))
spy, bad = out.get("SPY", {}), out.get("ZQXWVK", {})
ok = fixed and spy.get("state") == "KEPT" and spy.get("reason") == "HISTORY_ROWS" and bad.get("state") == "NOT_KEPT" and bad.get("reason") == "NO_ROWS"
print("V2S " + ("OK SPY KEPT and ZQXWVK NOT_KEPT" if ok else "FAIL want SPY KEPT HISTORY_ROWS and ZQXWVK NOT_KEPT NO_ROWS"))
sys.exit(0 if ok else 1)
PYEOF
chmod 644 "$PYF"
echo "V2S script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$WD" $SETENV "$PY" "$PYF"
RC=$?
echo "V2S transient unit rc=$RC"
rm -f "$PYF"
exit $RC
