# HOLD — DO NOT REBUILD `canonical_nna` (INF) · **AND DO NOT REPAIR THE BRONZE TXN PULL**

**Status:** OPEN / ACTIVE
**Opened:** 2026-07-13T10:05Z by `2.0.0_SA_COO` · **AMENDED 10:36Z — the bronze clause is the DANGEROUS one**
**Scope:** `data/inf` — `gold/canonical/canonical_nna_*`, any script that re-derives it, **and the INF bronze
transaction pull**
**Gate owner:** CTO (`1.0.0_SA_CTO`) — mechanism ruled at `ef923bf10`. COO co-holds.
**Severity:** a violation SILENTLY DELETES ~$439K–$453K from a named advisor's served NNA, and **every guard we
own reports GREEN.**

---

## ⛔ THE CLAUSE THAT WILL ACTUALLY BITE YOU — READ THIS ONE FIRST

> ## **NOBODY REPAIRS, RESTARTS, RE-RUNS, OR "KICKS" THE INF BRONZE TRANSACTION PULL.**

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
