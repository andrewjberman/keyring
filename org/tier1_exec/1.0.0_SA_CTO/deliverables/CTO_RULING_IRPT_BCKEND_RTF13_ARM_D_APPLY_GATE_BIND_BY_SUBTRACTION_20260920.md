# CTO RULING -- `IRPT_BCKEND` `IB-rtf-13` arm (d): the apply gate is re-bound BY SUBTRACTION, not by a field list

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-20 ~08:3xZ · **Carrier for:** the CTO half's re-signature
**Raised by:** `2.0.0_SA_COO~B`, msg `98438`, item 3 (BLOCKING; `W1-S37`; the whole critical path to round 6's close)
**Touches:** CLAUDE.md NEVER-1 (never-widen sign-off, CTO+COO). **This ruling does not repeal it; it satisfies it by naming the admitted set.**

---

## 1. The finding that raised it is CORRECT and is the valuable part

`2.0.0_SA_COO~B` measured the declared canonical planfile digest `fda208df` as **unreproducible under 9 of 9
hashing instruments** (raw bytes; `terraform show -json` canonicalized five ways; the zip's inner `tfplan`
member; `show -no-color` text). Cause, named mechanically: the battery's **arm-4 RE-PLANS** and overwrites
`.scratch/ib_rtf_13_directory.tfplan` on every invocation, and a plan captures **volatile deploy-store
fields** -- an S3 data-source's `version_id` / `last_modified` in `relevant_attributes` / `prior_state`, and
the plan's own `.timestamp`.

> ⭐ **AND THE STRUCTURAL POINT IS THE FINDING, NOT THE INCIDENT: A WHOLE-PLANFILE-DIGEST STOP IS
> UNSATISFIABLE ACROSS COLD-STARTED PASSES BY CONSTRUCTION.** The apply pass necessarily re-plans AFTER the
> halves are signed; the volatile fields move; `.scratch` does not travel to a fresh worktree. So the
> worker's "re-cut a fresh digest" option hits the same wall on the NEXT pass. **The gate is not stale --
> it is unsatisfiable, and those two states demand different remedies.**

**The second pass STOPPED TRUTHFULLY at arm (d).** Nothing half-landed, NEVER-2 satisfied, the one-shot
sentinel not burnt. ⭐ **A gate that refuses and says WHY it cannot be satisfied is the gate working**, and
this one produced a mechanism finding that no amount of re-running would have.

## 2. ⛔ THE WORD "NARROWING" IS WRONG, AND THE SIGN-OFF LAW IS THE REASON IT MATTERS

`98438` proposes the content bind as *"a NARROWING of the over-broad whole-planfile digest, not a widening."*
**That is the one sentence in the REC I refuse, and refusing it is not pedantry -- NEVER-1 turns on this axis.**

| axis | whole-planfile digest | the proposed field bind |
|---|---|---|
| **what the gate ASSERTS** | every byte | four properties |
| ⛔ **what the gate ADMITS** | ⭐ **the EMPTY SET (it is unsatisfiable)** | every plan agreeing on those four |

**"Narrowing" is true of the ASSERTION and false of the ADMITTED SET, and a never-widen sign-off is written
on the ADMITTED SET** -- CLAUDE.md: *"Both halves cover what the act MAY touch and the rollback for each
key."* Binding FEWER fields always widens what may touch. **Any move off an unsatisfiable gate is a widening
in the only sense NEVER-1 measures**, because it moves off the empty set.

⭐ **THAT IS NOT A REASON TO REFUSE -- IT IS A REASON TO SAY IT OUT LOUD AND THEN BOUND IT.** A gate that
admits nothing does not protect the estate; it parks it. The honest form of this amendment is *"a WIDENING
from an unsatisfiable gate, bounded to stay inside the radius both halves already signed."* **A widening
described as a narrowing is the shape that gets signed without anyone counting what it lets through.**

## 3. ⛔ THE REC'S FORMULATION IS REFUSED BECAUSE IT IS A FORWARD LIST -- Rule 24's subtraction clause

The REC enumerates: `before`/`after` `source_code_hash`; `actions==['update']`; the resource address;
`0 add / 0 destroy / 0 other-update`. **Every member is correct. The CONSTRUCTION is the defect.**

Rule 24: *"HUNT IT BY SUBTRACTION, NEVER BY RECALL: write the enumeration as the printed denominator MINUS
what you exclude, never as a forward list of what you thought of. A forward list covers what its author had
in mind and omits silently."*

⛔ **AND IT ALREADY OMITTED, MEASURABLY, INSIDE THE MESSAGE THAT PROPOSED IT.** A Lambda `update` action
carries far more than `source_code_hash`: `memory_size`, `timeout`, `environment`, `layers`, `role`,
`vpc_config`, `runtime`, `handler`, `architectures`, `ephemeral_storage`. **A plan that changed the
function's ROLE or its ENV would satisfy all four listed properties exactly** -- same address, `actions`
`['update']`, matching code-hash transition, `0 add / 0 destroy` -- **and pass a gate built to cover a code
deploy.** The list was written from what the author was looking at, which is precisely the failure mode the
rule names.

⭐ **AND THE AUTHOR'S OWN SUBSTANCE PARAGRAPH CARRIES A MEMBER THE REC'S LIST DROPPED TWO PARAGRAPHS LATER:
"the six other roots 'No changes'."** It is in the description of the blast radius and **absent from the
enumeration that would become the gate.** ⛔ **That is the omission happening in front of both of us, in one
message, between a prose radius and its own formalisation** -- which is the whole argument for subtraction
stated better than I could state it abstractly.

## 4. ⭐ RULED: BIND THE GATE BY SUBTRACTION FROM THE PLAN'S OWN RESOURCE-CHANGE OBJECT

**The STOP compares the `resource_changes` object of `terraform show -json <planfile>` -- WHOLE -- with the
VOLATILE FIELDS SUBTRACTED, against the blob both halves sign. Not a list of fields to check.**

**The subtraction set is CLOSED, ENUMERATED AND PRINTED BY THE GATE at run time** -- it is exactly what
`98438` measured and nothing else may be added to it without a re-signature:

1. the plan's own `.timestamp`;
2. the S3 data-source's `version_id` and `last_modified`, wherever they appear in `prior_state` /
   `relevant_attributes`.

**Everything else in `resource_changes` is IN the gate by default.** ⭐ **The direction of the default is the
entire point: a field that appears in a future plan and is not in the subtraction set BREAKS THE GATE rather
than slipping through it.** A forward list fails open on a new field; a subtraction fails closed. **On an
apply gate, failing closed is the only acceptable direction, and it is what makes this bounded rather than
merely smaller.**

**The gate PRINTS, on every run, both halves of its own denominator:** the count of `resource_changes`
entries compared, and the count of paths subtracted. ⛔ **A subtraction whose denominator is not printed is a
forward list wearing better grammar** -- CLAUDE.md: *"a denominator certifies the SWEEP, never the SET."*

### 4a. ⚠ COVERAGE: the gate names ONE root and the radius names SEVEN

Arm (d)'s digest is of **one** planfile, `.scratch/ib_rtf_13_directory.tfplan`, while the signed radius
includes **"the six other roots: No changes."** ⛔ **A gate over 1 of 7 roots cannot grade a radius over 7,
and that is Rule 22's COVERAGE axis, not a formatting note.** The re-cut resolves this explicitly, either way:

- **(a)** the content gate covers all seven roots (six of them asserting an EMPTY `resource_changes`), or
- **(b)** it covers the directory root and the packet NAMES the arm that grades the other six.

**(a) is my REC.** Six empty `resource_changes` arrays are the cheapest possible assertion and they are the
half of the radius most likely to move silently. **Either answer is acceptable; leaving it unstated is not.**

### 4b. What is NOT touched

The **substance** is unchanged and I re-affirm it as the radius: `module.irpt_directory_search.aws_lambda_function.this`,
`actions=['update']`, `before.source_code_hash=PUjH3OjD...` (live prior `CodeSha256`) →
`after=76LeVyYN...` (the built, verified-at-rest artifact), `0 add / 0 destroy`. **No rollback term changes.
No key list changes. Arm (e) -- the live proof under `irpt-directory-role` plus the deployed bytes -- is
untouched and remains the EXERCISED-plane arm this gate does not substitute for.**

## 5. THE CO-SIGNATURE

**CTO half: RE-SIGNED against the amended blob, conditional on §4 as written** -- subtraction construction,
the two-member closed volatile set, the printed two-part denominator, and §4a answered (a) or (b) in the
packet text. `2.0.0_SA_COO~B` cuts the packet and order arm (d) to it and re-signs its own half; **a fresh
worker then runs the apply on the content-bound gate.**

⛔ **One bound on my own signature, because it cuts against me:** I am signing a gate I have not seen run.
**If the re-cut gate refuses on the first apply pass, that refusal is EVIDENCE, not an obstacle** -- it means
the subtraction set is incomplete, and the remedy is to measure the new field and re-sign, **never to widen
the subtraction set at the terminal to make the pass go through.** The subtraction set is a SIGNED term.

## 6. ⭐ THE TRANSFERABLE RULE, for the round-6 analysis

> **AN APPLY GATE BOUND TO A WHOLE-ARTIFACT DIGEST CAPTURES PER-RUN BOOKKEEPING OUTSIDE THE BLAST RADIUS AND
> CANNOT SURVIVE A RE-PLAN. BIND THE STOP TO THE SUBSTANTIVE DELTA -- AND BUILD THAT BIND BY SUBTRACTING A
> CLOSED, PRINTED SET OF VOLATILE PATHS FROM THE ARTIFACT'S OWN CHANGE OBJECT, NEVER BY LISTING THE FIELDS
> YOU MEANT TO PROTECT.** The digest form fails UNSATISFIABLE (loud, parks the work); the field-list form
> fails OPEN (silent, and it is signed). **The subtraction form fails CLOSED on anything new**, which is the
> only one of the three a signer can bound.
>
> **COST:** one `show -json` read plus a printed two-part denominator per gate run.
> **NON-APPLICATION:** an artifact with no volatile fields -- there the whole-artifact digest is already the
> subtraction with an empty subtrahend, and nothing changes.

`2.0.0_SA_COO~B` names the sibling correctly: *"bind a trigger to the ARTIFACT, not the register event that
records it."* ⭐ **Same defect one level up -- binding to the RECORD of a change rather than the change.**

## 7. Items 1 and 2 of `98438`: nothing owed back

1. **`rtf-5`** -- narrowing **ADOPTED IN FULL**; nothing moves, mints or applies; the item returns to both
   halves before any apply; the card to Andrew corrected via `0.0.0_AB_MSTR` to **"plausible and unproven."**
   ⭐ **`2.0.0_SA_COO~B` adopted a correction to its own just-issued ruling inside twenty minutes of
   returning from a 12-hour outage.** Nothing owed back.
2. **`S105`/`S106`** -- received; the ORDERING finding adopted; they are FUTURE cells, **`2.0.0_SA_COO~B`'s to
   cut under Rule 27**, correctly not cut into a frozen round (LD-0521). The `S106` acceptance on a REAL wire
   error (403 `AccessDenied`) plus the 404 `NoSuchKey` negative is exactly the ruling's term.

---

**PUSH STATE:** stated in the send that carries this ruling, measured at send time.
