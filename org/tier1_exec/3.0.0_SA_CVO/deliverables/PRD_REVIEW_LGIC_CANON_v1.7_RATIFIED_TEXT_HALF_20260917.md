# PRD review -- LGIC_CANON v1.7, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97706.
PRD: `org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md` @ `1bd1963781`, ratified-text half_hash `1cc005561a1b`.
Prior review: v1.6 REFUSED, review record @ `462451b6f7`, stamped by this seat.
Before that: v1.4 SIGNED at half_hash `1cd7a3546d93`, STALE since.

## VERDICT: SIGN

## Method

The v1.6 refusal named two things: the ENDPOINT section's FWD-5 carried DONE WHEN/ACCEPT substance the ratified
pin did not have, and an inline `(R-34)` annotation sat inside the section. Both are checked here against the
bytes, and the ratified pin is re-read at its NEW vintage rather than the one the refusal was written against --
a refusal's own cited pin ages the moment the fix lands, and re-reading the old one would have certified the
wrong object.

**The L2 act happened.** `c6914daf82` re-cuts `ENDPOINT_FWD_D14_PIPELINE_CANON_20260912.md`: FWD-5 now reads
`STATUS AMENDED at v3`, carries the practice-wave mechanism and the CARDED carve-out as RATIFIED TEXT, names both
authorities inside the STATUS line (Andrew-direct 2026-09-16 ~18:2xZ call 2, recorded at
`ANDREW_DIRECT_20260916_182xZ_RESERVED_GROUP_FOUR_CALLS_RULED.md`; and ruling R-34), and quotes the v1/v2 text it
replaces so the move is readable without a diff. Outcome and id unchanged, no other FWD touched -- the same
mechanism used for FWD-3/FWD-6's v1->v2 move. That is the act this half was refused for the absence of, and it is
CTO-only, so it could only ever have come from this direction.

## The verbatim check, run mechanically

Sliced both documents into FWD cards on the `^\s{0,3}FWD-\d+\s\s` boundary and compared card by card, stripping
only the STATUS line and its continuations from the pin side (the accepted trim class):

```
  pin cards: FWD-1..FWD-6      prd cards: FWD-1..FWD-6      (denominator 6 on both sides)
  FWD-1 MATCH   FWD-2 MATCH   FWD-3 MATCH
  FWD-4 MATCH   FWD-5 MATCH   FWD-6 MATCH
```

FWD-5 re-checked WITHOUT the indentation normalisation the first pass used, since a whitespace-insensitive
compare is a weaker claim than "verbatim": 22 lines on each side, `RAW-IDENTICAL-INCLUDING-INDENT: True`.

The inline `(R-34)` is gone from the section (v1.6:124 read `...can reach (R-34)`; v1.7 reads `...can reach`),
and it was correctly NOT carried into the pin either -- the authority lives in the STATUS line, which the PRD
drops, so no citation survives inside the section on either side.

## CONTRACTS

Unchanged from v1.6 -- the whole v1.6->v1.7 diff is three hunks: the version bump, one added bullet in the header
prose ABOVE the ENDPOINT heading recording the v3 pin, and the `(R-34)` removal. The header bullet sits outside
the section and is provenance, not in-section annotation. CONTRACTS was spot-checked at v1.6 against
`LGIC_ENFORCE`'s and `LGIC_NAMING`'s own CONTRACTS tables (the registry row, direction reversed as LGIC_ENFORCE's
table states explicitly, and the `NAMING_SCHEMA.json` row) and they agree; nothing in this version moves it.

## What this closes

LGIC_CANON's ratified-text half has been STALE since v1.4's signature (half_hash `1cd7a3546d93`). It is now
current at `1cc005561a1b`, and with the brief half already SIGNED by `2.0.0_SA_COO~O`, the PRD carries both.

-- 3.0.0_SA_CVO
