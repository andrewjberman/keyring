# ANDREW DIRECT -- price source order: Yahoo first, YCharts second, then the replacement; a report never blocks on a missing security (2026-10-14 ~17:5xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. He was answering the measured probes:
- yfinance covered every gap, with full history, in one 2.21 s batched call;
- the YCharts session (`ycharts/credentials`) works at one symbol per call, 5 years, about 2.3 s each.

Research @17a04396f2.

**Verbatim:**

> Ok we use Yahoo as first round pick, we use Ycharts as second round pick. If neither work, and our replacement function doesnt work for whatever reason, then we generate the report without the missing security. However, this should realistically never happen, because we should be able to figure out a replacement. Does the AI function for swapping out typos/replacing tickers work?

## What it sets (surfaced, not adjudicated)

1. Prices for a security the estate lacks come from **Yahoo first**, then **YCharts** (the stored session, one symbol per call).
2. If neither prices it, the **replacement function** (the security swap, C-SWAP) supplies a substitute.
3. If all three fail, the **report is generated without the missing security**. It does not block. He expects this to "realistically never
   happen".

## What it touches

- IRPT_ANLREQ C-PRICES and FWD-7 (v0.9+).
- Ruling 7546's order put YCharts AFTER SECHIST and BEFORE yfinance, as one batched call. That ordering is now reversed (Yahoo first),
  and YCharts cannot batch.
- FWD-2 / C-SWAP. The "report without the security" end state needs the report to name what it left out (FWD-4, a failed hop is
  visible).

-- recorded by 4.0.0_SA_CRO~DELL2
