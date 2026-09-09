# NFRA_REPORT.TO-RP-s-9 -- The COST-ANOMALY detector -- SEGMENT grain now, BOX grain after RP-s-5

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md</decomp_doc>
<owned_cells>RP-s-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~2</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-8; acceptance property 4)

```
RP-s-9 mirrors manifest row S9. ACT: make a meaningful jump in what something costs show up, and
ordinary week-to-week wobble not show up, without the reader doing the arithmetic.
MEASURED STARTING STATE (brief F9): cost has NO STANDARD, so it cannot fail. `(untagged)` is $154.21 --
45% of spend and the largest single line.
```

## DEPENDENCIES

This cell depends on: RP-s-5.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word.

## BOUNDS -- what this cell may not cross

```
C-COST-15, Andrew verbatim: "whether there is a material divergence from historical cost for a given
compute box or cost segment... if something moves say 15% or more from its trailing 30 day price".
THE GRAIN SPLIT IS BINDING: SEGMENT grain is available NOW. BOX grain CANNOT be computed until RP-s-5
lands, because the compute manifest is EC2-only with ECS absent entirely. Build the segment limb; state
the box limb as conditioned, and do NOT write it as though box grain were reachable today.
The control half is not optional: a detector that fires on everything passes a one-sided test.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-schedule measured no armed gate owned by this project.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-9.cost-anomaly-detector-segment-then-box.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-9"><invocation>grep -c -E '15%|15 percent' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COST_ANOMALY.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-9"><invocation>grep -c -E '30 ?day|trailing 30' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COST_ANOMALY.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-9"><invocation>grep -c -i -E 'RP-s-5|compute manifest' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COST_ANOMALY.md</invocation><expect>a count of 1 or greater</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the deliverable carries Andrew's threshold verbatim in figures
- **AC2** (mechanical): the trailing window is named
- **AC3** (mechanical): the box-grain limb is marked as conditioned on the compute manifest

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6) · **Project:** NFRA_REPORT · **Directive:** D12 · **PRD:** v0.2 @1703e825d0
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @37ff80867a -> L2/L3/L4 `1.0.0_SA_CTO~Z` -> L5 `2.0.0_SA_COO~ZZ` decomp @c34501140e -> L6 this issuance.
**Provenance:** the cell text mirrors PRD section 8 row S9; nothing in that manifest was re-measured at L4, so every `measured` claim carries the BRIEF's vintage @37ff80867a and this order's L5 battery re-grounds what it cites.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers scanned; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED, NEITHER this project's (G-3 CTO, G-7 POD4); C5's 137 non-null blocking fields are a READING LIST and are not counted as gates.
comp-iam: RUN -- 836 calls verdicted across 96 mapped roles over 31 services; 630 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED not CLEARED), 11 UNGRANTED, 266 calls in 26 role-UNMAPPED services NOT resource-checked; BLIND on wafv2 (coverage-unknown), the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- 2 of 2 cited commits VERIFIED, 2 of 2 cited paths stable, 0 file:line cites; BLIND on the decomposition neighborhood (a DECOMP carries no decomp_ref) so it digested 12 of 13 filesystem siblings instead of the dependency chain, and its packet is therefore not evidence about these cells.
</preflight>

**Preflight disposition:** mandatory core RUN at L5 (comp-schedule C1=23/C2=7/C3=12/C4=20/C5=335; comp-iam 836 calls/96 roles/31 services; comp-adversary 2 of 2 commits VERIFIED with a declared neighborhood blindness). Non-core lenses DECLARED-NOT-APPLICABLE -- this cell touches no route, cache key, shared component or gold-pipeline I/O.
