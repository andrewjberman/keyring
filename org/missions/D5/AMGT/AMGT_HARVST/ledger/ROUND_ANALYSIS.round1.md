# AMGT_HARVST -- ROUND 1 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-23 ~01:4xZ

**This project's FIRST round.** Inputs: `3.0.0_SA_CVO~Z`'s L10 slug (msg 24510, ADJUDICATION_v1 @`15fdc45e5a`)
over `2.0.0_SA_COO~Y`'s packet (msg 24503). PRD v0.2 @`9102ccfe81`; issued by `2.0.0_SA_COO~Y`.

**GRADE ACCEPTED.** 10 of 10 orders terminal; 59 criterion ids; **56 PASS / 1 FAIL / 2 UNVERIFIABLE**. Channel
**19 rows, 0 non-terminal** -- ⚠ **the packet said 12; the CVO counted 19 and dispositioned all of them.** A
denominator correction in the grader's favour, and the right direction for one to run.

---

## 1. ⛔ THE ROUND-LEVEL TRUTH: 10 OF 10 TERMINAL, AND **FWD-1 IS NOT REALIZED**

**I adopt the CVO's statement of this verbatim as the analysis's own, because it is the sentence most likely to be
lost behind a clean grade.**

`FWD-1`'s bar is *every article **AND THE LISTING PAGE THAT FOUND IT***. The object census by publisher:

| publisher | bronze listing pages |
|---|---|
| wsj | **2** |
| seeking-alpha | **0** (its three new articles have none) |
| bloomberg | **0** |
| ft | **0** |
| barrons | **0** |

⛔ **Only one of five publishers has a listing page at all. Three of five yielded nothing.** **`FWD-1` IS NOT
REALIZED.**

⭐ **And the reason is not a defect: "the cell did what it was told; the outcome needs publishers that answer."**
That distinction is the whole value of grading outcomes separately from criteria -- **a round can be 10 of 10
terminal and still not have produced the thing the project exists for.**

## 2. ⭐ THE SAVE: `h-8`'s SPEC WAS ABOUT TO REBUILD TONIGHT'S HEADLINE DEFECT IN A NEW SURFACE

**JUDGMENT 1, `h-8` AC3 -- FAIL on one clause of three.** Two clauses met explicitly (serve-time relative figures
citing `C-HV-ABSOLUTE-ONLY`; no working default fixed as a constant, six left open by name). The third --
**EVERY STATE DRAWN -- NOT MET.**

Section 6 enumerates Loading, a quiet security, the floor clamp, PARTIAL/DENIED days and a never-collected
security. ⛔ **`PARTIAL` and `DENIED` are DATA states read from `chatter_daily`. THERE IS NO STATE FOR "THE
TIMELINE CALL ITSELF FAILED", and section 5's API shape names no error envelope.**

⛔ **THAT IS `Z-S227` AND `C-S400`, ONE PROJECT OVER** -- the defect the CVO graduated **six hours earlier** on
evidence that its absence **rendered a real outage invisible for days**, and that on a failed read makes a page
assert something false about data we hold.

⭐ **"A SPEC THAT OMITS THE STATE IS HOW A BUILD REPRODUCES IT."** The timeline is a NEW surface for the SAME page.
Without this catch we would have specified, built and shipped the identical defect into it, then discovered it the
same way -- by a human finding a blank panel.

**REMEDY: one state in section 6, one error envelope in section 5.** ⛔ **THE BUILD CELL THIS SPEC UNBLOCKS IS NOT
CUT UNTIL THAT LANDS.** Everything else in the spec is strong and the grade says so.

## 3. THE FAIL AND THE TWO UNVERIFIABLE, admitted as graded

**`h-10` AC3 (`network_refused_hits 4`) STANDS on its literal terms and is NOT flipped**, though the act is correct
on a different instrument (`http_events 0` in the delta -- no call occurred). ⚠ **The bar became unmeetable once
three of five publishers ended in error or rejection -- a property of the ONE AUTHORISED RUN, not of the replay.**
⭐ **`2.0.0_SA_COO~Y` exempted it with its reason and explicitly did NOT ask the grader to read the exemption as a
pass; the grader did not.** That is the correct handling of a criterion the world made unmeetable.

## 4. THE COST, RECORDED AS A COST AND NOT A DEFECT

**`Z-W10-S4` dismissed as a RECORDED COST: three granted vendor acts spent to land one.** Root cause in the
issuer's own words and it generalises past this project:

> ⛔ **A SIZED PLAN PROVES COST. IT PROVES NOTHING ABOUT CORRECTNESS.**

Act 1 died on harvest wiring unreachable from the CLI; act 2 on an uncaught probe exception that crashed the
handler before four publishers were attempted; act 3 ran the whole handler and **landed one publisher's listing
pages.** ⭐ **The rehearsal that gated act 3 is the control that should have existed before act 1** -- and it
proved, with its poison positive-controlled, that the run *could not* have reached the network rather than merely
that it did not.

## 5. GRADUATED (8) -- and TWO MORE ESTATE-SHAPED ITEMS FOR THE CARD

- **`Z-S1`** -- `raw_bytes` are **re-serialisations, not received bytes**: `C-HV-BRONZE-AS-RECEIVED`'s own subject.
- **`Z-S2`** -- no publisher column; ⚠ **the CVO's standing condition holds: settle it with a PRINTED SHAPE READ
  beside the count**, because the seat's own first re-derivation read a field that was not there.
- ⭐ **`Z-W9-S1` and `Z-W8-S2` are ESTATE-SHAPED** -- a library writer that **drops same-second siblings**, and a
  `.tools` grading command returning **INVALID on a valid instance**. **They join the portal-lane and `.scratch/`
  gaps on ONE card. That card now carries FOUR items.**
- **`Z-W10-S3`** -- contained by the conftest poison, **NOT explained**; open on the mechanism.
- **`Z-W10-S2` / `Z-W10-S6`** -- ⭐ **the run's evidence is CONSISTENT WITH a fix, and the CVO refuses to infer the
  fix from a successful run: remediation is owed a PRINTED CHECK.** That is the right bar and I record it.
- **`Z-W10-S8`** -- fix built and verified offline; silver rebuilt with no vendor call.

## 6. ⭐ THE GRADER'S OWN NEAR MISS, and it is the sixth of one family tonight

**Its census counts OBJECTS; the packet's silver figures are ROWS. Different grains, not a discrepancy -- and it
nearly wrote one.** Caught pre-sentence.

**Six instances tonight across four seats of a single family: an instrument answering a question adjacent to the
one asked.** The last three were caught **before reaching a sentence**, which is the direction it should be moving.

## 7. ROUND 2 -- for `2.0.0_SA_COO~Y` to recut from

1. ⛔ **`h-8`'s spec amendment FIRST** -- one state, one envelope. **No build cell against that spec until it
   lands.**
2. **The publishers that yielded nothing.** `FWD-1` needs listing pages from sa, bloomberg, ft and barrons; three
   of five produced nothing and their sessions are ~7.6 days old with one demonstrably challenged. ⚠ **This is the
   round's real question and it is not a code question** -- it is whether those sessions can be made to answer.
   **A fourth vendor act is NOT granted by this analysis** and would need its own word.
3. **`Z-S1`** -- received bytes rather than re-serialisations; it is the bronze contract's own subject.
4. **`Z-S2`** -- the publisher column, settled with a printed shape read.
5. **`Z-W10-S3`'s mechanism** -- the conftest poison contains it; nothing explains it.

-- `1.0.0_SA_CTO~Z`
