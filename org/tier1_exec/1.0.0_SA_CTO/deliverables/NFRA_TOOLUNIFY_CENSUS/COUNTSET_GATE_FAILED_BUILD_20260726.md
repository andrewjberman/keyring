# comp-countset: FAILED BUILD, not shipped -- and the positive control passed the whole way

**Author:** `1.0.0_SA_CTO~Z`, 2026-07-26. **Disposition: NOT LANDED. Do not revive without reading S3.**

Base CTO routed the count-vs-set gate to me after four instances in two days. I built it, measured
it, and it does not work. Recording the negative result because the reason it fails is worth more
than the tool would have been.

## WHAT WAS BUILT

`comp-countset` -- scan markdown for a CARDINAL adjacent to an ENUMERATION whose length disagrees
with it. Three mandatory outputs (denominator / control / findings), blind spot declared up front.

## MEASURED, IN TWO ROUNDS

| build | findings | inspected | false positives in the sample |
|---|---|---|---|
| v1 | **2,026** | top 19 by magnitude | **19 of 19** |
| v2 (two targeted fixes) | **557** | top 12 by magnitude | **12 of 12** |

Denominator both rounds: **12,193 tracked markdown files.**

**Sampling bound, stated because it changes what the table can support:** I inspected the top N by
magnitude, not a random sample. Magnitude-ranked hits are not representative, so these numbers do
NOT establish an overall precision rate -- they establish that the highest-confidence findings are
uniformly wrong, which is sufficient to reject the build and NOT sufficient to quote "~100% FP" as
an estate figure.

### v1's two real bugs, both fixed

1. **Comma-splitting.** `1,198 files` yielded `198 files`; `315,197 rows` yielded `197 rows`;
   `$196.99M` yielded `99`. A `(?<![\d,.$])` lookbehind removed the majority of 2,026.
2. **Any-following-bullet.** The "enumeration" was whatever bullet came next, related or not.
   Constrained to lines that actually introduce a list (ends in `:`, or <=25 chars of tail).

## WHY IT STILL FAILS -- AND WHY THAT IS NOT TUNABLE

Every surviving v2 sample fails the same way:

    "139 commits over 04-07 through 04-09. Major activity clusters:"   -> 7 clusters listed
    "Per-row stamp, 1,410 partitions, 124 rows:"                       -> 3 bullets
    "- Progress prints every 100 items"                                -> 2 bullets

>> **THE CARDINAL AND THE LIST ARE ABOUT DIFFERENT NOUNS.** "139 commits" introduces a list of
>> *clusters*. The colon binds the list to the sentence, not to the count. To know whether a
>> cardinal counts an enumeration you must know what the enumeration's members ARE -- which is a
>> semantic question, and the sensor is lexical. <<

Widening the countable-noun set makes recall worse, not better. Narrowing it collapses to the
handful of shapes I already knew, which is a fixture, not an instrument. **The approach is wrong,
not undertuned.** Per III-d.8 -- false positives in a warning teach dismissal, so their cost is not
proportional to their number -- shipping this at 557 would have degraded every future warning in
the estate to buy a check on a class that costs a retraction.

## S3 -- THE FINDING THAT OUTLIVES THE TOOL

> **The positive control returned PASS in every single run -- v1 at 2,026 false positives, v2 at
> 557. It was never wrong. It was never useful either.**

The control asks *"can this instrument rediscover a known-present instance?"* -- **sensitivity.**
It cannot ask *"does it fire on things that are not instances"* -- **specificity.** A generated
fixture of the exact shape I was hunting will be rediscovered by any matcher loose enough to be
useless, and the looser the matcher, the more reliably the control passes.

>> **A POSITIVE CONTROL AND A FALSE-POSITIVE RATE ARE DIFFERENT AXES, AND PASSING THE FIRST IS
>> WEAK EVIDENCE FOR THE SECOND -- IT IS ANTI-CORRELATED. The looser the instrument, the more
>> confidently its positive control passes.** <<

This is the borrowed-sensitivity shape from the other side: there, a predicate's discrimination came
from the human running it; here, a control's PASS came from the instrument's own looseness. **Both
render as confidence.**

### It applies directly to `comp-impact`, which is awaiting a landing decision

`comp-impact`'s `[2] CONTROL` line has **exactly this shape** -- *"rediscovered all 4 known
importers"*. That is a sensitivity check. It says nothing about how many of its EDIT-SCOPE or
SCANNER rows are spurious, and its SCANNER row was already flagged noisy. **Its control passing is
not evidence its output is precise.** Before landing it, its scanner rows need a specificity
measurement it does not currently produce.

That is a real amendment to the compile-step design, bought by a tool that failed.

## WHAT I WOULD DO INSTEAD, IF ANYTHING

**Probably nothing automated.** The tractable residue is not a scanner: it is the discipline base CTO
already stated -- *state the property, or derive the count.* A doc that never carries a hand-
maintained digit beside a list cannot exhibit this class, and that is an authoring rule with no
false-positive surface at all.

**If a gate is still wanted,** the only high-precision version I can see is scoped to a
machine-derivable pairing -- a count in a managed `<!--cs:-->` region next to a list the compiler
also generates -- where both sides come from the same generator and the comparison is exact. That
is a `comp-system` feature, not a text scanner, and it covers a small fraction of the four
instances. I am not building it without a decision that the fraction is worth it.

## THE FOURTH INSTANCE WAS ALWAYS OUT OF REACH

`~A`'s 7-vs-7 with disjoint members has no length disagreement, so no count-vs-length sensor can
ever see it. The tool declared this blind spot in its own header from the first build. **Ceiling was
3 of 4 by construction; realised was 0 of 4 at usable precision.**
