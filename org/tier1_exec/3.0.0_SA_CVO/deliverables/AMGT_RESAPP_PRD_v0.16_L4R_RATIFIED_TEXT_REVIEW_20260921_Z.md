# L4-R review -- AMGT_RESAPP PRD v0.16, ratified-text half (`3.0.0_SA_CVO~Z`)

**PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`2d0da569e7`. **Half:** ratified-text, hash
`e231f4ecc4ce` (from `c224a5e60e21` at v0.15, which this seat signed @`a986a03423`), measured from the committed bytes.
**Delivery:** `1.0.0_SA_CTO~Z` msg 24032. **Verdict: SIGN.**

## What changed in this half

One hunk, inside CONTRACTS (section starts :537), in `C-EXEC-MANAGEMENT` (:764-767):

1. **Who the CEO is.** "the officer carrying a chief-executive title; for a Japanese-listed issuer with no such
   officer, a 'President' or 'Representative Director and President' is the chief executive. The rule is not extended
   to another jurisdiction without evidence for that jurisdiction." Lands the ruling behind rows `S195`/`S196`
   (Keyence's one officer, Tetsuya Nakano, role President). Precedence is unambiguous: a chief-executive title wins; the
   President rule applies only when none exists. Scoped to one jurisdiction, with an explicit evidence bar for others.
2. **Readable reasons.** "A served reason is always a readable sentence; a missing value is never printed into it as a
   literal." Testable, and consistent with the plain-English reason the as-landed rk-48 pair's remedy (R19-A) already
   bound. Prompted by row `S197` (Keyence's served roster reason prints "the persisted None filing doc-...").

Both rules sit beside, and do not loosen, the existing clause that each Bright Data search runs only under Andrew's
per-use word: Keyence's CEO becomes IDENTIFIED under rule 1, and still NOT SEARCHED until that word is given.

## The review's standing checks

- **ENDPOINT (:293-536):** no diff hunk falls inside it; byte-unchanged since v0.15.
- **No annotation, history or seat name inside the half:** the v0.16 change note sits at :204, in the preamble (brief).
  The new contract text carries no serial and no date.
- **The format contracts signed at v0.15** are untouched; section 11's re-pin of the plan (@`1a9f1c4469`, dropping a
  dual-write move order the same-window clause forbids) is in the brief half and moves in the contracts' direction.

-- `3.0.0_SA_CVO~Z`
