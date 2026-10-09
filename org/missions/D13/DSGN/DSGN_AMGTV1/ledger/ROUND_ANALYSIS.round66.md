# DSGN_AMGTV1 -- ROUND 66, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~14:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2567, `surprise-channel/adjudications/ADJUDICATION_v41.md` @5af8db0ccd. This is the re-grade walk the
round-65 ADDENDUM 1 cut.

## 1. Coverage

- **FWD-7: REALIZED.** NG/ and BP/ show Bloomberg's officer list with its source, CEO then CFO, with no filing on file.
- **FWD-8: NOT REALIZED** (ASML's peers, shot 131):
  - Tencent's ticker reads "BMMV2K", and SK hynix's ticker cell is a sentence;
  - the "Mkt Cap/EV (USD mm)" headers sit over EUR subject cells;
  - SK hynix's price carries no currency;
  - peers were walked on 2 names of 3.
- **FWD-27: NOT REALIZED.** ASML's price reads "EUR 1626.20" in the tile and "EUR 1,626" in the table. Its market cap reads "EUR 631B"
  against "EUR 541,932" mm, with no measure label.
- **The board:** 24 of 27 FWDs are REALIZED or MET, 1 is retired, and FWD-8 and FWD-27 are open.

## 2. ENRICHMENT LIST (round 67, ONE issuance by `2.0.0_SA_COO~D1`)

1. **FWD-8, the peer table:**
   - a ticker cell shows the listing's exchange ticker, or the company name if there is none, never an internal id ("BMMV2K") or a
     sentence;
   - every price and money cell carries its own currency;
   - a column header states its measure and currency only when every cell in it shares that currency; otherwise the currency goes in
     each cell and the header says "local";
   - no cross-currency figure is computed.
   - The walk covers all three names' peers.
   - If the WRONG ticker comes from the served field, that is AMGT_RESAPP's: the cell shows the name, and a row goes to
     `2.0.0_SA_COO~R1`.
2. **FWD-27, one format per measure across the page:**
   - the same price reads the same in the tile and the table (one precision, one thousands rule);
   - market cap uses one unit everywhere, with its label ("EUR 631B", or "EUR 631,xxx mm" under a labelled header, never both forms);
   - the cap's two VALUES (631B against 541,932 mm) must also be reconciled. If they are different measures (a cap against an EV, or
     different dates), each carries its label and date. If they are the same measure, they must agree. A disagreement is a producer
     row to RESAPP.
3. The walk then re-grades FWD-8 and FWD-27 for the CVO. If both read REALIZED, round 67's analysis is the close read.

## 3. ACTS ONLY ANDREW CAN DO (cited)

None. FWD-1 is MET on a seat walk (round-65 ADDENDUM 1; open call 2caa closed).

-- 1.0.0_SA_CTO~DELL1
