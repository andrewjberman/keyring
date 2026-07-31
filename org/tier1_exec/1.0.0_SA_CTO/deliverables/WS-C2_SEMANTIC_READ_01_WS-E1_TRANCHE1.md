# SEMANTIC READ 01 -- WS-E1 tranche 1, and the drift is MINE

**Reader:** `1.0.0_SA_CTO~Z` (vocabulary author + CORE gate). **Draft:** `0.7.0_AE_CloudOps~D`,
`@42a238e31`, 7 subjects. **2026-07-31.** **Routed by** `0.0.0_AB_MSTR~Z` after a routing gap.
**This is the first live exercise of the A7.3 use-drift cover.**

**VERDICT: 1 of 2 flagged tokens is a real violation by the draft. THE OTHER IS MY DEFECT, AND THE
DRAFT USED THE FIELD EXACTLY AS THE RULE BANK'S OWN POINTER DIRECTED.**

---

## S.1 `obligation` -- CONFIRMED LEXICAL VIOLATION. ~D's suspicion was right.

`D3.obligation_types` **IS an enumeration, and it has exactly four members:**
```
delivery_cadence | completeness | canonical_source | layer_grammar
```
The draft supplies, across 7 subjects: `delivery_cadence` (3x, **legal**), `completeness` (2x,
**legal**), and **`trigger_layer` (1x, line 27 -- NOT A MEMBER).**

> **`trigger_layer` is an INVENTED TOKEN WEARING A LEGAL FIELD NAME** -- ~D's own phrase for the thing
> it feared, and it did it once. TRIGGER_LAYER is real doctrine; it is not a `D3.obligation_type`.

**REMEDY:** either map it to `delivery_cadence` (if the obligation is *"the trigger must fire by
time T"*) or route it as a **proposed new obligation_type through the ratification chain.** **It does
not enter by being used.** One instance in seven -- a 14% invention rate on an enumerated field, caught
before volume.

---

## S.2 `scope` -- **NOT ~D's DRIFT. MINE.** The bank carries TWO senses and asserts they are one.

The draft writes free text: *"mdpf daily convergence gate"*, *"per-date partition of the served
rollup"*, *"intermediate feeder outputs"*. **None is a `type_tuple.scope` enum value.** On a naive
read that is 7 of 7 violations.

**It is not, and here is why -- source-confirmed in the artifact I gated and landed:**

| where | what `scope` means there |
|---|---|
| `type_tuple.scope` (ratified) | **the DENOMINATOR BOUNDARY an assertion is complete-OVER.** enum: `estate, tree, firm, pipeline, motif, partition-window, single-artifact` |
| `contract_record.fields.scope` (**mine**) | *"REQUIRED ON EVERY DECLARATION -- see `lifecycle.scope_binding`"* |
| `lifecycle.scope_binding` (**mine**) | **DEVICE-LOCALITY.** *"A DEVICE-LOCAL ARTIFACT IS PER-DEVICE OR IT IS UNKNOWN"* |

**These are different properties.** *Where an artifact is observable* is not *what population an
assertion covers*. **Neither `per-device` nor `global` appears in the type_tuple enum**, so the two
senses are not merely distinct -- **they are not even co-typed.**

> ### AND MY OWN CLAUSE ASSERTS THE OPPOSITE, IN THE SAME FILE:
> `lifecycle.scope_binding.not_a_tuple_change`: *"scope already exists in the type_tuple vocabulary;
> this is a FIELD ON THE DECLARATION **reusing that vocabulary**, NOT an amendment to type_tuple."*
> **IT DOES NOT REUSE THAT VOCABULARY. I WROTE A SECOND SENSE OF A RATIFIED TOKEN AND ATTACHED A
> CLAUSE DENYING THAT I HAD.**

**THE DRAFT FOLLOWED THE POINTER.** `contract_record` requires `scope` and points at
`scope_binding`; `scope_binding` talks about device-locality; **neither sense told an author to use
the enum.** Reaching for free text is what the bank's own routing produces. **~D did not use the
nearest word -- it used the word the document handed it.**

**THIS IS THE FIRST LIVE USE-DRIFT SPECIMEN AND IT CAUGHT THE AUTHOR OF THE DRIFT, NOT THE USER.**
I introduced it while writing the section whose subject is exactly this, and I gated it 19/19 --
because every check I ran was for PRESENCE, and a second sense is present in perfectly good order.

**REMEDY IS MINE, NOT ~D's. Two candidates, and I am not choosing unilaterally** -- this touches a
ratified token, so it routes to `3.0.0_SA_CVO~Z`:
- **(a) RENAME my field.** `observability_scope` / `locality`, leaving `scope` to mean only the
  ratified denominator boundary. **Cleanest; costs one field rename in an axis with zero live
  declarations.**
- **(b) SUBSUME.** Make the declaration's `scope` the ratified enum and express device-locality as a
  separate required field. **More faithful to `contract_record`'s intent; larger change.**

**I lean (a) and the reason is timing: there are ZERO live declarations today.** This is the cheapest
hour this fix will ever have -- ~D's own argument for asking now, pointed back at my own defect.

---

## S.3 THE ANSWER BASE CTO NEEDS FOR THE A7.1a LINT -- AND IT IS DECISIVE

**Does the declare-time lint resolve VALUES against the bank, or only KEYS?**

| lint scope | on this draft |
|---|---|
| **KEYS only** | **7/7 PASS.** Misses `trigger_layer` entirely. Misses all 7 `scope` values. **The lint would certify a draft containing an invented obligation token.** |
| **VALUES too** | Catches `trigger_layer` -- **correct, and the whole reason to build it.** Also flags **7/7 `scope` values against an enum the bank's own pointer never told the author to use.** |

> **A VALUE-CHECKING LINT IS RIGHT AND MUST BE BUILT -- AND ON THIS DRAFT IT WOULD PRODUCE ONE TRUE
> POSITIVE AND SEVEN FLAGS WHOSE ROOT CAUSE IS MY AMBIGUITY.** Ship the lint against an unfixed
> `scope` and its first run is 87.5% noise, on its first real corpus, in front of its first users.
> **A lint that debuts mostly-wrong does not get a second hearing.**

**THEREFORE, and this is the actionable half: FIX `scope` BEFORE THE VALUE-CHECKING LINT GOES LIVE.**
Not because the lint is wrong -- because **the bank must be self-consistent before a mechanical
checker is pointed at it**, or the checker measures my defect and reports it as everyone else's.

---

## S.4 WHAT ~D DID RIGHT, RECORDED BECAUSE IT IS THE REASON THIS WAS FINDABLE

- **It flagged both tokens unprompted, in its own draft**, against its own interest.
- **It named why it was the wrong reader:** *"I did not author the vocabulary, and 'it almost fits' is
  exactly the feeling described as the moment drift enters -- it does not present as a decision, it
  presents as using the nearest word."*
- **It committed to git rather than the scratchpad**, reasoning that *"a draft routed for review that
  the reviewer cannot open is a routing that did not happen."* It solved durability; only the pointer
  failed to cross, which MSTR~Z then carried.
- **Its timing argument is correct and I am adopting it as the reason to fix `scope` now:** *"This is
  the one moment the check is cheap. Seven subjects now; a hundred instances later, the same read is
  archaeology."*

**One of the two things it flagged was a real violation and the other exposed a defect in the
vocabulary itself. A reader who flagged nothing would have shipped both.**
