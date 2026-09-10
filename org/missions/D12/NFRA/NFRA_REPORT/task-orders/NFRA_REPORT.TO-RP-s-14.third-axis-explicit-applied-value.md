# NFRA_REPORT.TO-RP-s-14 -- AMENDMENT (a) -- a fully-applied row renders an EXPLICIT value on the third axis

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md</decomp_doc>
<owned_cells>RP-s-14</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~3</issued_to>

## THE CELL, INLINED IN FULL (manifest row S1; outcome FWD-2; acceptance property 2)

```
RP-s-14 mirrors manifest row S1. ACT: amend the state model so a fully-applied row renders an
EXPLICIT value on the third axis (`state: desired | applied | exercised`) instead of rendering nothing.
RULED AT L4 by the round-N analysis section 4(a): ABSENCE MAY NOT CARRY MEANING ON THIS AXIS.
STATE_MODEL.md s.5's RULE says the axis renders only when NOT `applied`; s.7's SPECIMEN prints a
literal marker. They disagree about what a fully-applied row looks like.
THE SPECIMEN IS CORRECT AND THE RULE IS THE DEFECT. AMEND THE RULE, NOT THE SPECIMEN.
```

## DEPENDENCIES

This cell depends on: none -- this cell is a ROOT and is ready at issuance.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word and never to a merge.

## BOUNDS -- what this cell may not cross

```
THIS IS FWD-2'S OWN PRINCIPLE ONE AXIS OVER: not being able to see something must never look
like seeing something. A blank that means "applied" is indistinguishable from a blank a broken renderer
left behind, and the whole project exists to remove exactly that confusion.
DO NOT EDIT, REMOVE OR REDEFINE ANY OF RULING 12's SIX RATIFIED AXIS-1 VALUES or the three axis-2
values. This amendment touches the THIRD axis's rendering rule only.
STATE_MODEL.md is round 1's committed deliverable. You are amending it in place, not rewriting it.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam is BLIND to wafv2 -- the plane C-SENTINEL-STATE lives on -- so comp-iam silence is
never evidence about the sentinel's enforcement path. Unchanged from round 1 and it still binds.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_NFRA_REPORT_ROUND1_20260910.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-14.third-axis-explicit-applied-value.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-14"><invocation>grep -c -i -E 'explicit' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-14"><invocation>grep -c -E 'desired|applied|exercised' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md</invocation><expect>a count of 3 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-14"><invocation>grep -o -E 'DENY-BY-DESIGN' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md</invocation><expect>the literal string DENY-BY-DESIGN</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the amended rule requires an explicit value when applied
- **AC2** (mechanical): all three third-axis values survive the amendment
- **AC3** (mechanical): the six ratified axis-1 values are untouched -- the least-used one is the probe

Every invocation runs under `timeout 120`; a timeout is recorded AS the output, so keep every invocation bounded.

⚠ THE MECHANICAL CRITERIA ABOVE ARE MOSTLY WORD-PRESENCE GREPS AND THEY ARE THE FLOOR, NOT THE BAR.
Three of round 1's twelve orders carried a criterion that could not test what it was written to test --
an under-cut cell, a wrong interpreter, and an OR-alternation counted by line. The cell's ACT is the bar.
If a criterion passes on a deliverable that does not do the ACT, say so in your report rather than
letting the grep stand in for the work.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>complete</status>
<round>2</round>
<sub_round>A</sub_round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
comp-schedule: RUN -- re-run at the round-2 cut, 5 of 5 carriers; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED (G-3 CTO, G-7 POD4), NEITHER this project's.
comp-iam: RUN -- re-run at the round-2 cut; 12 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 31 services; BLIND on wafv2, the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- on the round-2 decomposition; 1 of 1 cited commit VERIFIED, 1 of 1 cited path stable, 0 file:line cites; BLIND on the decomposition neighborhood (T11 NOT RESOLVED -- a DECOMP carries no decomp_ref), so its packet digested 12 of 420 filesystem siblings and is NOT evidence about these cells; class census S1/S2/S3 all 0 of 420, which is itself the clean signal.
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 2) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** round 1 CLOSED at L10 -> `1.0.0_SA_CTO~Z` round-N analysis @9dae635237 -> L5 recut `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md` -> this issuance.
