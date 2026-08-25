# ANDREW-DIRECT 2026-08-25 ~04:0xZ — FULL BLOOMBERG BACKFILL, ALL SECURITIES, AS FAR BACK AS EXISTS

**Channel:** direct to `0.0.0_AB_MSTR~Z` at the site-Z MSTR terminal
**Recorded by:** `0.0.0_AB_MSTR~Z` (the addressed seat), same turn as receipt
**Broadcast:** same turn, all six live site-Z seats, 6 DELIVERED / 0 QUEUED / 0 REFUSED

---

## ⛔⛔ QUALIFIED BY HIM ~04:09Z, ~7 MINUTES AFTER THE WORD BELOW. READ THIS FIRST.

**PHASE 2 (the deep per-security backfill) IS HELD. The title of this file names the UNQUALIFIED
form and is now only half-true.** His qualification, VERBATIM AND COMPLETE:

> "actually we maybe should not do that, need to assess how much data that would be. I would think
> 100 securities of deep backfill would not be a data quota issue, but its the kind of thing that we
> should do one time and then from here on out, we just add one incremental row of lookback and
> recalculate, never do that big pull again"

**THREE THINGS IT SETTLES:**
- **ASSESS BEFORE PULLING.** The size existed before the pull did: `1.0.0_SA_CTO~Z` measured
  **~800–900k rows, 5–6x the existing `bbg-testpull` archive**, ragged per security (AAPL 1982,
  AZN 1999, BBSEY nothing before 2000). **His instinct to size it first was correct.**
- ⭐ **IT IS A ONE-TIME SEEDING ACT, NOT A REPEATABLE OPERATION** — *"do it one time and then from
  here on out, we just add one incremental row of lookback and recalculate, never do that big pull
  again."* **That changes what gets BUILT:** the seeding path must be **idempotent and resumable**,
  and **the daily increment is the thing that has to be right forever.**
- **The archive therefore becomes a STANDING ASSET**, so its home and its KEYING matter more than a
  throwaway pull's would. ⚠ **Tonight produced TWO separate defects from partitions named for the
  wrong date (`:1375`, and the `history_topup` re-key). Carry that into the design rather than
  discovering it a third time.**

✅ **PHASE 1 IS UNAFFECTED AND STILL RUNS:** ~400 calendar days x 169 securities fills **every** current
return window (`RETURN_WINDOWS` longest = `1Y` = `as_of - 365d`), is small, and sits well inside the
terminal's free window before 07:00 local.

---

## VERBATIM (the 04:0xZ word, qualified above)

> "Yes I want full backfill for all of them because we want to be able to produce as far back as
> exists for the "Performance" views for these ETFS"

**Not a paraphrase. The phrasing is the ruling.**

---

## WHAT IT AUTHORISES — AND IT IS THE THING THE FABRIC COULD NOT DO WITHOUT IT

CLAUDE.md, Agent Autonomy: ***"NEVER call an external vendor API without Andrew's EXPLICIT PER-USE
WORD — availability in the toolset is NOT authorization."***

**This is that word, for the Bloomberg history backfill.** It is the constraint
`3.0.0_SA_CVO~Z` correctly refused to cross at 03:37Z when they declined to re-verify
`1.0.0_SA_CTO~Z`'s probe: *"an authorisation to do a thing is not an authorisation for a second seat
to do it again to confirm."* **The bar they named is now met by his own sentence.**

## THREE SCOPE POINTS — HIS SENTENCE IS BROADER THAN THE WORK WE HAD SIZED

**(1) "ALL OF THEM" IS NOT THE 61-TICKER GAP.**
The fabric had scoped **DIVZ/IDVZ** (28% / 7% uncovered) as "the real backfill" and **PFDE/PFOE**
(97% / 92%) as "plumbing off `bbg-testpull/`". **He said ALL.** The plumbing half does not become
unnecessary — but the archive's coverage is **no longer the boundary of the pull**, and anything
`bbg-testpull/` holds should be **verified against a fresh pull rather than assumed current**: the
producer's own comment at `etf_positioning_gold.py:41` labels it *"FROZEN QA reference — NOT read
here."*

**(2) "AS FAR BACK AS EXISTS" IS A MEASUREMENT, NOT A CONSTANT.**
The 2-ticker probe used **2020-12-31** and that start was ACCEPTED — **which proves the window is
AVAILABLE, not that it is the MAXIMUM.** His words are *as far back as exists*, **per security.**
⛔ **Measure the true earliest per ticker. Do NOT freeze 5.6 years into a spec because it is the
number in front of us** — an unmeasured exact constant fails closed looking principled, and this one
would silently truncate an ETF's entire history while every check passed.

**(3) THE PURPOSE IS NAMED AND IT BOUNDS THE SHAPE:** *"to produce ... the Performance views."*
The 8-window return maths is **already built and correct** — `etf_positioning_gold.py`'s own
docstring: *"Returns beyond 1D need a series... it UPGRADES FORWARD WITH NO CODE CHANGE as partitions
accumulate."* **This is a DATA ACQUISITION, not a producer rewrite.**

## ⛔ ONE BLOCKER THAT MUST LAND FIRST OR THE BACKFILL INHERITS IT

```
bbg/2026-08-24/history_topup.parquet   167 rows, internal date 2026-08-21   <- 08-21's rows
bbg/2026-08-21/history_topup.parquet   167 rows, internal date 2026-08-21   <- the same rows
load_history() CONCATENATES every partition in the lookback
```
`1.0.0_SA_CTO~Z` self-filed this against their own 02:50Z re-key; `3.0.0_SA_CVO~Z` confirmed the
concatenation. **Backfilling into a lookback that double-counts a trading day produces PLAUSIBLE
WRONG RETURNS on a client-facing panel** — the exact class this project spent the night on.
**Fix the duplication BEFORE the archive is wired, not after.**

## WHAT IS ALREADY PROVEN, SO NOBODY RE-DERIVES IT

- **The pull shape works on the hardest cases.** `1.0.0_SA_CTO~Z`'s 2-ticker probe deliberately chose
  two ADRs absent from `bbg-testpull/`: `AZN` ret 0.9058 / px 165.98 and `BBSEY` ret 3.3661 / px 7.37,
  **both tying EXACTLY to our stored `history_topup`.**
- **The tie-out is verified at a second seat with NO vendor call** — `3.0.0_SA_CVO~Z` re-derived the
  stored limb from S3 and matched **to the digit**.
- **What is NOT proven:** the true earliest date per security, and the cost at full-universe scale.
  **Size it on a measurement, not on the probe's window.**

## ROUTING

`2.0.0_SA_COO~Z` — dispatch. `1.0.0_SA_CTO~Z` — pull shape + the earliest-date measurement.
`0.4.0_DS_ClientPlatform~Z` — the `history_topup` duplication, first.
**MSTR~Z relays and records; it does not own the build.**
