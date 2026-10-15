# DSGN_RBNDV2 -- ROUND-5 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~16:2xZ)

**On:** the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v6.md` @045f877668 (MAY-CLOSE). The round was cut from
Andrew's Market Overview fix list, `deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_MARKET_OVERVIEW_FEEDBACK.md`, whose first
words are "It largely looks good". That answers `3c44`, so FWD-1's look is given. **Branch:** `feature/dsgn-rbndv2-light`, unpushed.

## 1. What round 5 moved

- **Six of Andrew's items are MET** (RB5X1..X6-AC3): on the CVO's three walks, plus the issuer's computed reads for the four checks
  it did not walk.
- **W13-S2's disarm is met.**

## 2. Open

1. **A regression of round 2's RB2I1-AC3: each Trending Topics row is boxed again.** Round 4's light-scope rules for
   `border-white/N` (`index.css`:593-596) made the row's `border border-white/10` visible (`ExecutiveSummary.tsx`:989).
   - Fix as a CLASS: list every `border-white/N` that round 4's rule now draws on a light ground. Keep the deliberate ones, such as
     section hairlines, and drop the rest, starting with the Trending Topics rows.
   - Proof: the before and after list printed, and one walk showing the Trending Topics rows unboxed.
2. **Footer casing: "Source: Global news." should read "Source: Global News."** The source is a proper name. This is the same
   class as Andrew's item 3, so the issuer sweeps every footer's source name, not one string.
3. **Andrew's item 2, tooltip placement (`002b`, held):** his to answer at the COO~RB terminal.
4. **FWD-4 (heat maps):** his, at the same terminal.
5. **The FWD-5 walk goes on page by page from his comments.** The pages after Market Overview follow as he sends them.

## 3. ENRICHMENT LIST for round 6 (one issuance; C-BRANCH binds)

1. The `border-white/N` class sweep, with the Trending Topics regression first (2.1).
2. The footer source-name casing sweep (2.2).
3. Andrew's next page's comments when he sends them, and `002b`'s answer when he gives it. Cut nothing on either before his words.
