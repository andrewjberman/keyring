# NFRA_REPORT.TO-RP-s-18 -- The RETIREMENT ROUND-TRIP -- something retired, and the NEXT edition stops raising it

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md</decomp_doc>
<owned_cells>RP-s-18</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~1</issued_to>

## THE CELL, INLINED IN FULL (manifest row S8; outcome FWD-7; acceptance property 2)

```
RP-s-18 mirrors manifest row S8. ACT: someone retires a dead thing, says why, puts their name to
it -- and THE NEXT EDITION STOPS RAISING IT. Anyone can later look up what was retired, by whom, and
for what reason.
ROUND 1 BUILT THE REGISTER; THIS CELL CLOSES THE LOOP. Its register already carries 0 RETIRED and 5
CARRIED rows, and 0 RETIRED is the TRUE number -- round 1's deprecation walk found nothing dead. The
round-trip is what FWD-7's bar actually asks for: a retirement that visibly changes the next edition.
```

## DEPENDENCIES

This cell depends on: RP-s-15, RP-s-16.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word and never to a merge.

## BOUNDS -- what this cell may not cross

```
THIS PROJECT CLASSIFIES; IT DOES NOT DELETE. Retiring SERVED OUTPUT still needs never-widen
sign-off (CTO+COO). A retirement record is a record, not a delete order.
Every row carries OWNER, REASON and DATE -- all three, together, on the same row. A terminal status
without its pointer is the rot with a tidier label.
IF NOTHING IS GENUINELY RETIRABLE, SAY SO. Round 1's walk found zero of ten dead; manufacturing a
retirement to demonstrate the mechanism would put a false row in a permanent register. A CARRIED item
suppressed from daily re-derivation is the honest demonstration if no RETIRED one exists.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-schedule: no armed gate owned by this project. The alerting moratorium is ARMED; this
cell records state and mints nothing.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_NFRA_REPORT_ROUND1_20260910.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-18.retirement-round-trip-across-editions.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/RETIREMENT_ROUNDTRIP.md`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-18"><invocation>grep -c -i -E 'next edition|subsequent edition|round-trip' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/RETIREMENT_ROUNDTRIP.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-18"><invocation>grep -c -i -E 'owner' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/RETIREMENT_ROUNDTRIP.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-18"><invocation>grep -c -i -E 'never-widen|classif' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/RETIREMENT_ROUNDTRIP.md</invocation><expect>a count of 1 or greater</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the round-trip is demonstrated across two editions
- **AC2** (mechanical): owner, reason and date are all required together
- **AC3** (mechanical): the classify-not-delete bound is stated

Every invocation runs under `timeout 120`; a timeout is recorded AS the output, so keep every invocation bounded.

⚠ THE MECHANICAL CRITERIA ABOVE ARE MOSTLY WORD-PRESENCE GREPS AND THEY ARE THE FLOOR, NOT THE BAR.
Three of round 1's twelve orders carried a criterion that could not test what it was written to test --
an under-cut cell, a wrong interpreter, and an OR-alternation counted by line. The cell's ACT is the bar.
If a criterion passes on a deliverable that does not do the ACT, say so in your report rather than
letting the grep stand in for the work.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>staged</status>
<round>2</round>
<sub_round>C</sub_round>
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
