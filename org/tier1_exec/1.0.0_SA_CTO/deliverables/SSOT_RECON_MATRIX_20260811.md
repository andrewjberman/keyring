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
| **mdpf (product-global + per-firm)** | **CERTIFIED** | **CERTIFIED** | **CERTIFIED** | **CERTIFIED** | **CERTIFIED** | **CERTIFIED** | CRO base @41692cd3d2; **CVO CERTIFIED @cc62267d89 055116Z, ZERO refused cells — CUTOVER GATE RELEASED.** Riders (neither holds cert): act-(ii) precondition = ground the staging producer identity (one CloudTrail/CW read); remediation-register line "consolidator carry-forward on stale staging inputs — verified/declared" before act (ii). CVO correction: mdpf-scheduled-floor IS live (SCHEDULER namespace) but targets the CONSOLIDATOR — delta row 4 stands: nothing clocks the EC2 chain |
| **advi × 49F/bd (08335338)** | HELD(CRO~A) | OPEN | HELD(CRO~A) | HELD(CRO~A) — the ARCHETYPE decomp, Andrew instruction 3 | OPEN | OPEN | archetype spec forthcoming; endpoint catalog + PATH_DISCOVERY exist |
| **advi × inf** | PARTIAL — endpoint catalog + 03 audit | PARTIAL — stop-mechanism record grounds the chain trigger | PARTIAL — silver dims read (TWR dim) | DELIVERED-UNCERT — 03 three-bucket map (5 illegit derivations; ~24/44 scripts UNREVIEWED, marked) | OPEN | OPEN | CRO~A: 01/02/03 records @INF_ATOMDECOMP_RUN_20260811 |
| **advi × cot** | **SOURCE-EXISTS-PIPELINE-ABSENT** (Andrew-direct ~0547Z via CRO @a4d5147211: BD Rebalance endpoint IS the model-holdings source; ingest build = goal 1's opening move, schema capture at RCN-0001's rebalancer-models [BODY-NOT-CAPTURED] gap) | OPEN | PARTIAL — custody inversion record @562cbd444d (fact_holdings grain) | OPEN | OPEN | OPEN | **RECON-5 — UNHELD** (5a endpoint inventory rides RCN-0001; 5b after archetype stabilizes) |
| **cross-cutting** | **RECON-4 DELIVERED @be316d868c (DRY→CVO queue)**: goal-3 join = THREE problems — 49F/bd 0.0% (identity-acquisition: feed account_id IS the SmartX allocationId, custodian hardcoded None; the allocation→custodian-account question rides ~A's RECON-2 under the standing SMARTX lift) · INF 98.0% joinable today (prototype the overlay here) · COT no model-holdings feed (goal 3 runs THROUGH goal 1 — a measured dependency edge) · RECON-6 **HELD(CRO base)** (the ~B spawn ask was retracted pre-spawn — premise false once RECON-4 delivered; RECON-5a queued behind it, same seat) · 49F identity question ANSWERED AT REST (no egress needed): `smartx/platform/silver/fact_allocation_account_map` allocation_id→8-digit account_number, 7,262 rows daily; residual = key-form test (8- vs 10-digit), ~A running; double name-vs-content specimen banked for the 2a field registry · ~~exception set~~ ~~pattern ratification~~ **BOTH RATIFIED ~0542Z @d272021791** | | | | | | |

**L1 KEY-ANNOTATION RULE (0546Z, from the measured three-family collision):** advi×49F/bd and
advi×cot L1 cells land under ONE shared vendor prefix (`opal-data-assets/blackdiamond/{49f,cottonwood}`).
Every L1 count carries the census KEY it was taken with. OPEN CHECK (CTO/CVO): does a bd-tree
script reading `blackdiamond/cottonwood/*` trip the bd↔cot commit gate + IAM deny? (`comp-firmsep-sweep`
is the instrument; not yet run against the shared-vendor-prefix shape.)

## THE QUALITY PARTITION (Andrew-direct instruction 4, ~0552Z via CRO~A record + MSTR relay)

**The recon's PRODUCT is a partition, not just a map: every script/engine/subsystem in the census
lands in EXACTLY ONE side — EXTRACT (quality structure, carried into the canonical build) or
DISCARD (patchy/fragile/methodologically unacceptable) — with grounded evidence per item.** Type
specimen (sovereign-confirmed, independently the audit's ILLEGITIMATELY-DERIVED #1):
transaction-engine holdings valuation → DISCARD. This binds ALL recon chapters' deliverable form;
L4 cells carry a `partition:` field from here forward. Existing certified cells are not reopened —
the partition field back-fills on each chapter's next touch.

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
   Banked from the mdpf cert (CVO, live): **schedule-existence questions MUST sweep BOTH
   EventBridge namespaces** (`events list-rules` AND `scheduler list-schedules`) — a
   single-namespace sweep returns a clean, complete-looking absence, which is the deletion-warrant
   direction. Method line routed to ~A (scheduling-axes/tool-adapters).

## OPEN ROUTING (CTO oversight queue)

- RECON-5 (cot advi) seat assignment — with COO (5a can ride RCN-0001 now).
- RECON-6 (endpoint-delta census) seat — fronts atom-8 conformance testing.
- comp-estate snapshot staleness fix + comp-pipescript denominator fix — CTO, in progress.
- L5/L6 columns for advi (publisher + portal read) — likely ONE sweep across all three firms once
  the archetype's L4 shape stabilizes; sequencing with COO.
