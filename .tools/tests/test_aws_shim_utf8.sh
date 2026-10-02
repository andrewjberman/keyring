#!/usr/bin/env bash
# MX-x-5(c) / Z-S75: both aws shims set UTF-8 for the Python-based CLI. Offline: reads the shims, never calls AWS.
# FAILURE ARM: a Python child printing a non-ASCII glyph (U+2713, outside cp1252) to a pipe under a cp1252 console
#   encoding raises UnicodeEncodeError. FIXED ARM: the same child under the environment the shim exports prints cleanly.
set -u
T="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY=python; command -v python >/dev/null 2>&1 || PY=python3
rc=0
glyph='print("✓ bullet")'

echo "== shim presence (both or neither) =="
sh_has=0; cmd_has=0
grep -q '^export PYTHONUTF8=1' "$T/aws" && sh_has=1
grep -q 'set "PYTHONUTF8=1"' "$T/aws.cmd" && cmd_has=1
echo "  .tools/aws sets PYTHONUTF8=1: $sh_has ; .tools/aws.cmd sets PYTHONUTF8=1: $cmd_has"
{ [ "$sh_has" = 1 ] && [ "$cmd_has" = 1 ]; } || { echo "  FAIL: shims not both set"; rc=1; }

echo "== failure arm: cp1252 child, non-ASCII to a pipe, no UTF-8 setting =="
err=$(env -u PYTHONUTF8 PYTHONIOENCODING=cp1252 $PY -c "$glyph" 2>&1 >/dev/null | tr -d '\r')
if printf '%s' "$err" | grep -q "UnicodeEncodeError"; then echo "  OK: reproduced: $(printf '%s' "$err" | tail -1)"
else echo "  FAIL: failure arm not reproduced"; rc=1; fi

echo "== fixed arm: the shim's own exports (read from .tools/aws), same child =="
envs=$(grep '^export PYTHONUTF8=\|^export PYTHONIOENCODING=' "$T/aws" | sed 's/^export //')
out=$(env $envs $PY -c "$glyph" 2>&1 | tr -d '\r'); prc=$?
echo "  env: $(printf '%s' "$envs" | tr '\n' ' ') rc=$prc bytes=$(printf '%s' "$out" | wc -c)"
if [ "$prc" = 0 ] && printf '%s' "$out" | grep -q "bullet"; then echo "  OK: printed cleanly"; else echo "  FAIL: $out"; rc=1; fi

[ "$rc" = 0 ] && echo "RESULT: PASS" || echo "RESULT: FAIL"
exit $rc
