# CVO ASSESSMENT — the graph's two-identity seam (~B brief @29ce04be8)

**Order:** Andrew-direct via ~B relay 063333Z ("write a brief on this matter, relay it to cvo
saying that i want them to assess this"). **Assessor:** 3.0.0_SA_CVO, 2026-08-04 ~06:4xZ.
**Method:** independent re-derivation on comp-kuzu (DB built 06:15Z today, provenance headers
read) + one instrument measurement ~B explicitly left open. ~B's reliability disclosure was
honored: no number below is inherited.

## VERDICT IN ONE PARAGRAPH

~B's measurements are CONFIRMED — and the population-level probes make the finding STRONGER
than the brief claims. This is not a single-specimen seam: **the producer plane and the serve
plane are disjoint sub-graphs.** Zero S3Key↔ServedURL edges exist anywhere (232 × 44), zero
S3Key↔Endpoint edges, zero 2-hop ServedURL→S3Key paths, and S3Key's complete edge-partner
vocabulary is producer-plane types only (S3_BUCKET 464 / C2Motif 456 / PipelineScript 443 /
PipelineFunction 130 / LAMBDA 25 — no serve type appears even once). Separately confirmed:
0 of 232 S3Keys under `json/`, the tier the portal reads directly. And the instrument
measurement ~B left open: **comp-blast on the specimen returns 3 pipeline keys + the bucket
and ZERO serve-plane nodes** — the tool projects the graph faithfully (and prints its declared
lower-bound warning); **the model, not the instrument, is what cannot answer "who consumes
this served artifact."**

## Probe log (all run 2026-08-04 ~06:4xZ, DB vintage 06:15Z, denominators printed)

| Probe | Result |
|---|---|
| Both identity nodes exist | S3Key `platinum/mdpf/aggregate_aua_timeseries.json` + ServedURL `endpointurl:/api/general/mdpf/aggregate-aua-timeseries.json` (+PipelineScript) — confirmed |
| ServedURL 1-hop neighborhood | S3_BUCKET_POLICY(opal-data-portal-v2), Endpoint(getMdpfAggregateAUATimeSeries), C2Motif(AServeMotif) — serve-plane only |
| S3Key count / json/ prefix | 232 / **0** — ~B confirmed |
| Cross-plane direct edges, whole graph | S3Key↔ServedURL **0**; S3Key↔Endpoint **0** |
| 2-hop ServedURL→S3Key | **0** — the planes do not touch through any single intermediate |
| S3Key partner-type census | producer-plane types ONLY (5 types, counts above) |
| comp-blast specimen, --direction down | rc=0; 3 S3Keys + 1 bucket; **0 ServedURL/Endpoint/COMPONENT**; lower-bound warning printed |

Any 3+-hop "path" between the planes runs through hub nodes (a bucket touches hundreds of
keys) and asserts nothing about WHICH key serves WHICH URL — hub transit is not identity.

## Answers to the brief's §6 candidate questions

1. **Design-vs-drift:** STRUCTURAL, not per-node drift — two censuses (producer-side, serve-
   side) that never join, by construction. Whether the disjunction was *intended* is the graph
   builder's design question (NFRA_GLOBGRPH), but intended-or-not it now contradicts the
   projections ruling's intent: the serve side IS the estate (opal-data-portal-v2), and every
   graph-grain answer terminates at platinum.
2. **Does comp-blast cross node types?** Mechanically yes (it returned buckets/keys), but it
   cannot cross an edge that does not exist — measured zero serve nodes in the radius. The
   instrument is faithful; blaming it would misdirect the fix.
3. **Is json/ at 0-of-232 intended coverage?** It is a coverage gap with a live consequence
   already on the record: F1 (`json/portfolios/aum-metrics.json` computed-into the MP page,
   ruled a read-dependency @387c0b1c24) is INVISIBLE to the graph — the exact artifact class
   the DE as-displayed map had to establish by hand.
4. **Do the three vocabularies admit a sound join?** Only via a DECLARED identity mapping.
   String normalization (underscore↔hyphen + prefix rewrite) is UNSAFE here by precedent: the
   4-way account-distribution name collision proves normalized-equal names with different
   semantics exist. A join must be modeled, never derived.
5. **Can freshness surfaces serve as Andrew's deprecated-route homing signals?** Only AFTER
   the identity join exists. The freshness configs' S3-URI vocabulary joins mechanically to
   S3Keys but to ServedURLs only through the unsafe normalization above — so today the homing-
   signal read would silently miss every route whose serve name diverges from its key name,
   which is precisely the deprecated-route shape being hunted.

## Implications — routed

**A. The primary fix is at the CENSUS/GRAPH layer, not in comp-blast** (cross-plane identity
edges + json/-tier ingestion). This is the same conclusion my dial-inputs ledger reached on
the phantom-freshness-checker: target the shared census producer, not each tool's rendering.
It lands naturally as a PREMISE of CTO's two-grain toolscape PRD — the node-grain navigator
dead-ends at platinum until artifact identity is a modeled primitive (canonical artifact node
with plane-scoped aliases). Without it, grain-1 navigation cannot deliver Andrew's model.

**B. Candidate comp-blast edits (cheap, honest, non-pretending — for the dial record's
re-dial scope):**
   1. A declared-limitation line when the subject resolves to a served-tier artifact:
      "serve-plane consumers are NOT modeled in the graph (cross-plane edges absent as of
      <vintage>); consult comp-routes / the DE as-displayed map" — the same honesty pattern
      as its existing lower-bound warning.
   2. Near-match surfacing across the identity seam: blast already has near-match machinery
      (rc=5, duplicate/legacy signal per Andrew's framing); extend it to surface a name-
      normalized ServedURL sibling of the subject WITH an explicit "possible same-artifact,
      UNVERIFIED — the 4-way collision class makes this a lead, not a join" label.
   Neither edit fakes the missing edge; both stop a reader from mistaking plane-truncation
   for consumer-absence.

**C. ~B's meta-observation is adopted into the record:** these probes fail toward "nothing
here," and a false ABSENT is the dangerous direction (a false STALE gets checked). The
population-census method above (partner-type vocabulary, whole-graph edge counts) is the
control that catches it — absence claims should be made against a printed partner census,
not a single traversal.

## Residuals (stated, not chased)

`advisor_nna_canonical` absent from both node types (unexplained, ~B's flag stands); the 119
files with embedded freshness logic untested; whether ServedURL census covers all live routes
(44 vs comp-routes' behavior count) unmeasured.
