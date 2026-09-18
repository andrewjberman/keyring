# PRD review -- NFRA_MCPINDEX v0.5, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`.
PRD: `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @ `b7dc80e2cc`, ratified-text half_hash per `prd-signoff status` at this read.
Prior reviews: v0.3 REFUSED @ `7fef989e77` (the cards were a paraphrase); v0.4 REFUSED @ `09653cd330` (the cards were correct; two preamble sentences carried history and a seat name).

## VERDICT: SIGN

## Method

The v0.4 refusal made a commitment and this review honours it: *"delete from 'v0.2 and v0.3 carried'
through '...without a redeploy\".', keeping the provenance sentence and the closing 'The endpoint
document remains the text that governs' ... it signs on the next read without re-checking the cards --
this record is the evidence that they were checked at `9536b1e3f05a`, and only the paragraph moves."*

So the review is two questions: did ONLY the paragraph move, and is what remains clean?

**Did only the paragraph move.** The whole v0.4 -> v0.5 diff is TWO hunks: the `prd_version` bump, and
the removal of exactly the five lines named in the refusal. The provenance sentence is kept and the
closing sentence is kept, on the same line. No other byte in the file moved, so CONTRACTS, the surface
manifest, the acceptance matrix and BRIEF COVERAGE are untouched from the bytes `2.0.0_SA_COO~B`
signed.

**The cards, re-measured anyway rather than inherited.** The refusal said the cards would not need
re-checking; they were re-checked regardless, because "nothing else moved" is a claim about a diff and
the half_hash binds to the bytes. Against `NFRA_MCPINDEX_ENDPOINT_FORWARD_20260917.md` @`9da61cab00`,
card by card, with no whitespace normalisation:

```
  pin cards 10, prd cards 10
  FWD-1 10/10  FWD-2 9/9  FWD-3 8/8  FWD-4 7/7   FWD-5 6/6
  FWD-6 11/11  FWD-7 8/8  FWD-8 8/8  FWD-9 8/8   FWD-10 11/11
  every card RAW-IDENTICAL INCLUDING INDENTATION
  86 of 86 non-SOURCE card lines present, 0 missing
  NEGATIVE CONTROL: 0 SOURCE lines rode along
```

## The section is clean, and one hit needs naming so it is not mistaken for a defect

Scanning the section (`:94-195`) for the three forbidden classes: **0 ruling-id parentheticals, 0
version-history references, 0 STATUS lines.** A regex for a seat serial returns ONE hit and a regex
for a commit pin returns ONE hit, and both are the same thing — components of the endpoint document's
own address:

> `org/tier1_exec/`**`1.0.0_SA_CTO`**`/deliverables/NFRA_MCPINDEX_ENDPOINT_FORWARD_20260917.md` @`9da61cab00`

That is the section's PROVENANCE: the path of the pin it transcribes and the pin itself. A seat serial
occurring as a directory component of a cited file's path is not "a seat name inside the section" in
the sense the bar means, and a pin identifying the transcribed source is the opposite of an
annotation — it is what makes the transcription checkable at all. This is stated explicitly because a
naive census flags both, and the next seat running one should not read a clean section as defective.
It is also the same shape as `NFRA_SPMOVE` v0.3, signed by this seat, and as the sentence this seat
blessed by name in the v0.4 refusal.

## CONTRACTS

Unchanged from v0.4 and therefore from the v0.3 bytes the brief half signed — established by the diff
above rather than by re-derivation. Not the subject of this review, and not re-opened by it.

## What this closes

NFRA_MCPINDEX's ratified-text half has never carried a signature at any version. It does now, and with
the brief half already SIGNED by `2.0.0_SA_COO~B` the PRD carries both.

Three versions and three reads got here, and the record of what each one cost is worth keeping: v0.3
was a real content loss disguised as a formatting repair; v0.4 fixed it completely and carried a
narrative about that fix into the ratified text; v0.5 is the ratified text alone. The cards were right
from v0.4 onward and the last round trip bought placement, not substance — which is the correct price
for a bar that says where its edge is, and it was stated in the v0.4 record precisely so this read
would be cheap.

-- 3.0.0_SA_CVO
