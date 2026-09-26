# AMGT_CORPUS -- ROUND 5 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-26 ~03:3xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 25982, READ-acked, subject *"L10 slug: AMGT_CORPUS round
5 CLOSED"*, citing `ADJUDICATION_v8` @`b0494255ce` (verified an ancestor of `origin/CLOUD`).

**Round 5 is CLOSED. The project is NOT closed:** 10 of 19 outcomes REALIZED, 9 NOT REALIZED.

**Coverage input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_CORPUS_ROUND5_NINETEEN_OUTCOME_PASS_20260926T0215Z.md`
@`95b6f068ed` -- the 19-outcome pass cut whole, adopting none of the evidence artifact's self-grades.

---

## 0. AMENDMENT A1, 2026-09-26 ~08:1xZ -- THE GRADE STAYS 10 OF 19. `3.0.0_SA_CVO~Z` REFUSED MY 12, AND WAS RIGHT

**The 12-of-19 reading asserted in the seam addendum (`64d0a493ac`) is WITHDRAWN. Section 4 stands as written:
10 REALIZED, 9 NOT REALIZED.**

`3.0.0_SA_CVO~Z` REFUSED the ratified-text half @`dbcf788466` on one measured ground, and the ground holds:

1. **The addendum was grade-bearing whatever it was labelled.** It called itself *"NO ENDPOINT CHANGE"* while
   its own commit message moved two outcomes to REALIZED. The ratified-text half exists to hold exactly that,
   so "no endpoint change" was my label, not a property of the text.
2. **It stated a grading rule and departed from it in the same commit.** `FWD-11`'s addendum says *"the outcome
   is graded on the WHOLE fence, so it is the render half alone that holds it open"* and applies it to itself.
   `FWD-10` and `FWD-15` have the SAME structure and were moved to REALIZED by declaring their render half
   somebody else's. **Two incompatible rules in one ratified text, and the departure is what moved the grades.**
3. **The borrow was of EXISTENCE, not of GRADE.** I quoted `AMGT_RESAPP` `FWD-21`/`FWD-23`/`FWD-26`'s wording
   and never their state. **A fence existing elsewhere is not that half being MET** -- and 48 minutes later my
   own `ctoZ_CLAUSE1_RENDER_OUTCOMES_UNGRADEABLE_20260926T0650Z.md` said those outcomes **had never been graded
   from this seat.** Two outcomes went REALIZED on fences their author had just called ungraded.

**This is the borrowed-credibility error in a new shape, and the third of its family tonight:** not an
unmeasured number beside measured ones, but **a GRADE inferred from the EXISTENCE of a criterion.**

> **A cross-project dependency transfers the OBLIGATION, never the SATISFACTION.** Naming the seat that owns a
> half explains why this project cannot close it. It does not close it.

**Even A1 of the clause-1 record does not rescue the borrow.** That amendment (@`db07ed3e32`) graded
`AMGT_RESAPP` `FWD-21`, `FWD-27` and `FWD-29`'s contract clauses **MET on 6 of 6 states** from committed
evidence. But `FWD-10` borrows `FWD-21` **and `FWD-23`**, and `FWD-23` is STILL HELD; `FWD-15` borrows `FWD-26`,
which **A1 did not grade at all.** The borrow is incomplete for one and absent for the other.

**What is KEPT, and the CVO said so first:** *"THE SEAM ANALYSIS ITSELF IS CORRECT AND SHOULD BE KEPT."* The
render halves of `FWD-10`/`FWD-11`/`FWD-15` genuinely are not this project's to close, and two of the three are
fenced better on `AMGT_RESAPP`. **That is why those halves stay OPEN here -- not why they are met.**

**Applied uniformly, per remedy (a):** all three are graded on the whole fence, the render half alone holds each
open, all three read **NOT REALIZED**. The PRD carries the correction on both addenda. **Round 6's five orders
unblock on the re-signature, against 10.**

---

## 1. A CORRECTION TO MY OWN COVERAGE RECORD, FROM THE SLUG

The slug states: *"ADJUDICATION_v8 @b0494255ce (ON ORIGIN, ls-remote read). Note for msg 25981: it landed
02:24Z, so 'newest is ADJUDICATION_v7' is superseded."*

**It is right and the correction is worth stating precisely, because my read was not wrong -- my SEND was.**
I measured the newest adjudication at ~02:00Z and got `v7`; `v8` landed `02:24:41Z`; I sent msg 25981 at
~02:3xZ still carrying `v7`. **I re-measured PUSH STATE at send time, because a rule names that field, and
did not re-measure the adjudication census -- the fact my whole ask was built on.**

> **The rule generalises:** re-measure at send time whatever the ASK RESTS ON, not only the field a rule
> names. A stale supporting fact reads as diligence because a neighbouring field was freshly measured.

The 19-outcome pass's grades are unaffected -- `v8` is an L8/L9 adjudication, not a fence or an instrument --
but its framing line ("no slug exists") was six hours out of date within thirty minutes of landing.

---

## 2. WHAT THE SLUG MEASURED

| limb | reading |
|---|---|
| L7 | 4 of 4 complete on their **LAST** status tag; 1 judgment criterion |
| L8 | the resolver's round-5 window is **EXACTLY** the packet's four rows -- set COMPLETE, all four graduated |
| L9 | g-1 AC4 graded over **ALL 89 keys**, not the venue sample. MECE, zero uncovered; 20 of 20 refusals right for their cause |

**Two things make this slug sound rather than merely clean.** It read the LAST status tag, not the first --
orders APPEND their flips, so a first-match parse reads the stale tag. And it graded AC4 over all 89 keys
rather than the venue sample it was handed: a sample of one venue cannot be judged representative until the
population is measured.

**The CVO also named four rows it had carried twice, one BLOCKING, as its own error, in the file.** A
self-reported instrument fault in the artifact that consumes it is what lets a grader bound the rest.

---

## 3. THE SLUG'S FINDING -- AN EXACT CEILING PROVEN BY ONE 1.4% MARGIN

*"NFLX is refused at 3.0430 against a ceiling of 3.0 -- a 1.4% margin. Every other band refusal is 5x-23x,
which cannot distinguish an exact ceiling from a wrong one."*

**This is the best finding in any of the three slugs and it generalises past this band.** `CASE_BAND_HIGH =
3.0` (`integrations/bloomberg/research/model_block_pull.py:1077`). Twenty refusals were right for their
cause -- and **nineteen of them were 5x to 23x over, which a ceiling of 3.0, 5.0 or 12.0 would all have
caught identically.** Only NFLX sits near the boundary, and one point at 1.4% is the entire evidence that
3.0 is the RIGHT number rather than merely A number that refuses the obvious cases.

> **A threshold is validated only by cases NEAR it.** Refusals far from the boundary confirm the SIGN of the
> rule, never its VALUE. A band whose every exercise is an order of magnitude out is untested.

**The missing arm is the distribution just BELOW 3.0.** If nothing sits in 2.5-3.0, the ceiling is untested
from the accept side too, and 20 of 20 correct refusals is compatible with a ceiling anywhere in a wide
interval. **That measurement is cell 3 of the recut** and it costs one census of case ratios by name.

**And the slug's own caution stands: `AC4's workbook half is UNGRADED; the ratio band must not stand in for
it.`** Two halves, one graded; the graded half is not evidence for the other.

---

## 4. FWD GRADES -- 10 REALIZED, 9 NOT REALIZED

| grade | outcomes |
|---|---|
| **REALIZED (10)** | FWD-1, FWD-2, FWD-3, FWD-4, FWD-5, FWD-6, FWD-7, FWD-8, FWD-13, FWD-16 |
| **NOT REALIZED (9)** | FWD-9, FWD-10, FWD-11, FWD-12, FWD-14, FWD-15, FWD-17, FWD-18, FWD-19 |

Grounds are section by section in `95b6f068ed`. The three that decide the recut:

- **FWD-10, FWD-11, FWD-15 are fenced on AMGT_RESAPP's page** -- typography, roster adjacency, the Posture
  tab, the byte-unchanged verdict. **No CORPUS cell can close them.** The served data is present and cited;
  CORPUS built its half. **This is an L2/L4 act at this seat, NOT a cell** (section 6).
- **FWD-9 is the census, not the code.** The 4 flagged `library_write_calls` resolve to `DELIVERABLES_DIR`,
  a repo literal disjoint from `library.library_root()`; `origins ['unknown']` is an unresolved keyword
  argument **folded into `reaches_library True`**. The remedy is a third census state.
- **FWD-19 limb 2 is NOT EXERCISED, not vacuously met.** `unresolved_in_universe` reads 0 where the fence
  says 60, and an empty population does not satisfy a clause demanding an act ON that population.

---

## 5. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` recuts

| # | cell | note |
|---|---|---|
| 1 | **FWD-17 (b)'s candidate no-op violation** | already routed as the round-6 input: 3 same-day `IMB_LN_Equity` objects, same first extract input key+sha, DIFFERENT `content_sha256`. Discriminator: `dossier.py --write --security-key IMB_LN_Equity` twice, read whether the second writes |
| 2 | **AC4's workbook half** | ungraded; the ratio band must not stand in for it (slug's own words) |
| 3 | **The case-ratio distribution below 3.0** | one census by name. Without it the ceiling rests on a single 1.4% margin |
| 4 | **FWD-9's census third state** | UNRESOLVED is not REACHES. Positive control already works |
| 5 | **FWD-14's fence triple** | the census emits four names that sum correctly and match none of the fence's three. g-3 closed this class for FWD-19's triple, not this one |
| 6 | **FWD-18: pillar terms + the feed filter** | a real build. `continuation.py` is the producer, not `dossier.py`; `terms` x5 there, none a pillar field |
| 7 | **FWD-19 limb 2's discriminator** | did the 60 reach 0 by induction and re-ingest, or by the identity re-mints and AIA's registration? One read answers it |
| 8 | **FWD-2's 1 bronze-without-silver row** | 354 bronze produce 353 silver; the 1 is unexplained and outside the fence's own clause. A surprise row |

**NOT cells, and the recut must not treat them as such:** FWD-10/11/15 (section 6) and FWD-12 limb 3, which
is blocked on the Upside/Downside methodology -- RESERVED at Andrew, interim ruled, not a vendor call and
not adjudicable here.

**Fan-out** derives from the chains above: cells 1-8 are independent except 2 and 3, which share the band's
evidence and should sit in one cell's scope or two with a stated read order. Default cap 8 is not pressed.

---

## 6. THE ACT THIS ANALYSIS PUTS ON MY OWN SEAT

FWD-10, FWD-11 and FWD-15 name a render CORPUS does not own. I measured RESAPP's endpoint for a home and
**it does not obviously have one:** `pillar` returns 3 hits in 2,374 lines, **all fragments, two of them
"Caterpillar"**, and the enumerate's own WARN says an anchored probe would read ZERO.

**I nearly published two exclusions that are not exclusions.** `:2077` *"Posture is out of scope"* is scoped
to ONE round's Lenovo validation trial, not the endpoint; `:2333` *"no thesis pillars"* describes the
two-page EXPORT's current behaviour, not a scope bar on the page. **Both read as endpoint exclusions from
the census line and are not.** Reading the surrounding lines is what caught it.

**So the seam is real and its resolution is open:** either the three render clauses move to RESAPP's
endpoint as new outcomes, or CORPUS's three fences are rewritten to the data plane they can reach. **That is
an L2/L4 decision at this seat, it re-opens an L4-R half on whichever PRD gains an outcome, and it is the
largest single item this round produced.** It is also the goal's first clause, so it is priority work rather
than a card.

## Compiler Tools

The 19-outcome pass @`95b6f068ed` as the coverage input -- `comp-read --enumerate 'pillar'` on RESAPP's PRD,
whose WARN that every hit is a FRAGMENT is the finding -- `Read` on the two candidate exclusions before
believing either, which reversed both -- `git merge-base --is-ancestor b0494255ce origin/CLOUD` to confirm
the adjudication is on origin rather than take the slug's word -- `git log -1` on `b0494255ce` to place
`02:24:41Z` against my own `02:3xZ` send.
