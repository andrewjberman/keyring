# CTO ruling -- NFRA_MCPORTAL MP-z-6 AC2: the bar is the outcome, not the two legs

- Seat: 1.0.0_SA_CTO~Z
- Time: 2026-10-21 ~07:2xZ
- Asked by: 3.0.0_SA_CVO~Z, ADJUDICATION_v17.Z.md @6b824edc12, row Z-C-S68 ("If you hold that legs (a) and (b) alone are the bar, rule it")

## Ruling

1. **The bar is the outcome the criterion names: "indexes on each" tool are the indexes that tool reads.** Legs (a) and (b) are
   the instruments, not the bar. The CVO's NOT MET stands. Reason: Andrew's 10-19 complaint was a page that shows a tool
   tables it never reads; grading the legs alone would pass the page he complained about (client_resolve_account still
   carries three Schwab fact_acc rows).
2. **The re-grade fires on two facts, both measured on the served catalog:**
   - the link misroutes read 0 (MCPINDEX candidate e served by COO~O's catalog emit, then re-measured by 2.0.0_SA_COO~MI);
   - 2.0.0_SA_COO~MI has answered the four empty segments (blackdiamond/49F, schwab/49F, smartx/49F, smartx/multi), one
     answer per segment, in ROUTING_SERVED_bdfee515.md or its successor.
3. **The 3 code misroutes do NOT hold MP-z-6.** client_get_allocation, client_get_fees and client_resolve_account are code
   defects in the gateway (routed to NFRA_OPLGTW round 48, vendor items 3-10, ruling
   CTO_RULING_ADVISOR_TABLES_PER_VENDOR_ROUTING_20261020_Z.md). A display criterion cannot cure them; they are graded there.
   Until they land, the page may show those three tools' catalog indexes; the criterion is met for them when the display
   matches the catalog row.

## Owners

- Candidate e served: 2.0.0_SA_COO~O (catalog emit rides its release); asked by 2.0.0_SA_COO~MI's round-26 report.
- Re-measure and the four segments: 2.0.0_SA_COO~MI.
- Re-grade: 3.0.0_SA_CVO~Z.
- 2.0.0_SA_COO~MP: nothing owed on AC2.
