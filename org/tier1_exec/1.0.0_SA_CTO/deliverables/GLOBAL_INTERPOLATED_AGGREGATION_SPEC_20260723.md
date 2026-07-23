# GLOBAL INTERPOLATED-BACKFILL AGGREGATION SPEC (CTO, v0.4 — backtest third-class rulings)

## v0.4 RULINGS (pinned delta over v0.3, per CVO backtest tandem review @f2036230e)

**R-7 (F1, the crux — THE SUM-EXCLUSION IS STRUCTURAL): `backtest_projection` values NEVER enter
any actual-AUM sum, at Global or firm-total grain, enforced BY THE AGGREGATOR, not by label.**
The category distinction on the record: interpolated_estimate is estimated-ACTUAL AUM and is
summable (that is why it could be signed into the Global sum); a backtest is NOT AUM AT ALL —
no per-cohort label survives summation into a dollar total. Therefore:
- The backtest is a **PER-FIRM DISPLAY BAND ONLY** (the cottonwood view). At Global it does not
  render and does not contribute — a pre-creation date's Global point = the sum of the OTHER
  firms' measured/interpolated values with cottonwood **absent-for-sum** (exactly the existing
  structurally-absent-not-a-gap behavior; Global history unchanged). A Global hypothetical
  overlay, if ever wanted, is a separate Andrew product decision — not built by default.
- **THE THREE-CLASS point_class LATTICE, defined:** least-certain-PRESENT wins among classes
  that legally enter the sum: measured < interpolated_estimate. `backtest_projection` is NOT in
  the sum lattice at all (it cannot taint what it cannot enter); it exists only as the per-firm
  band's own class. A backtest-classed value reaching any summation path is a HARD FAIL (mutant
  e: a planted backtest point in the aggregator input must abort the Global build, loudly).
- A measured-AUM consumer filter therefore needs no backtest branch — exclusion upstream makes
  the downstream filter unreachable-by-construction for this class (defense in depth retained:
  the filter still rejects the enum if it ever appears).

**R-8 (F3): the constant vintage label does not stretch over degrading depth silently** — the
per-firm band carries an in-band per-point `lookback_days`, and the design sets a MAX-LOOKBACK
bound (CRO proposes the number with justification in his delta; Andrew may override at the
product review). One label covering a 2-month and a 5-year extrapolation identically is the
overstated-safeguard class; the depth indicator is the honest gradient.

**R-9 (F2/F4 status): both are ANDREW'S open words, already on his desk** — visual (anchored
w/ strong style vs rebased growth-of-$1; CRO leans anchored, CVO weighs rebased as the
STRUCTURAL guard — axis beats style for a thing that must never read as dollars) and the price
source (public-close pull vs ycharts vs holdings-only; ALL external paths require his word;
deep history is HARD-BLOCKED until he rules). The spec proceeds per-firm on holdings-derived
overlap meanwhile; nothing deep builds before his word.

---

## v0.2 RULINGS (delta over v0.1, per CVO tandem review @273bbe9c0 — supersedes conflicting v0.1 text)

**R-1 (S1/S4/S5 — the extend-vs-invent decision): ADOPT THE INCUMBENT VOCABULARY WHOLESALE.**
The honesty claim ("we extend Andrew's established channel") is only TRUE this way, and a
look-alike channel that does not interoperate with the 49financial provenance already served is
the two-null-semantics defect recreated at the provenance layer. Binding: enum =
`interpolated_estimate` (never `interpolated` — and it is the more honest string on its face);
container = `partners` (not by_firm); field = `backfill_method` (CRO's method id+version string
IS its value; `confidence` and `window_id` enter as ADDITIVE sibling fields per frozen-additive);
grain = **per-cohort (the incumbent's, which is FINER)** — the firm-level and Global point_class
derive as any-cohort-`interpolated_estimate`. CRO consolidates his three internal handles (S6)
onto this ONE channel and fixes the 5 internal enum inconsistencies (S1) in the same delta.

**R-2 (S2 relocated — the served-boundary reshape): TWO-STAGE, RESHAPE RIDES THE FLIP.**
The incumbent served slice stays parallel-arrays for now (49f/inflection FE reads it TODAY; a
breaking reshape outside the flip gate is exactly what LD-0330 exists to prevent). INTERIM
(structural at the code boundary): (a) an ADDITIVE derived `point_class[]` array lands in the
served slice (non-breaking); (b) the FE data layer gets ONE paired-read accessor returning
value+provenance tuples, components consume ONLY through it, enforced by a test that fails on
any direct read of the value arrays. AT THE FLIP (structural at the artifact boundary): the
revamp-family contract serves inline tuples — the reshape is part of 3F-F1's frozen set, full
gates, and the flip's pre-existing verification machinery covers it. Owner: DE (accessor+test)
/ DS (additive array) interim; F1 for the reshape.

**R-3 (P-A): the interpolation floor is `max(model_creation_date, account_existence_date)`, in
BOTH validators** (producer refusal + schema validator), per-account and per-model.

**R-4 (P-B): radial protection becomes a GUARD:** the radial/bell-curve producers assert
`source != timeseries-tail` (they read only current-snapshot inputs; a timeseries-derived
current value is a build error). Structural, not assumed.

**R-5 (process, adopted from CVO): schema changes re-enter review as PINNED DELTAS** — this
section is the first instance; CRO's next emission does the same. **R-6: CRO publishes the raw
B2 weight vectors in the spec** so all 5 washout coefficients re-derive from first principles
(4 of 5 currently table-consistent but weight-unverified).

Mutant set: v0.1 §5 four + CVO's M8 + M2-sharpened (planted point under BOTH enum strings — the
S1 regression test forever). Decomposition stays HELD until CVO signs the pinned pair.

---
*v0.1 text below stands except where R-1..R-4 supersede (§2 enum/container/grain, §3.2 ceiling,
§4 field names).*

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
  `provenance: {49financial: "measured", inflection: "measured", cottonwood: "interpolated_estimate"}`.
  Legal values: `measured` | `interpolated_estimate` | `absent` (v0.3: incumbent enum per R-1). (Carrier: the per-date
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
**⚠ v0.3: THIS BLOCK IS A RULING RECORD, NOT THE BUILD SURFACE. THE CANONICAL SCHEMA IS CRO'S
PINNED DELTA (his single re-emission against @76c786b5e) — build from THAT block only.** The
shape below is updated to the R-1 ruled vocabulary for record-coherence; if it and CRO's delta
ever disagree, CRO's delta wins and the disagreement is a review item (R-5 delta process):
```
{ date, model_aua, non_model_aua, total,
  partners: { <firm>: { cohorts: { <cohort>: { model_aua, non_model_aua,
                          provenance: measured|interpolated_estimate|absent,
                          backfill_method?: <method-id+version>,
                          confidence?: <per-pair washout-keyed>, window_id?: ... } } } },
  point_class: measured|interpolated_estimate   // derived: any-cohort-interpolated_estimate
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
