# NFRA_REPORT.TO-RP-s-1 -- The report's STATE MODEL -- the two-axis vocabulary, and the two states it cannot yet express

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md</decomp_doc>
<owned_cells>RP-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-2, FWD-4; acceptance property 2, 3)

```
RP-s-1 mirrors manifest row S1. ACT: establish the two-axis state model as the report's
rendering law, and close the two expressibility gaps the row's own bound column names.
AXIS 1 (THE INSTRUMENT -- did the check happen, and could it), RATIFIED SIX VALUES, verbatim from
ruling 12: CHECKED | BLIND | INERT | COARSE | UNCHECKED | DENY-BY-DESIGN.
AXIS 2 (THE WORLD -- what was found; meaningful ONLY where axis 1 = CHECKED): OK | DEGRADED | BREACH.
GREEN is defined as: every property CHECKED on axis 1 AND OK on axis 2. Nothing is green by virtue of
not having been looked at.
GAP 1 -- PERMANENT vs TEMPORARY BLIND. RESOLVED WITH NO NEW FIELD, ON YAGNI: the ratified enum ALREADY
carries it. DENY-BY-DESIGN means "cannot look, and that is intentional and recorded", which is exactly
the Website row: the blindness is recorded twice (NFRA_OPSEC202609 C-19 and this PRD's
C-WEBSITE-BLIND) and the choice not to remove it is Andrew's own -- "we do whatever we can without
having to engage with GoDaddy". THE WEBSITE SECURITY ROW RENDERS `DENY-BY-DESIGN` WITH ITS REASON
ATTACHED. Do NOT build a `resolvable` field; an earlier draft of this cell proposed one and it was
withdrawn as a second vocabulary for something the first already said.
GAP 2 -- DESIRED-not-APPLIED. A BLOCKED address row is INTENT no IP set enforces. INERT is closest and
still wrong: INERT means a control that CANNOT FIRE, and the sentinel CAN and is deliberately
watch-only. RESOLUTION DIRECTED: a THIRD ORTHOGONAL AXIS carrying CLAUDE.md rule 22's vocabulary
VERBATIM -- `state: desired | applied | exercised` -- rendered only when it is not `applied`. Build
ladder rung 2: the estate already holds this vocabulary. DO NOT MINT A SYNONYM FOR IT.
```

## DEPENDENCIES

This cell depends on: none -- this cell is a ROOT and is ready at issuance.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word.

## BOUNDS -- what this cell may not cross

```
C-FWD2-FIRST: this cell is the critical path into the entire NFRA_OPSEC202609 relationship.
C-WEBSITE-BLIND: the Website security row is settled PERMANENTLY, not pending -- it renders
DENY-BY-DESIGN with its reason attached (see GAP 1 in the cell). It does NOT wait on TO-OP-S-13 and is
NOT a gap awaiting a fix.
C-SENTINEL-STATE: a BLOCKED address is DESIRED, never APPLIED.
DO NOT EDIT, REMOVE OR REDEFINE ANY OF THE SIX RATIFIED AXIS-1 VALUES. RULED at msg 20595: neither
resolution amends ruling 12 -- an orthogonal axis adds no value to either enum, redefines none, and
cannot make the forbidden pair (BREACH or OK on a surface nobody looked at) printable. If the work
seems to require CHANGING a ratified value, STOP and file a surprise ROW.
ONE WORDING TENSION, CARRIED NOT HIDDEN: C-WEBSITE-BLIND says that row "renders BLIND". This order
reads that as the FAMILY (not-CHECKED) rather than the literal enum value, because the constraint's
substance -- permanent, reason attached, not pending -- is what DENY-BY-DESIGN means. If a reader
concludes the PRD intends the literal value BLIND, file a surprise ROW rather than choosing.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam does NOT model wafv2 -- the plane C-SENTINEL-STATE lives on. comp-iam silence is
NEVER evidence about the sentinel's enforcement path, and no criterion here may cite comp-iam as
evidence about it.
BUILD ALL SIX AXIS-1 VALUES AND CITE RULING 12 AS THEIR AUTHORITY. PRD v0.2's S1 row used to
abbreviate axis 1 as "CHECKED vs BLIND"; v0.3 now carries ruling 12 IN FULL, so the PRD and this order
agree. The six are inlined in the cell above BECAUSE THIS FACE IS THE WHOLE OF YOUR CONTEXT -- a value
this order does not carry is a value you never see, whatever any other document says.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-1.state-model-two-axis-vocabulary.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-1"><invocation>grep -c -E 'CHECKED|BLIND|INERT|COARSE|UNCHECKED|DENY-BY-DESIGN' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md</invocation><expect>a count of 6 or greater; a count below 6 means a value was dropped</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-1"><invocation>grep -c 'DENY-BY-DESIGN' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md</invocation><expect>a count of 2 or greater -- the value appears in the enum AND against the Website row</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-1"><invocation>grep -c -E 'desired|applied|exercised' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md</invocation><expect>a count of 3 or greater</expect></criterion>
  <criterion id="AC4" cell_refs="RP-s-1"><invocation>grep -o -E 'DENY-BY-DESIGN' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md</invocation><expect>the literal string DENY-BY-DESIGN, proving the least-used ratified value survived the edit</expect></criterion>
  <criterion id="AC5" cell_refs="RP-s-1" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the deliverable exists and names all six ratified axis-1 values
- **AC2** (mechanical): gap 1 is resolved with the RATIFIED value, not a new field -- the Website row renders DENY-BY-DESIGN
- **AC3** (mechanical): the third axis for gap 2 is present with all three of its values
- **AC4** (mechanical): no ratified axis-1 value was removed or renamed -- the additive bound, mechanically
- **AC5** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): LEGIBILITY: a reader who knows nothing about how the report is built can tell 'we have no way of seeing this' from 'we looked, and here is how bad it is', on rendered specimen rows INCLUDING the permanent-blind case and the DESIRED-not-APPLIED case. NOT self-gradeable by the builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6) · **Project:** NFRA_REPORT · **Directive:** D12 · **PRD:** v0.2 @1703e825d0
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @37ff80867a -> L2/L3/L4 `1.0.0_SA_CTO~Z` -> L5 `2.0.0_SA_COO~ZZ` decomp @c34501140e -> L6 this issuance.
**Provenance:** the cell text mirrors PRD section 8 row S1; nothing in that manifest was re-measured at L4, so every `measured` claim carries the BRIEF's vintage @37ff80867a and this order's L5 battery re-grounds what it cites.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers scanned; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED, NEITHER this project's (G-3 CTO, G-7 POD4); C5's 137 non-null blocking fields are a READING LIST and are not counted as gates.
comp-iam: RUN -- 836 calls verdicted across 96 mapped roles over 31 services; 630 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED not CLEARED), 11 UNGRANTED, 266 calls in 26 role-UNMAPPED services NOT resource-checked; BLIND on wafv2 (coverage-unknown), the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- 2 of 2 cited commits VERIFIED, 2 of 2 cited paths stable, 0 file:line cites; BLIND on the decomposition neighborhood (a DECOMP carries no decomp_ref) so it digested 12 of 13 filesystem siblings instead of the dependency chain, and its packet is therefore not evidence about these cells.
</preflight>

**Preflight disposition:** mandatory core RUN at L5 (comp-schedule C1=23/C2=7/C3=12/C4=20/C5=335; comp-iam 836 calls/96 roles/31 services; comp-adversary 2 of 2 commits VERIFIED with a declared neighborhood blindness). Non-core lenses DECLARED-NOT-APPLICABLE -- this cell touches no route, cache key, shared component or gold-pipeline I/O.
