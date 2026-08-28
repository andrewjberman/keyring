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

## THE THREE CLASSES

| class | has an owner? | has a clock? | will it ever be met? |
|---|---|---|---|
| **WITHHELD** | no | no | **No — by ruling** |
| **RELOCATED** | yes | yes | **Yes — elsewhere** |
| **RETIRED-UNREACHABLE** | not yet | not yet | **Only if a named event occurs** |

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
