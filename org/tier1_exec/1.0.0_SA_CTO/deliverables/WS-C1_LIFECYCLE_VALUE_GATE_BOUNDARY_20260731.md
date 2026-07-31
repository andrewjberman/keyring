# WS-C1 -- THE LIFECYCLE-VALUE GATE: WHERE THE BOUNDARY RUNS

**CORE owner's WORKING boundary. PROVISIONAL -- routed to Andrew via MSTR~Z for confirmation.**
Issued because seats are blocked without one under an exclusive regime. It is NOT a re-statement
of Andrew's ruling and MUST NOT harden into one.

## THE RULING BEING BOUNDED (Andrew, verbatim; four-hop relay, stated as such)

> "It is impossible to know the Lifecycle Value of the resource without the user input pipeline you are building."
> "you [~B] are going to be proceeding the User Input Pipeline and when it is further along, you can lead the Lifecycle Values feature."

CORE-governing clause as relayed: the lifecycle VOCABULARY MECHANISM continues; POPULATING
lifecycle VALUES is gated; do not stand up a value-population seat.

## THE QUESTION

Raised by CVO~Z, who explicitly declined to adjudicate it and routed it here: WS-E1 tranche 1
landed declarations carrying POPULATED `lifecycle_class`. **Does the gate reach work already landed?**

MEASURED, not assumed -- 2 of 14 subjects declare `PERMANENT`. (Not "all UNDECLARED": that was
~C's first report, self-corrected. CVO asked the question without knowing this, so it is live,
not hypothetical.) Both cite `intent_source: docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md`.
One is joinable and is the single kill-list-eligible surface of 439 scored.

## THE DISCRIMINATOR IS `intent_source`, AND IT IS A REQUIRED FIELD THAT PREDATES THE RULING

Andrew's claim is about KNOWABILITY. The user-input pipeline's function is to SUPPLY INTENT THAT
IS NOT OTHERWISE WRITTEN DOWN. So the boundary runs on whether the intent already exists in
citable form:

- **DERIVED FROM A CITED, EXISTING `intent_source`** -- a ratified PRD, an Andrew-direct, or a
  producer declaring its own artifact. **Knowable today. LEGAL. Not gated.** Both landed
  `PERMANENT` records are this shape.
- **DECIDED WITHOUT AN `intent_source`** -- walking the estate resource-by-resource assigning
  values nobody has written down. **Exactly what Andrew gated**, exactly what the pipeline
  supplies, `~B`'s to own. **No such seat is stood up and none will be.**

### THE STRONG FORM: THE MECHANISM STRUCTURALLY CANNOT PRODUCE THE GATED CLASS

`contract_record.required` carries `intent_source`. Populating-without-knowing IS
populating-without-an-`intent_source` -- and that is UNWRITABLE in this grammar. A declaration
missing a required field renders UNKNOWN-LOUD with `kill_list_eligible: False`
(`comp_legacywriter.py:865-870` @88bf8f7bb), with **no fallback to the declared value and no
fallback to PERMANENT**. **The gate Andrew imposed was already enforced by a required field,
four hours before he stated it.** That is not luck: `intent_source` was made required precisely
so a lifecycle value could not exist without naming where the intent came from.

**GROUNDING CLASS: EXERCISED, not source-read (Rule 22a).** I originally cited this branch from
source. `3.0.0_SA_CVO~Z` then established that it is the exact branch they EXERCISED in their
increment-2 verify -- the half-declared case returning `gated=False`, `kill_list_eligible=False`,
`UNKNOWN, LOUD` -- **and that a mutant proved it could fail.** So the load-bearing claim under this
ruling is behaviour-grounded by a test run by a different seat before I made the claim, not by my
reading. **That is the strongest grounding available to a provisional ruling, and it is why I am
comfortable sending it up rather than holding it.**

## `locality` IS NOT REACHED

CVO asked whether the gate also reaches `locality` (7 records, all `global`), since it sits under
`lifecycle.locality_binding`. **Ruling: no.** `locality` is OBSERVABLE from the artifact's own
addressing -- one bucket, one object, served to all clients is `global` by construction.
`lifecycle_class` is INTENT. **Andrew gated intent-that-requires-asking; locality does not require
asking.** (`locality`'s own weakness -- `enum_exercised`, one of three values ever used -- is a
DIFFERENT defect and remains open. Do not let this ruling close it.)

## COST OF BEING WRONG -- BOUNDED, AND STATED BECAUSE THAT IS WHAT LICENSES PROCEEDING

If Andrew means the gate reaches PRD-sourced values too: flip 2 records to `UNDECLARED`,
eligibility returns to 0. **Nothing can have acted on it in the interim** -- a repo-wide search
finds NO automated consumer of `kill_list_eligible` outside the census tool that computes it.
The only path from eligibility to action is a human reading a census and applying judgment.
**Kill-list ELIGIBLE is permission to assert deadness, not a deletion.**

## CORROBORATION -- LABEL CARRIED INTACT, NOT UPGRADED

MSTR~Z relayed that base `~D` independently held ESTATE Bucket-1 on "`intent_source` structurally
unavailable / cannot infer PERMANENT," and explicitly marked it as their READ, not a verified
equivalence. **My finding names the same field.** That is a striking convergence and I am NOT
converting it into proof: I have not read `~D`'s artifact (other fabric), and "the same field is
named" is not "the same wall was hit." **Two parties naming one field is corroboration; upgrading
it here would be the could-map-therefore-does inference I have already made three times this
session.** The label stays as MSTR~Z set it.

## WHAT I AM ASKING ANDREW

**Only this, and only because a four-hop relay is exactly where a boundary gets assumed rather
than stated (CVO~Z's point, and it is correct):** does "populating lifecycle values" reach a
declaration whose value is READ OFF AN EXISTING RATIFIED DOCUMENT, or only one that would have to
be DECIDED? I have proceeded on the second reading. If it is the first, the remediation above is
one commit.
