# ANDREW-DIRECT 2026-09-22 ~13:1xZ -- AMGT: Andrew delivers the starting list; meanwhile a field-level map of every channel, per page component

**Where:** the `1.0.0_SA_CTO~Z` terminal (site Z). **Answering:** this seat's ~13:0xZ frame:
- card 1: a proposed 10-name starting list;
- card 2: a ~50-security, 7-field identifier canvass.

## VERBATIM

> "I will deliver a list which will be our starting backfill list, and that is what we can actually go deep on. It is
> more logical to build our structure off the basis of these selected securities. In the interim however, i would
> recommend getting field level understanding of the pulls across opal-data-harvest bronze, that means the
> barrons/wsj/financial times/bloomberg/seeking alpha various pulls and pages (e.g. Seeking Alpha peers as well as the
> ticker-specific news from the others), the format of the EDGAR filings and associated shape, the shape of the
> bloomberg financial ratios figures and etc, the structure for investor relations/blogs for specific companies and what
> that ingestion looks like since it is more ad hoc by nature, the methodology for translation and how that plays with
> the data contracts, the format of the lusha pulls, the shape of any SERP operations, any social feeds if that is a SERP
> function, and so on. There are a lot of channels that need to all be identified across each component, 1.) Lead
> Panel, 2.) Thesis, 3.) Exec Mgmt, 4.) Peers, 5.) Model. We will cover 6.) Posture on a next version build it is not in
> scope for the initial research."

## WHAT IT RULES (the narrow reading, stated as such)

1. **Andrew supplies the starting backfill list.** This seat's 10-name proposal (card 1) is superseded. The structure
   (keys, contracts, backfill cells) is built off his selected securities.
2. **Card 2, the identifier canvass, is not approved by these words.** It is re-sized against his list when it
   arrives. No Terminal pull runs meanwhile.
3. **Interim work: a FIELD-LEVEL map of every channel's pulls.** "Across opal-data-harvest bronze" plus the pages it
   feeds. It covers at least:
   - Barron's, WSJ, FT, Bloomberg and Seeking Alpha pulls and pages, including SA peers and ticker-specific news;
   - the EDGAR filing format and shape;
   - the shape of the Bloomberg financial ratios and figures;
   - investor-relations and blog ingestion (ad hoc);
   - the translation methodology and how it meets the data contracts;
   - the Lusha pull format;
   - SERP operations;
   - social feeds;
   - "and so on".
   Every channel is mapped to the page components that consume it.
4. **In scope: 1) Lead Panel, 2) Thesis, 3) Exec Mgmt, 4) Peers, 5) Model.** 6) Posture is OUT of scope for the
   initial research and deferred to a next version build.
5. **The backfill hold stands** (records @`2a192b6e07`, @`5c20841dd1`, @`6f1a72e4be`).

## ACTS

- This record, committed; broadcast to the fabric the same turn.
- `1.0.0_SA_CTO~Z` runs the field-level map as READ-ONLY research: code, Terraform, and sample-object GETs from Opal
  S3. No vendor call, no Terminal pull, and no personal contact value quoted, only field shapes. The result is one
  document with a per-channel field dictionary and a channel-by-component matrix for components 1-5.

-- `1.0.0_SA_CTO~Z`
