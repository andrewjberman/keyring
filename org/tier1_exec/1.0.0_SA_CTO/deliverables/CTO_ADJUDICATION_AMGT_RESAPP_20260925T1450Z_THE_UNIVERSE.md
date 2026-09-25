# CTO ADJUDICATION -- `AMGT_RESAPP` / `AMGT_CORPUS` -- WHAT "THE UNIVERSE" MEANS -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~14:5xZ

**Authority.** `/open-calls --adjudicate`, on Andrew's word of 2026-09-03 ~05:2xZ: *"after that point, no matter
what happens, I want the canonical loop to be able to keep cycling in its pattern and get the thing done."*
Both projects are past L2. **This is the card that has sat at Andrew across five ticks while the count of
outcomes turning on it went from one to five.** It is ruled here so nothing waits; **Andrew's answer supersedes
this ruling the moment it arrives, and no work done under it is wasted either way** (see RULING clause 5).

---

```
+-- CALL 1 of 2 ------------------------------------------------------+
  **When an AMGT fence says "every company the page covers", which
  population is that -- and what are the other three numbers?**
  Five surfaces now serve four different denominators for what looks
  like one question, and five outcomes are graded against it.
  ----------------------------------------------------------------------
  **REC --** The LIVE RESEARCH LIBRARY (94 today). The goal sentence
  names it outright: "every single security in the Asset Management
  research folder".
+---------------------------------------------------------------------+
```

## THE FOUR NUMBERS, EACH WITH THE INSTRUMENT THAT PRINTED IT

| n | what it actually is | instrument, read today |
|---|---|---|
| **94** | the LIVE research library | `library.list_folders(library.library_root())` -> **94**, root `.../Shared - Documents/Asset Management/Research`, measured by me at 14:4xZ with the producer's own reader |
| **89** | a coverage SNAPSHOT taken 2026-09-10T23:18Z | `freshness.universe_denominators.coverage` = 89; the crosswalk's own `coverage_vintage.snapshot_stale_against_live` reads **True** |
| **250** | the UNION of coverage and holdings | `freshness.universe_denominators`: `coverage 89, holdings_distinct 167, union 250, both 6` |
| **7** | the Exec tenure comparison pool | `ADJUDICATION_v49`: *"the pool 4.09 years over 40 officer(s) of 7 NAME(S)"* |

**RULING -- the live research library, and the other three are not competitors:**

1. **"Every company the page covers" = THE LIVE RESEARCH LIBRARY.** Today that is **94**. **This is not my
   preference; it is the goal's own words** -- *"all Asset Management research companies"*, *"every single
   security in the Asset Management research folder"*. The folder exists, the reader reads it, and it answers
   94. A fence that says *"every company the page covers"* is answered by that reader and no other.
2. **89 IS SUPERSEDED AND MUST NOT BE THE BASIS OF ANY FENCE.** It is a 2026-09-10 snapshot and the producer
   already declares it stale against the live list (`snapshot_stale_against_live: True`). It stays as a
   DISCLOSED VINTAGE -- `rp-1` measured it and stamped it, which was correct -- and stops being a population.
   **Nothing is re-graded on this alone**: `FWD-30`'s 84-of-89 divergence is a statement about the names it
   measured, and widening the population cannot improve it.
3. **250 IS CORRECT AND IS A DIFFERENT QUESTION.** `FWD-19`'s fence *requires* names outside coverage --
   *"an Opal holding when the company is not held, a non-Opal name when it is"* -- so the Posture's symmetric
   comparable is drawn from the union by design. **The defect `FWD-19` found is not that Deere is outside the
   corpus; it is that a comparable drawn from the union has no pack.** Ruling: **the union is the
   POSTURE-COMPARABLE population and must be labelled as such wherever it is served**, and a comparable
   selected from it carries either a pack or a stated reason it has none. `FWD-15`'s ranked list is ranking
   the union while its fence says *"covered names"* -- **that is a mislabel to fix, not a population to
   change**: serve the axis over the union and say so, or filter to the library; either satisfies the fence
   once the label matches.
4. **7 IS A DEFECT, not a fourth population.** `3.0.0_SA_CVO~Z` already classed it a stale disclosed
   denominator in `ADJUDICATION_v49`. The tenure pool is the library (94). `FWD-17` stays NOT_REALIZED and its
   fix is now specified rather than open.
5. **THE FIELD IS NOT THE PROPERTY, and this ruling names the property only.** `identity_universe` is the
   crosswalk's RESOLUTION INPUT -- **narrowing it to 94 would break resolution from 250 names to 94**, which is
   the error `2.0.0_SA_COO~X` caught in my round-3 ruling and which I adopted its correction for
   (`ROUND_ANALYSIS.round3.md` amendment @`2f209b5e0f`). **The implementer picks the field that carries
   "the live research library"; this ruling does not name one.** Where a producer needs the live list it is
   read the way `crosswalk.main` reads it (`_research_folders_for_disclosure`), which returns
   `(None, None)` on failure and lands absent-with-reason -- **never a zero** (see my CORPUS half @`081f598b9f`
   section 3).
6. **94 IS TODAY'S VALUE, NOT A CONSTANT.** Every artifact that serves a count of the library serves it with
   `research_folders_live` and `read_at` beside it, so a later 95 is a new reading and not a contradiction.
   **Nothing pins 94 into a fence.**

**WHAT THIS UNBLOCKS, and it is why the ruling could not keep waiting:** `FWD-17` (pool of 7 -> 94),
`FWD-19` (a union comparable owes a pack or a reason), `FWD-15` (label the axis's population), `rp-1`
(the snapshot is a vintage, not a population). **Four graded items move from "blocked on a word" to
"specified work" without any seat waiting.**

**IF ANDREW RULES OTHERWISE:** the only branch that changes work already done is (a) *"89, frozen"*, which
would make `FWD-17`'s fix wrong by five names and `FWD-15`'s label wrong -- **both one-line changes, and
neither is code that would have to be thrown away.** That is the whole exposure, and it is why ruling now
costs less than waiting.

---

```
+-- CALL 2 of 2 ------------------------------------------------------+
  **Who drains the on-demand pull queue, and on what cadence?**
  FWD-2 cannot close without it; no Lambda consumer may be built
  because the consumer reaches the Bloomberg terminal on loopback.
  ----------------------------------------------------------------------
  **REC --** No recommendation offered. This one is genuinely yours:
  it is a vendor-terminal cadence, reserved to you BY NAME.
+---------------------------------------------------------------------+
```

**RULING -- RESERVED, and the citation is on the card.** `AMGT_RESAPP_PRD.md:1042-1051`
(`C-ROUND12-PULL-WIRED`, ruled at L10 `ROUND_ANALYSIS.round11.md@4055200e2f` A1.3 R3 as corrected by
Addendum 2 C1), verbatim: ***"NO LAMBDA CONSUMER IS BUILT, and the consumer's CADENCE is RESERVED to Andrew by
name, on the same standing as the harvest cadence -- a card, never a cell."***

**I am not ruling this and I did not exercise it.** Calling the refresh route for an uncovered ticker enqueues
work whose consumer reaches a vendor terminal; *availability is not authorization*. **`FWD-2` stays
NOT_REALIZED with its reason recorded, no cell is cut for it, and the loop does not wait on it** -- which is
what a reservation is supposed to cost.

---

## CARRIERS

Recorded here; broadcast the same turn to `2.0.0_SA_COO~Z`, `2.0.0_SA_COO~X`, `3.0.0_SA_CVO~Z` and
`0.0.0_AB_MSTR`. Cited by `FWD-15`/`FWD-17`/`FWD-19`'s round-43 inputs and by `rp-1`'s vintage note.
**Call 2 remains in the ordinary `/open-calls` queue at Andrew.**
