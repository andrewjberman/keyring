# NFRA_REPORT.TO-RP-s-12 -- The ANOMALY BREAKDOWN -- connected resources COMPUTED, the written account GENERATED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md</decomp_doc>
<owned_cells>RP-s-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-12; acceptance property 3, 5)

```
RP-s-12 mirrors manifest row S12. ACT: when something looks wrong, a reader sees what it is connected
to -- what feeds it, what reads it, what else would be affected -- and a few sentences on what appears
to be happening. Nobody has to assemble that picture themselves before they can judge it.
```

## DEPENDENCIES

This cell depends on: RP-s-1, RP-s-11.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word.

## BOUNDS -- what this cell may not cross

```
C-AI PARTS 1 AND 2, and they are the cell's spine:
DECLARED PER REGION -- every part is COMPUTED, GENERATED or QUOTED, legible without knowing how the
report is built.
A GENERATED PART MAY NEVER BE THE SOLE CARRIER OF A FACT. The connected-things breakdown is COMPUTED
(it comes from the dependency graph); the analysis beside it is GENERATED and is a READING OF that
evidence. STRIP EVERY GENERATED SENTENCE AND THE REPORT MUST STILL BE TRUE AND STILL CHECKABLE.
The bar was TIGHTENED before landing: the written account must assert NOTHING THE BREAKDOWN DOES NOT
SUPPORT. Read the PRD's version, not the L2 endpoint's earlier one.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
BUILD-LADDER RUNG 2 BEFORE ANY BUILD, and the PRD says so in terms: the connected-things half is
VERY LIKELY A QUERY, NOT A BUILD. The estate already holds a dependency graph with a call manifest, and
CLAUDE.md rule 20 says QUERY IT, NEVER REBUILD; a blast-radius surface already exists. Pick from
org/modules/graph/graph-call-manifest.yaml; read the provenance header; never rebuild the graph.
BOUND EVERY INVOCATION -- an unbounded graph sweep is killed at 120s and the timeout becomes the
evidence.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/modules/graph/graph-call-manifest.yaml
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-12.anomaly-breakdown-computed-plus-account.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-12"><invocation>test -f org/modules/graph/graph-call-manifest.yaml && echo PRESENT</invocation><expect>the literal string PRESENT</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-12"><invocation>grep -c -E 'COMPUTED|GENERATED|QUOTED' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ANOMALY_BREAKDOWN.md</invocation><expect>a count of 3 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-12" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the dependency graph was QUERIED rather than rebuilt -- the call manifest is readable
- **AC2** (mechanical): every region of the deliverable is declared COMPUTED, GENERATED or QUOTED
- **AC3** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): Whether stripping every GENERATED sentence leaves the deliverable still true and still checkable -- the C-AI part-2 test, which cannot be decided by a pattern match. Graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>4</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6) · **Project:** NFRA_REPORT · **Directive:** D12 · **PRD:** v0.2 @1703e825d0
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @37ff80867a -> L2/L3/L4 `1.0.0_SA_CTO~Z` -> L5 `2.0.0_SA_COO~ZZ` decomp @c34501140e -> L6 this issuance.
**Provenance:** the cell text mirrors PRD section 8 row S12; nothing in that manifest was re-measured at L4, so every `measured` claim carries the BRIEF's vintage @37ff80867a and this order's L5 battery re-grounds what it cites.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers scanned; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED, NEITHER this project's (G-3 CTO, G-7 POD4); C5's 137 non-null blocking fields are a READING LIST and are not counted as gates.
comp-iam: RUN -- 836 calls verdicted across 96 mapped roles over 31 services; 630 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED not CLEARED), 11 UNGRANTED, 266 calls in 26 role-UNMAPPED services NOT resource-checked; BLIND on wafv2 (coverage-unknown), the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- 2 of 2 cited commits VERIFIED, 2 of 2 cited paths stable, 0 file:line cites; BLIND on the decomposition neighborhood (a DECOMP carries no decomp_ref) so it digested 12 of 13 filesystem siblings instead of the dependency chain, and its packet is therefore not evidence about these cells.
</preflight>

**Preflight disposition:** mandatory core RUN at L5 (comp-schedule C1=23/C2=7/C3=12/C4=20/C5=335; comp-iam 836 calls/96 roles/31 services; comp-adversary 2 of 2 commits VERIFIED with a declared neighborhood blindness). Non-core lenses DECLARED-NOT-APPLICABLE -- this cell touches no route, cache key, shared component or gold-pipeline I/O.
