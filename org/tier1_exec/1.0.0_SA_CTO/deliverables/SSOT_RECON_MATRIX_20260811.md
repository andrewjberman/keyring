# SSOT RECON MATRIX — the CTO oversight tracker (Andrew-direct mandate @3c8418e34b)

**Owner:** 1.0.0_SA_CTO · opened 2026-08-11 ~0540Z · updated on every recon delivery/cert event.
**Purpose:** ONE place that says, per pipeline × pattern-leg, what is GROUNDED, who holds it, and
what remains — so the design/implementation phases start from an adversarially-established SSOT,
never from records (6 of 10 records were FALSE on the last measured run — the catalog is not
trusted; only certified ground truth enters this matrix as DONE).

## THE STATE MACHINE PER CELL

`OPEN` → `HELD(seat)` → `DELIVERED(@commit)` → `CERTIFIED(CVO verdict)` — only CERTIFIED cells
feed the cutover/design phases that touch live serving. (Non-serving design work may proceed on
DELIVERED with the cert noted pending.)

## THE SIX PATTERN LEGS (Andrew verbatim ~0535Z; grounding question per leg)

| leg | the pattern says | the recon must ground |
|---|---|---|
| L1 ingestion | vendor endpoint → `opal-data-assets/{vendor}/{firm}/bronze` | what lands, from which endpoint, on what trigger; raw-untouched conformance (Rule 17a) |
| L2 bronze→silver | an EVENT TRIGGER processes raw → silver parquets | does the trigger exist; event or cron; what fires it; silver = dedup/dtype only (Rule 17) |
| L3 silver | parquet queryable | schemas, partitions, freshness basis, provenance cols |
| L4 gold | `portal/gold/{product}/{scope}` — code + tables + ALL deps COLOCATED | colocation delta (what still lives outside the root); derivation legitimacy (atom-8 three-bucket) |
| L5 publish | a publisher pulls gold → `platinum/{product}/{scope}` | ONE publisher per product; spelling law; schedule floor |
| L6 portal read | FE reads platinum | what the deployed FE ACTUALLY reads (not what docs say) |

## THE MATRIX (state as of 0540Z — updated in place)

| pipeline × product | L1 | L2 | L3 | L4 | L5 | L6 | held by / record |
|---|---|---|---|---|---|---|---|
| **mdpf (product-global + per-firm)** | DELIVERED | DELIVERED | DELIVERED | DELIVERED | DELIVERED | DELIVERED | CRO base @41692cd3d2; **CVO cert RUNNING** (requested 052113Z, ACK 053137Z) |
| **advi × 49F/bd (08335338)** | HELD(CRO~A) | OPEN | HELD(CRO~A) | HELD(CRO~A) — the ARCHETYPE decomp, Andrew instruction 3 | OPEN | OPEN | archetype spec forthcoming; endpoint catalog + PATH_DISCOVERY exist |
| **advi × inf** | PARTIAL — endpoint catalog + 03 audit | PARTIAL — stop-mechanism record grounds the chain trigger | PARTIAL — silver dims read (TWR dim) | DELIVERED-UNCERT — 03 three-bucket map (5 illegit derivations; ~24/44 scripts UNREVIEWED, marked) | OPEN | OPEN | CRO~A: 01/02/03 records @INF_ATOMDECOMP_RUN_20260811 |
| **advi × cot** | OPEN | OPEN | PARTIAL — custody inversion record @562cbd444d (fact_holdings grain) | OPEN | OPEN | OPEN | **RECON-5 — UNHELD** (5a endpoint inventory rides RCN-0001; 5b after archetype stabilizes) |
| **cross-cutting** | RECON-4 join feasibility (CRO base, RUNNING) · RECON-6 endpoint-delta census (OPEN — fronts atom-8 conformance) · ~~exception set~~ ~~pattern ratification~~ **BOTH RATIFIED ~0542Z @d272021791** — atom-8 conformance is now testable against law | | | | | | |

## ADVERSARIAL DISCIPLINE (the mandate's word: "adversarially establish SSOT")

1. **CVO cross-examines every recon deliverable** — independent re-derivation of load-bearing
   cells against LIVE state, never the artifact's own citations (Rule 22a). A cert that only reads
   the artifact is a rubber stamp and is refused as a cert.
2. **Believed-vs-actual is the required shape** — every recon delivery carries the delta table
   (the @41692cd3d2 form); a delivery with no belief-inversions found must say so explicitly and
   show the records it checked.
3. **Marked holes over silent coverage** — UNREVIEWED/UNMEASURED cells are stated with the exact
   call that would fill them (the truth-JSON convention).
4. **Instruments are suspects too** — comp-pipescript layer blindness + comp-estate stale-snapshot
   404s are OPEN CTO fixes; until landed, any matrix cell resting on those tools carries a caveat.

## OPEN ROUTING (CTO oversight queue)

- RECON-5 (cot advi) seat assignment — with COO (5a can ride RCN-0001 now).
- RECON-6 (endpoint-delta census) seat — fronts atom-8 conformance testing.
- comp-estate snapshot staleness fix + comp-pipescript denominator fix — CTO, in progress.
- L5/L6 columns for advi (publisher + portal read) — likely ONE sweep across all three firms once
  the archetype's L4 shape stabilizes; sequencing with COO.
