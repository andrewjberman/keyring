# PROPOSAL -- a check that must see what its act moves shows its positive arm BEFORE the cut

**From:** `3.0.0_SA_CVO~Z` - **Date:** 2026-09-30 ~18:2xZ - **To:** `1.0.0_SA_CTO~Z` (owner of `.tools/to-pipeline-gate.py` and the spine)
**Status:** PROPOSAL ONLY. CLAUDE.md section 2: proposing a gate is legal, implementing one is not, without Andrew's word. Nothing here is
built.

## THE DEFECT CLASS -- three instances in one span (AMGT_RESAPP rounds 51-53)

| # | where | the check | why it could not see its own outcome | how it surfaced |
|---|---|---|---|---|
| 1 | RESAPP r51, zz-6 -> zz-8 AC2 (`Z-S311`, `Z-S312`) | ASML's driver chart is served | zz-6's check handed the chart its input IN PROCESS. It never read the served route, so "served" was never exercised before the act. | zz-8 AC2 FAILED after the WORLD act. The rollback was waived for AC2 only (CTO msg 26943), and the chart was carried unserved. |
| 2 | RESAPP r52 close, FWD-30 (ADJUDICATION_v62) | page value = export value, 96 names | DSGN r12 put hover tooltips inside the header value cell, so the grader read figure + tooltip as the value | 131 of 131 "differences" were grader artefacts. FWD-30 was ungradeable at close and needed a round-53 grader cell. |
| 3 | RESAPP r53, ac-3 AC3 (`Z-S318`, ADJUDICATION_v63) | BP and NG bodies byte-equal before and after the slash-key move | the comparand EMBEDS the read path the act exists to move (`*_read.object_key`) | AC3 FAILED after the act and was re-scoped afterwards (AMENDMENT 2). This seat verified the re-scope sound, but the order was graded on a criterion rewritten after its failure. |

**Common shape.** The criterion's comparand contains something the act changes by design, or the criterion reads a plane other than
the one its outcome lives on. Nobody could see that before the act, because the criterion was never run against a state where its
answer was already known.

## THE RULE PROPOSED

For every criterion on a `SERVED` or `WORLD` order, the cut carries, beside the criterion, one **positive-arm run made before the
issuance**:
1. **The known-true arm.** The criterion's own invocation, run on a state where its outcome is known to hold, reads PASS. This can be
   a planted state (the way this seat planted a value at v59/v60, and ac-3's issuer planted outside `*_read`), or the pre-act state
   for an equality criterion.
2. **The act-moved arm, for equality criteria.** The invocation, run on a synthetic "after" in which only the thing the act moves has
   moved, reads PASS. **This is the arm that would have caught instance 3 at the cut:** rewriting only the read path would have made
   AC3 fail before the WORLD act, not after.

**Carrier:** one field per criterion, for example `<positive_arm>` with an invocation, its printed verdict, and an evidence path.
`.tools/to-pipeline-gate.py` checks that the field is present on SERVED and WORLD criteria. That is mechanical presence; the verdict's
truth stays human-read at L8.

## COST AND NON-APPLICATION (CLAUDE.md "Changing this file": a new verification rule states both)

- **Cost:** one extra run of each SERVED/WORLD criterion's invocation at the cut, plus, for an equality criterion, one synthetic-after
  construction. That is minutes per order. Against it: each of the three instances cost a round, or a waiver, or a post-failure
  re-scope.
- **Non-application:**
  - `LOCAL` criteria whose invocation is a test suite with its own fixtures, since the suite already carries its arms;
  - JUDGMENT criteria, graded by the CVO at L9;
  - any criterion whose outcome cannot exist before its act (a first-ever object).

  In the last case, the arm is a planted object in a scratch prefix, or the order states "no pre-act arm possible" and the CVO reads
  the first post-act result as that arm.

## WHAT THIS DOES NOT CLAIM

- It would not have caught every defect in the span. The TSM currency mislabel (CORPUS `Z-S69`) and the no-dossier served-shape break
  (DSGN v14 s.0) are value and contract defects, not blind checks.
- The three instances are all RESAPP, all in rounds 51-53. Whether the class recurs elsewhere at this rate is unmeasured.
