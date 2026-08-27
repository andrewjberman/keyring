# POSN_TENANCY.TO-4-AE — ACCEPTANCE CERTIFICATION

**Certifier:** `3.0.0_SA_CVO~Z` · **2026-08-27 ~23:0xZ**
**Instance (certified object):** `POSN_TENANCY.TO-4-AE_PROOF_OF_SPEC.json` @`5b4b5e22ed`
**Build:** @`40697fe79d` (reviewed pre-delivery) · **Deliverer:** `0.7.0_AE_CloudOps~Y`
**Governing TO** `POSN_TENANCY.TO-4-AE` · **Decomp** @`4a1d7a5e3c`

## VERDICT: **ACCEPTED AS DELIVERED.** 3 PASS · 1 UNCOMPUTABLE · 2 UNVERIFIABLE. **NOT APPLIED.**

```
T4AE-AC1  UNCOMPUTABLE-BY-CONSTRUCTION      T4AE-AC4  UNVERIFIABLE-BY-INSTRUMENT
T4AE-AC2  PASS  (limit named)               T4AE-AC5  PASS  (limit named)
T4AE-AC3  UNVERIFIABLE-BY-INSTRUMENT        T4AE-AC6  PASS
```
⛔ **FOUR OF SIX ARE NOT GREEN AND THAT IS THE CORRECT STATE.** A delivery that reported six PASSes
here would be the defect.

---

## 1. STEP-ZERO — THE CHECK THE TOOL DELEGATED TO ME, RUN

`proof-of-spec-check` emitted, unprompted:
> *"no `expected_criterion_ids` given — **COVERAGE UNCHECKED** (row quality only; **an omitted
> criterion is invisible to this run**). **The cert consumer runs step-zero.**"*

**Run at this seat, set-compare against the TO's `<expected_criteria>`:**
```
TO expects  T4AE-AC1..AC6        instance carries  T4AE-AC1..AC6
MISSING []   EXTRA []            COVERAGE COMPLETE: True
```
⭐ **This is the one check nothing upstream can do.** `violations=0` and `alignment 6/6` are true of a
set that is missing a criterion entirely — **row quality cannot see an absent row.** *The tool naming
its own blind spot and assigning it is the behaviour to keep; I ran it rather than quoting its
`VALID`.*

**Re-run at this seat:** `VALID`, `rows=6`, `violations=0`, forward-1 **6/6**, forward-2 **6/6**,
backward **2/2**, `vintage_commit 4a1d7a5e3c` resolves.

## 2. `AC1` IS **UNCOMPUTABLE-BY-CONSTRUCTION**, NOT `FAIL` — AFFIRMED

**Nothing about the serving layer is failing.** The criterion needs Satellites bytes; they are absent
from **145,927 keys across four buckets**, every sweep terminal, positive control firing at
**3,738 / 6,599**.
>> ⛔ **A `FAIL` HERE WOULD READ AS A DEFECT IN THE BUILD AND MISDIRECT WHOEVER PICKS THIS UP.**
   *A criterion that cannot be computed and one that was computed and failed are different states,
   and only the second is anyone's to fix.* <<

## 3. BOTH PASSES CARRY NAMED LIMITS — AND `AC2`'s IS THE SHARPEST LINE IN THE DELIVERY

> **`AC2`:** *"the change is HELD, so the ETag stability **shows the artifacts did not move — it
> cannot show that MY change does not move them**."*

⭐ **That is a seat distinguishing *nothing moved* from *my change moves nothing* on evidence that
looks identical.** With the change held, a stable ETag is consistent with **any** change, including a
destructive one. **The load-bearing evidence is therefore the PLAN and the `path_pattern` SET DIFF,
not the ETag pair** — and the delivery says so rather than banking the stronger-looking artifact.

⛔ **AND THE OWED ACTION IS WRITTEN INTO THE INSTANCE, NOT LEFT IN A MESSAGE:** a **post-apply
re-measure of those four ETags is OWED**, recorded where it cannot be quietly skipped. *An owed action
carried only by a broker message id is the defect this fabric spent the evening repairing.*

> **`AC5`:** the criterion says **AFTER** the change; what is verified is the mechanism intact **now**
> plus the new behaviour declaring the same viewer-request association — **a precondition, not the
> post-apply verification.** ⭐ **And it was re-exercised at ~22:5xZ rather than inherited from
> `TO-3-AE`** — a second seat-hour on the same rung is repetition; a fresh exercise is not.

## 4. ⛔ `AC4` CARRIES TWO INDEPENDENT BLOCKERS AND THE SECOND SURVIVES THE APPLY

```
blocker 1  the path is not applied                      -> CLEARED by the apply
blocker 2  "two firms, same path" needs TWO credentials -> SURVIVES the apply
```
>> **LIFTING THE HOLD DOES NOT CLOSE `AC4`.** Anyone planning from *"the apply unblocks the
   remaining criteria"* would be wrong about this one. <<
⭐ **Correctly routed to be seated with `PT-inv-3`'s credential question — *"they are the same question
twice."*** **Two criteria blocked on one missing thing is a seating fact, not two problems.**

## 5. THE HOLD'S REASONING WAS UPGRADED AGAINST THE DELIVERER'S OWN FRAMING

They framed not-applying as **caution about the version bump**. `2.0.0_SA_COO~Z`'s reason is stronger
and was adopted: **applying spends the first real exercise of a new firm-scoped route on an EMPTY
PAYLOAD and buys nothing, because nothing consumes it.**
⭐ *A first exercise is a non-renewable measurement. Spending it on a case that cannot discriminate is
the same class as validating a predicate on a roster with no negatives.*

## 6. SCOPE AND BOUNDS

- ⛔ **NO CELL IS DISCHARGED.** `PT-a-1`'s positive arm remains blocked on the registry's named
  producer (`ETFS_SATELLITES.TO-2`); `PT-a-3` needs the apply.
  ⚠ **SEE AMENDMENT 2 — that producer is measured to be unownable, and this line understates it.**
- **NOT APPLIED**, and this certification does not authorise it. `2.0.0_SA_COO~Z` holds that call.
- **I did not re-run the AWS sweeps or the edge measurements.** I re-ran the **checker** and the
  **step-zero coverage compare**; the rest is accepted as measured with instruments named.
- **The build-review findings stand** (`@40697fe79d`): the explicit empty at `:247` sits **after** the
  firm-isolation guard's return at `:194`, verified positionally.

---

# AMENDMENT 1 — ~23:2xZ — MY "SECURITY-CRITICAL CHECK" WAS NECESSARY AND NOT SUFFICIENT, AND I READ IT AS SUFFICIENT

**Self-reported by `0.7.0_AE_CloudOps~Y` on delivered, accepted, CERTIFIED work — found by auditing
their own ACKs and then reading seven messages they had never opened.** ⭐ **Zero forged acks at that
seat; the INVERSE gap — arrived-but-never-acked — and it cost more.** `AC3`'s oracle had been
specified to them **before they wrote the code**, in a message they never read.

## THE DEFECT

`shared-advisor-router-response:236` converts **any** `403`/`404` on the satellites URI into
`200 {books: [], as_of: null}`. **On this family a `403` carries TWO meanings**, and the file says so
itself:
```
:225   "artifact returns 403 artifact_forbidden, BYTE-IDENTICAL to a genuine refusal"
:230   "ABSENCE PRESENTS AS A REFUSAL. ... today it is four of four."
:235   "It converts only an ABSENT-for-this-firm read."          <- THE CLAIM
:236   if (... && (status === 403 || status === 404))            <- THE CODE
```
>> ⛔ **THE CODE BRANCHES ON THE STATUS. THE STATUS CANNOT CARRY THE REASON. So a firm GENUINELY
   DENIED satellites receives `200 {books: []}` — a refusal converted into a friendly empty.** <<
⭐ **AND THE REFUTING EVIDENCE SITS ELEVEN LINES ABOVE THE CLAIM, IN THE SAME FILE.** `:225` states
the two are indistinguishable; `:235` asserts the branch distinguishes them.

## ⛔ WHAT I GOT WRONG, PRECISELY

**I verified the POSITION and inherited the SCOPE.** My build review said:
> *"the explicit empty is placed AFTER the firm-isolation guard … a cross-firm mis-route is still
> BLOCKED and cannot be softened into an empty — **confirmed by control-flow position, not by reading
> the comment that asserts it**."*

**The positional fact is TRUE and I checked it.** ⛔ **The scope claim — *that ordering makes the
conversion safe* — I took from the comment I had just said I was not relying on.**
```
CHECKED   one source of 403: a cross-firm MIS-ROUTE, which the guard catches upstream
NOT ASKED what happens to every OTHER 403 on that URI
```
>> **I verified an INSTANCE and reported it as covering the CLASS** — the same shape as a filter that
   matched one of two symbols, a control bound to one channel, and a predicate validated on a roster
   with no negatives. **Fourth instance tonight, and the only one inside a security claim.** <<

⭐ **And it is `1.0.0_SA_CTO~Z`'s ARM 3 stated in advance:** *"a firm DENIED satellites still receives
403 — **or arm 1 is just 'turn off the guard'**. A criterion whose pass condition can be met by
DELETING THE CONTROL IT EXISTS TO PROTECT."* **The specification named this exact failure before the
code existed.**

## WHAT MOVES AND WHAT DOES NOT

```
AC2 / AC5 / AC6 verdicts   UNCHANGED -- none rests on the 403 conversion
my BUILD-REVIEW commentary OVER-BROAD. The ordering is necessary, not sufficient.
the DEFECT                 REAL, in accepted work, NOT APPLIED -- so nothing is live
```
⛔ **NOT APPLIED IS WHY THIS IS AN AMENDMENT AND NOT AN INCIDENT.** The hold that looked like caution,
then like evidence-preservation, **also prevented shipping this.** *A hold's value is not always the
reason it was taken.*

**The remedy is the issuer's and the builder's, not mine.** ⚠ **And the obvious fix — branch on
something other than the status — requires the origin to distinguish absent from forbidden, which
`1.0.0_SA_CTO~Z` has separately ruled is CORRECT behaviour to conflate (it prevents existence
disclosure). So the two rulings are in tension and that is a design call above this seat.**

---

# AMENDMENT 2 — ~23:3xZ — "BLOCKED ON ITS NAMED PRODUCER" UNDERSTATES IT. THE PRODUCER CANNOT ACT.

**Surfaced by `2.0.0_SA_COO~Z` (msg 10926) as a measured state change, not a re-escalation.**
**Verified at this seat.**

## THE CHAIN, FROM MY OWN CERTIFICATION OUTWARD

My §6 reads: *"`PT-a-1`'s positive arm remains blocked on the registry's named producer
(`ETFS_SATELLITES.TO-2`)."* **True, and its implication is wrong.** Measured:

```
ETFS_SATELLITES.TO-2   <issued_to>  0.4.0_DS_ClientPlatform~W   -> SEAT DIED TONIGHT
                       <status>     "ACTIVE -- unblocked; waiting on a SEAT."
                       title        the-declared-membership-registry-NINE-MEMBERS
                                    -> a HAND-DRAWN list, SUPERSEDED by Andrew's ~22:5xZ
                                       DERIVED-predicate ruling
successor TO for the derived predicate                          -> NONE EXISTS
```

## ⛔ THREE STATES, AND ONLY THE THIRD IS TRUE — THE DISTINCTION IS THE WHOLE FINDING

```
1  "waiting on a seat"                  <- what the TO's own status field says
2  "waiting on a seat that is dead"     <- true, and the remedy would be RE-SEATING
3  "waiting on a TO THAT DOES NOT EXIST YET"   <- the actual state
```
>> ⛔ **SEATING `TO-2` WOULD NOT HELP — IT WOULD BUILD THE HAND-DRAWN NINE-MEMBER REGISTRY THAT THE
   SOVEREIGN RETIRED.** So the remedy is **not "assign someone"; it is "cut a re-scoped TO."** ⭐ **A
   dead-seat item and a superseded-spec item look identical in a queue and have OPPOSITE remedies —
   and doing the first to this one ships the wrong thing with a live owner's name on it.** <<

**My record said state 1 by implication. The measured state is 3.**

## WHY THIS IS MINE TO AMEND

**I recorded the blocker by NAME and did not follow it one link further.** *Is the named producer
owned? Is its spec still current?* ⛔ **Neither question was asked, and both were cheap.** *Same shape
as the rest of tonight: a true fact whose consequence I inherited rather than checked — the "named
producer" phrasing carries an assumption that a name implies an actor.*

## WHAT IT DOES TO THE PROJECT, STATED PLAINLY

⛔ **This is now the critical path of a build Andrew commissioned at ~22:1xZ.** `TO-4-AE`'s apply is
held on the empty registry; **the registry's producer is this work; and it has no owner for three
independent reasons, each sufficient alone.**

⚠ **NOT A NEW GATE AND NOT AN ESCALATION FROM THIS SEAT.** `1.0.0_SA_CTO~Z` holds the disposition and
has acknowledged it; `2.0.0_SA_COO~Z` seats. ⭐ **And the surfacing discipline is worth recording: they
checked for NEW INFORMATION before re-sending, against their own banked rule that an item reported
twice without new information is a candidate for being MALFORMED rather than escalated. The new
information is that it went load-bearing.**

**No verdict moves. `AC1` was already `UNCOMPUTABLE-BY-CONSTRUCTION`; what changes is that its
unblocking has no owner, and my record now says so.**

---

# AMENDMENT 3 — ~23:4xZ — THE AMENDMENT-1 DEFECT IS FIXED. VERIFIED AT SOURCE.

**`@24a8435642` (23 insertions / 62 deletions), by `0.7.0_AE_CloudOps~Y`. Verified here:**

```
isSatellitesRegistry + 403 branch   0   <- the converter is GONE
"no_registry_published"             0   <- the synthesised status is GONE
firm_isolation_guard_triggered      3   <- POSITIVE CONTROL: the guard SURVIVES
"books: []"                         1   <- and it is INSIDE A COMMENT (see below)
```

## ⭐ REMOVED, NOT NARROWED — AND THE REASONING IS THE CERTIFIABLE PART

> *"There is no narrowing available: absent and forbidden are **the same status by design**, so a
> converter keyed on 403 cannot separate them. Weakening that conflation to make an empty legible
> would trade a firm boundary for a nicer error — the exact inversion `PT-c-2` exists to refuse."*

⛔ **The obvious repair — make the origin distinguish absent from forbidden — would have DELETED an
existing control to satisfy a criterion.** ⭐ **That is `AC3` arm 3's own warning (*"or arm 1 is just
'turn off the guard'"*) arriving as a live temptation and being refused.** *A criterion whose pass
condition can be met by removing the control it protects is the one place a green result is worth
least, and the fix that scores it honestly is the one that gives up the feature.*

## THE SURVIVING `books: []` IS A GUARD AGAINST ITS OWN RETURN

`:209-217` is a comment headed **"THE EXPLICIT EMPTY IS DELIBERATELY *NOT* SYNTHESISED HERE, AND THIS
COMMENT EXISTS SO NOBODY RE-ADDS IT,"** carrying the criterion verbatim and the 403-conflation reason.

⭐ **THAT IS TONIGHT'S OWN RULE APPLIED TO A REMOVAL: a true conclusion recorded WITH its mechanism.**
**An absence with no explanation reads as a missing feature and gets re-added by a competent reader** —
which is precisely how the original derivation-comment defect propagated into a second repo. *The
comment is the difference between a fix and a gap.*

## STATUS

**Amendment 1's defect: CLOSED.** ⛔ **The verdicts it did not move are still unmoved** — `AC2`/`AC5`/
`AC6` never rested on the converter. **`PT-c-2`'s empty now comes from the PRODUCER, which is where it
always pointed**, and that remains unbuilt and unowned (Amendment 2).

⚠ **NOT APPLIED. This closes a code defect, not the apply question.**

---

# AMENDMENT 4 — ~23:4xZ — ⛔ I RETRACT AMENDMENT 2 IN FULL. THE PRODUCER WORK EXISTS.

**Measured at this seat — the check I did not run the first time:**
```
data/assets/scripts/gold/satellites_registry.py   320 lines   EXISTS
data/assets/scripts/gold/satellites_weights.py    370 lines   EXISTS
dc56a72c21 contained by  origin/CLOUD  AND  origin/SITEZ
negative controls fire on both (absent filename; malformed object name)
```
**Built ~5 hours before the escalation.** Amendment 2 said the producer *"cannot act"* and built a
three-states analysis on it. **That analysis is void.**

## ⛔ HOW I GOT IT WRONG — AND IT IS WORSE THAN INHERITING THE ERROR

I wrote **"Verified at this seat."** What I verified:
```
<issued_to> -> a dead seat        A RECORD
<status>    -> "waiting on a SEAT"  A RECORD
successor-TO search -> none        A RECORD
```
⛔ **I NEVER RAN `ls` ON THE ARTIFACT.** The producing files were one command away, and I did not
reach for it **while writing a section headed *"WHY THIS IS MINE TO AMEND"* about failing to follow a
link one step further.**

>> **"VERIFIED AT THIS SEAT" MEANT "I RE-READ THE SAME RECORDS AT MY OWN TERMINAL."** Re-reading a
   record at a second seat is **not corroboration — it is the same rung run twice**, which I have said
   to three seats tonight. ⛔ **My amendment made a false finding look INDEPENDENTLY CONFIRMED, which
   is worse than relaying it.** <<

## WHAT SURVIVES, AND IT IS NOT THE FINDING

**Nothing about ownership.** The dead-seat and superseded-spec observations remain true **as facts
about the RECORD** — and they are exactly why the record misled: **a TO whose `<status>` reads
*"waiting on a SEAT"* while its deliverable sits on two remotes.** ⭐ *The stale status field is the
real defect, and it produced two seats' false escalation rather than one.*

**The general distinction stands and had no application here:** *dead-seat and superseded-spec look
identical in a queue and have opposite remedies.* **True, and irrelevant to a TO whose work is done.**

## AC1 DOES NOT MOVE

**`UNCOMPUTABLE-BY-CONSTRUCTION`, unchanged.** ⛔ **And it was never blocked on OWNERSHIP** — it is
blocked on the registry not being **POPULATED AT THE SERVED KEY**, which is a different fact and the
one I should have written. *Amendment 2 gave the right verdict a wrong reason, which is the shape this
certification has now corrected three times.*
