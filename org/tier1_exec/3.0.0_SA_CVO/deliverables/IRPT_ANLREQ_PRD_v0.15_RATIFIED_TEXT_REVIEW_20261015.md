# IRPT_ANLREQ PRD v0.15 -- L4-R review, ratified-text half (C-FILING-HINT restated)

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-15 ~15:5xZ. **Delivery:** msg 8418 (ENDPOINT hash unchanged; CONTRACTS text changed). **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @1671e13361. **Compared against:** v0.14 @81d9691b71, which this seat signed.
**Read:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/r41/FILING_HINT_DESIGN_READ.json` (merged @039f9279c4).

**Verdict: SIGN.** Only the C-FILING-HINT row moved in this half.

- **Source.**
  - The hint is the upload door's own `suggestion` on a `TICKER_NOT_FOUND` finding. The design read names that source
    `KIMI_CHECK_PROVIDER_VERIFIED`: a proposal checked against the price provider at upload, by the door's existing step.
  - That is consistent with C-SWAP step 1 (verified against the registry and yfinance, never YCharts).
  - The form reads no catalogue and makes no vendor call of its own.
- **Dropped rules.** The CUSIP/ISIN rank and the catalogue source are dropped because the file carries ticker and amount only, as the
  design read measured.
- **Andrew's 10-15 word is kept.** "Did you mean" at filing; "swaps are not up to the filer". Specifically:
  - Use or Keep, and nothing is replaced without the filer's click;
  - the form never reads swap `suggestions` and never shows `NAME_PROXY`;
  - a kept unknown symbol files and reaches C-SWAP.
- **The interim state is stated honestly.** Until the door change rides the ENGINE release (owner `2.0.0_SA_COO~G2`, the C-SWAP owner), a
  kept unknown symbol is refused as today, and the form says so in words.
- **Agreement.** The row agrees with C-SWAP, C-PRICES and FWD-2. FWD-1 to FWD-7 are unchanged; the ENDPOINT hash is unchanged.

**One limit, carried and not a condition.** The design read states it did not read the provider's live behaviour (Kimi, yfinance). The
words "provider-verified" therefore rest on the code path (`upload_suggestions.py`, `uploads.py:578-580`), not on a measured run. The
FWD-2 run exercises it.

-- 3.0.0_SA_CVO~DELL2
