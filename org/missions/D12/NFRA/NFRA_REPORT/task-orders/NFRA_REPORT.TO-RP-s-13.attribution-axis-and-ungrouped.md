# NFRA_REPORT.TO-RP-s-13 -- The PROPERTY+OWNER ATTRIBUTION axis and its mandatory rendered UNGROUPED value

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md</decomp_doc>
<owned_cells>RP-s-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~2</issued_to>

## THE CELL, INLINED IN FULL (manifest row S13; outcome FWD-4; acceptance property 3)

```
RP-s-13 mirrors manifest row S13. ACT: every finding rolls up to a NAMED part of the business
with an owner, and a live surface that no ratified group covers renders a MANDATORY, EXPLICIT
`UNGROUPED` value -- shown in plain sight, never omitted and never guessed into a group.
THIS IS THE ONLY STRUCTURALLY UNCOVERED OUTCOME OF ROUND 1. S13 was split out of S1 after round 1's
issuance, so no round-1 cell ever served FWD-4.
```

## DEPENDENCIES

This cell depends on: none -- this cell is a ROOT and is ready at issuance.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word and never to a merge.

## BOUNDS -- what this cell may not cross

```
FWD-4's ACCEPT was RE-CUT at L4 and you build against the NEW text, not the endpoint's older
one: "Every problem belongs to a named part of the business and names who would fix it. Anything we run
that has no part named for it yet is shown as not-yet-grouped, in plain sight, and is never quietly
left out."
THE MEMBER NAMES ARE AN OPEN CALL AT ANDREW -- is the third property Gateway, Graph, or BOTH (a
four-member axis)? DO NOT DECIDE IT AND DO NOT GUESS. `UNGROUPED` is precisely what makes this cell
buildable without that answer, and Andrew's eventual naming must not invalidate what you build.
Two live surfaces are known to have no ratified group today: `opal-gateway` and `canonical-schwab-si2`.
Render them UNGROUPED rather than assigning them.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-schedule (round 2, re-run): C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED, NEITHER this
project's. No gate binds this cell.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_NFRA_REPORT_ROUND1_20260910.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-13.attribution-axis-and-ungrouped.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-13"><invocation>grep -c 'UNGROUPED' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md</invocation><expect>a count of 2 or greater</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-13"><invocation>grep -c -E 'opal-gateway|canonical-schwab-si2' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md</invocation><expect>a count of 2 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-13"><invocation>grep -c -i -E 'open call|not decided|Andrew' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md</invocation><expect>a count of 1 or greater</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the axis renders an explicit UNGROUPED value
- **AC2** (mechanical): the two known ungrouped surfaces are shown rather than assigned
- **AC3** (mechanical): the member names are left open rather than decided

Every invocation runs under `timeout 120`; a timeout is recorded AS the output, so keep every invocation bounded.

⚠ THE MECHANICAL CRITERIA ABOVE ARE MOSTLY WORD-PRESENCE GREPS AND THEY ARE THE FLOOR, NOT THE BAR.
Three of round 1's twelve orders carried a criterion that could not test what it was written to test --
an under-cut cell, a wrong interpreter, and an OR-alternation counted by line. The cell's ACT is the bar.
If a criterion passes on a deliverable that does not do the ACT, say so in your report rather than
letting the grep stand in for the work.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>staged</status>
<round>2</round>
<sub_round>A</sub_round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
comp-schedule: RUN -- re-run at the round-2 cut, 5 of 5 carriers; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED (G-3 CTO, G-7 POD4), NEITHER this project's.
comp-iam: RUN -- re-run at the round-2 cut; 12 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 31 services; BLIND on wafv2, the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- on the round-2 decomposition; 1 of 1 cited commit VERIFIED, 1 of 1 cited path stable, 0 file:line cites; BLIND on the decomposition neighborhood (T11 NOT RESOLVED -- a DECOMP carries no decomp_ref), so its packet digested 12 of 420 filesystem siblings and is NOT evidence about these cells; class census S1/S2/S3 all 0 of 420, which is itself the clean signal.
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 2) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** round 1 CLOSED at L10 -> `1.0.0_SA_CTO~Z` round-N analysis @9dae635237 -> L5 recut `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md` -> this issuance.
