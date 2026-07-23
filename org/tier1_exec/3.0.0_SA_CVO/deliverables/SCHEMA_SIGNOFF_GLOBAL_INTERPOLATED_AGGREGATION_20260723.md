# TANDEM SCHEMA SIGN-OFF + PERSPECTIVE -- Global interpolated-backfill aggregation

**Verifier:** `3.0.0_SA_CVO` · **2026-07-23** · **archetype:** VALIDATE
**Andrew-named** (CTO relay 023059Z; chain Andrew -> CTO/CRO -> CVO review -> COO decomposition).
**Two producers reviewed IN TANDEM:** CTO aggregation spec `@7ed8a6fd0` · CRO interpolation design
`org/tier1_exec/4.0.0_SA_CRO/briefs/COTTONWOOD_INTERPOLATED_BACKFILL_DESIGN_SPEC_20260723.md`.
**Incumbent carrier grounded at source:** `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py`
(read this session; last-touch Jul 2, so run-vintage == the shape below).

---

## VERDICT: **SCHEMA NOT YET AGREED -- DO NOT BUILD EITHER SIDE.** Design is sound on both; the two
specs describe **five incompatible shapes for one channel**, and three of them are the *exact*
"two treatments of one concept" class this tandem check exists to stop (the by_model NULL-vs-0.0
artifact from tonight). None is a disagreement about the METHOD; all are shape. **They are cheap to
reconcile now and silent-breaking after build.** Perspective on the guards is strong-with-two-holes.

---

# PART 1 -- SCHEMA AGREEMENT (the tandem surface I own)

## >> S1 (P0) -- THE ENUM STRING DISAGREES, AND IT SILENTLY DEFEATS THE TAINT RULE. <<
- **Incumbent code, Andrew-established:** the literal is **`interpolated_estimate`**
  (`build_aggregate_aua_timeseries.py:482`, `:530` basis-provenance comment; 49financial precedent).
- **CRO** aligns exactly (`§3.1`, `§6` "extend the convention, do not fork") -> emits `interpolated_estimate`.
- **CTO** writes `provenance: measured|interpolated|absent` (`§2`) and `point_class: measured|interpolated` (`§4`).

CTO's aggregator derives `point_class` by **any-component-interpolated**. If the producer stamps
`interpolated_estimate` and the aggregator tests `== "interpolated"`, **the test never matches -> every
interpolated point derives `point_class = measured` -> renders SOLID, unlabeled, and passes into
measured-only consumers.** That is precisely §5.1's "planted interpolated point renders unlabeled"
mutant -- **live in the current spec pair, not hypothetical.** **Resolution: `interpolated_estimate`
is canonical (it is the incumbent + CRO). CTO's spec adopts it, or the schema declares one explicit
mapping table and both sides cite it.** One string; it is the whole ballgame.

## >> S2 (P0) -- GUARD 1 CONTRADICTS THE ACTUAL CARRIER. The served shape is PARALLEL ARRAYS. <<
CTO guard 3.1: *"values and provenance ship in one dated tuple, not parallel arrays a consumer can
split"* -- the construction the "no unlabeled read possible" claim rests on.
**The incumbent served slice is parallel per-date arrays** (`:573-578`): `model_aua: []`,
`non_model_aua: []`, `partner_custody_total: []`, **`cohort_provenance: []`** -- four independent
arrays indexed by date position. **A consumer CAN read `model_aua[i]` without `cohort_provenance[i]`;
the arrays are exactly "splittable."** And CRO `§3.1` explicitly **extends this parallel-array channel.**
So guard 1 is either (a) a **breaking re-shape** of the served series into per-date tuples -- a v1
contract change CTO's own "v1-frozen-additive" discipline forbids -- or (b) aspirational, in which case
**"an unlabeled read is impossible" is FALSE** and the headline guard does not hold. **This must be
decided before build: tuple-reshape (and own the migration) OR keep parallel arrays (and replace guard 1
with an index-alignment validator + a consumer-contract that reads the pair or refuses).** It cannot be
both.

## S3 (P1) -- PROVENANCE GRANULARITY: per-firm scalar (CTO) vs per-cohort array (incumbent + CRO).
Incumbent `cohort_provenance` is **per-date, per-COHORT**: `{custody: measured|rollforward, model_1a:
measured, sma_1c: interpolated_estimate}` (`:480-482`). CTO `§4` flattens to **one scalar
`by_firm.{firm}.provenance`.** These are different grains. It matters for the real Cottonwood case my
own sweep tonight measured: **`fact_holdings` is measured 06-09->07-20 while `fact_model_assignment` is
07-21/22 only** -- so in 06-09->07-20 Cottonwood's VALUE is measured but its ASSIGNMENT is interpolated.
The per-cohort channel represents that natively; CTO's single scalar must **collapse** it, and CRO `§5`
does collapse (assignment taint dominates -> whole point `interpolated_estimate`). **The collapse rule
is correct but UNSTATED in CTO's schema.** Fix: schema states the per-firm scalar is the *derived
taint-collapse* (any-cohort-interpolated) of the preserved per-cohort vector -- never a second,
independently-written field. Two writers, one derived-from-the-other, never two sources.

## S4 (P1) -- CONTAINER SHAPE: `by_firm: {<firm>: {...}}` (CTO) vs `partners: {firm_id: {...}}` dict
already in code (`:568` `.items()`). Same idea, different key name -> an aggregator written to CTO's
`by_firm` will not find the producer's `partners`. Pick one key. (Incumbent is `partners`.)

## S5 (P1) -- INTERP-METADATA FIELD NAMES forked three ways.
| concept | CTO `§4` | CRO / incumbent |
|---|---|---|
| method tag | `interp.method_version` | `backfill_method` (`:409`), union `backfill_methods` (`:454`); CRO `cot_snapshot_flow_fuzzy_20260723` |
| period | `meta.interpolation.affected_period` + a separate `interp.window_id` | CRO `affected_period [start,end]`; **no `window_id`** |
| confidence | `interp.confidence` | CRO `confidence` scalar (`§5`) -- **agree** |
`method_version` is a new name for the existing `backfill_method`; `window_id` has no counterpart and
may be `affected_period` named twice. **Canonicalize to the incumbent names** (`backfill_method`,
`affected_period`); keep `confidence`.

## S6 (P1) -- TWO ENFORCEMENT HANDLES for one quarantine. CRO `§3.3` filters measured-only consumers on
**`source=interpolated`** (the append-spec `source` key); CTO guard 3.1 filters on **`provenance`
class**; the incumbent channel is **`cohort_provenance`**. **Three field names for "is this point
interpolated?"** A consumer filtering on `source` while the aggregator tags `cohort_provenance` misses.
**One canonical quarantine key, cited by every measured-only consumer.** This is S1 wearing a second hat
and it is the same failure family.

## S7 (P2) -- ABSENT vs NULL. CTO provenance enum includes `absent`; incumbent uses **null**
`cohort_provenance` for unlabeled regions (`:484`, `:542`); CRO says `null/absent`. Two spellings of
"no label here." Pick one token; a mixed `absent`/`null` is a miniature of the artifact this check
exists to prevent.

---

# PART 2 -- PERSPECTIVE (CTO ask 1: any path to a measured-only consumer or an unlabeled render?)

**Two real paths beyond the schema mismatches above (S1 and S2 are themselves the two biggest paths in).**

## >> P-A (P1) -- THE ABSENCE FLOOR IS PER-MODEL IN CTO, PER-ACCOUNT IN CRO. The looser one re-admits a
YANG_SITTW sibling. << CTO guard 2: no interpolated point *"before the model's creation date."* CRO
`§5` + `§8.2`: no point before model creation **AND** before the **account's first-existence date**
(*"an account created 07-06 has no interpolated history before 07-06"*). **CTO's floor is weaker:** an
account created 07-06 on a model created 05-28 could receive interpolated points 05-28->07-06 under
CTO's guard (model existed) that CRO's rule forbids (account did not exist). **That is the exact shape
of the logged fabrication both specs cite** (`YANG_SITTW.TO-1`: $19.67M invented where the true value
was $0). **The binding floor is `max(model_creation, account_first_existence)` per point, enforced by
BOTH producer and validator.** CTO's schema ceiling must carry the per-account floor, not only the
per-model one.

## P-B (P1) -- RADIAL/BELL PROTECTION IS AN ASSUMPTION, NOT A GUARD. CTO `§1` protects the radial +
bell curve "by construction (current snapshot)." True **only while the radial's data source is a live
current read.** The leak path: if the radial ever computes its current figure as `timeseries[-1]`, and
there is any lag window where the newest Cottonwood point is interpolated (measured-forward not yet
landed), an interpolated value reaches the fee-basis radial. CTO's own `§2` hedges with "while the
fee-basis figure is current-only" -- **that "while" is the load-bearing conditional and it is
unguarded.** Make it structural: **assert `radial.source != timeseries-tail`** (radial reads the
current-snapshot artifact), and mutant M-B below plants an interpolated tail and confirms the radial
does not move.

**What is genuinely SOUND and I am not re-opening:** additivity-unchanged (value = sum regardless of
provenance; label not haircut) is correct and matches Andrew's "doesn't need to be exact." Supersession
being provenance-derived (overlay window shrinks automatically) is the right construction. CRO's
value-leg/assignment-leg split (value measured where snapshots exist, estimate only on assignment) is
honest and my sweep grounds its period map. The fingerprint-ban reconciliation (`§3`: inference-as-
interpolation is a different product category than inference-as-fact) holds **provided S6's single
quarantine key makes "never crosses into the fact channel" structural rather than promised.**

---

# PART 3 -- MUTANT SET (design-before-build; CTO's four + three the mismatches force)

| # | mutant | must produce | proves |
|---|---|---|---|
| M1 | planted `interpolated_estimate` point in the series | rejected by EVERY measured-only consumer (fee/DDB/identity/freshness) **and** renders yellow-dashed | CTO §5.1 core |
| M2 | same point, but stamped `interpolated` (CTO's string) | **the test above must still catch it OR the build fails** | **S1 -- the enum-mismatch is the mutant** |
| M3 | pre-**model**-creation date | refused by producer AND validator, independently | CTO guard 2 |
| M4 | pre-**account**-existence date (account 07-06, model 05-28, point 06-15) | refused by BOTH | **P-A -- the per-account floor** |
| M5 | interpolated estimate attempts to supersede a correctly-emitted **null/$0** | **FAIL LOUD** | YANG_SITTW replay (CRO §3.4 / §7) as a test, not a promise |
| M6 | read `model_aua[i]` without `cohort_provenance[i]` (parallel-array split) | **impossible, or the read refuses** | **S2 -- guard 1 vs the real carrier** |
| M7 | interpolated tail point + read the radial | radial value **unchanged** | **P-B -- radial source is a live read** |

**Each must be designed so it CAN fail** -- M2/M4/M6 in particular exist because a spec that agrees with
itself would pass them while the two-spec pair does not.

---

## ROUTING (verify-not-fix; I sign off nothing until the shapes are one)
- **CTO:** adopt `interpolated_estimate` (S1); decide guard-1 tuple-reshape vs parallel-array-validator
  (S2); state the per-firm scalar as derived-collapse (S3); align container + field names to incumbent
  (S4/S5); carry the per-account floor (P-A); make radial-source a guard (P-B).
- **CRO:** confirm the producer emits the incumbent `cohort_provenance` per-cohort array (not a per-firm
  scalar) and one quarantine key (S6); confirm the per-account floor is in the producer, not only the
  validator (P-A/M4).
- **COO:** do NOT decompose either spec into build TOs until S1+S2 are resolved -- they change the
  producer's output contract, so a TO written now builds the wrong shape.

## RESIDUAL / not verified
- I did **not** confirm the Global aggregator currently reads Cottonwood at all pre-07-21 (it may
  contribute nothing to Global `model_aua` today, since model_aua needs assignment). If it does not,
  interpolation is purely additive to Global history; if it does, there is an existing value to
  supersede. **COO's decomposition should settle this before the producer TO.**
- CRO's METHOD (backwards value reconstruction, fuzzy assignment, terminal-model washout) is **out of my
  scope** per CTO `§6` and CRO `§9`; I reviewed the SCHEMA and the honesty boundary, not the estimator's
  accuracy.

-- `3.0.0_SA_CVO`
