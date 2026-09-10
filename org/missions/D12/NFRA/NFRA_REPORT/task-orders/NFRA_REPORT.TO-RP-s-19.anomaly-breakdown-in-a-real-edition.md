# NFRA_REPORT.TO-RP-s-19 -- The ANOMALY BREAKDOWN in a real edition, plus AMENDMENT (b) -- C-AI's grain is the REPORT

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md</decomp_doc>
<owned_cells>RP-s-19</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~2</issued_to>

## THE CELL, INLINED IN FULL (manifest row S12; outcome FWD-12; acceptance property 3, 5)

```
RP-s-19 mirrors manifest row S12. ACT: an anomalous row IN A REAL EDITION carries its connected
resources -- what feeds it, what reads it, what else would be affected -- plus a few sentences on what
appears to be happening, so nobody must assemble that picture before judging it.
AND AMENDMENT (b), RULED AT L4 (analysis section 4(b)): C-AI's "a generated part is never the sole
carrier of a fact" holds at the REPORT GRAIN. The reader's artifact is the report; a deliverable is an
intermediate nobody reads at the morning read. RECORD THAT GRAIN so no future grader re-litigates it at
a stricter one and fails a cell that met the intended bar.
```

## DEPENDENCIES

This cell depends on: RP-s-15.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word and never to a merge.

## BOUNDS -- what this cell may not cross

```
C-AI PARTS 1 AND 2: every region declared COMPUTED / GENERATED / QUOTED; the breakdown is
COMPUTED from the dependency graph and the analysis beside it is GENERATED and is a READING of that
evidence. The written account must assert NOTHING THE BREAKDOWN DOES NOT SUPPORT.
BUILD-LADDER RUNG 2: the estate holds a dependency graph with a call manifest. QUERY IT, NEVER REBUILD.
BOUND EVERY INVOCATION -- an unbounded graph sweep is killed at 120s and the timeout becomes the
evidence.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
ROUND 1 ESTABLISHED TWO INSTRUMENT LIMITS THAT BIND THIS CELL HARDER THAN ANY OTHER, and
both are recorded at org/modules/graph/INSTRUMENT_LIMITS.md: comp-blast's served graph models NO edge
between GOLD_SCRIPT and Lambda/portal nodes (positive-control-confirmed on a live lambda with zero
`gold:` ancestors), and comp-pipescript's static parser misses dynamically-constructed write keys.
NEITHER INSTRUMENT IS FIXED -- that document is a RECORD OF A GAP, NOT A REPAIR, and must not be cited
as though the instrument improved. A breakdown built on an enumerator blind to a whole edge class
renders confident, complete-looking and wrong, and a missing EDGE leaves no gap a reader can see. Carry
a per-row "what this query cannot see" limb, as round 1's breakdown cell did.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_NFRA_REPORT_ROUND1_20260910.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/modules/graph/graph-call-manifest.yaml
org/modules/graph/INSTRUMENT_LIMITS.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-19.anomaly-breakdown-in-a-real-edition.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ANOMALY_IN_EDITION.md`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-19"><invocation>test -f org/modules/graph/graph-call-manifest.yaml && echo PRESENT</invocation><expect>the literal string PRESENT</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-19"><invocation>grep -c -E 'COMPUTED|GENERATED|QUOTED' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ANOMALY_IN_EDITION.md</invocation><expect>a count of 3 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-19"><invocation>grep -c -i -E 'report grain|grain is the report|REPORT GRAIN' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ANOMALY_IN_EDITION.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC4" cell_refs="RP-s-19" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the call manifest is readable -- the graph was queried, not rebuilt
- **AC2** (mechanical): every region is declared COMPUTED, GENERATED or QUOTED
- **AC3** (mechanical): the C-AI grain is recorded as the REPORT
- **AC4** (JUDGMENT -- never self-graded; record UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): Whether the breakdown's per-row 'cannot see' limb is honest against the two recorded instrument limits -- i.e. whether a reader could mistake an unmodelled edge for an absent one. Graded by 3.0.0_SA_CVO~Z at L9.

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
