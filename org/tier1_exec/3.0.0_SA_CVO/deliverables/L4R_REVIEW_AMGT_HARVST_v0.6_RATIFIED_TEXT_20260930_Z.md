# L4-R ratified-text review -- AMGT_HARVST v0.6 @803ea38a9e (CONTRACTS only)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~10:1xZ - **Asked by:** CTO~Z msg 27080
**Span:** from this seat's own signed bytes (v0.5 @`8c0b34526b`, half `8aa3b349c926`) to `803ea38a9e` (half `7d6e277537bd`). The ENDPOINT
hash is `974dada544a2` at both, so there is **no ENDPOINT change**. The diff is one hunk, in `C-HV-RANK-DECLARED-SET`.

## THE CHANGE

1. **Exit** is "refused for the whole universe OR ran no job at all", read from the run records. Config alone decides membership.
2. **An EMPTY declared set HOLDs** with `NO_DECLARED_PUBLISHER`, and is never scored. This answers this seat's v0.5 note.
3. **A per-name trial run now keeps an enabled publisher IN the set** (it is a run, so "ran no job" is false). Names that publisher
   did not cover are ineligible. This **reverses** v0.5's "neither adds a publisher nor keeps one out".

## CHECKS

- **Coherent and decidable.** Membership comes from `ENABLED_PUBLISHERS` (`barrons, bbg, ft, sa, wsj`, read at the v0.5 review), and
  both exit tests read the run records. No case is left undefined, and the empty-set branch is closed.
- **Consequence of change 3, stated here so no reader is surprised by it.** sa's runs cover ASML_NA and ASML_US only (26 PARTIAL days
  each; HARVST ADJUDICATION_v36).
  - sa stays in the set, so every other name, **189 of 191**, is ineligible on sa alone, whatever bbg and wsj later reach.
  - One enabled publisher's single-name trial therefore holds the whole rank until that publisher runs universe-wide.
  - The text says so ("Names that publisher did not cover are ineligible"), so this is a deliberate rule, not an ambiguity.
- **Agreement with FWD-7:** unchanged. A rank that HOLDs rather than ranks over unsearched names is the honest reading.

## VERDICT: SIGN

**Two notes for the round-28 analysis, neither a condition:**
1. The census should print, per excluded name, WHICH declared publisher it lacks. A rank held by one trial publisher then reads as
   exactly that, not as generic "coverage incomplete".
2. If the intent is that a trial does not bind the universe, the exit test would be "ran no universe job". That is the CTO's
   design call. As written, the rule is strict and explicit.
