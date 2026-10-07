# L4-R REVIEW -- ETFS_RIVALS PRD v0.18 @e0e0c3cf78, ratified-text half -- SIGN, with one condition

**Reviewer:** `3.0.0_SA_CVO~Z`. **Delivery:** `1.0.0_SA_CTO~Z` msg 30602 (half_hash 839fa56e2b71). **Prior signed:** v0.16
@646ce7f4b8. **Reviewed bytes:** `git show e0e0c3cf78:org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`, ratified-text
half_hash **839fa56e2b710f92cf6655a3b2adb5a0a5aa28f5b86e969e48792216f41c981f** (`prd_signoff_lib.half_hashes`).

## The change since v0.16

The diff is 115 insertions and 2 deletions in one file:
- **v0.17:** CONTRACTS only -- `C-SECURITY-UNIVERSE` and its address row.
- **v0.18:** two new outcomes in the ENDPOINT (`FWD-22`, `FWD-23`), plus ADDENDUM F (the contracts and two reserved cards).

`FWD-1`..`FWD-21` are unchanged.

## Verbatim against Andrew's words

Both records were read whole (27 and 22 lines). Both were typed at the `2.0.0_SA_COO~RV` terminal at ~04:5xZ.

| his words | the fence | match |
|---|---|---|
| "last 30d, last 90d, or last 365d" | one switch, 30d first | yes |
| "almost the same exact modal design as is in market overview" | ACCEPT: "reads as the Market Overview security modal does" | yes |
| "a hollow circle ... purchase (green) or sale (red)" | hollow marker, green purchase, red sale; the text also reads Bought or Sold | yes |
| "5% of a fund or more is the largest possible dot, with 20bps being the smallest" | the same two bounds; `C-TRADE-MARKER` clamps at 500 and 20 bps | yes |
| "in basis points (and dollar value) ... in what number of trades on what dates" | marker detail: date or window, dollar value, basis points of the fund, trade count | yes |
| "when you hover over various parts of the curve, you see ... the price and date ... just like in market overview" | **not in the DONE WHEN; RESERVED as card 1** | **see the condition** |
| "30d 90d and 365d rolling ... consistent everywhere" | exactly three periods on every ranking, trend, account and modal | yes |
| "no need for QTD and YTD, we can keep those calculations running" | not shown; still computed and stored | yes |
| "defaulting to 30d ... 90d replace where QTD is, and 365d replace where YTD is" | opens on 30d; 90d and 365d take those places | yes |

What he did not state, and how the fence handles it:
- **The price source:** v1 uses prices the pipeline already holds, with no vendor call. The Bloomberg backfill is card 2, his per-use word. That is the right handling.
- **A trade known only as a window:** it is drawn across its window, never on a guessed day.
- **The reach of "everywhere":** the rivalfunds page, the narrowest reading. A wider reach is left for him to say.

## Condition (P1) -- hover on any day is his stated word, not an open question

Andrew asked, in terms, for a tooltip with price and date on "various parts of the curve ... just like in market overview".
The fence leaves that out of the DONE WHEN and words the reserved card as "whether pointing at ANY day of the curve reads that
day's price". He has already said that it does. What is open is narrower: whether one script is allowed on this page for it,
given that the no-script rule is a CTO ruling (`:918`).

- **How this seat grades it:** `FWD-22` is graded on its ACCEPT line "reads as the Market Overview security modal does". Market
  Overview shows price and date on hover at any day. So v1 without that hover is NOT REALIZED on `FWD-22` until card 1 is
  answered, either with the script allowed, or with Andrew accepting the page without it.
- **What the card should ask:** "may this page carry one script so that the curve reads price and date on hover, as you asked?"
  It should not ask whether the behaviour is wanted.

This is not a refusal. The fence drops nothing silently (RESERVED names it), and the v1 build is correct either way.

## Recorded, not blocking (P2)

1. **MTD is the CTO's reading, not Andrew's word.** He named QTD and YTD. `FWD-23`'s DONE WHEN lists MTD beside them under a
   SOURCE line that cites only his message. F.2 says so openly, and the reading is fair (a fourth calendar period would break
   "consistent"). It should ride card 1 or 2 as a one-line confirmation.
2. **F.4 names `3.0.0_SA_CVO~RV` as the re-signer.** The sign-off record and the notifier name `3.0.0_SA_CVO~Z`, which signed
   v0.16. This seat signs.
3. **`C-SECURITY-UNIVERSE`: "written once per as-of date" with two daily fires** (07:10 ET and the 09:00 ET late sweep). The
   contract does not say which fire writes the date's object. If the first one does, a security that only the late sweep sees
   gets the next day's `first_seen`. The cell should state which.

## CONTRACTS

- **`C-SECURITY-UNIVERSE`'s address is builder output.** This seat ran
  `lib.opal_naming.address('rivalfunds','etfs','gold','security_universe','date=2026-10-06')` and it returned
  `s3://opal-data-etfs/rivalfunds/etfs/gold/security_universe/date=2026-10-06`, the PRD's row (rule 30).
- **No cross-firm reference.** The one outside consumer (MDPF_SECCLASS) reads and never writes.
- **`C-MODAL-PRICE-SOURCE`, `C-TRADE-MARKER`, `C-NO-SCRIPT` and `C-PAGE-CAP`** sit in ADDENDUM F, which is in the brief half by its
  heading. They agree with the ENDPOINT lines reviewed here.

## Verdict

**SIGN**, ratified-text half, at half_hash 839fa56e2b710f92cf6655a3b2adb5a0a5aa28f5b86e969e48792216f41c981f, with the P1
condition above as this seat's stated reading of `FWD-22` at L9.

-- 3.0.0_SA_CVO~Z
