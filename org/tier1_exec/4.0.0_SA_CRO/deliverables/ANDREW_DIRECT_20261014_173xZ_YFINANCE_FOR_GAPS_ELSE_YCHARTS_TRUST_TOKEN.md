# ANDREW DIRECT -- yfinance for the price gaps if it works; otherwise the YCharts long-term trust token and its EC2/Lambda REST pattern (2026-10-14 ~17:3xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. He was answering the price-coverage finding
(@895de345f4): no keyed YCharts data API exists, ^SPXTR and four holdings are absent, and four holdings are thin.

**Verbatim:**

> We can use yahoofinance for this if it works. If it does not work, keep in mind we keep a long-term trust token, and the associated ec2 crawl/lambda rest api pattern for authenticated access. I recommend pulling that trust token and seeing if you can just hit the necessary API right now and what the throughput/timeline is for a roundtrip of that call

## What it sets (surfaced, not adjudicated)

- **yfinance is an accepted price source for the gaps, if it works.**
- **The fallback is YCharts**, through the existing long-term trust token and its EC2 crawl / Lambda REST pattern for authenticated access.
- **This seat is asked to:**
  - test yfinance;
  - pull the trust token and hit the needed YCharts API now;
  - measure the throughput and timeline of one round trip.

## What it touches

- IRPT_ANLREQ PRD C-PRICES / FWD-7 (v0.9+): one YCharts data call per request, after SECHIST and before yfinance. Under this word,
  yfinance is acceptable and YCharts is the fallback.
- Trace hop 9.

-- recorded by 4.0.0_SA_CRO~DELL2
