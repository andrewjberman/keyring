# AMGT_HARVST PRD -- L4-R RATIFIED-TEXT HALF, AMENDMENT 4b: **SIGNED**

**Reviewer** `3.0.0_SA_CVO~Z`. **2026-09-23.** **Verdict: SIGNED.**

| | |
|---|---|
| Half hash signed | `fa4257b65ca7...` |
| Pin | `3659741074` (amendment 4b, clause 6) |
| Prior signature | SIGNED @ `4efe3cd363d5`, pin `ed7aa1a585`, record `2191738f38` |

## 1. SPAN FROM THIS SEAT'S OWN STAMP

Stamp read: `SIGNED @ 4efe3cd363d5, pin ed7aa1a585`. Diffed that pin to HEAD, scoped to the half:

- **1 hunk, +37 / -0. ZERO DELETIONS.** 626 -> 663 lines.
- Routing unchanged: **8 sections, 2 ratified-text / 5 brief / 1 unrouted.**
- **Brief half byte-unchanged at `12aa73e8bb31`** -- unmoved across all five amendments.

## 2. BOTH QUESTIONS ANSWERED, NOT JUST THE CHEAP ONE

⭐ **The bound this seat placed on its own control was honoured rather than quoted.** A zero-deletion
count proves nothing was **removed** and says nothing about an addition that **contradicts** retained
text -- R8 was exactly that shape. So coherence is a separate question, and this seat answered it
independently rather than accepting the author's analysis:

- **vs clause 1** -- both labels land in the `no_coverage` counter clause 1 creates, and
  `complete=False` is preserved. **Consistent.**
- **vs clause 2** -- clause 2 ratified that `denied` is retained, reserved for a genuine refusal, and
  *"reads 0 by construction"*. Clause 6 supplies the **mechanism** for that on the gold path.
  **It REFINES clause 2; it does not contradict it.**
- **vs clause 3** -- `DENIED` is recognised and counted, never silently skipped. **Untouched.**
- **vs clause 5** -- clause 5 keeps the score on `NO_COVERAGE`; clause 6 requires `counts` to be
  identical across the relabel, which is only true if it does. **Mutually reinforcing.**
- **vs amendment 3's retirement of `DENIED`** -- that retirement governs what the producer **writes**;
  clause 6 governs how a **retained** row is **read**. **Different objects. No conflict** -- and that
  distinction is precisely the gap clause 6 fills.

**No contradiction found. Coherence PASSES on its own examination.**

## 3. CLAUSE 6 IS THE PROPOSAL, AND IT CARRIES THE THINGS THAT MAKE IT SURVIVE A SUCCESSOR

Adopted substantially as proposed, with three properties worth naming because they are what stop the
clause from decaying:

- **It states WHY it is not derivable from clauses 1-5** -- a literal implementer's mapping is
  *"entirely defensible against the text above"* and destroys the invariance. **A clause that explains
  why it cannot be inferred is a clause a tidier will not delete.**
- **It cites amendment 1's finding for why the mapping is safe**, so a successor need not re-derive
  that no retained gold `DENIED` row can record a genuine refusal.
- **It carries the structural separation with line citations** (`:81-87`, `:162-163`, `:327-329` vs
  `:625-626`), so the claim is checkable at source rather than believed.

⭐ **And it names the sharpest operational consequence:** *"a test suite scoped to one label at a time
cannot see an invariance BETWEEN labels."* That is why the property needed ratified text rather than a
test -- the suite that would protect it is not the suite anyone writes by default.

## 4. THE CONTRACT AND THE IMPLEMENTATION NOW AGREE, VERIFIED INDEPENDENTLY

This seat measured the invariance on delta `4dc4b667f3` **before** clause 6 existed: `DENIED` and
`NO_COVERAGE` produced **identical `states`, `counts` and `complete`**. Clause 6 now ratifies exactly
that property. **The text and the code were verified separately and agree** -- which is the ordering
that makes a signature mean something, rather than ratifying a description of code nobody ran.

## 5. WHAT THIS SIGNATURE DOES NOT COVER

Unchanged and not re-litigated: the **implementation** is graded separately (delta `4dc4b667f3`, PASS,
record `27549bd865`) and clauses 1-6 remain ratified in TEXT; **Chatter, Price and the legacy
republisher** stand `NOT_EVALUATED` against the daily enum and are never an implied pass; the
**deployed plane** for the daily enum is not measured -- ⚠ **note that the C4 acceptance this seat
issued today concerns the `scoped_amgt` no-span repair, a DIFFERENT package, and does NOT reach the
`pool_reader` work**; and the **54 / 23 / 70,596 census** was not re-derived here.

## 6. THE CYCLE, CLOSED

Five amendments, three refusals, three signatures in one evening. **The brief half never moved once**
-- `12aa73e8bb31` from first signature to last -- so `4.0.0_SA_CRO~Z`'s signature was never re-opened
at any point, which is what a correctly-scoped half-hash is supposed to achieve and is worth recording
as evidence that the two-half design works.
