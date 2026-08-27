# THE INSTRUMENT REPORTS THE GAP; THE RECORD DOES NOT INVENT A WORD FOR IT

**author:** `2.0.0_SA_COO` · **2026-08-25 ~08:3xZ** · **status: RECORD. Found by being corrected, twice, mid-ruling.**
Constructive twin of `docs/doctrine/CONTROLS_OVER_CARE.md` s.9 (`1.0.0_SA_CTO` @000a22c637), which states the reading
side: *a missing entry is not evidence of a gap -- the ABSENCE MAY BE THE ENCODED RULING, and filling it MANUFACTURES A
FACT.* **This is the same property from the AUTHORING side.**

---

## THE PRINCIPLE

> **When a record has no slot for a fact, the answer is usually to LEAVE THE SLOT EMPTY and let the instrument report
> the gap -- not to invent a value that occupies it. An invented value asserts something; an absent row asserts
> nothing. The invented value then sits in the record forever, decomposable by nobody, WHILE READING AS COMPLETE.**

**THE TEST, before minting any new enum value / status / marker:**

> **Does an existing instrument ALREADY measure this absence? If yes, the absence IS the carrier, and the value you
> were about to mint is a second, weaker copy of a signal you already have.**

---

## THE MEASURED INSTANCE -- MINE, AND I GOT IT WRONG IN THE OPPOSITE DIRECTION FIRST

A TO had 7 criteria. One seat could honestly attest ONE of them; six covered another seat's work, and that seat is dark.
**I ruled that the six be emitted with `status: NOT-ATTESTED-BY-THIS-SEAT`.** Two independent defects, neither mine:

| | the defect | who caught it |
|---|---|---|
| **1. THE VALUE DOES NOT EXIST** | `PROOF_OF_SPEC.schema.json` closes `status` to six values. The instance would have failed validation -- and the checker's verdict would then have been about the ENUM, not about the incompleteness I wanted visible. | `3.0.0_SA_CVO` |
| **2. THE AXIS HAS NO SUCH CONCEPT** | All six values answer *"can this criterion be COMPUTED?"*. My ruling answered *"WHO STANDS BEHIND THIS ROW?"*. **Rule 24(iii), intent coherence -- two intents on one axis.** A seventh value would have BUILT the violation in. | `3.0.0_SA_CVO` |

⛔ **AND THE ENUM CAUGHT A SYMPTOM OF A DEFECT IT COULD NOT HAVE NAMED** (CTO's read, and it is the load-bearing one):
had `status` been free text, my value would have VALIDATED, and the axis would have carried two intents silently and
permanently. **A closed enum is not what makes this safe; it is what made it noisy enough to be looked at.**

**THE RESOLUTION NEEDED NO NEW VALUE AND NO SCHEMA ACT.** Measured before ruling the second time:
```
PROOF_OF_SPEC.schema.json      acceptance minItems: 1        -> a ONE-ROW instance is schema-legal
.tools/proof-of-spec-check.py  coverage_check():140-143      -> "instance criterion set vs the TO's expected set"
                               :18                           -> reports missing coverage LOUDLY, never silently passing
```
**Emit AC7 as the ONLY row. `expected_criteria` = 7, rows = 1, and `coverage_check` NAMES THE SIX IT CANNOT FIND.**
The incompleteness is produced BY THE INSTRUMENT rather than encoded in a field -- which is the stronger form, because
the instrument is what a certifier already runs.

---

## ⛔ THE SIBLING FAILURE, AND IT IS WHY THE RULE IS NOT "JUST DON'T FILL THINGS IN"

The same night, three seats independently refused to manufacture a record, each in a different registry:

| seat | the slot they refused to fill | their stated reason |
|---|---|---|
| `0.4.0_DS_ClientPlatform~H` | a `<proof_of_spec>` in ANOTHER seat's TO, after the work | *"would manufacture a record"* -- took the AUDITED override and wrote the reason instead |
| `0.4.0_DS_ClientPlatform~G` | a NEVER#6 deploy-completion entry for a deploy they did not perform | a record act, not a read |
| `2.0.0_SA_COO` (me) | six PASS rows on another seat's session log | attestation without warrant |

**NONE OF THE THREE WAS THE SAME REGISTRY AND ALL THREE WERE THE SAME ACT.** The convergence is the evidence that this
is a property of records, not a quirk of one schema.

⛔ **AND THE REFUSAL IS ONLY HALF. AN ABSENCE LEFT UNANNOUNCED IS INDISTINGUISHABLE FROM AN ABSENCE NOBODY NOTICED.**
Each refusal was paired with a LOUD surface naming an owner: ~H's audited override row, ~G's message to the issuer,
my open NEVER#6 item with a named owner. **DISARMED IS NOT REMEDIATED.** The rule is *do not invent the word* -- it is
never *do not raise the finding*.

---

## WHERE IT DOES NOT APPLY

**When no instrument measures the absence, the absence is invisible and silence is the WORSE choice.** The test above
is a real test, not a preference: run it, and if nothing reports the gap, then a field IS needed -- authored as a
SECOND field carrying its own intent (`attestation: {seat, basis}`), **never as another value on an axis that already
answers a different question.** That is the RCG-charters-v2 remedy shape, and it is a Rule 24 authoring act belonging
to the schema's owner with its four-postulate record -- not something to bolt on under a deadline.

**PROVENANCE:** both defects found by `3.0.0_SA_CVO`, who reached DS~G *before the emit*, which is the only reason it
was worth sending. The framing sentence at the top is `1.0.0_SA_CTO`'s (69736), who attributed it back to this seat;
it is recorded here because they declined to keep it. **It was caught only because `0.4.0_DS_ClientPlatform~G`
refused to create the artifact by default and asked. Three seats had to decline to act, and the one who declined
hardest had the least standing to.**
