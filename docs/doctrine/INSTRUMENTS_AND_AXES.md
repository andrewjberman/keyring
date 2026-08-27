# INSTRUMENTS AND AXES — a correct instrument pointed at the wrong thing returns a PASS byte-identical to a true one

**Sibling to [`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md).** That file says *care is not a
control*. **This file says something narrower and nastier: a control can be real, careful, and
correctly run — and still be aimed at the wrong axis, the wrong population, or the wrong basis.**

**Instances:** [`docs/references/INSTRUMENTS_AND_AXES_INSTANCES_20260722.md`](../references/INSTRUMENTS_AND_AXES_INSTANCES_20260722.md).
Every principle below cites the instance that earned it (`I-n`). Split from a combined 384-line file
2026-08-05 on Andrew-direct: governance docs carry principles and reference an id; incidents live in
the incident record.

---

> ## Before you trust a result, ask what it is OF: which axis, which population, which basis.
> **A rigorous instrument on the wrong axis survives review — that is precisely what makes it dangerous.**

---

## The principles

**1. CHECK THAT THE AXIS IS WELL-FORMED, NOT ONLY THE VALUES ON IT.** Every rule of the form *"check
X against the axis"* has a silent precondition: *the axis is the right kind of axis.* Check the
precondition once, explicitly, and record that you did. *(I-1: 21 of 429 points on closed-market
days, 20 real trading days omitted, unasked for ~429 days.)*

**2. COHERENCE IS NOT CORRECTNESS.** A coherence check relates quantities **to each other**, so it is
structurally blind to a transformation applied **uniformly to all of them** — a shift, a rebasing, a
wrong vintage. *(I-2: the composition identity held exactly, 7 of 7 dates, on a foreign-day roster.)*

**3. A DETECTOR'S FLOOR IS PART OF ITS OUTPUT — QUOTE IT, OR THE VERDICT IS UNREADABLE.** A negative
from a thresholded sweep is evidence about the instrument, not about the data. Where a threshold hid a
real defect once, the repaired clause is **threshold-free by design**, not re-tuned — and name the
residual limit of the repair. *(I-3: 0.87% under a 5% floor; an exact-revert tolerance rejecting a
drifting leg.)*

**4. WHEN AN INSTRUMENT DEGENERATES, REPORT THE DEGENERACY, NOT ITS OUTPUT.** A number produced by a
broken comparison is not a measurement. **Verdict `UNBOUNDED-BY-CONSTRUCTION` is worse than
"unmeasured"** — no amount of re-running that *class* of test will close it. **Then make the gap
actionable: name the test that WOULD reach it.** A declared gap with no route is a complaint; with a
route it is work. *(I-4: "407 of 407" was the instrument failing.)*

**5. HAVING JUST FIXED A CLASS OF ERROR IS NOT PROTECTION AGAINST COMMITTING IT AGAIN IMMEDIATELY.**
**Report a right answer reached by a bad route as an error anyway** — strike the evidence, keep the
ruling, re-ground on an independent axis. *(I-5: the same wrong-axis error three times in one session,
each caught by a different agent; the third had a correct conclusion on contaminated evidence.)*

**6. AN ABSENT PROCESS AND A QUIET PROCESS PRODUCE THE SAME OBSERVATION.** A feed that stops
converting is byte-indistinguishable from a feed with no new data. **Acceptance requires exercising
the path unattended, never observing that the artifact exists** — and a hand-staged artifact proves
the CODE works, never that the production path emits it. *(I-6: the human who was the automation.)*

**7. WHERE A RECORD LIVES IS PART OF WHETHER IT IS TRUE.** *"Knowingly chosen"* is a property of the
record's **reachability**, not of intent at signing time. Ranked carriers: **(a)** a gate that denies
the act — fires against any actor, reads nothing; **(b)** a commit-time gate — catches the repo path,
misses the console; **(c)** a registry row keyed on the artifact path — only fires for someone already
suspicious. **Prose that must be read is the weakest carrier, and the default path is the one where
nobody reads it.** *(I-7.)*

**8. NONSENSE GETS CHECKED; COINCIDENCE GETS BELIEVED.** A wrong reading that lands on a real
mechanism recruits the estate's own truths as corroboration. It is the *plausible* misreading, not the
absurd one, that survives review. **Operationally: `aws s3 ls` prints local time with no zone marker —
prefer `list-objects-v2` for any claim about *when*.** *(I-8: an mtime artifact pre-corroborated by a
genuinely existing `cron(0 2)`.)*

**9. STATE WHICH LEGS AN EVENT EXERCISES AND WHICH IT CANNOT, BEFORE BANKING IT AS EVIDENCE.**
"End-to-end" is a claim about a path, and a path is only as proven as its least-exercised segment. **A
green obtained for the wrong reason is the expensive kind.** *(I-9.)*

**10. BEFORE EDITING A SHARED OR VENDORED FILE, ASK WHO EMBEDS IT — AND ANSWER FROM THE MANIFESTS.**
The file cannot tell you. **An import added to a multi-package module is a multi-package deploy
decision wearing the costume of a one-line change.** Prefer a **structural** bound (lazy import inside
the one function that needs it) over a careful one. *(I-10: blast radius 4 → 1.)*

**11. FOUR TRUE SIGNALS CAN ALL ANSWER ONE LAYER BELOW THE CLAIM.** Verification Law #1 — *deployed
means downloaded AND imported* — with an anatomy. A size+sha match establishes the upload, not the
contents; a swapped `CodeSha256` establishes a file swap, not that it imports; a parity check
establishes copies match sources, not **closure over imports**. **A latent vendor gap is invisible
until somebody rebuilds, and the rebuilder inherits a break they did not write.** Fix the class, don't
blame the rebuilder. *(I-11.)*

**12. A TEST ASSERTING A PROHIBITION IS A RATCHET AGAINST ITS OWN RETRACTION.** A test is an
**enforcing copy with teeth**: it does not enforce the rule on the estate, it enforces the rule on
anyone trying to REMOVE it. The lift makes the suite red, the red reads as *"the lift broke
something,"* and the cheapest repair re-arms a retracted rule. Therefore: **a retraction sweep must
include TESTS in its denominator**; preserve the machinery in a FIXTURE rather than an assertion; add
the negative control the suite never had (a suite that can only assert *"the hold is on"* has no
expressible success state for it being off); and **fix the oracle first**. *(I-12.)*
**Generalize past holds: any test asserting a POLICY rather than a BEHAVIOUR is a vote against
changing that policy, cast by someone no longer in the room.**

**13. A COVERAGE FRACTION IS EVIDENCE ONLY IF ITS DENOMINATOR COMES FROM OUTSIDE THE INSTRUMENT'S OWN
CONFIGURATION.** A green derived from a hardcoded list is not evidence of coverage — it is evidence
that the list was iterated. **A guard cannot report missing a subject it was never told to look for**,
and `9/9` is a true statement about `PUBLISH_MAP`. Where subjects are enumerable, the denominator is
the **subject registry**, and the check is a **set-difference** against it. *(I-13.)*
- **13a. Tightening a permission does not catch a forgotten subject** — and an enumerated grant that
  blocks is a completeness signal you did not design and must not rely on. The wildcard grant is the
  better policy *and* removes the loud failure. *(I-13a.)*
- **13b. Triage this class by whether the defect MIS-STATES an outcome or CHANGES one.** A green
  report on a wrong number is expensive; **a guard that silently excludes a subject outranks every
  reporting instance in the same sweep** — the subject is not merely unreported, it is unprotected.
  *(I-13b.)*
- **13c. Read the commit, not the headline — especially your own source's headline.** *(I-13b: the
  reporting defect and the safety defect arrived in one commit; the ruling banked only the first.)*

**14. A FAILURE SIGNAL IS NOT A REASON, AND NEITHER IS A PASS.** Check **WHICH** failure — especially
when the failure is the one you wanted. A test asserting only *"something refused"* measures the
SUITE, not the gate it names: assert the discriminating outcome, then mutate each gate individually
and confirm **only** its own tests redden. And **name the scope a green covers, because an unstated
scope reads as "everything"** — unit-green plus unit-green is not seam-green. *(I-14.)*

**15. A SWEEP THAT PROVES A POPULATION SMALL IS AS VALUABLE AS ONE THAT PROVES IT LARGE, AND A
RETRACTION THAT SHRINKS A SCARE IS RARER THAN ONE THAT GROWS IT.** The value is in the denominator,
not the direction. *(I-14.)*

**16. A CONDITION STATED BEFORE THE WORK IS A SPEC; SPRUNG AT THE GATE IT IS A HOLD.** Publish
sign-off terms in advance.

**17. INDEPENDENCE IS WHAT AN INSTRUMENT PHYSICALLY READS, NOT WHAT IT IS CALLED.** Rule 22 already
says a second seat's confirmation *via the first seat's method* is REPETITION. **The sharper form is
about SUBSTRATE, and it does not need a second seat at all:** two differently-named instruments that
read the same store are ONE instrument, and they agree because they are the same measurement twice.
**Therefore a discrimination gate needs an ORACLE OUTSIDE THE PIPELINE THAT PRODUCED THE DATA.**
Where no such oracle exists, coverage is **UNMEASURED, not LOW** — and those are different claims of
which only one is true. *(I-15: one session, four grains — INSTRUMENT, PARSER, SUBSTRATE, PROPOSAL.)*
- **17a. The test is a PHYSICAL question, and it is cheap: what bytes does each arm read?** Two arms
  on one store fail it however different their code is. One arm on the filesystem and one on a graph
  pass it however similar. **Name the plane of each arm, not the name of each tool.**
- **17b. A SET DIFFERENCE BETWEEN TWO STORES IS NOT A POPULATION FACT** without recorded scan scope
  or matching vintages. "Present in A and not in B" and "B never swept it" are the same observation.
  This is the residual-bucket law on a set operation rather than an arithmetic one.
- **17c. AND THE ORACLE MUST SIT OUTSIDE THE PROPOSAL, NOT ONLY OUTSIDE THE PIPELINE.** A seat
  verifying its own sequencing proposal validated a shape it had built in memory — the post-change
  state — never the committed artifact, which was the only state the proposal put at risk. **A
  control on the wrong subject looks exactly like rigour:** it had two numbers, a firing negative
  control, and a stated conclusion.

**COST, stated because a verification rule that hides its cost only ratchets:** naming the plane of
each arm is one sentence per gate, and it is free when the arms differ. **The real cost lands where
NO outside oracle exists** — the honest output is then `UNMEASURED` with the missing discriminator
NAMED, which is less quotable than a percentage and is the whole point.

**NON-APPLICATION:** this governs DISCRIMINATION — telling absent from unaddressed, real from
artifact. It does NOT bind a plain reading of a single authoritative record: reading `owner` off the
manifest that defines ownership needs no second plane, because there is no second truth for it to
disagree with. **Demanding an outside oracle for a definitional read manufactures work and is the
failure mode of over-applying this rule.**

---

## THE CHECK — before recording a PASS, or citing one

1. **What is this OF?** Which axis, which population, which basis. Name it.
2. **Is the axis well-formed** — not just the values on it?
3. **Could this instrument have returned this answer if the defect were present?** If not it is
   decorative. **Mutant-prove it against the live defective artifact; RED, or it does not ship.**
4. **What is the denominator, and what is the detector's floor?** Quote both.
5. **Does my evidence come from the thing under suspicion?**
6. **A "works" claim — did I exercise the path, or observe that an artifact exists?**
7. **A debt — is the record where the actor will be standing when it fires?**
8. **Do my two arms read the same STORE?** If yes they are one instrument. Name the PLANE of
   each arm — and if there is no arm outside the producing pipeline, the answer is `UNMEASURED`, not
   a number.

---

*Split 2026-08-05 by `4.0.0_SA_CRO` (384 → this + the instance record). Original authored
`1.0.0_SA_CTO` from the 2026-07-22 MDPF_REVAMP count-axis incident, with instances contributed by
COO, DS, CVO and others. **Nothing was cut — the evidence moved and is linked.***


---

## Grounded evidence in agent memory

> Citations of the form `memory/<slug>` root at the **agent memory DIRECTORY**
> (`~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/`), **now under version
> control** (genesis `6843c2f`, 2026-08-05). Those records are the *grounded incidents* — typically
> 40–60 lines each with measured numbers; the law here is their compression. **Doctrine holds the
> law; memory holds the evidence.** Wired 2026-08-05 on Andrew-direct; the two corpora had **zero**
> links between them before that.

- `memory/feedback_profile_before_reporting_a_mechanism` — principle 5: a right answer reached by a bad route.
- `memory/feedback_shared_derivation_instruments_cannot_cross_check` — principle 14's seam, and §11's shared-sensor agreement.
- `memory/feedback_entity_truth_over_aggregate_snapshot` — principle 13, the denominator half.
- `memory/feedback_a_predicate_is_not_a_roster` — principle 13: a hardcoded list is not coverage.
