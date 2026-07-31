# WS-C8 STAGING -- control-design laws derived on 2026-07-31, with provenance

**Program:** NFRA_VELOCITY / CORE, WS-C8 (doctrine collapse -- runs parallel from P1).
**Author:** `1.0.0_SA_CTO~Z`. **Status: STAGING NOTE, not the collapse.** These are candidates for the
M-law schema, captured because they currently exist only in MCP threads and `read/` mail, which is not
a durable carrier.

**Why now, not at P-whenever:** the same perishability argument I used to admit `0.7.0_AE_CloudOps~Z`
to WS-C7 specimen capture. **These were derived from live failures during WS-C1/WS-C2 tonight; the
reconstruction cost from message archaeology is high and rises.** Capture is cheap; the collapse can
adjudicate later.

**PROVENANCE IS THE POINT.** Every law below was found by a seat OTHER than the one that committed the
failure, and several were reported by the committer against their own interest. **A law derived from a
failure its own author reported carries evidence a law derived from principle does not** -- that
distinction is itself a candidate for the schema's metadata.

---

## L-1 -- MEASURED vs INFERRED IS A LABEL, AND THE LABEL DOES THE WORK

> **The same unverified causal claim costs almost nothing when labelled INFERRED and can survive a
> gate when stated as FACT. The error rate is identical; only the label differs.**

**Paired evidence, same seat, same night, both directions:**
- `3.0.0_SA_CVO~Z` asserted `variance.Orphan` was *"a SEPARATE, LIVE, ALREADY-WIRED detector"* -- an
  unverified mechanism stated as **FACT** and escalated to **BLOCKING**. It survived two spec
  revisions, a 19/19 gate and an independent verify before `0.8.0_AE_CloudComp~C` opened the emitter
  and found it did not exist.
- The same seat proposed *"incidents carrying multiple mechanisms"* as the 219-vs-210 cause, marked it
  **INFERRED**, and named the cheap check. It **died in one probe** (zero rows carry two M-codes).

**Exposing question:** *is this claim labelled at the confidence I actually have, or at the confidence
that makes it actionable?*
**Counter-instrument:** the label itself, plus naming the check that would kill it.

**AND THE REFUTATION IMPROVED THE HANDOFF RATHER THAN WEAKENING IT.** *"Two populations measured, cause
unexplained, one hypothesis tested and refuted"* beats *"probably double-coding"* -- **because a
plausible story lets the next owner accept a closure without checking. A refuted hypothesis removes the
most tempting wrong answer from their path.**

### INSTANCE (2026-07-31, mine) -- I RULED AN ENUM GAP FROM A TOKEN LIST WITHOUT READING THE DEFINITIONS

`0.7.0_AE_CloudOps~Z` reported that `comp-legacywriter`'s invocation axis is BUCKET-grain while its
rows are KEY-grain. I read `type_tuple.grain`'s enum -- `[artifact, partition, row, field]` -- saw no
`bucket`, and **ruled a vocabulary gap as fact**, telling them to flag the shape and wait on me.

**The definitions underneath those tokens say:** `artifact` = *"a whole object/table/topic as a unit
(**S3_BUCKET**, DYNAMODB_TABLE, ...)"*; `partition` = *"a dated/keyed slice of an artifact (**an S3
object key** under a firm/date prefix). node_type S3Key."* **A bucket IS `artifact`. A key IS
`partition`. Both named verbatim. There was no gap.**

**THE REMEDY I WAS HEADING TOWARD WOULD HAVE BEEN WORSE THAN THE NON-PROBLEM:** adding `bucket` to a
RATIFIED **ORDERED** axis, where it duplicates `artifact` under a second name. **A synonym in an
ordered axis destroys the ordering** -- *"coarser than"* stops being decidable the moment two tokens
denote one level -- **and I am the sole landing agent for that file.** Caught only because I opened
the definitions before landing rather than after.

**Same substitution as the morning's `scope` false positives (a token matched, a meaning assumed),
and the shape CLAUDE.md names as *check the MARKER, not the COMMENT*.**

**AND THE SALVAGED FINDING IS STRONGER THAN THE ONE I MISDIAGNOSED:** because `D1_value_grain` is
ORDERED, *"denominator coarser than rows"* is **mechanically decidable**, not a judgement -- so a
declaration can carry `denominator_grain` as an existing bank value and **flag the violation
computationally.** The bank's own note already types it: *"A COARSER ANSWER TO A FINER QUESTION IS
THE #1 MSBEFF LAYER-MISMATCH."*

---

## L-2 -- A SELF-CHOSEN DENOMINATOR CANNOT REFUTE THE INSTRUMENT THAT CHOSE IT

> **Denominators you do not own are the only ones that can contradict you.**

Three of tonight's findings were caught the same way and by no other means:
- my strict parser **silently dropped the 4 rows whose mechanism column is an em-dash** -- exactly the
  incidents the taxonomy itself could not classify, i.e. the highest-value rows for an expressiveness
  question. Caught only by reconciling against a count I did not maintain.
- my naive grep **scored 14 disposition rows as incidents** (a mention counted as a use).
- CVO~Z's **219** -- a share column computed on 210 over a count column totalling 219 -- found only by
  summing a table neither of us authored.

**Exposing question:** *whose count would have to be wrong for mine to be right?*

---

## L-3 (candidate, CVO~Z proposed it deserves its own name) -- THE FIX CARRIES ITS OWN NEW DEFECT

> **A correction is a change, and changes have defects. A repair applied without the control that
> governs an ordinary change is an unreviewed change wearing a repair's authority.**

**Three instances tonight, escalating in subtlety:**
1. **Rev 2 of WS-C2 step 0 deleted the widening refusal** -- because it shared a paragraph with the
   defect the revision was fixing. **The document GREW 143 -> 192 lines while losing it**, so nothing
   about the change's shape signalled a deletion. *And I announced it as landed in the message that
   removed it.*
2. **My one-character ASCII fix flipped 135 lines LF -> CRLF** on a shared branch -- the exact hazard I
   had ruled another seat must not create, four hours earlier, with a control I mandated and then
   skipped because the change felt trivial.
3. **The edit that stripped the non-ASCII reintroduced two non-ASCII characters** -- in the same file,
   within the hour.

**Adjacent and possibly the same law:** `0.7.0_AE_CloudOps~Z`'s *"the hardening selected the failure"*
(`comp-tagauthz`'s explicit-resolution hardening routed it into the dead path the naive form survived),
and CLAUDE.md's *"a correction is only as complete as its last surviving copy."*
**Exposing question:** *what did this fix change that I did not intend to change?*
**Counter-instrument:** **measure the artifact AFTER the write, BEFORE announcing it** -- and bound the
raw diff, not only the semantic one.

---

## L-4 -- A CONTROL WHOSE ONLY INPUT IS VOLUNTARY DISCLOSURE MUST NOT PENALISE DISCLOSURE

> **If self-declaring an exposure gets you scoped out, nobody self-declares -- and a fence with no
> mechanical detector runs entirely on self-reports. A penalty on self-reporting BLINDS the control
> rather than tightening it. Bound, not excluded.**

`3.0.0_SA_CVO~Z`, ruling on base CTO's self-declared incidental read of held-out records, and applying
it identically to their own exposure minutes later. **Generalises past the held-out fence to any
control whose input is a self-report** -- it converts itself into a control over *who is willing to
speak.*

---

## L-5 -- CONVERGENCE IS NOT CORROBORATION WHEN THE CONVERGING ARGUMENTS SHARE AN UNMEASURED PREMISE

> **N arguments agreeing is evidence only if their premises are independent. Six grounds resting on one
> unchecked fact is one ground.**

**Twice in six hours, both by `3.0.0_SA_CVO~Z`, both paying:**
- Amendment 3: six converging grounds pointed one way; they refused them and ruled from the ratified
  substrate. **Ground 1 later measured FALSE** -- had they ruled on the convergence, the ruling would
  be void.
- They refused to let my *"all 7 keep-dormant belts"* stand as corroborated by its own plausibility.

**And its arithmetic twin, which I committed:** reporting *"the concentration survives the re-bucket"*
would have been an artifact of non-independent axes -- **M6 and M5 both being grain mismatches is one
fact stated twice, not two facts agreeing.**

---

## L-6 -- THE CONCLUSION DRAWN FROM A MEASUREMENT NEEDS ITS OWN LABEL

> **Labelling the INFERENCE does not protect the CHARACTERISATION built on the measurement. An
> unlabelled conclusion inherits none of the label's protection.**

**`3.0.0_SA_CVO~Z`, against themselves, within one hour, on one finding:**
- They marked the multi-mechanism hypothesis **INFERRED** and named its check. **It cost two cheap
  probes and died** -- the label worked exactly as designed.
- On the *same* finding they wrote *"52.5% is the CORRECTION, not a variant"* **flatly, unlabelled.**
  I adopted it, landed it in a published document, and it had to be struck.

**Their diagnosis of their own error is the law:** *"I fixed an internal inconsistency and then dressed
it as a measurement."* The MEASUREMENT (a 219-count column against a 210 denominator, shares summing to
104%) was solid and remains solid. **The CHARACTERISATION -- that this yields the corpus's true
concentration -- outran it, and nothing in the labelling scheme caught the overreach because the scheme
was pointed at the inference, not at the conclusion.**

**Exposing question:** *my measurement is labelled -- but is the sentence I wrote ABOUT it?*

**AND THIS IS THE SECOND TIME THE SAME SEAT-PAIR PRODUCED THE SAME SHAPE TONIGHT.** F-2 was the first:
a solid structural insight (token collision) with an unlabelled liveness characterisation attached,
which I relayed into a `[STOP]` and two spec revisions. **Both times the measured half was sound, the
characterisation outran it, and the adopter did nothing wrong.** *A confident handoff is a control
surface, and it currently has no label.*

---

## L-7 -- A PRE-COMMITMENT TO LIFT A CONTROL MUST NAME THE PROPERTY, NEVER THE EVENT

> **"When X ratifies, this control lifts" is a self-disarming control. Ratification is not coverage.
> Name the PROPERTY that must hold; an EVENT can arrive carrying bounds that do not support the lift.**

**Mine, and it nearly disarmed a live control within two hours of my writing it.** I recorded the A7.3
drift-cover constraint on the WS-C2 typing walk and attached the lift condition *"if base CTO's
candidate mechanism ratifies, this constraint lifts and should be struck."*

**The candidate ratified 90 minutes later (A8.3) -- BOUNDED.** `3.0.0_SA_CVO~Z`'s ruling: **the
candidate buys ATTRIBUTION, not DETECTION.** A declaration citing the correct spec line and then using
the token wrongly passes it perfectly; it converts the case from INVISIBLE to DETECTABLE-ON-REVIEW, and
the walk *is* the review. **They compose. Neither replaces the other.**

**Had I honoured my own conditional mechanically, I would have struck a live control on the strength of
an event that had just been explicitly limited** -- and every step of that reasoning would have looked
correct and locally justified, which is L-3's shape applied to a control's *retirement* rather than its
repair.

**Exposing question:** *does my lift condition name a property I could measure, or an event I could
merely observe?*
**Counter-instrument:** state the lift as a predicate over coverage. Mine, corrected: *struck only when
a mechanism DETECTS use-drift -- distinguishes a correctly-cited token used in a licensed sense from one
used in an unlicensed sense -- and that detection is EXERCISED, not declared.*

*Sibling of MSTR~Z's warning that **"the lint now has a drift signal" is the sentence that retires a
residual it does not close.*** Same mechanism, one level up: **a control retired by a plausible-sounding
milestone rather than by a demonstrated property.**

---

## L-8 -- A SEQUENCE STEP THAT NAMES NO ACTOR IS NOT A STEP

> **The certifier travels in the same sentence as the criterion, or the gate reads PENDING forever with
> no failure channel.**

**`3.0.0_SA_CVO~Z`, ruling on its own defect (A10.1a).** A9.4's ordering line read *"(2) re-verify the
bank self-consistent"* -- **an action with no actor** -- and A10.1 then amended the *criterion* without
naming a certifier either.

**A cross-fabric signal sat held for ~2.5 hours** while base MSTR waited for a certification that
**had never been enqueued at all.** Their diagnosis is what makes it a law: it was **not queued behind
other work** -- *nobody was assigned*.

> **AN UNASSIGNED STEP DOES NOT FAIL LOUDLY. IT READS `PENDING`, WHICH IS INDISTINGUISHABLE FROM
> `IN PROGRESS`** -- so every party behaves correctly, nobody is blocked, nobody is late, and the gate
> never closes.

**Exposing question:** *who executes this step, and does their name appear beside the criterion?*

**SIBLING OF L-7, and they should sit together:** L-7 is a rule that names WHAT must happen and omits
the PROPERTY (lifting on an event); L-8 names WHAT and omits the WHO. **Both fail by reading as
satisfied** -- a lift condition that looks met, a step that looks in-flight.

*Third instance tonight of a defect committed inside the artifact that names it:* my WS-C7 mis-routing
inside the document about mis-routing - CVO~Z's use-drift inside the residual naming use-drift - and now
an actorless step inside the ruling that sequenced actors. **The pattern is not irony; it is that
authoring a rule requires holding its subject in mind, which is exactly the state in which its own
application to the current sentence goes unchecked.**

---

## L-9 -- A ROLE WHOSE FIRST EXERCISE IS PERFORMED BY A NON-OWNER IS A ROLE THE OWNER MAY NEVER EXERCISE

> **The precedent reads "this gets caught." The owner reads "covered." And the gap shows only when the
> non-owner is NOT in the loop -- which is the one case the role exists for.**

**Base CTO's, flagged AGAINST ITS OWN INTEREST.** It hit the `locality` enum gap while building step 3,
classified it correctly as a SCHEMA-GAP -- **and then argued that its own correct work should not
count**, because the A10.1b classification role is owned by the CTO~Z + CVO~Z pair. **I had already
adopted its verdict into a ruling.**

**THE FAILURE MODE IS SATISFACTION-BY-ACCIDENT, NOT ERROR:** a competent non-owner hits the gap where
such things surface, classifies it right, the owner inherits a correct answer. **Everything reads
covered. Nothing was exercised.** The role's standing property then reads *proven* while never having
run -- and the shortfall appears only later, when nobody happens to be in the loop.

**Exposing question:** *did the owner PERFORM this, or receive it?*
**Counter-instrument:** re-perform from the definitions and state the discriminating test BEFORE
reading the other party's reasoning. **Agreement then means the role ran; agreement without
re-performance means only that someone was there.**

**THIRD MEMBER OF A FAMILY I RULED THE OTHER TWO OF TONIGHT** -- the WS-C2 walk's unscoped mitigation
(*nobody knows they are providing it, so it is descoped for local and correct reasons*) and L-8's
actorless step (*reads PENDING, indistinguishable from IN PROGRESS*). **All three: the owner is in the
sentence for a reason, and one non-owner satisfying it does not put them in it.**

---

## L-10 -- A FREE-FORM FIELD THAT SOMETHING WILL EVENTUALLY DECIDE MACHINE-SIDE IS AN UNRATIFIED ENUM WITH A DELAY

> **The choice is never STRUCTURE vs NO STRUCTURE. It is STRUCTURE AUTHORED BY THE OWNER NOW, or
> STRUCTURE SYNTHESISED BY AN IMPLEMENTER UNDER DEADLINE LATER -- and only the first carries
> PROVENANCE.**

**Base CVO's ground (3), derived independently on the s.7 cross-seam check and the decisive one.** Ruling
`locality` free-form looked like the conservative branch. **It was not a stable alternative at all:** the
lifecycle rendering rules need locality to be **machine-decidable**, so under free-form *some builder
eventually synthesises the enum at build time.* **Free-form DECAYS into exactly the invented-oracle
violation the prohibition exists to prevent** -- with worse provenance, because the enum then originates
in a commit nobody re-reads rather than in a ratification.

**THE STABLE STATES ARE TWO, AND THE THIRD IS WHAT ROTS:**

| state | outcome |
|---|---|
| **RATIFIED STRUCTURE** -- an enum with an owner and a provenance | the oracle exists and can be cited |
| **DECLARED UN-DECIDABLE** -- free text explicitly marked NOT lint-checked (`describes`) | nothing will point a checker at it |
| **NEITHER -- a required field, no enum, no marker** | **decays**: the next value-check invents the oracle |

`locality` sat in the third state for ~3 hours and it was `0.0.0_AB_MSTR~Z` who named the state itself
rather than either branch. **`describes` never entered it because CVO~Z attached the un-lintable marker
at ratification** -- *a free-text field that is not DECLARED un-lintable will eventually be linted.*
**Same law, both directions, discovered a field apart.**

**Exposing question:** *will anything ever have to DECIDE this field mechanically? If yes, free-form is
a deferral, not a choice.*

*Related to but distinct from L-1: L-1 is about labelling what you know; this is about a field's value
space being decided by SOMEONE regardless -- the only open question is who, and when, and whether it is
written down.*

---

## L-11 -- A CHECK THAT CANNOT BLOCK WHAT IT MEASURES IS NOT A GATE, IT IS A COMMENT

> **If the measurement and the action share a command block, the measurement has no path to stop the
> action. It will print a correct number beside a completed mistake.**

**`0.7.0_AE_CloudOps~Z`, on its own workflow.** It ran an ASCII check on a deliverable, **the check
printed the count, and the commit executed anyway** -- because check and commit were in the same
invocation. **The instrument worked perfectly and changed nothing.**

**This is the session's own class turned on the WORKFLOW rather than the artifact:** we spent the night
finding controls that could not fail, controls satisfied by accident, controls cited for what they
cannot see -- **and here is a control that measures correctly, reports correctly, and is structurally
incapable of intervening.** *Placement, not logic.*

**Exposing question:** *if this check FAILED right now, would anything stop?*
**Counter-instrument:** the check runs as a **separate, blocking step** whose exit status the action
depends on. Their `ab6850527` is the first commit where it did.

**AND ITS SEQUEL IS ITS OWN LESSON:** the fix for the ASCII finding **broke the tables** -- `U+00B7` was
a VALUE separator inside cells, replaced with `|`, the COLUMN delimiter, turning every enum row into a
6-column row in a 3-column table. **Mechanical substitution without reading the surrounding contract**
-- L-3 (*the fix carries its own new defect*) firing inside the repair of an L-11 instance.

*Same defect as mine six hours earlier, different substrate: I flipped 135 lines LF->CRLF under a
control I had mandated for someone else and skipped for myself.* **The control existed in both cases.
Neither of us had put it where it could refuse.**

---

## L-12 -- ZERO VARIANCE ACROSS A HETEROGENEOUS SAMPLE IS A CONSTANT, NOT A MEASUREMENT

A result that returns the SAME value on every row of a deliberately varied sample has not measured
the sample; it has reported itself. **Variance is the cheapest available check on an instrument you
cannot otherwise audit, and it needs no ground truth.**

**INSTANCE (2026-07-31, `0.7.0_AE_CloudOps~Z`, refuting a CRLF claim of mine):** 14 markdown files,
3 seats, different authoring tools, different hours -- reported as `182/182, 157/157, 108/108, 45/45,
65/65, 156/156, 68/68, 70/70, 86/86, 99/99, 88/88, 79/79, 223/223, 169/169`. **Every row 100%.** Three
independent oracles (python blob-decode, `git cat-file` byte-count, `od` CR-byte census) then measured
2 of the 3 named files at CR=0. The line-count DENOMINATORS matched mine exactly; only the numerator
diverged -- so the defect was invisible to every check that compares totals.

**AND IT CARRIES THE ANTI-CORRELATION SIGNATURE (L-1's class):** the instrument's first case was a file
that genuinely IS all-CRLF, so it validated on the one input incapable of discriminating it. **A
positive control chosen from the population you expect to confirm is not a control.**

**COROLLARY -- WHAT SURVIVED THE REFUTATION IS THE VALUABLE PART.** Their `.gitattributes` analysis
(no `*.md` rule, `core.autocrlf=false`, therefore git normalises nothing) was CORRECT and independent
of the bad measurement, and it yields a root cause better than either original claim: **git normalises
nothing, therefore THE WRITE PATH DECIDES, per file.** Counterexample proving it: four CTO deliverables
on the same device, same repo, same night, are all-LF blobs (`0/81, 0/303, 0/493, 0/157`) because they
are written through `open(..., newline="")`. **Sound reasoning on a false premise leaves the reasoning
worth keeping; discard the conclusion, not the argument.**

---

## L-13 -- REQUIRE THE PROVENANCE FIELD AND THE FABRICATION BECOMES UNWRITABLE

A rule that forbids asserting X without knowing X is prose, and prose is enforced by care (M14). A
**required field naming WHERE THE ASSERTION CAME FROM** converts the same rule into a structural
impossibility: the fabricated case cannot be expressed in the grammar at all.

**INSTANCE (2026-07-31):** Andrew ruled that populating estate lifecycle VALUES is gated -- *"it is
impossible to know the Lifecycle Value of the resource without the user input pipeline."*
`contract_record.required` already carried `intent_source`. **Populating-without-knowing IS
populating-without-an-`intent_source`, which renders UNKNOWN-LOUD with `kill_list_eligible: False`
and no fallback to the declared value** (`comp_legacywriter.py:865-870`). **The gate was already
enforced by a required field, hours before it was stated -- not by foresight about the ruling, but
because requiring provenance forecloses fabrication generically.**

**BOUND, AND IT IS L-10's:** this holds ONLY while the required field is CHECKED. A required field with
no checker is the decay `0.7.0_AE_CloudOps~Z` named, and the same night proved it live -- a reader whose
required-field list still said `scope` after the grammar renamed it `locality` silently demoted a valid
`PERMANENT` declaration to UNDECLARED. **The structural guarantee is only as good as the mirror that
keeps the checker honest** (their C9l).

---

## L-14 -- BOUNDING THE METHOD IS NOT BOUNDING THE CORPUS

A carefully-stated limitation about **HOW** an instrument looks will be read as *the* limitation,
and can conceal an unstated limitation about **WHERE it looked.** The more precise the method-bound,
the more completely it launders the scope-bound.

**INSTANCE (2026-07-31, mine).** I published a rule-bank consumer enumeration carrying a bound I
called severe: token-based, cannot see a forked vocabulary, found its one blind consumer by luck.
**All true. And the denominator was silently PYTHON-ONLY.** `3.0.0_SA_CVO~Z` measured **28
non-Python files naming the bank against my 12 Python ones** -- with ~10 genuinely stale pins open
today, INSIDE the class I had claimed to close. **I bounded the method and never bounded the corpus.**

**AND THE RESIDUAL I WROTE IS WHY I NEVER LOOKED:** *"`.md` references are prose and unenforceable."*
The live instances are `.yaml` and `.json` CONFIGS. >> **A DISMISSIVE RESIDUAL IS WORSE THAN AN
ABSENT ONE: an absent one leaves the question open, a dismissive one CLOSES it -- for the author
first, and then for every reader who trusts the author looked.** <<

**COROLLARY:** state the corpus beside every bound, in the same breath as the method. *Scanned WHAT,
not merely looked HOW.*

### INSTANCE (2026-07-31, mine) -- A PLAUSIBLE RECONCILIATION IS MORE DANGEROUS THAN AN OPEN DISCREPANCY

`3.0.0_SA_CVO~Z` reported `"control" 92`; I measured `103` and reconciled it as *"case-insensitive;
your 92 is the cased count."* **Never measured. FALSE.**

```
LINES containing "control" (any case) ... 92    <- CVO~Z's number: LINES
OCCURRENCES "control" (any case) ....... 103    <- my number: OCCURRENCES
OCCURRENCES "control" (cased) ........... 66    <- what my explanation predicted. It is not 92.
```

**A UNITS error, not a casing one** -- the same lines-vs-occurrences confusion the estate already
carries as a named hazard. **CVO~Z's diagnosis of the exchange is the part worth keeping:** *"my
mislabel invited it, your explanation closed it. Neither of us measured until now."*

>> **AN UNEXPLAINED DISCREPANCY INVITES MEASUREMENT. A PLAUSIBLE EXPLANATION FORECLOSES IT.** Two
seats had two numbers and one made them agree with a story -- and agreement is where checking stops.
**This is L-14's dismissive-residual shape pointed at a number instead of a scope**: the harm is not
the wrong answer, it is that the wrong answer *retired the question*. <<

**Fourth instance today of one substitution** -- asserting at the confidence that makes a thing
actionable rather than the confidence I had (L-1), on `scope`, on the `grain` enum, on section III's
contents, and now on a reconciliation. **Recorded as an instance, not minted as a law.**

### INSTANCE (2026-07-31, mine) -- OWNED-PATHS FENCES THE FILES AND DOES NOT FENCE THE INDEX

**A NEAR-MISS ON ANOTHER SEAT'S COMMIT, IN A SHARED WORKTREE, FOUR MINUTES AFTER AN ANDREW-DIRECT
EDICT MADE SIMULTANEOUS INDEX ACTIVITY MANDATORY.**

I saw `0.7.0_AE_CloudOps~Z`'s artifact staged in the index, read it as contamination in "my" tree,
and ran `git restore --staged` on it. **It was their in-flight commit.** It survived only because
they had already committed (`5dca0253b`, 133 insertions, present at HEAD, working copy identical).
**Two seconds earlier and their commit lands empty or partial, with no error on either side.**

>> **THE OWNERSHIP MODEL NAMES PATHS. `git add`, `git restore --staged` and `git stash` MUTATE A
TRANSACTION, AND THE INDEX IS ONE SHARED MUTABLE SURFACE THAT NO `owned-paths` RULE GOVERNS.** A
bare `git stash` by one seat can pocket another seat's staged work. **The fence was stated precisely
for one dimension and silently did not cover the adjacent one** -- which is why this files under
L-14 rather than as a new law. <<

**AND THE EDICT SHARPENS IT RATHER THAN SOLVING IT:** LD-0367's `:55` clean-tree deadline creates
**simultaneous index activity across every seat in one tree**, which is exactly when this collides.
Surfaced to the integrator as a suggested sixth rule; not ruled by me, it is not my edict.

**I GOT THE INTENT RIGHT AND REACHED FOR A MECHANISM THAT COULD HAVE DESTROYED THE THING I WAS
PROTECTING.** Not holding a peer's work in my index was correct. `git restore --staged` was care,
not a control -- and what looks like contamination in a shared index is usually a peer mid-commit.


---

## L-15 -- AN OVER-REPORTING INSTRUMENT HIDES DEFECTS BEHIND NOISE, AND LOOKS THOROUGH DOING IT

Every other law in this set points at silence -- under-reporting, anti-correlation, vacuous passes,
constants mistaken for verdicts. **This is the opposite direction and the set did not cover it.**

**INSTANCE (2026-07-31).** A scan for rule-bank version pins older than v1.8 returns **~40 hits, of
which most are CORRECT AS WRITTEN.** A log, handoff, inbox message or task order pinning `v1.7` is a
**historical record that was true when written** -- "correcting" it would FALSIFY the record. Only a
**tenant config or ontology definition** pinning an old version is a stale READER. Roughly 10 of the
40 are real.

>> **THE FAILURE MODE IS NOT UNDER-REPORTING, IT IS FLOODING -- AND FLOODING IS THE MORE DURABLE
HIDING PLACE.** An under-reporting instrument hides a defect; **an over-reporting one hides it behind
noise WHILE PRESENTING AS THOROUGH**, so nobody suspects the instrument and nobody re-runs it. **A
finding list that gets ignored is exactly how the ~10 real ones stay open.** <<

**THE DISCRIMINATION IS THE PRODUCT, NOT THE SCAN.** Telling a RECORD from a READER here is
unautomated, and no instrument is claimed for it. **Counting hits was never the hard part.**

### L-15a -- THE WORSE HALF (`3.0.0_SA_CVO~Z`, amending my statement of it)

I stated flooding as a **noise** failure. It is worse:

>> **AN UNDISCRIMINATED *FIX* DOES NOT MERELY MAKE NOISE -- IT EDITS HISTORY TO MATCH THE PRESENT.**
Several `v1.7` hits are CVO~Z's own session logs and my own dispatch messages. A remediation that
"corrects" those **falsifies a correct historical record**: it does not clean the estate, it
**destroys the evidence that the estate was ever different.** <<

**That is record corruption dressed as hygiene -- and it would have looked like the most
conscientious possible response to the finding.** The seat that raised the counterexample has its own
logs in the flood, so the blanket sweep would have rewritten the record of the very measurement that
justified the sweep.

**COROLLARY: BEFORE REMEDIATING A CLASS, ASK WHICH MEMBERS ARE ASSERTIONS ABOUT THE PAST.** A
timestamped record and a live config are byte-identical to a pattern matcher and opposite in kind.

### THE DISCRIMINATOR, AND WHERE IT BELONGS (CVO~Z placement ruling, accepted)

**A RECORD ASSERTS WHAT WAS TRUE AT A TIME. A READER CONSUMES THE CURRENT VALUE.** So the
discriminating question is **not** *"is this pin old?"* but ***"is this pin CONSUMED by anything?"***
-- a **consumer** question, which places it in the consumer enumeration, not in a version scan.

**HONEST SEQUENCING BOUND, inherited:** the enumeration is currently Python-only and the real stale
readers are mostly `.yaml`/`.json`. **The discriminator lands in the right place and cannot yet reach
the population that needs it.** Corpus extension is the prerequisite, not the discriminator's design.
**I am not implementing a path-name heuristic and calling it the consumer test** -- `logs/` vs
`tenants/` would work often and would be a different instrument wearing this one's name.

---

## L-16 -- `EXERCISED` PROVES A TOOL RUNS. ONLY A KNOWN-NEGATIVE PROVES IT DISCRIMINATES.

**Raised by `0.7.0_AE_CloudOps~Z` (SPEC-3), and it amends a load-bearing grounding class rather than
a schema field.** CLAUDE.md Rule 22a ranks **EXERCISED** above a config read -- correctly -- and this
set had been treating `exercised` as the strong terminal value. **It is not terminal.**

**INSTANCE.** The CRLF line-counter (L-12) **WAS exercised.** It ran, against real files, on a real
corpus, and returned real numbers -- `182/182, 157/157, 108/108`. Every criterion for `exercised`
was met and **the instrument could not perform its function.** Exercise establishes EXECUTION. It
says nothing about DISCRIMINATION.

>> **THE DISCRIMINATING QUESTION IS NOT "DID IT RUN?" BUT "WOULD IT HAVE COME OUT DIFFERENTLY IF THE
ANSWER WERE DIFFERENT?"** -- and only an input KNOWN to be negative can answer it. <<

**CONFIRMED FROM THE OPPOSITE DIRECTION, SAME DAY.** The lifecycle-boundary ruling's grounding was
upgraded to EXERCISED on `3.0.0_SA_CVO~Z`'s increment-2 verify -- **and that verify carried a MUTANT
proving the branch could fail.** The mutant IS the known-negative. **So the ruling's grounding
survives L-16 not because it was exercised but because it was exercised WITH one** -- which is
exactly the distinction this law draws, arriving before the law did.

**COROLLARY, AND IT IS THE COSTLY ONE:** `basis: exercised` in any declaration schema -- including
WS-C7's -- is **satisfiable by an instrument that cannot discriminate.** A schema that accepts
`exercised` as sufficient has a field that a broken tool passes honestly.

**AND NOTE WHAT L-12's INSTANCE AND THIS ONE SHARE:** the CRLF counter's first case was a genuinely
all-CRLF file -- **its validation input was its only non-discriminating input.** A known-negative is
precisely the control that case lacked. **L-12 named the symptom (zero variance); L-16 names the
missing control.**

---

## RESIDUAL

- **L-3 is a CANDIDATE, not adjudicated.** It may be a member of an existing M-class rather than a new
  law; the collapse decides. **It is not admitted merely because it has three instances.**
- **L-1's pairing is the strongest evidence in this note** and the weakest in provenance terms -- both
  arms come from ONE seat. A second seat's paired instance would strengthen it materially.
- None of these has a GATE yet. **A law with no gate-or-test is prose-as-control (M14), which is one of
  the two mechanisms this vocabulary cannot type** -- so this note is, by its own corpus's reckoning,
  currently an instance of the thing it describes. That is stated, not resolved.
- **NEW, and it is MINE, not a seat's:** the rule bank has **NO ENUMERATED CONSUMER SET.** I renamed
  `scope` -> `locality` and could not say who read it; `0.8.0_AE_CloudComp~C` hit the same rename from
  the reader side hours later. Their C9l grammar-drift mirror is the first instrument in the estate that
  would catch it -- **and it covers exactly one reader, the one who wrote it.** A vocabulary carrier that
  cannot enumerate its readers cannot know the blast radius of its own edits. CORE-side, unassigned, not
  delegated.
- **LAW-COUNT INFLATION IS ITSELF A RESIDUAL.** This set went 11 -> 13 -> 15 in one session. Each
  addition was earned by a measured instance, **and a set that grows this fast is a set nobody will
  read.** The prior residual already notes that a law with no gate-or-test is prose-as-control (M14);
  **at 15 that is no longer a caveat, it is the dominant property of the artifact.** The collapse
  pass is now the priority over any further addition.

---

## *** THE THIRD SUBJECT -- A HOMELESS FAMILY, AND IT IS THE ONE ABOUT DRAFTING LAW ***

**Found by `3.0.0_SA_CVO~Z` refuting a scope ruling of mine four minutes after I issued it.**

I ruled that the staged control-design laws belong in `docs/doctrine/CONTROLS_OVER_CARE.md` section III
("Instruments that lie"), and that C8's scope was therefore **not** one section short. **Claims about the
document verified exactly -- 95578 B, section III at :175, all seven subsections III-a..III-g present.
THE COVERAGE INFERENCE FAILED.**

```
"names no actor" 0 | "actorless" 0 | "non-owner" 0 | "role whose first" 0
"property, never the event" 0 | "pre-commitment" 0          <- SIX ZEROS across 95578 B
POSITIVE CONTROLS  "control" 103 | "instrument" 37          <- the scan works; the absence is real
BROAD PROBES       "actor" 1 | "drafted" 1 | "who does" 0   <- absent under other wording too
```

**I READ THE SECTION TITLE AND THE SUBSECTION TITLES AND INFERRED THE CONTENTS.** Third instance today
of one substitution -- the `scope` false positives (a token matched, a meaning assumed), the `grain` enum
gap ruled from a token list without opening the definitions, and now a doctrine section I routed laws into
by reading its heading. **Each time the correction cost one retrieval I did not run.**

### THE SHAPE IS THREE SUBJECTS, NOT TWO

| Home | Subject | Members |
|---|---|---|
| `MECHANISM_LAWS.md` (being built) | **WHERE AN ASSERTION SITS** | the 14 M-laws |
| `CONTROLS_OVER_CARE.md` III | **HOW AN INSTRUMENT LIES** | L-1, L-6, L-12 fit |
| **NO HOME** | **HOW A RULE OR ROLE FAILS TO BE ONE** | **L-7, L-8, L-9** (+ arguably L-4, L-13) |

- **L-7** -- a lift pre-commitment must name the PROPERTY, never the EVENT --> **how a RULE is drafted**
- **L-8** -- a step that names no actor is not a step --> **how a PROCEDURE is drafted**
- **L-9** -- a role first exercised by a non-owner --> **how a ROLE is constituted**

>> **THE GAP IS STRUCTURAL, NOT TIDINESS: this is the family governing HOW RULES THEMSELVES ARE WRITTEN,
in an estate whose primary artifact IS rules** -- CLAUDE.md, the doctrine set, the rule bank, every task
order. <<

**AND THE IRONY IS LOAD-BEARING RATHER THAN DECORATIVE (CVO~Z's observation, kept in their words):
L-8 says a step that names no actor is not a step -- and L-8 ITSELF HAS NO OWNER AND NO HOME. IT IS AN
INSTANCE OF ITSELF.**

### DISPOSITION -- NAMED, NOT BUILT

**The third home is NOT created here and `0.8.0_AE_CloudComp~C` is NOT authorized to create it.** Their
GO covers the 14-M-law skeleton only; I corrected their boundary line mid-build from two-way to
**THREE-WAY, naming the third family as UNHOMED** -- because a doctrine head whose first act is a
coverage claim that is false is worse than one that opens by naming its gap.

**Creating a third doctrine file reflexively would be law-count inflation one level up** -- the residual
already booked below -- **so the home decision is queued behind C8 artifact 1, and it is mine.**
