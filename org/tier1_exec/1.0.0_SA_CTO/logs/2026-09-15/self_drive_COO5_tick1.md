# /self-drive MDPF_TAXSMA,NFRA_OPLGTW,LGIC_NAMING,LGIC_ENFORCE,LGIC_CANON -- tick 1 (2026-09-15 ~19:5xZ)

state: ARMED | cadence 30m (CronCreate e5ff987a, `13,43 * * * *`, session-only, expires after 7 days) | carrier
org/XXX.md @6cfec7a785 | adjudicator: 1.0.0_SA_CTO (Andrew-direct ~19:3xZ, "YOU ADJUDICATE THEM") |
paired_with: the /goal-set loops of 2.0.0_SA_COO~G, ~T and ~O.

## Scope state (read ~19:4xZ; 5 projects, laptop)

| project | COO lane | register status / dep_stage | PRD (prd-signoff status) |
|---|---|---|---|
| MDPF_TAXSMA | 2.0.0_SA_COO~T | scoping / PRD | v0.5 @5061a43a46 WITHHELD: both halves owed (CVO, CRO; live) |
| NFRA_OPLGTW | 2.0.0_SA_COO~O | scoping / EXECUTING | v0.2 ADMITTED |
| LGIC_NAMING | 2.0.0_SA_COO~G | active / EXECUTING | v1.8 ADMITTED on CLOUD; v1.9 ADMITTED on lgic-v19-landing @bf506e53be |
| LGIC_ENFORCE | 2.0.0_SA_COO~G | active / EXECUTING | v1.2 ADMITTED; round 2 issued @4f9a9eb3f3 |
| LGIC_CANON | 2.0.0_SA_COO~G | active / EXECUTING | v1.3 ADMITTED |

sequence-check: stage 0 MDPF_TAXSMA then NFRA_OPLGTW; stage 1 the LGIC trio; CAPACITY 3 of 3 (AT CAP); NEXT COO SLOT
ADVI_FIRMBKTS -> MDPF_CANON -> IRPT_BCKEND (LANE-DARK). No WAITING, HELD or OUT-OF-SEQUENCE flag in scope.

COMPLETION TEST: NOT DONE -- 0 of 5 projects read `status: complete`.

## Acts this tick

- Goals sent (each to arm /goal-set): 2.0.0_SA_COO~G, 2.0.0_SA_COO~T and 2.0.0_SA_COO~O. Broadcast 97215-97217 to
  0.0.0_AB_MSTR, 3.0.0_SA_CVO and 4.0.0_SA_CRO.
- Whether each lane armed its /goal-set loop is read at tick 2.

## Open calls in scope: 2, both ADJUDICATED by this seat; 0 RESERVED

**CALL 1 -- LGIC_ENFORCE FWD-5 (2.0.0_SA_COO~G, 97210): is a class-(d) RAISE an acceptable END for the census?**
- REC (2.0.0_SA_COO~G): yes. A (d) RAISE is a stated verdict, not a skipped name, and FWD-5's ACCEPT asks for a
  ranked whole-estate list, not one with no RAISEs.
- RULING: YES, on two conditions.
  - The census prints the (d) set as its own class, counted in the denominator, each with its name, type, plane and
    the rule clause it RAISES on.
  - Each distinct rule gap goes to LGIC_NAMING as a row, because FWD-5's "fix" for a (d) name is the rule's.
  - No new cell.

**CALL 2 -- row LGIC_CANON-W8-S1 (ARMED, disarm owner 1.0.0_SA_CTO): address() writes `.../advisor_id=A123`;
grade() calls it OUT-OF-PATTERN, canonical `advisor-id=a123`.**
- RULING: address() and the schema are right; `advisor_id=A123` is the schema's own entity-partition example.
- The defect is grade()'s _new_served (lib/opal_naming.py :1102-1111), which reads a trailing `name=value`
  partition segment as a leaf file name.
- INERT today. org/mcp/naming-gate.enforce is absent (read ~19:4xZ; the positive control,
  org/mcp/comprail-gate1.enforce, is present), so the gate only WARNs.
- The fix: grade() reads a trailing k=v segment as a partition. It lands before the gate flips to enforce, which DEC-6
  announces to live seats first. It is carried into LGIC_ENFORCE's round-2 analysis, or into LN-g-2 (2.0.0_SA_COO~G's
  cut).

Both rulings were sent to 2.0.0_SA_COO~G in its goal message (20260915T195010Z).

## RESERVED at Andrew (in scope): none

Carried at Andrew from outside this tick: the ADVI gold redesign DONE WHEN confirmation (the endpoint file
@6a2beed8d2). It is not in this scope. The CLOUD push was set aside by his "DOesnt matter right now".
