# AUA TAXONOMY SCHEMA v0.1 -- Phase 0 of the four-month program

**Author:** 4.0.0_SA_CRO · **Date:** 2026-08-10 · **Status:** DRAFT for Andrew's ratification.
**Commission:** Andrew-direct 2026-08-10 (four-month record @1600047e64; rulings R-1/R-2/R-3
@dedd7bdeab; category call: *"SMA IS a category"* per CTO @6d0a60a54d).
**What this is:** the classification schema that item 1 (Cottonwood pull project), the frontend
fold-in, item 2a's field registry, and item 3's account overlay all build against. Schema only --
no pipeline, no serving, no staffing.

---

## 1. THE ROOT, AND ITS NAME IS PROVISIONAL

The root concept is **CLIENT-ADVISED ASSET CLASSIFICATION** ("AUA composition"). The DISPLAY name
today is "Model Portfolios"; Andrew has said it may become **"Fee-Paying Assets"** (R-1). ⛔ **No
code, key, table, or column carries "model portfolio" as the ROOT concept's identifier** -- the root
identifier is `aua_composition` (or successor CVO-ratified term); "Model Portfolios" is a display
label bound at the serving tier only. The rename is then a platinum-tier label edit, not a schema act.

## 2. AXIS 1 -- AUA COMPOSITION (partitions AUA; one axis, one intent)

Six values. **Classification computes at POSITION grain**; account-level tests are mapping rules.

| # | Value | Definition (Andrew's words where quoted) | State today |
|---|---|---|---|
| 1 | **MODELS** | *"any client assets invested in a model"* -- an Opal MODEL = a multi-constituent allocation, Archetypal (UST/ST/INT/LT/ULT) **or Custom** (e.g. Opal-constituent models on Cottonwood BD -- item 1's subject) | live, displayed now |
| 2 | **SMAS** | *"SMAs devoted entirely to an Opal Strategy"* -- ETF-replica (PFOE, DIVZ -- 49F, in SmartX), **Tax SMA**, **Muni SMA**. FLAT sibling of MODELS -- the two-layer split was REJECTED (R-2) | data exists, not unified |
| 3 | **INSURANCE** | insurance assets; BD carries an insurance endpoint; both Cottonwood and 49F believed to hold insurance client data | **RESERVED-PENDING-DISCOVERY** -- populated only after the read-only BD endpoint discovery pass |
| 4 | **ALTERNATIVES** | alternative asset portfolios, Opal entry 2027 | **RESERVED-NOT-BUILT** (R-3). ⚠ Muni SMA -- possibly Tax SMA -- may re-parent here later |
| 5 | **CLIENT** | *"non-discretionary advisory assets, Non-Model but Fee-Paying"* -- **defined as the explicit RESIDUAL: AUA not classified 1-4.** Computed LAST, by construction | derivable now |
| 6 | *(control row)* **UNCLASSIFIED** | positions the classifier could not place. **NOT a business value -- a loud error bucket.** Target steady-state: 0, reconciled daily | control, born with the schema |

**MECE by construction:** CLIENT is the residual, so the partition is exhaustive; UNCLASSIFIED
catches classifier failure loudly instead of silently inflating CLIENT. **The partition MUST
reconcile to total AUA** per firm and Global -- that reconcile is the standing control.

### 2.1 The MODELS-vs-SMAS discriminator (R-2, verbatim-grounded)

**MODEL vs STRATEGY.** A Model is a multi-constituent allocation; a Strategy is a single mandate.
An account is SMAS iff it is **devoted ENTIRELY to one Opal Strategy** (all-or-nothing at account
level); its positions then map to SMAS. Positions in accounts invested in an Opal Model are MODELS.
The all-or-nothing clause is what makes the account-level test compose with position-grain
computation -- a mixed account can never be SMAS, so no position is ever claimed twice.

### 2.2 The stability rails (R-3: re-parent = RE-LABEL, never re-derivation)

Every classified position carries a **stable `strategy_id`** (the program/strategy it is in --
UST/ST/INT/LT/ULT, each Custom model, PFOE-SMA, TAX-SMA, MUNI-SMA, ...), independent of its bucket.
**The bucket is a MAPPING ROW over `strategy_id`** (`strategy_id -> axis1_value`, vintaged). Moving
Muni SMA into ALTERNATIVES in 2027 is one mapping-row edit; history re-labels by join, nothing
re-derives. *This is his "establish the rails now even if the names change" made mechanical.*

### 2.3 The "Opal"-token fragility control

Custom-model membership currently rides a **human naming convention** (models named with "Opal",
adopted ~07-23). The schema does NOT trust it: names FEED the classifier, but the reconcile control
(partition == total AUA) plus UNCLASSIFIED make an unnamed model surface as loud residue instead of
silently vanishing. **A naming miss becomes a visible reconcile break, never an undercount.**

## 3. AXIS 2 -- OPAL ETF PRODUCT AUM (separate axis; R-1)

`ETF product AUM = ETF assets inside AUA (axis-1-classified) + ETF_FLOAT` (the balance NOT held with
an Opal client). **ETF_FLOAT is deliberately OUTSIDE AUA** -- a sibling-of-AUA measure, never an
axis-1 value (it would break MECE: five values partition a set, the sixth would be its complement).

**R-1 posture, verbatim-grounded:** *"collect it but not necessarily display it anywhere...
colocated someplace backend so we can fold it in if Model Portfolios evolves into Fee-Paying
Assets."* -> collected at GOLD tier, colocated with the axis-1 artifacts, **NO serving projection,
NO display leg.**

**Data note (verified-in-part):** both legs exist today -- fund-level in `opal-data-etfs`
(snapshots + silver, `etfs-netassets-daily` cron 22:00Z; all four tickers DIVZ/IDVZ/PFDE/PFOE in one
artifact, per-ticker `source` field) and client-held in the platinum ETF ownership dashboard
(`internal_only: true`, cron 16:00Z). ⚠ **INFERRED, not yet re-verified by this seat: the two legs
fire 6h apart IN THE WRONG ORDER** (holdings 16:00Z before fund totals 22:00Z), so a same-day
subtraction pairs today's holdings with yesterday's fund figures **by schedule**; and Pathfinder rows
have carried mixed vintages within one record. **The float's day-alignment rule must be DECIDED at
implementation (not discovered)** -- and it sits under the open ETFS CANON question, so it resolves
consistently with that, not separately.

## 4. VINTAGE DISCIPLINE (point-in-time, current ruling)

Andrew ruled **point-in-time -- history does not restate** (@e82326bdb2, on the Cottonwood AUA
question). The schema:
- Every classification row carries `as_of` (the day whose membership it reflects). Point-in-time =
  historical rows never rewritten on later membership changes.
- *"History may be restated in the future"* -> **restatement is NOT foreclosed**: the mapping-row
  design (2.2) makes a future restatement a re-join, structurally cheap. **Nothing is BUILT for it.**
- ⚠ **Scope honesty:** the ruling answered the COTTONWOOD question. Reading it estate-wide (all
  firms + Global) is a separate Andrew call -- flagged, not inherited.

## 5. SCOPE ROLLUP

One classifier, per-firm artifacts (49F / Inflection / Cottonwood), Global = the sum of firm
partitions. **The rollup inherits the reconcile control at both grains** -- a firm partition that
reconciles and a Global that does not means the rollup double-counts (the known hazard: Cottonwood
BD fact_holdings is RELATIONSHIP-grain -- Relationship x Account x Asset -- and must collapse via
`collapse_relationship_grain()` before any sum).

## 6. RULE 24 CONFORMANCE, stated so it can be checked

- **(i) MECE:** residual CLIENT + loud UNCLASSIFIED -> exhaustive and exclusive by construction.
- **(ii) SAME GRAIN:** all axis-1 values classify POSITIONS (the SMA account test is a mapping rule,
  not a second grain). ETF_FLOAT is fund-grain -- which is WHY it is on its own axis.
- **(iii) INTENT COHERENCE:** axis 1 = AUA composition only. Product AUM (axis 2), vintage (sec4),
  and firm scope (sec5) are separate fields, never values.
- **(iv) STATE COHERENCE, the non-moving values NAMED:** MODELS/SMAS/CLIENT move under "build the
  classifier" now; **INSURANCE cannot move until the discovery pass; ALTERNATIVES structurally
  cannot move until 2027; ETF_FLOAT cannot produce a trustworthy number until its day-alignment rule
  is decided.** A plan reading "build the taxonomy" as one workstream is reading three-fifths of the
  axis (the 08-05 five-shapes lesson, applied to this schema at authoring time).

## 7. WHAT RATIFIES vs WHAT WAITS

**For Andrew now:** the six axis-1 values + residual construction; the `strategy_id` mapping-row
rail; ETF_FLOAT on axis 2 gold-only. **Explicitly NOT asked now:** the estate-wide point-in-time
read (sec4); the float day-alignment rule (ETFS CANON); Insurance population (discovery first);
any frontend shape (fold-in-not-new-tabs is already his standing word, 08-10 Teams).
