# IRPT_ANLREQ -- decomposition, round 59, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** the CTO's ruling msg 9670 (relayed by `2.0.0_SA_COO~V2` msg 9673): a synthetic user minted after the ticket-service release carries `allowedFirmIds` = [the one firm] and the mint's read-back prints the scope and the entitlement rows. The FWD-5 second-firm mint helper (`fwd5_mint.py`, AR-ty-56) prints neither. The FWD-5 live run's pair is a draft until it does.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-69` | FWD-5 | the mint's read-back prints `MINT-SCOPE allowedFirmIds=.. entitlement_rows=..` and refuses nonzero entitlement rows; tests | `fwd5_mint.py`, `test_cross_firm_mint.py` | LOCAL (helper and tests; nothing run) |

## Edges and chains

- One chain (M = 1); no dependency (AR-ty-56 is merged). The live run (a WORLD act by the CloudOps lane under a pair) follows V2's release and this cell.

fanout: 1 of 1 chains, cap 4, reason: one amendment cell
