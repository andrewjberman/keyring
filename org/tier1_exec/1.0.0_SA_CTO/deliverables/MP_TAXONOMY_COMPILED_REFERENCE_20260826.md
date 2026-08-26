# The Model Portfolios Taxonomy — COMPILED REFERENCE (2026-08-26, `1.0.0_SA_CTO`)

**What this is:** the MP layering framework as Andrew has ruled it across 2026-08-19 → 08-26,
compiled from the ruled records, verbatim Andrew-directs, the PRD, and the shipped registry code —
each element cited to its source. Compiled on his 16:3xZ instruction ("look through logs and records
and try to compile it all... we have gone over this many times"). **This document ADDS no vocabulary
and rules nothing** — it is the existing rulings in one place. Where two records use different words
for one thing, the supersession chain says which governs.

---

## 1. THE TREE, AS RULED

```
L0  (what is PRESENT for the firm):   Client · Models · SMAs · Alternatives
        Insurance EXCLUDED from the MDPF view tree ("we don't take fees on it") --
        it remains a top-level value in the 08-19 REGISTRY taxonomy; the exclusion
        is on the VIEW axis only.                                    [A2 §2; A1]

L1  Client:   "Client - Opal Supervised" / "Client - Opal Unsupervised"
        Discriminator: fee-taking, under the OPAL definition of Supervised (below).
        (08-24 first ruled as "Client Supervised/Unsupervised"; renamed 08-25 --
        supersession chain §3.)                                      [A2 §3; A3; PRD s.8.7]

L1  Models:   Primary / Custom                                       [A2 §4; A5]
L1  SMAs:     Tax · Muni · DIVZ · PFOE  -- "so far, maybe others will eventually
        be added" = an OPEN enumeration; the registry admits additions without a
        code change.                                                 [A2 §5; PRD :57,:297]
L1  Alternatives:  no drilldown yet -- "we will not get into just yet."  [A2 §6]

L2  Models > Primary:  UST · ST · INT · LT · ULT  (the current main five)  [A2 §4; A5]
L2  Models > Custom:   DISCOVERY RULE -- any Opal model that is NOT the Primary
        five ("models that say Opal in them that are discovered",
        e.g. Opal Fixed Income), enumerated at L2 drill.             [A2 §4; A6 verbatim]
```

His 16:36Z restatement (A6) names L0 as "Models SMAs and Client" — consistent with A2's four-value
L0 read as elliptical (Alternatives has no drilldown yet); A2's verbatim carries the full L0 set.

## 2. "SUPERVISED" — TWO MEASURES, ONE GOVERNS HERE (A3, 08-25 ~04:2xZ, verbatim record)

| perspective | definition | governs |
|---|---|---|
| Cottonwood-Supervised | everything the client supervises (the whole ~458M) | `COT_CANON458` — the client's own canonical number |
| **Opal-Supervised** | **DERIVED: the residual account value of any account with Opal Models contained within the portfolio** | **the MDPF/D1 display taxonomy — his explicit word** |

**Label obligation (ruled in A3):** every artifact carrying a "Supervised" figure declares
`supervised_basis: opal-models-residual` vs `client-supervision-fact` on its face.
Predicate spec: `SPEC_COT_OPAL_SUPERVISION_PREDICATE_20260825.md` (DS~F); spec fold ruling:
`RULING_20260825_DSF_OPAL_SUPERVISION_SPEC_FOLD_FOUR_HOMES.md`.

## 3. SUPERSESSION CHAIN (which words govern)

1. 08-19 ruling: `Client = Advised + Residual` (advisory-scope axis) → **08-24 view tree** renames
   the VIEW split to Supervised/Unsupervised with FEE-TAKING as the discriminator (A2 §3) →
   **08-25**: values become **"Client - Opal Supervised" / "Client - Opal Unsupervised"** (PRD
   s.8.7 — the operative values), on the **Opal definition** (A3).
2. The registry code carries BOTH axes deliberately (`mdpf_category_registry.py:84-99`):
   `advisory` (08-19 gate: Advised+Residual) and `fee_taking` (08-24: Supervised+Unsupervised) —
   two axes, not a conflict (Rule 24(iii): different intents).
3. 08-24 "Client Supervised" enum → superseded by "Client - Opal Supervised" (PRD s.8.7 states it
   in terms: "THOSE VALUES ARE SUPERSEDED").

## 4. CUSTOM MODELS — the ruling chain that closed today's blocker

- 08-19 gate + 08-24 view tree: `Models = Primary + Custom`, Primary = the five, Custom = any Opal
  model not those, at L2 drill (A2 §4).
- **08-26 ~15:2xZ (A5): "yes Opal Fixed Income is a 'Model', it is a 'Custom' model, as opposed to
  a 'Primary' Model which comprises of UST ST INT LT ULT"** — supplied the INTENT no instrument
  could reach; unblocked the canonical-key P0 (COO 72417 record; key landed, lambda rebuilt at
  minimal pin, verified).
- 08-26 ~16:36Z (A6): the discovery RULE restated as the Custom membership definition.
- The registry already modeled it: `mdpf_category_registry.py:410` — "'Models' rolls up
  Primary+Custom" — his words supplied the membership rule for an axis the estate had built
  (CVO 72430 §2).
- **Boundary note (engineering seam):** the discovery rule defines TAXONOMY membership; the served
  Global union's canonical-key guard (no-auto-slug) is a SEPARATE standing mechanism — a discovered
  model still gets its served key deliberately.

## 5. THE 08-26 DIVERGENCE, RESOLVED INSIDE THIS FRAMEWORK

The ad-hoc QA fire (his drive-now law) surfaced a cottonwood identity refusal: decomposed
$147.0M vs dim $190.7M (delta $43.7M; 483 vs 489 accounts). Resolved same hour:
- **Re-attribution, not new money** — firm AUM identical to the cent (480,687,460.42) on both
  sides; `MODEL_DETAIL_SCOPE` widened to `Scope="all"` (applied 08-25, running), `fact_model_blend`
  37→117 edges (+80 added, 0 removed) (PartnerETL~A 72575, COO-ratified 72580, CVO cent-exact 72571).
- **His word (A4, 16:34Z): "what is being discovered is the 'Client - Opal Supervised' segment...
  covered in the Taxonomy that we are building for Model Portfolios."** The dim is right; the
  decomposition side learns the segment per THIS framework, not ad hoc.

## SOURCE INDEX (the anchors; each is the citation for the sections above)

| id | artifact | vintage/date |
|---|---|---|
| A1 | `org/tier1_exec/1.0.0_SA_CTO/deliverables/D1_TAXONOMY_GATE_RULING_20260819.md` — the ruled Rule-24 taxonomy (binds) | 08-19 |
| A2 | `.../ANDREW_DIRECT_20260824_D1_VIEW_TREE_L0_L1_L2_CLIENT_MODELS_SMAS_ALTERNATIVES.md` — the view tree VERBATIM | 08-24 ~18:5xZ |
| A3 | `.../ANDREW_DIRECT_20260825_SUPERVISED_IS_TWO_MEASURES_OPAL_DEFINITION_GOVERNS_MDPF.md` | 08-25 ~04:2xZ |
| A4 | `.../ANDREW_DIRECT_20260826_1634Z_COTTONWOOD_DIM_JUMP_IS_CLIENT_OPAL_SUPERVISED_SEGMENT_MP_TAXONOMY.md` @2390e15d90 | 08-26 ~16:34Z |
| A5 | 'Opal Fixed Income' Custom ruling — COO 72417 verbatim record | 08-26 ~15:2xZ |
| A6 | `.../ANDREW_DIRECT_20260826_1636Z_MP_LAYERING_L0_L1_L2_WITH_CUSTOM_DISCOVERY_RULE.md` @0e59cfa58d | 08-26 ~16:36Z |
| — | `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md` — s.8 pipeline entry; s.8.6/8.7 (:293-320) the operative Client values; :57-62 the composition mapping; :57/:297 SMA members | 08-19→08-25 |
| — | `data/mdpf/scripts/gold/mdpf_category_registry.py` :84-99 (L1 values, two axes), :410 (Models rolls up Primary+Custom) | shipped |
| — | `.../ANDREW_DIRECT_20260824_MODEL_TAXONOMY_BEELINE_D1_PIPELINE.md` | 08-24 |
| — | `workflows/atom_decomposition/runs/d1-catviews/20260824T195537Z/DECOMP.md` — stage-3 decomp v2 (view-tree cells) | 08-24 |
| — | `SPEC_COT_OPAL_SUPERVISION_PREDICATE_20260825.md` (DS~F) + `RULING_20260825_DSF_OPAL_SUPERVISION_SPEC_FOLD_FOUR_HOMES.md` | 08-25 |

Directive homes: **D1** (the taxonomy + views: `D1_CATVIEWS`, active, decomp v2 28→31 cells);
**D8** (the pipeline fortification the served plane rides). Register rows carry both.
