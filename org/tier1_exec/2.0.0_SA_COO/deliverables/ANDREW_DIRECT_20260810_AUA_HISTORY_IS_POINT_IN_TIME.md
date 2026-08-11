# ANDREW-DIRECT 2026-08-10 — OPAL AUA HISTORY IS **POINT-IN-TIME**. IT DOES NOT RESTATE.

**archetype:** COORDINATE
**Recorded by:** `2.0.0_SA_COO` · **Channel:** direct, at the COO terminal · **~2026-08-10 17:0xZ**
**Broadcast same turn:** `1.0.0_SA_CTO` · `0.0.0_AB_MSTR` · `4.0.0_SA_CRO` · `0.7.0_AE_CloudOps`
**Answers:** the blocking call raised by `1.0.0_SA_CTO` @a66080db54, carried to him from two terminals.

---

## 1 · VERBATIM

**The question put to him:**
> *When accounts are assigned into an Opal model, does Opal AUA history RESTATE, or is it
> POINT-IN-TIME?*

**His ruling:**
> **"Point-in-time, history does not restate."**

**And immediately after, the qualifier — which changes the REMEDY'S SHAPE, not just its label:**
> **"History 'may' be restated in the future when we have the bandwidth to do cosmetic work like
> this, but right now we need to be focused on current-day execution."**

### ⇒ READ BOTH TOGETHER. THE SECOND MESSAGE IS NOT A SOFTENING — IT IS A SCOPE INSTRUCTION.

| what he said | what it binds |
|---|---|
| **"Point-in-time"** | the **semantics** the builder must implement **now** |
| **"may be restated in the future"** | ⇒ **DO NOT FORECLOSE RESTATEMENT.** This is a **current ruling, not a permanent architectural commitment.** A remedy that makes restatement structurally impossible later would over-serve it. |
| **"cosmetic work like this"** | ⇒ **HIS CLASSIFICATION OF RESTATEMENT'S VALUE — cosmetic.** Nobody re-raises it as a correctness issue. |
| **"right now… focused on CURRENT-DAY EXECUTION"** | ⇒ ⛔ **THE REMEDY IS THE MINIMUM THAT LETS TODAY'S CYCLE EMIT. NOT A HISTORICAL RE-DERIVATION PROJECT.** |

> ⛔ **THE TRAP THIS CLOSES, AND IT IS A REAL ONE: "point-in-time" READS LIKE AN INVITATION TO GO
> REBUILD THE HISTORY CORRECTLY.** It is not. He ruled the semantics **and in the same breath told us
> not to spend bandwidth on history.** An engineer who hears "history is point-in-time" and starts
> re-deriving past partitions has inverted his instruction while believing they are executing it —
> **the same shape as the scoping-versus-priority trap he closed with "Nevertheless" an hour ago.**
> **Fix forward. Emit today. Leave history alone.**

---

## 2 · WHAT IT DECIDES, IN DOLLARS

`build_cottonwood_mdpf_slice.py` refuses on a `value_date=2026-08-06` collision between two
partitions carrying **different** Opal totals. The difference is **ten accounts joining three Opal
models** — an **assignment** change, not a revaluation (`1.0.0_SA_CTO` @a66080db54: Ultra Short-Term
8→10, Conservative Growth 96→103, Short-Term 107→108; 460→470 accounts; +$5,299,757.63; seven models
byte-identical; non-Opal residual constant to the cent).

| reading | 2026-08-06 Opal total | status |
|---|---|---|
| **POINT-IN-TIME** — on 08-06 those ten accounts were **not** in Opal models | **$133,914,199.99** | ✅ **RULED** |
| ~~RESTATED — history reflects today's roster~~ | ~~$139,213,957.62~~ | ⛔ **REJECTED** |

---

## 3 · ⇒ THE GUARD WAS RIGHT. THE **TOLERATED PATH** IS THE DEFECT.

CTO's framing: *"The builder currently has it BOTH ways… its tolerated path is 'latest
assignment_date wins' (restated) while its guard treats that same restatement as fatal. One has to
go."*

**His ruling picks which one.**

| limb | behaviour | verdict under this ruling |
|---|---|---|
| **THE GUARD** (`:269-292`, refuses on the collision) | treats restatement as fatal | ✅ **ALIGNED — it was enforcing the ruled semantics before anyone had ruled them.** It stays. |
| **THE TOLERATED PATH** ("latest `assignment_date` wins") | silently restates | ⛔ **MISALIGNED — this is the defect.** It must resolve the assignment in effect **as of** the `value_date`, not the latest. |

> **⇒ THE REMEDY DIRECTION IS NOW FIXED AND IT IS NOT "MAKE THE ERROR GO AWAY": the builder must
> resolve `dollar_value = f(value_date, assignment_date)` at the assignment state in effect AS OF
> that `value_date`.** The underlying defect stands as CTO diagnosed it — Rule 24(ii), **two grains
> collapsed onto one axis** — and the fix is to stop collapsing them, not to widen a tolerance.

⚠ **AND CTO'S REFUSAL TO DELETE THE 08-07 PARTITION NOW PAYS OFF.** They declined on the grounds
that deleting it *"would destroy the point-in-time reading before he has chosen one."* **He chose
point-in-time — the reading that deletion would have destroyed.** Recorded because it is the clearest
case today of a hold that looked like caution and was actually load-bearing.

---

## 4 · ⛔ SCOPE — SURFACED, NOT ADJUDICATED

**His words are general** — *"history does not restate"* — and the question he was answering was
about **Opal AUA history**, not about one builder. **I am applying it to the question asked
(cottonwood's AUA history) and NOT unilaterally extending it estate-wide.**

**If it is meant as an estate-wide semantics ruling for every AUA/holdings history, that is a
materially larger change** — it would bind inflection, 49financial, global and any other series that
re-resolves a roster. **That is his to confirm, not mine to infer.** Flagged rather than assumed,
because a sovereign phrase read wider than intended is how scope gets manufactured.

⛔ **AND IT MUST NOT BE APPLIED TO INFLECTION AS A MECHANISM.** Cottonwood is
**count-and-value-moving-together**; inflection is **count-present / value-NULL**. **Different
shapes, different firms, different vendors.** CTO's standing constraint on the inflection read is
that cottonwood's mechanism is given **to REFUTE, never to confirm** — this ruling does not soften
that, and if anything it raises the risk, because a ruled cottonwood mechanism is more tempting to
carry across than an unruled one.

---

## 5 · WHAT IT UNBLOCKS, AND WHAT IT DOES NOT

**UNBLOCKS:** cottonwood's remedy — it was the only thing gating it (mechanism established, remedy
blocked on this call, nothing emitted).

**DOES NOT UNBLOCK:**
- **inflection** — mechanism still unknown; `0.7.0_AE_CloudOps` is reading the 08-06 partition now.
- **global** — inherits inflection.
- **the repair as a whole** — by the bar he set and CTO accepted, cottonwood is repaired only when
  the remedy lands, **the SCHEDULED cycle emits** (ad-hoc is QA, never production evidence), and
  served platinum's `meta.generated_at` / `as_of_last` advance — **never the S3 mtime**, which is
  rewritten daily and looks fresh while carrying 08-07 content.

**PRIORITY UNCHANGED:** the repair remains the main fabric priority; Cottonwood **model-pull** work
remains sequenced behind it. ⚠ *And the two-Cottonwoods trap still stands — this ruling is about the
cottonwood **slice build inside the floor**, which is part of the repair, NOT about the deprioritised
model pull.*

*Recorded per the Andrew-direct law: durable + verbatim + broadcast, same turn.*
