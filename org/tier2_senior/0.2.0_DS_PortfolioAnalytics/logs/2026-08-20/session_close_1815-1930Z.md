# COT_SUPERVISED Close-Out at Both Gates + DATA_BDINSURANCE Reframe Thread — 0.2.0_DS_PortfolioAnalytics

**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE, VALIDATE

**Date:** 2026-08-20
**Task Order:** COT_SUPERVISED.G1-G7.retroactive-filter-and-portfolio-group (close-out window) + DATA_BDINSURANCE (context, pre-decomposition)
**Status:** COMPLETE (window); TO rows G4/G4b remain open riding tonight's named run

---

## Objective

Close the DS side of COT_SUPERVISED on the record (proof instance + RAVC + gates), and
handle the DATA_BDINSURANCE context thread that grew out of one adjacent observation
this seat sent with its acknowledgment.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | .tools/proof-of-spec-check.py <instance> "G2,G3,G4,G4b,G5,G6,G7" | PASS | VALID rc=0, 7 rows 0 violations -- run at authoring and again after the G7 flip |

No comp-* runs this window: it was close-out + coordination; all comp-tool verification
(comp-pipescript io/deployed, comp-validate vs served bytes, comp-find, comp-pulse) ran in
the build window and is recorded in the prior log (`cot_supervised_g2_g6_retroactive_filter_1720-1815Z.md`).

**What worked:** proof-of-spec-check's positional-coverage arg made the expected-set claim mechanical.
**What failed:** nothing.
**Gap found:** none this window.

---

## Work Completed

### 1. COT_SUPERVISED DS close (commits 6a83f3f08a, f88692d7b4)
- Proof-of-spec instance authored + committed @6a83f3f08a: 7 acceptance rows, VALID rc=0
  positional G2-G7 (G1 in 0.6.2's instance per the group split); G4/G4b honest
  UNCOMPUTABLE-BY-CONSTRUCTION riding tonight's NAMED scheduled run; mutant
  FIRED-AS-EXPECTED; determinism STABLE.
- RAVC close sent to COO cc CTO (63439/63440).
- COO VALIDATED (63441): rc=0 re-run at the COO seat, @8d19ea52a3 verified -- DS legs ACCEPTED.
- CTO G7 ARCH-GATE CITE GRANTED (63443): independent live read of
  s3://opal-data-cot/gold/artifacts/supervised_split.json at the CTO seat -- 08-19 row MECE
  to the penny, caveats on the artifact face. Cite explicitly does NOT pre-clear G4/G4b.
- G7 row flipped to PASS citing both, instance re-validated rc=0, committed @f88692d7b4.

### 2. DATA_BDINSURANCE thread (no dispatch taken; context + one tested hypothesis)
- CTO amendment context read (63540): Andrew narrowed the project backend-only; RESTATEMENT
  third change class is the central design work; cot insurance_accounts.json dead mirror
  (0 readers / 114 files) in scope.
- My acknowledgment carried one adjacent observation (the unsupervised held-away cohort as a
  free first observation set for statement-cycle cadence). CTO TESTED IT (63549): CONFIRMED
  and reframed the project -- 42 accounts / $41,559,989 flat to the cent across 4 partitions
  over 9 weeks = static manual valuations already in the current book (8.7% of $480M),
  now PRD sec 4.4.5 (valuation_basis classifies the EXISTING book; value_as_of load-bearing;
  FLAT-IS-NOT-BROKEN).
- COO banked the reframe (63553): this seat is the PRESUMPTIVE W3-classification lane,
  confirmed at decomposition cut, not before; COT tonight-rows close first.
- CTO follow-up (63560): decision (1) resolved via BD's Position Only dim; cross-tab surfaced
  $26.0M in 4 supervised Voya accounts flat across the Q2 close -- UNDETERMINED (legit
  low-frequency cadence vs stalled feed), discriminating asOfDate test named, W1 first-order.
  Noted at this seat: that $26.0M rides inside the served $449.7M supervised figure; no
  artifact change without a ruling.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| G4/G4b rows left open at the gate close | The cite's own words: not pre-cleared; behavioral acceptance = tonight's named run + morning verify |
| No self-dispatch on DATA_BDINSURANCE items | No TO/GO; presumptive lane confirmed at decomposition only (P0-is-what-Andrew-says discipline) |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.2.0_DS_PortfolioAnalytics/deliverables/COT_SUPERVISED_PROOF_OF_SPEC_020_20260820.json` | Authored; then G7 row -> PASS with CTO cite | Yes -- 6a83f3f08a, f88692d7b4 |

---

## Blockers

None. Two open TO rows ride tonight's scheduled cot run (external time gate, named).

---

## Current State (handoff-grade)

- COT_SUPERVISED DS legs: CLOSED at both gates (COO 63441, CTO 63443). Proof instance
  VALID rc=0 at `org/tier2_senior/0.2.0_DS_PortfolioAnalytics/deliverables/COT_SUPERVISED_PROOF_OF_SPEC_020_20260820.json` @f88692d7b4.
- Served artifacts live: `s3://opal-data-cot/gold/dimensions/accounts_dimension_latest.parquet`
  (943x27), `s3://opal-data-cot/gold/artifacts/supervised_split.json` (98 dates, 4 books,
  G6 caveats in meta), `s3://opal-data-cot/silver/account_attributes/2026-08-19.parquet`.
- OPEN: G4 invariant first fire + G4b behavioral acceptance ride TONIGHT'S scheduled cot
  ingest run (the nightly enumerates TABLE_QUERY_TYPE.keys(), which now carries
  account_attributes). Morning-after: verify bronze sentinel + run/verify silver consuming
  the new date + confirm B_00's invariant line, then flip both rows and re-validate the
  instance. 0.6.2 owns the run observation for G4; their bronze proof instance + RAVC follows it.
- PENDING (not dispatched): DATA_BDINSURANCE W3-classification leg presumptively routes here
  at COO's decomposition cut.
- Watcher: persistent Monitor task bkwsvar5i live; broker summary current.

## Next Steps

1. [me] Morning-after G4/G4b verification -> row flips -> instance re-validation -> one-line to [2.0.0_SA_COO] cc [1.0.0_SA_CTO].
2. [2.0.0_SA_COO] DATA_BDINSURANCE decomposition cut; W3 lane confirmation if it routes here.
3. [0.6.2_AE_PartnerETL] Tonight-run RAVC + bronze proof instance (their lane; no action from me).
