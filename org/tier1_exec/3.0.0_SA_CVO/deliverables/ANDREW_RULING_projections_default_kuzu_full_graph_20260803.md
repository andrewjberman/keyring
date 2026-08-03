# ANDREW-DIRECT RULING — projections default to the KuzuDB full resource graph

**Channel:** 3.0.0_SA_CVO terminal, 2026-08-03 ~22:4xZ, during the comp-tools dial session
(mid-thread on the opal-data-mdpf consumer trace). **Recorded verbatim per org/XXX.md; broadcast
same turn to CTO + COO + MSTR. Scope surfaced, not adjudicated (receiving agent does not
adjudicate).**

## VERBATIM

> Ok this is exactly the problem that I thought we already established, all projections should by
> default be kuzudb full resource graph, or at the very least territory-specific full graph (e.g.
> MS Cloud, Git, etc.). Why is comp-blast only checking on those properties? It should be checking
> all of AWS. There are some cases where there are hand-drawn registries, or otherwise specific
> amalgamations, for example comp-estate and its semantic layer for c3.ii that we're building with
> the Kimi pipeline, but that should be the exception not the norm and extremely explicit/
> intentional. Comp-blast absolutely should cover all of AWS.

## CVO reading (flagged as reading; the verbatim wins on divergence)

1. **DEFAULT LAW FOR TOOL UNIVERSES:** any comp-tool projection defaults to the KuzuDB full
   resource graph, or at minimum a TERRITORY-specific full graph (AWS_CLOUD / MS_CLOUD / GIT).
   A tool-private, hand-assembled universe is non-conformant by default.
2. **EXCEPTION CLASS, EXPLICIT ONLY:** hand-drawn registries / deliberate amalgamations (named
   instance: comp-estate's C3.ii semantic layer fed by the Kimi pipeline) are legal ONLY as
   extremely explicit, intentional exceptions — declared, not incidental.
3. **comp-blast SPECIFICALLY: must cover ALL of AWS.** Its current universe does not conform.

## The measurement that triggered it (grounding, all OBSERVED this session)

- comp-blast builds a private trace graph at invocation: **2,255 nodes / 2,950 edges**, with
  exactly 4 S3_BUCKET nodes (bd / inf / portal-v2 / assets); `opal-data-mdpf` NOT-FOUND, so the
  consumer question for a real production bucket was unanswerable by the tool.
- The canonical graph (`comp-kuzu`, kuzu_nessie_db from the Nessie territory map): **20,480 nodes /
  40,945 edges**, built 2026-08-03T21:24Z (1.7h old at probe), CloudTrail-incremental +
  02:00Z full re-derive — and it **carries `opal-data-mdpf` as a CloudNode**.
- The full graph existed, was fresh, and knew the answer; the projection did not ask it.

## Routing

- **CTO:** architecture ruling lands with you — comp-blast universe re-architecture (project from
  the canonical graph / territory graph rather than a private scan) is a build to route; this also
  seeds the comp-blast P1 purpose ruling the 07-31 dial left open.
- **Dial session:** banked in DIAL_comp-pipescript_INPUTS_20260803.md as a P0/P1 default-law that
  every subsequent dial checks: "is this tool's universe the canonical graph, a declared territory
  graph, or a DECLARED exception?" — anything else is a finding.

— 3.0.0_SA_CVO
