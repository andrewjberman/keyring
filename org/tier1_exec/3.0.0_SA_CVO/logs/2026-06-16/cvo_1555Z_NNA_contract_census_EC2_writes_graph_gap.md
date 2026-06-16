# CVO finding — NNA contract census surfaced a Q2-coverage gap (EC2 writes not in the graph) — 2026-06-16 ~15:55Z

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, VALIDATE

Authoring NFRA_GCONTR TO-3 next-wave: the `advisor_intelligence`/NNA (SEV1) contract row. The per-surface producer + forbidden_writers census (CTO condition (a): completeness = catch-power) surfaced a real blocker on the **policy limb** before I authored a broken row.

## Census result
- **Canonical producer:** `bd-gold-layer-runner` EC2 (HAS_PROFILE → `bd-exporter-profile`), running `gold_dispatch.sh` D_00f.advisor_nna_canonical.py → writes `s3://opal-data-bd/platinum/firm/advisor_nna_canonical.json`. So NNA's canonical_writer is the EC2 instance-profile role, NOT a Lambda role (unlike the benchmark seed = yang-pipeline-lambda-role).
- **Threat model differs from benchmark:** NNA has NO known override/dual-writer (benchmark had smartx-model-monthly-pull as a real root-cause). So NNA's `forbidden_writers` is, on the known surface, EMPTY — there is no BMKAUD-equivalent bad writer to list. (Honest completeness: the complete set of *known* non-canonical NNA writers = ∅; catch would rest on canonical-match + WATCH + the value-limb + the IAM backstop.)

## FINDING [P1 — AE lane, graph-derive] — Q2 cannot resolve an EC2-produced surface's canonical_writer
The graph's WRITES-edge derivation is **Lambda-centric**: a census of WRITES into `opal-data-bd` returns ~37 LAMBDA writers and **0 non-Lambda writers**; `bd-gold-layer-runner` EC2 (and its `bd-exporter-profile`) has **0 WRITES edges** in the canonical graph (kuzu_nessie_db, HEAD current). So AE's Q2 JOIN (`observed_via_roles = principals with a WRITES edge into the contracted bucket`) would see the NNA canonical_writer as **ABSENT** and the ~37 Lambda co-tenants as the entire observed set → canonical never matches, everything → WATCH. The NNA SEV1 contract's **policy limb (Q1/Q2) silently can't fire** until the derive captures EC2-instance / instance-profile WRITES (or a role-attribution path for EC2 producers).

This is a TO-2↔TO-3 **seam** failure (mechanical): my contract row would declare a correct canonical_writer that AE's Q2 reader cannot see. A rushed NNA row would have buried it — a SEV1 surface with a dead policy limb reading as "contracted."

**Scope:** affects every EC2-gold-produced platinum/firm surface, not just NNA. The benchmark seed (yang **Lambda** → yang-pipeline-lambda-role) is Q2-resolvable and unaffected. The model_portfolios.* surfaces (headline/peers/aum) producer-type (Lambda vs EC2) is TBD — must check before authoring (same gap if EC2-produced).

## Disposition
- **HOLD** the NNA row's policy limb (canonical_writer / forbidden_writers / Q2) pending AE's derive-side resolution (capture EC2/instance-profile WRITES so the EC2 canonical_writer is a graph principal). Routed to AE (CC COO).
- The NNA **value limb** (period_defs assertion on the NNA windows — QTD/YTD/MAX/1Y/3Y/q_current/q1/q2/q3, from the served advisor_nna_canonical I verified earlier today) is Q2-independent and authorable; I'll draft it as part of the period_defs value-check deliverable.
- Benchmark seed row remains the live RATIFIED milestone (f3334f112; Andrew-signed; AE writing in-VPC). NNA does not block it.
- Next: check model_portfolios.headline/peers/aum producer-type before authoring those rows.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-kuzu (canonical graph) | WRITES-edge census into opal-data-bd + EC2-role trace (HAS_PROFILE) | the finding — 0 non-Lambda writers; EC2 gold-runner has 0 WRITES edges |
| pipescript advi-bd | NNA producer lineage (bd-gold-layer-runner EC2 / gold_dispatch D_00f) | producer confirmed = EC2, not Lambda |
| comp-surface-check list | Phase-1 scope ceiling (earlier) | 5 surfaces, 0 drift |

— 3.0.0_SA_CVO
