set -u
# Ledger-free READ (IRPT_ANLREQ TO-READ-EXCCLASS, issuer 2.0.0_SA_COO~G2): name the REAL exception class yfinance raises for ZQXWVK inside the resident service's own
# environment, with the r34d root's checker code (CTO msg 9345). READ ONLY on the host: TWO Yahoo calls (ZQXWVK, then SPY as the control), no write but a temp file, no job, no queue message.
# The user, Environment entries and interpreter are READ from the unit (systemctl show) and handed to a transient unit (systemd-run); only PYTHONPATH and the working
# directory are pointed at the r34d root (kept on the host after its rollback), so the checker's _failure_reason and _is_ticker_missing are the shipped r34d ones.
# Prints the exception's module, name, whole MRO (module.name), the first 200 characters of the message (a crumb= token is redacted), the cause and context class names,
# the last four stack frames (file:line in function, no locals), what the r34d checker would answer for it, and yfinance's own _ERRORS entry for the symbol.
# Written for IRPT_ANLREQ round 38 (issuer 2.0.0_SA_COO~G2). NOT RUN: a CloudOps applier runs it, as root (systemd-run needs it).
U=irpt-analysis-resident.service
PROBE_ROOT=${PROBE_ROOT_OVERRIDE:-/opt/irpt-resident/0485393f3a-r34d}
echo "PROBE unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U) running root: $(systemctl show -p WorkingDirectory --value $U)"
USR=$(systemctl show -p User --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
echo "PROBE user=$USR interpreter=$PY probe root=$PROBE_ROOT"
if [ -z "$USR" ] || [ -z "$PY" ]; then echo "PROBE FAIL a unit property is empty (user or interpreter)"; exit 61; fi
if [ ! -f "$PROBE_ROOT/intake/yfinance_check.py" ] || ! grep -q "def _is_ticker_missing" "$PROBE_ROOT/intake/yfinance_check.py"; then echo "PROBE FAIL $PROBE_ROOT does not hold the r34d checker"; exit 62; fi
SETENV=""
for e in $ENVS; do
  case "$e" in PYTHONPATH=*) e="PYTHONPATH=$PROBE_ROOT";; esac
  SETENV="$SETENV --setenv=$e"
done
PYF=${PROBE_PYFILE:-/tmp/probe_exc_class_r34d.py}
cat > "$PYF" <<'PYEOF'
import importlib.util
import os
import re
import sys
import time
import traceback

root = os.getcwd()
spec = importlib.util.spec_from_file_location("yfinance_check", root + "/intake/yfinance_check.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
import yfinance as yf  # noqa: E402  (the service's own import path)
print("PROBE process: uid=%s cwd=%s yfinance=%s from=%s" % (getattr(os, "getuid", lambda: -1)(), root, yf.__version__, os.path.dirname(yf.__file__)))


def clean(text):
    return re.sub(r"crumb=[^&\s'\"]*", "crumb=REDACTED", str(text))


def probe(sym):
    previous = yf.config.debug.hide_exceptions
    shared = getattr(yf, "shared", None)
    errors = getattr(shared, "_ERRORS", None)
    if isinstance(errors, dict):
        errors.pop(sym, None)
    yf.config.debug.hide_exceptions = False
    try:
        frame = yf.Ticker(sym).history(period="1mo", auto_adjust=False)
        print("PROBE %s NO EXCEPTION rows=%d _ERRORS=%r" % (sym, len(frame), clean(errors.get(sym)) if isinstance(errors, dict) else None))
    except BaseException as exc:  # a probe prints whatever is raised
        kind = type(exc)
        print("PROBE %s EXCEPTION module=%s name=%s" % (sym, kind.__module__, kind.__name__))
        print("PROBE %s MRO %s" % (sym, ",".join("%s.%s" % (c.__module__, c.__name__) for c in kind.__mro__)))
        print("PROBE %s MESSAGE[:200] %r" % (sym, clean(exc)[:200]))
        print("PROBE %s CAUSE %s CONTEXT %s" % (sym, type(exc.__cause__).__name__ if exc.__cause__ else None, type(exc.__context__).__name__ if exc.__context__ else None))
        frames = traceback.extract_tb(exc.__traceback__)[-4:]
        print("PROBE %s FRAMES %s" % (sym, " | ".join("%s:%d in %s" % (os.path.basename(f.filename), f.lineno, f.name) for f in frames)))
        print("PROBE %s CHECKER _is_ticker_missing=%s _failure_reason=%s" % (sym, mod._is_ticker_missing(exc), mod._failure_reason(exc)))
        print("PROBE %s _ERRORS=%r" % (sym, clean(errors.get(sym)) if isinstance(errors, dict) else None))
    finally:
        yf.config.debug.hide_exceptions = previous


probe("ZQXWVK")
time.sleep(1)
probe("SPY")
print("PROBE DONE")
PYEOF
chmod 644 "$PYF"
echo "PROBE script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$PROBE_ROOT" $SETENV "$PY" "$PYF"
RC=$?
echo "PROBE transient unit rc=$RC"
rm -f "$PYF"
exit $RC
