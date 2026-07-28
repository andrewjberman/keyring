# CONTROLS OVER CARE — verification doctrine

**These are binding principles, not history.** Each one was paid for. The incidents that earned them —
the measured numbers, the falsified mechanisms, who caught what — are preserved verbatim in
[`docs/references/INCIDENTS_2026-07-13.md`](../references/INCIDENTS_2026-07-13.md).

**The rule that points here:** CLAUDE.md Rule 22 / 22a.

> ## THE CAPSTONE
> In ONE night, **eleven instruments lied**, across six agents, including the CTO's. **Every one was caught
> by a control failing. NOT ONE was caught by being careful** — and several were written by the agent who
> had, that same hour, landed the rule against them.
>
> # **CARE IS NOT A CONTROL. CARE IS WHAT YOU HAVE INSTEAD OF ONE.**
>
> **KNOWING A FAILURE MODE BY NAME DOES NOT IMMUNIZE YOU AGAINST WRITING IT.** The doctrine below protects
> nobody. **The exercise does.** Run the positive control. Run the mutant. Look at what actually came back.

---

## 0. Before you model a system, READ WHAT IT IS ALREADY TELLING YOU

> # **SIX MECHANISMS. SEVEN AGENTS. ELEVEN HOURS. ZERO CORRECT.**
> # **AND THE ANSWER WAS IN A LOG FILE THE WHOLE TIME.**

The INF gold chain was frozen for three days and nobody could say why. **Six mechanisms were proposed,
defended, ratified, and built upon. Every single one was falsified** — *bronze-is-the-trigger*, *the $439K
deletion*, *roster-departure*, *Orion-recovery-is-a-clock*, *the staleness ceiling*, *the dispatch lock*.

The truth: `sync_scripts()` **died at step zero on a basename collision**, deployed the exact hour gold
stopped. **It was found at hour eleven by the one agent who read the chain log. Nobody had read it.**

> **We theorised all day about a system that was printing its own cause of death to CloudWatch.**
> *Seven agents, each grounding carefully, each citing source — and not one of us opened the log.*

**Read the log. Read the error. Read what the system says about itself — BEFORE you build a model of why it
is behaving that way.** A ratified mechanism that nobody checked against the system's own output is a
committee's opinion.

**A CONTROL THAT ARGUES FOR ITSELF WITH A CLAIM THE READER CAN FALSIFY IN ONE QUERY WILL BE SWITCHED OFF BY
THE FIRST COMPETENT PERSON WHO READS IT.** Ask not only what your control *does*, but what it *says*.

---

## I. Controls

**A CONTROL THAT CANNOT FAIL IS NOT A CONTROL.**
Before recording a PASS, ask: *could this have failed?* If not, it measured nothing.
*A shim was validated in a shell that had no `.tools` on PATH and therefore could not have failed. The row
was recorded PASS. It was RIGGED, NOT PASSED.*

**A CONTROL CAN PASS BECAUSE BOTH SIDES ARE EQUALLY BROKEN.**
*A harness compared `HEAD_FAILED` against `HEAD_FAILED` off a 404 and scored it green.*

**A CONTROL ONLY DISCRIMINATES WITHIN THE AXIS IT SAMPLES — THE AXIS IS PART OF THE STATE SPACE.**
*CVO's AC4 lane-1 mutant (patched `ok=TRUE` vs canon `ok=FALSE`) was a REAL control — but BOTH arms ran
comp-kuzu's PROJECTED edge inventory (53), so it was structurally blind to a RAW-axis error: 2 edge-types
(`IN_SUBNET`, `SENDS_TO`) live only on the producer's raw `graph_edges` (55) and were invisible to the
projected sample. A rigorous point-verification survived review because it sampled the WRONG axis
(Verification Law #6); the live-cadence check on the CONSUMER's raw axis caught both on run #1. This
sharpens "enumerate the state space before choosing a control" (Rule 22b): the AXIS is part of the state
space — a control that does not enumerate the axis it samples is measuring less than it thinks, and
reports full confidence while doing so. (CVO surfaced, CTO generalized, COO consolidated; paired with the
LD-0314 CHECK-LIVE-NOT-FROZEN instance-#4 run-#1 catch, 2026-07-18.)*

**A CONTROL THAT FAILS LOUDLY GETS FIXED. A CONTROL THAT PASSES VACUOUSLY GETS TRUSTED.**
**And a number that is merely WRONG gets QUOTED — because nothing about a wrong number announces itself.**
Three costumes, one shape; all three ran on 2026-07-16 and only the loud one summoned anyone:
- **FAILED LOUD** → the RV watermark stopped advancing. Andrew noticed and spawned a CVO. *Fixed.*
- **PASSED VACUOUS** → "Append-only integrity: PASS both logs" — both logs untracked + gitignored, in-window
  commits `0` and `0`, so the `numstat` walk measured an **EMPTY SET AND COULD NOT FAIL**. It reported PASS
  straight through a real in-window non-append edit. *Trusted, for weeks.*
- **JUST WRONG** → `7` overrides "this window" was the **07-14 DAY**; the window was **10**; the review built to
  catch exactly that carried its own third number (`6`). **Three records, three numbers, none of them right,
  none noticing the others** — and the wrong one was spent justifying a permanent grant.
**A wrong number has no failure mode; it has a readership.** *(CVO `3.0.0_SA_CVO`, RV-0050 F-F, 2026-07-16.)*

**AND THE UNCOMFORTABLE COROLLARY: THE THING THAT ACTUALLY WORKED HAS NO GATE BEHIND IT.**
Every catch on 2026-07-16 ran through the same uninstrumented path — **somebody read the thing and checked**:
the wrong-key `0` (read the artifact's real schema), the `'*'` wildcard misread as *"1 member, not permitted"*
(read the value behind the verdict), the retracted LD-0204 carve-out (read the authority before obeying it),
the day-quoted-as-window (a peer opened the log the accusation named), the `trn_nna` gap (read the box's actual
output leg-by-leg instead of accepting *"the box does it"*). **Not one was caught by a gate.**
*And the gate that looked like it fired did not: a peer's `STOP --` was the bare English word, not the `[STOP]`
token — `halt-gate-check.sh:128` requires literal brackets, so nothing classified and nothing hard-blocked. The
record was stopped by being READ. Crediting the token would have been the very error under correction:
**attributing an outcome to a mechanism that was not involved.** The peer got the proportionality right by
accident — brackets would have hard-blocked a whole lane over a documentation error.*
**Do not let a near-miss be written up as a gate working.** A gate that did not run gets no credit, and an
instrument that was not consulted gets no blame. **Write down which one actually caught it** — because the
estate will fund the mechanism the story names, and today the story's true subject was reading.

**SCRUPULOSITY IS NOT RIGOR. IT HAS THE SAME POSTURE AND NONE OF THE CONTROLS.**
Care that *feels* like rigor reaches for the first mechanism that confirms the worry — and never opens the log.
**Correcting toward your anxiety is not the same as correcting toward the evidence, and it looks identical from
the inside.** The test is not how uncomfortable the correction makes you; it is whether you ran anything.
*COO filed a self-correction impeaching its own number via a "census that never walks the sovereign-override
log." The number came from a walked log. The log invoked contained exactly ONE line — COO's own read event. The
correction was built with no control at all: **the accuser never opened the file it was accusing.** A peer opened
it; one read killed the whole thing. And the error ran the other way — the true count made the grant MORE
justified, not less.* **A correct finding mis-applied is still a wrong record — and it is the durable kind,
because it arrives with a citation.**

**A POSITIVE CONTROL IS ONLY A CONTROL IF IT IS RUN IN ISOLATION FROM THE TARGET.**
A control batched with the thing it is controlling for is corrupted by its own presence.
*`simulate-principal-policy` with 2+ `--resource-arns` flips the HELD ones to `implicitDeny` — it silently
disarms the very control the rule leans on.*

**KEEP A PROVEN-RED CASE IN EVERY CENSUS.**
**A census that scores a known defect as SAFE is broken, and its verdicts on everything else are worth
nothing.** A census never observed to say RED has not been shown to be able to.

**CONTROL ON THE DEFECT *LINE*, NOT THE DEFECT'S *FILE*.**
A file-level positive control cannot tell you the instrument found the *actual* defect. *One census reported
"C_07 flagged" — and the line it flagged was `:411`, not the defect at `:229`. It told him the tool worked
while the tool was blind to the one thing he built it for.*

**A TEST THAT ASSERTS THE DEFECT WILL DEFEND IT.**
When a fix makes a test fail, **ask first whether the TEST was encoding the bug.**

**WRITE THE *PROPERTY*, NOT THE *SHAPE OF THE DEFECT YOU JUST EXERCISED* — this is WHY the rule above keeps
happening to people who already know it.**
> ***"Neither of us wrote the PROPERTY. We both wrote the SHAPE OF THE DEFECT we had just been staring at.
> When you have just finished exercising a defect, the defect's shape is the most available thing in your
> head, and it writes itself into your assertion."***

*Three agents wrote the bug into their own tests, independently, on the day the rule landed. The two wrong
answers were **mirror images** — one demanded the lost row SURVIVE (fabricated attribution), the other
demanded the field that drops it stay NULL (the silent drop itself). **Neither wrote the actual property:
"the loss must not be SILENT."*** **Exercising a defect is what makes you able to write the test — and it is
also what makes you write the WRONG one.**

**REMEDY: after you exercise a defect, do NOT write the assertion from memory of what you saw. State the
INVARIANT the system must hold — in a sentence, with no reference to the bug — and assert THAT.**

**A BAR THAT ENCODES A REMEDY GRADES THE FIXER ON OBEDIENCE, NOT CORRECTNESS.**
A ruling that says *"do X"* tests whether X was done. A ruling that says *"the system must never Y"* tests
whether the defect is gone. **Rule the PROPERTY; let the fixer choose the mechanism — he can see the code and
you cannot.**

**A WARN IN A LOG IS NOT A GATE.** If a check cannot block, the record must SAY it is advisory — never let its
output be read as a pass. *Silence from a tool that was never called is a fact about the caller.*

---

## II. Grounding

**GROUND ON THE RIGHT LAYER.**
- **STATE / IAM** → the comp-tool (DESIRED) **AND** the live primitive (`get-role-policy` / `head-object` /
  `describe-*`) for APPLIED truth. A comp-tool alone cannot tell **landed** from **planned**.
- **BEHAVIOR / "it works" / "GREEN"** → **EXERCISE the path** — the test that fails if the claim is false.
  Never a config read.

**GROUND ON THE RIGHT *MACHINE*, IN THE RIGHT *CLOCK*.**
**Before believing a negative, ask: could this instrument, on this machine, in this clock, EVER have returned
a positive?** *A local `ps` for a job running on EC2 can only ever report DEAD — and "none" is the EXPECTED
healthy reading. `aws s3 ls` renders `LastModified` in LOCAL time while the fabric reasons in Z.*

**A FALSE *FAIL* IS MORE DANGEROUS THAN A FALSE *PASS*, BECAUSE ITS REMEDY IS DESTRUCTIVE.**
A false dead-job reading gets someone reaching for RESTART at 3am.

**A BARE VERDICT LOSES TO THE AGENT'S OWN INSTRUMENTS. CARRY THE MECHANISM.**
A "do not restart" order is fragile if the agent's own probe keeps saying the job is dead. **The mechanism is
what survives contact with contrary evidence. A bare prohibition does not.**

**A LINE CITATION WITHOUT A VINTAGE IS NOT A CITATION.** Cite `file:line @ <commit-ish>` (or `@ working-tree`).
`file:line` alone resolves at every vintage, to different code.

**PUT THE CONTROL ON THE RETRIEVAL, NOT THE PATTERN. PRINT THE DENOMINATOR OF EVERY SCAN YOU REASON FROM.**
*`git log --all -40 | grep <author>` printed "zero commits" from a 40-of-19,907 window and falsified a ruling.*
*`grep -c` returns `0` from an error message just as happily as from a real absence.*

---

## III. Instruments that lie

**A COMMENT IS A CLAIM WITH NO VINTAGE AND NO TEST.**
We write the invariant we MEAN into a comment, then read the comment back as evidence the invariant HOLDS.
**A comment is never source-confirmation. The assertion is the claim.**

**AND THE MOST DANGEROUS COMMENT IS NOT A FALSE ONE — IT IS A TRUE ONE THAT THE GROUND MOVED UNDER.**
It argues **persuasively, authoritatively, in the codebase's own voice, for the exact harm it now causes.**
A false comment can be caught by reading the code; **one that was right and became wrong cannot.** Only asking
*"is this still true?"* catches it. **When you move what is canonical, re-read every rationale that predates
the move.**

**CENSUS BY *FUNCTION*, NEVER BY *MENTION*.**
**A grep scores a COMMENT as an IMPLEMENTATION.** Ask *does it READ the value? which mode does it inherit by?*
— never *does the string appear?*
It cuts **both ways**: a pattern-census yields false POSITIVES (a mention read as an enforcement) *and* false
NEGATIVES (an enforcement read as absent, because it goes through a helper or an imported symbol).
> ### **WHEN THE ANSWER IS "ZERO", OPEN THE FILE.** A zero is the one result a pattern can produce for reasons
> that have nothing to do with the estate.

**A GREEN THAT RESTS ON THE *ABSENCE OF A SYMBOL* IS NOT A GREEN.**
Symbol-absence is not behaviour — a **renamed** clobber looks identical to a **removed** one. Assert on the
**served value**; treat a missing path as an **INSTRUMENT BREAK**, never as a pass.

**ASSERT THE THING, NEVER A PROXY FOR IT — and key on EVERYTHING the artifact is a function of.**
A partition key is a proxy for CONTENT and **under**-fires. A `run_id` is a proxy for PROVENANCE and
**over**-fires. **The digest IS the thing.**

**AN ENV VAR NOTHING READS IS A COMMENT WITH A DTYPE. A GUARD IN THE CODE BUCKET THAT NOTHING CALLS IS A
COMMENT WITH PARENTHESES. A FUNCTION NOBODY INVOKES IS A COMMENT WITH PARENTHESES.**
**APPLIED-CONFIG is not BEHAVIOUR.** A structural test must assert the fix is **CALLED**, not merely defined.

**A SUCCESS TOKEN CAN REPORT ON THE WRONG EVENT.**
*An SSM `rc=0` came back in 2.0 SECONDS for a full gold chain — it is a LAUNCH RECEIPT, not an outcome.
`ChainFailed` never fired because the chain dies BEFORE the metric is armed.*
**A pipeline that cannot tell you whether it succeeded should not be dispatching unattended.**

**AN ABSENCE-OF-SIDE-EFFECT PROOF IS WORTH NOTHING WITHOUT PROOF THE INVOCATION ARRIVED.**

**A TOOL THAT DECLARES WHAT IT *CANNOT* DO IS WORTH MORE THAN ONE THAT FAKES THE CAPABILITY.**

**A PRESENT-DAY FIX AND A STALE-ARTIFACT BUG PRINT THE SAME RED ON A SERVED READ.**
The served bucket carries the lie; the code that would re-create it may already be gone. **Before you dispatch
a producer fix off a served-artifact symptom, READ THE DEPLOYED PRODUCER.** *Two executives measured a real
defect on a served artifact, asserted the mechanism, and dispatched a "one-line fix" to a lane — and the
producer had been fixed for two weeks. The bug was RESIDUE.* **The remedy for residue is not the remedy for a
live defect, and only the deployed bytes tell you which one you have.**

**A DATE FIELD THAT LIES ABOUT ITSELF DOES NOT STOP LYING BECAUSE YOU READ IT FROM A LOWER LAYER.**
*Told that a producer's `source_as_of` was untrustworthy, we sent an agent to read the "true" vintage from the
source partition's own internal `date` column. **It carried the same lie.** Going one layer further down again:
the **silver pull** stamps `as_of_date`/`snapshot_date` with **the date it REQUESTED**, not the vintage of what
came back — the vendor returns the same book on Sat/Sun/Mon, and every layer above faithfully propagates it.*
**Going one layer down is not the same as finding an independent source. Ask what the lower layer DERIVES its
answer from** — if it is the same field, or the same producer's belief about itself, you have not left the
lie, **you have re-read it.**

> # **AND SOMETIMES YOU DESCEND ALL THE WAY AND THE TRUTH IS NOT THERE.**
> *We chased this one to the vendor: **Orion's own `asOfDate` ALSO echoes the requested date** — query for day
> X and it returns the latest book, stamped X.*
> ```
> ORION fabricates the vintage -> bronze faithful -> silver faithful -> gold faithful -> ETF faithful
> ```
> ## **EVERY LAYER IN THE ESTATE WAS A FAITHFUL REPORTER OF A LIE WE DID NOT AUTHOR.**
> **That is exactly why no code review at any single layer could have caught it: EACH LAYER IS INDIVIDUALLY
> CORRECT.** Do not go looking for the layer that "introduced" it — there may not be one.

**WHEN THE HONEST VALUE DOES NOT EXIST IN THE SOURCE, THE ANSWER IS A DETECTOR, NOT A FIX.**
**There is no field to swap to.** A "fix" would have to *invent* the value — which is fabricating attribution.
**Detect the symptom at the serving layer instead** (here: a repeat-guard keyed on **value-movement**, scoped
to trading days).
> **And SAY SO, LOUDLY, IN THE RECORD** — otherwise the next agent hunts for a field that is not there.
> ***What was missing was not the fix. It was the KNOWLEDGE that no fix is possible.***

> ## **BUT DO NOT WITHHOLD THE WORK TO PROTECT SOMEONE FROM A HUNT — SCOPE IT TO A *LOCATE*.**
> *I retracted an allocation because I feared it would send an engineer hunting for a week for a field that does
> not exist. **The COO had already scoped it to a LOCATE, not a repair** — "CITE THE LINE. NOBODY FIXES IT
> WITHOUT A CO-SIGN." **Dispatched 17:14Z. Answered, source-confirmed, 17:27Z. Eleven minutes.** And the answer
> **WAS** "no fix exists."*
> ### **AN ALLOCATION SCOPED TO A REPAIR CAN BURN A WEEK. AN ALLOCATION SCOPED TO A QUESTION CANNOT.**
> **The remedy for *"we do not know whether a fix exists"* is NOT to withhold the work. It is to scope the work
> to a LOCATE.** *Withheld, "no fix exists" stays a Tier-0 ASSERTION — the exact class of ungrounded relay the
> withholding was meant to avoid. **Dispatched as a question, it comes back as a grounded deliverable.***
> **Protecting a lane's week is the right instinct. WITHHOLDING is the wrong instrument. THE INSTRUMENT IS THE
> SCOPE.**

**A RIGHT CONCLUSION RESTING ON AN OVERSTATED PREMISE IS AS DANGEROUS AS A WRONG ONE — because the next person
reasons from the PREMISE, not from your conclusion.**
*An agent reported "the ONLY columns that differ are the date stamps." **His own output showed `asset_class`
differed on 2 rows. He read it and glossed it, because it fit no part of his story.*** The verdict survived —
the *value* moved on **0 of 33,381** rows, and that was the real finding — **but the sentence carrying it was
false, and the next agent's hash flipped on exactly those 2 rows and nearly produced a confident contradiction
off the SENTENCE, not off the data.**
> **Lead with the arm that actually carries the claim** (*"the value did not move"*), **not the one that sounds
> strongest** (*"the columns are identical"*). **And when a measurement produces something that fits no part of
> your story, MEASURE WHETHER IT IS NOISE — do not file it as noise.**
> *A clean sentence over a measurement that was not clean is how a true conclusion poisons the next
> investigation.*

**A HASH IS A PROXY; THE COLUMNS ARE THE THING.**
*An agent hashed three daily partitions, got three distinct digests, and concluded "the source differs, so my
consumer must be fabricating." **The hash was dominated by the two date-stamp columns he had not dropped** — the
very fields under investigation. He was one bad measurement from convicting his own script.* **He caught it by
asking WHICH COLUMNS DIFFER instead of trusting the digest.**
**When you hash to prove sameness, you must first remove the fields whose sameness is the question.**

**A SATURDAY BOOK EQUALLING FRIDAY'S IS CORRECT. MONDAY'S IS THE LIE.**
*Before you condemn a repeat, ask whether the world moved.* A carried value on a **non-trading day** is honest;
the same value under a **trading-day** stamp is not. **Scope your detector to the days on which a change was
possible** — a repeat-detector that fires on weekends is crying wolf, and one that ignores Mondays is blind.

**YOU CANNOT STAMP A DATE YOU CANNOT DETERMINE.**
When the true value is unrecoverable, **a "correction" writes a CONFIDENT, PRECISE, WRONG value onto a served
field.**
> ## **REPLACING AN OBVIOUS LIE WITH A PLAUSIBLE ONE IS STRICTLY WORSE: AN OBVIOUS LIE GETS CAUGHT; A PLAUSIBLE ONE GETS CITED.**
**Disclose the uncertainty (`carried:true`, `vintage_confidence:uncertain`) — never fabricate the precision.**
*An instrument that cannot observe must SAY SO.*

---

## III-a. An exercise that cannot REACH the governed state tests nothing — and a describing-comment never beats the state file

Two edges the session's "exercise, don't assume" discipline did not cover, earned when the VERIFIER ITSELF
passed a false verdict: CVO cleared *"broad repo-grep = staged-nudge"* while COMPRAIL Gate-1's estate-scoped
broad-grep DENY was **ARMED** (`org/mcp/comprail-gate1.enforce` present); ~Z caught it, CVO retracted + owned.
**The regime worked on the controller** — which is the point, and the deepest cut of the discipline.

> **INPUT-REACHABILITY: exercising an input OUTSIDE the control's governed domain proves nothing about the
> governed state.** "Exercise the path that fails if the claim is false" (Rule 22a) has a hidden precondition:
> the input must actually **reach** the governed case. Both agents *did* exercise — on NON-governed paths
> (non-estate files) — and both exercises passed while the governed case (an estate-scoped path) would have
> DENIED. A test on an input the control never evaluates looks like a control and tests nothing. **Before you
> accept a GREEN, ask: did my exercise input actually reach the branch the claim is about?** A positive
> control run outside the governed domain is not a control; it is a comfort.

> **STATE-FILE > DESCRIBING-COMMENT: when the live state and prose that describes the default disagree, the
> state wins, always.** The same miss had contradictory evidence — a marker FILE saying ARMED vs a hook
> COMMENT saying staged — and it resolved toward the comment. The comment describes the DEFAULT/intent; the
> marker file IS the live state. A describing-comment is a *claim about* the state, not the state; ground on
> the enforce-marker / applied config / live primitive, never the prose that narrates it. Same family as VL#8
> (a stale record speaks with authority) and comp-iam's DESIRED-vs-APPLIED — the describing layer drifts from
> the enforcing layer, and only the enforcing layer is true.

---

## III-b. Conservation is a nearly-useless oracle

> # **CONSERVATION IS INVARIANT UNDER A SWAP — AND UNDER A SIMULTANEOUS BOTH-SIDES DELETION.**

*"The firm total ties to the cent"* was cited, repeatedly, by everyone, as evidence that nothing was wrong.
**It is blind to both of the day's real defects, BY CONSTRUCTION:**

- **A SWAP** — credit moving from one advisor to another **changes no total at all.** The money leaves one
  bucket and enters another and `sum(advisors) == firm_total` holds *perfectly*.
- **A SIMULTANEOUS BOTH-SIDES DELETION** — a vanished row leaves the **advisor** side and the **firm** side
  *at the same instant*, so both shrink together and **the equation still ties to 0.00 — and it ties BECAUSE
  the money is gone.**

> ## **A RECONCILIATION THAT TIES BOTH SIDES OF THE SAME OMISSION IS NOT A RECONCILIATION.**
> ## **AN INVARIANT THAT ONLY EVER COMPARES THE ARTIFACT TO ITSELF WILL CERTIFY ANY CONSISTENT LIE.**

**THE ONLY INSTRUMENTS THAT CAN SEE THESE:** a comparison against a **PRIOR VINTAGE** of the served artifact,
or against **a source the pipeline does not derive from.** *(The $2.6M swap was finally found by diffing an
artifact that had been sitting in the bucket, unread, for two weeks.)*

**Conservation tells you the pipeline is internally consistent. It tells you NOTHING about whether it is
right — and "internally consistent" is exactly what a corrupted pipeline looks like from the inside.**
**Never lead a co-sign with conservation. State it, then state what it CANNOT see.**

---

## III-c. Count-shaped instruments and silent absence (2026-07-22, five exercised instances in one night)

**AN INSTRUMENT THAT ANSWERS WITH A COUNT CANNOT DISTINGUISH "NOTHING IS THERE" FROM "I LOOKED IN
THE WRONG PLACE." PREFER ONE THAT THROWS, OR THAT STATES ITS DENOMINATOR.**
**Scope: SILENT ABSENCE ONLY.**

The five that earned it, one night, all the same shape (ask for a count, get zero, and zero is
byte-identical between empty and misaimed): an unpaginated `list-rules` census recorded as a PRD
absence-finding; the aws-shim `--delimiter /` mangle returning `CommonPrefixes=[]` at rc=0; a
`grep -c '^+[^+]'` blank-line undercount; a `_complete/` sentinel read as absent pre-dating the
sentinel's own existence; two `s3 ls | grep -c` false zeros of the auditor's own making, caught
only by positive-controlling the parent prefix.

The scope line is load-bearing, and its narrowness is the asset:
- **FALSE PRESENCE is a different failure with a different control** (a resolver returning a
  commented-out call site had honest input and an honest denominator — resolution-time liveness
  is the control there, not this rule).
- **An unmeasured claim in a record is not an instrument failure at all** — no tool ran.
- A doctrine claiming one strength above what it does is itself the docstring-overstates-the-
  safeguard defect, INSIDE the doctrine written against that class.
- **Gateable as written:** name the count-shaped call; require a positive control or a printed
  denominator beside any absence-verdict it produces.

The DS line, verbatim, because it is the whole point: *the parquet footer read caught what every
path-based scan missed because it COULD NOT FAIL QUIETLY, not because DS was more careful. Care
is not a control; instrument choice can be.*

## III-d. What one day earned (2026-07-25, NFRA_TOOLUNIFY → COMPLEARNS; the wrong mechanisms were caught by controls failing, not by anyone being careful)

> **This header carried a frozen count — "Six that earned it" — while the section held twelve items,
> because each was appended without re-reading the whole. That is the third instance of one shape in a
> single day, all by the same author: a rule saying "ONE axis of three" above four listed axes; a spec
> stating its own status three contradictory ways; and this, inside the section whose first item is
> about gates that cannot be satisfied.** The count is now gone rather than corrected, per the estate's
> own lesson: *a number a document hand-maintains WILL drift, so state the property instead.* The rate
> is the finding — **knowing a failure mode by name does not immunize you against writing it, and
> writing it down does not immunize you either.**

**1. AN UNSATISFIABLE GATE IS NOT A STRICT GATE — IT IS AN AMBIGUOUS ONE, AND AMBIGUITY RESOLVES
TOWARD WHOEVER NEEDS TO SHIP.** An emit-flip was gated on "the 14-mutant conformance suite lands"
when one member's mutant is *unwritable by construction* — the suite tops out at 13, permanently.
Two failure modes pull opposite ways: **STALL** (wait forever for a mutant nobody can write) or,
likelier, **FUDGE** (land 13, call it complete, absorb the exemption silently). **The fudge path
required no corner-cutting — an ordinary reading of the gate reaches it.** Fix: state the bar as
`13 SATISFIED + 1 DECLARED-EXEMPT`, rendered by the suite itself. *Gateable: any gate whose
condition names a count must be checkable against a reachable maximum.* Sibling: the second time
in one day a rule failed by being *followed* (the other: an "avoid parens" workaround that
under-covered 4 of its 5 real triggers and **read as complete**).

**2. "I VERIFIED THE FIX" IS NOT "I VERIFIED THE MECHANISM OF THE FIX" — ONLY ABLATION ANSWERS
WHICH PART IS LOAD-BEARING.** A guard was measured end-to-end (0 → 9 matches) and its closure
attributed to the wrong component; removing the *actual* load-bearing part (`shlex.quote`) showed
4 of 5 hazard shapes silently corrupting **inside** the guard. The misattribution reached CLAUDE.md
and was caught only by re-reading the landed text. **A law that misattributes a control's closure
is the premise a reader needs to REMOVE the control while reasoning correctly from the record.**

**3. A MECHANISM CLAIM ENTERS A RECORD ONLY AFTER INDEPENDENT REPRODUCTION — AND THE REPRODUCTION'S
ORACLE MUST OBSERVE THE HYPOTHESIZED FAULT DIRECTLY.** Symptoms record immediately; mechanisms wait.
When the hypothesis is *"the argument is being corrupted,"* the only valid oracle **echoes the
argument back** — the downstream tool's verdict cannot distinguish *intact* from
*corrupted-but-matched-by-luck*. A verifier's "NOT REPRODUCED" was a **false negative** produced
exactly that way: its own control was being mangled the whole time and matched by coincidence.
Three parties held three wrong stories about one real symptom before the echo-back settled it.
*Corollary already paid for: a sweep scoped off an unverified mechanism does not merely waste
effort — it manufactures a FALSE ALL-CLEAR over the actual hole.*

**4. A CORRECT EXCLUSION CAN DELETE THE ONLY TELL OF A BLINDNESS.** Filtering sub-resource
constructors out of a coverage census was *right* (they make no API call) — and it removed the one
textual marker of a code shape whose operations were **entirely untraced**. Verified mechanically
correct, and consequentially blinding. *When you exclude a token, ask what else that token was the
only evidence of.*

**5. REDUNDANT DERIVATION IS A CONTROL ONLY WHEN THE DERIVATIONS CAN DISAGREE — AND PUBLISHING RAW
DENOMINATORS DOES NOT MAKE THEM ABLE TO.** The day's
error-detection came from producers publishing **raw accounting lines** that collided — not from
the verification lane being right (it was wrong 8 times, self-caught). Conclusion-only reporting
structurally removes the detector, and **two agents asserting the same wrong thing sail through
with nothing flagging it.** Design consequence: a report contract must require the raw denominator
and predicate, not just the verdict — that is what makes the *verifier* verifiable.

> ⚠ **CORRECTED 2026-07-25 (base CTO, cross-lens; the remedy above is NECESSARY AND NOT SUFFICIENT,
> and the difference changes what this item LICENSES).** Two independently-built consumer censuses
> **published full raw member lists — denominators, not conclusions — and agreed member-for-member at
> 13.** Both carried the identical `if not f.endswith('.py')` filter; both were short by the same
> extensionless file (`.tools/comp-secrets`). The remedy in force was *pin the SET, not the COUNT*,
> authored precisely to defeat count-level agreement — **and the member-level diff returned
> "identical, no action."**
>
> >> **PUBLISHING RAW DENOMINATORS MAKES DISAGREEMENT VISIBLE; IT DOES NOT MAKE THE DERIVATIONS
> >> INDEPENDENT. Only a DIFFERENT ENUMERATION can disagree about what was never enumerated.** <<
>
> The defect was **upstream of reporting**, in the shared enumeration — so no reporting contract could
> have caught it. **Two agents publishing matching denominators reads as verification and is not.**
> The independence that matters is in the SENSOR (`ROUTE_LOGIC_AND_THE_SEMANTIC_BOUNDARY.md` §5a), and
> the only check that dissents across a shared sensor is the positive control (§5a.1): *name a member
> you KNOW is in `I`; does `S` emit it?*

**6. EVERY COMPARISON HARNESS GETS AN EXPLICIT `INCONCLUSIVE` BRANCH.** The failure mode is a
**broken side reading as a negative result**: a set-diff printed "NOT IDENTICAL" because one vintage
loaded empty (a `__file__`-derived path resolved into a scratch dir), and a map-census reported
"1,677 invisible items" because it diffed against a set its parser had read as zero. Both were
caught only because a number contradicted something the author already knew. *A harness that cannot
say "I don't know" says "no" instead.*

**7. AN END MUST BE CHOSEN, NOT REACHED — AND "IT KEEPS FINDING THINGS" IS NOT A REASON TO CONTINUE.**
A remediation arc ran six stages in ~two hours, *each one generated by the previous stage's verify*.
Productive, and unbounded — the same shape as a control escalated four times in one morning. The
verifier proposed its own stop, unprompted: **close after the current round regardless of what else
remains findable, with residuals NAMED rather than chased.** What makes stopping safe is that
**a residual its author has named is BOUNDED — the next reader inherits the limit along with the
tool.** The threshold that makes it checkable rather than a mood: *fix it only if it (i) makes an
output WRONG, (ii) moves a number that will be quoted, or (iii) creates a NEW silent absence;
everything else is a named residual.* Companion move: when a genuinely separate defect surfaces
mid-arc, **re-tag it OUT of the arc** — filing it as "Stage N+1" makes a closed thing look open,
which is the appearance the stopping decision exists to prevent. *A verifier who never says "enough"
is applying process, not judgment.*

**8. FALSE POSITIVES IN A WARNING TEACH DISMISSAL — so their cost is not proportional to their
count.** One wrongly-annotated row (a chained `Key('pk').eq(...)` flagged as needing a grant when it
issues no request) sat beside correct annotations and masked nothing. It still mattered: a reader who
checks one annotation, finds it needs no grant, and discounts the rest **has been trained by the
instrument to ignore it.** A warning surface is judged by whether it survives being checked, not by
its precision rate.

**9. TWO WEAK SIGNALS AT DIFFERENT GRAINS DO NOT COMPOSE INTO A STRONG ONE — AND A DISQUALIFICATION
RULE CANNOT REPAIR A GRAIN MISMATCH.** A tracer's operation list (CODE grain, and a *floor*) was to be
joined with AWS's `RoleLastUsed` (ROLE grain, and genuinely immune to every one of the tracer's blind
spots) to answer *"is this specific grant unused?"* — an ACTION-grain question. **The immunity claim was
correct and irrelevant: you cannot get an action-grain conclusion out of a code-grain floor joined to a
role-grain observation.** The proposer's protective instinct — disqualify the verdict for any role whose
code carries an untraced-grant annotation — guarded the join at the *role* level while the unsound step
was the *grain change*. Two instruments that each cannot license a deletion **do not jointly license
one**, and a false warrant assembled this way arrives wearing the platform's authority, which is worse
than a floor wearing none. **Controls: state the grain of every input and of the conclusion before
joining anything; and when an instrument can only support a weaker claim, THE NOUN IS THE CONTROL** —
name the output `INVESTIGATE-CANDIDATE`, never `UNUSED`, because the misreading path requires no
corner-cutting, only an ordinary reading. Companion mode from the same measurement: an ABSENT
observation (`LastUsedDate: None`) **conflates never-used with not-used-inside-the-tracking-window** —
the EMPTY-vs-ABSENT distinction again, in a new instrument, and the mode most likely to be read as
"safe to delete." Render UNKNOWN with the window named.

**10. A PREDICATE'S SENSITIVITY CAN BE *BORROWED* FROM A HUMAN DISCIPLINE RATHER THAN INTRINSIC TO THE
INSTRUMENT — AND A BORROWED SENSITIVITY FAILS SILENTLY THE MOMENT THE DISCIPLINE LAPSES.** Measured by
the first monotonicity sensor: a `version_pin` check is SENSITIVE to an addition *only if a human bumps
the source's declared version*; the same addition **without** a bump reads MONOTONE-BLIND — which is
precisely the Class-2 hole the migration to `version_pin` was performed to close. A `derived_count` check
over the same change is sensitive unconditionally, because **it counts**. Two remedies that had been
recommended interchangeably are therefore **not equivalent, and the ranking is now measured: where a
countable population exists, prefer the counting check; the declared-version check is the fallback for
things with nothing to count — and wherever it is used, the borrowing must be stated in the instrument's
own output.** The general test before trusting any guard: *what has to keep happening, by a person, for
this check to keep working?* If the answer is not "nothing," the guard's real strength is the discipline's
strength, and the guard will not tell you when that strength ends.

**11. RESOLVING A QUESTION IS NOT THE SAME AS MOVING THE INSTRUMENT — a resolution that lives only in a
report leaves the contract still saying "assume."** A verifier established live facts that settled an
open assumption (grant present, zero failures over fourteen days) and recorded it as RESOLVED. But the
unit's check type returned `ASSUMPTION` **unconditionally** — classified by the sensor as
`IMMOBILE-BY-CONSTRUCTION`, a predicate **no change to the estate can ever move.** So the finding was
real and the instrument was untouched: the same gap as fixing prose while leaving the pin. **Pair every
resolution with the question "which predicate now moves that did not move before?" — and if the answer
is none, the resolution is an assertion in a document, not a change in what the system can detect.**
Corollary from the same measurement: keep **DECLARED** (undetectable by design) strictly separate from
**UNKNOWN** (could not synthesize a test). They are opposite epistemic states, and folding them together
converts "nothing could ever catch this" into "nobody got around to it," or worse, the reverse.

> **INSTANCE 2026-07-25 — a WARNING is the same defect as a resolution, and this one recurred against
> itself.** `sovereign_held.py:127-129` carried a NAME NOTE recording that *an unflagged rename here
> made a reviewer's positive control return a false ABSENT (2026-07-22)*. **Three days later the same
> rename did it again** — `SOVEREIGN` → `PROD-TARGET:` — this time to the regression suite guarding a
> **live, never-retracted** production-write prohibition: the guard fired correctly while its only
> detector sat red, so the control was working and effectively unwatched.
>
> >> **THE NOTE RECORDED THE INCIDENT AND DID NOT BECOME A CONTROL.** << The prose was accurate,
> prominent, and in the very file it was about. **No predicate moved, so nothing detected the repeat.**
> Control question unchanged: *which predicate now moves that did not move before?*

**12. REVIEW THE DESIGN, NOT ONLY THE BUILD — the cheaper loop by an order of magnitude, measured in
one day against its own alternative.** Two remediation patterns ran side by side. **Pattern A:** six
stages, each generated by a verify finding something *after* it was built — productive, and each round
cost a full build-verify cycle. **Pattern B:** the dispatcher held one proposal for a design read before
any code; the reviewer measured the instrument, killed the proposer's framing outright (an
action-grain conclusion from a role-grain observation), and returned a hard scope; the build came back
**honoring every bar with no scope defects, plus one mode handled better than specified.** Cost: one
message. **The asymmetry is structural, not luck — a scope defect found after building is a rebuild,
while a scope defect found in a design read is an edit to a sentence.** Corollary earned in the same
pass: a verifier that cannot exercise a render path must NAME it — "structurally correct but not
exercised" is a different verdict from "verified," and the gap between them is closed by a synthetic
self-test, not by more sampling.

**13. A TEXT MATCH OVER CODE CANNOT DISTINGUISH A MENTION FROM A USE — THE PARSE TREE CAN.** Three
instances in one day, all on *controls* rather than on ordinary searches, which is what makes it
doctrine: a builder pre-named it in a code comment (*"a literal grep for the forbidden word cannot
distinguish an assertion from a mention"*); a verifier's forbidden-vocabulary grep then produced exactly
that false positive — seven hits of one word used in an unrelated, correct sense; and the same builder's
own *"this suite makes zero network calls"* proof false-positived on its **own docstring**, which named
the very functions it was explaining that it does **not** call. **The remedy is structural, not more
careful pattern-writing: inspect the AST and collect the calls actually made** (that run resolved to
`classify/check/datetime/set/len` — never the network functions the text match had flagged). The general
form, and the reason it sits beside the echo-back oracle: **when the question is "does this code DO X,"
a string search answers a different question — "does this text CONTAIN X" — and the two diverge exactly
where documentation, negation, and explanation live, which is precisely where careful authors write.**
Companion discipline from the same delivery: *prove a suite can redden by making it redden* — insert a
deliberately wrong check, watch it FAIL and exit non-zero, then remove it and re-confirm the clean pass.
An assertion that a suite *could* fail, never once run wrong, has not been tested.

> ⚠ **NARROWED 2026-07-25 — the second clause of the title ("THE PARSE TREE CAN") was OVER-CLAIMED and
> is FALSE unqualified.** Reached independently by three reviewers on three evidence sets, one of whom
> had not read the others.
>
> >> **A PARSE TREE DISTINGUISHES MENTION FROM USE ONLY IF IT RESOLVES *BINDING*. PARSING ALONE DOES
> >> NOT — AN AST MATCH ON A BARE NAME IS TEXT MATCHING WEARING A PARSE TREE.** <<
>
> **Both directions were measured, and the recall failure is the dangerous one:**
>
> | direction | instance |
> |---|---|
> | **under-match (silent)** | `boto3.resource(svc)` → `.Table(name)` → `.put_item(...)` is **never traced**. `opal-data-refresh-api` executes **5 real DynamoDB operations** and comp-iam's AST output contained `"dynamodb"` **ZERO times** — zero positive-controlled, verified 0→30 after the fix `@65876f746`. **The parse tree did not confuse mention with use; it missed the use ENTIRELY, and its silence was indistinguishable from absence.** |
> | **over-match (loud)** | a bare `ast.Name` census matched `_HERE` / `self_test` / `_git_head` across unrelated modules and returned **5,033 of 5,312 files**, then 233. Correct only once an **import edge** was required. |
>
> **So the remedy in the body above ("inspect the AST and collect the calls actually made") is right for
> its instance and generalises wrongly:** it works because a call node binds its callee. Where the value
> reaches the call through a derived object, a re-export, or a locally-defined wrapper, **the AST is as
> silent as the grep and far more trusted.** Ask what the parse tree RESOLVES, not whether you used one.
>
> **Sub-mode recorded here rather than as its own item — VALUES THAT CANNOT DISCRIMINATE WHAT NAMES
> CAN.** `RETRACTED_20260709_PATHS` and `PROD_WRITE_FORBIDDEN_PATHS` were **byte-identical**, as were
> both BUCKET tuples: one retracted, one a live production-write prohibition, **separable only by the
> binding identifier.** The natural remedy — grep the bd/schwab literals and remove them — cannot
> discriminate, removes both, and **looks like it worked.** Key on the symbol, never on the values.

**14. A COMPARISON BETWEEN TWO OUTPUTS OF THE SAME COMPUTATION IS NOT A CHECK — IT IS A TAUTOLOGY THAT
RENDERS PASS FOREVER AND LOOKS LIKE COVERAGE.** A remedy chain reached its obvious final step —
compare a source population's size against a newly-added report-side count of that same population —
and the step was **wrong**: the source side reads `len(roles)` from a file, and the report side is a
compiler's serialization of `len(roles)` from that same file. **The two sides cannot disagree.** The
same check type had been genuinely powerful one unit over, where the report side was a **managed number
a human could let drift** — so **the type is not what makes a check real; the INDEPENDENCE of its two
sides is.** The question to ask before wiring any comparison: *what would have to happen for these two
sides to disagree?* If the answer is "nothing — the same code computes both," it is not a check, and
shipping it is worse than shipping nothing because it manufactures the appearance of coverage. *Caught
here two minutes after the dispatch, by a reviewer who had recommended the underlying remedy and
therefore had every incentive to let its natural conclusion stand.* The re-aimed target was the real
one: the same derived value, checked against **six hand-copied prose copies** that had drifted precisely
because nothing derived them.

**15. A CLAIM A LATER COMMIT OBSOLETES IS NOT AN ERROR — THE MISSING SCOPE IS THE VINTAGE.** A lane
determined "no migration is possible; no report-side count exists," named its own falsifier
(*"unless you find a count I missed"*), and refused a plausible near-miss after checking its provenance.
A subsequent build then **created** the count. **That is supersession by construction, not a wrong
determination** — and recording it as "they were wrong" would misattribute careful work and teach the
lane to hedge next time. Companion controls: **(a)** a vocabulary control must match on the **assertion,
not the token** — measured twice in one hour, in two distinct modes: *polarity-blindness* (a refusal
line reading "not UNUSED" passes a `\bunused\b` search **because it contains the word**) and
*sense-blindness* (a forbidden-token sweep flagging seven correct uses of one word in an unrelated
sense). Check the structured field, never the rendered prose. **(b)** **A schema/reader mismatch is
undetectable by exercise alone**, because the happy path never populates the missing field either — it
needs a **WRITE-SITE CENSUS: for every field a surface READS, name the code that WRITES it.** Two dead
fields were found on one surface that had already passed an adversarial verify; neither was found by
reading code — one fell out of grounding a wrong hypothesis, the other only because "did it happen
twice?" was made an explicit acceptance criterion with a printed denominator.

**16. NOT EVERY STALE-LOOKING COPY IS A DEFECT — A DATED MEASUREMENT IS A RECORD, AND AUTOMATION THAT
"CORRECTS" IT FALSIFIES HISTORY.** After a day spent converting hand-copied numbers into derived ones,
the census of one estate's copies came back in **three** categories, not two: **MANAGED** (regenerated
from a run-time value), **CITE-NOT-COPY** (mechanically unreachable — point at the source instead), and
**FROZEN-WITH-REASON** — dated verification records, seed-transition narratives, an audit-time
measurement. Those last are *correct precisely because they do not track current state*: a number
recorded as "what we measured on date X" becomes a lie the moment a refresher updates it, and the lie is
**invisible afterward**, because the value now looks right. **So the classification question is not "is
this copy stale?" but "is this an ASSERTION ABOUT NOW or a RECORD OF THEN?"** — and a record wrongly
classed as current is the worst outcome available to a managed-region system, strictly worse than the
drift it was built to fix. Recursive corollary from the same census: **a `grep` FOR a hand-copied count
is itself a hand-copied count** — the check inherits the defect it checks for, and the fix is to drop the
digits from the pattern and verify the remaining limbs.

**17. WHEN YOU MOVE VALUES INTO A GUARD, VERIFY THE GUARD'S COVERAGE REPORTING *BEFORE* THE MOVE, NOT
AFTER — a migration raises the stakes on the destination's blind spots, and the person recommending the
migration owes that check.** Filed by a verifier against itself as **the third instance in one session**:
it recommended a check-type migration and left the coverage denominator at one of three sites; it
recommended that check type again without knowing its sensitivity was borrowed rather than intrinsic; and
then it ruled that nineteen hand-copied numbers should become managed regions — a correct ruling,
executed well — **without first looking at whether the managing mechanism could report what it was
watching.** It could not: the guard printed *"0 drifted"* with **no denominator**, and a malformed region
was silently unscanned (demonstrated against the regex, not inferred), so *"all 24 regions are
malformed"* and *"nothing has drifted"* rendered identically — and the contract unit consuming that exit
code would have read PASS under a description asserting freshness. **A true verdict about nothing.** The
pattern in the verifier's own words, which is the sharpest form of it: *each time, the recommendation
improved the estate and quietly increased what a single unexamined silence could hide.* **The pre-step
is cheaper than the post-hoc every time, and the fix is usually one line: make the guard state its
denominator — "N regions compared across M files, 0 drifted" — so a wiring typo appears as a count drop
instead of as silence.**

**18. A SCALAR IS LEGITIMATE IFF ITS UNIT MEANS THE SAME THING ACROSS EVERYTHING IT SUMS — the test
that turns "this total looked wrong" into a rule.** An aggregate published `138 covered items` over five
sensor reports and it was a violation; the same aggregate published `2 of 5 tools have a doc plane` and
that was correct. **The distinguishing question is not "is it a total?" but "does the unit survive the
population?"** — `item` silently changes meaning (a *call site* in one report, a *graph edge-type* in
another, an *env key* in a third), while `tool` is invariant regardless of which address space a tool
emits. **The prohibition on aggregating across an address space exists because address spaces make the
UNIT incommensurable, not because counting is bad**; a count over a homogeneous population that merely
*has* an address-space attribute is fine. Stated this way it is a test the next aggregate can apply,
rather than a precedent it has to pattern-match against.

**19. A WHITELIST HAS THE DISCRIMINATION OF ITS LOOSEST MEMBER — AND ITS FALSE-ACCEPTS ARE SILENT WHILE
ITS FALSE-REJECTS ARE LOUD.** A declared-vocabulary validator flagged every *accurate but undeclared*
term and passed every *declared but wrong* one. Measured instance: two declared terms sat one word away
from live ones with genuinely different meanings (a node's *identity* vs its *kind*; a *branch* vs a
*call site*), so an author reaching for the near-miss got a **clean report about the wrong thing**, while
an author emitting the accurate novel term got flagged. **Being precisely wrong was rewarded; being
accurately novel was penalised.** Loud errors self-correct — someone sees the flag. Silent ones compound.
**And the consequence that undercuts the obvious metric: the flag's RATE IS A BIASED ESTIMATOR of
vocabulary health, because it counts the accurate-novel emissions and structurally cannot count the
precise-wrong ones.** The instrument that surfaces this class cannot measure the half of it that
matters. Remedies: disambiguate near-misses *at the term* (state what it is NOT), and **report both
denominators — declared, live-emitted, and their intersection — because "over-declared" and
"under-conforming" have opposite remedies and a single ratio picks neither.** Corollary, learned by
proposing the wrong fix first: an `ANTICIPATED` marking with no owner and no trigger **recreates the
indistinguishability it was invented to remove, one level up** — a forgotten term with better branding.

> **PROVENANCE NOTE — `git log -p` ON THIS FILE IS MISLEADING FOR ENTRIES 18 AND 19.** They were authored
> by `1.0.0_SA_CTO~Z` and were sitting **uncommitted in the working tree** when `3.0.0_SA_CVO~Z` committed
> entries 20-21 at `e4ce672101` with a file-level pathspec — so **18 and 19 landed inside that commit,
> under CVO~Z's author line.** Their text was not altered; only the author line and the commit they
> arrived in are wrong. The commit was already pushed to `origin/CLOUD`, and NEVER#7 forbids rebasing a
> shared branch, so this note is the record rather than a rewrite. *(Same class and same remedy as the
> CLAUDE.md provenance note: a probe commit swept another agent's working-tree edit, and the correction
> has to live in the file because the commit history cannot be fixed.)*
>
> **How it was caught, because that is the transferable part: NOT by care.** The commit reported **68
> insertions** against a block of roughly **45**. That mismatch — an arithmetic check against an
> independently-derived expectation — was the entire detector, and it is the same discriminator as all
> four instances in **21** below, which was being landed in that very commit. **Residual named, no control
> exists for it:** `safe-commit` with a file-level pathspec **cannot distinguish your hunk from a peer's
> in the same file**, and the commit gate checks content, not authorship-of-hunk. Nothing would have
> objected.

**20. THE OR-BOUNDARY — WHICH DISJUNCTIVE CHECKS ARE ACTUALLY SUSPECT.** Four findings in one day were
against OR'd patterns, and the over-generalisation forming from them — *"disjunctive checks are
unreliable"* — is false and expensive. The boundary:

> **A disjunction of PROPER NOUNS is a legitimate presence check. A disjunction that mixes proper nouns
> with GENERIC vocabulary has the sensitivity of the GENERIC TERM.**

`comp-debris|comp-similar|comp-iam-usage` is fine — each limb names one thing that either exists or does
not. `catalog|tools_index|ledger` is not: the generic limb matches almost any prose, so the check passes
whatever the specific limbs' real state. **The defect is never the OR; it is a generic limb silently
carrying the whole predicate.** Recorded because the narrower claim had *already* changed behaviour —
frozen digits were dropped from an unrelated pattern on the strength of it — so leaving the broad version
standing would have licensed edits the evidence never supported. **A correction issued against your own
findings, published WITH them, is worth more than the findings: most instruments never emit the boundary
that tells a reader which of their own alarms were real.**
**FIRST ACQUITTAL, recorded as a property of the boundary and not just an instance:** applied to
`NOT yet tenant-neutral|Opal-bound|not tenant-parameterized`, this rule **cleared** the check — three
specific multi-word phrases, no generic limb carrying the predicate — and the real defect was found on a
different axis entirely. **A rule that has only ever convicted is indistinguishable from a rule that
always convicts; its first acquittal is what proves it discriminates.** Without the boundary, *"OR'd
patterns are suspect"* would have taken a scalp on a pattern that is correct.

**21. A SILENT-FAILING RETRIEVAL HAS NO FAILURE CHANNEL, SO IT NEEDS AN EXTERNAL DENOMINATOR.** The estate's standing
line is *control the retrieval, not the pattern*. **One day produced four instances, in four different
hands, by four different mechanisms — and not one produced an error:**

| mechanism | what it produced |
|---|---|
| case-mismatched `grep` against an `IGNORECASE` checker | a confident **0** from a pattern that never matched |
| MSYS rewrote the search pattern before the tool saw it | a confident **0** — *the wrong question asked correctly* |
| `grep -c … \|\| echo 0` — **`grep -c` exits 1 on zero**, so the fallback appended a SECOND zero and `"0\n0" != "0"` | **the precise INVERSE of the truth for all 15 files**, rendered as a clean list |
| a 34-failure run piped through `tail -25`, then counted in the artifact | **24 of 34**, grouped by file, presented as the complete distribution — inside a correction, which carries extra credibility |

**One class, not four bugs: the RETRIEVAL was broken and the PATTERN was fine.** Every output was
well-formed, plausible, and confidently shaped. **In all four the tool's own verdict could not detect it
— only an external count could:** the producer's own total (34 vs 24), a positive control that MUST be
non-zero, or an arithmetic check that must close. One of the four was caught by **taste alone** — 15-of-15
was too tidy to be real — and that is the warning, not the reassurance: **the control did not exist, and
only judgment stood between a clean inverted list and the record.**

>> **A COUNT YOU CANNOT CROSS-CHECK IS NOT EVIDENCE, HOWEVER CLEAN IT LOOKS. And note where these were
>> caught: on `bytes: 0`, on a per-file positive control, on a producer's own total — every one on a
>> CONTROL, not one on the conclusion, because every conclusion read entirely reasonable right up until
>> the control contradicted it.** << Four independent agents, one session, one class — including a
Tier-1: **this is not a lane-level discipline problem, and any single instance would have read as
carelessness.**

> ⚠ **NARROWED 2026-07-25 (CVO~Z, falsified against its OWN session). The original title — "a
> retrieval has no failure channel" — is FALSE as a universal**, and the body's *"not one produced an
> error"* described the four selected instances, not retrievals in general. **Counter-instances from
> the same day:** a YAML parse assuming name-keyed dicts → `TypeError: unhashable type: 'dict'`;
> native Python spawning `aws` → `FileNotFoundError [WinError 2]`; a redirect to an unwritable
> scratch path → downstream `FileNotFoundError`. **All LOUD. No wrong value produced.**
>
> >> **THE DISCRIMINATOR IS SHAPE. Does the broken retrieval still return a well-formed value OF THE
> >> EXPECTED TYPE? A shape MISMATCH raises. A shape MATCH with wrong content is silent — and that is
> >> the entire class.** << Check the four instances above: a count, a count, a count, a list. **Every
> >> one returns the right type. That was the selection criterion, and the item generalised past it.**
>
> **Why the over-claim cost something:** an agent whose retrieval *did* raise reads "a retrieval has no
> failure channel," sees that theirs plainly did, and concludes the item is not about them — when the
> advice applies **precisely** when the type is right and the value is wrong.
>
> **SECOND SCOPE LINE (CTO~Z): an external denominator bounds what was SCANNED, never what EXISTS.**
> A census published an honest denominator (304 files), stated its predicate (AST live imports), and
> was **still an undercount — because its ROOTS were wrong**, missing a vendored copy under `infra/`.
> **Print the denominator AND the roots, and treat the root set as the thing most likely to be wrong**
> — for a code-consumer census the growing source is the **packaging/deploy manifest**, because a
> legitimately vendored copy exists *because* a deploy boundary forced it.

**22. A STALE CAVEAT UNDER-BOUNDS THE THING IT EXISTS TO BOUND — staleness inside a caveat has a
DIRECTION, and it favours the claim being caveated.** Lead with the corollary, because it is what makes
this worse than ordinary drift:

> **A reader treats a caveat as the CONSERVATIVE bound, and it has silently stopped being one.**

A stale descriptive claim is merely wrong. **A stale caveat is wrong while wearing the costume of
caution** — and a reader who *notices* the caveat and *respects* it is more misled than one who ignores
it. A caveat exists to bound an over-reach; when its measured scope ages, the bounded surface has
typically GROWN while the caveat still cites the smaller figure, so **the honesty mechanism itself drifts
optimistic and quietly returns the over-claim it was written to prevent.**

**This composes with 16 rather than duplicating it: 16 classifies WHETHER drift is a defect
(assertion-about-NOW vs record-of-THEN); this states WHICH WAY it errs once it is one.** A stale caveat
fails 16, and *then* fails in a direction 16 has nothing to say about.

>> **THE MECHANISM, which is why caveats age WORSE than descriptive claims even though both are subject
>> to growth: a caveat's number is written ONCE, at the moment of MAXIMUM KNOWLEDGE — the instant someone
>> was actively thinking about the limit — and then never re-derived, because re-deriving it feels like
>> RE-LITIGATING A SETTLED DISCLOSURE. The honesty was already performed; going back looks like undoing
>> it. A descriptive claim invites re-measurement; a caveat REPELS it. That is what makes the drift
>> self-sealing.** <<

**Measured instance:** a scope caveat bounding a tenant-neutrality claim reads *"the **~61** query CLIs
are Opal-bound."* Live populations: **84** extensionless CLIs / **69** `tools_index` / **87** ledger union
— **none is 61**, and no stated rule maps any of them to it (its parenthetical is an illustrative list
with an ellipsis, not a definition). **So it is not merely stale, it is UNFALSIFIABLE BY CONSTRUCTION: a
number with no derivation can never be found WRONG, only found UNEXPLAINED.** The un-generalized surface
it discloses is therefore larger than disclosed and grows with every tool added, while the follow-on work
it defers is correspondingly under-sized in the record.

**Remedy — and the same ruling landed three times in one day (a PATH probe, a verdict register, this):
a managed region or an explicit derivation rule, NEVER a hand-corrected literal, which only resets the
same clock.** Here the remedy required no invention at all: **the sibling document one file over already
manages the same population family in auto-refreshed regions.** Two docs, same population, one mechanised
and one hand-copied — the fix was to notice the neighbour had solved it.

**Two structural notes the day earned, recorded because they change what a record is FOR:**
**(a) A prematurely-checked prerequisite does not merely misreport status — it AUTHORIZES downstream
work.** A build-order item marked DONE on 2 of its 3 clauses would have opened a design phase the
unmet clause existed to prevent. **(b) The verification-depth call belongs to the DISPATCHER, not the
verifier.** A verifier under queue pressure starts accepting self-reports — the rubber-stamp path —
so thinning must be a decision with an owner (`FULL` = adversarial pass; `REDUCED` = re-derive the
headline only, tagged per item, untagged defaults to FULL), never ambient drift. Its first use
produced a *precision caveat* instead of a rubber stamp at the same cost.

## III-e. A ROSTER RESTATED IS A ROSTER ROTTED — and the control that inherits it certifies the failure it was built to catch (2026-07-28, MDPF; three substrates in one day)

**THE LAW:**
> **THE ROSTER IS DECLARED ONCE, AT THE PRODUCT'S AUTHORITY, AND EVERY CONTROL *READS* IT — NEVER RESTATES
> IT. TYPES ARE DERIVED PER SCOPE.**
> **A roster restated as a literal inside a control is a COPY, and a copy of a roster is a stale roster with
> a delay fuse.**

**Both halves are load-bearing and inverting either one produces a distinct, measured defect:**
- **Roster DERIVED from the data** → an absent member cannot register as absent. Its own completeness fields
  go quiet: `feeders_missing: []` is *literally true* over a denominator that never contained the missing
  member.
- **Types HAND-MODELLED per scope** → the producer ships only the shapes it was developed against and
  silently under-publishes every other scope.

**"DECLARED" WAS THE FIRST FORM OF THIS RULE AND IT WAS WRONG.** It was drafted as *"roster declared, types
derived,"* endorsed by a second Tier-1 agent, and held one commit short of landing. **The file that motivated
it DECLARES its roster — twice — and the draft would have certified it compliant.** The correction came from
reading the body after the location was already agreed.

**MEASURED — the control is purpose-built, ERROR-level, reviewed, and silent:**
```python
# data/mdpf/scripts/gold/mdpf_aggregate_aua.py  (71,863 B / 1,385 lines; `cottonwood` token count 0)
:492  def expected_partners_for(date):        # ROSTER COPY #1 -> drives sentinel 2
:497      base = {"49financial"}
:498      if date >= INFLECTION_PARTNER_ONBOARD_DATE: base.add("inflection")
:736  # MDPF_ASSETS.019 SENTINEL 2 -- expected partners present  <- built AFTER a 5/19 partial-emission miss
:744  missing_partners = sorted(expected - present_firms)
:750  s2_status = "ERROR"                     # if any expected partner is missing
:757  s2_detail = "all expected partners present: [...]"        <- WHAT IT ACTUALLY EMITS
:1132 expected_partners = {"49financial","inflection"}          # ROSTER COPY #2, different function
:1199 "feeders_missing": sorted(expected_partners - present)    # -> [] in the served artifact
```
The file's own header states why the control exists: *"the reconcile block never checked WHICH partners were
present."* **Someone found this class, built the correct control, and gave it an identifier.** It evaluates
`{49financial, inflection} - {49financial, inflection}` = empty and reports **PASS**, while a third declared
scope is absent from a client-facing number. **Five independent self-certifications passed on the same
artifact** — `status: "current"`, `lag_vs_as_of_days: 0`, `rolled_forward_partners: {}`, `feeders_missing: []`,
and a reconciliation identity that re-derives **to the cent**.

>> **THE CONTROL IS NOT BROKEN, BYPASSED, OR ADVISORY. IT IS TRUTHFUL AND SILENT, BECAUSE ITS EXPECTATION SET
>> AND THE DATA SHARE THE SAME OMISSION. ENROLLED-THEN-FAILED THROWS `ERROR`; NEVER-ENROLLED CERTIFIES
>> HEALTHY. THE CONTROL'S SENSITIVITY IS ANTI-CORRELATED WITH THE SEVERITY OF THE FAILURE — partial breakage
>> is caught, total absence is stamped compliant.** <<

**This is the third anti-correlated instrument in the estate's record, and the second substrate for this exact
signature:** the orphan watcher reads `REACHABLE` *because* the agent is deaf; the derived-denominator
artifact reads healthiest in the worst case; this control passes *because* the partner was never enrolled.
**All three share one mechanism — the instrument's denominator is derived from the thing being measured.**
When one failure signature appears in unrelated substrates (comms fabric and data pipeline) it is a design
class, not a coincidence.

**AND THE COPY-DIVERGENCE HALF WAS PAID FOR THREE TIMES IN ONE DAY, AT THREE ALTITUDES:** a `CLAUDE.md` rule
text that landed in one copy and not the other · the watcher skill's `/c/` drive prefix corrected in Step 3
and left wrong in **Step 0**, the instruction an agent reads *first* · and this partner roster duplicated
across two functions in one file. **Prose, procedure, and code. A correction is only as complete as its
last surviving copy.**

**CONTROL (cheap, and it is a question not a tool):** for any control that compares reality against an
expected set, ask **"where did the EXPECTED side come from, and is that the same authority that defines the
population?"** If the expected set is a literal in the control's own file, it is a copy — single-source it.
**And enumerate the copies before fixing one:** here, enrolling the missing member requires finding *both*
`:492` and `:1132`, and nothing links them.

**COROLLARY — a phased-enrollment mechanism makes absence AMBIGUOUS, and code cannot resolve it.** The same
file carries `INFLECTION_PARTNER_ONBOARD_DATE = "2026-05-18"`: members are deliberately phased in. So a
missing member is either a **DEFECT** or a **PENDING ENROLLMENT**, and *the wiring cannot distinguish them* —
that question belongs to the product owner, not the tracer. **But the LABEL is wrong either way:** a
member-scoped number carrying a population-wide name and asserting completeness is a defect regardless of
which answer comes back. **Only the roster fix is contingent on the ruling; the label is not.**

## IV. Guards

**A NULL THAT MEANS TWO THINGS IS A LIE ABOUT ONE OF THEM.**
**Absence-of-data and failure-to-read must never share a signature.** Fail closed on the **UNOBSERVABLE**, not
on the **OBSERVED-AND-EMPTY** — and do not then over-condemn a legitimate zero.
**An instrument that CANNOT OBSERVE must say so; one that OBSERVED NOTHING should say that instead.**
*An `except` block that manufactures a sentinel and feeds it forward is not error handling — it is error
laundering.*

**THE DISCRIMINATOR FOR "SHOULD THIS BLIP ABORT?": does what I am about to SERVE depend on the thing I could
not read?**
A blip on a **rebuildable output** → log and continue. A blip on a **SERVING INPUT** → **RAISE** (continuing
serves a *wrong* number instead of a stale one). *The question is never "how bad is a blip."*

**APPEND-ONLY + FAIL-ON-READ = A PERMANENT OUTAGE.**
The poison pill is never removed: the failure is not transient, it is **PERMANENT BY CONSTRUCTION**.
**A refactor that moves a fragile read into a blocking position converts a degradation into an outage** — when
you relocate code, re-ask what its failure now *does*.

**DEGRADE THE VERDICT, NOT THE AVAILABILITY — AND CLOSE BOTH DIRECTIONS.**
Skipping a corrupt input trades a loud outage for a **silent miss**. The ruling is all three: skip it, **alert
loudly**, and mark the basis INCOMPLETE so the detector reports **CANNOT-EVALUATE** rather than green.
**A rebuildable artifact must never take down the served pipeline — AND its loss must never silently green a
detector.**

**A BACKSTOP THAT PROTECTS THE OBSERVABLE AND NOT THE UNOBSERVABLE IS A BACKSTOP FOR THE READER, NOT THE DATA.**
*A floor was added to a field a human would SEE, leaving `<NA>` in the field that silently DROPS the row from
the aggregate. It closed the NULL and not the LOSS.*
**An exclusion should be a DECISION, not an artifact of `NaN != 'individual'`.**

**A GUARD CAN *INVERT* WHEN THE GROUND MOVES UNDER IT.**
**When you change the source of truth, every fix that was COMPENSATING for the old one becomes a DEFECT** —
and each will still argue persuasively, in its own docstring, for the harm it now causes.
**Census the compensations, not just the consumers.**

**AN "ON" CONTROL THAT MEASURES THE *PRODUCER'S* OUTPUT IS NOT A CONTROL ON THE *SERVED* VALUE.**
*The resolver folded 164 accounts; a downstream script then un-folded them.* The instrument asked *"did the
fold happen?"* The question that matters is ***"did the fold SURVIVE to the served artifact?"***
**Ground the verification on the layer the CLAIM lives on — and the claim is always about what we SERVE.**

**NEVER EMIT A VALUE THAT *LOOKS LIKE* THE THING AND IS NOT.**
A coverage residual wearing an advisor's shape is indistinguishable to every consumer. **Where you cannot
REMOVE the residual, ASSERT THE SHAPE** — and the durable fix is the assertion, not the cleanup: *a one-time
removal fixes today; the next residual walks back in under a different name.*

**AN ABSENCE WITH A CAUSE IS NOT AN ABSENCE.**
**And a DISCLOSED lie is worse than an undisclosed one, because it carries our signature.** *Two signatures
nearly disclosed a real advisor's money as "unattributable."*

**A GUARD WHOSE SOUNDNESS RESTS ON A PROPERTY OF THE PRODUCER IT EXISTS NOT TO TRUST IS NOT A GUARD.**

---

## V. Scope

**FIX THE CLASS, NOT THE NAMED INSTANCE.**
**A ruling names the shape the RULER happened to see, and the defect does not know that.** *One defect reached
the same destination by the OPPOSITE mechanism; a fix scoped to the ruling would have shipped it.*
**When you receive a ruling, fix the class it points AT, not the example it cites.**

**SCOPE BY *EFFECT*, NOT BY *VERB* — and scope the EXCUSE to the same unit as the MATCH.**
**An exclusion evaluated over a wider scope than the match it excuses is a DISARM VECTOR.** *A gate matched
`git stash push` correctly, then found its own bypass marker inside an **echo string explaining the bypass**,
and let it through. The stash executed and parked eight agents' work.*
**The unit is the SIMPLE COMMAND — not the line, and never the prose.**
> **The recurring shape: alarm-NAME → file-FOLDER → rule-vs-CALLER → VERB-vs-EFFECT → COMMAND-vs-HOOK.**
> **We keep governing what an agent *TYPES* instead of what the system *DOES*.**

**COUNT AT THE UNIT AT WHICH THE VERDICT IS RENDERED.**
**Never reconcile two counts by adjusting one until they agree** — that is how a census stops measuring
anything. **If you can be wrong about a line, the line is the unit.** *Counting by script lets a safe script
hide an unsafe write.*

**A COLUMN-LEVEL CHECK AND A ROW-LEVEL CHECK ARE TWO DIFFERENT CLAIMS — and `.dropna()` silently converts the
second into the first.**
An aggregate over a column (`.unique` / `.dropna` / `set` / `any` / `max`) **cannot answer a question about
the ROW — and the ROW is what gets SERVED.**

**VERIFY FINDINGS JOINTLY, NOT ONLY INDIVIDUALLY — ENUMERATE THE INTERACTION.**
Per-finding severity triage is **structurally blind to composition.** *One finding made a loss silent in the
data; another removed the alarm that would have caught it. Their PRODUCT is a silent served-number defect with
no alarm — and NEITHER FINDING ALONE SHOWS IT.*
Three axes routinely missed: **STATE** (the state a rollback CREATES, not the one you are in), **INVOCATION**
(a flag that bypasses the chain), and **COMPOSITION**.

**A HAND-OFF TO AN OWNER YOU HAVE NOT VERIFIED IS A DELETION.**
*A detector was removed because "the coverage axis is owned elsewhere." Nothing owned it.*
**If you remove a check because "X covers it," you must EXERCISE X.**

**A BLANKET FIX ACROSS AN UNGROUNDED BLAST CAN *INTRODUCE* A DEFECT INTO A CORRECT SCRIPT.**

**A FIX THAT ALIGNS EVERY CONSUMER ONTO ONE SOURCE IS ONLY AS GOOD AS THE SOURCE IT PICKS.**
**Aligning everyone onto the WRONG partition is worse than the skew it cured** — *a skew is detectable by
disagreement; a CONSENSUS ON A WRONG VALUE IS NOT.*

---

## VI. Shared worktree

**IN A SHARED WORKTREE, ANY COMMAND THAT MUTATES GLOBAL STATE TO ANSWER A LOCAL QUESTION IS A HAZARD.**
`git stash` is the sharpest: `reset`/`rebase` only rewrite YOUR history; **`stash` will happily park ANOTHER
AGENT'S unsaved work — and it LOOKS read-only and reversible while being NEITHER.**
**To read a committed vintage without touching the tree: `git show HEAD:<path>`** (pipe it:
`git show HEAD:.tools/x.py | ruff check -`).

**A `git push` IS A DEPLOY.** `safe-deploy` is a pre-push hook. **An agent who obeys a "do not deploy" order to
the letter — commits, pushes, never touches the AWS CLI — HAS DEPLOYED.**
**Deploying is not a thing an agent CHOOSES to do; it is a thing that HAPPENS to them.**

**AND THE COROLLARY AT THE OTHER END: YOU CAN BE PUBLISHED BY A COLLEAGUE'S PUSH, HAVING CHOSEN NOTHING.**
`git push` pushes **THE BRANCH**, not the caller's commits. One worktree, one branch, N agents ⇒ **any** peer's
push publishes **every** agent's local commits on it. **"I have not pushed" is therefore not a control — it is a
hope, and its measured half-life is four minutes.**
*2026-07-16: COO wrote "this log is LOCAL-ONLY until 16:30Z" INSIDE the commit message of `9825431c9` (16:18:59Z)
and did not push. At 16:24:30Z `git push` returned "Everything up-to-date" — DS~A's honest 16:23:07Z
package-close push had already published it, along with CVO~B's Andrew-record. DS~A obeyed the push binding
perfectly and chose none of it.*
**THE CONTENTION CONTROL SURVIVES; THE PROMISE DOES NOT.** Batching PUSHES is real (fewer operations ⇒ fewer
ref-lock races ⇒ nobody reaching for `--force` or a rebase to "fix" one). But **publication control is COMMIT
control**: if it must not reach origin, it must not be **committed** to the shared branch — keep it uncommitted
or on a scratch branch. **A hold that the estate can break without consulting you was never yours to give.**

---

## VI-b. Granting and withdrawing

> # **A WITHDRAWAL NEEDS NO GROUNDING; A GRANT DOES.**

*A co-sign was granted on a premise that was later falsified. The signer **voided it immediately, without
re-verifying anything** — then declined to grant the replacement until he could ground it himself.*

**The asymmetry is the whole point: refusing to act is always the safe direction.** So:
- **Withdraw FIRST, ask questions second.** A withdrawal cannot cause the harm the grant was gating.
- **Never grant what you cannot see.** *"I will not sign what I cannot ground"* is not obstruction — **a
  co-sign is a claim, and an ungrounded claim on a served-output change is the thing the co-sign exists to
  prevent.**

**And when the premise of your own ruling is falsified: WITHDRAW IT YOURSELF, LOUDLY, BEFORE SOMEONE ACTS ON
IT.** *Two executives recommended a fix; the lane proved it unexecutable; both withdrew within the hour rather
than defend it.* **A ruling you have to defend against your own evidence is already dead — the only question is
whether it takes someone's work down with it.**

---

## VII. Holds and safety measures

**A SAFETY MEASURE WHOSE COST IS NEVER PRICED IS HOW A PAUSE BECOMES A POLICY.**
Name what the hold *costs*, not only what it prevents. A hold that freezes a known-wrong served number is a
**BET** — a wrong-but-STABLE number beats an unknown-but-MOVING one, *for exactly as long as you have no
instrument.* **State it as a bet, with an expiry.**

**A VERIFIED FIX IS NOT A LICENCE.**
A fix that repairs the DERIVATION has not repaired the ARTIFACT. Its status is **CORRECT-ON-NEXT-DERIVE** —
**never "the number is right."**
> **A coherent, well-evidenced, verification-citing argument for a destructive act is FAR more dangerous than
> an obviously bad one — nobody argues with the man holding a green cert.**

**23. A CHANGE THAT DISABLES THE INSTRUMENT REQUIRED TO LAND IT IS SELF-SEALING — the repair cannot be
committed through the gate the change breaks.** *Added 2026-07-25 (base CTO, MISSING lens; absence
verified by sweep before adding — the nearest existing item, `1`, is an unsatisfiable gate you can
never MEET, which is a different failure from a gate that can no longer RUN.)*

**EXERCISED, not reasoned** — a `meta_path` import blocker simulating the deletion, repo untouched:
```
.tools/commit_gate_runner.py:96   import comp_constants_cli
comp_constants_cli.py:36 / :39    from [.]sovereign_held import RETRACTED_20260709_*
      simulated removal -> BOTH arms ImportError (a relative-vs-absolute FALLBACK that retries the
      SAME module, not a missing-module guard)
.tools/commit-gate.sh:43          exec python ".../commit_gate_runner.py" "$@"
.tools/commit-gate.sh:23          "Blocks (exit 1) on any failure."
      exec -> python's rc IS the gate's rc -> FAIL-CLOSED
```
Deleting one module would have blocked **every agent's `.py` commit fabric-wide — including the commit
that removes the import.** Exits are an audited `--force` or a non-`.py` repair; both are worse than
not creating the condition.

>> **AND THE PROPERTY THAT MAKES IT DOCTRINE RATHER THAN AN ANECDOTE: FAIL-CLOSED IS THE CORRECT DESIGN
>> FOR A COMMIT GATE, AND THAT IS EXACTLY WHAT MAKES THIS DANGEROUS — the gate cannot distinguish "this
>> change is bad" from "I could not load myself." THE SAFER A GATE IS, THE MORE COMPLETELY IT LOCKS THE
>> DOOR ON ITS OWN REPAIR.** <<

**CONTROL (cheap, a pre-step like `17`):** before deleting or renaming any module, ask *"does the gate
that lands this change import it, transitively?"* — and answer by **SIMULATED ABSENCE, not by reading
the chain.** Reading the chain was the standard an hour earlier; the lane that found it flagged it as a
read and **declined to call it verified**, which was correct.

---

**PROSE CAN GOVERN A HUMAN; IT CANNOT GOVERN A CRON.**
If something must reach every agent, that is a signal it needs a **GATE**, not a paragraph.
