# L4-R review -- MDPF_SECCLASS PRD v0.3, ratified-text half (3.0.0_SA_CVO, 2026-10-05 ~04:0xZ)

PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` @35e313ec06 (equal at HEAD); half_hash 066397f2493a7f5a...
Delivered by 1.0.0_SA_CTO msgs 105127, 105133. Previous signature bound ENDPOINT hash 6e0126e78546.

## What changed (git diff 301332beb4..35e313ec06)

- Header: v0.3; endpoint_outcomes gains FWD-9 and FWD-10. FWD-1..FWD-8 byte-unchanged.
- FWD-9: every stock collected for Rival Funds has its entry in the shared list (class, sub-class, fund or individual
  stock), history filled back three years (or to its first trading day), none missing, none further back than three years.
- FWD-10: a stock newly entering through the trading of the Opal ETFs or the rival ETFs gets its entry and three-year
  history by a dedicated routine, without a person starting it; an outside source or model needs Andrew's word.
- Outside ENDPOINT: ADDENDUM v0.3 (C-BACKFILL, the list as an input from ETFS_RIVALS, vendor and moratorium notes).

## The pins, read

- `cooRV_ANDREW_DIRECT_20261005_03xxZ_RIVALFUNDS_BENCHMARKS_CLICKABLE_TICKERS_ETFCLASSIFIER_BACKFILL.md` @41158af7f9, verbatim:
  "Every single stock that is collected for the purpose of Rival Funds should be ingested with full backfill on the
  ETFClassifier canonical opal table. As new stocks enter from trading activity of the Opal ETFs and the Rival ETFs, those
  stocks should be backfilled and included in the ETFClassifier table through some kind of routine, dedicated mechanism."
- The cap, record `..._RIVALFUNDS_LOOKBACK_CAP_3Y.md` @357e681ddf (site-Z local), relayed verbatim by 0.0.0_AB_MSTR msg
  105116: "we can just put a cap on all lookback of 3 years for rivalfunds inclusions".

## Verdict: SIGNED

- FWD-9 carries item 3 with the cap; "full backfill" bounded at three years is the cap's own words.
- FWD-10 carries item 4. The cap reaches it as written, not by analogy: the Rival Funds page (ETFS_RIVALS PRD, addendum A
  FWD-1) shows the two Opal ETFs (IDVZ, PFOE) on one plane with their rival peer groups, so a stock entering through either
  side's trading is a Rival Funds inclusion.
- "Without a person starting it" is the plain reading of "routine, dedicated mechanism"; the vendor clause restates the
  standing rule. The SOURCE lines quote his words; no seat name or history inside ENDPOINT; CONTRACTS unchanged.

-- 3.0.0_SA_CVO
