# ANDREW-DIRECT 2026-09-21 ~17:2xZ -- AMGT_RESAPP: promote if there are features; the pipes are dry by design; the backfill waits on the bronze/silver shape

- **Channel:** Andrew, direct, at the `1.0.0_SA_CTO~Z` terminal, two messages minutes apart. **Recorded by:**
  `1.0.0_SA_CTO~Z`, same turn. **Scope:** surfaced verbatim, adjudicated neither wider nor narrower.

## His words, verbatim and entire, in order

> Yes to both of your earlier calls, also might as well just push DEV to PROD if there are new features as its gated
> to only me on PROD anyway. The only issue on that side is I actually don't believe that there is any water in these
> pipes. Unless a lot of work has been done that I don't understand, the impression I get is we have very little
> data. I don't know how much frontend work has realisitcally been done. I don't believe the lead panel would have a
> top list on either trending or breakout views. I dont believe we ever established a lot of the working operations of
> the front end. So in my opinion prod promote doesnt really matter, unless you are aware of material progress on that
> side and have a clear test case on how to visually smoke that (e.g. "search nvidia, see what comes up"

> It is ok if there isnt a lot of data in the pipes, I've been holding back on a coordinated backfill until we knew the
> pipes worked/had the final shape of the pipes and backend database, as I dont think we've really hammered out the
> format of the bronze/silver opal-data-harvest for the various vendor/publication ingestion channels.

## What he answered (the two cards put ~16:5xZ)

1. **Promote AMGT portal DEV to PROD: YES**, conditioned in his own words on "if there are new features". Measured
   this turn: `origin/PROD..origin/DEV` = 6 commits, all AMGT: 4 page changes (thesis driver chart labels and links,
   `db1c5f64` empty-reason on an EMPTY list, `796f5c9c` honest CEO reading, `d74ff760` ModelTab score blocks) and 2
   merges. The condition is met, modestly. PROD stays gated to him.
2. **Open the page to the managers: YES, but no names were given**, and he says PROD is "gated to only me" today.
   Parked until he names the managers. The gate is not widened on this record.

## His reading of the pipes, measured by this seat the same turn (read-only)

He is right, and the second message says it is deliberate.
- **Lead panel:** TRENDING_CHATTER serves 2 names today (3 on 09-19); BREAKOUT_CHATTER is EMPTY (189 of 191 no
  signal); TRENDING_PRICE and BREAKOUT_PRICE have NO generation on any day 09-17..09-21.
- **Coverage:** the crosswalk holds 96 records, 36 with a Bloomberg key, 60 unresolved. **NVDA is not covered.**
  The Security Analysis page has **no search control** on DEV. The only search UI in the portal is Portfolio
  Management's mock lookup. So "search nvidia" is not an action the page supports today, and would find nothing.
- **Filings:** 14 resolved source documents of 194; 180 are UNRESOLVED placeholders.
- **Other prefixes:** model blocks 37 names; posture and scores 33; management 16; drafting 12 objects; peers 191
  names / 797 objects; publications 7 objects, newest 2026-09-15; publication-links 3 names; social empty. The
  chatter-axis schedule is ENABLED; no ingestion collection is scheduled, per his 09-15 hold on the collection
  mechanism.

## Reading, narrow

- The empty pipes are **intended**: he holds a coordinated backfill until (a) the pipes are proven to work and
  (b) the final shape of the pipes and backend database is set.
- **The open item he names is the FORMAT of bronze/silver in `opal-data-harvest` for each vendor and publication
  ingestion channel.** This record does not decide that format.
- It ties to two items already on the record: the 2026-09-18 CRO~Z task ("the shapes of the data RESAPP pulls from
  every source ... and a plan to manage it properly" -- only the measurement half, `LGIC_NAMING_STANDARD_READ_20260918.md`,
  landed; it states it "contains no plan and no recommendation"), and the laptop CRO lane's R4 doctrine act.

Broadcast same turn to `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`, `0.0.0_AB_MSTR~Z`.

-- `1.0.0_SA_CTO~Z`
