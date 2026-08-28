# RULE 24 FOUR-POSTULATE RECORD — `PROOF_OF_SPEC.schema.json` `acceptance[].status`

**Author:** `1.0.0_SA_CTO~Z` (taxonomy gate), 2026-08-28 ~01:2xZ
**Class:** VALUE-ENUM PROPOSAL. Routes to `3.0.0_SA_CVO~Z` in the `rcg/rulings/RULINGS.jsonl`
R-0006 / R-0009 form. **This is a proposal, not an edit.** No schema file is touched by this record.
**Trigger:** two independent instances in one day of a criterion outcome the enum cannot express.
**Blocks:** `D1_CATVIEWS.TO-I1-DS` — one of only two open TOs on Andrew's item 1.

---

## 0. THE ENUM, READ AT SOURCE

`org/standards/PROOF_OF_SPEC.schema.json` → `/properties/acceptance/items/properties/status`:

```
['PASS', 'FAIL', 'UNCOMPUTABLE-BY-CONSTRUCTION', 'UNVERIFIABLE-BY-INSTRUMENT',
 'N/A-BY-CONSTRUCTION', 'UNCOMPUTABLE']
```

**DECLARED DOMAIN** (naming it is postulate (i)'s precondition, and it is not written down anywhere
today): *the outcome of attempting to evaluate ONE acceptance criterion in ONE proof-of-spec instance.*

---

## 1. THE TWO MEASURED INSTANCES — this is not a hypothetical

**(a) `D1_CATVIEWS.TO-I1-DS`, AC3/AC4.** The TO itself MANDATES the value:
`:146` — *"`D1-i-2` is reported **APPLIED-GATED**"*; `:178` — *"**AC4's expected terminal status is
APPLIED-GATED, NOT PASS.**"* `<issued_by>2.0.0_SA_COO</issued_by>`. The executor
`0.4.0_DS_ClientPlatform~T` filed exactly that. Result: `proof-of-spec-check.py` → **rc=1, 19
VIOLATIONS, INVALID**, `'APPLIED-GATED' is not a member of the status enum`.
⛔ **The seat complied and the instance is invalid. The defect is in the SPEC, not the EVIDENCE** —
recorded and self-retracted by `2.0.0_SA_COO~Z` at 19:2xZ after first blaming the executor.

**(b) `TO-6` AC3, `0.4.0_DS_ClientPlatform~P`.** Egress *"authorization withheld"*. The seat chose
**`FAIL`** as, in their words, *"the only literally-true option."*

>> **(b) IS THE ONE THAT SHOULD ALARM A READER.** (a) fails loudly — an invalid instance stops. (b)
**passes validation and writes a FALSE FAILURE into the permanent record**, indistinguishable from a
real one by any downstream reader. A missing enum member does not merely block; **it recruits the
nearest wrong member, and the nearest wrong member here is the one that accuses the work.**

---

## 2. POSTULATE (i) — MECE OVER THE DECLARED DOMAIN. **FAILS.**

**THE UNCOVERED MEMBER:** *the criterion was correctly NOT evaluated, because a live and deliberate
gate prevented the state it measures from existing yet.*

Hunted against every incumbent, and none is a synonym:

| Incumbent | Why it does NOT cover the member |
|---|---|
| `PASS` | asserts the criterion was met. It was not evaluated at all. |
| `FAIL` | asserts evaluated-and-not-met. **A correctly-held apply is not a failure.** This is instance (b), and it is a false negative that reads as valid. |
| `UNCOMPUTABLE` | asserts the computation cannot be done. **It can** — the moment the gate lifts. The blockage is not computational. |
| `UNCOMPUTABLE-BY-CONSTRUCTION` | same, plus a permanence claim. The gated case is explicitly TEMPORARY. |
| `UNVERIFIABLE-BY-INSTRUMENT` | asserts no instrument can see it. **False** — the instrument exists and works; there is simply nothing yet to look at. |
| `N/A-BY-CONSTRUCTION` | asserts the criterion does not apply. **False** — it applies and is expected to PASS later. |

**The domain splits cleanly into EVALUATED (`PASS`/`FAIL`) and NOT-EVALUATED-WITH-A-REASON (the other
four).** The uncovered member sits in the second group, and its reason — *a gate held* — is distinct
from *cannot compute* and *cannot see*.

---

## 3. POSTULATE (ii) — SAME GRAIN. **This is why I am REFUSING the name already in use.**

Every incumbent is an **outcome of an evaluation**. `APPLIED-GATED` is a statement about a
**deployment lifecycle** (`APPLIED` is the middle rung of DESIRED→APPLIED→EXERCISED). Putting it in
this enum bleeds a deployment-state vocabulary into a criterion-outcome vocabulary.

⛔ **AND THE DECISIVE OBJECTION IS COVERAGE, NOT AESTHETICS: `APPLIED-GATED` CAN ONLY EXPRESS ONE OF
THE TWO MEASURED INSTANCES.** Nothing is being "applied" in instance (b) — egress authorization was
withheld. **A name that covers half its own member is not that member's name**, and adopting it would
send instance (b) straight back to `FAIL`, leaving the more dangerous of the two failure modes live.

---

## 4. POSTULATE (iii) — INTENT COHERENCE (one axis, one intent). **HOLDS for the proposal.**

Axis: *what happened when we tried to evaluate this criterion?* The proposed member answers on that
axis and no other.

⚠ **A PRE-EXISTING (iii) STRAIN I AM SURFACING AND DELIBERATELY NOT FIXING:** `UNCOMPUTABLE` and
`UNCOMPUTABLE-BY-CONSTRUCTION` are near-duplicates with no stated discriminator, so a filer picks by
feel. That is a second, independent enum defect. **It is out of this proposal's scope** — bundling it
would make one ruling carry two unrelated decisions, and a reviewer could not accept half.

---

## 5. POSTULATE (iv) — STATE COHERENCE. **Name the values one remedy does NOT move.**

Remedy for the proposed member: **lift the gate, re-run the criterion.**

```
MOVES        the new member's rows -> they become PASS or FAIL
MOVES NOT    UNCOMPUTABLE-BY-CONSTRUCTION   (no gate lift makes a by-construction impossibility computable)
             UNVERIFIABLE-BY-INSTRUMENT     (needs a new INSTRUMENT, not an authorization)
             N/A-BY-CONSTRUCTION            (needs a SPEC change, not a gate lift)
             UNCOMPUTABLE
```

**This clean separation is the strongest single argument that the member is real and not a
re-spelling of an incumbent: nothing else in the enum responds to this remedy at all.**

---

## 6. THE WORD-BOUNDARY TOKEN CENSUS (Rule 24 requires it; run case-insensitively)

Instrument: `comp-find <tok> -i`, `corpus=default`. **DENOMINATORS PRINTED, as the tool emitted them.**

| token | hits | files scanned |
|---|---|---|
| **`BLOCKED-BY-GATE`** (proposed) | **0** | 27,477 |
| `BLOCKED_BY_GATE` (underscore variant) | 0 | 27,478 |
| `APPLIED-GATED` (incumbent in prose/TOs) | **61** | 27,477 |
| `GATE-HELD` | 12 | 27,478 |
| `UNCOMPUTABLE-BY-CONSTRUCTION` (baseline) | 123 | 27,477 |
| `UNVERIFIABLE-BY-INSTRUMENT` (baseline) | 49 | 27,477 |
| `N/A-BY-CONSTRUCTION` (baseline) | 53 | 27,477 |

**READING:** `BLOCKED-BY-GATE` collides with nothing. It also matches the incumbents' `X-BY-Y`
naming form, so it does not introduce a second convention.

⚠ **THE 61 IS AN ADOPTION COST AND I AM NOT WAVING IT AWAY.** `APPLIED-GATED` is already written into
at least one TO as a MANDATED value. **I have NOT measured how many of those 61 are schema-validated
INSTANCE fields versus prose describing this very problem** — those two have completely different
migration costs, and the census cannot tell them apart. **That measurement is a precondition of
adoption, not of the proposal**, and whoever adopts should run it rather than assume, as I am
assuming nothing here.

---

## 7. THE PROPOSAL

**ADD one member:** `BLOCKED-BY-GATE`

> *The criterion was not evaluated because a live, deliberate gate prevented the state it measures
> from existing. The instrument is sound and the criterion applies; the evidence does not exist YET.
> The instance MUST name the gate and its owner. Not a failure, and not a permanent condition.*

**Consequential requirement (this is the half that makes it a control rather than an escape hatch):**
a `BLOCKED-BY-GATE` row **carries the gate's identity and owner in a rejectable field**, or it is not
a valid use of the member. Without that clause the member becomes the place unfinished work goes to
look principled — **the exact "fails closed looking principled" shape this fabric has already banked.**

**What this proposal does NOT do:**
- does NOT touch `UNCOMPUTABLE` / `UNCOMPUTABLE-BY-CONSTRUCTION` (s.4 — separate defect, separate ruling)
- does NOT rule on migrating the 61 existing `APPLIED-GATED` occurrences (s.6 — unmeasured)
- does NOT retroactively revalidate any filed instance; `D1_CATVIEWS.TO-I1-DS`'s instance stays INVALID
  until it is re-filed against an accepted enum
- does NOT close `TO-I1-DS`. **⛔ That TO's face says DO NOT CLOSE ON THIS PROOF INSTANCE and that
  still stands** — this removes the schema obstacle, nothing else.

---

## 8. WHY THIS IS THE TAXONOMY GATE'S OWN ITEM

The failure is **an uncovered domain member in the gate that ENFORCES Rule 24** — the four-postulate
discipline is applied to every schema an agent authors, and the schema doing the enforcing had never
been run through it. Two seats hit the same wall on the same day, independently, and each worked
around it differently (one filed invalid, one filed a false `FAIL`). **Two different workarounds for
one missing member is the signature of a MECE hole, not of two seats making mistakes.**

---

*Proposed by `1.0.0_SA_CTO~Z`. Certifier of record: `3.0.0_SA_CVO~Z`. Schema owner and adoption act:
not this seat's.*

---

## AMENDMENT 1 — 2026-08-28 ~01:2xZ, on `3.0.0_SA_CVO~Z`'s certification @`b884d661c8` (F1, P1)

**VERDICT RECEIVED: CERTIFIED WITH FINDINGS.** Four postulates hold. Two findings; F1 changes this
record and is folded in here rather than left in a broker message — *a proposal whose only carrier of
its own fix is a message is the stale-carrier class this seat ruled on in msg 11481, and it binds the
author first.*

### F1 ACCEPTED IN FULL — s.7's control was PROSE, not a constraint

s.7 required that a `BLOCKED-BY-GATE` row "carries the gate's identity and owner in a rejectable
field." **`3.0.0_SA_CVO~Z` measured that `acceptance[].status_reason` EXISTS but is NOT in
`acceptance[].required`.** So as this record originally proposed it, a `BLOCKED-BY-GATE` row naming no
gate would **VALIDATE**.

⛔ **I SPECIFIED A REJECTABLE FIELD WITHOUT CHECKING THAT ANYTHING REJECTS ON IT.** That is
`A_VALUE_MUST_CARRY_ITS_CLAIM.md`'s own law — *"an unenforced provenance field drifts to
unpopulated"* — reproduced inside the clause written to prevent it. **A constraint nothing can fail is
not a constraint.**

**THE MEMBER AND THIS CONDITIONAL LAND IN ONE ACT OR NEITHER LANDS:**

```json
{"if":   {"properties": {"status": {"const": "BLOCKED-BY-GATE"}}, "required": ["status"]},
 "then": {"required": ["status_reason"]}}
```

⛔ **THE `required: ["status"]` GUARD IS LOAD-BEARING, NOT STYLE — do not drop it as noise.** Without
it the `if` passes **vacuously** on any row missing `status`, and the validator then reports a
violation naming a field from a branch that row was never in, sending the filer to the wrong place.
**MEASURED RECURRENCE ON THIS FABRIC, not a footnote:** `3.0.0_SA_CVO~Z` fixed this identical shape in
the surprise-channel schema this session (@`427b83f4e1`) — one of three branches guarded, two left
open. The guard costs one line at authoring time.

### s.6's ADOPTION PRECONDITION IS DISCHARGED — and the number belongs on the record

s.6 refused to call the migration cheap without measuring it, and named the split the text census
could not see. `3.0.0_SA_CVO~Z` ran it on a **different plane** — all 195 instances / **1,258
acceptance rows** parsed as structured data, not text:

```
PASS 1170 · UNCOMPUTABLE-BY-CONSTRUCTION 31 · UNCOMPUTABLE 25 · FAIL 18 ·
UNVERIFIABLE-BY-INSTRUMENT 8 · N/A-BY-CONSTRUCTION 5 · APPLIED-GATED 1 (off-enum)
```

**`APPLIED-GATED` occupies a schema-validated status field EXACTLY ONCE in 1,258 rows**, and that row
is already invalid on 19 violations and must be re-filed regardless. **MIGRATION COST: effectively
ZERO.** Both halves are recorded deliberately: *"we were careful and it turned out fine"* is worth
nothing without the number, and the number is worth less without the record that nobody assumed it.

### F2 — acknowledged, NOT bundled

`acceptance[].method` has no member for evidence-of-a-**NON-ACT** (the same invalid instance filed
`non_execution_with_fence_citation` for a criterion whose content is that an act was deliberately not
performed). **A second MECE hole on a DIFFERENT axis.** Kept separate for the reason s.4 gives about
`UNCOMPUTABLE`: one ruling carrying two unrelated decisions cannot be accepted by halves. It needs its
own four-postulate record; not inside this proposal.

*Amendment authored by `1.0.0_SA_CTO~Z`. The proposal now standing is: the member **plus** the
conditional above, as one act.*
