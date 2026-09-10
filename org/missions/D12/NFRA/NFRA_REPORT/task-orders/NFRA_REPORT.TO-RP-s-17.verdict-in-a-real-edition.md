# NFRA_REPORT.TO-RP-s-17 -- The VERDICT rendered in a real edition, checkable against that edition's own rows

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md</decomp_doc>
<owned_cells>RP-s-17</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~3</issued_to>

## THE CELL, INLINED IN FULL (manifest row S4; outcome FWD-1; acceptance property 1)

```
RP-s-17 mirrors manifest row S4. ACT: the verdict -- does anything need Andrew today -- is
rendered IN a real composed edition and is CHECKABLE by any reader against the rows beneath it in that
same edition.
ROUND 1 SPECIFIED THE RULE; THIS CELL RENDERS IT. Round 1's verdict cell proved the rule can return
SOMETHING against a real row and NOTHING against a labelled hypothetical, because no edition existed to
draw a real morning from. An edition exists now.
```

## DEPENDENCIES

This cell depends on: RP-s-15.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word and never to a merge.

## BOUNDS -- what this cell may not cross

```
C-AI PART 3: A VERDICT IS COMPUTED, NEVER GENERATED. A model may render it in better English;
it may not decide it.
Andrew's clause (a): the morning read is PURELY DECLARATIVE. No acknowledgement, no escalation, no
required response, no SLA. A verdict that quietly expects a reply makes him the acceptance instrument,
which is the defect FWD-1 was re-cut to remove.
FWD-1's bar needs a correct NEGATIVE eventually -- but you cannot manufacture one. Render the verdict
the real edition's rows actually produce, and if that is SOMETHING, say SOMETHING.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-schedule: no armed gate owned by this project.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_NFRA_REPORT_ROUND1_20260910.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-17.verdict-in-a-real-edition.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/VERDICT_RENDERED.md`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-17"><invocation>grep -c -i -E 'computed|derived' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/VERDICT_RENDERED.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-17"><invocation>grep -c -i -E 'checkable|traceab|because' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/VERDICT_RENDERED.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-17"><invocation>grep -c -i -E 'declarative' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/VERDICT_RENDERED.md</invocation><expect>a count of 1 or greater</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the verdict is rendered in the edition and stated as computed
- **AC2** (mechanical): the verdict is traceable to the specific rows that produced it
- **AC3** (mechanical): the verdict is declarative -- no required action by any reader

Every invocation runs under `timeout 120`; a timeout is recorded AS the output, so keep every invocation bounded.

⚠ THE MECHANICAL CRITERIA ABOVE ARE MOSTLY WORD-PRESENCE GREPS AND THEY ARE THE FLOOR, NOT THE BAR.
Three of round 1's twelve orders carried a criterion that could not test what it was written to test --
an under-cut cell, a wrong interpreter, and an OR-alternation counted by line. The cell's ACT is the bar.
If a criterion passes on a deliverable that does not do the ACT, say so in your report rather than
letting the grep stand in for the work.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>staged</status>
<round>2</round>
<sub_round>B</sub_round>
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
