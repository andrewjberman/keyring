# NFRA_COMPUNIFY — Macro-Project Brief (the top-down coverage taxonomy)

**Author:** 0.0.0_AB_MSTR (Tier-0, MSTR)
**Date:** 2026-06-30
**Authority:** Andrew-direct (MSTR session 2026-06-30, live design) + LD-0227.
**Issued to:** 1.0.0_SA_CTO — for PRD authoring + arch-gate + TO decomposition + macro stand-up.
**Program:** NFRA_COMP* (`docs/briefs/nfra-comp-program-architecture-20260630.md`) — the foundational
schema the COMPDRIFT + COMPLEARN loops reference.
**Status:** Commissioned.

> One-line: build the **MAP** of the comp-tool estate — a top-down, **non-redundant**,
> **provenance-clear** coverage taxonomy over **5 surfaces (local / git / aws-cloud / ms-cloud /
> trino)**, from a narrow apex down to territory-specific detail, so that for any question we know
> exactly which tool answers it, at what level, and why it is not redundant with its siblings.

---

## 1. The problem — the toolset has no top-down map

We have ~38 comp-tools documented in a FLAT, alphabetical `tools_index` + scattered `DISTINCT from X`
prose. There is no structured answer to: *what are our surfaces? which tool is the high-level entry for
each? which tools cover the seams between surfaces? where does coverage thin out or overlap?* The
consequences are real and observed:
- **Undeclared redundancy.** IAM is touched by 3 tools, "parity" means 3 different things (the CTO
  needed an arch-gate just to disambiguate the WORD), "freshness" spans 4 tools. The distinctions
  exist only as prose, not as a structural rule.
- **Invisible gaps.** MS-CLOUD has no dedicated comp-tool; LOCAL has one; Trino-as-federation has no
  clean comp-front. Nobody can see the coverage asymmetry because there is no map to see it on.
- **Discovery friction** (the LD-0224 audit): agents fall to raw grep 38% of searches partly because
  the catalog is a flat list, not a "drill from your surface" hierarchy.

## 2. The thesis — a narrow apex, progressively drilled down

COMPUNIFY structures coverage **from the top down**: a narrow apex of the **5 primary surfaces**, the
**high-level tool** for each, the **seam tools** for inter-surface connections, then
**territory-specific drill-down tools** for detail. Every tool gets exactly one HOME in this hierarchy,
with declared provenance — so coverage is auditable top-down and redundancy is structural, not prose.

## 3. The 5-surface apex (Andrew-direct)

Four **territory** surfaces (where state actually lives) + Trino as the **federation** surface (the
derived join-layer ACROSS the others — special, not a peer):

```
APEX:        LOCAL        GIT          AWS-CLOUD       MS-CLOUD       [ TRINO = federation ]
          (working      (committed    (Lambda/S3/     (M365: SP/      (joins the derived
            tree)        history)      EC2/DDB/IAM)    Teams/users)    models of all 4)
high-level: comp-heat    comp-heat     comp-aws        GAP: no         comp-kuzu
            drift        + comp-xray                   comp-ms         (+ comp-fed, future)
                          code/config                  (m365 MCP +
                                                        graph ms-layer
                                                        only)
```

The derived MODELS (Nessie -> Kuzu -> Iceberg) are the MAP layer over the territory — they feed Trino,
they are not surfaces (they are derived and can drift; the comp-kuzu provenance-header lesson). Trino
is the apex's special node: the unified federated query surface (the COMPLEARN behavior catalog +
COMPDRIFT seam fan-in both live here).

## 4. The hierarchy — seams + drill-down

```
SEAMS (inter-surface parity = the COMPDRIFT consumption surface):
  LOCAL->GIT     comp-heat drift
  GIT->AWS       comp-pipescript deployed | comp-lambdamap parity | comp-iam reconcile
  GIT->MS        (msgraph deploy -- thin)
  SURFACE->MODEL->TRINO   comp-aws derive | comp-kuzu HEAD | seam-5/6 (GAP)

DRILL-DOWN (territory-specific detail):
  AWS:  comp-routes(CF) comp-cache(RQ) comp-transform(portal) comp-freshness(data)
        comp-secrets(SM) comp-xray(content) comp-parity(served) comp-pii
        comp-platinum comp-blast/trace(lineage)
  GIT:  comp-pipescript io  comp-validate  comp-constants
```

## 5. THE LOAD-BEARING INVARIANT — non-redundancy + provenance (Andrew-direct, the acceptance criterion)

> **Every tool has exactly one HOME = (surface OR seam) x granularity x concern. Two tools may touch
> the same RESOURCE only if their CONCERN differs — and that difference must be DECLARED. Silent
> overlap is a COMPUNIFY violation -> merge or disambiguate.**

This is the project's acceptance criterion, not a nicety. It makes the current undeclared overlaps
explicit:
- **IAM** -> `comp-iam` = grant-analysis; `comp-aws` = IAM-as-graph-nodes; `comp-lambdamap` = deploy-SHA.
  Same resource, three concerns, declared.
- **"parity"** -> `comp-lambdamap parity` = deploy; `comp-parity` = data/served; `comp-incrparity` =
  incremental. Same word, three concerns, declared.
- **"freshness"** -> `comp-freshness` = pipeline-data; `comp-heat` = estate-object; `comp-graph` =
  graph-vintage; `comp-xray` = content-motion. Same word, four concerns, declared.

A tool that cannot be placed at a single (surface|seam) x granularity x concern node, or that overlaps
a sibling WITHOUT a declared concern-difference, is a **finding** -> merge, retire, or disambiguate.

## 6. Deliverables

1. **The coverage/provenance ledger** (machine-readable, e.g. `org/modules/graph/comp-coverage-map.yaml`):
   surface -> high-level tool -> seam tools -> drill-down tools, each node carrying
   `{concern, granularity, surface|seam, distinct_from:[...]}`. This **replaces the flat
   `tools_index`** with the top-down hierarchy (the manifest's flat list becomes a generated VIEW of
   the ledger).
2. **The gap census** — every (surface x level) node with NO tool (ms-cloud high-level; local depth;
   trino-federation front; seam-5/6) flagged as a coverage gap -> feeds the COMPLEARN worklist.
3. **The redundancy census** — every undeclared overlap surfaced -> merge/disambiguate worklist.
4. **comp-which reorg (optional, high-value)** — route by SURFACE first, then drill down, so discovery
   mirrors the taxonomy (ties to the LD-0226 router work + the LD-0224 ambient-discovery finding).

## 7. Why FIRST in the program (the meta-drift argument)

COMPUNIFY's schema is what COMPDRIFT (seam ledger) and COMPLEARN (gap-scoring) both reference. Built
after them, each loop invents its own surface/seam model and they drift from each other — the
anti-drift program drifting internally. So COMPUNIFY's taxonomy skeleton lands FIRST as the shared
schema; the loops build against a stable apex. (Full program frame:
`docs/briefs/nfra-comp-program-architecture-20260630.md`.)

## 8. Relationship to COMPDRIFT + COMPLEARN

- **COMPDRIFT** consumes COMPUNIFY's SEAM taxonomy (the inter-surface parity invariants ARE the
  seams). The COMPUNIFY seam list and the COMPDRIFT propagation topology must be ONE artifact.
- **COMPLEARN** scores tool-gaps AGAINST COMPUNIFY's coverage map (a "demanded-but-missing" gap is a
  COMPUNIFY empty node with high COMPLEARN demand). The COMPUNIFY gap census seeds the COMPLEARN
  worklist.

## 9. Lane / asks to CTO

1. Author the NFRA_COMPUNIFY PRD + arch-gate; stand up the macro (JSON + REGISTRY).
2. Formalize the coverage/provenance ledger schema + the non-redundancy invariant as a machine-checkable
   acceptance criterion (CVO verifies completeness + non-redundancy).
3. Decide the ledger's relationship to the existing `graph-call-manifest.yaml` (supersede the flat
   `tools_index` with a generated view, vs a parallel artifact) — do NOT create a second drifting
   catalog.
4. Reconcile the COMPUNIFY seam taxonomy with the COMPDRIFT propagation topology into ONE shared
   artifact (sequence with LD-0221).
5. Run the first gap + redundancy census as the macro's deliverable #1 (the IAM/parity/freshness
   overlaps + the ms-cloud/local/trino-front gaps named here are the seed).
6. Priority: STRATEGIC but FOUNDATIONAL — its cheap skeleton unblocks the other two; phase the deep
   build behind the firefight, but the skeleton is the high-leverage first step.
