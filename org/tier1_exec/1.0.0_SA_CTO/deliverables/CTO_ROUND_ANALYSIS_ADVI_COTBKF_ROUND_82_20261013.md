# CTO ROUND-82 ANALYSIS -- ADVI_COTBKF -- answering the round-81 slug, under the dell2 pivot direction (2026-10-13 ~19:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 7195,
`org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v50.md` @43b340c673: L9 3 PASS, D2-S134's disarm VOID, W155-S1 and
W158-S2 ARMED to this seat. **Governs:** crossbox `XB-20261013T180328Z-d4a5`, `DIRECTION_DELL2_20261013.md` section 2 O4 and section 4:
"ONE active-set + reverse-match cell, then PARK"; ranked "deep, deep, deep" historical by Andrew; it never draws from O1 or O2.
**Binding:** the backfill floor (2012; a client's earliest record; 365 days for non-client needs); the Opal Shape word (~18:2xZ).
**No PRD addendum.**

## 1. What round 81 did

- **The consumer read:** two CODE readers of the minted table. One is the ARD adapter (`commonwealth_account_return_daily.py:221-226`); the
  other is the price-basis census (`:292-295`). Neither is a page. The ARD output reaches a portal page only through a read route that is
  planned, not applied.
- **The stage read:** for APH, CTVA and HON, the build and the minted copy equal the vendor Close, and the store is nearer the price paid.
- **New (W158-S2):** the price store carries two asset names under one ticker (SCCO, a bond row at the equity's price, on 1,027 dates;
  APH CL A and NEW CL A, on 70 dates). A ticker-only read takes two rows.
- **The date-bound re-read:** 1 of 4 bounds moves (the price store).

## 2. Rulings

1. **W155-S1 disarms on a READ, not a correction, if the read shows no person can see these prices.** The CVO's remedy offers exactly that:
   "a read that the second hop reaches no page". So the cell reads whether the route ARD -> gold `account_return_daily` -> reporting-publish
   -> dashboard is LIVE, from code and from the deployed config.
   - **Not live:** W155-S1 disarms. The prices are recorded as a known defect of a parked project, fixed when (if) the route is applied.
   - **Live:** this seat cuts the correction under a never-widen pair. The project does not park until it is done.
2. **W158-S2 disarms on a read that names 0 ticker-only readers** (the builder `build_canonical_prices_v2.py` and the two minted-table
   readers first), or, if any exists, on a keyed fix to the (ticker, asset_name) pair. The keyed fix is in pattern: one store, one Opal key.
3. **The adapter header's "no S3 write"** is corrected in the same cell (W158-S5). The file carries a guarded `--apply` mint.
4. **O4's one cell (the direction):**
   - the active Cottonwood set: every currently active account, with its per-security held windows, under the 2012 floor and each
     account's earliest record;
   - the reverse match: every current Black Diamond Cottonwood account with its Commonwealth predecessor or "none".
   - It is read-only. Its path goes to dell1's MDPF_DEMQUE through `0.0.0_AB_MSTR~DELL2`, so former clients are EXCLUDED from every draw.

## 3. ENRICHMENT LIST for round 82 (ONE issuance, all read-only)

1. **The active set and the reverse match** (O4). One file plus its path. Counts printed, no account value.
2. **The route read for W155-S1** (ruling 1): the served minted objects are read, not the scratch copy.
3. **The ticker-key read for W158-S2** (ruling 2), plus the header correction (ruling 3).

**Then PARK.** If items 2 and 3 disarm both rows, this seat parks ADVI_COTBKF at the round-83 analysis, and `2.0.0_SA_COO~C2` stands down
once worker branches drain (direction section 8, MSTR act 3). A LIVE route keeps it open for the one correction pair only.

## 4. Acts only Andrew can do

None.

-- 1.0.0_SA_CTO~DELL2
