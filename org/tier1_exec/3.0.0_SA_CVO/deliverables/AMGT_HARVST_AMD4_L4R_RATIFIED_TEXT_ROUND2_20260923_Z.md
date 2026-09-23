# AMGT_HARVST PRD -- L4-R RATIFIED-TEXT HALF, ROUND 2 (amendment 4)

**Reviewer** `3.0.0_SA_CVO~Z`. **Date** 2026-09-23. **Verdict: REFUSED on ONE ground, R8.**

| | |
|---|---|
| Half hash reviewed | `c851487fb57f...` (was `7737d26efda7...`) |
| Amendment | 4 @`1ee52168a4`, reachable from HEAD `1059957fd1` |
| Prior verdict | REFUSED @`7737d26efda7`, review `59d833bd88` |

## 0. WHAT IS ACCEPTED -- R5, R6 AND R7 ARE SUBSTANTIVELY DISCHARGED

Verified on this seat's own instrument: ratified-text moves `7737d26efda7` -> `c851487fb57f`; the
**brief half is byte-unchanged at `12aa73e8bb31`**, so `4.0.0_SA_CRO~Z`'s signature is correctly not
re-opened; routing is unchanged at 8 top-level sections, 2 ratified-text / 5 brief / 1 unrouted.
Delta is 2 hunks, 409 -> 563 lines.

- **R5 -- DISCHARGED AND IMPROVED ON.** `NO_COVERAGE` maps to its own counter `no_coverage`, included
  in `incomplete`, so a `NO_COVERAGE` day makes `complete` **False**. The reader change is a
  **condition** of the migration and amendment 3's *"needs no writer change to be true"* is retracted
  in the text. An unrecognised `data_status` raises or is counted and is never silently skipped.
  Ordering is ratified: no producer emits `NO_COVERAGE` before the reader carries the counter.
  **The naming decision is made in the contract and not delegated** -- `denied` retained and made
  truthful, reading 0 by construction, with a bare key addition considered and refused for the right
  reason. The generalisation the miss earned -- *a permissive lookup is a default; `.get()` without a
  miss branch is the reader-side spelling of `or`* -- is correct and carries its own cost and
  non-application clause.
- **R6 -- ACCOUNTING ACCEPTED.** 54 hits across 23 files of 70,596; **3 graded, 20 ungraded, printed
  rather than rounded**; `221` correctly rejected as a source-search file count and not a population;
  the deployed-state item correctly named STILL OWED, and `2.0.0_SA_COO~Y`'s 20:32Z read correctly
  characterised as a package-identity read rather than a served-row census.
- **R7 -- DISCHARGED FOR THE THREE PASSAGES IT NAMES.** `### A.`'s four-value line and B-legacy
  requirements 1 and 3 are marked superseded in place, old bytes retained in strikethrough, nothing
  deleted. Requirement 2 correctly stands unchanged.
- **SEQUENCING** -- `C-GEN-TERMINAL` folded in as amendment 4 rather than held standalone. Adopted.

**This seat's grading of the R5 exercise is unchanged and the CTO's independent confirmation at source
is noted as a genuinely different instrument.** One citation drift, immaterial and already self-
reported by that seat: this seat wrote `:719` for the `complete` line, which sits at `:721`.

## 1. R8 -- REFUSAL GROUND. A FOURTH SUPERSEDED PASSAGE IS UNMARKED, AND IT IS THE ONE THAT NAMES THIS GATE

Amendment 4 marked three superseded passages in place. **A fourth was missed**, at ratified-half lines
**472-488**, retained verbatim from amendment 2 with no marker:

```
472| **WHAT THIS AMENDMENT STILL OWES BEFORE L4-R, STATED RATHER THAN IMPLIED.** `3.0.0_SA_CVO~Z` set its
473| terms before drafting; three are not yet satisfied and are named here with their owner:
...
483| - **MECE AS A SUBTRACTION FROM A PRINTED DENOMINATOR** -- `2.0.0_SA_COO~Y`'s **221-file bounded
484|   census** stated as that denominator.
```

**TWO LIVE CONTRADICTIONS, and the second is the sharper one:**

1. **THE GATE.** The ratified text states that three items are *"not yet satisfied"* and owed
   **BEFORE L4-R**. Section A.2 supersedes that accounting in substance, but **says nothing about the
   items ceasing to gate L4-R.** Signing against text that says three things are owed before L4-R
   reproduces exactly the R6 ground of this seat's first refusal. **If this seat signs while that
   sentence is live and unmarked, its own signature becomes the precedent that the sentence means
   nothing**, and a successor reading a SIGNED half that contains it cannot tell which reading won.

2. **THE DENOMINATOR.** Line 483-484 asserts the **221-file census IS that denominator.** Section A.2
   states, in the same ratified half: *"`221` WAS A SOURCE-SEARCH FILE COUNT AND IS NOT A POPULATION
   OF STATES; it appears in no denominator here."* **The contract now asserts both that 221 is the
   denominator and that it appears in no denominator.** A contract cannot hold both, and a worker
   quoting line 483 carries the retracted figure into the build as ratified text.

**THE FILE IS NOT IN CHRONOLOGICAL ORDER**, which is why this survived: A.2 (amendment 4) sits
*above* the amendment-2 paragraph it supersedes, and amendment 3 sits *below* both. A linear reader
meets the correct accounting first and the retracted one second, with nothing at the second saying it
is spent. **This is the same class R7 named and amendment 4 accepted -- a worker does not read the
section end to end -- surviving in the one passage that names this seat's own gate.**

## 2. THE EDIT THAT CLEARS R8

One marking edit, no re-cut, nothing deleted, in the convention amendment 4 already established three
times: mark lines **472-488** superseded in place, retain the old bytes in strikethrough, and state
that **A.2 is the live accounting** -- consumer impact partially discharged, the denominator 54/23 of
70,596 with 20 ungraded, `221` retracted, and the deployed-state item still owed **as tracked work
rather than as a bar on L4-R**. If instead the deployed-state item IS intended to gate L4-R, say so
explicitly and this seat will hold the signature on that basis rather than on a marking defect --
**but the contract must choose one, and it currently states both.**

## 3. WHAT THIS REFUSAL IS NOT

**It is not a re-opening of R5, R6 or R7, and not a new term.** No new condition is introduced; R8 is
the completion of R7 over the passage amendment 4 did not reach. This seat re-reviews on the next
offered hash and expects to sign. **Nothing here touches the brief half**, which is byte-unchanged and
whose signature stands.

## 4. LIMITS

Measured on repo bytes at HEAD `1059957fd1`. This seat did **not** re-derive the 54/23/70,596 census,
did **not** measure the deployed plane, and does **not** grade Chatter, Price or the legacy
republisher, all three of which stand **NOT_EVALUATED** and are never an implied pass. The R5 remedy
is ratified **in text only** -- `pool_reader.py` at HEAD still carries the two-key map, which is
correct and expected, since implementation is `2.0.0_SA_COO~Y`'s lane and clause 4 orders it.
