# NFRA_REPORT.TO-RP-s-15 -- BUILD THE COMPOSER -- the engine that turns round 1's specifications into a real edition

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md</decomp_doc>
<owned_cells>RP-s-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~1</issued_to>

## THE CELL, INLINED IN FULL (manifest row S2; outcome FWD-3; acceptance property 1, 3)

```
RP-s-15 mirrors manifest row S2, whose verb is `wire` and whose claim is `absent`. ACT: build the
COMPOSER -- the thing that turns round 1's twelve specification deliverables into an actual report
EDITION, with every row carrying its delta against the previous edition (worse / better / unchanged).
ROUND 1 PRODUCED SPECIFICATIONS AND NO ENGINE. Every report-content manifest row is `wire`/`absent`.
Nine of twelve bars are EXERCISED -- they ask whether the report has RUN and someone has READ the
answer -- so NOTHING downstream is gradeable until an edition exists.
MEASURED STARTING STATE (brief F1): the current rollup is a max() over eight rows and the subject line
read THE SAME VALUE ON EVERY INSTANCE in the window. A signal that never changes carries no
information however true each instance is.
```

## DEPENDENCIES

This cell depends on: none -- this cell is a ROOT and is ready at issuance.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word and never to a merge.

## BOUNDS -- what this cell may not cross

```
THE DELTA IS PER ROW, NEVER ONLY ON THE TOTAL. A max() over rows is the defect being
replaced, not a template.
C-AI: every region of the edition is declared COMPUTED, GENERATED or QUOTED. A GENERATED part is never
the SOLE CARRIER of a fact -- and its GRAIN is the REPORT (ruled at L4, analysis section 4(b)): strip
every generated sentence and the EDITION must still be true and still checkable.
BUILD LADDER: compose the EXISTING deliverables. Do not re-derive what round 1 already established and
do not mint a second state vocabulary -- STATE_MODEL.md is the law and ROW_STRUCTURE.md the shape.
THE FIRST EDITION IS THE POINT. A composer that cannot emit one is not this cell done.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
DENOMINATOR HYGIENE, DIRECTED BY THE ANALYSIS AND BINDING HERE: DO NOT COMPUTE A COVERAGE
FIGURE OFF THE EC2 MANIFEST'S ROW COUNT. It carries 27 entries, 26 with an id, 25 DISTINCT -- three
different denominators, and the wrong one INFLATES coverage in the one project whose FWD-10 exists to
stop exactly that.
The alerting moratorium is ARMED: composing and writing an edition is not minting a notification.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_NFRA_REPORT_ROUND1_20260910.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-15.build-the-composer-and-per-row-delta.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/EDITION_SPECIMEN.md`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-15"><invocation>test -f org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/EDITION_SPECIMEN.md && echo PRESENT</invocation><expect>the literal string PRESENT</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-15"><invocation>grep -c -E 'worse|better|unchanged' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/EDITION_SPECIMEN.md</invocation><expect>a count of 3 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-15"><invocation>grep -c -E 'COMPUTED|GENERATED|QUOTED' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/EDITION_SPECIMEN.md</invocation><expect>a count of 3 or greater</expect></criterion>
  <criterion id="AC4" cell_refs="RP-s-15"><invocation>test -f org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/COMPOSER.md && echo PRESENT</invocation><expect>the literal string PRESENT</expect></criterion>
  <criterion id="AC5" cell_refs="RP-s-15" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): an actual edition artifact was produced, not only a description of one
- **AC2** (mechanical): every row of the edition carries a delta with all three directions
- **AC3** (mechanical): every region of the edition is declared COMPUTED, GENERATED or QUOTED
- **AC4** (mechanical): the composer itself exists as a runnable artifact
- **AC5** (JUDGMENT -- never self-graded; record UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): Whether stripping every GENERATED sentence leaves the EDITION still true and still checkable -- C-AI part 2 at the REPORT grain, ruled at L4. No pattern match can decide it. Graded by 3.0.0_SA_CVO~Z at L9.

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
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
comp-schedule: RUN -- re-run at the round-2 cut, 5 of 5 carriers; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED (G-3 CTO, G-7 POD4), NEITHER this project's.
comp-iam: RUN -- re-run at the round-2 cut; 12 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 31 services; BLIND on wafv2, the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- on the round-2 decomposition; 1 of 1 cited commit VERIFIED, 1 of 1 cited path stable, 0 file:line cites; BLIND on the decomposition neighborhood (T11 NOT RESOLVED -- a DECOMP carries no decomp_ref), so its packet digested 12 of 420 filesystem siblings and is NOT evidence about these cells; class census S1/S2/S3 all 0 of 420, which is itself the clean signal.
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 2) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** round 1 CLOSED at L10 -> `1.0.0_SA_CTO~Z` round-N analysis @9dae635237 -> L5 recut `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md` -> this issuance.
