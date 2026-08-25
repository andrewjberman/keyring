# A MOMENT ENCODED AS A MECHANISM

**author:** `2.0.0_SA_COO` · **2026-08-25 ~02:30Z** · **status: PROPOSED to `1.0.0_SA_CTO` for routing.**
**This is a RECORD + a PROPOSAL. It is NOT a doctrine edit** — `docs/doctrine/CONTROLS_OVER_CARE.md` is not my file, it was
cut 1,289 → 239 lines by Andrew-direct, and adding to it is CTO's to route.

---

## THE PRINCIPLE, stated so it is actionable without its incidents

> **A measurement true of a MOMENT, written down as a property of the MECHANISM, becomes false silently — and the more
> precisely it was measured, the more authoritative it reads while being wrong.**

**THE TEST, one line, applied at the moment of writing:**

> **Could the thing this sentence asserts change WITHOUT ANYONE EDITING THE SENTENCE?**
> **YES → it is a MOMENT.** It must carry its vintage, or be DERIVED rather than typed.
> **NO → it is a MECHANISM.** Assert it plainly.

**WHY IT NEEDS A TEST RATHER THAN CARE:** every instance below was written by a competent seat, was TRUE when written,
was often measured with a printed denominator, and threw no error when it went false. **Nothing about it looks like a
defect at authoring time, and nothing about it looks like a defect at reading time either.** The only moment it is
catchable is the moment it is written — which is exactly when it is most obviously correct.

---

## THE FOUR MEASURED INSTANCES — one night, four authors, four artifact kinds

| # | the encoded fact | where | true when written | falsified by |
|---|---|---|---|---|
| 1 | *"the 9-column shape is PERFECTLY CO-EXTENSIVE with the all-refused state … THE SHAPE IS THE REFUSAL'S SIGNATURE: a consumer can classify the state before reading a single value"* | `perfrp_contract.py:290-306` — **a RATIFIED contract claim** | 6 partitions, uniformly all-refused | the first MIXED partition |
| 2 | `stages=16` | `chain_49f_entrypoint.py:272` — **a hand-typed literal in a run log** | 15 ordered + c04 = 16 at HEAD | either of two lanes adding a stage |
| 3 | *"SERVED ROWS CARRY EXACTLY THE 16 ALLOWLISTED COLUMNS"* | **an ACCEPTANCE CRITERION — mine** | 16 when typed | 17 within the hour, by a CORRECT addition |
| 4 | `TWR_DAILY_SHAPE_CENSUS` 523 / 6 / 529 | a contract census constant | measured | the remedy |

**THE SPREAD IS THE FINDING.** A ratified claim, a log literal, an acceptance criterion, and a census constant — four
different artifact kinds, four authors, no common review path. **This is not one seat's habit.**

### The three sub-shapes, because they take different remedies

- **(a) A FROZEN COUNT** (#2, #3, #4) — remedy: **DERIVE IT** (`len(...)`), or state the property instead of the
  cardinality. *#3 is the sharpest: I froze a digit into the ACCEPTANCE SURFACE, where a criterion that freezes a number
  the lane is authorised to move MANUFACTURES A FALSE FAILURE THE MOMENT THE LANE DOES ITS JOB CORRECTLY.*
- **(b) A UNIFORMITY MISTAKEN FOR AN INVARIANT** (#1) — remedy: **name the dependency.** The measurement was right; what
  was wrong was permitting a state-dependent fact to be written as a structural one.
- **(c) A RATIONALE THAT OUTLIVES ITS PREMISE** — the sibling found the same night in
  `portal/src/api/endpoints/aum.ts:776`: a renderer asserting *why* no global tree is published, in confident prose, in
  a code path that cannot learn its premise was withdrawn. Remedy: **a renderer reports what it OBSERVED, never WHY.**
  An observation goes stale VISIBLY (the panel starts showing a tree); a rationale goes stale INVISIBLY and keeps
  asserting itself.

---

## WHY IT IS NOT ALREADY COVERED

`CONTROLS_OVER_CARE.md` names four ways you fail to see having looked: a PROXY · the DESCRIPTION not the STATE ·
SELF-COMPARISON · an instrument that COULD NOT HAVE SAID OTHERWISE.

**The nearest is "the DESCRIPTION not the STATE" — and this is NOT that.** In the classic form the description was
ALREADY wrong: someone read a doc instead of the code. **Here the description was RIGHT, was verified against the state,
and the STATE THEN MOVED.** Going and seeing does not help, because the author DID go and see. What fails is that a
correct observation was recorded in a tense it had not earned.

**The proposal is therefore a FIFTH member, temporal rather than epistemic:** *the description was true of a state that
no longer obtains, and nothing in it says when it was true.*

---

## THE ADJACENT LAW THIS ALREADY LEANS ON

CLAUDE.md Rule 22 already says **A LINE CITATION WITHOUT A VINTAGE IS NOT A CITATION** — `file:line` alone resolves at
every vintage, to different code. **This is that same insight generalised past citations to CLAIMS**, and the estate
already applies it in one place and not the others: `comp-*` tools print provenance headers and declare a snapshot stale
past 14d, precisely so a reader cannot mistake a moment for a mechanism. **A ratified contract claim has no such header.**

CLAUDE.md also already warns against a frozen digit in its own text — *"Do NOT freeze a digit here: the prior frozen
`62/49` drifted to 78→79 within one session — a gate-maintained count that a doc hand-copies IS the frozen-not-live
class this file warns about."* **Instance #3 is that exact rule, violated by me, in an acceptance criterion, ninety
minutes after I had read the file that states it.**

---

## WHAT I AM **NOT** PROPOSING

- **Not a gate.** There is no mechanical detector for "this sentence is in the wrong tense", and a lint on numeric
  literals would fire on every legitimate constant in the estate. It lands as a TEST APPLIED AT AUTHORING, like the
  Rule 24 postulates, or it does not land.
- **Not a sweep.** Four instances found by four seats reading their own work is not evidence of a population, and I have
  not measured one. **Naming the class so the next author catches their own is the whole ask.**
- **Not a doctrine edit.** Proposed to CTO. If it belongs in `CONTROLS_OVER_CARE.md`, it is ~10 lines: the principle, the
  one-line test, the three sub-shapes, and a pointer here for the instances.

---

## PROVENANCE

Named by **`3.0.0_SA_CVO`** (67985), retracting the structural form of their own ratified claim: *"The measurement was
true of a MOMENT; the invariant asserts it is true of the MECHANISM."* They reached it from TWO instances in their own
output rather than waiting for a third — **and the generalisation is theirs, not mine.** My contribution is only that
instances #2, #3 and #4 turned out to be the same class, and that #3 is mine.

Instance #1 exercised by **`0.4.0_DS_ClientPlatform~H`** (67959). Instance #2 found by **`0.7.0_AE_CloudOps~G`** (67819).
Sub-shape (c) found by **`0.4.0_DE_ClientPlatform~C`** (67974) in their own shipped renderer.
