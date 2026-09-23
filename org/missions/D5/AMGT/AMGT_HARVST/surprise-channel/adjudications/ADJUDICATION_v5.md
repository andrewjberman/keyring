# AMGT_HARVST round 2: CVO adjudication, ADDENDUM 3 -- SETTLED ON THE TEXT, and this seat stops moving

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T03:2xZ, LOCAL on SITEZ. **Corrects/settles:** `C-S7`
(ADJUDICATION_v3) and `C-S8` (ADJUDICATION_v4), and dispositions `Z-S7`.

## The oscillation, stated so it ends

`Z-S5` (mechanism not covered) -> my `C-S7` adopted it -> `Z-S6` withdrew it -> my `C-S8` adopted the withdrawal
-> `Z-S7` restores `Z-S5`. **Five moves on one question, four of them adoptions of whatever arrived last.**
⛔ **Every move after the first was a seat reading another seat's SUMMARY rather than the spec's TEXT.** I am
settling it on the text, and I will not move again without new bytes in the spec.

## The text, read once more, at `:205-218`

Three clauses bear on it:
1. the failed state is **"decided by the transport/envelope outcome, never by any row `chatter_daily` or
   `chatter_event` holds"**;
2. **"Never a blank chart, an empty series, or a zero-height line is drawn for this state"**;
3. **"It renders its own distinct, PAGE-LEVEL error state"**, and a failed dissection call shows the state in its
   own panel **"independently"**.

## The settlement: BOTH FINDINGS ARE TRUE OF DIFFERENT OBJECTS, AND NEITHER SIDE WAS WRONG

| claim | verdict on the text |
|---|---|
| `C-S400`'s HARM (absence asserted as fact) cannot recur | **TRUE.** Clause 2 forbids the empty render during a failure, whichever component would have produced it. |
| A build may still contain a surface with no error input | **TRUE.** Clause 3 puts the state at PAGE level, so a compliant build may gate at the container and never render the inner chart during a failure. |
| "A surface that cannot receive the transport outcome VIOLATES the spec" (**my `C-S8`**) | ⛔ **TOO STRONG. WITHDRAWN.** It violates only if it RENDERS during a failure; a container that withholds it is compliant. |
| "The spec closes one of the two cited defects" (**`Z-S5`, restored**) | **TRUE AS TO THE MECHANISM, and not as to the defect.** The missing-channel PATTERN survives; the DEFECT — the false sentence a viewer sees — does not. |

⭐ **So the two findings never actually contradicted: `Z-S5` is about a CODE SHAPE, my v2 was about a RENDERED
OUTCOME, and the criterion asks about the outcome.**

## AC4's PASS stands, and it never depended on this

The criterion asks whether every state is DRAWN such that a build cannot reproduce the `Z-S227` / `C-S400` defect
on this surface. **Under BOTH readings the defect cannot be reproduced.** The grade has not moved in v2, v3, v4 or
here; only my stated reason moved, twice, and it is now fixed to the text rather than to a peer's summary.

## What is owed, finally

- **The typed-channel clause is worth cutting anyway**, at the issuer's position 2 — not because the spec fails
  the criterion, but because **"the container gates it" is a build-time decision the spec currently leaves open**,
  and a later refactor that renders the chart during a failure would be a spec violation nobody would catch at
  review. A clause that removes the freedom costs one sentence.
- **No remediation row is owed on `C-S7` or `C-S8`.** Both are superseded here.
- ⛔ **A DISCIPLINE, stated for every seat in this exchange including me: an adoption is not a measurement.** Four
  of the five moves were adoptions. The only two acts that produced new information were the original scan and the
  re-reads of the text — and the re-reads settled it.

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S9",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T03:25Z",
    "one_line": "SETTLES the Z-S5/Z-S6/Z-S7 and C-S7/C-S8 oscillation on the spec's own text: the HARM cannot recur (an empty render during a failure is forbidden whichever component would produce it) and a surface with no error input CAN exist in a compliant build (the state is PAGE-LEVEL, so a container may gate it). Both findings are true of different objects; my C-S8's 'such a surface VIOLATES the spec' was too strong and is withdrawn.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC_SECTION_timeline.md :205-218, read here: the state is decided by the transport/envelope outcome never by a stored row; never a blank chart, empty series or zero-height line is drawn for it; it renders its own distinct PAGE-LEVEL error state, and a failed dissection call shows the state in its own panel independently.",
        "Sequence: Z-S5 -> C-S7 adopted -> Z-S6 withdrew -> C-S8 adopted the withdrawal -> Z-S7 restored Z-S5. Four of five moves were adoptions of the latest arrival rather than reads of the text."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A build against this spec cannot reproduce the Z-S227 / C-S400 defect on this surface.",
    "world_is": "It cannot reproduce the defect under either reading; the missing-channel code shape survives, gated at the container.",
    "notes": "AC4's PASS never moved and does not depend on this. ⛔ THE TYPED-CHANNEL CLAUSE IS STILL WORTH CUTTING at the issuer's position 2 -- not because the spec fails the criterion, but because 'the container gates it' is a build-time freedom the spec leaves open, and a later refactor rendering the chart during a failure would violate the spec with nobody positioned to catch it. ⛔ DISCIPLINE FOR EVERY SEAT IN THIS EXCHANGE, MINE INCLUDED: AN ADOPTION IS NOT A MEASUREMENT. Four of five moves were adoptions; the only acts producing new information were the original scan and the re-reads of the text.",
    "adjudicates": [
      "AMGT_HARVST-Z-S7"
    ],
    "dismissal_reason": "A settlement record on the text: both prior findings are true of different objects, this seat's own overreach is withdrawn, no grade moves and no remediation follows."
  }
]
```
