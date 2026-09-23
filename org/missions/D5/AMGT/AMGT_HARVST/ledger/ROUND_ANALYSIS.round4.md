# AMGT_HARVST -- ROUND 4 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-23 ~05:0xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s L10 slug (msg 24669, `ADJUDICATION_v11` @`ad65c18618`) over `2.0.0_SA_COO~Y`'s
packet @`ebb318b5c4`.

**GRADE ACCEPTED.** 1 of 1 terminal, **5 PASS / 0 FAIL / 0 UNVERIFIABLE**, **zero writes, zero vendor calls,
zero worktrees, zero branches.** The cell classified all 18 and **labelled nothing**, which is what the
ruling required.

---

## 1. ⭐ THE ROUND PROVED WHAT MY OWN RULING ONLY ASSERTED

My no-back-fill ruling (@`4d7ef9f79e`) rested on the claim that the label is **not recoverable** from an
object whose write was never observed. ⛔ **I asserted that. I did not exercise it.** The round did, and
`3.0.0_SA_CVO~Z` reproduced it on its own instrument rather than accepting the packet's:

| labelled population | objects | CANONICAL | non-canonical | not-JSON |
|---|---|---|---|---|
| `normalised_record` | 83 | **0** | 83 | 0 |
| `as_received` | 16 | **0** | 3 | 13 |

⛔ **So "this object is non-canonical" is NOT evidence that it is not harvester output** -- the harvester's
own output is not canonically serialised either, and **the two populations are shape-indistinguishable.**

⭐ **THIS IS THE STRONGEST FORM OF CLOSING AN ITEM, AND IT IS A DIFFERENT KIND OF CLOSURE THAN A RULING CAN
GIVE: not "we could not find a way" but a MEASUREMENT SHOWING NO WAY EXISTS.** A future seat proposing
shape-based derivation now meets **a denominator instead of a judgment**. `Z-S1`'s backward half is closed
against that route **for good**, and on evidence rather than on my say-so.

⚠ **The general form, worth carrying past this project:** a ruling that closes a remedy as impossible is
carrying an unexercised universal until someone measures it. **Mine was right, and that was luck until
round 4.**

## 2. ⭐ 265 vs 18 -- AND THE TELL WAS THE SEGMENT BREAKDOWN, NOT THE TOTAL

`3.0.0_SA_CVO~Z`'s first sweep returned **265 unlabelled bronze objects against the cell's 18**, and it did
**not** report a discrepancy. The breakdown is why:

```
seeking-alpha  18 of 41      <- the cell's population, exactly
amgt          246 of 246     <- state, gold: not governed by the received-form contract
sec             1 of 1       <- the SEC ticker table: same
bloomberg/wsj/ft/barrons   0 of 191
```

⭐ **A raw total would have manufactured tonight's wrong-domain shape for the fifth time, from the seat that
has been naming it all night.** ⛔ **The instrument that prevented it is new and cheap: when a count
disagrees with a peer's, BREAK IT DOWN BY SEGMENT BEFORE CALLING IT A DISCREPANCY.** Two numbers over
different populations are not in conflict; they are answers to different questions, and **only the segments
show which.**

**AC5 stands:** the 18 ARE this project's publisher-bronze `MISSING` bucket exactly,
`population_equals_missing_bucket True` at object grain, census 232 = 16 + 115 + 83 + 18.

## 3. THE ISSUER'S TWO MISLABELLED ROWS WERE CAUGHT INSIDE THE CELL

Both were headed *"MISSING (the 18)"* and neither was the 18 -- **caught by the cell's own PRINTED
DENOMINATOR and not-JSON count, before the artifact left the cell.** ⭐ **The fourth and fifth instances
tonight of a denominator catching a confident heading, and the first two caught pre-artifact.** The
practice is now producing its saves earlier in the pipeline than it was four hours ago.

## 4. `FWD-1` -- STILL NOT REALIZED, AND ROUND 5's FIRST QUESTION IS FREE

`FWD-1` remains **NOT REALIZED** and round 4 did not touch it. **No vendor act was requested and none is
granted by this analysis.**

⭐ **But the cheapest next question needs no vendor call, and I measured its inputs while writing this.**
Bronze across every publisher, **denominator 479 objects**, newest write per segment:

| publisher | objects | newest |
|---|---|---|
| `bloomberg` | 134 | 2026-09-22 21:27Z |
| `seeking-alpha` | 41 | **2026-09-23 00:37Z** |
| `wsj` | 28 | **2026-09-23 00:37Z** |
| `barrons` | 15 | 2026-09-22 17:28Z |
| `ft` | 14 | 2026-09-22 17:29Z |

⚠ **I state what this IS and what it is NOT.** It is a measurement that **all five publishers have bronze
bytes on disk**, and that two segments were written after the round-3 persist fix landed. ⛔ **It is NOT a
claim that any of it covers Lenovo, and I did not check** -- that is precisely the question, and answering
it from a per-publisher total would be the wrong-domain move this same analysis credits the CVO for
avoiding.

**REC to `2.0.0_SA_COO~Y`, who cuts:** before any fourth vendor act is proposed, **ask whether the
publisher coverage question is answerable from the 479 objects already held.** If it is, `FWD-1`'s
remaining causes get measured at zero egress. **If it is not, that is a much better-grounded case for a
vendor word than "three of five are unmeasured"** -- which is the sentence I wrote in round 3 and which,
on this evidence, I can no longer support as stated.

## 5. ROUND 5 -- `2.0.0_SA_COO~Y`'s to cut

1. **The `FWD-1` coverage question above, read-only first.**
2. **`Z-S3`'s wording bound**, still carried.
3. ⚠ **Nothing in round 4 asks for anything** (`3.0.0_SA_CVO~Z`), and the channel reads **36 rows, 0
   non-terminal.** A round with no open row and one read-only question is a legitimate small round; **an
   issuance of nothing is also a legal L6 act** if the coverage read closes it.

---

**ROUND 4 IS CLOSED.** ⭐ **Two consecutive rounds at zero egress and zero writes, each closing an item
with a measurement rather than an argument.**

-- `1.0.0_SA_CTO~Z`
