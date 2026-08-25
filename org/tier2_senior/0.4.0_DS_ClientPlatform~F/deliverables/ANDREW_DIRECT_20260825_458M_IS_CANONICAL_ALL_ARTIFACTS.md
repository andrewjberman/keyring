# ANDREW-DIRECT 2026-08-25 ~03:0xZ — 458M IS THE CANONICAL COTTONWOOD NUMBER, EVERY ARTIFACT

**Terminal:** `0.4.0_DS_ClientPlatform~F`. **Evidence:** second Black Diamond dashboard screenshot,
08/21/2026, MARKET VALUE 458.05M, Total ending market value 458,053,742.
**Status:** RECORDED VERBATIM + BROADCAST SAME TURN. **Answers all three open calls.**

## VERBATIM

> 1.) The number has to add to 458m, look right here: [screenshot]. DO you see how the supervised
> figure comes to 458m? That means that Cottonwood, the Client for whom this Dashboard is for, sees
> 458m as the canonical number. THat means that showing 449m is the wrong number. I need to make this
> blisteringly clear. With that in mind, YES, every artifact should be processed in such a way that as
> of todays data, the total number adds to 8m. 2.) Confirmed. 3.) Approved.

⚠ **READING NOTE, flagged not silently corrected:** *"the total number adds to 8m"* is read as
**458m** — the entire message argues 458M is canonical, and no reading makes 8M a firm total. Flagged
here so the record shows the interpretation rather than burying it. **If he meant something else by
"8m", this record is wrong and he should say so.**

## WHAT IS RULED

**CALL 1 — RULED, and stated by him as emphatic:** 458M is what **the client themselves see**, so it
is **the canonical number**. **Showing 449M is WRONG.** **EVERY artifact** is processed so the total
comes to 458M on today's data. The SCOPE question is answered: **all cot artifacts, not D1 only.**
**CALL 2 — CONFIRMED:** Supervised x All Assets is the canonical Cottonwood view.
**CALL 3 — APPROVED:** his PRD *"~$30M Client"* meant **CLIENT HELD AWAY** ($30,322,927.42), not the
non-model residual. **Both PRD s.6.5 estimates were correct all along** — ~$7M = the Custom Models
($6,622,450.40 under his Call 2 rule), ~$30M = held-away. There was never an 11x error, only an
unidentified referent.

---

# ⛔ THE EXCLUSION ALONE DOES NOT PRODUCE 458M. COTTONWOOD'S CHAIN IS TWO TRADING DAYS BEHIND.

**This is the finding that decides whether his instruction is satisfiable by the work already scoped,
and the answer is NO.**

Applying the held-away exclusion to cot's CURRENT pipeline data yields **449,733,561.36** — *precisely
the number he just called wrong*. It is not a rule error. **449.7M is the supervised figure at
2026-08-19; 458.05M is the same measure at 2026-08-21.** Same rule, same filter, two dates.

## MEASURED — MDPF aggregate-aua-timeseries, latest partition per firm

| firm | latest partition | written |
|---|---|---|
| 49financial | **2026-08-21** | 2026-08-24 09:31Z |
| inflection | **2026-08-21** | 2026-08-24 09:31Z |
| **cottonwood** | **2026-08-19** | 2026-08-20 09:31Z |

**NEVER#1 DISCIPLINE APPLIED — THIS IS NOT A WEEKEND ARTIFACT.** Trading calendar resolved first:
2026-08-19 Wed · 08-20 Thu · 08-21 Fri · 08-22 Sat · 08-23 Sun · 08-24 Mon. The missing cot
partitions are **Thursday and Friday — ordinary trading days.**

**THE DISCRIMINATOR IS THE SIBLING COMPARISON, NOT THE AGE.** The SAME 09:31Z run on Monday 08-24
produced a `2026-08-21` partition for 49financial AND for inflection, and produced nothing for
cottonwood. A calendar effect would hit all three identically. It did not. **cot is two trading days
behind its siblings on a shared schedule** — a wall-clock age would have proved nothing here, and the
cross-firm control is what makes this a finding rather than a Monday false alarm.

## WHAT IT MEANS FOR HIS INSTRUCTION
His words are *"every artifact ... processed in such a way that as of today's data, the total number
adds to [458]m."* That has **TWO** requirements, and only one was scoped:
1. **EXCLUDE HELD-AWAY** — ruled, measured, ready. **NECESSARY.**
2. **BE ON CURRENT DATA** — cot's chain must reach 08-21. **NOT SUFFICIENT WITHOUT IT, AND NOT IN
   ANY D1 CELL.**
Shipping (1) alone emits 449.7M and **fails his instruction while appearing to comply with it** —
the exclusion would be correctly implemented and the served number still wrong.

**A SECOND, INDEPENDENT VINTAGE CONSTRAINT SITS BEHIND IT:** `dim_model_portfolio`'s freshest
`value_date` is **2026-08-19** across every assignment partition through 08-24. Even with the
aggregate chain advanced, the MODEL ATTRIBUTION layer must also value to 08-21 or the
Models-vs-Client split cannot be struck at his canonical date.

## ROUTING
**NOT THIS LANE'S CELL AND NOT THIS LANE'S DIAGNOSIS.** The cot chain's freshness belongs to whoever
owns the cot MDPF producer; this lane measured it, resolved the calendar, and controlled it against
two sibling firms. Routed to COO/CTO with the numbers. **Cause NOT diagnosed — an absent partition
has several possible mechanisms and Rule 22 makes any of them a hypothesis until source-confirmed.**

**Author:** `0.4.0_DS_ClientPlatform~F`. **Cells:** D1-b-1, D1-h-p2, D1-d-1 (+ a dependency outside D1).
