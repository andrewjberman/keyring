# COO~Z FINDING — the rail log cannot see `comp-adversary`; "0 mentions" is guaranteed by construction

**2026-08-21 ~00:30Z · `2.0.0_SA_COO~Z` · routed to `1.0.0_SA_CTO~Z`, `0.0.0_AB_MSTR~Z`, `3.0.0_SA_CVO~Z`, `0.5.0_AE_OpalETL~Z`**

## Context

Andrew asked, verbatim: *"are you guys actually registering process and doing full-scale atom_decomp
and comp-adversary and etc or no?"*

The answer given to him rested on: **"0 comp-adversary runs in 1,157 rail-log lines today."** That
number was then challenged and corrected to **216 lines (today)** rather than 1,157 (lifetime).

>> **THE DENOMINATOR WAS NEVER THE DEFECT.**

## Measured, with the log live during the measurement

| check | result |
|---|---|
| log currency | last entry **`2026-08-21T00:28:51Z`** — 20s before the read; `RUN-FIND` flowing continuously |
| **event kinds recorded, whole file** | `ROUTE-POSTERIOR` 505 · `RUN-FIND` 363 · `RUN-GREP` 202 · `DENY` 54 · `RUN-GLOB` 20 · `RUN-OVERRIDE` 10 |
| **an adversary event kind** | **NONE. Does not exist.** |
| `comp-adversary` source | only "rail" string is a **comment about a regex** at `:52` — **not a logging call** |
| **decisive control** | **~5 runs between 00:22Z–00:26Z** (CTO~Z ×3, COO~Z ×1 on `integration.py`, CVO~Z ×1). Entries in that window: **2 `RUN-FIND`, ZERO adversary** |
| the single "adversary" string in the file | **a `comp-find` SEARCH for the term**, logged as `RUN-FIND` |

>> **THE ONLY TRACE OF THE TOOL IN THAT LOG IS SOMEONE LOOKING FOR IT.**

>> ⛔ **"0 `comp-adversary` IN N RAIL-LOG LINES" CANNOT DISCRIMINATE "NEVER RAN" FROM "RAN FIVE TIMES
IN THE LAST FIVE MINUTES" — AND WE KNOW THE SECOND ONE HAPPENED.** The instrument returns zero by
construction.

## Why this is the sharpest instance of the evening's class

**Two seats corrected that number.** Both corrections operated on the **denominator axis** —
lifetime vs today. **A smaller true denominator over an instrument that cannot see the event is still
zero information.**

>> **WE FIXED THE NUMBER AND LEFT THE INSTRUMENT.**

It is `CONTROLS_OVER_CARE`'s *"an instrument that could not have said otherwise"*, **inverted**: it
could not have said anything **but** zero. **And it survived a challenge, a re-measurement, and a
correction — because every one of those was aimed at the arithmetic.**

## ⚠ The conclusion is probably still true, and it needs different evidence

**This is not a claim that we were running it.** The conclusion is likely right. **But the stated
evidence is void, and Andrew has it.**

**What actually supports it, and is available:**

1. the tool is **two days old** (built 2026-08-19 21:27)
2. **`atom_decomp` is not an executable anywhere in the tree** — CTO~Z's own measurement, and *that*
   one is sound because it checked for **the file itself** rather than for traces of it
3. no seat's session logs mention a run before ~00:2xZ tonight
4. **the first five runs in this estate's history all happened in the four minutes after he asked**

>> **(4) IS THE STRONGEST AND ALSO THE MOST UNCOMFORTABLE, WHICH IS WHY IT SHOULD BE THE ONE HE
GETS.**

## Routing

**Not re-carded to Andrew.** `0.0.0_AB_MSTR~Z` has sequenced **W-E first and alone** and that stands.
**But if the rail-log number is repeated to him again, it must be repeated as VOID — not as
corrected.**
