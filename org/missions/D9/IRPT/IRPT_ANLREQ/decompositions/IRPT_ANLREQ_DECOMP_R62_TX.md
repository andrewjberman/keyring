# IRPT_ANLREQ -- decomposition, round 62, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** `1.0.0_SA_CTO~DELL2` msg 9907 and row IRPT_ANLREQ-D2-S157 (@e5c3a20521): the FWD-5 live sitting's four report-side 200s were CONTRACT_VERSION refusal envelopes for BOTH identities (body lengths 434/414/424/446 are the CONTRACT_VERSION lengths; FIRM_BINDING would be 430/410/420/442), because the driver sent no `X-Contract-Version: v1` and graded any 2xx by status. S156 is disarmed; FWD-5 stays ungraded and S134 stays ARMED.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-72` | FWD-5 | the driver sends the contract version on every GET and grades the four report-side routes by the envelope (`ok`, `status.public_reason_code`): fence codes REFUSED, other refusals UNREACHED, ok true LEAK or ALLOWED; tests | `fwd5_driver.py`, `test_fwd5_driver_envelope.py`, the three older driver test files (named edits only) | LOCAL (driver rule and tests; nothing run) |

## Edges and chains

- One chain (M = 1); no dependency. The second live sitting (a WORLD act by the IRPT CloudOps lane under a re-signed pair) follows this cell and the packet's update.

fanout: 1 of 1 chains, cap 4, reason: one repair cell
