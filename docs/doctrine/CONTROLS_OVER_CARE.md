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
