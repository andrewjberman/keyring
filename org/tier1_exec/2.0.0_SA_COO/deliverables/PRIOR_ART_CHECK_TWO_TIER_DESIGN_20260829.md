# PRIOR-ART CHECK — two-tier design, COO pen

**Author:** `2.0.0_SA_COO~Z` | **Date:** 2026-08-29 ~04:0xZ
**Status:** ⛔ **DESIGN. NOT LANDED. Andrew's feature, Andrew's call.** No gate is created by this
file and nothing is held behind it.

## 1. THE WORD

> **Andrew, 2026-08-29 ~03:5xZ, VERBATIM (relayed by `0.0.0_AB_MSTR~Z`, msg 16024):**
> *"ill deal with them, talk to COO about the prior art feature, i think both CTO at PRD level and
> COO at TO level should have some kind of prior art check, maybe CTO broadly checks and COO's check
> is more operational in the context of new/reuse operational build"*

⚠ **THE HEDGE IS CARRIED, NOT TRIMMED: he wrote "maybe" and "some kind of."** **The TWO-TIER SHAPE is
his and is treated as ruled. The split's exact wording is OFFERED, and everything in §4 below is my
proposal, not his instruction.** `2.0.0_SA_COO~Z` holds the pen on his word *"talk to COO"*;
`1.0.0_SA_CTO~Z`'s surface is named in his sketch, so they are a co-designer here and not a recipient.

## 2. ⛔ THE PRIOR-ART CHECK ON THE PRIOR-ART FEATURE — RUN FIRST, AND IT HITS

**A design for a prior-art rule that does not itself run a prior-art check would be self-refuting.
Ran it. It returns a hit, and the hit is 22 days old and NOT LANDED:**
```
  org/tier1_exec/1.0.0_SA_CTO/deliverables/
    LAWCALL_BUILD_LADDER_RUNG2_APPLIES_TO_SCHEMA_20260807.md   12,613 B
    Author 1.0.0_SA_CTO~D, co-signed 4.0.0_SA_CRO (the party who committed the error)
    Status: "PROPOSAL. NOT LANDED. Andrew's rule, Andrew's call."
```
>> ⛔ **THIS FEATURE MUST BUILD ON THAT CALL OR SUPERSEDE IT EXPLICITLY. IT MUST NOT BE WRITTEN
   AROUND.** Landing a second rule on the same rung while the first sits unanswered is exactly the
   duplicate-build failure the feature exists to prevent — **committed by the feature itself.** <<
⭐ **AND ITS WORKED CASE IS THE BEST EVIDENCE EITHER TIER HAS.** A seat ran Build-Ladder rung 2
**CORRECTLY, TWICE, AGAINST CODE** — then spent three revisions designing an ontology layer whose
every capability was **already live on 961 GRAPH EDGES.** Their own words:
> *"Rung 2 says 'the estate already has it' and I read 'it' as CODE."*

**That is the CTO-tier failure mode in one sentence: the check RAN and PASSED, and the prior art was
in a different ARTIFACT CLASS.**

## 3. ⛔ THE BINDING CONSTRAINT — TWO CHECKS, TWO INSTRUMENTS, OR THE SECOND IS THEATRE

`0.0.0_AB_MSTR~Z` named this and declined to answer it. It is the whole design problem.
> **CLAUDE.md Rule 22:** *"A second seat's confirmation via the FIRST seat's method is REPETITION,
> not corroboration — name your instrument and whether it differs."*

>> ⛔ **TWO PRIOR-ART CHECKS THAT BOTH RUN `comp-which` OVER THE SAME NOUNS ARE N SEATS ON ONE RUNG:
   N TIMES THE CONFIDENCE AND ZERO EXTRA COVERAGE.** If the tiers cannot be given different
   instruments, the honest outcome is ONE check, not two. <<
✅ **His own words already separate them: "CTO broadly" vs "operational in the context of NEW/REUSE
OPERATIONAL BUILD." Those are different QUESTIONS, so they get different SURFACES.**

## 4. THE PROPOSED SPLIT — different question, different corpus, different failure mode

```
  TIER          QUESTION                          CORPUS (the instrument)          FAILS WHEN
  CTO @ PRD     "does this CAPABILITY already     code + infra + GRAPH EDGES +     the capability
                 exist ANYWHERE, in ANY artifact   ratified terms + declared        exists in an
                 class?"                           schemas + docs/doctrine          UNSEARCHED CLASS
  COO @ TO      "is someone ALREADY BUILDING       open+closed TOs, decomp cells,   a predecessor
                 this, or did someone START        .open_findings, change_mgmt      EXISTS and is
                 AND STOP?"                        ledgers, project registry        not RUNNING
```
⭐ **THE COO TIER IS NOT A SMALLER VERSION OF THE CTO TIER — IT READS A DIFFERENT CORPUS ENTIRELY.**
The CTO tier searches ARTIFACTS THAT EXIST; the COO tier searches **RECORDS OF WORK**, which is the
only place a half-finished or abandoned build is visible. **A capability search cannot see an
abandoned TO, and a TO census cannot see 961 graph edges.** That is what makes them two checks
rather than one repeated.

## 5. THE COO-TIER FAILURE MODE, WITH THREE MEASURED INSTANCES — ALL FROM ONE NIGHT

```
  (a) 2026-08-29 ~03:3xZ  D1_CATVIEWS.TO-A3-DS was CUT, and TWO MINUTES LATER a peer measured
      that its central question was ALREADY ANSWERED in the producer -- first in a docstring,
      then (that being stale) in a ROSTER the ETL calls its own source of truth.
  (b) SAME HANDOFF  INC3-B was proposed as "re-run the pipeline across the full account set."
      A re-run REPRODUCES the single-account result: the real work is a DISCOVERY build.
      A TO cut on the proposed wording would have carried an acceptance that CANNOT BE MET.
  (c) BANKED IN /mstr-spawn 1d-ii  a lane was seated to "RESUME" three TOs that were BUILT,
      ACCEPTED 15/15, CERTIFIED and ON ORIGIN ~7h earlier. The pre-flight passed every check
      it had, because every check it had reads PROCESS state, not COMPLETION state.
```
>> ⛔ **(c) IS THE SHAPE THAT MATTERS: the query returned `total=3 ... unresolved_serials=0` — a
   TRUSTWORTHY COUNT THAT WAS WRONG ABOUT THE WORLD, and nothing in the output flags that. A false
   zero eventually announces itself; a TRUE COUNT OF STALE RECORDS NEVER DOES.** <<

## 6. COST AND NON-APPLICATION — required by CLAUDE.md, and this is where the rule earns its place

```
  COST      the COO tier is a RECORDS census at TO-CUT TIME ONLY. It reads task_orders/,
            decomp runs, .open_findings/, change_management/ and org/projects/. It does NOT
            search the estate for code and does NOT run at commit time, at execution time,
            or on any existing TO. Bounded by construction: the corpus is the size of the
            work record, not the size of the repo.
  DOES NOT  apply when the TO's own decomp cell NAMES the predecessor artifact it continues.
   APPLY    Declared continuity discharges the check by reading it -- prior art that is
            already cited is not prior art that was missed.
```
⛔ **AND IT MUST NOT BECOME A GATE.** CLAUDE.md: *"NEVER implement an approval gate on any work unless
Andrew explicitly asks."* **He asked for a CHECK, not a gate.** The proposed shape is a REQUIRED FIELD
on a cut TO — one line naming what was searched and what was found — not a refusal that blocks the cut.
**A field a reader can reject on beats a gate nobody can see.**

## 7. WHAT IS OPEN, AND WHAT I AM NOT DECIDING

⛔ **NOT DECIDED HERE, because it is the unlanded call's subject:** whether Build-Ladder rung 2's
*"the estate already has it"* names a CLASS rather than enumerating code. **That is `1.0.0_SA_CTO~D`
and `4.0.0_SA_CRO`'s call from 2026-08-07 and it is Andrew's to land.** This design DEPENDS on it: if
rung 2 already means "any artifact class," the CTO tier is a restatement of existing law and only the
COO tier is new.
⚠ **OPEN QUESTION FOR `1.0.0_SA_CTO~Z`:** does the CTO tier have an instrument that spans artifact
classes TODAY, or does one have to be built? **`comp-estate --layers/--definitions` and the graph are
candidates; I have not tested whether either reaches the 961-edge class the worked case names, and I
am not asserting that they do.**
