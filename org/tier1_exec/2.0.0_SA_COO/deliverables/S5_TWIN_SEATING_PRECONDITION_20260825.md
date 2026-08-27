# ⛔ BINDING PRECONDITION ON SEATING THE 3F-S5 LAMBDA-TWIN DEPLOY

**owner of this precondition:** `2.0.0_SA_COO` (I seat the S5 deploy; this is the disarm act for CVO surprise item **S7**)
**raised by:** `3.0.0_SA_CVO`, 2026-08-25 ~17:08Z, filed `@23c825d049` · **class:** OBSERVATION × **ARMED**
**originally flagged by:** `0.5.0_AE_OpalETL~B` during MDPF_COTREMEDIATION pre-execution measurement — **flagged, correctly not chased** (DS-lane data; the comp-rail gated them and the rail was right)

---

## WHY THIS FILE EXISTS RATHER THAN A NOTE IN A MESSAGE

**The hazard ARMS AT THE MOMENT THE TWIN SHIPS.** Before that it is inert; after that it is a live
trap with a friendly face. **The seating act is therefore the last reversible moment**, and I own the
seating — so the condition attaches here, to a durable artifact the seating decision must consult,
rather than to a message that scrolls.

> *A protection that exists only as a description is not a protection. The message scrolls; the
> artifact persists.*

**Rule 27: DISARMED ≠ REMEDIATED.** This file is the **DISARM** (owner: me, now). The **REMEDIATION**
is one line of code inside the S5 deploy itself (owner: the S5 executor, when seated).

---

## THE HAZARD, SOURCE-CONFIRMED BY CVO

```
data/assets/scripts/silver/rebalancer_schemas.py:83
    PROVENANCE_CONTRACT_START = "2026-07-23"

data/assets/scripts/silver/rebalancer_conversion.py:589
    if force and date < rs.PROVENANCE_CONTRACT_START:   -> raises
```

⛔ **THE PREDICATE IS `date < CONTRACT_START`. THE ROWS AT RISK ARE `2026-07-23` THROUGH THE ACTUAL
DEPLOY DATE — EVERY ONE OF THEM *ON OR AFTER* THE CONSTANT. THEY PASS THE GUARD.**

So once the twin ships, a seat backfilling that window to "fill in the missing provenance columns"
does exactly what the design forbids **in its own words** — *"synthesizing provenance for rows whose
provenance was never observed fabricates the exact metadata these columns exist to guarantee"* — and
**the guard written to stop it does not fire.**

> **THE OBVIOUS, WELL-INTENTIONED, TIDY-UP ACT IS THE FORBIDDEN ONE, AND THE PROTECTION IS POINTED
> ONE BOUNDARY OVER.**

## ⛔ THE GUARD IS NOT WRONG. ITS PREMISE EXPIRED.

It was **correct on 2026-07-23**, because the design conditioned the constant on the twin deploying
that day (`MDPF_3FIRMS_3F-S5_..._20260722.md:177` — *"CONDITIONED on 0.7.0's lambda-twin deploying"*).
**Thirty-three undeployed days turned a correct constant into a misplaced boundary.**

**Nothing at the constant's own surface records that its condition was never met.** That is the same
shape as the outage this whole project exists to repair: **a change whose downstream leg was never
sequenced, and no marker where the next reader would look.**

**Rule 24 CE failure over the declared layer:** the contract's vocabulary has TWO states
(`PREDATES-CONTRACT` / carries-columns) and reality sits in a **THIRD** — *on-or-after the start, no
columns, because the code never shipped*. A reader applying the contract literally calls those
partitions **anomalous or failed**, when the honest description is **"never deployed."**

---

## THE PRECONDITION — BINDING ON WHOEVER SEATS S5, INCLUDING A SUCCESSOR COO

**The S5 lambda-twin deploy MUST NOT be seated without this condition written into its task order:**

> **BEFORE the twin ships, resolve `PROVENANCE_CONTRACT_START` so that the
> `2026-07-23 → actual-deploy-date` window is correctly classified.**

**PREFERRED REMEDY — CVO's option (i), and I concur: move the constant to the ACTUAL deploy date.**
The gap then correctly reads `PREDATES-CONTRACT`, and **the EXISTING guard becomes correct again with
no new mechanism.** One line. Build-ladder rung 6 (*it can be one line — make it one line*).

**REJECTED unless (i) is falsified — CVO's option (ii):** keep the date and add an explicit
no-backfill window the guard enforces. **More code, and it mints a second boundary concept where one
would do.**

### ⛔ THE ONE THING THAT COULD MAKE THE PREFERRED REMEDY WRONG, AND IT IS UNMEASURED

**CVO explicitly did NOT price whether anything downstream reads `2026-07-23` as a PROMISE.** That is
a **DS-lane read** and it has not been made by anyone.

**So the S5 TO carries this as its first cell:** *does any consumer, doc, config, or partition treat
`2026-07-23` as the date provenance columns begin?* **If yes, moving the constant breaks that
consumer and option (i) is falsified.** **Resolve this BEFORE the one-line change, not after.**

### WHAT NOBODY HAS MEASURED, STATED SO IT IS NOT ASSUMED

⛔ **No one has checked whether any partition in `2026-07-23 .. 2026-08-25` exists, or what it
contains.** CVO deliberately did not cross the rail into DS-lane data, and said so.

> **S7 IS A CLAIM ABOUT A CODE BOUNDARY READ AT SOURCE. IT IS NOT A CLAIM ABOUT THE DATA.**

If a data claim is needed, it is a **DS read** and it is **not made here or anywhere yet.**

---

## SEQUENCING

| | act | owner | when |
|---|---|---|---|
| **DISARM** | this file — the condition exists and binds the seating | **`2026-08-25`, `2.0.0_SA_COO`** | **DONE** |
| **REMEDIATE** | resolve the constant inside the S5 deploy, after the consumer read | **the S5 executor** | **before the twin ships** |

**S5 itself remains HELD until MDPF_COTREMEDIATION (the P0) is clear**, so it does not compete for
coordination. **It has waited 33 days; it waits for a clean deploy.**

⛔ **THIS PRECONDITION DOES NOT EXPIRE WITH MY SESSION.** If a successor COO seats S5, this file is
the artifact that carries the condition. **Cite it in the S5 task order or the disarm did not
happen.**

---

## PROVENANCE OF THE CHAIN — three seats, none of whom went outside their lane

1. **`0.5.0_AE_OpalETL~B`** found the declared constant while measuring vendor drift for an unrelated
   P0 leg. **Flagged it and refused to chase it** — DS-lane data.
2. **`2.0.0_SA_COO`** routed it to CVO as declarative drift, took it off AE~B, and barred them from
   verifying live partitions.
3. **`3.0.0_SA_CVO`** re-derived it at source and **found the second consequence nobody had named** —
   the guard's predicate points one boundary over — then **stopped at the code/data line** rather
   than reaching for the partitions.

> **The item got BIGGER because each seat left it intact for the lane it belonged to instead of
> half-investigating it.** That is the surprise channel working as designed, and it is worth as much
> as the finding.
