# CT-w-10 stopped before the build: the data proxy's log group holds refresh_token and device_trust cookie material — 0.7.0_AE_CloudOps~U7

**archetype:** DIAGNOSE
**Date:** 2026-10-12
**Task Order:** NFRA_CTLPLN.TO-CT-w-10.data-proxy-logging-fix-apply-and-exercise
**Status:** BLOCKED-SOVEREIGN (Andrew's purge decision); nothing built, uploaded or applied

---

## Objective

Apply the third pair's logging fix (stop printing the whole event) after measuring what the log group already holds. Written for a reader with no prior context.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | service opal-portal-data-proxy | PARTIAL | 35 calls, 18 GRANTED, 17 UNRESOLVABLE-RESOURCE; a floor, unchanged |
| deploy_ledger.py | open, hold --pre-apply | PASS | entry nfra-ctlpln-ctw10-data-proxy-logging-fix-20261012 is HELD-PRE-APPLY, gate sovereign |

**What worked:** piping the log read straight into a counter, so no token or cookie value touched disk; counting by key name and age bucket only.
**What failed:** nothing.
**Gap found:** the CTO ruling and the pair assumed only 15-minute access tokens were in the logs; the events also carry the `cookies` list with `refresh_token` and `device_trust`.

---

## Work Completed

1. Read the order and both halves whole; verified pin `5a0dfc9af8` and its three member hashes; read the handler diff (the print replaced by one Request line).
2. BEFORE state: live CodeSha256 `aWwkzuxR...`, rollback artifact version `iuIjViflW5mz8ggUo9w.jxijqwIEKE8p`.
3. PRE over the whole 14-day group (1202 events): 49 JWT-shaped lines; 38 lines with Cookie/cookie/refresh; 0 with Set-Cookie. Key names: `refresh_token` 38 lines (16 aged 7 days or less), `device_trust` 29 lines (all 30 days or less).
4. Verdict per the order: a long-lived credential is a STOP. Built, uploaded and applied nothing; ledger put on HELD-PRE-APPLY (sovereign gate).
5. Filed row NFRA_CTLPLN-S9112 (ARMED, disarm owner Andrew).

## Decisions Made

- Obeyed the STOP although the fix would stop new credential lines: the order and the CTO half both say apply nothing. The decoupling (fix now, purge later) is recommended in the measure file, for the issuer and CTO to decide.

## Files Modified

`org/tier2_senior/0.7.0_AE_CloudOps~U7/deliverables/NFRA_CTLPLN.TO-CT-w-10.pre-apply-measure.txt`, the ledger entry and sentinel, the surprise channel (one row).

## Blockers

BLOCKED-SOVEREIGN: Andrew's answer on purging `/aws/lambda/opal-portal-data-proxy` events. Until then the old handler keeps writing a bearer and cookie line for each request.

## Current State

Live code unchanged (the second pair's). No walker armed, no row created, no token minted this order.

## Next Steps

1. `[2.0.0_SA_COO~C]` Relay the one-line ask to Andrew; with the CTO, decide whether to re-issue the GO with the purge decoupled.
2. `[0.7.0_AE_CloudOps~U7]` On a re-issued GO: release the hold, then build, apply and read the new lines.
