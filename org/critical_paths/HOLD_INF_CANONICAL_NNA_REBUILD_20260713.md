# HOLD — DO NOT REBUILD `canonical_nna` (INF) · **AND DO NOT REPAIR THE BRONZE TXN PULL**

**Status:** OPEN / ACTIVE
**Opened:** 2026-07-13T10:05Z by `2.0.0_SA_COO` · **AMENDED 10:36Z — the bronze clause is the DANGEROUS one**
**Scope — FUNCTIONAL, NOT BY FOLDER (amended 10:52Z; the `data/inf` scope was a HOLE and `0.7.0` found it):**
> **ANYTHING WHOSE EFFECT IS TO ADVANCE THE INF GOLD CHAIN, IN ANY REPOSITORY PATH.**
> Explicitly includes — **and these are NOT under `data/inf`**:
> - `infra/aws/terraform/inf-pipeline/lambdas.tf` (esp. `:96`) and **any `*_SILVER_STALENESS_CEILING_DAYS` value**
> - `infra/aws/terraform/inf-pipeline/eventbridge.tf` (the three `inf-gold-trigger` rules)
> - `infra/aws/lambda/inf-pipeline/inf-gold-trigger/` (the dispatch-env injection at `:266-270`)
> - `orion-gold-dispatch.sh` and the EC2 gold runner
>
> **An agent obeying a `data/inf` scope LITERALLY AND CORRECTLY, touching not one file under it, can open door 2
> from `infra/`.** *I fixed the ALARM axis to be functional and left the FILE-SCOPE line lexical — in the same
> document, four minutes apart.* **Scope by the CHAIN, never by the FOLDER.**

---

## 🕐 AND THE MODEL AT THE TOP OF THIS FILE WAS WRONG. IT IS NOT A KEYSTROKE. IT IS A CLOCK.

**I wrote: *"the countdown is not a clock, it is a keystroke, and it belongs to someone who does not know he is
holding it."* `0.8.0` read the deployed trigger (sha-matched to live) and falsified it.**

**`inf-gold-trigger` HAS NO BRONZE-FRESHNESS GUARD. NO DATA-STATE CHECK OF ANY KIND.**
(`infra/aws/lambda/inf-pipeline/inf-gold-trigger/lambda_function.py:176-345 @ 677dd4d72`; live
`CodeSha256` matches. **NOTE: a DECOY copy exists at `infra/aws/lambda/inf-gold-trigger/` — NOT deployed.**)

On `mode=full` it: validates the mode → **starts the EC2 box if stopped** → takes the dispatch lock →
`ssm.send_command` → **`bash orion-gold-dispatch.sh --chain full --bg`** → returns 200. **Every time.**
**And `mode=full` SELF-PRODUCES bronze + silver in-process** (CTO's own TF comment, `eventbridge.tf:266`).

> ## **THE CHAIN IS NOT WAITING FOR A HUMAN TO FIX BRONZE. IT IS RE-ATTEMPTING THE BRONZE PULL ITSELF, THREE TIMES A DAY, EVERY DAY.**
> ## **THE ONLY THING BETWEEN US AND THE DELETION IS THAT THE ORION API IS STILL DOWN.**
> ## **IF ORION RECOVERS ON ITS OWN — a vendor fix, a transient outage clearing, a rate limit resetting — GOLD RE-DERIVES AND $439,326.22 LEAVES THE SERVED SPINE WITH NOBODY HAVING TOUCHED ANYTHING.**

> **WE ARE NOT BEING CAREFUL. WE ARE BEING LUCKY, ON A SCHEDULE — AND THE CUSTODIAN OF THE CLOCK IS A THIRD-PARTY
> API'S UPTIME.**

**NOT YET GROUNDED (and nobody is asserting it):** that the chain currently aborts *at the bronze step*, and that
an Orion recovery would carry it through to the gold write. **`orion-gold-dispatch.sh` has not been read.** *The
disarm decision does not depend on that link* — whatever is stopping the chain lives **downstream of a trigger
that is armed and firing, in a script nobody has read, and it is being re-tested 3×/day.*

---

**Legacy scope line (superseded, kept for the record):** ~~`data/inf` — `gold/canonical/canonical_nna_*`, any
script that re-derives it, and the INF bronze transaction pull~~
**Gate owner:** CTO (`1.0.0_SA_CTO`) — mechanism ruled at `ef923bf10`. COO co-holds.
**Severity:** a violation SILENTLY DELETES ~$439K–$453K from a named advisor's served NNA, and **every guard we
own reports GREEN.**

---

## ⏰ **A SCHEDULED TEMPTATION LANDS WEDNESDAY 2026-07-15. PUT A DIARY ENTRY ON IT.**

```
2026-07-14 (Tue)   trading-days-behind = 2   ->  still within ceiling.  QUIET.
2026-07-15 (Wed)   trading-days-behind = 3   ->  3 > 2  ->  INF_API_SILVER_TXN *** BLOCKS. HARD. LOUD. ***
```

**On Wednesday the ceiling FINALLY ENGAGES, an alarm fires, and the obvious one-line fix is:**
```
TXN_SILVER_STALENESS_CEILING_DAYS = "10"      <- mirroring the PERF bump, green ledger, in infra/
```
**…which is DOOR 2, wearing a CTO-RATIFIED PRECEDENT (`20260706T1440Z_inf-perf-ceiling-bump`, CLOSED, GREEN).**

> ## **THE CONTROL WE ARE COUNTING ON BECOMES VISIBLE ON THE EXACT DAY IT BECOMES TEMPTING TO REMOVE.**

**CTO has REVOKED his own 07-06 ratification for TXN.** **DOOR 2 STAYS SEALED — any value, any lane, no
exceptions — and it is MORE important on Wednesday than it is today, not less.**

---

## 📏 THE NUMBERS ARE IN DIFFERENT UNITS. DO NOT RECONCILE THEM BY ADJUSTING ONE.

| number | unit | meaning |
|---|---|---|
| **$439,326.22** | **all 14 accounts (full Class B)** | ***the amount that LEAVES on a re-derive.*** **This is the at-risk total.** |
| $453,179.39 | the 9-account SUBTOTAL | larger than the 14-account total **only because the 5 extras net NEGATIVE (−$13,853.17)** |
| $52,604.80 | 3 accounts, 07-09 cohort | Patrick's phantom — the *served* misattribution, a different defect |

**All three are correct in their own unit.** *Reconciling two counts by adjusting one until they agree is how a
census stops measuring anything.*

---

## 🔬 "EVERY GUARD REPORTS GREEN" IS NOT RHETORIC. IT IS **MEASURED** (CVO, `3a1459644`, exercised).

```
BEFORE (served today)      sum(advisors) = $133,107,667.64   firm_total = $133,107,667.64   TIES.  GREEN.
AFTER  (Class-B deleted)   sum(advisors) = $132,668,341.42   firm_total = $132,668,341.42   TIES.  GREEN.

VANISHED: $439,326.22 from THREE NAMED ADVISORS
          peter_lee -$328,965.68 · patrick_scanlan -$84,213.71 · inflection_wealth_management -$26,146.83
```

> ## **A CONSERVATION INVARIANT CANNOT DETECT A CONSERVED LOSS.**
> **`sum(parts) == whole` catches REDISTRIBUTION and is STRUCTURALLY INCAPABLE of catching DELETION.**
> ## **A GUARD THAT TIES IS NOT A GUARD THAT SAW.**

**Every value-based, sum-based, or reconciliation-based guard in the estate is blind to this BY CONSTRUCTION.**
**Only a COVERAGE check can see it** — *"every account carrying NNA history yesterday still carries it today"* —
because **COVERAGE IS THE ONE PROPERTY DELETION CANNOT PRESERVE.**

**That detector is F7 — the one DELETED on a *"the coverage axis is owned elsewhere"* hand-off.** So:
> **DS's F7 coverage guard is the PRECONDITION for the hold-lift, NOT a parallel workstream.** Until it lands and
> is EXERCISED, **there is no instrument in the estate that can go RED on this class** — which means lifting the
> hold without it is not *"risk-managed,"* it is ***UNOBSERVABLE.***

**AND THE CONFIRMING EXPERIMENT IS RE-POINTED AT THE GUARD, NOT AT A RE-DERIVE (CVO struck her own proposal):**
> *"The thing I was predicting — the rows vanish — **IS THE HARM.** I would have been running the incident in
> order to verify the incident. **An experiment whose positive result IS the harm is not an experiment; it is the
> incident with a hypothesis attached.**"*

```
PRECONDITION : DS's F7 coverage guard lands FIRST.
EXPECTED     : it FIRES on 14 accounts / $439,326.22 and BLOCKS.
FIRES            -> the guard works; we caught the class before it ever served.
DOES NOT FIRE    -> THE GUARD IS BROKEN, and THAT is the finding.
Scratch prefix. Never prod. Zero risk. Tests the thing we actually need to trust.
```

---

## ⛔ THE CLAUSE THAT WILL ACTUALLY BITE YOU — READ THIS ONE FIRST

> ## **NOBODY REPAIRS, RESTARTS, RE-RUNS, OR "KICKS" THE INF BRONZE TRANSACTION PULL.**

### 🚨 **THERE IS A FOURTH DOOR, AND NO CENSUS BY RULE OR POLICY CAN SEE IT** (CTO~B, 11:03Z)

> **THE SILVER AGGREGATOR INVOKES `inf-gold-trigger` *DIRECTLY* — NOT VIA ANY EVENTBRIDGE RULE — AND IT FIRES
> `{"mode":"full"}` EVERY DAY AT 13:47Z.**

```
aws events list-rule-names-by-target   -> BLIND (it lists RULES; this is not a rule)
aws lambda get-policy                  -> BLIND (it lists SERVICE principals; an IAM-ROLE caller
                                                 needs no resource-policy statement at all)
THE LOGS CAUGHT IT. NOT A RE-READ. BOTH CENSUS INSTRUMENTS RETURNED CLEAN.
```

**SO THE TWO-RULE EVENTBRIDGE DISARM — THE THING I ASKED FOR AND CTO RATIFIED — IS *ITSELF* A PLACEBO.** *A fourth
caller walks straight past it.* **Third time today a disarm/census has been scoped by the wrong axis.**

> ## **THEREFORE THE LOAD-BEARING CONTROL IS A HOLD AT THE *CHOKEPOINT*, NOT AT THE DOORS:**
> ## **`INF_GOLD_DISPATCH_HOLD` on `inf-gold-trigger` itself — refusing EVERY dispatch BEFORE any side effect**
> ## **(no EC2 start, no lock, no SSM).**
>
> **Every path must traverse that function — the aggregator, both rules, and DOORS THAT DO NOT EXIST YET.**
> **And it holds EVERY MODE, not just `full`:** `INF_C_01` is in `CHAIN_GOLD_C`, so a `gold-c` run re-derives the
> protected artifact. ***A mode-scoped hold is walked past by choosing another mode.***
>
> The two rule-disarms ride along as **defence-in-depth in the same apply.**

**STATUS: AUTHORED, GATE-BLOCKED (correctly), NOT APPLIED.** `owned-paths` refused CTO~B's commit (`infra/aws` is
AE-lane). **He did not force it.** Routed to `0.7.0_AE_CloudOps` for SoD: adversarial review → `safe-commit` →
build-and-upload → `safe-apply` → 0-diff → **EXERCISE**. *With hours of margin there is no excuse for bypassing
SoD; **a wrong control is worse than a late one.***

---

### AND THE THREE DOORS BELOW ARE STILL SHUT — but they are the SYMPTOMS, not the chokepoint.

### THERE ARE **THREE DOORS** INTO THE SAME KEYSTROKE. GUARDING ONE IS GUARDING NONE.

| # | The door | Who walks through it |
|---|---|---|
| **1** | **Repair / restart / re-run `INF_API_PULL_TXN`** (bronze, dead since 07-10) | an AE clearing an obvious 3-day-stale P1 |
| **2** | **Clear, raise, or bypass the silver staleness BLOCK** — `convert_transactions_to_silver.py:128`, `STALENESS_CEILING_TRADING_DAYS = 2`, already breached and escalating to FAIL-LOUD-BLOCK | an engineer "unblocking" a blocked converter |
| **3** | **"Fix" the frozen mdpf / OPAL_ASSETS daily bucket** — a *different project*, with a *sovereign mandate*, that **never touches an INF file** | an agent on Andrew's own commissioned work |

> ### 🛑 **STRUCK 10:57Z — "THE SILVER STALENESS BLOCK IS THE SAFETY CATCH" IS FALSE. I WROTE IT; IT IS WRONG.**
> ```
> bronze/transactions last pull : 2026-07-10  = FRIDAY
> today                         : 2026-07-13  = MONDAY
> TRADING days behind           : 1           (Sat + Sun are not trading days)
> ceiling (:128)                : 2           ->  1 <= 2  ->  WARN. *** IT DOES NOT BLOCK. ***
> ```
> **THE CEILING IS NOT ENGAGED. IT IS NOT HOLDING ANYTHING.** `0.8.0` asserted it, **CTO RATIFIED IT AND SENT
> IT TO TWO AGENTS AS A RULING**, I put it in this file as a load-bearing safety claim — **and none of the three
> of us did three lines of arithmetic.** *Fifth symptom-promoted-to-mechanism of the day, and the first one
> laundered into a ruling other agents were told to act on.*
>
> **DO NOT RAISE THE CEILING ANYWAY. DO NOT ADD A BYPASS FLAG.** It is still a door (see door 2) — **it is just
> not currently the thing keeping us alive.** *Do not relax it on the strength of this correction; relax nothing.*

---

## ☠️ **WE DO NOT KNOW WHAT IS HOLDING THE LINE.**

**Measured, we know four things that are NOT holding it:**

| candidate | verdict |
|---|---|
| the trigger (`inf-gold-trigger`) | **NOT a guard** — no data-state check of any kind; fires 3×/day, 0 errors |
| the EC2 runner being stopped | **NOT a guard** — the trigger calls `start_instances()` on a stopped box |
| the silver staleness ceiling | **NOT ENGAGED** — 1 trading day behind, ceiling 2 → WARN, not BLOCK |
| the 14:47Z cron being "blocked" | **NOT a control** — it merely LOSES A RACE to a dispatch lock, **by 16 minutes.** *Luck with a TTL.* |

**And `bronze-complete` ITSELF dispatched `{"mode":"full"}` on 07-10, 07-11 AND 07-12** — the `_BRONZE_COMPLETE.json`
marker is still written even though the pull is dead. **THE CHAIN IS BEING DISPATCHED DAILY. GOLD IS NOT ADVANCING.
SOMETHING ELSE ABORTS IT AND NOBODY HAS READ IT.**

> ## **WE ARE NOT PROTECTED. WE ARE UNHARMED, AND WE DO NOT KNOW BY WHAT.**

**THEREFORE THE EVENTBRIDGE DISARM IS NOT DEFENCE-IN-DEPTH — IT IS THE ONLY CONTROL, AND IT IS RIGHT *BECAUSE* WE
ARE IGNORANT.** *You cannot rely on a guard you cannot name.* Every door works by letting the CHAIN PROCEED, and
the chain only runs if the trigger DISPATCHES. **Kill the dispatch and it does not matter what we failed to
understand.**

> ## **AND THE ACTOR IS NOT A HUMAN.**
> **The pulls are `tolerate`, not fail-fast. NO HUMAN IS REQUIRED. If Orion simply comes back up on its own, the
> chain proceeds and the deletion lands WHILE WE SLEEP.**
> **PROSE CAN GOVERN A HUMAN. IT CANNOT GOVERN A CRON.**
> **Every instrument shipped today — this hold, the broadcast, the door-2 seal — addresses an AGENT. The actor is
> a SCHEDULER. A HOLD IS NOT A CONTROL WHEN THE ACTOR CANNOT READ.**

## ⚠️ AND THE COVERAGE GUARD IS **NOT LIVE** — DO NOT READ DS'S COMMIT AS CLEARANCE

DS built it, it is **21/21 tested with proven-RED fixtures**, and it **fires RED on live data** (14 accounts /
**$439,326.22**, reproducing CTO's and MSTR's numbers **to the cent**, derived independently). **It is committed
(`d52ab4cbe`).** **AND IT IS NOT PROTECTING ANYTHING:**

```
safe-deploy on push:
  SERVE-HELD: INF_C_01.canonical_nna.py   -- committed but NOT served (AoR sentinel)
  DEPLOYED  : lib/nna_coverage_guard.py   -- the LIB only

s3://opal-data-inf/code/gold/INF_C_01.canonical_nna.py -> guard calls = 0
  (control on the retrieval: wc -l = 764 -> the file is REAL, so the ZERO is a REAL ABSENCE)
```

> **A GUARD IN THE CODE BUCKET THAT NOTHING CALLS IS A COMMENT WITH PARENTHESES.**
> DS: *"I tested the SOURCE and shipped the DEPLOYMENT."* His structural test asserts the call site exists **in
> the repo** — it cannot see that the repo file **never reaches the runner.**

**THE COLLISION (two CORRECT mechanisms):** the `DEPLOY-SERVE-HELD` sentinel that keeps the AoR fold off the
served path is now **HOLDING THE SAFETY GUARD HOSTAGE.** Both are right. **CTO ruling required** — nobody touches
the sentinel unilaterally (NEVER#2 / CTO~B gate).

**And every instrument an engineer owns is currently screaming at him to walk through door 1:** a dead pull, a
`ChainStepDegraded=1` metric firing nightly, a breached staleness ceiling escalating to FAIL-LOUD-BLOCK.
> **Every one of those instruments is RIGHT about the symptom and WRONG about the remedy.**
> *A bare "don't touch it" will lose that argument — and it will lose it to a competent, conscientious engineer
> doing exactly his job.* **That is why this file leads with the mechanism and not with the order.**

```
bronze/transactions          DEAD since 2026-07-10 09:43   <-- reads as an obvious, correct, urgent P1
silver/transactions          DEAD (starved by bronze)
gold/canonical               has not run since 2026-07-10 10:44
silver/api_dims/accounts_v2  STILL ADVANCING DAILY          <-- the roster feed is HEALTHY
```

**`inf-gold-full-on-bronze-complete` is EVENT-DRIVEN on bronze-complete.** Gold has not re-derived for exactly one
reason: **bronze never completes.**

> ### **THEREFORE THE REPAIR IS THE TRIGGER.**
> Fix the bronze pull and gold **immediately re-derives 1,389 of 1,410 partitions back to 2020**, against a silver
> snapshot that has **ZERO ROWS** for 14 accounts carrying **$439,326.22 of currently-served NNA**. Those rows do
> not move to a catchall — **they cease to exist** — and `sum(advisors) == firm_total` **still ties perfectly**,
> because the money leaves the advisor side and the firm side at the same instant.

> ## **THE GOOD FIX AND THE DESTRUCTIVE ACT ARE THE SAME KEYSTROKE.**
> **Nobody looks at a stale-data P1 and thinks "I must first check whether repairing this deletes an advisor's
> book."** That is why this clause is at the top of the file.

**INF STALENESS IS NOW A DELIBERATE STATE, NOT A DEFECT TO BE CLEARED.**

**AND THE FRESHNESS ALARMS ARE ACTIVELY DANGEROUS — THEY ARE INSTRUCTING AGENTS TO PULL THE TRIGGER.**
> *An alarm that instructs an engineer to perform the destructive act is worse than no alarm.*

### ⚠ SCOPE THE STOP BY **WHAT THE ALARM POINTS AT**, NEVER BY WHAT IT IS **CALLED** (0.8.0, 10:36Z)

**The first version of this order said "ignore all INF freshness alarms." THAT WAS A CENSUS-BY-MENTION BUG IN A
SAFETY ORDER, and `0.8.0` caught it inside four minutes — live, exercised:**

```
12 of 14  mdpf-cohort-freshness-stale-*  ARE IN ALARM RIGHT NOW
          incl. ...-inflection_models AND all nine 49f_* cohorts   (only etf_pfde / etf_pfoe are OK)
NONE of them has "inf" in its name.
```

**`mdpf-cohort-freshness-stale-inflection_models` IS an INF freshness alarm wearing a different prefix.** It fires
*because* of this freeze and it points its reader at the same repair. **An agent obeying the old STOP LITERALLY AND
CORRECTLY could still page on `mdpf-*`, conclude mdpf is broken, and go unblock the chain.**

> ## **THE RULE IS FUNCTIONAL, NOT LEXICAL:**
> ## **ANY alarm whose remedy is "refresh / unblock / repair / re-run the INF chain — OR ANYTHING DOWNSTREAM OF IT" IS UNDER THIS STOP, WHATEVER IT IS NAMED.**
> **Do not ask "does the alarm say INF?" Ask "would obeying it advance the INF chain?"** If yes: **DO NOTHING.**

**Named instances (NOT exhaustive — the functional rule above governs):**
`inf-gold-freshness-check-trigger` (18:30Z) · the NNA partition check (19:30Z) · **all 14
`mdpf-cohort-freshness-stale-*`** · **any OPAL_ASSETS "daily AUM bucket has not advanced" alarm.**

### AND THE HAZARD REACHES INTO PROJECTS THAT NEVER TOUCH AN INF FILE

**OPAL_ASSETS' daily emitter is FROZEN at `run_date=2026-07-10`** (`lambda_function.py:842,844 @ 677dd4d72` —
`run_date` comes from the SOURCE FILENAME, never the emit date). mdpf cannot advance past a gold that last wrote
07-10. **So from the OPAL_ASSETS lane the symptom presents as *"the Andrew-commissioned DAILY AUM bucket has not
advanced in 3 days"* — a clean, urgent, entirely legitimate P1 with a sovereign mandate behind it — and its repair
path runs straight into the $439,326.22 deletion.**

> **AN AGENT WORKING OPAL_ASSETS, IN GOOD FAITH, WOULD FIX THIS AND NEVER TOUCH AN INF FILE TO DO IT.**
> The blast radius of the "obvious repair" is **WIDER THAN THE INF LANE**. Scope this hold by the CHAIN, not by
> the folder.

**`0.8.0` is deliberately NOT building the obvious missing control** — a "daily AUM bucket has not advanced in N
days" staleness alarm — **because under this freeze that alarm has exactly one function: to page a future agent
into the destructive repair, with a green-looking justification and a sovereign mandate behind it.** *A loaded gun
with a helpful label.* **It ships when the hold lifts, WITH a `frozen-by-deliberate-hold` discriminator so it can
never again mean two things.** *That is the correct call and it is recorded as such.*

**THE REAL CONTROL, REQUESTED OF CTO (`103534Z`), NOT YET LANDED: DISARM `inf-gold-full-on-bronze-complete`.**
The trigger is **already effectively dead** (bronze never completes), so **disabling it is a NO-OP TODAY and a
REAL CONTROL TOMORROW** — zero behavioural change, fails safe, trivially reversible, and it lets an AE repair
bronze *correctly* without holding a loaded gun. **Then this bronze clause can be LIFTED.** *We should not have to
keep a pipeline broken to keep the data safe.* **Until it lands, prose is the only thing holding this — and prose
is what we watched fail all day.**

---

## THE REBUILD HOLD

> **NOBODY RUNS A FULL REBUILD, A BACKFILL, OR A DATE-RANGE RE-DERIVE OF `gold/canonical/canonical_nna_*`
> UNTIL THE SILVER `rep_id` NULL IS FIXED AND A COVERAGE ASSERTION IS IN PLACE.**

This includes: `INF_C_01.canonical_nna.py` run over any historical range, `_rebuild/` sweeps, "re-run the chain
from date X", and any repair that re-derives an old partition. **A normal forward nightly on TODAY's partition is
not what this hold is about — but if you are about to re-derive a PAST date, STOP.**

An ad-hoc gold run to "validate" or "just refresh" the numbers is the exact action this hold forbids
(and NEVER#4 already forbids ad-hoc gold runs for validation).

## WHY — MEASURED, NOT INFERRED

`INF_C_01:444-464` derives `advisor_key` by mapping **`rep_id` on the TRANSACTION ROW** (`:375-380` map:
`3`→firm, `6`→joe, `11`→patrick_scanlan, `12`→peter_lee). **Roster presence plays NO part in the derivation**
(the 2026-07-13 "roster departure" mechanism was ruled and then FALSIFIED — see `ef923bf10`).

Twelve accounts are absent from today's roster and carry NNA. Per-row census over **1,410 partitions,
124/124 rows classified**, S3 `LastModified` read in **Z**:

```
silver/transactions/2026-07-10.parquet   written 13:44:22Z   <- 3 accts present w/ rep_id=<NA>; 9 accts ZERO rows
gold canonical_nna partitions            written 14:41:xxZ   <- ~1 hour LATER

PHANTOM(3)  560/703/1225   rebuilt_after_silver = TRUE   113/113 rows   -> stamped inflection_unmapped_rep
SURVIVOR(9) 77/100/302/…   rebuilt_after_silver = FALSE   11/11 rows    -> still stamped with the REAL advisor
                                                                            (partitions last written 05-13/06-02/06-29)
```

**PERFECT SEPARATION. The discriminator is not the account, not the advisor, not the roster — it is WHETHER THE
REBUILD TOUCHED THE PARTITION.**

> **RE-DERIVATION IS THE ACT THAT DESTROYS THE ATTRIBUTION.**
> **The 9 survive ONLY because nothing has re-derived them yet. "Untouched" is not a safety property — it is a
> countdown.** The defect is PROGRESSIVE and advances one partition at a time.

## AND THE FAILURE MODE FOR THE 9 IS DELETION, NOT MISATTRIBUTION

- The **3** ARE in silver with `rep_id = <NA>` → they produce a row → `.fillna()` → **catchall**. The money stays
  in the firm total, visibly wrong. **This is the recoverable case.**
- The **9** are **NOT IN SILVER AT ALL — 0 rows.** A re-derive of their partitions produces **NO ROW**.
  → **Peter Lee's $368,965.68 and Patrick Scanlan's other $84,213.71 do not move. THEY CEASE TO EXIST.**

## >> AND THE RECONCILIATION CANNOT SEE IT <<

`sum(advisors) == firm_total == raw gold` currently ties to **0.00**. That is TRUE and it is **NOT reassurance.**

**A deleted row leaves the ADVISOR side and the FIRM side AT THE SAME INSTANT.** Both totals shrink together, so:

```
sum(advisors) == firm_total     -- STILL TRUE. STILL 0.00. FOREVER.
```

> **A RECONCILIATION THAT TIES BOTH SIDES OF THE SAME OMISSION IS NOT A RECONCILIATION.**

The co-signed invariant (`sum(advisors) + unattributed == firm_total`) is **blind to this by construction** — it
was built to catch money moving *between* buckets. **This is money leaving the building, and every bucket agrees
it was never there.** *An invariant that only ever compares the artifact to itself will certify any consistent lie.*

**The only instrument that can see it compares the served total against a PRIOR VINTAGE of itself, or against a
source the pipeline does not derive from.**

## ⚑ PRE-REGISTERED PREDICTION — WRITE THE NUMBER DOWN **BEFORE** THE RE-DERIVE RUNS (CVO, `5be383519`)

> ## **A PREDICTED NUMBER-MOVE IS A VERIFICATION. AN UNPREDICTED ONE IS AN INCIDENT.**

The re-derive that LIFTS this hold will do **two correct things at once**, in **opposite directions**, and only
one of them is the one everybody is watching for.

### 🛑 THE FIRST VERSION OF THIS PREDICTION WAS WRONG BY 30× AND IN THE WRONG DIRECTION. IT IS REPLACED.

**I committed `+$13,853.17 / peter_lee +$40,000` here at 10:47Z. CVO falsified it at 10:50Z by measuring, and
`REPLACED IT HERSELF`. If you are reading a cached copy of that number, DISCARD IT.** *Checking a correct rebuild
against the old number would have HALTED IT as a regression — a false FAIL with a destructive remedy, which is the
class we spent the entire day on.*

**WHY IT WAS WRONG — and it kills my own claim, not just hers:** I told CTO *"the 9 survivors SURVIVED a
post-silver re-derive."* **CVO measured the `LastModified` of EVERY partition carrying EVERY one of the 14:**
```
COO's 9  -> partitions in the 07-10 rebuild: 0     never touched: 11
CVO's 5  -> partitions in the 07-10 rebuild: 0     never touched:  9
                                                   ------------------
                                                   20 of 20 NEVER TOUCHED
```
> **"THE 9 SURVIVED THE REBUILD" IS FALSE. THEY DID NOT SURVIVE ANYTHING — NOTHING EVER RE-DERIVED THEM.**
> **That claim was the ONLY evidence anyone had that a re-derive does NOT delete a feed-absent account.**
> **IT IS GONE. NOTHING NOW CONTRADICTS THE DELETION MECHANISM.**

**AND THE 14 ARE ONE POPULATION, NOT TWO.** COO's 9 + CVO's 5 were the same class found through two different
doors. All 14 are **roster-absent AND feed-absent.**

**CORRECTED EXPECTED DELTA — ACCEPTANCE CRITERION:**

```
THE RE-DERIVE DELETES ALL FOURTEEN.

    NET CHANGE TO SERVED NNA HISTORY:   -$439,326.22
    peter_lee:                          -$328,965.68
```

**WHY:** those 5 accounts' entire served NNA lives in **8 partitions the 07-10 rebuild never touched**
(all written 2026-05-13 06:52Z; 8 of 8). They have **ZERO rows** in the canonical snapshot `INF_C_01` derives from
(`:306` — single-snapshot source-selection, over ALL of history). **When the re-derive reaches those partitions,
those rows cease to exist — and that is CORRECT: a number the source cannot produce should not be served.**

> **BOTH OUTCOMES ARE RIGHT. THAT IS EXACTLY WHY IT IS DANGEROUS.**
> The same delta lands on the same night either way. The only variable is whether it reads as
> *"the re-derive did what CVO said it would, to the cent"* — or as
> ***"peter_lee's historical NNA moved $40,000 and nobody knows why."***
> **We have spent this entire day on numbers that moved without an owner.**

**IF THE DELTA IS ANYTHING OTHER THAN THE ABOVE, *THAT* IS THE ALARM.** Halt and restore from the backup.

**AND THIS MAKES THE PREDICTION FALSIFIABLE FOR FREE.** CTO wanted a dry re-derive of one untouched partition and
said it needed an owner. **The hold-lift re-derive IS that exercise, at zero extra cost** — provided someone reads
the result against a number written down **in advance**. *It stops being a prediction and becomes a measurement.*
**Safe:** 8,805 gold objects backed up + ETag-verified (0 missing / 0 mismatched), so a wrong prediction is
recoverable.

> **THE GENERAL SHAPE (CVO):** *"F2 × F7 taught us that per-finding triage is structurally blind to COMPOSITION.
> This is the same thing between two findings of MINE, in two different scripts, filed an hour apart, that I never
> held up against each other. Individually: 'a collapse to repair' and 'some stale rows.' Jointly: a single
> re-derive that changes served advisor numbers in TWO DIRECTIONS AT ONCE, one of which nobody is expecting."*
> **ENUMERATE THE INTERACTION, NOT JUST THE FINDINGS.**

---

## TO LIFT THIS HOLD

1. **Ground and fix the upstream defect: WHY is `rep_id` NULL in `silver/transactions` for accounts 560/703/1225?**
   (3,283 rows between them, NULL on every row, re-firing nightly.) The silver converter has NOT been read by
   anyone as of this writing — **do not guess it.**
2. **A COVERAGE assertion, not just a key-validity assertion.** A *vanished* account has no key to be invalid.
   Assert: *every account with NNA history yesterday still has it today* — and RAISE. **This is F7**, currently
   SERVE-HELD with the AoR bundle. **F7 would have caught both the 07-09 phantom AND this deletion class.**
3. **A vintage comparison on the served spine** (today's `advisor_nna_canonical.json` vs yesterday's), because the
   internal reconciliation provably cannot.

## NOTE

**INF gold has been STALLED since 2026-07-10** (platinum last written 07-10; `data_as_of` 07-09). **That stall is
currently the only thing holding this line — AND A STALL IS NOT A CONTROL.** It will end, and when it does this
hold is the only thing standing between us and a silent half-million-dollar deletion.

*Filed by COO after a reconciliation run to CONFIRM a claim instead refused to tie. Mechanism ruled by CTO
(`ef923bf10`) after he opened the script none of the four of us had read.*
