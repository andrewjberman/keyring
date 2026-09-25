# AMGT_RESAPP -- ROUND 40 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-25 ~01:5xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s slug, msg 25828, and `ADJUDICATION_v50.md` @`6f7e5ed7ca` (blob IDENTICAL at
that pin and at HEAD, verified -- the citation is not aging separately from its text); the drain-end
packet @`cc1a74568e`; `0.7.0_AE_CloudOps~A`'s `ro-7` proof-of-spec; `FWD-30`'s DONE WHEN read at the PRD
bytes (`AMGT_RESAPP_PRD.md:739-752`) rather than from memory.

**GRADE ACCEPTED.** L10 preconditions MET: 7 of 7 orders terminal, 6 rows dispositioned, both judgment
criteria graded -- and, for the first time in three rounds, **graded non-vacuously**.

---

## 1. `FWD-30` IS REALIZED -- on branch (b), on the served plane, for ONE NAME

Round 39 RETRACTED `FWD-30` to NOT_REALIZED because the export published figures the page does not show
and missed an absence the page discloses. **Both defects are now measured closed on deployed bytes**
(`pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo=`, fresh served capture):

| set | page | rich | same | missing | **extra** |
|---|---|---|---|---|---|
| FIGURES | 165 | 165 | 165 | 0 | **0** |
| CITES | 15 | 15 | 15 | 0 | **0** |
| ABSENCES | 17 | 17 | 17 | 0 | **0** |

`EXPORT-COMPARE OK`, `rc=0`. Against the DONE WHEN clause by clause: branch **(b) machine-readable
rich-text output** is produced; *"the SAME figures"* 165/165; *"the SAME cites"* 15/15; *"the SAME
absences"* 17 of 17 covered; *"NOTHING in the export that is not on the page"* -- **extras 0 on all three
sets**, which is the clause round 39 retracted on.

**I checked the base run before accepting this and it disagrees, which is why the distinction matters.**
`round40/base-runs/ro-7.AC2.log` reads `FIGURES page=162 rich=179 same=162 missing=0 extra=17` -- the
very 17 extras that caused the retraction. That is the PRE-ACT control, not the outcome. **A round's
`base-runs/` directory is the failing arm on purpose, and grading from it would have re-retracted an
outcome that is now met.**

### 1a. THE PASS IS A MEASUREMENT AND NOT A TAUTOLOGY -- the failure arm is populated

`0.7.0_AE_CloudOps~A` kept the failing read instead of deleting it: on act B's bytes
(`ROZKMZGgC4UCGxD5yiJxtF1BAOf+Ccn3Qu+lTZ7cRTU=`) the SAME check on the SAME instrument read **ABSENCES 16
of 17, EXPORT-COMPARE NOT OK, rc=1**. **The pre-B2 world supplied the failing arm, so the 17-of-17 pass
was free to fail.** This is the standing rule I wrote after round 39 -- that a round touching served
figures carries at least one judgment criterion -- being satisfied in its strongest form: not just
graded, but shown capable of failing.

The `pe-relation` limb is sound on the same test: it exits 0 only on `cols.length===2 && ok>0 && bad===0
&& nul===0`, and 24 = 12 members x (ey, ey_ntm) with `nul=0` enforced. **A checker that can pass on an
empty population is worthless; this one cannot.**

### 1b. THE BOUND, AND IT IS THE ONE THAT MATTERS FOR THE GOAL

**This is ONE SECURITY.** 165 figures, 15 cites and 17 absences are `BA_US_Equity`'s. The goal's clause
is *"every single security in the Asset Management research folder"*. **`FWD-30` is REALIZED for the
exercised name and is UNMEASURED for the other 88.** Carrying 165/165/0 into a statement about the
corpus would be a true number moved into a population it never measured, and this analysis does not do
it. **Round 41's first enrichment item is the export exercised across a SAMPLE of the 89, not a second
pass on BA.**

The **ACCEPT** clause is likewise NOT exercised: *"Adam forwards the output without reformatting it"* is
a person-read and no person has forwarded it. DONE WHEN is met; ACCEPT is owed. I am recording that split
rather than letting a measured DONE WHEN imply an acceptance nobody performed.

## 2. THE FINDING THE ROUND PRODUCED THAT NOBODY CUT A CELL FOR

From the `ro-7` denominator line, stated by that lane and not by me: *"The join's own pre-served
acceptance read CITES 43/43 and ABSENCES 17/17 on the LANDED fixture -- the 43 -> 15 cites move is the
tell that the fixture run and the served run read different populations, which is the whole finding."*

**A fixture pass and a served pass are not two reads of one thing.** The fixture carried 43 cites where
the served document carries 15, and BOTH read `same, missing 0` against their own page -- so both were
internally consistent and only their DENOMINATORS disagreed. **An acceptance that passes on a fixture
certifies the fixture.** The CVO acted on this correctly and independently: it graded both criteria on
`real-run-served/` ONLY, because `real-run/` carries no verdict field, and *"grading `ro-3` there would
have read an UNMEASURED verdict as the absence of a fix"* -- `ABSENT != EXERCISED-AGAINST`, caught before
it produced a false FAIL.

**Standing rule, added here:** a criterion that can run on a fixture AND on the served plane states WHICH
it ran on and prints BOTH denominators, or its pass names no population.

## 3. `ro-3` AC3 -- the round-39 finding closed the way the round-39 analysis ruled

The thesis verdict was fixed at **the SECTION, not the header**, which is what that analysis directed,
and the load-bearing claim verifies at the bytes: `scoped_amgt.py:2510` is the ONE definition, and
header, section and export all read that one field. **The defect was two carriers of one claim, and the
remedy REMOVED the second rather than re-synchronising it** -- the only fix shape that cannot drift
again. The apparent contradiction (three sentences carrying PASS badges under a header saying no sentence
passes the describes-the-business test) was checked and is a different axis.

`ro-1` AC4: the export now prints `IS_DIV_PER_SHR: REFUSED -- unit/sign convention is...`, **the page's
own refusal**. The artifact that published 10 figures the page refuses now carries the refusal instead,
and `Z-S268` closes at the artifact.

## 4. THE COMPILE IS SOUND AND TWO OF ITS CARRIES RESOLVE DIFFERENTLY NOW -- MY DOING

The L8 compile dispositioned 6 of 6 with a reason on every carry. **Two carries defer to a ruling that
no longer exists.** `Z-S270` is carried as *"the GROUND of the three-valued ruling @`0d568cdf51`, whose
surface is still to be named"*, `Z-S273` as *"feeds the same open ruling"*, and section 3 records the
three-valued P/E rendering as an ENRICHMENT item on my list.

**I VACATED that ruling at `479eee52ff`, twenty minutes before the slug arrived.** `2.0.0_SA_COO~Z`'s
`Z-S273` measured the served Peers tab carrying P/E for **12 of 12** members, the three I said could never
fill included, corroborated by `ro-7` AC3's relation read of 24 of 24. My premise was wrong twice: the
Peers tab's P/E is the reciprocal of each member's earnings yield and not `BEST_PE_RATIO` at all, and I
reasoned from a capture taken 2.5 hours before the act that filled the cells -- **an act I had myself
signed.** `Z-S274` carries it.

**So, as dispositions:**
- `Z-S270` -- its claim is SUPERSEDED, not merely carried. It stands as the record of a wrong inference.
- `Z-S273` -- it does not feed an open ruling; **it CLOSED one.** It graduates on that basis.
- **No enrichment cell is owed for a three-valued Peers P/E.** Section 3's item is struck.

**The CVO was one step from this and its phrasing said so** -- *"whose surface is still to be named"* is
exactly the defect. Naming the surface is what falsified it. **A ruling whose SURFACE is unnamed is not
yet a ruling**, and that is worth more than the ruling was.

`Z-S269`, `Z-S272` carry unchanged, each with a named reason (one subject superseded by `Z-S273`; one
needing a posture re-run this round did not hold).

## 5. ROUND 41 -- `2.0.0_SA_COO~Z`'s to cut, the ENRICHMENT LIST

1. **`FWD-30` ACROSS THE POPULATION.** The export exercised on a SAMPLE of the 89, not a second pass on
   BA, with per-name `FIGURES/CITES/ABSENCES same/missing/extra` and the denominator per name. This is
   the goal's own clause and the largest unmeasured thing in the project.
2. **Branch (a) is untouched.** DONE WHEN offers *"(a) a presentation in Opal Brand Guidelines form ...
   AT MOST TWO PAGES"* OR (b). Only (b) has ever been exercised. Whether (a) is wanted is Andrew's --
   the goal text names both -- and no cell is cut for it until he says.
3. **The ACCEPT clause** -- a person forwarding the output unreformatted. Needs a person, so it is
   carded, not cut.
4. **`Z-S272`'s posture re-run**, which needs its own authorisation.
5. **NOT a cell:** the three-valued P/E rendering. Struck per section 4.

## 6. WHAT THIS ROUND DOES NOT CLOSE

`AMGT_RESAPP` is **not** complete. `FWD-30` is realized on one name; the population is unmeasured; branch
(a) is unexercised; ACCEPT is owed. **A round that closes an outcome for one security does not close a
project whose goal names 89.**

Routed elsewhere, recorded here so it is not lost: **`AMGT_CORPUS-Z-S29`** @`39c7ab0733` -- the corrected
FWD-12 pull returned history `{}` for EVERY key while reference and forecast landed, with the historical
request grown 23 -> 39 fields and **the client DROPPING a request-level error**. That is a failed
retrieval returning a VALUE at the client layer. It belongs to round 3's analysis and I will carry it
there with its two halves separated: the dropped error is MEASURED, the per-request field limit is
INFERRED.

---

**ROUND 40 IS CLOSED.** `FWD-30` REALIZED (branch b, served plane, `BA_US_Equity`, ACCEPT owed).
`2.0.0_SA_COO~Z` recuts round 41 from section 5 in ONE issuance.
