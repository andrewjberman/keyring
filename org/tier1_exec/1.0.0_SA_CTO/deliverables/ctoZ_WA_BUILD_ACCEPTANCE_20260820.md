# W-A BUILD — ACCEPTED AT THE GATE (build leg; apply is the laptop's)

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~21:45Z · **Build:** `0.5.0_AE_OpalETL~Z` @`81c502cff2`
**Verdict:** **BUILD LEG ACCEPTED.** Nothing is deployed by that commit; WA-1/2/3/8 land their DEPLOYED evidence at the apply.

---

## 1. WA-6 IS A FINDING, AND IT WAS FOUND THE WAY RULE 22a PRESCRIBES

The role **could not read** `opal-users-v2` — `implicitDeny`. Measured **on the live primitive before any
TF was written**, **one `--resource-arns` per call**, with the **positive control run as a SEPARATE
invocation** (same role, same action, `opal-tickets` → allowed).

**That is the full Rule-22a protocol executed correctly, including the part everyone skips:** the positive
control in isolation is what makes the deny *real* rather than an artifact of the instrument's three known
false-deny modes. **The role carried exactly one inline policy, scoped to the tickets table** — so the gap
was genuine, not a modelling artifact.

**The grant is resolved through a data source rather than a literal ARN, so a rename fails the plan loudly
rather than granting on a string that resolves to nothing.** Correct instinct: a silent grant on a dead
string is the failure that never announces itself.

## 2. TWO SELF-FOUND DEFECTS — and the second one is the better catch

**(a) The key shape was wrong.** The draft used `Key={"email": ...}`; the table is a single-table design
keyed `PK="USER#<email>"` / `SK="PROFILE"` (live `describe-table` + a bounded sample).

> **It would have raised `ValidationException` on EVERY claim — and the enrichment FAILS SOFT by design, so
> it would have been SWALLOWED SILENTLY and produced permanently blank claimer names that look exactly like
> "this user has no directory record."** The IAM gap and the key shape **would have failed the same
> invisible way**, which is why finding one did not guarantee finding the other.

**(b) The field I specified does not exist.** There is no `user_id` attribute on that table — the measured
set is `PK SK email name firstName lastName firmId tier role status` plus password/audit fields. **Named for
the gate rather than quietly resolved**, which is the behaviour I want.

## 3. ⛔ THE BEST ARTIFACT OF THE NIGHT — and it is a control, not a result

> **THE TEST STUB HAD ENCODED THE SAME WRONG ASSUMPTION AS THE CODE**, keying the fake directory on
> `"email"`. **The battery passed 22/22 while the real call could never have worked.**

**RULED AS DOCTRINE, because it generalises past this build:**

> **A FIXTURE BUILT FROM THE SAME ASSUMPTION AS THE CODE CANNOT TEST THAT ASSUMPTION.**

This is `CONTROLS_OVER_CARE`'s *instrument that could not have said otherwise*, arriving in the one place
teams least expect it — **the test suite itself**. And it **compounds with soft-fail**: a green battery over
a call that always throws, whose throw is swallowed and rendered to a human as *"no directory record."*
**Three layers each individually reasonable, composing into a permanent silent wrong answer.**

**The remedy is the right one and is what I am accepting on:** the stub was **rebuilt from the MEASURED
table**, then **the exact bug re-run as a mutant** — it now fails precisely the enrichment check with
`user_id None`, the silent-degradation signature. **That mutant is a better artifact than the green run**,
and it is the proof the hole is closed.

Two further controls, both accepted: the pre-W-A engine scores **6/22** (the 6 being regression checks that
*should* pass on both — a discriminating tally, not a coincidence), and obtaining that honest number
required **fixing a harness that CRASHED on a missing attribute instead of reporting it.** *A harness that
dies is not an instrument* — same defect class as TO6, inverted.

## 4. WA-9 — ALL FOUR DECIDED AT THE TABLE. RATIFIED.

**(a) GSI: NO INDEX IN W-A, obligation TRANSFERRED to W-C. RATIFIED, and the reasoning is better than
mine.** I had said *decide the index at the table touch*. Their counter is correct: **the requester-keyed
access pattern's correct key depends on W-C's query shape, which is unsettled — and a guessed index is a
second home for an unspecified pattern.** Building the wrong index now is worse than building none.
**THE TRANSFER IS THE LOAD-BEARING PART AND I HOLD THEM TO IT: W-C MUST PRINT ITS BOUND if it lists client
tickets by scan.** That is the client-facing-completeness hazard, preserved rather than dropped.

**(b) Caps: per-entry 2000 × per-ticket 50 ≈ 100KB. RATIFIED — including the detail that matters:** the
per-entry cap **matches the existing `resolution` cap rather than minting a new number.** Reusing a
ratified constant beats inventing a defensible one. **The S3 spill is UNNECESSARY, not deferred** — named
in the record and verifiably not built. Over-cap append **REFUSED 409**, and append-only is a **property of
the surface** (the only `client_updates` write anywhere is `list_append`), not a convention.

**(c) `_sod_block` needs NO new carve-out — it is already ACTION-scoped**, proven by the second half of the
test (the requester is still refused on *claim*). **Better than my ruling**: I reasoned a requester-class
MATRIX action would be needed; the existing scoping already delivers it, and they proved the negative half
rather than asserting it.

**(d) The grain landed exactly as ruled** — stored scalars current-cycle by definition, cross-cycle derives
from `events[]`, `reopened_at[]` served-but-derived, `reopened_count` stored.

## 5. THE `user_id` SCHEMA CALL — it was named for me, so I rule it

**It stays** — it is in Andrew's day-one field set, and narrowing his set is not mine to do. **It carries
the directory's ACTUAL primary key**, which is the right value: a real identifier from the real source
rather than a fabrication or a null.

**AND I RATIFY THE CAVEAT RATHER THAN BURYING IT:** today `PK` is a **deterministic function of email**, so
**`user_id` carries no information `email` does not already carry. It is not yet earning its place — and
that is acceptable**, because the day the directory's key stops being derivable from email is the day the
field becomes the only thing that survives, and storing it now is what makes that transition non-breaking.

⛔ **WHAT MUST NOT HAPPEN: nobody may treat `user_id` as a STABLE IDENTITY ACROSS AN EMAIL CHANGE.**
Whether the directory guarantees that is **UNMEASURED**, and the field's shape today (`USER#<email>`)
suggests it would *not* survive one. **Recorded so a future consumer does not infer stability from the
field's name** — the same defect class as `expired` reading actor-neutral.

## 6. SEQUENCING CONSTRAINT ON THE APPLY — ratified and load-bearing

> **WA-6's grant MUST be applied BEFORE the deployed enrichment exercise means anything, or it will read as
> "works, no names."**

**That is the soft-fail hazard reappearing at the acceptance layer**, and it is exactly the shape that would
have produced a false PASS on the apply leg: a green exercise whose greenness is manufactured by the very
gap it was meant to detect. **Apply order is part of the acceptance, not an implementation detail.**

### 6a. ⛔ CONDITION OF ACCEPTANCE — THE PRINT MUST DISCRIMINATE, and it subsumes the ordering discipline

`3.0.0_SA_CVO~Z` (3172) sharpened this and the sharpening changes what the remedy has to be.

> **THE DEGRADED STATE IS SEMANTICALLY VALID.** A ticket showing no claimer name is the **correct**
> rendering for a claimer who genuinely has no `opal-users-v2` record. So the failure does not merely lack
> an error — **it produces an outcome that a reader, a client, and a future auditor would all read as
> normal and correct.**

**Therefore "every degradation prints its reason" is NECESSARY AND NOT YET SUFFICIENT.** If the print
collapses to one message — *"no name available"* — then **ABSENT-FROM-DIRECTORY** (legitimate, expected,
permanent) and **LOOKUP-FAILED** (IAM deny, wrong key shape, transport error) emit **the same line**, and
the record still cannot separate them. **True to the letter and false to the purpose: a control that fires
identically on the healthy and the broken case discriminates nothing.**

**CONDITION, stated as a property — the mechanism is `0.5.0_AE_OpalETL~Z`'s:** the print separates at least

- **"the lookup ran and the directory has no such row"** — *a fact about the world; needs no follow-up*, from
- **"the lookup did not complete"** — *a defect; names which way it failed and needs follow-up.*

⚠ **AND HERE IS WHY THIS IS THE STRONGER REMEDY: THE SEQUENCING HAZARD AND THE PRINT REQUIREMENT ARE THE
SAME DEFECT FROM TWO ENDS.** *"Works, no names"* **is** the indistinguishable state.

```
print DISCRIMINATES  -> a mis-sequenced exercise ANNOUNCES ITSELF instead of passing green
print COLLAPSES      -> the exercise passes, and the grant's absence is invisible
                        IN THE ONE TEST WRITTEN TO CATCH IT
```

**So the discriminating print does not merely satisfy §6 — it DISCHARGES it**, converting an ordering
discipline that a human must remember under apply-time pressure into a property that holds whether or not
they do. **That is the third time tonight a seat has turned one of my prose constraints into a control**
(after the inverted WF-4 mutant and the self-reverting landing script), and it is the pattern I most want
continued.

> ⛔ **THE RELATION IS ONE-WAY. IT IS NOT "FIX EITHER AND BOTH CLOSE."** `3.0.0_SA_CVO~Z` (3192) tested
> both directions and they are not symmetric:
>
> | Fix | Acceptance evidence | Operational blindness |
> |---|---|---|
> | **PRINT** discriminates, sequencing unfixed | **CLOSED** — the mis-sequenced exercise announces itself | **CLOSED** — every future lookup failure stays separable from a legitimate blank |
> | **SEQUENCING** fixed, print collapsed | **CLOSED** — grant applies first, the test passes correctly | ⛔ **UNTOUCHED, FOREVER** — a failed lookup and a genuinely absent user emit the same blank in live serving from then on |
>
> **The sequencing remedy is ACCEPTANCE-SCOPED AND ONE-SHOT. WA-10 / §6a is a PROPERTY OF THE SYSTEM.**
> "Fix either and both close" is true **inside the acceptance-evidence frame** — which is where
> `2.0.0_SA_COO~Z` stated it, fairly — **and false one sentence outside it.**
>
> **THE FAILURE MODE IS SPECIFIC: someone at the apply reads "fix either", takes the cheaper one, and the
> cheaper one is RE-ORDERING TWO STEPS.** ⛔ **WA-10 / §6a IS NOT DISCHARGEABLE BY POINTING AT THE
> SEQUENCING.** It is discharged only by the print itself discriminating.
>
> *Provenance corrected: **"unfalsifiable" is `2.0.0_SA_COO~Z`'s** (msg 3181). I credited it to
> `3.0.0_SA_CVO~Z` in a broadcast body while my own subject line said whose it was — and they declined it
> for the right reason: **an absorbed credit detaches an idea from the person who can qualify it**, which
> is exactly what would have happened here, since the qualification came from a third seat.*

*`3.0.0_SA_CVO~Z` has not read the enrichment code and does not claim it collapses the two. **If the build
already separates them, this condition costs nothing and is discharged by saying so.***

**Open at the apply (laptop's leg):** TF plan/apply, the deploy-completion ledger opened and closed, the
tag, and the DEPLOYED exercise of WA-1/2/3/8 — **WA-6's grant applied first**, and **§6a confirmed**.
