# D11 / NFRA_C3MATERIALIZE — THE FOUR WAVE-1-BOUNDARY DECLARATIONS (L3-C01, L3-C03, L3-C04, L4-C02)

**Author / owner** `1.0.0_SA_CTO~X` (design lane) · **issued** 2026-08-29 01:4xZ · **due** at the wave-1 boundary per the framing sec 4 (`D11_L3_CUT_FRAMING_20260828_222xZ.md` @`519d4a7a4e`) and called by the issuer at 80177: *"these four declarations are the wave-2 gate: no fusion cut is issued until they land."*
**Boundary reached:** L3 wave 1 CLOSED at the faces — TO-L3W1-CCX + TO-L3W1-COX @`60d51210f8`, TO-L3W1-CCY @`519bb75c8f`, on `3.0.0_SA_CVO~X` PASSes 011716Z / 011809Z / 012746Z; 76 of 76 cells; **the bridge registry's settled pin is `@8ff31fa1c8`** (8 shards + VIEW_PAIR + BRIDGE_ROW.schema.json, issuer-measured by `ls-tree`).
**Every number below is measured at a named pin or declared `held` with its exercise named. Nothing here is a milestone claim, and NOTHING here discharges a PRD §6 falsification test.**

---

## 0. WHAT THE FOUR ARE FOR, IN ONE LINE EACH

| id | question | this declaration |
|---|---|---|
| **L3-C01** | how do we know a fused affinity is stable rather than one run's artifact? | a split-half metric PAIR, a declared floor, and a permuted control that must fail |
| **L3-C03** | cover or partition for the cross-domain memberships? | **COVER**, measured; a partition is a projection of it, never its replacement |
| **L3-C04** | SNF, or something else? | **SNF retained** — and a measured precondition that changes what wave 2 can fuse |
| **L4-C02** | over how many nightly runs is identity persistence measured? | not a constant — an observable, because the cadence field it would have rested on is null 47 of 72 |

---

## 1. L3-C01 — STABILITY METRIC AND THRESHOLD

**THE DECLARATION.** A fused affinity is admitted as evidence only when it is shown STABLE against the stochasticity of its own inputs, by a **split-half** exercise reported with **two** statistics:

1. Build the stochastic view's consensus **twice**, from **disjoint halves of its N runs** (for the delivered STRUCTURE view: runs 1–12 and 13–25 of the accepted N=25 battery, `build eb009c01`, image `sha256:17fdebd7…`), fuse each half identically with the other admitted views, and compare the two fused matrices **over the full pair domain**.
2. **SPEARMAN RANK CORRELATION** of the pair values, ρ.
3. **TOP-DECILE PAIR-SET JACCARD**, J — the intersection over union of the top 10 % of pairs by fused affinity in each half.

**THRESHOLD (declared floor):** ρ ≥ **0.90** AND J ≥ **0.80**. **BASIS: `held`, not `measured`** — these are the floors this seat is willing to defend before any fusion has run; the FIRST fusion experiment REPORTS the observed ρ and J, and the floor is **re-derived from that evidence before it binds any acceptance**. A threshold that has never seen its own distribution is a preference, and it is labelled as one here rather than shipped as a measurement.

**WHY TWO STATISTICS AND NOT ONE — measured, and it is the whole point.** B4's discrimination gate measured **26 distinct affinity values over 189,764,421 pairs** with a heavily zero-weighted histogram (`W_STRUCTURE_FACTORIZED.json` sha256 `e91d6991…`, CRO STRUCTURE CONFORMS 212818Z). A rank correlation over that domain is dominated by the agreeing zero mass: **two halves could agree at ρ > 0.99 while disagreeing about every pair that carries signal.** J is the arm that can fail when the zeros agree. **A single statistic is REFUSED for this reason**; both must pass, and both are reported with the pair denominator beside them.

**THE FALSIFIER (required, and it must FIRE).** Fuse view A with a **randomly relabelled** view B — the same values, permuted across entities — and recompute ρ and J. **Both must drop below the floors.** If the permuted control does not drop, the statistics are not measuring agreement between views and the threshold means nothing: that is a defect in the instrument, reported as such, and no fused artifact is admitted on it. (This is the same shape as B4's all-one mutant, which is why it is specified before the first run rather than after a suspicious result.)

**COST AND NON-APPLICATION, stated:** one extra fusion pass per experiment (B4's measured battery was 468.9 s wall on `BUILD_GENERAL1_LARGE` at ≈ USD 0.16 on an unverified published rate; a split-half doubles the consensus assembly, not the 25-run battery). It binds **fusion experiments only** — no wave-1 registry row, no L2 artifact, and no re-delivery is re-opened by it.

---

## 2. L3-C03 — COVER vs PARTITION

**THE DECLARATION.** The membership layer is a **COVER**. An algorithm may emit a **partition** as a view — SBM does, and B4's accepted artifact is one — but **the partition is a PROJECTION of the cover, never its replacement**, and no fusion or identity act may treat a partition as the membership truth.

**MEASURED, at the registry's settled pin `@8ff31fa1c8`** (each figure from the lane that owns the subject; the probe's capability is stated with every result):

| bridge | multi-parent | probe could return > 1? | verdict |
|---|---|---|---|
| `motif_to_pipeline` | **187 of 1,291** targets, max 3 | yes | **COVER** |
| `motif_to_arn` | **194 of 1,101** bridged, max 5 (1:907, 2:53, 3:87, 4:52, 5:2) | yes | **COVER** |
| `motif_to_path` | **10 of 91** resolved paths | yes | **COVER** |
| `symbol_to_file`, `arn_to_service`, `pipesym_to_firm`, `motif_instance_to_family` | 1 by construction | **NO — a CONTAINS edge carries one source; a firm/service parse yields one token** | **UNMEASURED, not FUNCTION** |

**Every direction whose instrument COULD answer "many" DID.** The single-parent results are properties of those probes, not of the world — L1's own disowned `fan-out = 1` tautology (`L1_CANONICAL_GRAIN_DECLARATION.md` :52-58), here made refusable instead of repeated. The capable probes are the positive control for the incapable ones: the instrument class is shown able to return a multi-parent answer.

**THE 540 CROSS-DOMAIN MEMBERSHIPS — the regression cohort, operationalised.** PRD §10 (d) already ruled membership persistence COVER-CAPABLE and named the 540 a required regression cohort. This declaration makes that mechanical: **every clustering / materializer / fusion experiment record carries a REQUIRED field reporting the cohort's disposition — `preserved` / `merged_away` / `split` per member, with the denominator 540 printed.** A run that cannot state it does not report "no change"; it reports the field ABSENT, which is a refusal to credit the run's membership claims. (PRD §5: *for the 1,843 a partition is a CLEANUP, for the 540 it is a LOSS.*)

**THE FAMILY AXIS IS TWO CATALOGUES, NOT ONE ENUM** (this seat's ruling 79923-26, re-measured independently by `0.8.0_AE_CloudComp~Y` by set equality): the 19 motif families are **13 STRUCTURAL archetypes** (AB store: a-access … b-struct) **+ 6 DEFECT motifs** (base store: dead-component, orphan-endpoint, …), **intersection 0**. Wave 2 carries two axes, or one axis per catalogue — **never a flat 19-valued enum**, which would compare an archetype to a defect and return a full matrix (Rule 24 (iii), one axis one intent).

**THE FALSIFIER.** Exhibit a bridge direction whose probe CAN return multiple parents and, over the whole population, does not — that direction is a FUNCTION and the cover claim is over-broad for it. One such case narrows the declaration to the directions it was measured on.

**⛔ NOT DECIDED HERE.** The **PRODUCT SEMANTICS** of the 540 — what a cross-domain membership MEANS to a user — is recorded in PRD §10 as **still open at Andrew** and is untouched by this declaration. This is the engineering form only: the storage is a cover, the cohort is reported, and nothing forecloses either answer to his question.

---

## 3. L3-C04 — SNF vs THE ALTERNATIVES

**THE DECLARATION.** **Similarity Network Fusion is RETAINED** as the fusion method. Alternatives, each named and refused **on the record** as the framing requires:

- **(a) Weighted linear combination of view affinities — REFUSED.** The PRD's own reason (§L3: *"weights are a declaration"*) plus a measured aggravation: with **two** admitted views a weight is a **one-parameter free choice that decides the answer**, and no seat can ground it. SNF is nonparametric in exactly this respect.
- **(b) Multilayer / multiplex SBM — REFUSED FOR THIS WAVE, and it is the strongest alternative.** Two grounds, both measured: (i) it requires all layers over **one node set**, and the delivered views share **|S ∩ B| = 0** (below); (ii) it returns a **partition natively**, colliding with §2's cover declaration — it would decide the cover question by choice of algorithm. **Recorded as the alternative to revisit** when a third view lands and a common set exists; this refusal is scoped to wave 2, not permanent.
- **(c) Intersection of the per-view graphs — REFUSED as empty.** Measured: the intersection is **0 entities**; the product would be empty. (PRD §L3 already forbids intersection for the coverage reason; here it is also vacuous.)

**⛔ THE MEASURED PRECONDITION, AND IT CHANGES WHAT WAVE 2 CAN FUSE.** SNF requires **one entity set across views**. Measured (`D11_L3_OVERLAP_VS_L2_20260829.json` @`bdc1246987`, CVO-verified; VIEW_PAIR cell at `@8ff31fa1c8`, three positive controls firing):

```
  |STRUCTURE| 19,482   |BEHAVIOR| 3,726   |STRUCTURE ∩ BEHAVIOR| = 0     (measured, not assumed)
  bridges reaching STRUCTURE : motif_to_arn 1,045 · motif_to_portalsym 1,495 · motif_to_pipeline 1,291
  bridges reaching BEHAVIOR  : NONE — motif_to_path's 91 endpoints are ALL under portal/, and
                               portal is a SUBMODULE GITLINK (mode 160000), so BEHAVIOR (a
                               workspace Git-DAG walk) carries 0 of 3,726 ids under portal/
```

**So the two delivered views cannot be fused with each other at wave 2 — not directly (zero intersection) and not through the registry (no bridge reaches BEHAVIOR).** What IS runnable today is a fusion over the **STRUCTURE entity set** of its topology view with a **motif-membership view** derived from the bridges that reach it (1,045 + 1,495 + 1,291 entity touches) — two views, one set, MEASURED/ABSENT per feature per PRD §L3, never the intersection.

**PRD §10.3 (f) IS NOT SATISFIABLE ON THE DELIVERED VIEWS, and that is Andrew's sequence, not mine to amend.** His ruled consequence reads *"first bridge is symbol→file, first fusion experiment runs at FILE carrier grain."* Measured: the `symbol` space is not a delivered L2 view, and no bridge reaches a workspace FILE. The first fusion can therefore only run at the **cloud-node carrier**. **This is SURFACED, not amended** — it is a carried card at Andrew (§5 below) and it does not block: wave 2 can be cut at the cloud-node carrier under his ruling's evident intent (run the first fusion where a bridge actually lands), or wait for the BEHAVIOR-over-portal view that would make FILE reachable. **The choice of which is his; the measurement is the design lane's.**

**THE FALSIFIER.** Exhibit two admitted views with a non-empty shared entity set at a declared grain, fuse them under SNF and under one refused alternative, and show the alternative's result better satisfies §6.3 (firm separation ≥ its own inputs, 0.989 / 0.974). One such case re-opens the choice.

---

## 4. L4-C02 — THE N-RUN WINDOW

**THE DECLARATION.** **N is not a constant to pick.** The persistence window is defined by an **observable**, with a floor and a ceiling, and the first run reports the evidence that the window was long enough:

> **The window must contain, for EVERY input in the fusion's population, either (a) at least TWO OBSERVED CHANGES of that input, or (b) an explicit FROZEN declaration for it.** A persistence rate measured across a window in which an input never moved does not measure survival — it measures that nothing happened, and it reads as a strong result.

**FLOOR 7 consecutive nightly runs · CEILING 30 for the first reporting window** (basis `held`; the floor observes any weekly rhythm at least once, the ceiling is one month of a nightly cadence). **The per-input change census — inputs changed ≥ 2 / changed once / unchanged / declared frozen, with the population denominator — is a REQUIRED output of the first persistence report**, and N is re-derived from it.

**⛔ WHY IT CANNOT BE DERIVED FROM DECLARED CADENCE — measured at this seat, over the 72 v3.1 cards at the settled pin `cf66984cfc`:**

```
  process.cadence present on            72 of 72 cards      (the field exists everywhere)
  declared_rhythm NULL                  47 of 72            (two thirds declare NO rhythm)
  live_matches_declared:  yes 8  ·  no 11  ·  unmeasured 28  ·  not_applicable 25
                                        -> of the 19 where it was actually MEASURED, 11 DO NOT MATCH
```

**A window derived from declared cadence would rest on a field that is absent two thirds of the time and wrong in a majority of the cases where anyone checked.** That is not an argument for a longer N; it is an argument that the DECLARED value is the wrong input and the OBSERVED change is the right one. (Instrument note, because the first read of this census was wrong at this seat: my first pass read `cadence.declared` and reported 47 ABSENT; the field is `cadence.declared_rhythm`, present on 72 of 72 and NULL on 47 — same number, right reason, and it was checked before it was quoted.)

**THE FALSIFIER.** Run the persistence measurement over a window in which a NAMED input is known to have changed. If no identity depending on that input moves at all, either the window is too short **or the signature does not depend on that input** — both are findings, and the second is the more interesting one.

**⛔ NOT DECIDED HERE.** The succession **MATCH threshold** (§L4's "match above threshold → SAME identity") is downstream of the first signature run and is L4's own declaration, not this one. **Identity-minting authority and cross-fabric reconciliation policy remain open at Andrew** (PRD §10).

---

## 5. WHAT THIS DECLARATION SET LEAVES OPEN, NAMED

1. **PRD §10.3 (f)'s FILE carrier grain is unreachable on the delivered views** (§3) — a carried card at Andrew; wave 2 is cuttable at the cloud-node carrier meanwhile.
2. **A BEHAVIOR view over the portal submodule's own history** — the gap that makes `motif_to_path` fusible; a **NAMED GAP for the BEHAVIOR view's producer** (`4.0.0_SA_CRO~A` lane family, TO-L2-CROA's deliverable), not an L3 act.
3. **A registry that MINTS part ids** — the derived-identity class logged three times on this project; owed by this seat as a registry v1.1 contract act at the next boundary, with the compile-provenance fields (`compiled_at_commit`, `subject_disposition`, `compile_note`) admitted at the same time.
4. **Product semantics of the 540** and **identity-minting authority** — open at Andrew, untouched here.

---

## 6. ADDENDUM 1 (2026-08-29 04:3xZ) — L3-C01: THE FLOOR RE-DERIVATION FORM, declared BEFORE the first run's spread exists

**Trigger.** The first fusion's preliminary shape (CCX 80783, read via broker, not consumed): J = 0.8033 against the held floor 0.80 — a 0.0033 margin over a floor that had never seen its own distribution. Ruled 80787: the held floors bind run 1 in **neither** direction; run 1 is admitted on the permuted control firing (permuted ρ −0.1448 / J 0.1790 against observed 0.9584 / 0.8033); the re-derived floor binds run 2. 80787 deferred *"the exact form"* to the first run's record. **The form does not depend on the numbers, so it is declared here, before them** — a form chosen after seeing where 0.8033 falls would be a floor fitted to the result.

**THE FORM.** For each statistic S ∈ {ρ, J}, over the metric domain of 80804 (the both-measured pairs):
- **null_S** = the value of S under the permuted-labels control; **spread_S** = the standard deviation of S over **N ≥ 5** independent permutations (N printed).
- **floor_S (RE-DERIVED)** = **null_S + 3 · spread_S** — three null-spread widths above the run's own noise floor. The multiplier 3 is DECLARED here, not derived, and is the one typed constant in the form; it is chosen so a statistic that clears the floor is outside the null by a margin no single permutation draw reaches, and it is recorded as `held` until a second run shows the spread is stable across runs.
- **Sanity arm (must hold, printed):** floor_S must lie strictly BELOW the observed S of the run it was derived from — a re-derived floor the deriving run itself fails is a finding about the spread (too wide to discriminate), reported as such, and the floor status stays HELD-UNEXERCISED for run 2.
- **If only ONE permutation exists at publish** (the preliminary shape reports one): spread_S is UNMEASURED, no floor is re-derived, `floor_status` stays **HELD-UNEXERCISED** into run 2, and the N ≥ 5 permutation battery is run 2's first addition. The record states which case it is.

**What this replaces and what it does not.** It replaces the held constants 0.90 / 0.80 **only from the run at which spread_S exists**; until then they stay reported as HELD-UNEXERCISED beside the observed values (CCX's checker already encodes that regime, `floor_status ∈ {HELD-UNEXERCISED, RE-DERIVED}`). It does not touch the validity arm (the permuted control must still drop below the observed for both statistics — that binds every run), the metric domain (80804), or the two-frame sec-6.3 rule (80835), which is a separate axis.

**Falsifier.** Exhibit a run whose observed S clears null_S + 3·spread_S while a second, independent permutation battery of the same run yields a spread under which it does not — the multiplier is then too small for the noise at this view pair and is raised on the record, never lowered.

### 6a. ADDENDUM 1a (04:4xZ) — THE DERIVATION-PROVENANCE CARRIER, one canonical shape so no two lanes mint incompatible ones

**Trigger.** CCX's typed checker (80860) found that its two exit-2 verdicts — SPREAD_SANITY_FAIL and STABILITY_FAIL — were the SAME comparison, because the sanity arm is about **the run the floor was derived from** while the binding check is about **the run being evaluated**, and with one observation set the two are indistinguishable. CCX proposed a `deriving_run_observed` field; the certifier accepted the requirement and reserved the key to the design lane (044353Z). Ruled here.

**THE CARRIER.** On any artifact whose `floor_status = RE-DERIVED`, one block per statistic, `floor_derivation.<S>` for S ∈ {rho, J}:

| field | type | meaning |
|---|---|---|
| `derived_from_run_id` | string | the run whose permutation battery produced the floor |
| `derived_at_commit` | commit | where that run's artifact is pinned |
| `metric_domain` | string | `both-measured` + the pair denominator (80804) |
| `null` | number | S under the permuted-labels control, that run |
| `spread` | number | sd of S over the battery |
| `n_permutations` | integer ≥ 5 | the battery size (N = 1 → this block MUST NOT exist; `floor_status` stays HELD-UNEXERCISED) |
| `multiplier` | number | 3 (basis `held` until run-2 spread stability) |
| `floor` | number | = null + multiplier · spread, and the checker RECOMPUTES it (FORM_DEFECT if it differs) |
| `deriving_run_observed` | number | S observed on `derived_from_run_id` — the SANITY arm's reference |
| `sanity` | bool | `deriving_run_observed > floor` (strict) |

The **evaluated** run's own `observed.<S>` lives beside it, outside the block, and is what the **binding** check reads. ~~When the deriving run IS the evaluated run (run 1 → run 2 derivation applied within run 1's record), the two references coincide by construction — the only case where they should.~~ **⛔ THAT SENTENCE WAS A DEFECT — struck by Addendum 1b below (certifier 045433Z): a same-run block would have to carry `derived_at_commit` = the hash of the commit containing itself.**

### 6b. ADDENDUM 1b (04:5xZ) — NO SAME-RUN EMISSION: the `floor_derivation` block lives only in a LATER artifact, and always points BACKWARD to a committed one

**The defect (3.0.0_SA_CVO~X 045433Z, verified at @61891652ef):** 6a permitted the deriving run to equal the evaluated run while requiring `derived_at_commit` to pin the deriving run's artifact — inside an artifact that IS that run's. An immutable artifact cannot contain the hash of the commit that contains it. The certifier refused to improvise a sentinel, a parent pin, or a self token; correct.

**THE RULING — one non-circular shape, and it is the one §6 already implied:** the re-derived floor **binds the NEXT run**, so it never needs to appear in the run it came from.
- The **fusion artifact of run N** carries the permutation battery as **evidence** — `null`, `spread`, `n_permutations`, and run N's own `observed` per statistic — but its `floor_status` is **HELD-UNEXERCISED**, and it carries **no `floor_derivation` block**. A run-N artifact with a RE-DERIVED status is refused (FORM_DEFECT).
- The **`floor_derivation` block appears only in a LATER, separately committed artifact** that evaluates against the floor: run N+1's fusion record, or the stability consumer's binding rows (CCX's L3W2-xkbc) for run N+1. Its `derived_from_run_id` / `derived_at_commit` / `derived_artifact_sha256` point **backward** to run N's already-committed artifact; `deriving_run_observed` is read FROM that artifact, never restated; the block's own `floor` is recomputed from that artifact's `null` and `spread`.
- Consequence for run 1 tonight: **the fusion artifact prints the battery (if N ≥ 5) and stays HELD-UNEXERCISED**; the first RE-DERIVED floor is applied by run 2's consumer, citing run 1's commit. The "deriving == evaluated" case of 6a is not a special case — it is **unreachable by construction**, which is the point.

**Fields added to the block:** `derived_artifact_sha256` (content digest of the deriving artifact at `derived_at_commit`, so the pointer is content-addressed as well as commit-addressed). `derived_at_commit` MUST be an ancestor of the artifact carrying the block (the checker tests it; a non-ancestor is FORM_DEFECT).

**Falsifier:** exhibit a well-formed `floor_derivation` block whose `derived_at_commit` is not an ancestor of the carrying commit, or whose `deriving_run_observed` differs from the value in the deriving artifact at that pin — either is a provenance defect, not a stability result.

### 6c. ADDENDUM 1c (05:0xZ) — THE RUN-N BATTERY EVIDENCE CARRIER, structured for N = 1 as for N ≥ 5

**Trigger.** The union re-emission @`1f5d4f6136` carries the one-permutation case as PROSE (*"ONE permutation was run, so this run provides a POINT, not a spread"*) beside `observed` and `permuted_control` values, with no `n_permutations` or `spread` field. Both certifiers (CRO 050207Z, CVO 050306Z): prose is not a rejectable carrier — a checker that reads it reads the tool, not the world. Correct; the design lane owes the shape.

**THE CARRIER.** On EVERY run-N fusion artifact, inside `stability_L3C01`, one block per statistic, `permutation_battery.<S>` for S ∈ {rho, J}:

| field | type | N = 1 | N ≥ 5 |
|---|---|---|---|
| `n_permutations` | integer ≥ 1 | 1 | N |
| `null` | number | the single permuted draw | mean of the draws |
| `spread` | number \| null | **null** | **SAMPLE** sd of the draws (ddof = 1; pinned 05:5xZ — every emitted battery tonight used it: b6 @`f8c1ad1b09` reads 0.109991 / 0.064550 where population sd would read 0.100407 / 0.058926; a population-sd artifact fails the `null`/`spread` arm as FORM_DEFECT) |
| `spread_status` | enum | **UNMEASURED** | MEASURED |
| `draws` | array of numbers | [the one draw] | all N (so a re-derivation can recompute null and spread) |
| `observed` | number | this run's S | this run's S |

`floor_status` on a run-N artifact is always **HELD-UNEXERCISED** (6b). A checker reads `n_permutations` and `spread_status`; it never parses prose. **Typed refusals:** `spread_status = MEASURED` with `n_permutations < 5` → FORM_DEFECT; `spread` non-null with `spread_status = UNMEASURED` → FORM_DEFECT; `draws` length ≠ `n_permutations` → FORM_DEFECT; `null` ≠ mean(`draws`) (or ≠ `draws[0]` at N = 1) → FORM_DEFECT. Prose beside the block is permitted and non-binding.

**Delivery for @`1f5d4f6136` (immutable):** a **superseding run-addressed restamp** by the emitter — every measured value byte-identical, the block added, `supersedes` naming `1f5d4f6136` — **not a sidecar.** A sidecar would split the evidence from the artifact the certification cites, and a split carrier is the class this fabric corrected three times tonight. The 6b block (`floor_derivation`, run N+1) reads `null`, `spread`, `n_permutations`, `observed` from THIS block at the deriving pin — the two carriers are now one contract.

### 6d. ADDENDUM 1d (05:3xZ) — ONE NULL PER ARTIFACT; a draw outside the band is evidence about the TAIL, and the battery grows before any floor is derived from it

**Trigger — read at the restamp @`ab8a2276bb`** (`fusion_l3w2cox-union-394bdac4c227-b5.json`, superseding `1f5d4f6136`; 0 of 179 measured leaves changed, 1c block present, all four FORM_DEFECT arms clean on both statistics, N = 5 MEASURED). The emitter ran N = 5 where the GO said N = 1; **1c governs and N = 5 is ACCEPTED** — five measured draws are not reduced to one to fit an instruction written before they existed. But the artifact ALSO carries the original single draw as `permuted_control` (ρ −0.144792, J 0.179046), untyped, beside the battery — and on J that draw lies **outside the battery's own band**: null 0.030864 + 3 × 0.025177 = **0.106395 < 0.179046** (≈ 5.9 spreads above the null; the five draws max at 0.066813). On ρ it lies inside (−0.145 within null ± 3 × 0.1008). Two null evidence sets on one artifact that disagree about J's tail is a **two-carriers-of-the-null** defect, and a run-2 J floor derived from the five alone (≈ 0.106) would be contradicted by a draw the same artifact already holds.

**RULING.**
1. **ONE NULL PER ARTIFACT.** Every permuted draw on a run-N artifact is either a member of `permutation_battery.<S>.draws` (same scheme, same metric domain) or is typed OUT of it: `permuted_control` survives only as `{scheme: <named>, metric_domain: <named>, in_battery: false, why: <one line>}`. A bare number beside a battery is FORM_DEFECT. The emitter answers WHICH by a line: if the 1f5 draw was the same scheme on the same 8,596,731-pair domain, it is `draws[0]` and N = 6 (null and spread recomputed; on J that is mean ≈ 0.0556, sd ≈ 0.066, band ≈ 0.25); if the scheme differed, it is labelled and does not enter.
2. **A DRAW OUTSIDE THE BAND OF THE OTHERS IS A TAIL OBSERVATION, not a stability result and not a falsifier.** It is recorded on the artifact as `permutation_battery.<S>.tail_observation: {draw, band_of_others, n_others}`; it moves NO multiplier (the falsifier of sec 6 is a second battery under which the OBSERVED no longer clears — here the observed 0.803 clears every draw by a wide margin). What it moves is **N**: the deriving battery for that statistic must reach **N ≥ 20** before any run-N+1 floor is derived from it (6b), and `floor_derivation` for that statistic carries `tail_observed_at_n: <N when first seen>`. Rationale: J is a top-decile overlap over a domain with heavy zero mass — discrete, skewed, tail-heavy; five draws bound its centre, not its tail, and a floor is a claim about the tail.
3. **Nothing about run 1's admission changes.** Admission stays on the fired control + observed-vs-permuted gap under every reading of the draw; `floor_status` HELD-UNEXERCISED; no `floor_derivation` on this artifact (6b). The 6.3 result and every other leaf are untouched.

**Delivery:** one line from the emitter (branch 1), then a further superseding restamp carrying the typed `permuted_control` and, on J, the `tail_observation` — values byte-identical again; or, if the emitter can run the N = 20 battery now on the same domain, the restamp carries it and 6b's run-2 derivation has a tail-bounded spread to read. **Falsifier of this addendum:** show the 1f5 draw was produced on a different metric domain than the battery — then it was never a sixth draw and item 2's N ≥ 20 trigger does not fire on its account (the trigger stays armed for any in-battery outlier).

### 6e. ADDENDUM 1e (06:2xZ) — FOUR CONTRACT GAPS THE CONSUMER FOUND BY RUNNING AGAINST THE REAL ARTIFACT (CCX 81104), plus the split-half carrier

**Trigger.** `0.8.0_AE_CloudComp~X` bound 1c/1d/sec 10 and ran its consumer against b6 @`f8c1ad1b09` at the pin: 0/4 arms fire on both statistics, sample-sd reproduces exactly, the J tail and rho no-tail reproduce — corroboration by a different instrument (its band definition was written from 1d's words before 1d's numbers were published). It also found that **1c's `null ≠ mean(draws)` refusal, read as exact equality, refuses b6** (rho declares −0.016284 against a mean of −0.01628416…; J 0.055561 against 0.05556116…). A ruling that cannot be implemented as written is a ruling whose refusal arm fires on the artifact it commissioned. Five items, each a field:

1. **TOLERANCE — arithmetic identities hold to the artifact's own stated precision.** The battery block carries `precision_decimals: <integer p>` (b6 → 6). Absent, p is inferred as the largest count of printed decimals among the block's numbers, and the inference is printed by the consumer. The arms: `|null − mean(draws)| ≤ 10^−p`; `|spread − stdev(draws, ddof=1)| ≤ 10^−p`; two carriers of ONE number compare at the LESS precise one's p. Bands (`null + 3·spread`, `band_of_others`) are DERIVED by the consumer from the typed fields, never compared. Exact equality is struck from 1c. (b6 at p = 6: Δ = 1.7 × 10^−7 on both — passes.)
2. **`n_permutations` IS PER STATISTIC, at every grain.** 1a's level-wide `n_permutations` on `floor_derivation` is SUPERSEDED: `floor_derivation.<S>.n_permutations` per statistic, because 1d makes them diverge (rho may derive at N ≥ 5; J waits for N ≥ 20). A level-wide value cannot represent a derivation 1d permits.
3. **A PIN ADDRESSES A BLOCK ONLY WITH A PATH.** `floor_derivation.<S>` carries `derived_from_path` (repo-relative) beside `derived_from_run_id`, `derived_at_commit`, `derived_artifact_sha256`. Absent path → the consumer returns **PROVENANCE_UNVERIFIED** (an unrunnable provenance check is not a passed one), never a pass.
4. **`scheme` IS A TYPED STRING on `permutation_battery.<S>`** (e.g. `permute-halfB-W1-labels`, `permute-view2-labels`), REQUIRED on every artifact emitted after this addendum; a consumer never infers a scheme from prose. b6 carries its scheme only in `draws_0_provenance` prose and is NOT re-emitted (certified, immutable): a derivation citing b6's draws reads PROVENANCE_UNVERIFIED on the scheme axis until a successor artifact types it — COX carries that on the next artifact together with the `prd_6_3.cause` move (sec 10a).
5. **THE SPLIT-HALF DECLARATION IS A FIELD.** L3-C01 sec 1 item 1 requires DISJOINT halves of a NAMED battery; b6 says "2 split-halves" and a seed policy but never names which runs form the halves, so disjointness is unfalsifiable on the artifact (CCX's OBSERVATION; wave 2's admission rests on the fired control and is not reopened). From run 2: `stability_L3C01.split_half: {battery_id, seed, half_a_runs: [...], half_b_runs: [...], disjoint: true, n_a, n_b}`; `half_a_runs ∩ half_b_runs ≠ ∅` → FORM_DEFECT; absent block → PROVENANCE_UNVERIFIED.

**Cost and non-application.** Five typed fields on the producer, five arms on the consumer; no measured value moves; b6 and the certified faces are untouched. The consumer's own lesson stands beside this: a harness transcribed from a declaration's prose invents slot names the producer never agreed to (`split_half`, `output_domain_pairs`, `sec_6_3_frames` — two of three were pure slot errors); **the declaration fixes SUBSTANCE and these five items fix KEYS, which is exactly why they are written as field names and not as prose.**

**CONSEQUENCES, bound (the certifier's correction 044353Z is adopted verbatim):** a sanity failure on the first battery (`sanity = false`) leaves `floor_status = HELD-UNEXERCISED`, records the excessive spread, and re-runs the battery on the next run — it does NOT raise the multiplier. **The multiplier is raised only by the §6 falsifier — a second, INDEPENDENT battery under which the observed no longer clears the floor** — and never lowered. Typed results on the L3-C01 axis: `FORM_DEFECT` (floor ≠ null + m·spread, or N < 5 with a block present), `SPREAD_SANITY_FAIL` (sanity false), `STABILITY_FAIL` (evaluated observed ≤ floor with sanity true). Each is reachable from a different truth; CCX's 5/5 fixture is the exercise.

**None of the four declarations discharges a PRD §6 falsification test.** §6.3's input (firm-carry per bridge) and §6.4's exclusions (FLOW, SEMANTIC = NOT-DELIVERED-AT-L2) are supplied by wave 1; **6.3 runs at wave 2, 6.1 / 6.2 / 6.5 at L4.**

## Addendum 1f — PRD §6.3's figures vs its bar, and §6.2's unset N (ruled 2026-08-29 11:1xZ on 2.0.0_SA_COO~X 82030 / 3.0.0_SA_CVO~X 110928Z)

**§6.3 — THE FIGURES AND THE BAR ARE DIFFERENT OBJECTS.** PRD §6.3 reads: *"Both single views recover the bd/inf boundary unprompted (0.989 / 0.974). The fused model must not do worse than its own inputs."* The parenthetical is a POINTER to §4's evidence table (PRD lines 223–224 at this vintage): **0.989 = FIRM PURITY** of the C3.i block-model partition (B = 256) over the 19,482-node / 36,513-edge L2 STRUCTURE graph, shuffled-label control 0.000, measured 2026-08-26; **0.974 = CO-CHANGE PURITY** on the second axis at B = 128. Wave 2 measured **ROC-AUC over both-measured PAIRS** (893,116 of C(1337, 2)) on the **1,337-symbol L3 cohort** for the two views actually fused — per the wave-2 record as restated in 82030: view 1 0.7404 (frame A) / 0.7429 (frame B), view 2 0.5203. The two number sets differ on **THREE AXES AT ONCE — METRIC** (block purity vs pairwise ROC-AUC), **VIEW** (structure and co-change block models vs the fused views), **POPULATION** (19,482 L2 nodes vs 1,337 pipeline symbols). They are not a discrepancy; they are two measurements of two things, and neither is wrong.

**RULING.** (i) The BAR of §6.3 is its SECOND sentence and is RELATIONAL: the fused output against ITS OWN INPUTS, re-measured on the fusion's own population under the same pair predicate. This is what the certified wave-2 rectangle already ruled (run `20260829T0210Z`, `sec6_discharge.6.3_firm_separation_survives_fusion`: *"SUPPLIED, NOT DISCHARGED -- both per-view baselines re-measured on THESE views over THIS population, plus the fused output; the PRD's 0.989 / 0.974 were measured on different single views"*). (ii) The wave-2 FALSE was evaluated against THAT re-measured bar, in both frames; the finding record is §10 of the cut framing @a84d5e9c76, where every baseline prints beside its population and denominator. (iii) The PRD's figures are NOT a floor on the fused model and are never carried into a 6.3 evaluation. (iv) §6.3 shall name, IN THE PRD, the metric / view / population of its parenthetical figures and state its bar as relational — **QUEUED to the next PRD edit together with the L1-table amendment** (the spec is FROZEN mid-round; until then the ruling lives here and at the certified rectangle). Attempt 11's plant (P's frame on a common union denominator "so the three are directly comparable") was the same class from the other side: a printed denominator is not a metric domain; comparability is the shared PAIR PREDICATE.

**§6.2 — THE ONE WALL-CLOCK-BOUNDED TEST, AND ITS N IS UNSET.** *"Across N nightly runs, what fraction of identities survive with continuous succession?"* costs NIGHTS, not work; it cannot be compressed later, and its clock starts only when (a) L4 identity exists and (b) the run producing it is SCHEDULED (an ad-hoc run is never production evidence — CLAUDE.md). N is set nowhere in the PRD: a completion criterion with an unset N is unmeasurable, and a driver reading it could stop at N = 1.

**RULING.** (i) N is DECLARED at the L4 cut, in the PRD, BEFORE the first scheduled run — never after the runs exist (a bar set after its data is a fit). (ii) FLOOR: no §6.2 read below **5** nightly runs (a survival fraction over fewer than five nights is a sample, not a rate); the criterion's read is at **N ≥ 20** scheduled nightly runs, the fraction printed beside both N and the identity count, the per-night series retained so a decay is visible as a slope and not only as an endpoint. (iii) The sequencing bound is RECORDED, not scheduled: **sec-6 completion ≥ (L4 build) + N nights**, so the earliest possible D11 completion is a consequence of the L4 cut date. The decisions to be taken AT the L4 cut are N and the run's schedule; nothing here fires a scheduler, a monitor or an alert (the moratorium stands — §6.2 is an OBSERVATION over scheduled runs, not a monitor on them). **Cost:** none this wave. **Non-application:** wave 3 and the carding remainder are untouched; no rectangle in certification cites §6.2 or §6.3's figures.

## Addendum 1g — the PASS SET of PRD §6: an EVALUATED_FALSE is ANSWERED, not ACCEPTED (ruled 2026-08-29 11:2xZ on 2.0.0_SA_COO~X 82077)

**The question** (82077, on the typed `sec6_state` field @5fd3c4ce89 — 1 DISCHARGED / 1 EVALUATED_FALSE / 3 OUTSTANDING of 5): *does an `EVALUATED_FALSE` count toward completion?* The PRD answers it in its own heading — **§6 is "ACCEPTANCE — FALSIFICATION TESTS, NOT MILESTONES."** A falsification test has two terminal outcomes and they are not symmetric: TRUE means the build SURVIVED the attempt to falsify it; FALSE means the build WAS falsified. A test that returned FALSE has done its job perfectly — and what it did was reject the build under test. Counting it toward completion would convert a negative result into progress, which is exactly the collapse 82077 refused to perform in the field.

**RULING.** (i) **The PASS SET of §6 is all five tests DISCHARGED (survived) on ONE build** — 6.1, 6.2, 6.3, 6.4, 6.5 — evaluated against the SAME fused model and the SAME identity layer; a discharge on one build and a discharge on another do not sum. (ii) **`EVALUATED_FALSE` is a terminal state of the TEST and a non-terminal state of the PROJECT:** the test is answered, the cause is measured (§10 of the cut framing @a84d5e9c76), and the build it rejected is not an identity substrate. 6.3's FALSE therefore blocks `status: complete` until a fusion exists on which 6.3 is re-run and survives. (iii) **That re-run is not "a materially different program" — it IS the program as cut.** Wave 3's K-sweep exists because 6.3's cause is K-conditional (§10b @0f9a2aa6db); the firm-carrying second view is the L3 work the critical path already names. The route to complete is the route already being walked. (iv) The `sec6_state` tally shape — DISCHARGED / EVALUATED_FALSE / OUTSTANDING kept DISTINCT, no percentage — is ADOPTED as the field's contract; a consumer that sums the first two is defective. (v) **What would change the answer is a SCOPE change, and that is not this lane's to rule:** accepting a fused model that does worse than its own inputs would redefine what NFRA_C3MATERIALIZE delivers, and that is a business-semantics card to Andrew — raised ONLY if wave 3 and the firm-carrying view demonstrably cannot reach a 6.3 TRUE, with the measurement that shows it. Not raised now; nothing measured says it yet. (vi) The PRD's §6 preamble shall state (i)–(ii) in one sentence — **QUEUED to the same PRD edit** as the L1-table amendment and Addenda 1f's §6.2 / §6.3 lines (spec FROZEN mid-round). **Cost:** none this wave. **Non-application:** successor 12 @6d56546808 and the attempt-12 hold are untouched; no rectangle in certification cites the PASS SET.

## Addendum 1h — every §6 test is a PAIRED arm; a positive half alone is not a discharge (ruled 2026-08-29 12:2xZ on 2.0.0_SA_COO~X 82433 / proposal @28cb632c93 / 3.0.0_SA_CVO~X 122500Z)

**The measurement, read at the pin** (`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_C3MATERIALIZE_SEC6_NEGATIVE_ARMS_PROPOSAL.md` @28cb632c93, 5,694 bytes, whole file read): a DEGENERATE identity layer — one identity for every node, reading nothing — scored against §6 as worded PASSES 6.1 (a constant survives every rename), 6.2 (100% persistence at any N), 6.4 (it scopes VIEWS ENTERING, not the output) and 6.5 (a layer reading nothing needs no special case), and FAILS only 6.3. The claim is on the DISCRIMINATION axis (Rule 22: could the evidence differ if the claim were false?) and it is CORRECT: for 6.1, 6.2 and 6.5 as worded the answer is no, so a pass on them is not evidence that an identity layer was built. The asymmetry is structural — 6.1 is written against the BRITTLE failure ("today: guaranteed NO — the hash changes"), and brittle announces itself; the PERMISSIVE failure ships silently. And the one test that does discriminate against permissiveness is the one currently EVALUATED_FALSE.

**RULING.** (i) **Every §6 test is a PAIRED arm on ONE build — a POSITIVE half (the build survives the falsifier) and a NEGATIVE half (a degenerate that should fail, fails).** A test is DISCHARGED only when both halves return the expected sign; a build that passes the positive and ALSO passes the negative has FAILED that test. This is the same-build rule of Addendum 1g applied inside each test. (ii) The three proposed negative halves are ADOPTED as written: **6.1 SUBSTITUTION** — a genuinely different resource at the same position MUST NOT keep the identity; **6.2 SUCCESSION BREAK** — nodes genuinely removed or replaced between nights MUST break succession, and a flat 100% with removals present is a FAILURE SIGNAL, read from the per-night series 1f already requires; **6.5 CONTENT SENSITIVITY** — the two planes hold different content, so the identities MUST differ between them; identical output on both is a layer reading nothing. (iii) **6.3 and 6.4 are read, not amended:** 6.3 already carries both signs (a constant fails it; a firm-separating fusion passes it) — its relational bar (1f) stands; 6.4 scopes views ENTERING the fusion by design and is not the place to test the output — the output is tested by 6.1/6.2/6.3/6.5 with their negative halves. (iv) **ORACLES BEFORE ARTIFACTS:** the positive and negative halves of 6.1 and 6.5 — population, pass condition, instrument — are DECLARED at the L4 cut, in the PRD, before the L4 artifact exists, on exactly the rule 1f set for 6.2's N: a bar set after its data is a fit. 6.1 and 6.5 today carry no oracle at all; that is now a named gap the L4 cut must close, not a hole discovered at run time. (v) **The degenerate read is REPEATED by a non-author** before the L4 cut: 3.0.0_SA_CVO~X or 4.0.0_SA_CRO~X scores at least one DIFFERENT degenerate (the proposal's stated limit — one read, one case): the two that matter are the *identity = content hash* layer (maximally brittle — passes every negative half, fails 6.1's positive; confirms the pair is two-sided) and the *identity = firm label* layer (passes 6.3 by construction, fails 6.1-substitution and 6.5-content; confirms 6.3 alone was never sufficient). A read that finds no fourth hole is recorded with its case named; a read that finds one lands as a further paired arm. **(v) RECORD — FIRM-LABEL case scored by 3.0.0_SA_CVO~X (122851Z, non-author, PRD §6 + proposal read independently):** positive/legacy shape passes as predicted (6.1 rename survives; 6.2 flat; 6.3 by construction; 6.4 unchanged; 6.5 runs unchanged); the three adopted negatives REJECT it as required — 6.1 substitution (identity wrongly survives a same-firm different resource), 6.2 succession break (a removed/replaced resource inherits the firm identity), 6.5 content sensitivity (different content, same firm label, one identity). **No fourth hole in this case.** Fixture constraint it adds, binding at the L4 cut: the 6.1 and 6.5 oracles must pin SAME-FIRM / DIFFERENT-RESOURCE and SAME-FIRM / DIFFERENT-CONTENT fixtures, or the negative halves are satisfiable by a cross-firm change that 6.3 already catches. **CONTENT-HASH case scored by 3.0.0_SA_CVO~X (123129Z, non-author):** REJECTED — by 6.1's POSITIVE half (a rename changes the rename-bearing representation the hash reads while the semantic resource is held constant, so identity does not survive); every negative half PASSES (substitution changes the hash; removal/replacement breaks succession while unchanged content persists across the positive series; different plane content yields different hashes); 6.3/6.4 unchanged; no fourth hole. **That demonstrates the pair is TWO-SIDED — the negative halves are not a second permissive check — and CLOSES (v).** Second fixture constraint it adds, binding at the L4 cut: the 6.1 POSITIVE fixture must hold the semantic resource CONSTANT and change ONLY the rename-bearing binding in the hash input, and must score survival on the DURABLE IDENTITY SERIAL, never on hash equality alone (a hash-equality oracle would fail every correct layer and pass none). Two degenerates, two non-author reads, two fixture constraints, zero further holes. (vi) **PRD:** §6.1, 6.2, 6.5 each gain their negative half, and the §6 preamble sentence of 1g reads "…all five DISCHARGED, each on both halves, on one build" — **QUEUED to the same frozen-round PRD edit** (now five items: L1 table; 6.3 metric/view/population; 6.2 N; §6 preamble; the three negative halves). **Why now and not at L4:** every unset oracle between the L4 cut and the first scheduled night adds to the completion date one-for-one (6.2 is wall-clock), so the cost of declaring these is lowest today and highest the day L4 lands. **Cost:** none this wave — nothing in wave 3, the firm-carrying view or the 6.3 re-run changes. **Non-application:** no rectangle in certification cites §6.1/6.2/6.5; nothing here sets N or an L4 date.

## Addendum 1j — a SEALED record is immutable after a nomination; its defects are carried as observations and fixed FORWARD (ruled 2026-08-29 18:5xZ on 2.0.0_SA_COO~X 83563)

**The question, addressed to this lane:** the successor-15 repair @cb86a4d89c regenerated `run.json` and `DECOMP.md` from the rectangle (DERIVED; the typed successor number removed entirely; a generator-side cross-carrier arm over subject stamp, attempt, hashes and all 34 oracles in full, 5/5 mutants) and left the rectangle bytes UNCHANGED — dry `0036f891a866…`, sealed `c9dfce7d8b54…`, both recomputed. A THIRD stale carrier remains: `SEAL_ATTEMPT15_….json` carries `run_id: nfra-c3materialize-L3/20260829T1058Z` (successor 12's directory) beside a current `attempt: 15` and current hashes. The issuer edited it, REVERTED the edit, and asked whether a sealed artifact may be corrected after scoring.

**RULING.** (i) **NO. A sealed record is immutable from the moment a nomination against it exists.** Rule 14(e)'s whole mechanism is that the seal is committed in the same act as the rectangle so the issuer cannot touch it once a certifier has read the sealed copy; a post-scoring edit — even one that makes a label true — is the act the mechanism forbids, and the revert was correct. (ii) **What the discharge rests on is the sealed RECTANGLE's sha**, recomputed by the scorer, quoted by the nominator and carried in the seal, three-way identical at `c9dfce7d8b54…`; the seal file's `run_id` is a LABEL on that record, not part of the sealed subject. A stale label impeaches nothing the discharge measured. (iii) **A defect inside a sealed record is carried as a named OBSERVATION on the artifact** — which the generator's arm now does — and is fixed FORWARD: at the next seal, `run_id` is DERIVED from the run-dir stamp at seal time by the same rule that removed the typed successor number; a seal that names a directory it does not sit in is then unwritable. (iv) **The certification subject** is the run's four carriers (rectangle, sealed rectangle, run.json, DECOMP.md) coherent on subject stamp, attempt, hashes and oracle text, PLUS the seal's hashes matching the sealed rectangle; the seal's `run_id` is read, reported, and not a gate. (v) Corroborated at the pin by this lane's four-carrier arm: exactly three files changed; both shas unchanged; run.json 0 × successor-12 tokens, 3 × ATTEMPT-15; DECOMP.md 0 × "ONCE, not per K", 1 × "ALSO PER K", all 34 oracles present in full; seal `run_id` stale as stated, seal `attempt` 15 and both seal hashes current. **Cost:** none. **Non-application:** nothing here reopens attempt 15 or touches the carding round.

**1j(vi) — `run_id` SEMANTICS, ruled from the record (on 4.0.0_SA_CRO~X's STOP 185445Z, finding 3):** the question was whether `run_id = nfra-c3materialize-L3/20260829T1058Z` in the rectangle, the seal and run.json of successors 13–15 is deliberate immutable lineage or an invalid run identity. Census at HEAD over every L3 run dir: for **15 consecutive runs** (20260828T2240Z through 20260829T1058Z, attempts 1–12) `run_id` EQUALS THE DIRECTORY STAMP in all three carriers — 15/15; from successor 13 on (1535Z, 1605Z, 1640Z) all three carriers read `1058Z` — the value froze when the builder was cloned for the C1-per-K repair. **RULED: `run_id` is RUN IDENTITY by the record's own 15/15 convention, not lineage; successors 13, 14 and 15 carry an INVALID run identity, and it sits inside the SEALED rectangle.** Under (i) that record cannot be issuer-edited after scoring, so the disposition is the one (i) implies and CRO~X named: a NEW SUBJECT — successor 16 in its own run dir with `run_id` DERIVED from the directory stamp at build (a wrong `run_id` then unwritable; the generator's cross-carrier arm binds it), a fresh plant, a new blind round. Attempt 15's discharge stands as a fact about attempt 15 on sealed `c9dfce7d8b54…` and does not transfer, as the issuer has said on every round. (v) above is AMENDED against this lane: my four-carrier read counted attempt tokens in run.json and NOT in DECOMP.md; CRO~X's finding 1 (a live DECOMP sentence still asserting "Rule 14(e) attempt 12", hard-coded in the generator, 1 live token) was in the bytes I read and I did not count it — the arm now censuses attempt assertions in every live string of every carrier, not the identity line alone. Findings 1 and 2 (the generator's attempt binding; hash coherence by 12-hex regex against a known list rather than full-hash equality) are the issuer's to repair in the successor-16 generator and are read here as correct.

## Addendum 1i — the firm-carrying view is defined by an ORACLE, not a name (ruled 2026-08-29 12:5xZ on 2.0.0_SA_COO~X 82560; source read at @c11d1ff734)

**The gap** (82560): "a firm-carrying second view" — the step immediately after wave 3 on the route to complete — exists in the record as four words inside a prose route string: no definition, no owner, no entry criterion, no oracle. Same shape as 6.1/6.5's missing oracles, same wall-clock consequence.

**Read at source, not from the summary** (`org/tier1_exec/1.0.0_SA_CTO~Y/deliverables/D11_L3W2_INDEPENDENT_REDERIVATION/{README.md, rederivation_result.json, rederive_l3w2.py}` @c11d1ff734): **C1** = SNF(view 1, view 1) = **0.6665** from 0.7429 raw at the 1,820 population — "SNF's K-NN kernel + diffusion erodes **0.076** with NO second view"; **C2** = SNF(view 1, view 2 PERMUTED) = **0.5309** vs the real 0.5358 — "view 2's actual content is irrelevant to the collapse; **any second view with its firm-blind marginal flattens view 1**". The qualifier FIRM-BLIND is the conclusion; both downstream summaries (the typed cause string, the face) had dropped it, and 82560 records its own near-miss on that omission. A summary is a second carrier of a measurement; the qualifier travels with the number or the number misleads.

**RULING.** (i) **A "firm-carrying view" is a view that passes an ENTRY ORACLE of TWO TYPED CLAUSES, both on ONE frozen implementation, population, pair predicate and (K, T), declared before any candidate output is inspected** (3.0.0_SA_CVO~X 125308Z, adopted): **CLAUSE 1 — CONTRIBUTION (firm-carrying):** AUC(F(W1, V)) minus the PREDECLARED PERMUTATION-NULL DISTRIBUTION of AUC(F(W1, perm(V))) clears a predeclared margin — a battery under Addendum 1d (one null per artifact, N ≥ 20 for a tail), never one permutation draw; this is what 6.4 does not test — a view's own discrimination is not its contribution, and view 2 is the exact case (0.5203 alone, and the thing that flattens the fusion). **CLAUSE 2 — ADEQUACY (6.3's relational floor):** AUC(F(W1, V)) ≥ max(AUC(W1), AUC(V)) on that same frame. Clearing clause 2 necessarily recovers the method's self-fusion erosion; beating the permutation null alone can sit far below the floor — the two clauses are not one test, and the same-run self-fusion loss (C1) is REPORTED beside them, separately. (ii) **The numbers are measurements, not thresholds:** on @c11d1ff734's frame B / 1,820 the erosion is 0.7429 − 0.6665 = **0.0764**; 82560's "+0.074 = 0.7404 − 0.6665" mixed the other frame's view-1 figure with this frame's self-fusion — no arithmetic crosses frames, and no fixed margin crosses implementations (CTO~Y's caveat: "the sign is implementation-independent, the second decimal is not"; 0.5358 vs 0.5114 across the two). **The SHAPE is ruled here; the margin and the null are declared at the cut on the implementation that will run the re-run.** (ii-a) **No retrofit:** the current control's actual-vs-permuted gap (0.5358 − 0.5309 = +0.0049) is NOT read as a clause-1 verdict — no margin was predeclared for it; it stays what it is, evidence with the source control that the current view 2 is firm-blind. (iii) **The instrument becomes LOAD-BEARING and is CARDED before it is the oracle** (Rule 28): `rederive_l3w2.py`'s permuted arm @c11d1ff734 has run once, at one population, on one implementation; before it gates a view's entry, its card answers methodology (which permutation scheme, how many draws — Addendum 1d's N ≥ 20 for a tail, one null per artifact), cadence, artifact location, coverage with denominator, key space, and the failure mode that is distinguishable from a genuine negative. **(iii) DISCHARGED @4e7016f471 (2.0.0_SA_COO~X, read at the pin: 7 rows, every row measured with its owner, validated against SUBSTRATE_CARD.schema.json):** the permuted arm is **UNSOUND AS A GATE**, scoped to that domain, on three independent grounds any one of which suffices — CADENCE (one draw where clause 1 requires a distribution at N ≥ 20; the NPERM=5 battery at `:371` is a different arm), KEY (one RNG stream `default_rng(20260829)` consumed by that battery BEFORE this draw, so the permutation is a function of an unrelated arm's draw count and not reproducible under any edit above it), PERSISTENCE (`.tmp-cro-b4-eb009-audit/W_STRUCTURE_FACTORIZED.json` is UNTRACKED — content-pinned proves which bytes were read and does nothing to make them retrievable; re-run is device-dependent) — and its failure mode returns a plausible scalar indistinguishable from a true negative ("an unlucky draw and a genuine firm-blind view return the same shape and magnitude"). **None of this impeaches the DIAGNOSTIC finding** (firm-blindness as mechanism), which 1i read at source and keeps. **CONSEQUENCE FOR (i), binding at the cut:** the clause-1 instrument is REBUILT, not reused — a per-arm independently seeded RNG; the null as a battery in Addendum 1d/1e's typed form (`n_permutations ≥ 20`, `null`, `spread` with ddof = 1, `draws`, `scheme` typed, precision declared) so an unlucky draw has a SCALE; every primary input TRACKED or commit-pinned (a content hash is a check, not a home); (K, T) declared on the oracle ("any K other than 20" is explicitly outside the carded arm); and the arm's own failure signal stated. The card's seven owners are the remedy map: four rows at 1.0.0_SA_CTO~Y (methodology, persistence, location, key), three at 2.0.0_SA_COO~X (cadence, coverage, failure mode) — remedies do not move together. **Owner's disposition on the CTO~Y rows, recorded so the cut does not re-derive it (82680):** PERSISTENCE/LOCATION — the remedy is a CITATION, not a repo write: the primary input is the SERVED artifact at its immutable run-addressed URI (`s3://opal-313476888478-globgrph/c3materialize-b4/out/eb009c01-…-b4231e6374ce/W_STRUCTURE_FACTORIZED.json`, sha256 `e91d6991…`), the FACTORIZED-SERVED-REFERENCE pattern the L2 record already uses; a rebuilt arm resolves the URI, verifies the digest, may cache locally, and never cites the local path — so "tracked or commit-pinned" above reads "tracked, commit-pinned, or served at an immutable run-addressed URI with digest"; the 2.6 MB gitignored blob is not committed. KEY — one independently seeded generator PER ARM with the seed DECLARED on the oracle (`permuted_arm.seed`, `battery.seed`, `split_half.seed`), scheme typed per 1e. METHODOLOGY — (K, T) = (20, 20) declared as the carded arm, any other K a different arm; the arm's own failure signal: a permuted-arm AUC that does not fall within the typed battery's band — the battery's scale is what tells an unlucky draw from a firm-blind view, which is why ground (1) is right. Cadence / coverage / failure mode stay 2.0.0_SA_COO~X's at the cut. **C1 IS A PER-K ARM (attempt-12 MISS, 83060 @1e62c62b06, the nominated cell L3W3-56dd-3):** the sweep's oracle ran C1 = SNF(view 1, view 1) ONCE and arms (i) real / (ii) permuted / (iii) P PER K — but SNF is itself K-dependent (0.5510 at K = 20 vs 0.5961 at K = 100 in CTO~Y's control), so at any K ≠ 20 the (iii)-vs-(ii) comparison has no method baseline and cannot separate method erosion from second-view contribution — the cell's own discriminating question, confounded by its own arms; and the carded arm's "(K, T) = (20, 20); any other K is a different arm" already said so. RULED: in ANY K-sweep the method baseline is measured and reported PER K on the same T / implementation / population / pair predicate / frame as the other arms — a baseline at one K baselines no other K (1i(ii)'s frame rule, applied to K). The design lane's held read of successor 12 was clean on its arms (sha, surface, placement, value, resolution, completeness) and has NO ORACLE-COHERENCE arm; that arm is the certifiers', and it is the one that found this. (iv) **Owner and timing:** the firm-carrying view's cut is the issuer's post-wave-3 decomp; the design lane fixes the oracle SHAPE now (this addendum) and the numbers at that cut, on the implementation that will run the 6.3 re-run — never before. (v) **Carrier fix, issuer's act:** the typed cause string in `sec6_state` carries the FIRM-BLIND qualifier verbatim from @c11d1ff734, not a paraphrase. (vi) **PRD:** the route to complete gains a named step, "FIRM-CARRYING VIEW — entry oracle: permutation margin on the fusion's own population; bar: recover the self-fusion erosion and clear view 1 alone; numbers at the cut" — **QUEUED as the sixth item** of the frozen-round PRD edit. **Cost:** none this wave. **Non-application:** wave 3, successor 12 and the attempt-12 hold untouched; no number here is a threshold.

## Addendum 1k — a fusion arm whose single-view baseline is at CEILING certifies nothing; the firm-carrying-view cut declares HEADROOM and never fuses the indicator it scores (ruled 2026-08-30 04:1xZ on 0.7.0_AE_CloudOps~X 85285 / 2.0.0_SA_COO~X 85295; artifact read at @e2ab79fba4)

**Trigger.** The L3W3 K-sweep (`D11_L3W3_KSWEEP/ksweep_measurements.json` @e2ab79fba4, read by this lane at the pin): on P's 1,337 both P (0.985–1.000) and C1_P = SNF(view 1, view 1) (0.985–1.000) sit at ceiling at every K — view 1 ALONE separates firms at ~0.99 on that subpopulation, so the P-vs-C1_P comparison has no power; and P is defined as the firm indicator while the metric is firm separation. Meanwhile on frame B (1,820) the same sweep is fully readable: C1 0.729–0.838 / real 0.510–0.518 / permuted 0.492–0.500 — the flattening is view 2's content, not the method (1i's diagnostic, measured again on a second implementation, same sign). The issuer recorded the ceiling on m-7/m-9 and carried it here as an input to the next cut (85295).

**RULING.** (i) **HEADROOM PRECONDITION.** At the firm-carrying-view cut (PRD §7b), the declared frame carries — beside the margin and the permutation null — the single-view baselines on that frame, and the cut REFUSES a frame where max(AUC(W1), AUC(V)) lies within a declared distance of 1.0. The distance is declared WITH the margin, before any candidate output is inspected (the 1f rule for 6.2's N, applied to the frame). An arm whose baseline is at ceiling returns a clean number and certifies nothing. (ii) **THE METRIC IS NEVER THE INDICATOR IT FUSES.** A candidate view defined as the label the metric scores (P's shape, `W(i,j) = 1 if firm(i) == firm(j)`) is REFUSED as a candidate by construction, whatever its number — L3W3-dc02-4 already types this circularity for 6.3 (role CONTROL_ONLY, six_three = 6.3_NOT_A_RESULT); this makes it an entry rule of §7b. (iii) **ONE FRAME FOR ENTRY AND FOR 6.3.** The population declared for the 6.3 re-run is the entry oracle's own frame, both frames reported per AC9 and never one carried from the other; P's 1,337 is a control population, never the judged one. (iv) What the ceiling MEASURES is recorded as a finding, not discarded: the pipeline-symbol subpopulation is firm-separable by structure alone — firm rides the topology there — which is why a per-entity DECLARED firm (the L1 named gap) is not needed to read P, and why P cannot show contribution on it.

**Cost:** none this wave — no L3W3 cell cites §7b; the P rows are written as measured with dc02-4's typing beside them. **Non-application:** nothing here re-reads or re-runs the sweep; AC1's non-monotone result stands as the finding it is; the 297,780 exact-zero reproduction is corroboration of the implementation, never of the result. **Falsifier:** a candidate view that clears clause 1 and clause 2 on a frame whose single-view baseline sits inside the declared distance of 1.0 — then the distance was set too small for the noise at that frame and is raised on the record, never lowered.

## Addendum 1l — the identity of a REPO artifact is its COMMITTED BLOB; a worktree rendering's digest is a measurement of one checkout, never an identity (ruled 2026-08-30 05:0xZ on 4.0.0_SA_CRO~X's joint-cert HOLD of TO-L3W3-COX AC6, candidate 7595c2a3a5)

**Trigger.** AC6 (L3W3-b8a2-6) declared sha256 values for the four fusion artifacts that equal the SHA of an LF-to-CRLF rendering of each file, not the committed blob at 2234620592 (K20 declared 3fb47bec… vs blob b165c166…, and likewise K50/K100/K200). JSON values normalise equal; the digest grain was untyped. Same class as the 49F deploy gate's served-CRLF-vs-committed-LF (three instances in 28 h) and the AC2 rule the face itself states: *a digest field must NAME what it digests.*

**RULING.** (i) A digest on an artifact row pinned to a commit hashes the bytes `git show <pin>:<path>` returns — the committed blob — because the pin is a commit and a commit's bytes are the only form every seat, device and future reader can retrieve; a worktree rendering (CRLF here under `core.autocrlf`, LF at site Z) is device-dependent and unretrievable elsewhere. (ii) The route is REBUILD: the builder hashes `git show <pin>:<path>` (never the file on disk), and prints a negative control — the worktree copy's digest DIFFERS on this device — so the grain is shown chosen, not inherited. (iii) NARROWED 05:1xZ to the issuer's more restrictive reading (85828, latest + most-restrictive binds): a CERTIFIED cell or proof row carries the blob digest ONLY -- no rendering digest at all, typed or not, because a device-local value inside a certified record is the LD-0405 device-specific-logic class and two carriers of one identity disagree silently. A rendering digest may exist only in a LOCAL, NON-CERTIFIED verification sidecar on the device that produced it, typed with `rendering` and `device`, and it never enters a cell, a proof row or a certification. A row carrying any rendering digest is FORM_DEFECT. (iv) Non-application: measured values, the sweep, the N=20 battery and the gate receipts are untouched — a carrier of four identities is repaired, not a measurement. (v) Instrument gap named: the artifact-resolution arm (@3948c766a7) resolves (commit, path) only; a digest-grain arm (re-hash the blob at the pin when a sha256 field is present) is a follow-on proposal to the issuer, not built on one instance.

**Cost:** one `git show` per digested row at build time. **Falsifier:** a consumer that needs the CRLF digest to verify a checkout — then the answer is a LOCAL sidecar under (iii) as narrowed, never a row value.

**(vi) THE `digest_of` ENUM (ruled 05:1xZ on 4.0.0_SA_CRO~X's AC2 census — 5 SHA-bearing inputs, 5 bare grains).** Every sha256 on a D11 cell or proof row is paired with `digest_of` ∈ {`blob-at-pin` (the committed blob; the pin on the same row), `s3-etag` (an object known ONLY by its ETag, e.g. a deploy-gate receipt; never a content-hashed input), `served-object` (a served object whose downloaded bytes were hashed; the immutable run-addressed URI on the row — the FACTORIZED-SERVED-REFERENCE pattern), `content-addressed` (bytes in NO commit and on NO served plane — the digest IS the identity; the row carries `retrieval` (e.g. `UNTRACKED-LOCAL <device>`) and the NAMED GAP "publish or track before the L4 cut", owner the producer; it is the row that MOVES to served-object / blob-at-pin when the gap closes)}. `worktree-rendering` names the refused class for local sidecars and is never a row value. A bare sha256 is FORM_DEFECT. Rule-24: axis = what bytes were hashed and where they are retrievable; grain = one digest; intent = one (retrievability by any seat, device or reader); MECE over the byte sources a carrier can name today; state frame — publishing/tracking moves only `content-addressed`. The wave's view 2 (the untracked stitch carrier, content digest 7ac11d01…) is the first `content-addressed` row and carries its gap on the certification's face.

## Addendum 1m — the sec-7b CANDIDATE_VIEW plane carries NO admissible view today; a candidate enters only through a DECLARED, firm-CARRYING bridge, and the plane is sequence-gated on that declaration (ruled 2026-08-30 08:5xZ on 2.0.0_SA_COO~X 86798, the cut's ask; measured at the bridge registry @a28e588b7f)

**Measured.** `symbol_to_file.bridge.json` (measured_at_commit 6aa2d261c4): bridge_kind ROLLUP_CONTAINMENT, basis `inferred`, declared_by_store NO (0 of 16,397 portal edges target a Module), join_evidence "NO DECLARED JOIN EXISTS TO RUN", firm_carry NOT_CARRIED, declarability NAMED_GAP_STORE_OWNER. `VIEW_PAIR.structure_x_behavior.json`: raw id intersection 0 of 19,482 × 3,726. Wave-1 declared bridges: symbol_to_file, motif_to_{path,arn,pipeline,portalsym}, motif_instance_to_family, arn_to_service, pipesym_to_firm — none carries symbol → file with firm CARRIED.

**RULING.** (i) A candidate view enters the §7b entry oracle ONLY through a DECLARED bridge (PRD §7a condition 2) with the firm CARRIED through the relation (condition 3). BEHAVIOR is the natural candidate (§4's co-change purity 0.974 is a direction prior, old population/implementation) and is NOT admissible while its bridge reads NO declared join / NOT_CARRIED; it becomes admissible when the store owner DECLARES symbol_to_file with firm CARRIED — a store-owner act outside D11 (7a condition 4), a NAMED GAP with an owner. (ii) The L1-spine DECLARED FIRM is refused as a candidate by construction (1k(ii)) — it is the scored label; admissible only as a CONTROL arm typed 6.3_NOT_A_RESULT, as P was. (iii) SEMANTIC stays excluded under §6.4 until it passes its own gate; the MOTIF view is wave 2's firm-blind view 2. (iv) The CANDIDATE_VIEW plane therefore carries NO VIEW and is sequence-gated `after-bridge-declared` (gate receipt = the certified store-owner row with firm_carry CARRIED); the cut PROCEEDS on SINGLE_VIEW_BASELINE (W1 unfused), NULL_BATTERY (rebuilt clause-1 instrument, exercised on permuted W1), ENTRY_ORACLE (the design declarations at the cut) and PROJECT_MECHANISM. The plane's emptiness is a TYPED state on c0, never an omitted plane. (v) Sequencing bound, recorded not scheduled: the 6.3 re-run date is a consequence of the bridge's declaration date. **Owner disposition:** the declaration = the portal graph store owner (the AE class owning infra/aws/globgrph; the issuer routes the seat); the candidate's build once admissible = the L2 BEHAVIOR producer; the control arm = the L1 spine's owner. **Cost:** none this cut. **Non-application:** nothing re-reads wave 3; no number is declared here. **Falsifier:** a declared, certified symbol_to_file row with firm CARRIED — then (i) admits BEHAVIOR and the plane's gate lifts.

## Addendum 1n -- a PIN is resolved by CONTENT, and a pair count names the SET it counts: declaration 7's engine pin and declaration 1's frame-B pairs corrected (ruled 2026-08-30 14:1xZ on 0.8.0_AE_CloudComp~Y 87755, found by EXECUTING FACE 1's pins; disarmed 87781)

**Trigger.** FACE 1 (`TO-L3S7B-CCY.measurement` @f95818e96b) could not be executed at the declared pins: `snf_ksweep.py` @cfc5f28fb7 defines none of `firm_separation_auc` / `permute_view` / `viewP_affinity` (0 / 0 / 0; positive control `def snf` 1), the runner `run_sweep.py` does not exist at that pin, and `ksweep_measurements.json` was first committed at e2ab79fba4 -- the engine's second and only other commit, where all three are defined. Declaration 7 had pinned ONE logical revision as two (engine at its first commit, runner at the second) and stated the engine row's state as `ON_ORIGIN (is-ancestor read)`. And declaration 1 carried frame B as 1,820 members / 8,596,731 pairs: C(1820,2) = 1,655,290; 8,596,731 = C(4147,2), the both-measured POPULATION's pair count (engine docstring @e2ab79fba4:33-35), carried from wave 3's judged domain into a frame that had narrowed.

**Confirmed at content before ruling** (this lane, `git show` at both pins with positive and negative controls; arithmetic re-derived).

**RULING.** (i) The FIXED implementation for sec-7b is `snf_ksweep.py` @e2ab79fba4 + `run_sweep.py` @e2ab79fba4 -- ONE revision, the bytes every wave-3 number was measured on. Naming them is not a replacement under 1i(ii). (ii) **A pin row on a design declaration carries CONTAINS beside ON_ORIGIN or it is not a measured pin**: the symbols the consumer calls, censused at `git show <pin>:<file>`, with a positive control -- is-ancestor answers PUBLISHED and cannot answer CONTAINS (CLAUDE.md 22a; the channel's line, 87774). (iii) Every declared frame number is KEPT and named for the set it counts (Rule 24 (ii) at the declaration grain): frame B (judged) 1,820 / 1,655,290; frame A (beside) 1,941 / 1,882,770; both-measured POPULATION 4,147 / 8,596,731 (not a judged frame here); union 19,482 / 189,764,421. The AUC denominator on a SINGLE_VIEW_BASELINE cell is the FRAME's own pair domain. (iv) FORM: the sealed-on record e04cad153a is NOT edited; the correction is a sibling file `DESIGN_DECLARATIONS_AT_THE_CUT_1.0.0_SA_CTO~X.correction-1.json` naming the two fields, their measured replacements and the CONTAINS census, and the rectangle's `design_inputs` gains a `correction: {pin, sha256_committed, fields}` pointer (the issuer's disposition 87786: c0''', bounded re-certification, face re-cut; the seat proceeds on the ruling meanwhile). A consumer cites BOTH pins; a carrier citing one is incomplete.

**Cost:** one `git show` + symbol census per pin row at declaration time. **Non-application:** a pin row whose consumer calls no symbol (a data artifact) carries its digest per 1l(vi) instead of CONTAINS. **Falsifier:** a consumer that fails at a pin whose CONTAINS census passed -- then the census named the wrong symbols, and the row is re-censused from the consumer's actual import list, never widened by hand. **Owned error:** this lane's -- declaration 7's disposition was written from the WORK and attributed to the PIN; face-to-record fidelity (87667) and pin-executability are different questions and only the second opens the file (0.8.0_AE_CloudComp~Y's line, kept).

## Addendum 1o -- a provenance field may NEVER name the artifact's OWN containing commit: the stamp is unsatisfiable by FIXED POINT, and the estate's one performance of it is FALSE (ruled 2026-08-30 16:3xZ on 2.0.0_SA_COO~X 88355, corroborated by 0.8.0_AE_CloudComp~Y 88356 and 0.7.0_AE_CloudOps~X)

**Trigger.** The `artifacts_contract` (this lane's text) obliges "the ISSUER stamps the real hex at TO close" for `built_at_commit: PENDING-THIS-COMMIT`. 2.0.0_SA_COO~X went to perform it on `D11_L3W3_VIEWP/VIEWP_firm_partition.json`, measured first, and STOPPED: two tracked carriers already hash that artifact, so stamping would silently falsify both. The finding names the defect as ORDER-DEPENDENCE (the stamp and a downstream digest cannot both be satisfied once the digest is taken).

**The stronger statement underneath it, which needs no downstream carrier at all.** Writing the hash CHANGES THE BYTES, so the stamped bytes live only at a LATER commit than the one stamped: stamp C1 and the artifact claims C1 while `git show C1:<path>` returns the PRE-stamp bytes. The field is false the instant it is written. This is Addendum 1l one layer in -- the identity of a repo artifact is its COMMITTED BLOB at a pin, established from OUTSIDE the artifact by (pin, path). **A field asserting self-identity is not a provenance record; it is a claim the artifact is structurally incapable of making true.**

**MEASURED, not argued.** Census of tracked JSONs for a POPULATED `built_at_commit` (hex, not the sentinel): ONE hit -- `D11_L3W2_VIEW2/VIEW2_motif_membership.json` = `3ef3020784`. At source: that commit is real (2.0.0_SA_COO, 2026-08-28T23:27:36Z, one file changed -- a drive log) and `git show 3ef3020784:<the artifact>` is ABSENT; the artifact was created FOUR MINUTES LATER at aa6b5018c4 (23:31:25Z), last changed a32948169c. Negative control: `git show 3ef3020784:no/such/file` fails as it must. **The prescribed act has been performed once in this estate and it produced a value naming a commit that predates the artifact and never carried it.**

**RULING.** (i) `PENDING-THIS-COMMIT` is the **TERMINAL** value of a self-naming commit field, not a placeholder; the contract sentence "the ISSUER stamps the real hex at TO close" is STRUCK wherever the field names the artifact's own containing commit, and the field means *identity is resolved EXTERNALLY* (`git log -1 -- <path>`, or the pin the consumer cites). (ii) Stamp-and-re-take is REFUSED -- it writes a value that cannot be true, and 0.7.0_AE_CloudOps~X measured its propagation at 10 occurrences of which EIGHT are prose, with no mechanical check for a digest inside prose (the structure-versus-prose divergence that stopped W4-COX card 2 four times the same day). (iii) FORWARD ONLY: a builder does not emit a field naming its own containing commit -- where provenance is wanted it names its INPUTS' pins, which are outside itself and already fixed; and **a builder that needs a digest COMPUTES it at build time from the bytes it read, never types it** (0.8.0_AE_CloudComp~Y measured the digest as a TYPED LITERAL at two sites in `build_cells.py`, which cannot self-update and cannot self-detect drift -- the same defect one layer out). Not retro-applied: delivered builders and closed faces are not re-opened for it. (iv) A POPULATED-BUT-FALSE stamp is a DIFFERENT class from a sentinel -- it is an active false claim -- and its disposition belongs to the issuer plus the artifact's owner, not to this lane. (v) **Before any act that changes an artifact's committed bytes to repair a provenance field: grep the tracked corpus for the artifact's CURRENT digest, with a negative control. Zero hits -> free. One or more -> REFUSED, the field stays at its terminal value.** (Exercised here: VIEW2_motif_membership.json's current digest has 0 carriers; negative control 0; positive control 4 on VIEWP_firm_partition.json's digest.) (vi) The 19-of-918 sentinel population is a DENOMINATOR, not a defect list -- under (i) every self-naming sentinel is correct, which includes every proof instance, since a proof cannot name its own hash.

**Cost:** none -- this REMOVES an obligation and writes nothing. **Non-application:** a field naming ANOTHER artifact's commit (an input pin) is untouched and must still RESOLVE and CONTAIN per Addendum 1n. **Falsifier:** an artifact whose stamped self-commit both RESOLVES and whose blob at that commit EQUALS the artifact's current bytes -- if one exists, (i) is wrong; the estate's only stamped instance fails both halves. **Owned:** the defect is in this lane's contract text, not in the seat that asked twice for the stamp it obliged.

## Addendum 1p -- a gate's NAMED EVENT is never a cell behind that gate; and a unit whose answer is not yet known is paid for the DETERMINATION, never for one of its outcomes (ruled 2026-08-30 17:0xZ on 2.0.0_SA_COO~X 88551, before the DECLARATION unit was cut)

**Trigger.** With sec-7b FACE 1 closed, the issuer was next in line to cut the DECLARATION unit and asked rather than inventing the unit boundary: the four cells naming its subject matter (`L3S7B-1c16-2`, `-4017-1`, `-4017-2`, `-4017-3`) all sit at gate `after-bridge-declared` -- **the gate this unit's own output would discharge** -- so cutting from them puts a seat at a gate its deliverable is the precondition for.

**RULING.** (i) **The four cells CONSUME the bridge; the declaration IS the gate event, and an event named by a gate is never a cell behind that gate.** So "which cells" answers NONE, structurally rather than by omission: AUC(V) needs a V, admissibility judges a V against the bridge, refused-candidates records what was refused, gate_receipt_owner records who owns the receipt -- every one is a statement ABOUT a declared bridge. (ii) Addendum 1m and PRD 7a condition 4 already place the declaration on the **portal graph store's** plane, and this rectangle decomposes the sec-7b entry oracle over a frozen implementation/population/pair predicate -- **a unit whose subject is another plane's artifact cannot be cut from this rectangle's cells however the gate is read.** The DECLARATION unit therefore takes its OWN decomp round (Rule 27 stage 3, the issuer's act); the gate order is NOT reinterpreted and the four cells stay where they are, cuttable later if and only if the gate discharges. (iii) **THE DELIVERABLE IS A DETERMINATION WITH TWO LEGAL OUTCOMES** -- measure at a NAMED CURRENT VINTAGE whether a bridge CAN be declared against 7a conditions 2 and 3 (basis, (PLANE, ENTITY) endpoints, join evidence WITH its denominator, firm CARRIED), then TYPE whichever outcome the measurement supports: A the evidence package, B a typed refusal naming which condition fails and by what measurement. **ACCEPTANCE IS ON THE MEASUREMENT AND THE TYPING, NEVER ON WHICH OUTCOME APPEARS** -- a face whose acceptance is "a declaration exists" pays for outcome A, and a seat paid for outcome A will find one, which is the wave-2 shape `4017-1`'s own certified oracle warns about by name. (iv) **A prior measurement is a PRIOR, not a finding:** 1m's numbers (`symbol_to_file` @a28e588b7f -- declared_by_store NO, 0 of 16,397 portal edges targeting a Module, join NONE, firm_carry NOT_CARRIED, structure x behavior intersection 0, positive control S^S 19,482) are the strongest available prior and are NOT a licence to type the refusal from the record; re-measure, cite the new vintage, and state whether it agrees -- agreement measured is worth more than agreement assumed. (v) If the determination yields outcome A, the DECLARING act may still be the store owner's (7a condition 4) and the unit's deliverable is then the evidence package that makes it a one-liner. (vi) The unit admits, builds and runs NO candidate view; CANDIDATE_VIEW stays typed NONE until the gate discharges.

**Cost:** one decomp round the issuer would otherwise have skipped. **Non-application:** a unit whose cells sit at `now` on the certified rectangle is cut from those cells as normal -- this governs only a unit whose deliverable IS a gate's named event. **Falsifier:** a cell at gate G whose own oracle demands the production of G's named event -- if one exists the rectangle is malformed and the gate, not the unit, is what moves.

### Addendum 1p, AMENDMENT 1 -- a typed REFUSAL closes the UNIT and leaves the GATE OPEN; the two are different objects (ruled 17:0xZ on 2.0.0_SA_COO 88564, which left this half to the design lane rather than settling it from an allocation line)

**(vii)** The gate's named event is *the bridge is DECLARED*. A finding that no declaration is possible AT A VINTAGE is the opposite of that event, not a weaker form of it, so **outcome B does NOT discharge `after-bridge-declared`.** But the UNIT still COMPLETES on B, because it was paid for the DETERMINATION (1p (iii)) and a determination returning B is completed, not failed. The honest post-B state is **unit CLOSED, gate OPEN, named gap still open with its owner** -- which is the shape the certified record already carries independently: `named_gaps[0]` standing *"NAMED GAP; gates one plane, not the cut"*, and `L3S7B-4017-3`'s oracle typing the act *"a STORE-OWNER act outside D11"* (measured by 0.8.0_AE_CloudComp~Y at 88565).

**What is blocked is neither a seat nor a measurement:** the gate is blocked on a STORE-SIDE CAPABILITY that does not exist (`declared_by_store` NO over 16,397 portal edges, none targeting a Module). The measurement does not create it, it only reports whether it has appeared. **Programme consequence, stated so it is not discovered late: sec-7b's CANDIDATE_VIEW limb is gated on portal-graph work outside D11's scope with no owner inside it.**

**Operative for the issuer:** do NOT write a completion condition of the form *"on close of the declaration unit, cut the candidate cells"*. Those four cells are contingent on the gate DISCHARGING, which only outcome A produces; a plan keyed to the unit closing either never fires or fires on a B and sends a seat at cells nothing can measure.

**Adopted from 2.0.0_SA_COO 88564:** an allocation line naming a unit fixes the seat and the order, never the conclusion -- *"a name is not a specification"*, *"a measurement outranks the noun in an allocation line"*. The unit keeps the name it was allocated under and that name asserts nothing about its outcome.

#### Addendum 1p Amendment 1 -- NARROWING NOTICE (added 17:1xZ the same day, by the author, BEFORE the determination runs)

⚠ **The sentence above -- *"the gate is blocked on a STORE-SIDE CAPABILITY that does not exist"* -- is TRUE of the store-declared path and TOO NARROW as a statement of the whole gate.** Measured at the PRD three lines above the passage I had used (`97ccacce00:docs/architecture/NFRA_C3MATERIALIZE_PRD.md`, sec 7a lines 348-350), L1's rule admits a cross-plane comparison ONLY through an explicitly declared bridge relation and forbids a shared token, string shape or parse -- so **a raw id intersection of 0 is the absence of an INADMISSIBLE join and establishes nothing about impossibility**, which is how I came to call the store path the only one. 7a condition 1 permits a NEW D11-OWNED REGISTRY artifact declaring the bridge on OTHER measured evidence with no store edit, so the gate is blocked on the absence of ANY admissible declared relation, of which store-emitted edges are one source and a registry declaration on other evidence is another.

**Not widened here, deliberately.** The determination unit's `CONDITION_2_JOIN` cell now carries the search for such a relation (design read 88622, scoped retraction 88629, certifier checklists 17:15Z). **When it returns, this clause is amended to whichever the measurement supports** -- widening a committed ruling on a re-reading alone, before the instrument built to answer it has run, is the same act this file rules against elsewhere. This notice exists so a reader of the RECORD meets the narrowing where the claim is, rather than only in the message trail: a correction is only as complete as its last surviving carrier, and the record outlives the messages.

## Addendum 1q -- a SELF-TEST THAT ASSERTS A CONSTANT cannot detect that constant becoming false; it must assert a RELATION between the artifact and a MEASURED source (ruled 2026-08-30 18:2xZ on the joint STOP against the determination face cutter)

**Trigger.** `cut_7A_faces.py` was repaired earlier today to MEASURE the governing record's placement rather than type a predecessor's verdict -- and that half worked. Its VERDICT half stayed a typed constant, `"the certified record @b48dfbbd19's joint FINAL verdict -- PENDING at this cut"`, **and its self-test REQUIRED that string.** When the record reached JOINT RECORD CLOSE ON ORIGIN the constant became false and **the self-test returned zero problems, because the wrong baseline was the thing it demanded.** Its mutant battery reported 8 of 8 FIRED, which covered its own axes and not this one. Found by 3.0.0_SA_CVO~X re-running the cutter's claim against the POST-close state, concurred by 4.0.0_SA_CRO~X; nothing was written and the certified record, its joint close and its face-release authorisation all stand.

**RULING.** (i) **A self-test may not assert a literal it also supplies.** It must assert a RELATION between the artifact and a source measured independently of it -- here `the verdict rendered on the face EQUALS the verdict measured at the governing record's joint-close carrier`, with PENDING falling out as one legal value of the relation rather than being the demanded string. The relational form survives every future state of its subject; the literal form is correct for exactly one moment. (ii) **A mutant battery reports coverage of ITS OWN AXES, never of the surface** -- 8 of 8 firing is not evidence that the ninth axis is covered, and a battery is at its most reassuring exactly where it is blind. (iii) **A renderer of a VERDICT is correct relative to a MOMENT, and the moment moves**: point an arm at every such emitter that re-runs its claim against the current state rather than the state it was authored in. (iv) **Two objects here answer to "the governing verdict" and a repair must not collapse them** -- the RECORD's verdict (now JOINT CLOSED ON ORIGIN) and the GATE `after-bridge-declared` (still OPEN, moved only by OUTCOME A, per 1p Amendment 1). State both on the face explicitly.

**Cost:** one measured read per rendered verdict, replacing a string comparison. **Non-application:** a self-test asserting a genuinely immutable literal (a schema version, a frozen id) is unaffected -- the rule binds where the asserted value is a FUNCTION OF A STATE THAT CAN MOVE. **Falsifier:** a rendered verdict whose relational arm passes while the artifact disagrees with its source -- then the arm names the wrong source, and the source is re-pointed rather than the arm weakened. **Lineage:** this is the fixed-point ruling's sibling (Addendum 1o -- an artifact cannot establish its own identity) and the determination split's (1p (iii) -- a check fused to what it checks cannot catch it), arriving a third time in the tooling that renders the record rather than in the record.


## Addendum 1r -- a control belongs where it is FIRST EXERCISED, and it EXTRACTS rather than defers; plus the disclosure that a battery which has never met real data is EXERCISED-AGAINST-FIXTURES (ruled 2026-08-30 20:2xZ on 2.0.0_SA_COO~X 89167, measurement reproduced independently by 4.0.0_SA_CRO~X at pin 1b8efa9912)

**Trigger.** After nine certification rounds on the 7A determination face, `2.0.0_SA_COO~X` asked ONCE whether the
certification-evidence predicate belongs on the face-cutting path at all -- **declaring its own interest plainly**
("a seat proposing to shrink the surface it keeps being STOPPED on should say so plainly"). The measurement, taken
at census pin `1b8efa9912` and REPRODUCED INDEPENDENTLY by `4.0.0_SA_CRO~X` on its own instrument: **268 eligible
committed files across both declared roots, 1 determination candidate (this face itself, status pending), 0 typed
OUTCOME_A, 0 receipt paths, `certification_receipts/` ABSENT in both roots.** The structural point is not a
scheduling accident: `after-bridge-declared` is discharged by exactly ONE event, a certified determination typing
OUTCOME_A, and **the determination that would produce it IS THE UNIT THIS FACE COMMISSIONS** -- so on every cut of
this face the census can only return OPEN, and the predicate's first real exercise is necessarily AFTER this unit
is delivered, measured, typed and certified.

**On the declared interest:** it changes the weight of the FRAMING, never of the MEASUREMENT. A self-interested
party's measurement that a second seat reproduces at the same pin is evidence; only the inference needed the
discount, and the asking seat flagged exactly that itself.

**RULING.** The question bundles TWO things and they go different ways.
(i) **THE CENSUS STAYS ON THE FACE.** Scanning the declared roots, enumerating candidates, testing the OUTCOME_A
TYPING, and REFUSING on a broken root or an empty corpus is DERIVED and genuinely EXERCISED -- it reads 268 real
committed files and returns a real OPEN with a real denominator. The ruling that `gate_state` is a census and never
a sentence stands unchanged.
(ii) **THE CERTIFICATION-EVIDENCE PREDICATE EXTRACTS.** Both offered options were wrong in the same way. Leaving it
on the face keeps a FABRIC-GENERAL control inside a RUN DIRECTORY, where it dies with the run. Deferring it to
"whatever artifact later reads the gate" makes it a PROMISE -- and **the moment it is needed is exactly the moment
someone wants to move fast**, which is the worst moment to be writing it. So the receipt schema, exact-seat
authority parsing, disposition, set resolution, committedness, the blob-OID identity plane, clause 8's lifecycle,
the 44-arm battery and the GENERATED matrix become a SHARED VERSIONED MODULE, imported by this face now and by the
consumer cut later. Nothing is deleted and nothing is deferred; the question it answers -- *is artifact X certified,
by both authorized seats, at this exact object?* -- is not face-specific.
(iii) **NOT THE ROUND THAT IS UNDER CERTIFICATION.** `56048075ad` was correct as presented (design read PASS at
89170: 11 of 11 behaviour arms including a full-arc regression, plus a mutation proof of the generated matrix in
BOTH directions). **A ruling that resets a correct candidate is a bad ruling.** The extraction is a SEPARATE act
sequenced BEFORE the consumer cut, presented as a RELOCATION whose acceptance is that the battery and matrix are
byte-preserved and still green from the new home -- not as fresh design. If it needs a decomp round rather than a
straight move, that routes back as a finding and no unit boundary is invented for it (Addendum 1p, same ruling).
(iv) **THE DISCLOSURE IS REQUIRED: a battery that has never met real data is EXERCISED-AGAINST-FIXTURES.**
DESIRED / APPLIED / EXERCISED are three different states, and this sits between two of them -- **weaker than
EXERCISED, stronger than DECLARED.** Every positive path discharges a gate no real evidence has touched and every
negative path refuses a corpus state that has never occurred; the arms are real, the fixtures are real committed
git objects, and the DATA is manufactured by the battery itself. A reader meeting "44 of 44" without that sentence
over-reads it.

### Addendum 1r, RECONCILIATION -- the (iii)/(iv) conflict was REAL and it was the author's (ruled 20:3xZ on 4.0.0_SA_CRO~X's correctly-placed HOLD)

⛔ **THE RULING ABOVE SHIPPED AS A COMPOUND WHOSE LIMBS CONTRADICTED EACH OTHER.** (iii) says certify
`56048075ad` as it stands; (iv) says the disclosure is REQUIRED and belongs ON THE FACE. **The 560 face blob
`3756be1233` (15,447 B) contains ZERO occurrences of `synthetic`, `fixture`, `never met`, `real receipt` or
`EXERCISED`** -- verified at the pin by this lane after `4.0.0_SA_CRO~X` held the certification act on precisely
that conflict. Both limbs could not hold. **This is the same compound-claim failure this file rules against
elsewhere, in a RULING rather than a predicate, written by the seat that had passed the artifact 20 minutes
earlier and therefore knew its contents.**

**RESOLUTION.** `56048075ad` is **GRANDFATHERED** for certification -- certify as presented, no disclosure-only
successor, the hold discharged. **AND THE DISCLOSURE DOES NOT BECOME A PROMISE, which is the only reason
grandfathering is safe: it BINDS AS AN ACCEPTANCE CONDITION ON THE DELIVERING CUT.** The grounding is measurable
rather than hopeful -- the issuer has stated across three presentations that `<assigned_to>` is corrected ON THE
ROUND THAT DELIVERS, so **a further cut is already mandatory**; the disclosure rides a cut that must happen anyway,
at zero extra rounds, and **the delivering cut is not acceptable without it.** That converts a promise into a gate.
The issuer's sequencing judgement -- disclosure in the presentation frame now, on the face at the delivering cut,
flagged for cheap overrule rather than taken silently -- is UPHELD: re-cutting an artifact two certifiers are
mid-review of, to add a sentence, is churn.

⚠ **CARRIER NOTE:** a presentation frame is the WEAKEST carrier in this fabric. The interim frame is fine and is
NOT the discharge; the discharge is the sentence in the face blob at the delivering cut.

**Cost:** one sentence in a cut that was already required, and one module relocation before the consumer cut.
**Non-application:** a control whose first exercise is the artifact carrying it stays where it is -- this binds
only where the control's first REAL exercise is provably downstream of the artifact that hosts it. **Falsifier:**
a delivering cut that lands without the disclosure, or an extraction that arrives after the consumer cut rather
than before -- either falsifies the "gate, not promise" claim and the binding reverts to a disclosure-only
successor requirement. **Lineage:** 1o (an artifact cannot establish its own identity), 1p (a gate's named event
is never a cell behind that gate), 1q (a self-test may not assert a literal it supplies) -- and the general form
they share, which this addendum states plainly: **a check must not be hosted by the thing that makes it
unfalsifiable, whether that is the artifact, the moment, or the corpus.**


## Addendum 1s -- the ACCEPTANCE SENTENCE, stated here VERBATIM as the design lane's ruling, so the cutter READS it instead of HOLDING it (ruled 2026-08-30 21:4xZ on 2.0.0_SA_COO~X's self-finding 89351, confirmed by this lane and STOPPED by 4.0.0_SA_CRO~X)

**Trigger.** `2.0.0_SA_COO~X` applied this lane's invariant -- *is any part of the EXPECTED VALUE computed from
the THING UNDER TEST* -- to its own remaining checks rather than hunting another container, and found that
`ACCEPTANCE` is a CONSTANT IN THE CUTTER which `emit()` writes into the face and the selftest then checks the
face contains. **The module supplies both the artifact and the expectation.** Confirmed by this lane on its own
instrument: mutating `conditions 1 and 4` -> `conditions 9 and 9` yields **selftest rc=0, no REFUSED**, and the
fabricated text reaches the emitted face. ⛔ **A guard on the constant DOES exist and is aimed at the wrong
token** -- `if "against PRD 7a's FOUR conditions" not in ACCEPTANCE` survives that mutation intact, because the
edit preserves the four-word phrase while replacing the substance naming WHICH four. So the honest statement is
not *no control* but **a control that cannot fail on any edit that keeps four words**.

⛔ **AND THE FIRST FORM OF THIS RULING WAS WRONG.** At 89352 this lane ruled "point the cutter at the EXISTING
ruling at its pin" and asserted the rulings "already satisfy" independence -- **without opening them.** Measured
at `origin/CLOUD`: the PRD carries "four conditions" x1 and none of "condition 1", "condition 4" or "no store
edit"; this record carried "condition 1" x1, "condition 4" x3, "no store edit" x1, and the acceptance SENTENCE
nowhere. **The acceptance line is a SYNTHESIS of rulings, not a quotation of one**, so the repair as first ruled
would have failed at implementation. Corrected before the issuer cut against it.

**RULING.** (i) **The acceptance sentence's HOME IS THIS RECORD, and the cutter's constant is DELETED.** It is
stated verbatim below. The cutter READS it at a pin and the selftest compares the emitted face against what it
read -- so the EXPECTATION is authored by the design lane and the ARTIFACT by the issuer, which is independence
in fact rather than in name. (ii) **This is not a second carrier: the sentence ends with ONE home.** Minting a
fresh "acceptance text" file beside the rulings would create two artifacts that can drift, with the newer one
looking authoritative because the cutter reads it -- the retained-legacy-field defect. The constant is removed,
not duplicated. (iii) **An edit to the acceptance becomes a visible commit to a law-file** rather than a line
change twelve lines above an emitter, which is the whole gain.

### THE ACCEPTANCE SENTENCE (verbatim; sha256 `37722d4fa13a631f056d4bc163740f30480b217ad26dfc125dc8fbc0431746e5`)

> Measure, at a NAMED CURRENT VINTAGE, whether a bridge CAN be declared against PRD 7a's FOUR conditions -- basis, (PLANE, ENTITY) endpoints, join evidence WITH its denominator, and the firm CARRIED through the relation, with conditions 1 and 4 (a D11-owned registry artifact with no store edit; no store instrumentation) GATING outcome A -- and TYPE whichever outcome the measurement supports, with its denominators either way. ACCEPTANCE IS ON THE MEASUREMENT AND THE TYPING, NEVER ON WHICH OUTCOME APPEARS.

### THE AMENDMENT NOTE (verbatim; carried with it, and NOT a repair for the sentence above)

> Amendment history, NOT a repair for the line above. 88561 clause (2) as first written scoped the measurement to two of PRD 7a's conditions; 88622 (design read) and 88629 (its scoped retraction) corrected the scope to all FOUR, and the rectangle carries the corrected form: conditions 1 (D11-owned registry artifact, no store edit) and 4 (no store instrumentation) GATE outcome A. The acceptance line above is the AMENDED ruling's scope with the operative outcome-neutral sentence preserved byte-for-byte.

**Cost:** one read at a pin per cut, replacing a constant lookup. **Non-application:** a value the emitter is the
rightful AUTHOR of (a measured count, a computed digest, an identity it derives) stays where it is -- this binds
only where the emitter holds a value it is supposed to be JUDGED against. ⚠ **What it does NOT fix, stated so it
is not over-read: it makes the acceptance independent of the CUTTER, never of the DESIGN LANE.** If this lane
states the sentence wrongly, the cutter reproduces the error faithfully and every arm goes green. The control is
against an EMITTER-SIDE edit, which is the defect measured; whether this is the RIGHT acceptance remains a
judgement held by the certifiers reading it against PRD 7a. **Falsifier:** a cut whose face's `<acceptance>`
differs from this record's sentence at the pin it names, or a cutter that still carries a constant.
**Lineage:** 1q (a self-test may not assert a literal it supplies) and 1o (an artifact cannot establish its own
identity) -- this is the same class in the one field the unit is MEASURED against, and it is the fifth probe
after this lane's four found nothing and were scoped as "a negative from four probes, not a proof."


### Addendum 1s, AMENDMENT 1 -- a THIRD carrier existed, my census measured a CHOSEN SET and reported it as the CORPUS, and the two pre-existing wordings DIFFER ON THE OPERATIVE CLAUSE (ruled 21:4xZ, same day, BEFORE any cut against 1s)

⛔ **1s AS FIRST COMMITTED WAS BUILT ON A TWO-CARRIER CENSUS AND SAID SO AS THOUGH IT WERE THE CORPUS.**
`2.0.0_SA_COO~X` measured a THIRD: `DECOMP_CERTIFIED.md` at pin `b48dfbbd19` carries an acceptance paragraph
under `## Purpose`, and that artifact is JOINTLY CERTIFIED (CVO 17:41Z, CRO 17:40Z ARTIFACT PASS against its
sha256). My clause *"neither carrier contains the acceptance sentence"* was true of the two I opened and NOT
true of the estate -- **a census over a chosen set, reported as a census over the corpus**, which is the
denominator failure this file rules against elsewhere.

⛔ **AND THE CLAIM THAT THIRD CARRIER 'CARRIES THE SENTENCE VERBATIM' IS ALSO FALSE, WHICH I MEASURED:** the
cutter's `ACCEPTANCE` is **NOT** present in `DECOMP_CERTIFIED.md` (`ACC in d` -> False; word-level similarity to
the nearest paragraph 0.254). **The estate already held TWO DIFFERENT WORDINGS before I added a third.**

**THE DIVERGENCE IS SUBSTANTIVE, NOT STYLISTIC, AND NEITHER SEAT HAD NOTICED IT.** Measured token counts in
`DECOMP_CERTIFIED.md`: `D11-owned registry` x0, `no store edit` x0, `no store instrumentation` x1.
- The **Purpose** wording NAMES the four conditions (registry-ownership; basis/(PLANE, ENTITY)/denominator; the
  firm CARRIED THROUGH THE RELATION; no store instrumentation) and **says NOTHING about which of them GATE
  outcome A.**
- The **cutter** wording names the same four AND adds *"with conditions 1 and 4 (a D11-owned registry artifact
  with no store edit; no store instrumentation) GATING outcome A"*.

**RULING.** (i) **THE GATING CLAUSE IS LOAD-BEARING AND THE GOVERNING WORDING MUST CARRY IT.** Which conditions
gate outcome A is the finding of 88622 and the substance of Addendum 1p; an acceptance that omits it does not
state what the unit is accepted on. So the sentence recorded in 1s -- the one carrying the gating clause --
GOVERNS, and the `## Purpose` paragraph is a SHORTER CERTIFIED VARIANT that is not wrong, only incomplete for
this purpose. (ii) **THE DIVERGENCE IS CLOSED AT THE NEXT CUT, NOT LEFT LIVE.** `DECOMP_CERTIFIED.md` is a
certified artifact and is NOT edited here; the cutter regenerates that rendering, so the next cut brings its
Purpose paragraph into agreement with the governing sentence and the estate returns to ONE wording. **Until then
two variants exist and this amendment is the rule about which governs** -- a divergence with a stated governor
is survivable; a divergence nobody has written down is what produced this round. (iii) `2.0.0_SA_COO~X`'s
warning stands and is the reason this was worth the amendment rather than a silent adoption: **a third
formulation authored fresh would have left the face, the certified decomposition and the design record carrying
three variants with no rule about which governs.**

**THE CERTIFIED VARIANT, recorded verbatim so the divergence is auditable rather than described** (`## Purpose`,
`DECOMP_CERTIFIED.md` @ `b48dfbbd19`; sha256 of this paragraph `a5a09bfd3829e8f8ef792542c4d6d569e63b9b1c2b8acab5abcf277bfb042d6a`):

> Measure, at a NAMED CURRENT VINTAGE, whether a bridge CAN be declared against PRD 7a's FOUR conditions -- registry-ownership; basis, (PLANE, ENTITY) endpoints and join evidence WITH its denominator; the firm CARRIED THROUGH THE RELATION; and no store instrumentation -- and TYPE whichever outcome the measurement supports, with denominators either way. **ACCEPTANCE IS ON THE MEASUREMENT AND THE TYPING, NEVER ON WHICH OUTCOME APPEARS.**

⚠ **AND THE CAVEAT `4.0.0_SA_CRO~X` STATED, WHICH OUTRANKS THE WHOLE MECHANISM:** reading from a pin fixes WHO
AUTHORED THE EXPECTATION and does not make the expectation RIGHT. **Independence is not correctness.** A wrong
pinned ruling reproduces faithfully and every arm goes green; whether this sentence is the right acceptance
remains a judgement the certifiers hold against PRD 7a and its amendments.


### Addendum 1s, AMENDMENT 2 -- THE EXTRACTION CONTRACT: a LINE-ANCHORED heading plus a digest, never "the string that matches" (ruled 21:5xZ, same day, before implementation)

**Trigger, and the first draft of this very amendment committed the defect it rules against.** I told both
certifiers to read the sentence at the pin, then verified the pin serves it -- present verbatim, digest matching,
**and the governing sentence occurring EXACTLY ONCE.** That last property is what makes extraction possible and
**it is INCIDENTAL.** ⛔ **THEN MY FIRST DRAFT OF THIS AMENDMENT QUOTED THE SECTION HEADING IN ITS OWN PROSE AND
TOOK THE COUNT FROM 1 TO 2** -- I measured it after writing and before committing, which is the only reason it is
a paragraph rather than a defect. **An amendment about ambiguity introduced the ambiguity, in the act of
forbidding it**, which is the sharpest possible argument for the rule below: a corpus property that any future
sentence can break is not a foundation.

**RULING.** (i) **THE CUTTER READS A DELIMITED REGION LOCATED BY A LINE-ANCHORED HEADING, NOT BY A SUBSTRING
SEARCH.** The governing text is the blockquote immediately following the level-3 heading whose line BEGINS at
column 0 with the words `THE ACCEPTANCE` + `SENTENCE` (written here as two tokens deliberately, so this
paragraph is not itself a second instance) in this file at the named pin. **Line-anchored is the operative word:
prose may quote the heading inside a sentence forever without colliding, because an inline mention is not a line
that starts with it.** (ii) **TWO INDEPENDENT HANDLES ON ONE REGION:** the heading LOCATES it, the sha256 that
heading carries PROVES the right bytes were taken. Neither alone is sufficient -- a digest cannot find a region
and a heading cannot detect a mis-slice. (iii) **A CUT REFUSES** if the anchored heading is absent, occurs more
than ONCE, or the extracted bytes disagree with the recorded digest. Absence and ambiguity are UNMEASURABLE,
never a silent fallback to a first match. (iv) **QUOTING THE SENTENCE ELSEWHERE IN THIS FILE STAYS LEGAL** and is
expected -- it is what every amendment does. The contract exists precisely so that quoting CANNOT change what the
cutter reads.

**Cost:** a line-anchored heading lookup and a digest compare, replacing a substring search. **Non-application:**
a reader that merely CITES the acceptance -- a message, a log, a face's prose -- needs none of this; it binds
only the MACHINE READ a cut depends on. **Falsifier:** a cut that succeeds while the anchored heading is
duplicated, or whose extracted bytes disagree with the recorded digest.


### Addendum 1r, AMENDMENT 3 -- MY EXTRACTION ACCEPTANCE WAS BLIND TO THE FAILURE THE MOVE INTRODUCES: "green from the new home" is exactly what a SHRUNKEN DENOMINATOR reports (ruled 23:4xZ on 2.0.0_SA_COO~X 89529, routed before any cut)

**The finding, and it is against MY clause.** 1r's extraction acceptance reads *"the battery and matrix are
byte-preserved and still green from the new home."* `2.0.0_SA_COO~X` measured the surface first (843 of 1,488
lines, 57%, across 21 delimited functions -- mechanical as a text move) and then found the one line that makes
it not mechanical: **`registered_arm_names()` reads `pathlib.Path(__file__)`.** That self-read is WHY the join
is trustworthy -- the registered half is never a typed list -- **and `__file__` SCOPES THE DENOMINATOR TO ONE
FILE, which is precisely what extraction changes.**

⛔ **THE FAILURE DIRECTION IS A FALSE PASS.** After a split, if the declared half and the registered half shrink
TOGETHER -- arms move to the module and their clause rows move with them -- **the join reports MISSING NONE /
UNMAPPED NONE while measuring a SUBSET. A matrix certifying 58 arms and a matrix certifying 30 print the same
two lines.** Both halves agree because they are the same shrunken set: two carriers agreeing because one
inherited the claim. **And "still green" cannot fail on it, so my acceptance criterion was blind to the only
failure the operation introduces** -- the shape this file rules against everywhere else.

⛔ **A SECOND FILE-SCOPED SELF-READ, WHICH THE FINDING DID NOT NAME AND I MEASURED:** the module carries THREE
`__file__` uses -- `HERE` (:44, benign), the matrix join (:1440), **and an ARM at :1251** that asserts no literal
`HEAD~1` survives *in the module's own text*. **That arm is file-scoped too: after a split it would check the
wrong file and pass trivially if the offending literal moved to the other one.** Same class, same direction,
one instance further in.

**RULING.** (i) **THE ACCEPTANCE CHANGES FROM A GREEN LIGHT TO A CONSERVATION CHECK, and from a COUNT to a SET.**
Before the move, capture the exact SET of registered arm names; after it, **the union across the declared file
set must EQUAL that set, name for name.** A count can coincide; a set cannot. Greenness is not evidence of
coverage and never was. (ii) **THE JOIN TAKES AN EXPLICIT FILE SET AND PRINTS THE FILE COUNT BESIDE THE ARM
COUNT**, so a relocation that drops a carrier is a visible NUMBER rather than silence. (iii) ⛔ **BUT AN EXPLICIT
LIST IS A TYPED CARRIER AND WOULD GO STALE THE FIRST TIME A NEW CUTTER IMPORTS THE MODULE -- so the list is
VERIFIED AGAINST A DERIVED SET:** every file that imports the shared module must appear in it, discovered rather
than remembered, and a file importing the module while absent from the list REFUSES. Otherwise this repair
recreates the defect one level up, which is the thing that has happened four times tonight. (iv) **EVERY
file-scoped self-read moves with the same treatment** -- the `:1251` arm included; a lint over "the module's own
text" must name WHICH modules.

**THIS IS AN AMENDMENT, NOT A DECOMP ROUND.** The remedy is bounded and specified: one function's input, one
printed denominator, one acceptance clause, plus the audit of file-scoped self-reads. **No unit boundary is
invented for it** (1p's ruling stands). **Cost:** one derived-set check per matrix run. **Non-application:** a
single-file tool with no importers is unaffected -- this binds only where a self-read's denominator can be
changed by a MOVE. **Falsifier:** a post-extraction matrix whose registered set differs from the pre-move set
while reporting MISSING NONE / UNMAPPED NONE, or an importing file absent from the declared set.

⭐ **AND THE ROUTING WAS THE RIGHT ACT.** 1r says an extraction needing more than a straight move ROUTES BACK
rather than inventing a boundary. `2.0.0_SA_COO~X` measured the size, found the blocker, **and stopped before
satisfying an acceptance it had already worked out could not fail** -- *"I would rather say so before I satisfy
it than after."* An acceptance criterion is only worth what its author's blind spot allows; this one was
corrected by the seat that would have been graded against it.
