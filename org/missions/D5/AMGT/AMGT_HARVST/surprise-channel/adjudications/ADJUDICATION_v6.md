# AMGT_HARVST round 2: CVO adjudication, ADDENDUM 4 -- the entailment I had the sentence for and did not draw

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T03:3xZ, LOCAL on SITEZ. **Refines:** my own `C-S9`
(ADJUDICATION_v5 @`8798bed2d8`). **Dispositions:** `Z-S8`.

## Why I moved after saying I would not

v5 said I would not move again "without new bytes in the spec." **These are not new bytes — and that is the
point.** `2.0.0_SA_COO~Y` drew an ENTAILMENT from a clause **I had already quoted, in v5, as my own clause 3.**
⛔ **I had the sentence and did not reason from it.** Verified here before adopting anything, whitespace
normalised because the sentence is line-wrapped in the source:

> *"If the day/event dissection call fails while the line itself loaded, only the dissection panel shows this
> state independently -- it does not force the whole line into it."*

**The entailment holds and I checked it rather than took it:** for the panel to show the failure of ITS OWN call
while the line loaded fine, **the panel must receive its own call's outcome.** A panel with no error input cannot
satisfy that sentence. **So the spec DOES require a typed channel — at a specific named surface.**

## What that does to each standing claim

| claim | final |
|---|---|
| `Z-S5`'s UNIVERSAL ("no clause requires ANY surface to receive the error") | ⛔ **FALSE.** The independence clause requires it of the dissection panel. |
| my `C-S9` ("a surface with no error input CAN exist compliantly") | ⚠ **TOO BROAD.** True of the chart, which a container may gate; **FALSE of the dissection panel**, which the spec names. |
| `C-S400`'s harm cannot recur | **TRUE**, unchanged through all six moves. |
| the typed-channel clause is owed in the spec | ⛔ **STRUCK — it is already there**, written as a behaviour rather than as a prop. |

## ⛔ MY OWN FAILURE, AND IT IS SHARPER THAN THE ADOPTIONS

In v5 I listed that clause as **evidence for the opposite conclusion** — I quoted "a failed dissection call shows
the state in its own panel independently" in the same table where I wrote that a surface with no error input can
exist compliantly. **The sentence that refutes it was in my own settlement, in my own words, and I did not draw
its consequence.**

⭐ **That is a different failure from the adoptions, and worse: the adoptions were deference; this was having the
evidence and not reading it.** A quoted clause is not a used clause. **When a settlement quotes a sentence, the
test is whether the conclusion would survive if that sentence were read alone — mine would not have.**

## And the scan's limit, measured

The keyword list — `prop`, `component`, `interface`, `signature`, `contract`, `receives` — has **ZERO matches in
that clause.** The instrument could not have found it at any threshold, because the guarantee is written as a
BEHAVIOUR ("the panel shows this state independently") and not as a noun. ⭐ **A scan licenses "I did not find the
word"; it can never license "no clause requires it."** `2.0.0_SA_COO~Y` names Rule 24's tell on itself, and it is
the right one: a UNIVERSAL on five irrelevant hits.

## Standing, final

**AC4's PASS has not moved in v2, v3, v4, v5 or here — six records, one grade.** The typed-channel requirement
exists in the spec for the surface the spec names, the container may gate the rest, and **no clause is owed.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S10",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T03:35Z",
    "one_line": "REFINES C-S9 on an entailment this seat had the sentence for and did not draw: the independence clause ('only the dissection panel shows this state independently') REQUIRES that panel to receive its own call's outcome, so Z-S5's universal is FALSE, C-S9's 'a surface with no error input can exist compliantly' is TOO BROAD, and the typed-channel clause is STRUCK as already present.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Clause read here with whitespace normalised (it is line-wrapped in the source): 'If the day/event dissection call fails while the line itself loaded, only the dissection panel shows this state independently -- it does not force the whole line into it.'",
        "Entailment verified rather than adopted: a panel that cannot receive its own call's outcome cannot show that failure while the line renders normally.",
        "The scan's keyword list (prop, component, interface, signature, contract, receives) has ZERO matches in that clause -- the guarantee is written as a BEHAVIOUR, not a noun."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A build against this spec cannot reproduce the Z-S227 / C-S400 defect on this surface.",
    "world_is": "The defect cannot recur, and the spec additionally requires a typed channel at the one surface it names.",
    "notes": "⛔ MY OWN FAILURE, WORSE THAN THE TWO ADOPTIONS: in v5 I QUOTED this clause as evidence for the opposite conclusion. The sentence that refutes my formulation was in my own settlement, in my own words, unused. A QUOTED clause is not a USED clause -- the test is whether the conclusion would survive if that sentence were read alone, and mine would not have. AC4's PASS has not moved across six records. No clause is owed; position 2 is correctly struck.",
    "adjudicates": [
      "AMGT_HARVST-Z-S8"
    ],
    "dismissal_reason": "A refinement record on the text: it narrows this seat's own C-S9, adopts the verified entailment, strikes an owed clause as already present, and moves no grade."
  }
]
```
