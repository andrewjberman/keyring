# NFRA_DEBTSCAN TO-D3 -- canon-motif scorer-tool DESIGN (build-ready)

**Author:** 0.4.0_DS_ClientPlatform~A | **2026-07-07** | **Status:** DESIGN -> RAVC COO (CC CTO canon-author, CVO)
**Builds on:** AE first-pass census (canon-motif-scorecard-firstpass-20260618.md) which VALIDATED the
architecture + found the AC4 candidate. This formalizes the remaining build: the registered scorer-tool.
**Canon:** org/modules/graph/canon-patterns.yaml (v0.1 ef6110129 exists; CTO authoring the fuller schema).

## What the scorer IS (validated by the first-pass, Rule-20 thin-orchestrator)
`comp-canon-motif` -- a thin orchestrator over the canonical query surfaces + 2 gates, NOT a monolithic
re-extractor. For each canon class: compute the DOMINANT motif (>=60% share = the "expected" shape),
enumerate the OUTLIER tail (deviation candidates), clear the tail through twin-shadow + suppression
gates SEPARATELY, and file the residual as ADVISORY novel-candidates -> CVO adjudicates (AC4).

## Per-class source map (each class scores off the RIGHT surface -- query-don't-rebuild)
| Canon class | Graph source | Dominant motif | Outlier = deviation |
|---|---|---|---|
| SERVED_LINEAGE | comp-kuzu (kuzu_nessie_db, canonical) | `(ServedURL)-[SERVED_FROM]->(S3 node)` resolved (29/45=64%) | dangling_served / recompute_fork asymmetry |
| AUTH | comp-kuzu (canonical) | route with a resolvable auth path | missing_auth_edge (but 122->0 after FP_API_LAMBDA+FP_LEDGE -- needs a BEHAVIOR signal via comp-routes, not the unmodeled TRIGGERS edge) |
| DEPLOY | **deploy-ledger cross-ref** (canonical is bucket-grain, no code/-prefix nodes) | `(S3 code/ prefix)-[READS]->(runner)` | orphan_code_prefix / runnerless |
| PIPELINE | **comp-pipescript DEBT-flags** (don't re-derive reachability) | full-chain mounted-reachable | pipescript orphan-candidate / frontend-orphan flags |

## The 2 gates (applied SEPARATELY per the canon -- never conflated)
1. **twin_shadow_guard:** a per-firm TWIN of a dominant motif (advi-bd/advi-inf/advi-cot parallel
   pipelines; designed firm-separation) is EXPECTED, not a deviation -> cleared. (Same firm-token logic
   as the comp-dups DUP_BENIGN_CROSS_FIRM predicate.)
2. **suppression_v1.yaml:** the 18+ active FP classes (graph-modeling gaps / IAM-Deny / Day-0 auth)
   clear KNOWN false-positives. Applied AFTER twin-shadow, logged (no silent suppression, CTO cond-1).

## Tool architecture (build spec)
- **Home:** `org/modules/graph/debtscan/canon_motif_scorer.py` -> registered via comp-manifest-check as
  `comp-canon-motif` (PATH). Reads kuzu_nessie_db via the KUZU LIB directly (NOT a Python->comp-*
  subprocess -- banked Windows gotcha) AFTER a `comp-kuzu` freshness-assert (header current / pin==marker;
  refuse-or-warn on BEHIND/UNKNOWN-VINTAGE per the marker-oracle discipline).
- **Flow:** freshness-assert -> per-class score (dispatch to the source above) -> dominant% + outlier tail
  -> twin_shadow_guard -> suppression_v1 (logged) -> residual = ADVISORY novel-candidates -> emit the
  scorecard format (the firstpass md shape) -> exit.
- **Output:** the scorecard md + a machine-readable JSON (per-class {dominant_pct, outlier_count,
  suppressed_count, novel_candidates[]}) for the standing-scan ledger.
- **Novel-candidate contract (AC4):** any residual after both gates files ADVISORY (0 mutations) + routes
  to CVO. The current AC4 candidate = the SERVED_LINEAGE recompute_fork inflection name-fork
  (AdvisorsTab:374/420 + ClientsTab:291) -- NOTE this is the SAME asymmetry my TSGRAPH P3-2 D2 detector
  catches; recommend the two findings reconcile to ONE canonical instance (debt: inline magic-string fork
  vs the declared useTenantLayout per-firm framework), CVO adjudicates once.

## canon-patterns.yaml expected-schema (what the scorer consumes -- for CTO's authoring)
```yaml
canon_classes:
  - id: SERVED_LINEAGE
    dominant_motif: "(ServedURL)-[SERVED_FROM]->(:S3Node)"   # cypher-ish shape
    dominant_threshold: 0.60
    graph_source: comp-kuzu                                   # comp-kuzu | deploy-ledger | pipescript
    deviation_shapes: [dangling_served, recompute_fork]
    gates: [twin_shadow_guard, suppression_v1]
    incident_anchor: "cross-firm conditional asymmetry"       # the known exemplar the class must catch
```
Each class declares its dominant motif + threshold + source + deviation shapes + gates + an
incident-anchor (empirical-catch, mirroring the P3-2 empirical-validation bar). The scorer is
data-driven off this yaml -- add a class = add a yaml entry, no tool edit.

## comp-debt standing-scan wiring (TO item 3 -- the keystone)
Wire `comp-canon-motif` as a STANDING scan: a scheduled run (rides the existing debtscan cadence / a
daily EventBridge like NFRA_SILVERFRESH) that emits the scorecard JSON to a dated ledger
(org/modules/graph/debtscan/canon_motif/{date}.json) + alarms on a NEW novel-candidate (a residual not
in the prior run's CVO-adjudicated set). This turns D3 from a one-shot census into the running scan the
TO's "design-stage keystone -> running scan" asks for.

## Build sequence (RAVC gates)
1. RAVC this design -> COO/CTO (canon schema) sign-off.
2. Build canon_motif_scorer.py (SERVED_LINEAGE + AUTH kuzu-lib legs first -- census-validated; then the
   DEPLOY deploy-ledger + PIPELINE pipescript delegations).
3. Validate: reproduce the firstpass census numbers (29/45 served, 122->0 auth, the recompute_fork AC4).
4. Register (comp-manifest-check) + wire the standing scan (item 3).
5. CVO adjudicates the AC4 candidate -> AC4 MET (true deviation) or new suppression class.
