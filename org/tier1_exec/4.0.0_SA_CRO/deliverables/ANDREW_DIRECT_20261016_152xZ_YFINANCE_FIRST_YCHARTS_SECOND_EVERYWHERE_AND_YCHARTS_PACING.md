# ANDREW_DIRECT 2026-10-16 ~15:2xZ -- yfinance first, YCharts second, as a general rule for every part of the Analysis Request process; examine the YCharts request pacing

**Channel:** Andrew at the dell2 terminal, in session with `4.0.0_SA_CRO~DELL2`. **Recorded:** 2026-10-16 15:23Z (`date -u`).

## Verbatim

The CRO's question to Andrew (context): the upload door's holding check asks YCharts first and yfinance only on a YCharts
NOT_FOUND (`infra/aws/lambda/investor-reporting/intake/security_resolution.py:79-83`), and the Yahoo-first pricing chain is
built but off in the resident build (`infra/aws/lambda/investor-reporting/reports/build_resident_package.py:119`,
`"opal_pricing": {"enabled": False, ...}`). Should it go to the CTO as a design fork?

Andrew:

> Yeah we should consolidate on yfinance first and ycharts second as a general rule for any part of this process. Also want to examine the requests/second pacing for ycharts calls, because maybe that is not calibrated well.

## What it touches (surfaced, not adjudicated)

- IRPT_ANLREQ: the upload door's identity check (C-SWAP step 2), report pricing (C-PRICES, FWD-7), and any other YCharts-first
  call in the process. Owner of the ruling: `1.0.0_SA_CTO~DELL2`.
- The YCharts pacing read is research for this seat (`4.0.0_SA_CRO~DELL2`), delivered to the CTO as a file.

Prior record of the same order for prices: `ANDREW_DIRECT_20261014_175xZ_PRICE_ORDER_YAHOO_THEN_YCHARTS_THEN_REPLACEMENT.md`.
