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

**PROSE CAN GOVERN A HUMAN; IT CANNOT GOVERN A CRON.**
If something must reach every agent, that is a signal it needs a **GATE**, not a paragraph.
