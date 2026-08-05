# ASSERTION LAWS — the checklist and the taxonomy

> **FILENAME IS LEGACY, DELIBERATELY.** This file is `MECHANISM_LAWS.md` because **20 files point at
> that path** (vs 10 at the merged-in `VERIFICATION_LAW.md`, now a pointer). The *title* is the
> subject; the *path* is an address.

**Merged 2026-08-05 by `4.0.0_SA_CRO`, Andrew-direct** (*"also merge mechanism and verification
laws"*). Two documents over substantially one subject, each stating a boundary against the other, were
the one-directional-pointer trap in slow motion.

> ## ⚠ BOTH ID SPACES ARE PRESERVED AND MUST STAY STABLE.
> **`VL#1`…`VL#14`** (the checklist) and **`M1`…`M14`** (the taxonomy) are **PUBLIC INTERFACES.**
> *"Verification Law #6"* is cited **by number, 25 times across 9 distinct numbers**, by files that
> never name this path. **Renumbering either space breaks citations that no rename-sweep can find.**
> Add with the next free id; never re-order, never re-use.

**Instances, provenance, and the denominator caveat:**
[`docs/references/ASSERTION_LAWS_INSTANCES_AND_PROVENANCE.md`](../references/ASSERTION_LAWS_INSTANCES_AND_PROVENANCE.md).

---

## The boundary — this file is one of three families

> **THIS FILE** holds **WHAT TO RUN** (Part A) and **WHERE AN ASSERTION SITS** (Part B).
> **[`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md)** holds **HOW YOU FAIL TO SEE THE THING** — the
> root and the four ways looking does not produce seeing, including how an instrument lies. **The
> M-taxonomy does not type instrument fallibility, by construction**, so neither file contains the
> other.
> **[`INTENT_DENOMINATOR_SYNCHRONIZATION.md`](INTENT_DENOMINATOR_SYNCHRONIZATION.md)** holds the
> **DENOMINATOR ontology** — soundness (`D ⊇ I`, `P ⊨ Q`), route classification, sensor/oracle.
> **A THIRD FAMILY HAS NO HOME: HOW A RULE OR ROLE FAILS TO BE ONE** — a rule naming the EVENT instead
> of the PROPERTY; a procedure step naming no actor; a role first exercised by a non-owner.
> Measured-absent with positive controls, and named rather than quietly omitted.
> **AND ONE OF THOSE UNHOMED LAWS IS AN INSTANCE OF ITSELF:** *a step that names no actor is not a
> step* — and that law has no owner and no home.
>
> **Cite the CLAIM, never a section number.** A prose cross-reference is a dependency with no gate.

---

# PART A — THE CHECKLIST (`VL#`): what to run before you believe a result

**`VL#1` — DEPLOYED means downloaded AND imported.** A green test suite describes a **file**; a deploy
is about a **runtime**. Verify the artifact was fetched *and* loaded by the thing that runs it.

**`VL#2` — An injected column is a HYPOTHESIS.** Adding a column to prove a theory produces a value
shaped like evidence. It stays a hypothesis until something independent of the injection confirms it.

**`VL#3` — A false premise gets answered ON, and returns as corroboration.** Ask a question containing
a wrong assumption and you get a confident answer built on it. **Ask for the ARTIFACT, not the number.**

**`VL#4` — A guard nothing invokes is not a guard.** Existence is not enforcement. Find the call site
or treat the guard as absent.

**`VL#5` — An instrument that cannot fail is not an instrument.** If no input would make it report a
problem, it reports nothing about the world. Compounding: **there is no channel for "I don't know," so
not-knowing renders as confidence.**

**`VL#6` — Enumerate what a number is *OF* before explaining why it differs.** **A rigorous instrument
pointed at the wrong axis SURVIVES REVIEW**, because the rigor is real and the axis is unexamined.

**`VL#7` — "Well grounded" is not "FRESHLY grounded."** Grounding has a timestamp. A claim that *was*
verified is not a claim that *is* verified.

**`VL#8` — A stale record says something false WITH AUTHORITY.** **A retracted prohibition is only as
dead as its last surviving copy.** Retraction must propagate to every enforcing copy — including
**tests**, which are enforcing copies with teeth.

**`VL#9` — Care is not a control.** Care is what you have *instead* of one. **Knowing a failure mode by
name does not immunise you against writing it** — several instruments have been broken by the agent who
landed the rule against them that same hour.

**`VL#10` — State the coverage DENOMINATOR, and run the positive control SEPARATELY.** A hand-chosen
control measures **the author**; a generated one measures **the instrument**. A sweep that cannot find
a known-present instance is a broken instrument reporting silence. **A control batched with the target
can be corrupted by the target's presence.**

**`VL#11` — Host is UTC-4: no `Z` is ambiguous, and a HAND-TYPED `Z` is worse.** **Ambiguity *prompts*
the check; forgery *cancels* it.** Use computed-offset forms (`--date=iso-strict`), never a typed unit
or zone. **A zero from a time-windowed query needs a positive control.**

**`VL#12` — Control the RETRIEVAL, not the pattern.** A retrieval failure **returns a value**: `grep`
enters binary mode and truncates while exiting 0; `grep -c` counts zero matches in an error message;
`git show HEAD:<untracked>` returns a `fatal:` string a comparator will happily diff. **A wrong number
is more dangerous than a zero — a zero invites suspicion, a plausible count does not.** And **print the
PREDICATE, not just the denominator.**

**`VL#13` — Score controls on OUTPUT, never on rc.** Harness exit codes have been corrupted before, and
the fix is not reboot-durable.

**`VL#14` — Metadata about a record is not the record.** A summary field *about* a set of records is a
different object from the records, with its own — usually weaker — consistency guarantee. **Eventually-
consistent surfaces read stale exactly when you are debugging a live fire. Query the events.**
**Corollary:** *a probe aimed at one question will not volunteer the answer to a question you did not
ask, even when the data is on the screen.* **Enumerate what your output contains, not only what you
went looking for.**

> ## THE THROUGH-LINE
> **Most of these are one shape: an instrument produced a clean result and the cleanliness was
> MANUFACTURED BY THE FAILURE** — the orphan watcher that reads REACHABLE *because* it ate the mail,
> the PATH probe at 100% *because* the breakage was total and single-caused, the grep that exits 0
> *because* it stopped reading.
> ### THE CLEANER THE PASS, THE HARDER YOU SHOULD LOOK AT WHAT PRODUCED IT.

*(The count of members in that shape is deliberately not stated. It was written as "nine of the
thirteen" beside a list of fourteen — a hand-maintained digit beside a growing enumeration, which is
`M1`/`M4` committed by this file. The fix for a frozen count is never a fresher count.)*

---

# PART B — THE TAXONOMY (`M`): where an assertion sits

**Fourteen mechanisms, each with the question that exposes it and the gate or test that absorbs it.**
Ordered by assignment count. **⚠ The `n` values are counts of ASSIGNMENTS on an unstable base — see the
denominator caveat in the reference before quoting any of them. The ORDERING is durable; the digits are
not.** Every gate-or-test cell is populated; where no gate is possible the reason is stated.

**`M6` — AXIS / GRAIN MISMATCH** *(largest)*
**LAW:** An instrument sampled an axis the defect does not live on. The measurement is clean and
answers a different question than the one asked.
**EXPOSING QUESTION:** *State the grain of every input and of the conclusion.*
**GATE:** `type_tuple` grain/rail/scope declaration, enforced by comp-manifest-check's stage-2 vocab
invariant. **PARTIAL — it types TOOL declarations, not ad-hoc agent claims.**

**`M1` — SHARED DENOMINATOR**
**LAW:** The expectation was derived from the measured thing. Both sides trace to one authority, so the
gap reads zero by construction.
**EXPOSING QUESTION:** *Where did the EXPECTED side come from, and is that the same authority that
defines the population?* — and its sharper form: ***whose count would have to be wrong for mine to be
right?***
**GATE:** intent from ABOVE, denominator from BELOW, gap printed every run
([`INTENT_DENOMINATOR_SYNCHRONIZATION.md`](INTENT_DENOMINATOR_SYNCHRONIZATION.md) §13).
**COROLLARY (`L-2`): a self-chosen denominator cannot refute the instrument that chose it.**

**`M2` — SHAPE-MATCH, WRONG CONTENT**
**LAW:** Retrieval broke and returned the right TYPE. An error message counted as content; an empty
result read as a true zero.
**EXPOSING QUESTION:** *Could this have returned non-zero? Run the positive control.*
**GATE:** the positive control + `VL#12`. **A named practice, not an automated gate.**

**`M5` — SCALAR COLLAPSE**
**LAW:** A count, an rc, or a boolean summarised the population away. The number survived; the
population it was computed over did not.
**EXPOSING QUESTION:** *What population did it pass OVER, and can it name what fell outside?*
**GATE:** printed-denominator convention + the boundary-report registration invariant.

**`M14` — PROSE-AS-CONTROL**
**LAW:** The finding's only carrier is text nobody is required to read. Nothing halts on it.
**EXPOSING QUESTION:** *Can this fail? What stops on it?* — and ***if this check FAILED right now,
would anything stop?***
**GATE:** [`TRIGGER_LAYER.md`](TRIGGER_LAYER.md) — a finding lands as a GATE or an OWNED BLOCKING ITEM.
**NO AUTOMATED GATE POSSIBLE in general:** detecting that a document is un-read requires knowing who
was obliged to read it, which no instrument holds.
**COROLLARY (`L-11`): a check that cannot block what it measures is not a gate, it is a comment.** If
the measurement and the action share a command block, the measurement has no path to stop the action.
*Counter-instrument: the check runs as a **separate, blocking step** whose exit status the action
depends on.*

**`M8` — TEXT vs SEMANTICS**
**LAW:** A mention scored as a use. The string was present; the value was never read.
**EXPOSING QUESTION:** *Does it READ the value, or merely contain the string?*
**GATE:** AST-based checks over text matching. **PARTIAL and known-blind** — the tracer misses
derived-object and resource-style two-hop calls, **so its silence is not absence.**

**`M7` — SELF-REPORT AS POINTER**
**LAW:** The subject of the measurement chose its own target. The instrument measured what it was
handed.
**EXPOSING QUESTION:** *Did I establish the input from the CALLER's side?*
**GATE:** CLAUDE.md NEVER-rule — never trust a producer's self-report or `rc=0`; verify against the
SERVED artifact. Realised as the RAVC evidence requirement.

**`M11` — TAUTOLOGY**
**LAW:** Both sides of a check are the same computation. The check cannot fail.
**EXPOSING QUESTION:** *What would have to happen for these two sides to disagree?*
**GATE:** the MUTANT — mutate the subject and require the control to redden. **No automated
enforcement; a control never mutated has never been tested.**
**COROLLARY (`L-5`): convergence is not corroboration when the converging arguments share an unmeasured
premise.** N arguments agreeing is evidence only if their premises are independent. **And agreement
between two instruments that share a SENSOR is one measurement counted twice.**

**`M9` — DESIRED vs APPLIED**
**LAW:** A configuration read was used for a behavioural claim. Declared and landed were treated as the
same fact.
**EXPOSING QUESTION:** *Did I exercise the path that fails if the claim is false?*
**GATE:** CLAUDE.md Rule 22a — STATE/IAM cites both the DESIRED view and the live primitive; BEHAVIOUR
EXERCISES the path. GO withheld by the cert owner if absent.

**`M3` — PROXY FOR THE THING**
**LAW:** A hash, key, partition or name stood in for content. The proxy moved independently of the
thing it named.
**EXPOSING QUESTION:** *What is this a function of that I have not keyed on?*
**GATE:** grain declaration at the governed grouping key, not a name prefix. **PARTIAL.**

**`M10` — UNREACHED BRANCH**
**LAW:** The exercise never entered the governed domain. The test passed without touching the thing the
claim is about.
**EXPOSING QUESTION:** *Did my input actually reach the branch the claim is about?*
**GATE:** a fixture carrying the NON-DEFAULT value + a mutant proving the branch can redden. **NO
AUTOMATED GATE:** coverage tooling reports line entry, not whether the input was discriminating.

**`M4` — COPY DRIFT**
**LAW:** A restated literal diverged from its source. Both copies read as authoritative.
**EXPOSING QUESTION:** *Is this a copy or a read? Enumerate the copies.*
**GATE:** the MIRROR CONTROL — a reader asserts its own field list against the schema it depends on.
**Covers ONE reader; there is no general copy-enumeration gate.**

**`M12` — BORROWED SENSITIVITY**
**LAW:** It works only while a person keeps doing something. The control's discrimination is supplied
by a human habit, not by the mechanism.
**EXPOSING QUESTION:** *What has to keep happening, by a person, for this to keep working?*
**GATE: NONE POSSIBLE — by construction.** The dependency is on human behaviour outside the system; an
instrument cannot detect that its own sensitivity is on loan. The only counters are the exposing
question at design time and a `revalidate_by` decay that forces re-confirmation on a clock.

**`M13` — POLARITY / NAMING INVERSION**
**LAW:** The label asserts the opposite of the behaviour. The name reads as safety while its presence
does harm.
**EXPOSING QUESTION:** *Does the name describe what its PRESENCE DOES?*
**GATE:** token-collision refusal at ratification — a token already occupied on another axis may not be
reused. **Covers ratified vocabulary only.**

---

## How the two parts relate

They overlap **by design**: a checklist law often names a taxonomy shape. **A taxonomy tells you what
happened; a checklist tells you what to run.**

| If you are… | Use |
|---|---|
| about to believe a result | **Part A** — run the checklist |
| explaining why a result was wrong | **Part B** — name the mechanism |
| building a gate | **Part B**'s GATE-OR-TEST column |
| asked *"could this be wrong?"* | **Part A**, then the four ways in `CONTROLS_OVER_CARE.md` |

Rough correspondences, offered as navigation and **not** as a mapping to compute over — the two axes
were derived independently and are not MECE against each other: `VL#5`↔`M11` · `VL#6`↔`M6` ·
`VL#10`↔`M1` · `VL#12`↔`M2`/`M5` · `VL#4`↔`M14` · `VL#1`↔`M9`.

*Merged 2026-08-05 by `4.0.0_SA_CRO` (305 + 156 → this + the instance record). Original authors:
`0.8.0_AE_CloudComp~C` (taxonomy, NFRA_VELOCITY WS-C8) and the `MEMORY.md` verification-law corpus.
**Nothing cut — the evidence, the provenance and the denominator caveat moved and are linked.***
