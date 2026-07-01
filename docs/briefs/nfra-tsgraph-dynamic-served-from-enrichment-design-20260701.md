# NFRA_TSGRAPH -- dynamic Endpoint->artifact SERVED_FROM enrichment (design)

**Author:** 0.4.0_DE_ClientPlatform | **Date:** 2026-07-01 | **Status:** design (implementation-ready) -- CTO-routed from the COMPTEAM B1 graph-coverage-gap
**Routed by:** CTO arch-gate 2026-07-01 (B1 ask-2: ENRICH, my NFRA_TSGRAPH lane, B1-map-fed, non-blocking for B2).
**Feeds:** NFRA_COMPTEAM B2 (read-partition migrates to graph-native when this lands). **Input:** the B1 map (`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/NFRA_COMPTEAM.B1_portal_surface_data_source_map.json`).

## Problem
The canonical graph's `SERVED_FROM` (29 edges) grounds source->artifact ONLY for the static `/api/general/{X}.json`
family (`stitch_served_from` in `infra/aws/globgrph/derive_runner.py:1300`). The 78 DYNAMIC portal bindings
(ADVI/PM/MDPF, Lambda-mediated) have NO modeled Endpoint->artifact edge -> a B2 read-partition built only on
SERVED_FROM would miss 2/3 of the portal surface.

## Design-determining finding (graph-grounded 2026-07-01)
- Portal Endpoint nodes (`endpoint:getFirmLeaderboard` ...) are TERMINAL: `Hook -FETCHES-> Endpoint`, no onward edge.
- There are 6 `/api/scoped` ServedURL nodes but **ZERO for the ADVI-dynamic `/api/scoped/advisor-intelligence/platinum/*`** endpoints.
- => the enrichment CANNOT key off ServedURL nodes for the dynamic tier (they don't exist). It MUST key off the **Endpoint nodes** + a resolution map. That map is the B1 map (endpoint -> relative platinum key, firm-scoped) -- exactly the "B1 JSON is the enrichment input" CTO specified.

## The derive (mirror `stitch_served_from`, additive + both-ends-verified)
New function `stitch_served_from_dynamic(graph)`, wired right after the `stitch_served_from(graph)` call
(`derive_runner.py:1717`); same best-effort try/except (WARN + continue, never fails the derive). Pattern:
1. **Source:** iterate dynamic Endpoint nodes (node_type=Endpoint) that appear in the B1 map's DYNAMIC FIRM-LEVEL set (endpoint -> relative platinum key, e.g. `getFirmLeaderboard -> platinum/firm/leaderboard.json`).
2. **Firm fan-out:** for each firm in {bd:opal-data-bd, cot:opal-data-cot, inf:opal-data-inf}, resolve `s3://opal-data-{firm}/{relative_key}`.
3. **Both-ends verify (co-key by construction, the CTO both-ends rule):**
   - SOURCE side: `head_object` on the resolved key EXISTS (distinguish 403 IAM-denied [LOUD config error] from 404 absence, exactly as `stitch_served_from`).
   - TARGET side: `opal-data-{firm}` maps to an EXISTING cloud-graph S3 node; target its ACTUAL node_id (arn-form), never the bare bucket name.
4. **Emit** `Endpoint -SERVED_FROM-> S3 bucket node`, props `{firm, s3_key, relative_key, resolution:"advisor-intelligence-firm-config-fanout", verified:"object+node"}`. A distinct string discriminator (`SERVED_FROM` reused, or `SERVED_FROM_DYNAMIC`) -- NO schema change (additive, like the ts_semantic + static SERVED_FROM edges).
5. **Unresolved -> VISIBLE** (logged `SERVED_FROM_DYN_UNRESOLVED`, never force-keyed). PER-ENTITY endpoints (`platinum/advisors/{id}/*`) are param-templated -> recorded VISIBLE-unresolved v1 (a representative-{id} or template-node follow).

## Open decisions (for the implementation pass)
1. **B1-map input location:** the derive must read a DURABLE endpoint->key map. Options: (a) commit the B1 map's DYNAMIC FIRM-LEVEL slice as a small static resolution table under `infra/aws/globgrph/` (versioned, derive reads it); (b) derive parses `portal/src/api/endpoints/advisor-intelligence.ts` bases at derive-time. Rec: (a) -- stable, reviewable, decoupled from portal refactors; regenerated from the B1 map on change.
2. **Edge discriminator:** reuse `SERVED_FROM` (uniform query surface; firm in props) vs `SERVED_FROM_DYNAMIC` (explicit two-tier). Rec: reuse `SERVED_FROM` + a `tier:"dynamic"` prop so `comp-cluster`/B2 query one edge type.
3. **Multi-firm edges:** one Endpoint fans to up to 3 firm buckets (3 edges). B2 read-partition keys the firm off the consuming cohort (49financial->bd, cottonwood->cot, inflection->inf), so per-firm edges are correct + necessary.

## Validation (deploy + scheduled-derive gated; NEVER ad-hoc)
- Local dry-run: run `stitch_served_from_dynamic` against a graph snapshot (no commit) -> assert formed-edge count ~= B1 FIRM-LEVEL bindings x live-firms, 0 dangling.
- Deploy via the globgrph pipeline (Terraform, per CLAUDE.md -- no direct code push); validate on the NEXT SCHEDULED derive's committed graph (`comp-kuzu` for `SERVED_FROM tier=dynamic` edges), NOT an ad-hoc derive.
- Acceptance: every B1 DYNAMIC FIRM-LEVEL binding has a graph `Endpoint -SERVED_FROM-> bucket` edge per live firm; B2 can then query BOTH tiers from the canonical graph.

## Sequencing
Non-blocking for B2 (CTO): B2 consumes the B1 JSON map interim, migrates to graph-native when these edges land.
Next pass: implement `stitch_served_from_dynamic` + the resolution table (open-decision-1a) + local dry-run -> commit -> globgrph deploy -> validate on the scheduled derive.
