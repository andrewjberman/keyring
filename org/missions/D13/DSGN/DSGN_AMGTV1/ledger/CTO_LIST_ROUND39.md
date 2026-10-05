# DSGN_AMGTV1 -- round 39 list (1.0.0_SA_CTO~Z, 2026-10-05 ~13:2xZ)

**Input:** `2.0.0_SA_COO~D` round-38 close @96ebc7a629 (`ROUND38_CLOSE.md` section 4); my round-38 review @2e225582da. **Andrew
approved the DEV push** of rounds 37 and 38 once the CardFooter fix lands: msg 29559, record 121b7b016e, verbatim "3.) Yes,
recommendation approved."

## ROUND 39 (ONE issuance by `2.0.0_SA_COO~D`): the push is waiting on item 1, so cut it first

1. **CardFooter's unknown source.** `sourceWords()`'s last fallback returns `UNNAMED_SOURCE_WORDS`, never a de-punctuated raw code
   (FWD-11). The repairs38 arm plants an unknown long source (`issuer-site/harvest/silver/filing_source`) and expects the unnamed
   phrase.
2. **Row S3, PageEnd's invented clock.** The end line prints no clock after a bare served day. Either option is accepted:
   - one optional prop on the shared `PageEnd`, with every other page's default unchanged (the same pattern as round 38's PanelFooter
     props); or
   - a pre-formatted date passed from `SecurityAnalysis.tsx`.
   Pick the one that touches fewer shared files.
3. **Issuer instrument:** reads37's What-changed scope selector follows the probe component. This is the issuer's own; no portal file
   is touched.

## The push sequence (no further word from Andrew is needed)

1. Round 39 drains.
2. The candidate is merged onto the CURRENT `origin/DEV` (now `f1cdccd7`, moving under the DSGN_REBRND FAST lease).
3. This seat confirms the item 1 and item 2 diffs and a clean trial merge.
4. This seat sends `0.0.0_AB_MSTR~Z` the final hash.
5. MSTR~Z merges, pushes DEV only, and reports CI.

## REVIEW (2026-10-05 ~14:5xZ) -- items 2 and 3, candidate portal `71097b53` (COO~D msg 29609)

- **Placement:** `71097b53` CONTAINS `origin/DEV` `481b3bcc`, so it is a fast-forward. 2 files, +9/-3.
- **The shared `PageEnd.tsx`** gains an optional `asOfText`. When it is absent, the old `formatPanelTimestamp` path runs, so every other
  page is unchanged.
- **`SecurityAnalysis.tsx`** passes `longDate` for a bare served day (no clock) and `longStamp` for a served moment. That is row S3's
  fix, and it is the one-shared-file option the list preferred.
- **Item 3** (the reads37 selector) is the issuer's own instrument; no portal file is touched.
- **Owed after the push:** the live dated walk of the end line. The walker is held by the laptop's Y-6.

**APPROVED for DEV.** The push needs Andrew's own word: record 121b7b016e covered rounds 37 and 38 only (CLAUDE.md Portal, per-push
word for product files).
