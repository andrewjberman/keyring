# IRPT_ANLREQ -- decomposition, round 22 SERVER DEFAULTS THE PRICE DATE, workstream YR round 19 (issuer 2.0.0_SA_COO~Y2)

**Input:** `AR-y-243` (the portal drops the "Price date for share quantities" field, Andrew's own test, row `D2-S78`) was BLOCKED by its own read: the server REFUSES a Shares upload without a date (`intake/portfolio.py` :208-212 `PRICE_DATE_REQUIRED`; the template lane `SHARES_PRICE_UNAVAILABLE`; the refusal is asserted at `intake/tests/test_portfolio.py` :144); row `IRPT_ANLREQ-D2-W75-S1` (BLOCKING, ARMED, disarm owner this seat), record `0.9.0_WK_IRPT_ANLREQ~75/r22/PORTAL_PRICE_DATE_CANDIDATE.json`. Andrew's rule: the answer is always the prior trading day's close, so the SERVER takes it.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-245` | the server prices a Shares upload with no date at the prior trading day's close from the estate's one calendar source, states the date used; a sent date behaves as before; the packaging of the calendar source in the Lambda and the resident is read | `intake/portfolio.py`, `intake/uploads.py` (if needed), one new test file, `test_portfolio.py` (the one assertion if it is the removed refusal) | WORLD |

## Edges and chains

- None. M = 1 chain. After it: a two-leg release pair (Lambda `irpt-ycharts-generate`, resident), then `AR-y-243` is re-cut (the portal omits the date) and lands after the server leg is live.

fanout: 1 of 1 chains, cap 8, reason: one server change, one test file.
