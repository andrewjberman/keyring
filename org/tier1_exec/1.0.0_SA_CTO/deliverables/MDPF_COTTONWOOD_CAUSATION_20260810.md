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

## ⬛ RESOLVED — THE TEN ACCOUNTS WERE RE-LABELLED AT BLACK DIAMOND (added 2026-08-10 ~1725Z)

**This section previously read "UNTRACED." It is now measured.** Andrew put a hypothesis to me at my
terminal: that the movement came from **our** flip to addressing non-"Opal Satellite" strategies via
their Opal-named constituent models. I tested it rather than agreed with it.

**`blackdiamond/cottonwood/silver/fact_model_assignment`, `date=2026-08-07` vs `date=2026-08-08`:**
**920 accounts BOTH days. ZERO added. ZERO dropped. EXACTLY TEN changed `strategy_name`:**

| account_id | 08-07 | 08-08 |
|---|---|---|
| 26704871 | `Passive 80` | **`Opal Satellite 80`** |
| 26724611 | `Passive 80` | **`Opal Satellite 80`** |
| 26725041 | `Passive 70` | **`Opal Satellite 80`** |
| 26725551 | `--` | **`Opal Ultra Short Term`** |
| 26725561 | `Passive 80` | **`Opal Satellite 80`** |
| 26725571 | `Passive 80` | **`Opal Satellite 80`** |
| 26741461 | `Core \| Satellite 98` | **`Opal Satellite 80`** |
| 26748351 | `Passive 60` | **`Opal Satellite 15`** |
| 27276551 | `--` | **`Opal Satellite 80`** |
| 27501251 | `--` | **`Opal Ultra Short Term`** |

**⇒ NOBODY ONBOARDED AND NOBODY LEFT. Cottonwood RE-LABELLED ten existing accounts out of
non-Opal-named strategies into Opal-named ones, and our `is_opal_name` substring test then matched
them.** The same ten accounts carry exactly the $5,299,757.63.

**⚠ CORRECTION TO MY OWN SECTION ABOVE:** I wrote *"ten accounts joined three Opal models"* and
*"an assignment change."* The second is right; the first is **imprecise in a way that matters** — they
did not join Cottonwood, they were re-labelled within it. An "onboarding" reading invites looking for
new money that does not exist.

### ANDREW'S HYPOTHESIS: RIGHT ABOUT THE OBJECT AND THE LAYER, WRONG ABOUT WHOSE FLIP IT WAS

The flip he named is **real and deployed** — `build_dim_model_portfolio.py` moved from a strict
parent-strategy Opal filter to a **leaf-grain disjunction**, deployed **2026-08-07T18:07:22Z**
(read from S3 object versioning + both versions' source).

**But it cannot be the delta, on two independent grounds:**
1. **IT LANDED BEFORE BOTH SIDES OF THE COLLISION.** Deploy history: `c9bb31…` (08-06T14:22:24Z) →
   `89ba62…` (08-07T18:07:22Z, the disjunction) → next change **08-10T13:16:15Z**. The 08-07 partition
   (22:46:54Z) and the 08-08 partition (13:00:39Z) both ran **`89ba62…`, byte-identical.**
2. **THE FLIP WAS A ~$0 NO-OP ANYWAY**, exactly as `0.4.0_DS_ClientPlatform` measured at the time —
   *"the $0.00 delta is the finding, because the binding filter is one layer UPSTREAM at the bronze
   harvest."* The leaf scan finds nothing because bronze never harvested the constituents.

**⇒ HIS FLIP IS HALF-BUILT AND CURRENTLY INERT: gold scans at leaf grain; bronze does not supply the
leaves.** The half that would make it real is the **Cottonwood model pull** — item 1, deprioritised
behind this repair at ~1620Z. That sequencing is unaffected; it is simply worth knowing the gold half
is already live and doing nothing.

### ⛔ AN INSTRUMENT THAT LIED — `comp-pipescript deployed` REPORTS A FALSE `STALE`
`comp-pipescript deployed build_dim_model_portfolio.py --pipeline mdpf` returns **STALE**
(`local 89ba6227…` vs `s3 38cefe56…`). **THE CODE IS IDENTICAL.** Measured: local carries **545 CRLF**
line endings, the S3 object carries **0**; after newline normalisation both files are
**byte-for-byte equal (28,527 bytes, same md5)**. Today's `13:16:15Z` "deploy" was a **line-ending
re-upload with ZERO code change**.
**An agent reading that STALE would redeploy a fix that is already live — and on a Windows checkout
this fires on EVERY script the tool checks.** Banked to the remediation register.

## WHAT IS *NOT* GROUNDED, STATED PLAINLY

- **WHY Cottonwood re-labelled those ten accounts** — an advisory decision at their end — is outside
  our instruments entirely. Not a defect and not ours to trace.
- **The pre-08-08 write clocks are irregular** (22:01Z, 13:35Z, 03:51Z, 22:46Z) and from 08-08 they
  are rigidly 13:00:39/40/41Z — the floor. Something changed about how this producer is invoked
  around 08-08. **I have not identified the actor for any pre-08-08 write** and am not naming one.
- **A series-continuity argument does NOT adjudicate which 08-06 figure is right** — I tried it and
  it fails. A ~$5.3M step exists between 08-05 and 08-07 under *either* reading; the two partitions
  merely disagree about **which day it lands on** (08-07 reads +0.07% then +4.57%; 08-08 reads +4.03%
  then +0.59%). *Recording the failed argument deliberately: it is exactly the plausible-looking
  reasoning that would have let someone pick a number.*

---

## ⬛ RULED 2026-08-10 ~1712Z — POINT-IN-TIME. HISTORY DOES NOT RESTATE.

**Andrew-direct, VERBATIM (relayed by `2.0.0_SA_COO`, record `@e82326bdb2`):**
> **(1)** *"Point-in-time, history does not restate."*
> **(2)** *"History 'may' be restated in the future when we have the bandwidth to do cosmetic work
> like this, but right now we need to be focused on current-day execution."*

**⇒ `value_date=2026-08-06` IS $133,914,199.99.** And the data vindicates the ruling: on 2026-08-06
those ten accounts genuinely sat in `Passive 80` / `Passive 70` / `--`. Restating would have
retroactively claimed $5.3M of Opal AUA on a day that money was in passive strategies.

**WHICH LIMB DIES — and it is not the one that was firing:**

| limb | verdict |
|---|---|
| **THE GUARD** (`:277-283`) | ✅ **RIGHT.** It was enforcing the ruled semantics before anyone had ruled them. It STAYS. |
| **THE TOLERATED PATH** (`by_vd[vd] = group[-1][3]`, "latest assignment_date wins") | ⛔ **THE DEFECT.** It silently restates. |

**THE REMEDY IS ONE LINE, and `group` is already sorted on `assignment_date`:**
```python
by_vd[vd] = group[-1][3]   # latest assignment_date wins  -> RESTATES (the ruled defect)
by_vd[vd] = group[0][3]    # earliest assignment_date wins -> POINT-IN-TIME
```
**Verified against the ruled number:** earliest-assignment for `value_date=2026-08-06` is partition
`08-07` = **$133,914,199.99**, exactly as ruled. `value_date=2026-08-07`'s pair is equal to the cent
either way, so it is unaffected. **The build emits, and it emits the ruled figure.**

⚠ **IT FITS HIS SCOPE QUALIFIER BY CONSTRUCTION:** fix-forward, touches no history, re-derives
nothing — **and it does not foreclose restatement**, since `[0]`→`[-1]` is the switch if he ever wants
it. ⛔ **DO NOT DELETE OR WIDEN THE GUARD.** Its *error text* is what needs correcting: calling this
*"drift between two runs"* framed a vendor re-labelling as corruption and cost most of a day.

**LANE:** the edit is `data/assets/scripts/gold/**` = `0.4.0_DS_ClientPlatform` by Rule 13, **not
mine**. Routed via COO. Not written here, not gated.

**SCOPE, NOT WIDENED:** he answered the question asked, which was about **cottonwood's** AUA history.
This is **not** applied to inflection, 49financial or global. *A RULED mechanism is more tempting to
carry across than an unruled one — sovereign ratification raises a finding's authority about the case
it was ruled on and changes nothing about its reach.*

---

## ~~THE OPEN CALL THIS RAISES — ANDREW'S, AND IT IS A BUSINESS CALL~~ *(ANSWERED ABOVE — retained for the reasoning that framed it)*

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
  ⬛ **THIS HOLD TURNED OUT TO BE LOAD-BEARING, not merely cautious: he chose POINT-IN-TIME — the
  exact reading a deletion would have destroyed, and `date=2026-08-07` is now the SOURCE OF THE RULED
  FIGURE.** Recorded because the counterfactual is the whole lesson: had I "tidied" the duplicate
  partition to clear the collision, the build would have emitted the restated $139.2M under the
  ruling that forbids it, silently, and with the evidence gone.
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
