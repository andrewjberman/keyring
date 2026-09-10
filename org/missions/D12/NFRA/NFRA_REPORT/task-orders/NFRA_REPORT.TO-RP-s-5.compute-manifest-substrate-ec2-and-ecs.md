# NFRA_REPORT.TO-RP-s-5 -- The COMPUTE MANIFEST as a reporting substrate -- EC2 and ECS, duty cycle, autoshutdown, always-on by group

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md</decomp_doc>
<owned_cells>RP-s-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~2</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-9; acceptance property 4)

```
RP-s-5 mirrors manifest row S5. ACT: make one record answer "what compute do we run, and what
shuts itself down", spanning BOTH kinds of compute, each unit's duty cycle and autoshutdown state, and
the always-on set NAMED BY GROUP (Dashboard, Website, Graph) per Andrew's ruling 15b.
MEASURED STARTING STATE, from the L1 brief F8 and carried here rather than re-derived: 27 declared
services; 18 of 27 rows carry a LIFECYCLE WORD where a MACHINE TYPE belongs; two services share an id;
THE MANIFEST IS EC2-ONLY AND ECS IS ABSENT ENTIRELY; the manifest is itself 2014.2h old.
This is a PORT verb: reuse sync-ec2-manifest.sh, do not re-buy it (build ladder rung 2).
```

## DEPENDENCIES

This cell depends on: none -- this cell is a ROOT and is ready at issuance.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word.

## BOUNDS -- what this cell may not cross

```
BUILD LADDER: the estate already holds sync-ec2-manifest.sh. QUERY AND EXTEND, NEVER REBUILD.
Andrew's ruling 15b: the always-on exception set is named BY GROUP, not by box. moltbot is NOT in it --
it was torn down 2026-06-29 and independently verified gone; its absence from the manifest is CORRECT
and is not a gap to backfill.
OPEN SUB-ITEM, carried not resolved: no graph-ops box appears in the 27-service manifest and the
security sweep reports 7 unused opal-globgrph-* security groups, so the Graph group MAY BE EMPTY. An
empty group is a legitimate finding -- record it, do not manufacture a member.
THIS CELL IS EC2/ECS ENUMERATION ONLY. It creates no alarm, no monitor and no notification.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam: no cell of this decomposition creates, changes or requires an IAM grant. If this
cell appears to need one, STOP and file a surprise ROW -- do not add a permission.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
infra/aws/ec2/EC2_MANIFEST.json
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-5.compute-manifest-substrate-ec2-and-ecs.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-5"><invocation>test -f infra/aws/ec2/EC2_MANIFEST.json && echo PRESENT</invocation><expect>the literal string PRESENT</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-5"><invocation>grep -c -E '[0-9]+ of [0-9]+' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COMPUTE_MANIFEST_FINDINGS.md</invocation><expect>a count of 1 or greater -- a coverage claim with no denominator fails FWD-10's discipline</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-5"><invocation>grep -c -i 'ECS' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COMPUTE_MANIFEST_FINDINGS.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC6" cell_refs="RP-s-5" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the EC2 manifest is readable at the path the deliverable cites
- **AC2** (mechanical): the deliverable states a denominator for services covered
- **AC3** (mechanical): ECS is addressed explicitly rather than silently omitted
- **AC6** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): Whether the schema fix correctly separates MACHINE TYPE from LIFECYCLE on the 18 of 27 rows that conflate them, and whether the always-on set is correctly grouped. Graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6) · **Project:** NFRA_REPORT · **Directive:** D12 · **PRD:** v0.2 @1703e825d0
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @37ff80867a -> L2/L3/L4 `1.0.0_SA_CTO~Z` -> L5 `2.0.0_SA_COO~ZZ` decomp @c34501140e -> L6 this issuance.
**Provenance:** the cell text mirrors PRD section 8 row S5; nothing in that manifest was re-measured at L4, so every `measured` claim carries the BRIEF's vintage @37ff80867a and this order's L5 battery re-grounds what it cites.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers scanned; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED, NEITHER this project's (G-3 CTO, G-7 POD4); C5's 137 non-null blocking fields are a READING LIST and are not counted as gates.
comp-iam: RUN -- 836 calls verdicted across 96 mapped roles over 31 services; 630 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED not CLEARED), 11 UNGRANTED, 266 calls in 26 role-UNMAPPED services NOT resource-checked; BLIND on wafv2 (coverage-unknown), the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- 2 of 2 cited commits VERIFIED, 2 of 2 cited paths stable, 0 file:line cites; BLIND on the decomposition neighborhood (a DECOMP carries no decomp_ref) so it digested 12 of 13 filesystem siblings instead of the dependency chain, and its packet is therefore not evidence about these cells.
</preflight>

**Preflight disposition:** mandatory core RUN at L5 (comp-schedule C1=23/C2=7/C3=12/C4=20/C5=335; comp-iam 836 calls/96 roles/31 services; comp-adversary 2 of 2 commits VERIFIED with a declared neighborhood blindness). Non-core lenses DECLARED-NOT-APPLICABLE -- this cell touches no route, cache key, shared component or gold-pipeline I/O.
