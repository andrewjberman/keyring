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

---

# AMENDMENT A1 -- 2026-09-25 ~15:3xZ -- **THE CALL WAS ALREADY ANSWERED BY ANDREW, IN WRITING, AND I RULED IT ANYWAY**

**I found this myself, twenty minutes after signing, while reading `AMGT_CORPUS`'s PRD for its round-4 L10
analysis. It is the failure `/open-calls` names as its own worst one, and I committed the harder version of
it: not re-asking a settled question, but RE-RULING one.**

## The contract that already settled it

`org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:719-733`, ratified contract
**`C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER`**, quoting **Andrew-direct 2026-09-24 ~05:0xZ, VERBATIM**:

> *"Only when all of this is done for every single security in the Asset Management research folder is the
> goal complete."*

and ruling on it, in the PRD's own words:

> **"SO THE POPULATION IS THE FOLDER, IT IS 93, AND IT IS ALREADY MEASURED"** -- *"which makes `FWD-19`
> gradeable from day one instead of gated behind a card. `K6` is CLOSED by his word."*

**`AMGT_CORPUS` raised this exact question as a Rule-28 card (`K6`), got Andrew's word on 2026-09-24, closed
the card, and wrote the answer into a ratified contract.** `FWD-19`'s own fence (`:399-414`) then reads
*"EVERY SECURITY IN THE ASSET MANAGEMENT RESEARCH FOLDER"* and cites the contract by name.

## What survives, what is withdrawn

**THE SUBSTANCE OF CALL 1 STANDS AND IS UNCHANGED** -- the population is the live research library. **Its
AUTHORITY is withdrawn and replaced:** it rests on **Andrew's word of 2026-09-24 ~05:0xZ and the ratified
contract**, not on a CTO adjudication and not on my reading of the goal sentence. **A ruling that restates a
sovereign word as though it were the ruler's own is worse than no ruling: it launders his authority into
mine and makes the record harder to trace, not easier.** Clauses 2-6 stand as ENGINEERING CONSEQUENCES of
the contract -- what to do about 89, 250 and 7 is not in the contract and is properly mine.

**AND THE CARD SHOULD NEVER HAVE BEEN CARRIED AT ALL.** I carried "89 or 94?" to Andrew across five ticks,
and sharpened it twice, for a question he had answered in writing the previous day. **Every tick that
reported it as an open card at Andrew was wrong**, and `FWD-17`, `FWD-19` and `rp-1` were reported as blocked
on a word that existed.

## WHY IT WAS INVISIBLE, which is a real finding and not an excuse

`comp-find 'C-BACKFILL-DENOMINATOR'` over `org/missions/D5/AMGT/`: **6 hits across 1839 scanned files, ALL
SIX INSIDE `AMGT_CORPUS`** (its PRD twice, its round-2 decomposition, the `CRPS-d-4` order, one channel row).
**ZERO in `AMGT_RESAPP`** -- not its PRD, not its ledger, not its decomposition.

**So a POPULATION CONTRACT ratified in one project's PRD binds outcomes in its sibling's, and the sibling
does not cite it.** Standing in `AMGT_RESAPP`'s ledger, where the card lived, the answer was not reachable by
reading anything `AMGT_RESAPP` points at. **That is the mechanism, and the fix is a cross-reference**:
`AMGT_RESAPP`'s PRD must cite `C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER` wherever a fence says
*"every company the page covers"*. **Round-43 item, and it is the cheapest item on any list I have written
today.**

**THE GENERAL RULE, and it is the part worth keeping:** before carrying a population or semantics card to
Andrew, run ONE unscoped census of the term over every SIBLING project under the same directive -- not just
the project holding the card. **A card is not open because MY project has no answer; it is open because the
DIRECTIVE has none.** Cost: one `comp-find`. Non-application: a question with no sibling project.

## AND THE NUMBER MOVED, which is why the contract's METHOD matters more than its figure

The contract says **93**. My live read today says **94** (`library.list_folders(library_root())`, root
`.../Asset Management/Research`, 14:4xZ), and `3.0.0_SA_CVO~Z` independently read 94 at 15:2xZ in
`ADJUDICATION_v7`. **One folder has been added since 2026-09-24.**

**The contract anticipated exactly this and is written to survive it:** *"EVERY `FWD-19` POPULATION CLAIM IS
A SUBTRACTION FROM A FRESH READ OF THE ASSET MANAGEMENT RESEARCH FOLDER, WITH THE DENOMINATOR PRINTED."*
**So 93 is a reading, not a constant -- which is what clause 6 above says, and it turns out to be the
contract's own discipline rather than my addition.** Any artifact or census still asserting 93 as the
population is now one folder short, and `FWD-19`'s three counts must sum to **94** at the next census, not 93.
**That is a live consequence for `CRPS-d-4` and for round 5, and it is the one genuinely new thing this
amendment produces.**
