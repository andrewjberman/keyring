# C2 RARITY-COORDINATE RIDER -- spec (rides the R1 instance-materialization act)
**Seat:** 4.0.0_SA_CRO (base) · **Status:** SPEC-READY, PROPOSED · **Date:** 2026-08-20 ~2100Z
**Authority:** Andrew-direct 2026-08-20 ~1945Z ("Recs approved" on the /open-calls card -- BOTH populations, per-firm AND
estate-wide, each printed with its denominator; record `ANDREW_DIRECT_20260820_RARITY_DENOMINATOR_AND_DEVICE_AXIS.md`) +
his premise the same day (verbatim, the design constraint of this whole rider): *"basically just logging a figure of how
many times the shape was discovered in the estate, which is interesting if there is a C2 shape that is highly distinct but
very similar to one that is not highly distinct, for example, could be a sign ... we want to essentially 'stage' data in
very tight, high-signal manners for agents, because the agents then use their reasoning to do the magic."*
**Rides:** R1 (4.0.0_SA_CRO~B census report: C2/C3.i instance grain ABSENT from the graph -- 19 `C2Motif` rows, 0 instances)
-- the rider adds COORDINATES to the instance/family rows that R1 materializes; it does not materialize anything itself.
Machine-side owner candidate 0.8.0_AE_CloudComp (COO dispatches; CRO does not).
**Cites, never re-declares:** `org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` (the twelve families + `first_pass_recurrence`,
`honesty_invariants.c2_c3` "DISCOVERED, never declared -- membership comes from recurrence (>=2)"); PRD_EPISTEMIC_MECHANIZATION
sec.2 (Observation_Record envelope, denominators); Response II sec.2.4 (family identity is the quotient under a ratified
substitution policy that preserves D3 obligations; edit distance PROPOSES, never DEFINES).

## 0. The design constraint (why this is coordinates and not a verdict)
The rider STAGES axes; it computes NO verdict. "A distinct shape very similar to a common one could be a sign" is the
agent's inference to make from (recurrence, nearest_family, distance, that family's recurrence) -- if the rider pre-computed
"suspicious", it would be an alarm-shaped deliverable (the NEVER moratorium class) and it would be wrong the first time the
metric moved. High-signal staging = the four coordinates plus their denominators, nothing folded.

## 1. The rider fields (per C2 FAMILY row, and per C2 INSTANCE row where R1 materializes instances)
| Field | Grain | What it is | Produce-time honesty |
|---|---|---|---|
| `recurrence` | family x population | count of instances of THIS family in the population | computed from R1's materialized instances; until R1 lands the ONLY figure is the canonical's hand-counted `first_pass_recurrence` (estate-wide only, 12 families, values 2..30) -- carried as `basis: first_pass_hand_count`, never presented as a measured population figure |
| `rarity_denominator` | population | total C2 instances (ALL families) in that population -- the thing `recurrence` is a count OF | printed beside every recurrence; a recurrence without it is a number without a frame |
| `population_scope` | population | WHICH population the pair above is over: `ESTATE` or `FIRM:<tree>` (bd / inf / cot / mdpf -- the firm-partitioned trees, the same partition Rule 21's "name the tree you searched" law names) | BOTH rows are produced per family (Andrew's ruling); a family with 0 instances in a firm carries recurrence 0 WITH that firm's denominator -- a true zero, framed |
| `nearest_family` | family | the family whose canonical form is at minimum distance under the named metric -- EXCLUDING itself | PROPOSAL device only (Response II): identity is decided by the substitution policy, never by distance |
| `distance` | family pair | the metric value, under `metric_ref` (name@version, e.g. role-typed path edit distance) | a distance without `metric_ref` is not a coordinate; metric changes re-stamp every row (invalidation predicate) |
| `d3_preserving` | family pair | whether the substitution that maps this family onto `nearest_family` preserves the declared D3 obligations | enum below; today's D3 population is ~0, so the honest dominant value is `UNKNOWN_NO_D3_DECLARED` -- the rider MUST NOT emit `PRESERVED` by default |
| `vintage` | row | canonical blob + instance-set commit + metric version | every row; the coordinates are a fact at a vintage |

Two consumers, named so the rider is not YAGNI: (1) agents reasoning over C2 state (Andrew's premise); (2) the
motif-identity formalization (Response II sec.2.4 retrodiction pass) -- `nearest_family`+`distance` are its candidate
generator, `d3_preserving` its discriminator.

## 2. Rule-24 record for the rider's own enumerations
| Axis | Declared layer | Values | (i) MECE / CE | (ii) grain | (iii) intent | (iv) stability |
|---|---|---|---|---|---|---|
| `population_scope` | the populations a rarity figure is counted over | `ESTATE` · `FIRM:<tree>` (tree in the firm partition) | exclusive (one population per row); CE over the ruled two-population law -- hunted: "per-vertical" (C3.ii) is a DIFFERENT grain and is NOT a value here (it would be a third population; it is not ruled) | population | one (which denominator) | stable; a new firm tree adds a FIRM value by partition, not by authoring |
| `d3_preserving` | D3-obligation preservation under the mapping family -> nearest_family | `PRESERVED` · `NOT_PRESERVED` · `UNKNOWN_NO_D3_DECLARED` | exclusive; CE closed by the UNKNOWN terminal (the state most rows are in today) | family pair | one (does the substitution change obligations) | state axis = D3 population; as D3 obligations get declared rows MOVE from UNKNOWN to one of the other two -- all values move under ONE remedy (contract-record population), named |
| `recurrence.basis` | how the count was obtained | `MEASURED_INSTANCE_SET` · `FIRST_PASS_HAND_COUNT` | exclusive + exhaustive over the two ways a recurrence exists today | family x population | one (provenance of the number) | FIRST_PASS rows retire when R1 lands -- the axis exists to make that transition visible, not permanent |
Token census (word-boundary, RUN at authoring 2026-08-20 ~2058Z over SYSTEM_DEFINITIONS / rule bank / canonical, counts
printed as defs/bank/canon): `rarity` 0/0/0 · `rarity_denominator` 0/0/0 · `nearest_family` 0/0/0 · `d3_preserving` 0/0/0 ·
`population_scope` 0/0/0 · `PRESERVED` 0/0/0 · `NOT_PRESERVED` 0/0/0 · `UNKNOWN_NO_D3_DECLARED` 0/0/0 · `substitution_policy`
0/0/0 · `canonical_form` 0/0/0 -- all unoccupied; `recurrence` 1/2/1 = REUSED in the canonical's own sense (the honesty
invariant "membership comes from recurrence (>=2)"), not re-coined.

## 3. Production rule (for the R1 owner; the rider's one algorithm)
1. Materialize instances per family (R1's act, not this rider's). 2. For each family F and each population P in
{ESTATE} U {FIRM:t for t in the firm partition}: `recurrence(F,P)` = |instances of F in P|, `rarity_denominator(P)` =
|all instances in P|; emit BOTH rows; print the denominators. 3. For each family F: canonical form under the ratified
substitution policy@v (if none is ratified yet: the canonical's `shape` string, declared as `policy: NONE_RATIFIED`);
`nearest_family` = argmin over G != F of metric(F,G); `distance` = that value; `metric_ref` stamped. 4. `d3_preserving` =
`UNKNOWN_NO_D3_DECLARED` unless BOTH families carry declared D3 obligations, in which case compare them. 5. Every row
carries `vintage`. 6. Two-run byte reproducibility over the same inputs (the census standard) before the first commit.

## 4. What this spec does NOT do
Does not dispatch (COO routes the R1 owner act); does not mint a C2 family or touch the canonical; does not define family
identity (the substitution policy does, when ratified); does not compute a "suspicious" flag. Does not prejudge the
per-vertical population -- if Andrew wants a third population, that is a ruling, not an inference from this spec.
