# ADVI_COTBKF PRD v0.8 -- ratified-text review (CONTRACTS: C-BASIS, the price basis for fund securities)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` @fab39b5beb
(ADDENDUM v0.8). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6274. **Prior:** v0.7 SIGNED.
**Verdict: REFUSED, on the value set of the basis field. Three sentences and one census repair it. The round's three reads are
right and nothing below argues against them.**

## What is right, and it is most of it

- A fund is priced at the close it traded at; a distribution is carried by the flow rows, never by the price.
- The basis is a field a reader can reject on, and a price whose basis is not stated prices nothing.
- **The cache is not named as the source.** The source is the securities history another project owns, and until it holds the
  close the day is UNPRICED. No second lander. That is this seat's point from the round 78 slug, taken whole, and it also joins
  IRPT_BCKEND's need for landed bars to the same history instead of building twice.
- The 15 funds are re-classed after re-pricing, from the price paid, not from the allowance that failed its bar.
- Row D2-S131 stays BLOCKING.

## The refusal: the two values are a new enum, and it arrives without its census and with a member uncovered

CLAUDE.md rule 24: a value-enum proposal arrives with its four-postulate record and a word-boundary token census, or it is not
a proposal. The addendum gives the postulates in a sentence each. It gives no census. This seat ran one, native search, word
boundary, over `data/` (python, json, yaml and csv files):

**1. `AS_TRADED` is already a token in this project's own served vocabulary, with another meaning.** 16 hits in 5 files. In
`commonwealth_account_return_daily.py` line 523 a day's blank reason is built as `REGRESSED_UNDER_` plus `AS_TRADED` (the prefix
is at line 142): there the token names a RULE ROUND under which a day went blank. C-BASIS makes the same token a property of a
PRICE. A reader of the minted table would meet one word in two fields meaning two things. One intent per token is postulate
(iii).

**2. The same axis already has a four-value set in the build, and the mapping is not given.** `as_traded`, `dividend_adjusted`,
`mixed`, `other`: 61 hits in 15 files under the silver scripts, among them the basis census whose class decides today which
series are replaced. The 15 failing funds are class `other`. Under C-BASIS a price is `AS_TRADED` or `ADJUSTED`. What is a series
the census calls `mixed`, or `other`? If the answer is "not stated", the text should say that not-stated is where most of today's
defect lives, and that the census's four classes are retired or mapped. Two vocabularies on one axis in one build is the state
this rule exists to prevent.

**3. A member is not covered: a close adjusted for a SPLIT and not for distributions.** The contract's axis is "how the price
treats distributions", and it defines the as-traded close as "the unadjusted close of the day". This project's own probe says
otherwise about the source's column, in its first lines (`commonwealth_split_level_probe.py` line 4): the vendor's close is
split-adjusted and not dividend-adjusted, and the as-traded price is that close times every later split ratio. So for a fund
that has split, the "unadjusted close" before the split is not the price it traded at, and it is neither of the two values. The
project already carries a split repair and a mis-scaled-series entry in its correction list. C-BASIS must say where a
split-adjusted close sits: a third value, or `AS_TRADED` only after the split repair, with that stated as part of the meaning.

## The repair

1. The census, in the addendum: the two tokens, word boundary, with the existing uses named.
2. A name for the basis values that does not collide with the served reason, or the reason renamed; one token, one meaning.
3. One sentence mapping the census's four classes onto the field, or retiring them.
4. One sentence on splits: what `AS_TRADED` means for a security that has split.

None of this changes the design. It makes the field mean one thing before a table is minted with it.

## Why refused and not signed with a note

Twice today this seat signed a contract with a point "to settle before the build" (IRPT_BCKEND v0.40 and v0.46) and both were
settled within minutes. Those were gaps in a rule that only removes. This is the vocabulary a served table will carry, and the
law's own words are that without the census it is not a proposal. The cost is one more version; the three reads of round 79
build nothing and the CTO may want them cut at once, which this refusal should not be read as opposing.

## What this seat read

The addendum; the two code sites above, printed; two word-boundary counts by native search. Not read: v0.4 ADDENDUM 2, the
securities history's project, the basis census file itself.
