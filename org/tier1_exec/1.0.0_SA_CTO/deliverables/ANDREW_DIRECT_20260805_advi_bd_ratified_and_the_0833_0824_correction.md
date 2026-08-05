# ANDREW-DIRECT 2026-08-05 -- Phase-0 vertical 1 RATIFIED, and a correction to my evidence line

**Channel:** `1.0.0_SA_CTO~B` terminal, direct, during the Phase-0 ratification sitting (one
vertical at a time, his chosen format: *"No i want to answer one by one for Phase-0, it is
worthwhile"*).

## VERBATIM (unedited -- the phrasing IS the ruling)

> "First, the black diamond account for 49financial is the 0833 prefix schwab account, not the 0824
> prefix schwab account. We use 0833 for advi, known as "Advisor Intelligence" an Opal data product
> served by the Portal that is scoped per advisor (49 Financial, in this case, for 49F, and 0824 for
> mdpf, known as "Model Portfolios", (in this context, an Opal data product in the context of the
> Portal) for 49F, for business logic reasons. It is a permanent project nevertheless, although
> underlying conventions and resources may shift around with migrations/consolidations/refactoring/etc."

## WHAT THIS SETTLES -- three distinct things

### 1. RATIFICATION: `advi-bd` = **PERMANENT**
Phase-0 vertical 1 of 29 is ratified. *"It is a permanent project nevertheless."* The "nevertheless"
carries weight: he ratified PERMANENT **while** correcting the evidence I offered for it, i.e. the
value does not rest on the account-prefix detail I got wrong.

### 2. CORRECTION OF FACT (mine to own -- see below)
| | Schwab account prefix | Product | Portal-facing name |
|---|---|---|---|
| **ADVI** | **0833** | Advisor Intelligence | scoped **per advisor** (49 Financial here) |
| **MDPF** | **0824** | Model Portfolios | for 49F |

**The split is FOR BUSINESS-LOGIC REASONS** -- his words. It is not a storage-layout accident, and
the two are not interchangeable.
My Phase-0 table row 1 cited "49F Black Diamond medallion... (account 08242234)" as advi-bd's
evidence. **That is the MDPF account, not the ADVI one.**

### 3. THE GRAIN CONVENTION IS ANSWERED (this binds the remaining 28)
I asked whether `lifecycle_class` at VERTICAL grain means the business function's life-shape, given
the rule bank's polarity table is written at ARTIFACT grain. His sentence answers it:

> *"It is a permanent project nevertheless, although underlying conventions and resources may shift
> around with migrations/consolidations/refactoring/etc."*

**RATIFIED READING: the value names the BUSINESS FUNCTION's life-shape. Interior churn --
migration, consolidation, refactoring, a resource renamed or a route re-pointed -- IS NOT A
LIFECYCLE SHIFT.** That is exactly what the draft table's grain note proposed, now sovereign rather
than assumed. Consequence for R2: interior churn is what the **State layer WATCHES and proposes on**
(the shift-watch column), never what the value itself tracks.

## MY MISS, AND IT IS THE WORST KIND: THE GUARD WAS ALREADY LOADED

`memory/MEMORY.md` carries this as a STANDING banner, at the top, in the always-loaded index:

> `## !! TWO 49F SCHWAB BUCKETS: NEVER ADD, NEVER SUBSTITUTE !!`
> `0833`=ADVISOR INTELLIGENCE master - `0824`=MODEL PORTFOLIOS master, a BUSINESS-PURPOSE split
> (Andrew 07-16), **NOT mechanically enforced -- agent discipline only.**

**I had this in context and substituted anyway** -- the exact operation the banner names, on the
exact pair it names, into a ratification table meant to become canon. The banner even states its own
enforcement model: *agent discipline only.* There is no gate behind it. **I was the gate, and I
failed open**, in a document whose purpose is to be ratified and landed as the estate's semantic
truth.

Worth recording precisely because of what today has otherwise been about: I have spent the session
finding records that were confidently wrong and instruments that reported healthy while something
was broken. This one had a correct record, loaded, warning me in capital letters, and it did not
stop me. **A memory banner is a control with the same failure mode as a WARN-only gate -- it works
only if the reader chooses to act on it, and "I already know that" is how it gets skipped.**

## Routing
Recorded here (durable, committed under this seat's author line) and BROADCAST same turn to
`2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.0.0_AB_MSTR` per the `org/XXX.md` Andrew-direct law, plus
`3.0.0_SA_CVO` as the seat that LANDS ratified Phase-0 values in canon.
Proposal table row 1 corrected + marked RATIFIED in the same commit.
