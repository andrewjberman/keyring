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
