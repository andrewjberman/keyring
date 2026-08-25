# Four items, a number I got wrong, and the pattern under all of it — `3.0.0_SA_CVO~Z`

**archetype:** VALIDATE
**Seat:** `3.0.0_SA_CVO~Z` (site Z) · **This entry:** ~00:55Z → ~02:20Z
**Predecessor:** `session_2340-0055Z_the_gold_tier_break_and_two_errors_of_mine.md` @`8bf081ef8f`

---

## Objective

Hold the channel through Andrew's *"top priority / rectified immediately"* window on DIVZ/IDVZ.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `jsonschema` | VALID on every append, 8 this window | 36 items, ids contiguous 1..36 |
| `aws s3api` | token-walked every sweep | The 41-file Pathfinder census and the 73-partition silver census are both **full**, not sampled — and both findings depended on it |
| **execution** | 4 predicates run rather than read | The single highest-yield instrument this window (§5) |
| `safe-commit.sh` | 8 commits, `-F` via Write/heredoc | risk-reflex CLEAN each |

---

## Work Completed

### 1. Z-S33 — Pathfinder's `Date` is an EFFECTIVE date, not an as-of
CTO~Z grounded Andrew's *"no divergence between the providers"* on both issuers' bytes and it
reproduces. **But one file per issuer establishes that two values agree on one night; it cannot
establish what a date field means.** Full 41-file history: `Date` == capture day on **29 of 41**,
differs on **12** — and **all 12 are Sat/Sun**, zero counterexamples. On weekend captures Pathfinder
forward-dates to Monday. So *"assign `data_as_of` from the issuer's own Date"* would stamp 08-22,
08-23 and 08-24 all as **08-24**, labelling Friday's closing holdings as Monday.

### 2. Z-S34 — the pull resolves its as-of from LOCAL time
MSTR~Z's sovereign-priority run landed in `bbg/2026-08-21/` instead of 08-24: `pd.Timestamp.today()`
is local, and locally it was still Monday. **Separate from Z-S32 under Rule 24(iv)** — the calendar
fix bites 10 days a year, this bites a 4-hour window nightly, and **a correct calendar applied to the
wrong day is still the wrong day.**

> ⛔ **Z-S30's tripwire passed, live, in exactly its design case.** Both sides are the same
> expression, so both read the same local clock. **A guard cannot catch an error in a premise it
> shares with the thing it guards.** Filed as *latent* 80 minutes earlier; no longer latent.

### 3. Z-S28 discharged, Z-S35 and Z-S36 opened
**Z-S28 disarmed** — all four ADRs resolve, 3 of 169 unjoined and all three known-permanent. Tomorrow
is **not** blank analytics. **Z-S35**: SALXX — the only cash line in both funds — *joins* but carries
a null GICS and books as **Equity**. **Z-S36**: `classify()` has four return paths and **every one
returns Cash or Equity**; the sub-asset axis is *defined* as GICS-sectors-plus-cash. Andrew's answer
is neither expressible nor derivable — which is why he asked for a canonical classifier.

### 4. The synthesis: three findings, one fact
All three candidate as-of sources break on weekends, **each in a different direction** — the clock
one day too far back, the newest partition onto a non-trading day, the vendor Date forward to Monday.
One root cause: the producer fires on a flat daily cron, so weekends exist in the data.
**The remedy is not "pick a better source"; it is the trading-calendar filter on whichever you pick.**

---

## ⛔ Errors and the pattern under them

**I broadcast a wrong number to five seats.** I said `stats.is_cash_inferred` would read ~73; it
reads **0**. DS~Z *executed* the function; I read the increment site and the null count and combined
them without opening the branches. **My conclusion survived, my number did not — and the number was
the dangerous half**, because "expect ~73" manufactures an alarm out of correct behaviour on Andrew's
morning. I had warned in that same message that 73 would invite the wrong reflex, then supplied it.

**My Z-S28 disarm was plane-bound and I didn't say so.** "3 of 169 unjoined" answers *join coverage*.
SALXX joins. **Both my controls fired correctly and both were about the wrong plane.**

### The pattern, four instances, and it is the thing to carry out of this project

> **A true ADJACENT fact substituted for the one actually asked.**

| the substitute (true) | the question (answer) |
|---|---|
| "the string contains MMKT" | does the marker match? **no** |
| increment site + null count | what does `is_cash_inferred` read? **0** |
| the join test came back clean | does the row classify? **no** |
| `BDay(-1)` is the convention | which *day* does it resolve? **the wrong one** |

**In every case the substitute was TRUE, which is why none was caught by reading.** Remedy identical
each time: **execute the predicate, do not read around it.** I was on the wrong side of it twice and
the right side twice.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Allocated Z-S35/Z-S36 **same-turn** on request | The 01:00Z rule, written after the Z-S31 collision. First exercise came 3 minutes later. |
| Filed Z-S33 as attacking the **implementation**, not Andrew's ruling | His conclusion holds and is strengthened; the vendor `Date` field is what cannot carry it. |
| Adjudicated the three-seat marker dispute **by execution** | DE~Z right on the fact, COO~Z right on why the call site matters — different questions, not a conflict. |
| Marked Z-S32's evidence **destroyed, not wrong** | The bytes moved under a correct citation; a re-derivation would read it as an error. |

---

## Blockers

**None at this seat.** All seven BLOCKING+ARMED items are owned elsewhere.

---

## Current State

**36 items · 21 ARMED / 15 INERT · ids contiguous 1..36 · 0 ARMED without an owner.**
**BLOCKING+ARMED:** Z-S16, Z-S22, Z-S31 *(armed in production)*, Z-S33, Z-S34, Z-S35, Z-S36.
⛔ **`bbg/2026-08-24/` still does not exist. Andrew's item is still blocked.**

---

## Next Steps

1. **~11:00Z — the L1 fire.** `bbg/2026-08-24/` landing. Z-S28's ADR half is **already discharged**,
   so this is now a one-question read, not two.
2. **13:00Z — TO-5 AC7**, first *scheduled* gold fire. Read the invocation record, not a report.
3. **The Z-S35 oracle, values fixed in advance:** DIVZ `alloc_cash` ≈ **0.58**, IDVZ ≈ **0.89** if
   correct; both ≈ **0.00** with that weight in `alloc_equity` if it fired. ⛔ **Do NOT use
   `is_cash_inferred` — it reads 0 in both worlds.**
4. **Round v1 stays OPEN.** Seven BLOCKING items, one of them live on deployed bytes.
