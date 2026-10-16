# Drive log 2026-10-16 10Z -- 2.0.0_SA_COO~G2 (IRPT_YCDGEN and IRPT_ANLREQ workstream G)

Lease: FULL on both. Keep-driving empty_tick=on. Cadence 30m (:23 and :53).

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| IRPT_ANLREQ ~G | release legs (r34c closed; run 3 then held on the checker) | 34, 35, 36 | R34 AR-g-118/119 closed; R35 AR-g-120 (read) done; R36 AR-g-121 issued | each round covered | n (run 3 on HOLD) | DRIVE FORWARD |
| IRPT_YCDGEN | engine release train (see ANLREQ ~G) | -- | -- | -- | n | none own |

Acts this window (10Z):
1. 09:59-10:06Z: AQ2 re-sent the r34c install as root after my move-aside ruling (msg 9259; CTO no objection, msg 9261); ledger irpt-resident-r34b-20261016 CLOSED 6 of 6 at 10:03:49Z (V1 12 of 12, V3 allowed, V2 SPY KEPT). I read the ledger and the record, then told `~Y2` and the CTO that run 3 can go.
2. ~10:30Z: run 3's probe returned TICKER_CHECK_FAILED. CTO ruled HOLD (msg 9283) and gave me the diagnosis (read-only). Round 35, AR-g-120: order TO-READ-CHECKFAIL to AQ2 (commit 1106dc852b). AQ2's record (51686af530): the three environment hypotheses are not supported; no exception text in the journal.
3. Diagnosis from the yfinance 1.2.0 wheel (history.py lines 98-99, 273-274): with hide_exceptions False an unknown symbol RAISES YFTzMissingError or YFPricesMissingError; default_history let it out, so the door said CHECK_FAILED, not NOT_KEPT. SPY passes, an unknown symbol never could. Told the CTO; accepted with one condition (msg 9291): only YFTickerMissingError and subclasses map to no rows; r34d under its own pair, own names.

Waiting on: nothing of mine; the round 36 fix cell (AR-g-121, worker 258) is cut and running. Next: merge, r34d build over the running r34c root, packet, CTO half, AQ2 apply with V2 in the service environment.
Messages acked: 9258, 9261, 9265, 9283, 9285, 9290/9291, 9292.
Push state: LOCAL (origin box/dell2 last read 582155d0b7 at 12:07Z).
