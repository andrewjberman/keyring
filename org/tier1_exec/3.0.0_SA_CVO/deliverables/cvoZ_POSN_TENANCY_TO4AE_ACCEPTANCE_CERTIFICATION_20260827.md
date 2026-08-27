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
