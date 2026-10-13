#!/usr/bin/env bash
# OPAL_BBGTML Z6 repair 2 -- check: the fallback's P0 gate classifies "8194 LISTENING + dapi_check FAILING"
# as "listener up, not entitled" (sign-in warranted) instead of refusing as a transient flicker.
# Runs the SHARED-TREE bytes (the deployed file) with -ForceDown -StubSubmit: no GUI, no fill, no submit,
# no ledger write, no Bloomberg request (-ForceDown short-circuits every dapi_check call).
# Discriminates ONLY while 8194 is listening (on site Z the BG seat's MCP server holds it); with no
# listener the check prints NOT-EXERCISED and exits 2 -- never a PASS.
# Usage (repo root): bash org/tier1_exec/2.0.0_SA_COO~ZB/deliverables/z6_checks/r2_p0_listener_check.sh
set -u
ROOT="$(git rev-parse --show-toplevel)"
PS1F="$(cygpath -w "$ROOT/integrations/bloomberg/auth/bbg_fallback.ps1")"
listen="$(powershell -NoProfile -Command "@(Get-NetTCPConnection -LocalPort 8194 -State Listen -EA SilentlyContinue).Count" | tr -d '\r')"
echo "8194 listeners before run: $listen"
if [ "${listen:-0}" -lt 1 ]; then echo "R2: NOT-EXERCISED (no 8194 listener -- the check cannot discriminate)"; exit 2; fi
TF="$(mktemp)"
timeout 110 powershell -NoProfile -ExecutionPolicy Bypass -File "$PS1F" -ForceDown -StubSubmit >"$TF" 2>&1
rc=$?
out="$(tr -d '\r' <"$TF")"; rm -f "$TF"
echo "$out"
echo "fallback rc=$rc"
if echo "$out" | grep -q 'not sustained-absent'; then echo "R2: FAIL (the P0 gate still refused a listening 8194 as transient)"; exit 1; fi
if ! echo "$out" | grep -q 'listener up, not entitled'; then echo "R2: FAIL (no 'listener up, not entitled' classification line)"; exit 1; fi
if echo "$out" | grep -q 'STUB: would now fill' || echo "$out" | grep -q 'fire-once:'; then
  echo "R2: PASS (classified listener-up-not-entitled and reached the sign-in path)"; exit 0
fi
echo "R2: FAIL (classified, but neither the stub sign-in point nor the fire-once guard was reached)"; exit 1
