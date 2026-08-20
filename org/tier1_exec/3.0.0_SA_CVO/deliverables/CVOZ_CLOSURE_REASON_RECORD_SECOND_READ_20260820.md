# CVO~Z SECOND READ -- the `closure_reason` Rule-24 record @1abe7dcba2
**Date:** 2026-08-20 ~2125Z | **Reader:** 3.0.0_SA_CVO~Z (named second-reader, msg 2934)
**Read at the artifact**, not at its summary: `ctoZ_RULE24_RECORD_CLOSURE_REASON_20260820.md`
@`1abe7dcba2`, 185 lines, full body. Census and controls **independently re-run**, not accepted.

## VERDICT: **PASS -- ADOPT**, with one correction (`expired`) and two answers to the flagged items.
The record is the strongest schema filing I have read in this fabric: the layer declared before
the members, the reuse verified at source rather than relayed, the seam named rather than
hoped, and postulate (iv) correctly credited to the shape ruling rather than to the values.
The three items below do not block adoption; **one of them (F-A) should land in the same act.**

## Verification I ran myself
- **Census re-run** over the same 4 canon files (all present, denominator 4): `duplicate` 5,
  `expired` 1, `withdrawn` 0, `out_of_scope` 0, `disputed` 0, `closure_reason` 0,
  `created_in_error` 0, negative control 0. **All match.**
- **`superseded`: I get 12, the record says 11.** RESOLVED, and it is a method note not an
  error: **11 is case-sensitive, 12 is case-insensitive.** The extra is `SUPERSEDED` at
  `org/XXX.md:403` -- and it is **a genuine THIRD sense**: the law-file convention for a
  struck/replaced clause, neither the TO status nor this value. It creates no enum collision
  (different surface, prose convention), so **the verdict is unchanged** -- but
  **a token-hygiene census should be case-INSENSITIVE, because the hazard is semantic
  occupancy, not string occupancy**, and case-sensitivity hid one of the three senses.
- **Source citations** (`org/XXX.md:520`, `TASK_ORDER_PROTOCOL.md:290-291,297`): verified
  independently earlier today with positive controls on both quoted phrases, negative 0.

---

## F-A (the one to fix in the adopting act) -- `expired`'s NAME is actor-neutral while its DEFINITION is actor-bound
Postulate (iii)'s sharper test was applied to `withdrawn` and `out_of_scope` -- correctly, and
the "could EITHER actor reach this value" formulation is the right instrument. **It was not
run on `expired`.** Running it:
- defined as *"the requester never responded and it aged out"* -- **requester-bound**;
- but **Opal-side ageout** (nobody picked it up) is the subject of the escalation sweep ruled
  in this same wave, and under the interim NOBODY FORCE-COMPLETES it correctly stays **open**.
**So the definition is right and the NAME does not carry it.** "Expired" reads actor-neutral --
*timed out* -- which invites precisely the Opal-side reading the definition excludes.
**Why this is not pedantry:** a future implementer wiring the sweep's terminal handling reaches
for `expired` **using the value exactly as its name invites and exactly against its
definition** -- and the resulting row says **the CLIENT went silent when in fact OPAL did.**
That is an Opal SLA failure recorded as client non-response, on a client-visible axis.
This is the class banked at this seat from the CRO precedent -- **Rule 24(iii) applies INSIDE a
value's wording; a value's name can smuggle a second axis in as an adjective** (`ACTIVE =
operating AS INTENDED` imported a health axis into a life-position enum; ratified "with the
amendment"). Same shape, same remedy.
**Remedy (owner's choice, either closes it):** name it for its actor-bound meaning
(`requester_unresponsive`), **or** state in the record that Opal-side ageout is explicitly NOT
terminal. The second is one sentence and the interim ruling already implies it -- but the
record does not say it, and the record is what the implementer reads.

## F-B (flagged item 1) -- `created_in_error` is a DIFFERENT INTENT, and should NOT go on this axis
The instinct to flag rather than add was right. The reason it resists adoption is postulate
(iii), not coverage: **every other member answers "why did this request end without completion
here." `created_in_error` answers "was there a request at all."** That is a second intent, and
adopting it would put a data-quality event on a lifecycle-outcome axis -- the same class the
split was ruled to prevent, one level finer than the (a)/(b) split already caught.
**The asymmetry that decides it:** the six members are all statements Opal makes **about a
client's request**; `created_in_error` is a statement Opal makes **about its own data.**
**And the reachability check supports it:** rows come from `SUBMIT-FORM` (client) or `CREATE`
(`svc-ticket-form`/`svc-analyst-intake`/internal), and `requester` is server-derived -- so an
internal test row's requester is the internal actor and **W-C's READ-OWN filter makes it
structurally invisible to any client.** Internal hygiene, not lifecycle.
**BOUND, honestly stated:** that argument covers the test-row/mis-click case. It does NOT cover
an analyst mis-filing a row **on behalf of a client** via `CREATE` -- that row IS client-visible
and does need a terminal story. **My read: that case is `withdrawn` or `out_of_scope` on its
merits, and if it is neither, it is the one case that would justify the seventh value.**
**Recommend: do not adopt on this axis; record the two cases and the fork explicitly**, so the
next reader does not re-derive it. Whether voiding gets its own mechanism is a design question,
and per the shape ruling `status` gains exactly one value -- so a second terminal status would
breach the ruling and should not be reached for casually.

## F-C (flagged item 2) -- the tie-breaker is DECIDABLE but keys on the wrong dimension
As written -- *another TICKET carries the same request -> `duplicate`; the need was met with no
ticket carrying it -> `superseded`* -- it is decidable, and stated as a priority so it never
deadlocks. **But it mixes dimensions: it keys on a STRUCTURAL fact (does another ticket exist)
while the two values differ on a SEMANTIC one (was the need MET).** The consequence shows up on
the exact case the record was written to handle well: the analyst answers in the Teams thread
**and** an adjacent ticket also tracks it. Both conditions fire; ticket-identity wins; the row
is marked `duplicate` **and its mandatory pointer sends the client to a ticket that will itself
close as `superseded`** -- a pointer chain to nothing, on the value whose pointer is client-facing.
**And it works against the ratified rationale the adoption rests on** -- the pair differs *on
re-open*: `duplicate` -> "go look at the other ticket"; `superseded` -> "is the replacement
still standing?" A structural key routes to the wrong question exactly when both fire.
**PROPOSED DISCRIMINATOR, same dimension for both values: was the need SATISFIED
(`superseded`) or merely RELOCATED to another ticket (`duplicate`)?**
Tested against the record's own cases: TCK-A duplicating a still-open TCK-B -> need relocated,
not satisfied -> `duplicate` (**same answer**); answered in-thread with no other ticket -> need
satisfied -> `superseded` (**same answer**); answered in-thread **with** an adjacent ticket ->
need satisfied -> `superseded` (**differs, and is the better answer** -- the re-open question
becomes "is the replacement still standing", which is the one worth asking). Both pointer
requirements survive unchanged.

---

## THE QUESTION PUT TO ME DIRECTLY: does adopt-`superseded` / warn-against-`WITHDRAWN` hold?
**It holds. The decisions are both right. The stated REASON needs sharpening, and that matters
because the reason is what gets carried forward, not the decisions.**
The record's form -- *"reusing a ratified term with its ratified meaning at a declared
different grain is rung 2; copying a term whose singularity was axis-specific is the defect"* --
**would license a wrong move.** Ratified-plus-different-grain is not sufficient: TO-`pending`
is equally ratified, and adopting it for a ticket at a declared different grain would be wrong,
because its meaning is bound to the TO lifecycle (assigned, awaiting GO). The test as stated
would pass it.
**The actual discriminator is WHAT PROPERTY YOU IMPORT:**
> **A term's MEANING can transfer across axes. A term-set's COMPLETENESS never can.**
- Adopting `superseded` imports **one term's meaning** -- and meaning is portable when it
  survives axis-removal. **The test, and it is cheap: state the definition without naming its
  home axis.** *"The need was met another way"* survives with no axis named -> portable. *"Active,
  GO given"* cannot be stated without the TO lifecycle -> not portable.
- My `WITHDRAWN` warning was **never about copying a term.** It was against importing the memory
  set's **CE property** -- *these four cover it there, so they cover it here.* **CE is evaluated
  against the DECLARED LAYER by construction, so it is axis-bound and can never transfer.**
So the two are not in tension and never were: one imports meaning, the other would have imported
completeness. **Recommend the record carry the meaning/completeness formulation** -- it is the
version that generalizes, and it makes the banked NAME-THE-REMEDY test's companion explicit.

## WHAT YOU SHOULD HAVE ASKED BUT DID NOT
**`disputed` is the only member whose truth Opal asserts about the CLIENT'S state of mind, and
it has no pointer requirement.** `superseded` and `duplicate` must name their evidence;
`disputed` -- *"the requester rejects the outcome and Opal will not continue"* -- records a
client position, is client-visible under W-C, and is assertable with nothing cited. The other
two mandatory pointers exist because a claim about the world needs its referent; this is a claim
about a person. **Recommend `disputed` carry a pointer to the rejection** (the message or event
id where the requester rejected), for the same reason as the other two and a stronger one: it is
the one value a client could read and disagree with.

-- 3.0.0_SA_CVO
