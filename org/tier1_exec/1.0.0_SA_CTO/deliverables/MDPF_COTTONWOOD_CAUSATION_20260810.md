# Cottonwood causation — the (a)/(b) reads, run

**Author:** `1.0.0_SA_CTO` · **2026-08-10** · **Method:** ad-hoc QA reads (list + get, read-only).
Nothing written, nothing deployed, nothing repaired.

**Discharges** the item I named as mine and unstarted in `logs/2026-08-10/session_close_1345-1605Z.md`
Next-Step 1, and in my 151614Z message to COO: *"THE HONEST STATE: WE DO NOT KNOW WHY COTTONWOOD IS
A DAY BEHIND."*

We know now.

---

## THE ANSWER IN ONE PARAGRAPH

**Cottonwood's vendor data is NOT late. It is exactly at frontier.** Its newest `value_date` is
**2026-08-07** (Friday) — on a Monday, that is **zero trading days behind**, the healthiest possible
reading under the T-1 rule. The served view is stuck because
`build_cottonwood_mdpf_slice.py:280` **refuses the entire build** over a disagreement about a
*historical* date, 2026-08-06 — two days behind data it already holds. And the disagreement is not
corruption: **ten Cottonwood accounts were assigned into three Opal models between the Friday and
Saturday runs, and the Saturday run re-valued 2026-08-06 under the new roster.**

**Neither of the two causes suspected on 08-10 is operative.** Not the ingestion-cadence definitions,
not EventBridge ordering against the floor. This is the **third scope this window** where a correct
guard refusing was read as a timing failure.

---

## (b) WHAT THE FLOOR ACTUALLY READS FOR COTTONWOOD — answered at source

`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`, `ASSETS_BUCKET` = `opal-data-assets`,
`COTTONWOOD_GOLD` = `blackdiamond/cottonwood/gold/dim_model_portfolio/`.

The prefix is partitioned **by RUN DATE** (`date=<pdate>`). Each partition carries two date columns,
constant per partition (`:258-264` asserts exactly one of each, else `RE-KEY REFUSED`):

| column | meaning |
|---|---|
| `value_date` | the **market date** the dollars are as-of |
| `assignment_date` | the **roster date** — which accounts were in which model |

The re-key (`:269-292`) groups partitions **by `value_date` alone**, and where a value_date has more
than one partition it asserts the Opal dollar totals are equal. Unequal ⇒ `SystemExit`, verbatim:

> `VALUE_DATE COLLISION WITH DIFFERENT DOLLARS ... a differing-dollars collision is a DATA QUESTION
> (drift between two runs valuing the same snapshot), never silently chosen and never averaged.
> Refusing the build (CTO condition 1, 234639Z).`

## (a) WHAT THE PARTITIONS ACTUALLY CONTAIN — 13 of 13 read

`DENOMINATOR: 13 partition(s)`. Write clocks are UTC from `LastModified`; `value_date` is the
content vintage. **The two are deliberately reported side by side — R-23's trap is reading one for
the other.**

| partition (run date) | s3 write (UTC) | value_date | assignment_date | opal $ |
|---|---|---|---|---|
| 2026-08-05 | 2026-08-05T13:35:41Z | 2026-08-03 | 2026-08-05 | 132,521,716.52 |
| 2026-08-06 | 2026-08-07T03:51:52Z | 2026-08-05 | 2026-08-06 | 133,821,362.30 |
| **2026-08-07** | 2026-08-07T22:46:54Z | **2026-08-06** | 2026-08-07 | **133,914,199.99** |
| **2026-08-08** (Sat) | 2026-08-08T13:00:39Z | **2026-08-06** | 2026-08-08 | **139,213,957.62** |
| 2026-08-09 (Sun) | 2026-08-09T13:00:40Z | 2026-08-07 | 2026-08-09 | 140,029,264.18 |
| 2026-08-10 (Mon) | 2026-08-10T13:00:41Z | 2026-08-07 | 2026-08-10 | 140,029,264.18 |

**Every collision, not just the first** (the builder exits on the first, so this needed a re-derivation
without the `SystemExit`):

- `value_date=2026-08-06` — partitions `08-07` / `08-08` — **DIFFERING, build refuses**
- `value_date=2026-08-07` — partitions `08-09` / `08-10` — **EQUAL to the cent, tolerated**

## THE $5,299,757.63, ROW BY ROW — 3 of 10 models moved, and the accounts moved with them

| model | accounts 08-07 -> 08-08 | delta $ |
|---|---|---|
| Opal Ultra Short-Term Income | **8 -> 10** (+2) | +2,486,812.86 |
| Opal Conservative Growth | **96 -> 103** (+7) | +1,596,450.47 |
| Opal Short-Term | **107 -> 108** (+1) | +1,216,494.30 |
| *(7 other models incl. the $76.3M largest)* | unchanged | **0.00** |
| **TOTAL** | **460 -> 470 (+10 accounts)** | **+5,299,757.63** |

`is_opal` is unchanged on all 10 rows. `accounts_missing_value` is flat at 3.
The non-Opal residual is **constant to the cent** at $778,313.87.

**⇒ THIS IS AN ASSIGNMENT CHANGE, NOT A REVALUATION.** Ten accounts joined three Opal models, and
they brought their dollars. The `+139.6%` on Ultra Short-Term is the tell — a model does not double
on a market move.

**⇒ AND THE GUARD'S PREMISE IS WHAT FAILS.** Its text calls this *"drift between two runs valuing the
same snapshot."* It is not drift. It is a real business event — ten accounts onboarding to Opal
models — described by the instrument as corruption.

---

## THE MECHANISM, STATED AS A DEFECT

**`dollar_value` is a function of TWO dates. The re-key collapses on ONE.**

`dollar_value = f(value_date, assignment_date)`. Grouping by `value_date` alone and then asserting
equality treats `assignment_date` as noise **when it is part of the key**. Two partitions sharing a
`value_date` and differing in `assignment_date` are not expected to agree — they are *different
measurements by construction*.

That is **Rule 24 (ii), two grains on one axis**, in the collapse itself.

**The structural precondition is the RUN-DATE partitioning.** Because a partition is keyed by the day
the builder ran, every re-run — and **every weekend by construction** — mints a second partition for
a value_date that already has one. `08-09`/`08-10` demonstrate it harmlessly: two partitions, one
value_date, identical dollars, tolerated. The collision is not an exceptional event; it is the
*normal* state, and it only becomes fatal when the roster happens to change across it.

**⇒ So the two halves are separable, and only one of them is a surprise:**
- **structural / always present** — N partitions per value_date, from run-date keying
- **the trigger / this weekend** — the roster changed across one of those pairs

Nothing was wrong with the data on either side. The build stopped because it had two right answers.

---

## WHAT IS *NOT* GROUNDED, STATED PLAINLY

- **WHY the ten accounts appear on 08-08 and not 08-07** is UNTRACED. It could be a genuine
  Black Diamond onboarding, a vendor restatement, or our own harvest picking up a corrected file.
  I did not read the silver/bronze layer. `INFERRED`, not source-confirmed.
- **The pre-08-08 write clocks are irregular** (22:01Z, 13:35Z, 03:51Z, 22:46Z) and from 08-08 they
  are rigidly 13:00:39/40/41Z — the floor. Something changed about how this producer is invoked
  around 08-08. **I have not identified the actor for any pre-08-08 write** and am not naming one.
- **A series-continuity argument does NOT adjudicate which 08-06 figure is right** — I tried it and
  it fails. A ~$5.3M step exists between 08-05 and 08-07 under *either* reading; the two partitions
  merely disagree about **which day it lands on** (08-07 reads +0.07% then +4.57%; 08-08 reads +4.03%
  then +0.59%). *Recording the failed argument deliberately: it is exactly the plausible-looking
  reasoning that would have let someone pick a number.*

---

## THE OPEN CALL THIS RAISES — ANDREW'S, AND IT IS A BUSINESS CALL

**When accounts are assigned into an Opal model, does Opal AUA history RESTATE, or is it POINT-IN-TIME?**

- **Point-in-time** — on 2026-08-06 those ten accounts were not in Opal models, so 08-06 is
  **$133,914,199.99**. History is reproducible; a chart never moves under you.
- **Restated** — the accounts are in Opal models, so history reflects today's roster and 08-06 is
  **$139,213,957.62**. Comparisons are like-for-like across the current book.

**The builder currently has it BOTH ways, which is the incoherence:** its tolerated path is
`by_vd[vd] = group[-1][3]` — *latest assignment_date wins*, i.e. **restated** — while its guard
treats the very restatement that policy implies as a **fatal data error**. One or the other has to go.

⚠ **This rhymes with R-3 (2026-08-10), where Andrew ruled that re-parenting must be a RE-LABEL and
never a RE-DERIVATION.** Same shape one layer down. Flagged as a *resemblance for him to accept or
reject* — **not** applied as precedent. A ruling about category re-parenting is not a ruling about
account assignment, and reading it across would be exactly the inferred-scope-widening the fabric
forbids.

---

## A LEAD FOR `0.7.0_AE_CloudOps` — NOT A CAUSAL CLAIM

**2026-08-06 is now named by a third independent observation.** AE has: (1) inflection's 7 presence
disagreements, all on 08-06; (2) 08-06 missing from both the eclipse and orion feeds. This is (3) —
cottonwood's collision, at value_date 08-06.

And the *shape* of (1) and (3) is adjacent: both are **account_count and value disagreeing at
2026-08-06**. Inflection has count-present / value-None; Cottonwood has count-changed /
value-changed-with-it.

**Different firms, different vendors, different error classes.** AE's own standard applies and I hold
myself to it: *two* observations naming one date is a reason to look. Three is a stronger reason to
look. **It is still not a mechanism**, and I am not proposing one.

---

## DISPOSITION — what I am NOT doing

- **Not deleting the `date=2026-08-07` partition.** Deleting S3 objects requires Andrew's word
  (Agent Autonomy), and it would also destroy the point-in-time reading before he has chosen one.
- **Not relaxing the guard.** It did its job. `CTO condition 1, 234639Z` refused to let a $5.3M step
  be silently assigned to a day, and that was the correct call.
- **Not re-running anything.** The next scheduled floor will fail identically until the call is made.

**Cottonwood stays refusing until Andrew rules on restate-vs-point-in-time.** That is a real hold with
a named owner and a one-line ask — not a manufactured gate, and not something I can decide.

---

## Evidence

Re-derivation scripts (scratchpad, read-only, not committed):
`cot_rekey_read.py` (13/13 partitions, all collisions), `cot_collision_diff.py` (row-level).
Both re-implement `build_cottonwood_mdpf_slice.py:236-292` without its `SystemExit`.
Source read at `@3a5b625019`. Partition contents read live 2026-08-10.
