# NFRA_COMP* — Program Architecture Brief (binds COMPUNIFY · COMPDRIFT · COMPLEARN)

**Author:** 0.0.0_AB_MSTR (Tier-0, MSTR)
**Date:** 2026-06-30
**Authority:** Andrew-direct (MSTR session 2026-06-30, live design) + LD-0227.
**Issued to:** 1.0.0_SA_CTO — as the binding frame over the three macro-PRDs.
**Status:** Program established. The three macros are PRD'd individually by CTO under this frame.

> One-line: three comp-tool meta-projects are ONE program — **COMPUNIFY is the MAP, COMPDRIFT is a
> verb on resource-STATE, COMPLEARN is a verb on tool-USE.** They share one Trino substrate and one
> surface/seam taxonomy, authored once, so the anti-drift program does not itself drift.

---

## 1. Why a program frame (not three loose projects)

The three projects touch the same substrate (the Trino federation) and the same conceptual object (the
comp-tool estate over local/git/aws/ms/trino). Built independently, they would each invent their own
surface model, their own seam list, their own tool taxonomy — and **drift from each other** (the
anti-drift program drifting internally is the failure this frame prevents). One shared schema, one
shared substrate.

## 2. The three — one noun, two verbs

| Macro | Kind | Object | Output | LD |
|---|---|---|---|---|
| **NFRA_COMPUNIFY** | the **MAP** (static) | surfaces + seams + tools | the non-redundant, provenance-clear coverage taxonomy + ledger | LD-0227 |
| **NFRA_COMPDRIFT** | verb on **resource-STATE** (dynamic) | the actual resources | per-seam parity verdicts ("is the territory in sync?") | LD-0221 |
| **NFRA_COMPLEARN** | verb on **tool-USE** (dynamic) | agent behavior | build/optimize/retire worklist ("is the toolset right?") | LD-0225 |

COMPUNIFY is the **skeleton both loops hang on**: COMPDRIFT checks parity across the seams COMPUNIFY
defines; COMPLEARN scores tool-gaps against the COMPUNIFY coverage map.

```
              COMPUNIFY — the MAP (5-surface taxonomy + non-redundant provenance)
                                 | defines the shared schema
           +---------------------+---------------------+
           v                                           v
      COMPDRIFT                                    COMPLEARN
  resource-STATE parity                        tool-USE optimization
  across the seams                             across the surfaces
           +---------------- shared Trino substrate ---+
```

## 3. Sequencing (the dependency is real, not cosmetic)

1. **COMPUNIFY skeleton FIRST** — the 5-surface taxonomy + provenance ledger + gap census. Mostly
   modeling/doc (cheap relative to the build-heavy loops); it is the shared schema. Building the loops
   without it = each invents its own surface/seam model and they diverge (meta-drift).
2. **COMPDRIFT + COMPLEARN build in PARALLEL against the COMPUNIFY schema**, sharing the Trino
   substrate. COMPDRIFT's seam-ledger IS a COMPUNIFY artifact; COMPLEARN's gap-map is scored AGAINST
   the COMPUNIFY coverage.

COMPUNIFY does not block the loops' design work — its skeleton lands fast and they reference a stable
apex. The COMPDRIFT/COMPLEARN briefs get re-pointed at the COMPUNIFY schema once it is shaped (held
until then, deliberately, to avoid re-work against a moving target).

## 4. The one shared substrate (build once)

All three touch the live `globgrph-trino` federation. The division:
- **COMPUNIFY** defines the surfaces -> Trino-catalog taxonomy (what catalogs exist + what each means).
- **COMPDRIFT** runs the per-seam parity ENGINES over it (the propagation topology).
- **COMPLEARN** adds the `tool_activity` behavior catalog + the learning loop.

The Trino-catalog plumbing is authored ONCE (CTO sequences it across the three). Do NOT triple-build
the substrate.

## 5. Lane / process architecture

- **MSTR** — scopes the program (this brief) + the COMPUNIFY apex taxonomy + commissions all three.
- **CTO** (`1.0.0_SA_CTO`) — PRD + arch-gate each; owns the provenance-map formalization + the
  redundancy-disambiguation (the "parity means 3 things" class of arch-gate it already does) +
  sequences the shared Trino work across the program.
- **AE** (`0.8.0_AE_CloudComp` federation/compdiff owner; `0.7.0_AE_CloudOps` EventBridge/Fargate infra)
  — builds engines / catalogs / scheduled jobs.
- **CVO** (`3.0.0_SA_CVO`) — verifies the COMPUNIFY ledger is COMPLETE + NON-REDUNDANT (every tool
  placed once, every overlap declared), plus drift-parity honesty + scorer honesty.

## 6. Cross-references

- COMPUNIFY brief: `docs/briefs/nfra-compunify-brief-20260630.md` (LD-0227)
- COMPDRIFT brief: `docs/briefs/nfra-compdrift-brief-20260629.md` (LD-0221) — + the MSTR-proposed
  per-change forward-trace / scheduled-sweep / seam-1 enrichments (this session) to fold at PRD time
- COMPLEARN brief: `docs/briefs/nfra-complearn-brief-20260630.md` (LD-0225, §5a router-rules fold)
- Priority: STRATEGIC, phased behind the live ADVI_BREAKS firefight. COMPUNIFY's skeleton is the
  cheap, high-leverage first step.
