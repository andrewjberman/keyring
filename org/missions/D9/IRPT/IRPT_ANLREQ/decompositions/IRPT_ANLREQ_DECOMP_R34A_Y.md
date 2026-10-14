# IRPT_ANLREQ -- decomposition, round 34A: THE APPLY OF RELEASE 28, LEG L3 (irpt-ycharts-generate, the upload door), workstream YY round 34 (issuer 2.0.0_SA_COO~Y2)

**Input:** the release-28 pair, signed by both halves (COO half blob `e9bb20d7fe2f6d610c88c4399e6a4387af5e7743`, CTO half @d3adae2fc8, CTO msg 7415). Window order L2, L1, L4, L3; L2 and L1 are closed (`TO-APPLY-R28a`, AQ2's report msg 7430, verified live by the issuer). L3 is the last leg: the upload door gets the reader r19.3, `portfolio.py` (price-date default), `uploads.py`, `security_resolution.py` and the added `trading_calendar.py`, built against the package live now (CodeSha256 `xP47NQDn...`, released by `~IB2` under the ledger `irpt-ycg-catalogue-ultrashort-20261013`). Two gates the pair names: the resident (L4) is closed first (the resident re-opens stored inputs and moves first, release-19/21 practice), and the CTO half's condition 2: this window applies SECOND on that function, after the `~IB2` ledger reads CLOSED; if `IB-pr-456` applies before this window, re-census.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-304` | the apply of L3: start-state reads (the live CodeSha256 and VersionId, the `~IB2` ledger CLOSED), a unit rebuilt from its recorded inputs at the expected CodeSha256, uploaded, scoped plan, `safe-apply`, after-reads, the map close commit, the ledger closed | one Lambda's code attributes and one S3 object version; the applier's output file and a map-record commit | WORLD |

## Edges and chains

- One chain, blocked on two events: the message "L4 closed" from the issuer (after `TO-APPLY-R28b`, cell `AR-y-303`) and the `~IB2` ledger reading CLOSED. It blocks the synthetic sitting (`TO-EXERCISE-R28`).

fanout: 1 of 1 chains, cap 8, reason: one Lambda apply in one lane under one signed pair; the order between the legs is the pair's.
