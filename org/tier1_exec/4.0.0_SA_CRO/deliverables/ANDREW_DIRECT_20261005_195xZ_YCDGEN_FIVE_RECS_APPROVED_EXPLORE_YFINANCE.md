# Andrew-direct, 2026-10-05 ~19:5xZ (3:5x PM Eastern), at the 4.0.0_SA_CRO terminal -- VERBATIM

Channel: typed by Andrew into the 4.0.0_SA_CRO (base) session, in answer to this seat's `/open-calls` (five cards).

> all recs approved, but were out of quota for today on bloomberg + we cant get BQL, so id like to explore if this can
> be done via yfinance for now

## The five cards he answered, with each REC as it was shown to him

Source: section 8 of `docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md` @69141b561e.

1. **Standing authorization for data pulls scoped to live client holdings.** REC: yes, one standing word, limited to
   the union of securities in live client portfolios; it covers a longer Yahoo price backfill, Bloomberg reference and
   fund-allocation fields for client-held tickers, and public SEC filings.
2. **Start the daily Bloomberg fund-allocation capture now, before the build.** REC: yes, for client-held funds.
3. **Opal's own method, or a YCharts look-alike.** REC: Opal's own -- GICS sectors, Opal-defined market-cap buckets,
   no style box in the first version, each method stated on the page.
4. **Order of variants.** REC: Overview first, then Comparison and Multi together.
5. **Buy the Bloomberg query-language entitlement for this project.** REC: no.

## What his second clause changes (as stated, not widened)

- Bloomberg is out of quota today, so card 2's capture cannot start today. It stays approved; it is not started.
- The query-language entitlement is not obtainable ("we cant get BQL"), which agrees with card 5.
- He asks this seat to explore whether the process "can be done via yfinance for now". This seat reads that as his
  word for a yfinance probe on the reference portfolio's holdings (Yahoo is already the vendor of Opal's scheduled
  price pull, and card 1 covers Yahoo pulls scoped to client holdings). The probe is read-only and writes nothing to
  a production path.

## Routing

One line to `1.0.0_SA_CTO` naming this record (the approvals bear on the IRPT_YCDGEN endpoint revision). No other
broadcast.
