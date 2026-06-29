# SEAM: NFRA_COMPDRIFT propagation topology — local→git→cloud→nessie→kuzu→iceberg→trino→served (scale: MACRO, 7 seams)
**archetype:** VALIDATE
**For:** 0.0.0_AB_MSTR (RAVC, Andrew-direct request) · CC 1.0.0_SA_CTO (manifest/PRD owner — corrections route here) + 2.0.0_SA_COO (P1 coverage-map feed)
**Target:** the seams BETWEEN stages, 3-axis, grounded vs LIVE (never source/self-report). Manifest under audit: `org/modules/graph/drift-topology.yaml` + `docs/briefs/nfra-compdrift-brief-20260629.md` §3. **Article XIV: the verdicts are CVO's own.**

## Decisive cross-cutting ground-truth (the finding that reframes seams 5-7)
**Which stages exist LIVE today** (the question that distinguishes "GAP = live-seam-unchecked" from "stage-not-yet-built"):
- LIVE: **LOCAL, GIT, CLOUD, NESSIE, KUZU, ICEBERG.** comp-kuzu header (live): DB kuzu_nessie_db 18205 nodes/30569 edges, `source: nessie`, **nodes metadata = `warehouse/globgrph/graph_nodes_*.metadata.json` — i.e. the graph IS stored as ICEBERG tables under the Nessie catalog.** So Nessie↔Iceberg is a LIVE, carrying seam (the graph loads from Iceberg).
- IN-BUILD (NOT live): **TRINO + SERVED-HEAT-VIEW** — the heat-federation (design arch-gated this session, not deployed). No live Trino endpoint; comp-which finds no Trino-status tool.
**Implication:** seams 1-5 connect LIVE stages (testable now); seams 6-7 connect to a NOT-YET-LIVE consumer (Trino/served-heat) → their "GAP" is **stage-not-yet-built, not live-seam-unchecked** — they are UNVERIFIABLE-by-construction (no territory to map yet), which is a different manifest semantics than a covered/uncovered live seam.

## Per-seam 3-axis verdicts (priority on 3-7; declarative weighted highest per MSTR)

| Seam | MECHANICAL | DECLARATIVE (map vs territory) | SEMANTIC | Verdict |
|---|---|---|---|---|
| **s1 LOCAL→GIT** (every commit-worthy write committed) [claim: COVERED, comp-heat drift] | PASS — checker exists | PASS — COVERED claim true | n/a (no data payload) | SOUND (light-confirmed) |
| **s2 GIT→CLOUD** (deployed==committed) [COVERED: comp-pipescript deployed / comp-lambdamap parity / comp-iam reconcile] | PASS — I EXERCISED these this session (comp-lambdamap parity live 135 MATCH; comp-pipescript deployed) | PASS — COVERED true; note comp-lambdamap parity is now BUILT+registered (was "spec*"), so the `*` caveat is STALE → update | PASS (sha/artifact parity proven) | SOUND — manifest `*` caveat now stale (correct to COVERED) |
| **s3 CLOUD→NESSIE** (graph reflects LIVE estate) [PARTIAL: globgrph derive marker-oracle] | **PARTIAL-CONFIRMED** — graph built 14:05Z, now ~19:13Z = **5.1h stale**; it does NOT reflect live changes since (e.g. the 15:58Z lambda redeploys). The derive is periodic → a real staleness WINDOW. | PASS — the "PARTIAL" claim is ACCURATE (marker-oracle flags age/HEAD-advance but does not continuously close the live-parity window) | UNVERIFIED — would need a full live-estate-vs-graph diff (not run) | PARTIAL — claim accurate; the gap is the periodic-derive staleness window |
| **s4 NESSIE→KUZU** (query DB == latest Nessie HEAD) [SELF-HEAL, **NOT ASSERTED**] | PASS — self-heal works: header shows current | **DRIFT (correction to manifest):** the header DOES assert it — `Nessie HEAD: current (pin == marker HEAD)`. So **Kuzu-pin↔marker IS asserted** (current/BEHIND/UNKNOWN surfaced). What is genuinely NOT asserted is **marker↔TRUE-latest-Nessie** (the marker could lag actual Nessie HEAD). So "NOT ASSERTED" is too broad → refine to "Kuzu↔marker ASSERTED in header; marker↔true-Nessie-latest NOT asserted." | PASS — pin==marker held live | SOUND-mechanically; **manifest declarative claim needs refinement** (the highest-value correction) |
| **s5 KUZU/NESSIE→ICEBERG** (lakehouse tables == canonical graph source) [GAP] | PASS — LIVE seam: the graph nodes/edges ARE the Iceberg tables (`warehouse/globgrph/*`), Nessie-cataloged; comp-kuzu reads from them | PASS — GAP claim ACCURATE (no checker that Iceberg==graph-source) but **GAP=no-checker, the seam itself EXISTS + carries** (correct the framing if it implies no-seam) | UNVERIFIED — no Iceberg-vs-source content parity run | GAP-accurate (live seam, genuinely no checker) |
| **s6 ICEBERG→TRINO** (catalog binding == backing schema, per federated catalog) [GAP — design IN] | **UNVERIFIABLE** — TRINO NOT LIVE (in-build). Consumer stage does not exist to test. | PASS — "design IN" accurate; **sharpen: GAP is stage-not-yet-built, not live-seam-unchecked** | UNVERIFIABLE (no live Trino) | UNVERIFIABLE@all — stage in-build (correct manifest semantics) |
| **s7 TRINO→SERVED** (served heat view == Trino federation) [PARTIAL: comp-freshness + heat-view] | **UNVERIFIABLE** — served-heat-view is the heat-federation BUILD TARGET (in-build); no served heat artifact to read | PARTIAL claim is FORWARD-LOOKING — the checker exists in pieces (comp-freshness) but the served-heat surface it checks doesn't exist live yet | UNVERIFIABLE (no served heat view) | UNVERIFIABLE@all — consumer stage in-build |

## Knowledge-parity delta (corrections to CTO's drift-topology manifest)
1. **s4 (highest-value):** manifest "SELF-HEAL, NOT ASSERTED" is too broad — the comp-kuzu provenance header DOES assert Kuzu↔marker (`current (pin == marker HEAD)`). The genuine gap is **marker↔true-latest-Nessie** not being asserted. Refine the claim → an honest, narrower drift point for the comp-drift checker to target (assert the marker isn't itself stale vs live Nessie).
2. **s6/s7:** their GAP/PARTIAL is **stage-not-yet-live** (Trino + served-heat in-build), NOT "live seam, no checker." This VALIDATES the brief's strongest design recommendation (§4): make the parity signal an **acceptance criterion of the heat-federation build** so s6/s7 ship COVERED rather than landing as GAPs — confirmed correct, because the seams literally cannot be checked until the stages exist. Manifest should mark these `STAGE-IN-BUILD / UNVERIFIABLE` (distinct from a live GAP).
3. **s2:** the `comp-lambdamap parity [COVERED*]` `*` ("spec-complete, read-surface in flight") is STALE — the read surface landed + registered this session (`comp-lambdamap parity` is canonical, 135 MATCH live). Drop the `*` → COVERED.
4. **s3:** PARTIAL is accurate + ground-confirmed — observed a 5.1h staleness window today (graph 14:05Z vs live changes 15:58Z). The comp-drift checker for s3 should surface the derive-staleness window explicitly (age-vs-acceptable-lag), which the marker-oracle's header age already exposes.
5. **s5:** GAP accurate, but the seam EXISTS + carries (Iceberg IS the graph store) — frame as "live seam, no parity checker," not "missing seam."

## Verdict
**Topology weakest-seam-binds: the live sub-chain (s1→s5) is SOUND-or-PARTIAL with accurate manifest claims (one s4 refinement); the s6→s7 sub-chain is UNVERIFIABLE-by-construction (Trino/served-heat in-build).** The comp-drift thesis ("each hop in parity with the prior") is empirically TRUE-and-checkable for s1-s5 today; s6-s7 become checkable only when the heat-federation lands — so the brief's "parity-signal-as-build-acceptance-criterion" is the correct design, validated. Net: the manifest's coverage map is ~accurate with 5 named corrections (1 declarative refinement on s4, 1 semantics fix on s6/7, 1 stale-`*` on s2, 1 confirmation on s3, 1 framing on s5).

## grounding: field (Rule 22)
- "graph is 5.1h stale / doesn't reflect post-14:05 live" — SOURCE-CONFIRMED (comp-kuzu header `built 14:05:41Z` vs the 15:58Z lambda-redeploy I grounded earlier this session).
- "s4 header DOES assert Kuzu↔marker" — SOURCE-CONFIRMED (comp-kuzu header literal `Nessie HEAD: current (pin == marker HEAD)`).
- "Iceberg IS the graph store (s5 live)" — SOURCE-CONFIRMED (header `nodes metadata: warehouse/globgrph/graph_nodes_*.metadata.json`).
- "Trino/served-heat NOT live (s6/7 in-build)" — INFERRED (live-state-only): no live Trino found via comp-which + the design-arch-gate session record; NOT a deployed-Trino negative-probe. Flag: confirm with the heat-federation owner (could-not-verify a live Trino absence definitively, but no evidence of one).

## Residual / unknowns
- s3 SEMANTIC + s5 SEMANTIC (Iceberg-vs-source content parity) NOT exercised — would need a full live-estate-vs-graph and Iceberg-vs-canonical diff (out of scope for this pass; named for the comp-drift SEMANTIC-axis design).
- s6/s7: UNVERIFIABLE until Trino + served-heat land — re-run /seams on those when the heat-federation deploys (the build-acceptance-criterion hook).
- Trino-absence is evidenced-not-probed (no live endpoint found, not a definitive negative).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-kuzu (provenance header) | s3/s4/s5 ground-truth | PASS | the live header carried the decisive facts: Iceberg-as-store, 5.1h age, pin==marker assertion |
| comp-which | "is trino deployed/serving heat federation" | routed (no Trino tool) | corroborates Trino not-a-deployed-surface (in-build) |
| comp-lambdamap parity / comp-pipescript deployed | s2 (exercised earlier this session) | PASS | s2 COVERED checkers proven working live (135 MATCH) |

— 3.0.0_SA_CVO
