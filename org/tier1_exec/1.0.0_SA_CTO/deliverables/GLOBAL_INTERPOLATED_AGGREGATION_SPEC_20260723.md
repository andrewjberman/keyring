# GLOBAL INTERPOLATED-BACKFILL AGGREGATION SPEC (CTO, v0.1 for CVO review)

**Authority (Andrew-direct, verbatim, CTO terminal 2026-07-23 ~02:2xZ):** "Then while that is
happening, I need you to spec a plan for how to aggregate that backfill data into the 'Global'
aum-timeseries and also in the global radial aum-metrics and bell curve distributuiobn metrics.
THen get CVO perspective on that and have them verify the schema in tandem with the work with
4.0.0_SA_CRO."

Companion to CRO's interpolated-backfill design (Andrew-direct 022743Z tasking; chain CRO spec ->
CVO review -> COO decomposition). THIS spec covers the AGGREGATION half: how interpolated
Cottonwood model history enters the three Global surfaces. CVO reviews both IN TANDEM and
verifies the shared schema.

## 1. The sharp scope fact the whole spec turns on

Interpolation produces HISTORY (dated pre-07-21 Cottonwood model values). The three Global
surfaces split cleanly on their time axis:

| Surface | Time axis | Interpolation exposure |
|---|---|---|
| Global **aum-timeseries** | historical, per-date | **YES — the aggregation problem lives here** |
| Global **radial aum-metrics** | CURRENT snapshot | **NONE by construction** — current-day values are measured; no interpolated value can reach it while the fee-basis figure is current-only. If a HISTORICAL radial view ever ships, it inherits the timeseries rules below |
| Global **bell-curve distribution** | CURRENT snapshot | **NONE by construction** — same; account-size buckets are current-day measured |

So: radial + bell curve are protected by their own definition, and the spec's job is (a) to make
that protection STRUCTURAL rather than incidental, and (b) to define honest mixed-provenance
aggregation for the timeseries.

## 2. Aggregation semantics for the Global aum-timeseries

- **Per-date, per-firm provenance vector** rides every Global point:
  `provenance: {49financial: "measured", inflection: "measured", cottonwood: "interpolated"}`.
  Legal values: `measured` | `interpolated` | `absent`. (Carrier: the per-date
  `cohort_provenance` channel that EXISTS AND IS EMPTY today — 429/429 None, DE P1 measured —
  gets its first real population; no new channel invented.)
- **Taint propagation, one rule:** a Global aggregate point is `interpolated`-class iff ANY
  contributing component is interpolated. Rendering: the Andrew treatment (yellow dashed /
  "Interpolated" label) propagates to the GLOBAL series over exactly the affected period — the
  overlay window at Global = the union of firm-level interpolated windows.
- **Additivity unchanged:** Global value = sum of components regardless of provenance (the number
  is the number); PROVENANCE is what distinguishes it, never a haircut or a re-weighting.
  "Doesn't need to be exact" (Andrew) is honored by the label, not by adjusting values.
- **Absent vs interpolated stay distinct:** a firm with no value on a date contributes `absent`
  (existing honest-null law); interpolation never fills a hole silently — an interpolated point
  exists only where CRO's method emits one, provenance-marked.
- **Fee-basis series discipline:** the fee-basis Global series (§1.3 law) carries the same
  per-date provenance; a fee-basis HISTORICAL point containing interpolated Cottonwood model
  values is interpolated-class and renders under the overlay. The CURRENT fee-basis figure (the
  radial) remains measured-only per §1.

## 3. Structural guards (the "cannot fabricate" set — CVO's mutant surface)

1. **Channel separation:** interpolated values live in the same series arrays but are ONLY
   consumable alongside their provenance vector — the schema makes an unlabeled read impossible
   (see §4: values and provenance ship in one dated tuple, not parallel arrays a consumer can
   split). No consumer that computes MEASURED-only quantities (fee invoicing, DDB rows,
   identities, comp-freshness verdicts) may accept `interpolated`-class points: each such
   consumer filters on provenance, and CVO's mutant test is a planted interpolated point that
   MUST be rejected by every measured-only consumer and MUST render with the overlay in the FE.
2. **The 05-28 structural ceiling is schema-enforced:** no interpolated Cottonwood model point
   may carry a date before the model's creation date (per-model floor from the registry/dim);
   the producer refuses, the schema validator refuses independently.
3. **Supersession:** `measured` REPLACES `interpolated` per (firm, model, date) the moment real
   temporal data lands (the qt5-repair upside); the overlay window SHRINKS automatically because
   it derives from provenance, not from a stored config. Interpolated values are never
   overwritten silently — supersession is an evented re-emit with the meta diff named.
4. **Identity computations** (model+non_model==total etc.) run per provenance class: measured
   identities on measured points (hard-fail as today); interpolated points get a CONSISTENCY
   check (interpolated model_aua <= firm total on that date, components sum) that WARNS loudly
   but cannot fabricate a pass on the measured channel.

## 4. Schema (the tandem-verification surface for CVO + CRO)

Per-date Global timeseries entry (additive to current shape, v1-frozen-additive discipline):
```
{ date, model_aua, non_model_aua, total,
  by_firm: { <firm>: { model_aua, non_model_aua,
                       provenance: measured|interpolated|absent,
                       interp?: { method_version, confidence, window_id } } },
  point_class: measured|interpolated   // derived: any-component-interpolated
}
```
- `meta.interpolation`: { affected_period: [start,end], method: <CRO spec id + version>,
  generated_at, superseded_dates: [...] }.
- CRO's producer emits the firm-level tuples; the Global aggregator derives `point_class` and
  the meta block; the FE reads `point_class` for the overlay — three consumers, ONE provenance
  source of truth, no re-derivation.
- The interp confidence field is CRO's (his churn-measured degradation); the FE MAY render
  confidence, MUST render the label.

## 5. What CVO is asked to do (Andrew-named, in tandem with CRO)

1. **Perspective pass on this spec** — especially §2's taint rule and §3's guard set: is there a
   path by which an interpolated value reaches a measured-only consumer or renders unlabeled?
   Design the mutant set (planted-interpolated-point; pre-ceiling date; supersession race;
   parallel-array split) before any build.
2. **Schema verification IN TANDEM with CRO's design** — one schema, two producers (CRO's
   interpolator, the Global aggregator), three consumers (FE, freshness, identity checks); CVO
   owns that the shapes agree BEFORE either side builds (the two-null-semantics lesson: never
   two treatments of one concept in one artifact family again).
3. Verdict + schema sign-off to CTO, CC COO; COO decomposes both specs together on Andrew's
   chain.

## 6. Out of scope here

The interpolation METHOD itself (CRO's spec); FE component implementation (P3 lane on the
decomposed TO); any change to current-snapshot surfaces (protected by §1); DDB/fee consumers
(measured-only, unchanged, guarded by §3.1).
