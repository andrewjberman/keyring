# ANDREW DIRECT -- a single data call to YCharts for pricing data is OK (2026-10-14 ~15:5xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`.

**Context:** the /closer trace of the analysis-request workflow (@6766f4486d) found two gaps on the report's price side (hop 9):
- the Opal producer renders 6 of 257 sections because no price source is composed;
- the YCharts path is a signed-in browser session, down since 10-11.

Andrew asked this seat's approach to the price source. This seat recommended MDPF_SECHIST first, then a paced yfinance pull saved into
SECHIST, then Bloomberg through its queue, then a labelled proxy. It recommended no YCharts on the report path, and named the gateway's
YCharts data call as technically possible but a reversal of his 10-09 word.

**Verbatim:**

> I am ok with a single data call to YCharts for pricing data.

## What it sets (surfaced, not adjudicated)

- A single YCharts data call for PRICING DATA is permitted. This is a data call, distinct from the retired signed-in browser path that
  builds a portfolio and downloads the vendor PDF.
- Not stated, and left for the owners to read or to ask him once:
  - whether the call is the primary price source or a fallback after the estate's stores;
  - whether "single" means one call per request or one call per missing security;
  - whether it covers figures beyond prices (returns, risk).

## What it touches

- IRPT_ANLREQ PRD v0.8 `C-PRICES` (`:107`, "No YCharts price or figure") and FWD-7 (no YCharts call end to end). Both rest on Andrew's
  10-09 word (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261009_SECURITY_SWAP_AND_NO_YCHARTS.md`@9ae5d353d1). This later word
  relaxes them for pricing data.
- The CTO's ruling 7546 (estate verified stores first; yfinance labelled UNVERIFIED).
- The trace's hop 9 Close line.

-- recorded by 4.0.0_SA_CRO~DELL2
