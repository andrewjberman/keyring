# Certifying a criterion that did not PASS — three classes, and what each certificate must carry

**Author:** `3.0.0_SA_CVO~Z` · **2026-08-28T04:0xZ** · **Applies to:** any proof-of-spec instance this
seat certifies where a criterion is not `PASS`

> **WHY THIS FILE EXISTS.** I set the requirements for these three classes **piecemeal, across three
> broker messages, over two hours** (12463, 12566, and this one). A requirement whose only carrier is a
> broker message is the stale-carrier failure — I have filed that finding three times tonight and then
> built my own certification standard that way. **This is that correction applied to my own rulings.**

---

## THE COMMON SHAPE, WHICH IS `0.4.0_DE_ClientPlatform~Z`'s AND IS THE REASON ALL THREE NEED A RULE

> **AN ACT GATED ON A FUTURE ARTIFACT IS RECORDED AT THE MOMENT IT IS IMPOSSIBLE, AND NOTHING
> RE-EXAMINES IT WHEN THE GATE LIFTS.**

⛔ **AND THE PART THAT MAKES IT HARD: THEY ARE INVISIBLE *BECAUSE* THEY WERE HANDLED CORRECTLY.** Each
record was accurate when written. **The set is the finding, not any member** — which is why no
individual review catches it and why the rule has to attach at *retirement time*, not at read time.

---

## THE CLASSES — three chosen, one that happens to you

| class | has an owner? | has a clock? | will it ever be met? |
|---|---|---|---|
| **WITHHELD** | no | no | **No — by ruling** |
| **RELOCATED** | yes | yes | **Yes — elsewhere** |
| **RETIRED-UNREACHABLE** | not yet | not yet | **Only if a named event occurs** |
| **VACATED** *(added 04:2xZ)* | n/a | n/a | ⛔ **It already "passes" — and that is the defect** |

⛔ **The first three are DISPOSITIONS A SEAT CHOOSES. The fourth is not chosen and nothing announces
it** — an unrelated lane refactors away the construct a criterion names, and the criterion silently
stops being able to fail. **It is listed here because a certifier meets it in exactly the same place:
a row that is not a real PASS.**

### 1. WITHHELD — the path is closed by ruling
*Specimen: `ETFS_INGEST.TO-7` `AC3`, terminal-withheld 2026-08-28T03:32Z.*

The certificate carries **four things or it is not a certificate**:
1. the withholding **named as a withholding, not a failure**;
2. its **author and date**;
3. **the conditions verbatim**;
4. **that the path is CLOSED** — meeting them is forbidden.

⛔ **(4) INVERTED FROM WHAT I FIRST WROTE.** I required "meeting the conditions REOPENS it," assuming a
withholding is always a deferral. **A refusal's conditions are a WARNING, not a route.** Here, meeting
them would mean rewriting a landed historical partition — *editing the evidence to satisfy the
instrument*. If the artifact ever needs correcting, **a new artifact alongside; history is appended to,
never edited.**

### 2. RELOCATED — a forward reference with an owner and a clock
*Specimen: `ETFS_SATELLITES.TO-5-DS` `AC6`, relocated to `TO-6-AE` `AC3`, fires ~07:00Z.*

`2.0.0_SA_COO~Z`'s distinction, and it is sharper than my original requirement:
> **A relocated criterion has an owner and a clock; a withheld one has neither.**

The certificate carries a **FORWARD POINTER THAT RESOLVES** — destination criterion, its TO, its
owner, its clock. **Without all four, "5 of 6, one relocated" is exactly as opaque as a bare 5/6.**

⛔ **AND THE RELOCATION IS NOT THE DISCHARGE. A relocated criterion is met by the FIRE, not by the
move.** Certify it discharged only when the destination is *measured*.
⚠ **The cross-TO gap this creates:** the origin TO closes and cannot reopen itself; the destination has
no reason to report into a disposed face. **One line at either end** — the destination's evidence names
the criterion it discharges — so a reader arriving from either direction finds the other.

### 3. RETIRED-UNREACHABLE — must name the event that lifts it
*Specimen: `ETFS_INGEST` `TO5-AC4`, retired because a field was not pulled. **The field is pulled now
and the retirement is false**, but it still reads CLOSED.*

`1.0.0_SA_CTO~Z`'s ruling:
> **A criterion retired as UNREACHABLE / N-A / KNOWN-UNREACHABLE must name, IN THE SAME FIELD, the
> EVENT that would make it reachable.** "Unreachable" without its lifting condition is a claim with
> **no expiry and no re-read trigger** — it retires the OBLIGATION along with the impossibility.

**Cost:** one clause at retirement time, written by the seat that already knows the condition.
**Non-application:** a criterion unreachable **BY CONSTRUCTION** needs no event **and should say so
explicitly** — the explicit "never liftable" is what distinguishes it from an omission.

### 4. ⛔ VACATED — the criterion's SUBJECT ceased to exist, and it now passes trivially
*Added 2026-08-28T04:2xZ. Specimen: `ETFS_POSITIONING` `POS-TO7-AC5`, found by
`0.4.0_DE_ClientPlatform~C` and routed to this seat **before** certification rather than after.*

**This is not one of the three above, and I did not have it.** The other three are all *dispositions a
seat CHOOSES*. This one **happens to a criterion while nobody is looking.**

`POS-TO7-AC5` reads: *"The `isEtfs ? null : dataAsOf` ternary is in the mode switch — the Models branch
must be provably untouched."* **That ternary no longer exists.** It was added at `ee90fa8e`
(`ETFS_POSITIONING.TO-3`) and removed at `7ebe38b0` (`ETFS_SATELLITES TO-3`), and the replacement is
strictly better — a mode-TOTAL `Record<PositioningMode, boolean>` that forces every future mode to
declare, where the two-way ternary would have silently bound satellites to the `else` branch.

```
comp-find 'isEtfs ? null : dataAsOf'   ->  0 hit(s) across 27546 files
```

>> ⛔ **AND ZERO IS WHAT A PASS LOOKS LIKE.** A criterion checked by the *absence* of a named construct
cannot distinguish **"the Models branch is untouched"** (intended) from **"the construct was refactored
away"** (actual) from **"someone deleted the file"**. **The criterion did not become FALSE when its
subject died — it became VACUOUS, and vacuous scores as PASS.**

⭐ **THE GENERAL FORM, WHICH IS THE PART WORTH KEEPING: A CRITERION THAT NAMES A SPECIFIC CONSTRUCT
BINDS ITSELF TO THAT CONSTRUCT'S LIFETIME.** A legitimate refactor by an unrelated lane silently
converts it from *testable* to *un-failable*, **with no edit to the criterion and no signal to anyone.**
This is the third ground-expiry on this record tonight and the first where the expiry makes the
criterion **easier** to pass.

**Certification rule:** ⛔ **I will not certify `POS-TO7-AC5` — or any criterion — on a zero-hit search
for a named construct.** A zero is evidence the construct is absent and **nothing else**.
**The remedy is RE-GROUNDING, not weakening, and the distinction matters:** `AC5`'s intent is fully
intact and fully testable — `REGISTERS_YANG_AS_OF.models === true` **IS** the Models branch, and it is a
*stronger* subject than the ternary was. **Text is `2.0.0_SA_COO~Z`'s to change; I am naming what I will
and will not accept as evidence.**
⭐ **And the right instrument is already precedented by the commit that CREATED the dead ternary** —
`ee90fa8e`'s own subject reads *"Models mode proven byte-identical by a RENDERED-DOM DIFF, NOT BY
INSPECTION."* `0.4.0_DE_ClientPlatform~C` chose that method unprompted. **A source diff cannot see a
render that changed for a reason other than the line you edited.**

### 5. ⛔ AND THE ONE THAT IS NOT A CLASS AT ALL — **`FAIL` USED FOR "NOT YET EXERCISED"**
*Added 2026-08-28T04:3xZ. Specimen: `ETFS_SATELLITES.TO-5-DS` `T5DS-AC6`.*

**The enum already has the right value and the row is filed on the wrong one.**

```
FAIL                          the criterion was evaluated and came out false
UNCOMPUTABLE-BY-CONSTRUCTION  "rides a NAMED later run (status_reason names it)"   <- the schema's own words
```

`T5DS-AC6` requires a schedule that has **EXERCISED**. The trigger exists, is ENABLED at
`cron(0 7 * * ? *)`, and was censused across **both** EventBridge planes with denominators printed
(139 Rules + 18 Schedules = 157, `NextToken` ABSENT on both, the `138 -> 139` delta corroborating that
the +1 *is* the satellites rule and not census drift). **Nothing failed. The fire has not happened.**
The row's own `status_reason` already contains exactly what the correct value requires — *"The first
scheduled fire is 07:00Z; only that fire can discharge it."*

⭐ **AND THE ROW IS OTHERWISE THE BEST-EVIDENCED ONE I HAVE READ TONIGHT.** It re-measured after a peer
applied the remedy, **corrected its own now-stale sentence** (*"THE TRIGGER HAS NOT REACHED DESIRED"* —
true at 01:2xZ, false after the apply), and **retained the superseded measurement rather than
overwriting it**, for a stated reason: *"the pre-apply zero is what made this criterion's FAIL a
measurement rather than an assumption."* **Everything moved with the state except the enum.**

>> ⛔ **WHICH IS THE NIGHT'S PATTERN IN A THIRD ARTIFACT CLASS: THE PROSE WAS UPDATED AND THE FIELD WAS
NOT.** I found it in my own channel records (4 instances, *both* directions), then in a TO face, now in
a proof-of-spec status. **A consumer filters on the enum. The prose is the carrier that does not
travel** — the same asymmetry as a subject line over a body.
⚠ **`FAIL` was defensible when first written** — the earlier census found 0 of 138 and 0 of 18, so
nothing existed. **The defect is not the original choice; it is that a re-measurement moved the world
and the field stayed put.**

**Certification consequence, and it cuts both ways:** ⛔ **I will not certify `TO-5-DS` complete under
`FAIL` OR under the corrected value** — 5 of 6, and **only the 07:00Z fire discharges AC6.** The value
change alters what a reader concludes, not whether the TO is done.
⛔ **And a `status` edit is a RE-CERTIFICATION trigger, not an amend-and-disclose** (the line drawn for
prose fields does not extend to the enum): the instance's own lane changes it, and I re-run.

---

## ⛔⛔ THE RULE THAT SUBSUMES CLASSES 4 AND 5 — **STATE THE MEASURED BASELINE AT CUT TIME**
*`1.0.0_SA_CTO~Z`, 2026-08-28T05:1xZ. It indicts three seats equally and I am one of them.*

`TX1DE-AC2` went through **three** revisions by three seats, each a genuine improvement to *which
values pass* — and the baseline was later measured at **403**:

```
                                  PASS set                      baseline (MEASURED 403)   verdict
original      2.0.0_SA_COO~Z      404, 403                      403                       PASSES AT BASELINE
amendment     2.0.0_SA_COO~Z      404, 403, 401                 403                       PASSES AT BASELINE
ruling        1.0.0_SA_CTO~Z      401, 403, 404 (fail=HTML-200) 403                       PASSES AT BASELINE
```

>> ⛔ **ALL THREE VERSIONS WERE VACUOUS. THREE SEATS REFINED *WHICH VALUES PASS* AND NONE ASKED *WHICH
VALUE THE BASELINE PRODUCES*.** Every revision made the PASS set more precise and none of them made the
criterion able to fail.

> ### **A CRITERION STATES ITS MEASURED BASELINE AT CUT TIME, OR IT IS NOT KNOWN TO DISCRIMINATE.**

**This subsumes the two classes I minted tonight.** VACATED (§4) and unscoreable-free-variable (§5) are
both *special cases of a criterion whose baseline was never measured* — a refactored-away subject and
an unnamed viewport are two ways of not knowing what the unfixed state produces. **The general form is
cheaper than either: measure the baseline once, at cut time, and write it into the criterion.**

⛔ **MY OWN SHARE, NAMED.** I supplied the `401 = FAIL` revision. I argued the discrimination test —
*"would the observation differ if the claim were false?"* — at the render and at my own storage
criterion in the same hour, **and did not run it on the PASS set I was editing.** Third instance
tonight of applying a rule everywhere except to the artifact I was authoring.

---

## ⛔ AND A SCORING TRAP ON `T5DS-AC6` THAT CHANGES WHAT I CERTIFIED IT DISCHARGES ON
*`0.7.0_AE_CloudOps~S`, third pass. Read at source on the function's own logs.*

```
describe-log-streams  cot-satellites-registry-producer  ->  EXACTLY ONE stream
  an ad-hoc --dry-run at 01:39:10Z ending:
  [ERROR] BLOCKED: no roster partition at .../rebalancer_models/2026-08-28/page_000.json
          (S3 said AccessDenied). REFUSING to walk
```

>> ⛔ **THIS LAMBDA HAS NEVER SUCCESSFULLY WRITTEN THE REGISTRY.** Both existing object versions are the
DS lane's authorised QA act — **a different principal.** So *"the producer already wrote it once"* is
**not available** as evidence for the 07:00Z fire; that seat had it queued as a positive control and it
evaporated on the read.
>> ⛔ **A LOG STREAM AT ~07:00Z PROVES INVOCATION, NOT SUCCESS — AND THE ONE STREAM THAT ALREADY EXISTS
IS A FAILURE.** My `TO-5-DS` certificate says AC6 "discharges on the 07:00Z fire." **CORRECTED: it
discharges on a SUCCESSFUL WRITE at that fire, and a stream is not one.**

⭐ **And the IAM hypothesis was raised as live and FALSIFIED rather than assumed either way**, on the
role's own policy documents rather than `comp-iam` (which models `(action)` and not
`(action, resource)`, so it FAILS GREEN):
`GetObject` on the roster prefix **ALLOW** · `PutObject` on the registry key **ALLOW** · `ListBucket`
**ABSENT** — and *that absence* is why S3 renders a **missing key** as `AccessDenied` rather than `404`.
⭐ **The two-principal split is what makes it a measurement rather than a story:** the same 2026-08-28
key returns **404** to that seat's own credentials and **AccessDenied** to the role. **Same key, two
principals, two errors — isolating `ListBucket` and nothing else.** Positive control: the 2026-08-27
partition exists at `06:00:43Z`, the landing time this rule's own description is built on.

---

## ~~A COROLLARY THAT BINDS MY CERTIFICATES~~ — **CORRECTED WITHIN THE HOUR; AS FIRST WRITTEN IT WAS A FALSE DICHOTOMY**

**As committed, this section read:** *"A PROSE EXPECTATION IS NOT AN OBLIGATION. If a TO expects an
act, it is a CRITERION or it is not expected. The criteria table wins."* — with `TO-P1-AE:239` as its
specimen.

⛔ **`0.7.0_AE_CloudOps~Z` read both lines at source and the specimen is not an instance of the rule:**
```
:239  "<DE lane> re-derives the fixture against the served artifact once one exists,"   <- what the DE LANE WILL DO
:240  "and reports disagreement as a DE finding. Nothing is owed to that lane by this TO."  <- what THIS TO OWES DE
```
**Two obligations pointing opposite ways. A TO can coherently record a peer's expected act while owing
that peer nothing.** Not a contradiction.

⛔ **AND MY DICHOTOMY WAS FALSE — there is a third state.** An act may be legitimately recorded as
**context** on one TO while being a **criterion** on another. Both offered remedies fail on that:
- **PROMOTE** puts a DE act inside an AE TO's acceptance — **a criterion whose assignee structurally
  cannot satisfy it**, leaving that instance unclosable through no act of theirs;
- **STRIKE** deletes the only durable record the act is expected at all — *"retiring the OBLIGATION
  along with the awkwardness"*, which is exactly what class 3 exists to prevent.

>> **CORRECTED FORM: an expectation needs A CRITERION OR A NAMED OWNER — and not necessarily on the TO
that mentions it.** Where the mention is on the wrong TO, that is a **PLACEMENT error, not a
contradiction**: the criterion goes where the act lives, and the mention stays as true context,
re-faced GATED-ON-EVENT.
**What survives unchanged:** I will not certify an instance against an expectation that has no
criterion *anywhere*, and I will not treat a prose mention as an owed act on the TO carrying it.
Ratified by `1.0.0_SA_CTO~Z` (12624), whose sharper form is: **an act gated on a future artifact needs
a carrier ON THE LANE THAT PERFORMS IT — recording it on the other lane's TO is exactly how it became
invisible; it was written down, correctly, in a place that owed nothing.**

### ⭐ AND THE ARTIFACT CARRIES A STRUCTURAL DISCRIMINATOR THAT SETTLES IT WITHOUT READING THE PROSE

I read the file rather than the quotation, and the placement reading is **visible in the markup**:

```
:217  <standing>          <- the cell lives HERE, at :239-240, two lines before this block closes
:242  </standing>
:244  <proof_of_spec>     <- the criteria table starts HERE, five lines later
:255  </proof_of_spec>
```

**The author already filed it as context, not as a criterion — and was right to.** That is a
*different instrument* from the sentence-semantics argument (`0.7.0_AE_CloudOps~Z`'s) and from the
two-parties argument (`1.0.0_SA_CTO~Z`'s), and it agrees with both. **What was missing was never a
criterion on THIS TO; it was a carrier on the DE lane.**

⛔ **A LINE/SENTENCE DEFECT THAT ALL THREE OF US COMMITTED — BUT NOT THE SAME ONE, AND MY FIRST
WORDING OF THIS PARAGRAPH WAS ITSELF AN INSTANCE OF IT.**

**As first committed this paragraph said "the quoted `:240` silently drops…" and attributed a
TRUNCATION to all three of us. `0.7.0_AE_CloudOps~Z` checked and that is FALSE OF THEM:** their 12609
§1 reproduced **both lines verbatim, the dropped clause included** — the mis-labelling came in the
sentence *after* the quote. **So there are two different failures here with two different remedies:**

```
TRUNCATION   the quote itself omits text        -> remedy: quote more
MIS-LABEL    the quote is complete, the PROSE   -> remedy: cite SENTENCES, not LINES
             attributes it to the wrong line
```
**`0.7.0_AE_CloudOps~Z` committed the second, not the first. I asserted the first about them without
reading their message** — I inferred their quotation from `1.0.0_SA_CTO~Z`'s rendering of it. ⛔ **That
is the exact defect this section documents, committed inside the correction of it: I reasoned about a
quotation I had not read.** Their words for why it could not stand: *"a doctrine file that overstates
its own instance count is exactly the carrier problem it is about."*

**What is true of all three: the line break falls MID-SENTENCE and `:240` carries both halves:**
```
:239  "...re-derives the fixture against the served artifact once one exists,"
:240  "and reports disagreement as a DE finding. Nothing is owed to that lane by this TO."
```
The quoted `:240` silently drops *"and reports disagreement as a DE finding"* — the clause that names
the DE act's OUTPUT. **It does not change the ruling; it strengthens it** (the two obligations are
adjacent *within one line*, which is precisely why they read as one). But the citation is by LINE and
the claim is by SENTENCE, and those do not align here. **I inherited the truncation from a correction
I was endorsing** — a corrected quotation is still a quotation, and I re-checked the ruling without
re-checking the citation.

## ⭐ AND THE SHARPEST STATEMENT OF THE CARRIER PROBLEM, WHICH IS `0.7.0_AE_CloudOps~Z`'s

> **A COMMITTED ARTIFACT IS THE OTHER CARRIER THAT CROSSES A SESSION BOUNDARY, AND UNLIKE A HUMAN IT
> DOES NOT HAVE TO REMEMBER.**

And the discriminator for *which* committed artifacts survive — which explains every carrier failure on
this record:

```
WATCH FILE        bound by DISCIPLINE  -- someone must REMEMBER to query it.   FAILED.
SCORER + BASELINE bound by NEED        -- a successor scoring AC4 HAS to run the scorer, and the
                                          baseline is useless without it.      SURVIVES.
```

**A carrier bound by need survives; a carrier bound by discipline does not.** That is why the 08-25
watch file was walked past by three seats and why a scorer committed beside its baseline is not.
⚠ **It does not replace telling Andrew** — it is the redundant limb.

### ⛔ AND THE SECOND CLAUSE, WHICH `0.7.0_AE_CloudOps~S` PAID FOR AND I DID NOT HAVE

**Binding a carrier by NEED is necessary and NOT sufficient — and the two properties trade against each
other in a way I missed.** That seat wrote a need-bound post-fire recipe for `T6AE-AC3`, then **ran its
own reads against the live world and found two defects in its own steps:**

```
STEP 3  excludes the QA write by `provenance: ad-hoc-QA`
        MEASURED: no `provenance` key at either layer; the token is absent from the bytes.
        -> THE CONTROL CANNOT FIRE IN EITHER DIRECTION. A reader who finds the marker absent and
           concludes "not the QA write, therefore the fire happened" files a FALSE PASS -- against
           the one criterion whose whole job is separating scheduled from ad-hoc.

STEP 4  "unchanged LastModified == NO SCHEDULED FIRE"
        TWO causes, routing to DIFFERENT LANES:
          no invocation record  -> the trigger did not fire.        AE fault. A real AC3 FAIL.
          an invocation record  -> it fired, the producer did not write. DS fault, NOT a trigger
                                   failure at all.
        -> a reader applying step 4 literally files "the schedule did not fire" and sends an
           investigation at a trigger the same document measured INTACT.
```

>> ⛔ **THE INVERSION: THE PROPERTY THAT MAKES A NEED-BOUND CARRIER SURVIVE IS EXACTLY WHAT MAKES A
DEFECTIVE STEP DANGEROUS.** A discipline-bound carrier nobody reads is inert — its bad steps cost
nothing. **A need-bound carrier is GUARANTEED to be executed, literally, by a cold reader with no
context to catch the flaw.** So binding by need does not reduce the cost of an insufficient step; **it
converts a dormant defect into an executed one.**

**COROLLARY, and it is now part of the rule:** a need-bound carrier must state, for **every** step,
*what a wrong reading of this step produces* — which verdict, and **whose lane it routes to.** ⭐ *"Each
is a stated verdict rule a cold reader can apply LITERALLY and get a confidently wrong answer"* is the
test. **And the defects were found only by RUNNING THE READS** — writing the recipe did not surface
them, and no review of the prose would have.
⚠ **The design was right and I am not softening that:** the failures are in the SUFFICIENCY of the
steps, not in the decision to write a recipe instead of a watch file.

## ⛔ THE CARRIER RULE THAT GOVERNS ALL THREE

**Do NOT create a watch file.** The precedent failed and is on the record:
`org/critical_paths/WATCH_20260825T1300Z_ETFS_FIRST_SCHEDULED_FIRE.md` **says of itself that nothing
queries it, that it is in no sweep and no startup step** — and three seats carried a superseded figure
straight past it tonight.

>> **These belong on the TO FACES, where boards already read.** Not a monitor, not an alarm, not a
checker — the moratorium is untouched.

⭐ **And the one carrier that crosses every session boundary in this fabric is Andrew.** No session
here lives to 13:00Z. That is the lesson the WATCH file paid for, and it is why a gated obligation gets
told to him directly rather than filed somewhere clever.

---

— `3.0.0_SA_CVO~Z`
