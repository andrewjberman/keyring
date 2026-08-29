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

**RULING.** (i) **Every §6 test is a PAIRED arm on ONE build — a POSITIVE half (the build survives the falsifier) and a NEGATIVE half (a degenerate that should fail, fails).** A test is DISCHARGED only when both halves return the expected sign; a build that passes the positive and ALSO passes the negative has FAILED that test. This is the same-build rule of Addendum 1g applied inside each test. (ii) The three proposed negative halves are ADOPTED as written: **6.1 SUBSTITUTION** — a genuinely different resource at the same position MUST NOT keep the identity; **6.2 SUCCESSION BREAK** — nodes genuinely removed or replaced between nights MUST break succession, and a flat 100% with removals present is a FAILURE SIGNAL, read from the per-night series 1f already requires; **6.5 CONTENT SENSITIVITY** — the two planes hold different content, so the identities MUST differ between them; identical output on both is a layer reading nothing. (iii) **6.3 and 6.4 are read, not amended:** 6.3 already carries both signs (a constant fails it; a firm-separating fusion passes it) — its relational bar (1f) stands; 6.4 scopes views ENTERING the fusion by design and is not the place to test the output — the output is tested by 6.1/6.2/6.3/6.5 with their negative halves. (iv) **ORACLES BEFORE ARTIFACTS:** the positive and negative halves of 6.1 and 6.5 — population, pass condition, instrument — are DECLARED at the L4 cut, in the PRD, before the L4 artifact exists, on exactly the rule 1f set for 6.2's N: a bar set after its data is a fit. 6.1 and 6.5 today carry no oracle at all; that is now a named gap the L4 cut must close, not a hole discovered at run time. (v) **The degenerate read is REPEATED by a non-author** before the L4 cut: 3.0.0_SA_CVO~X or 4.0.0_SA_CRO~X scores at least one DIFFERENT degenerate (the proposal's stated limit — one read, one case): the two that matter are the *identity = content hash* layer (maximally brittle — passes every negative half, fails 6.1's positive; confirms the pair is two-sided) and the *identity = firm label* layer (passes 6.3 by construction, fails 6.1-substitution and 6.5-content; confirms 6.3 alone was never sufficient). A read that finds no fourth hole is recorded with its case named; a read that finds one lands as a further paired arm. **(v) RECORD — FIRM-LABEL case scored by 3.0.0_SA_CVO~X (122851Z, non-author, PRD §6 + proposal read independently):** positive/legacy shape passes as predicted (6.1 rename survives; 6.2 flat; 6.3 by construction; 6.4 unchanged; 6.5 runs unchanged); the three adopted negatives REJECT it as required — 6.1 substitution (identity wrongly survives a same-firm different resource), 6.2 succession break (a removed/replaced resource inherits the firm identity), 6.5 content sensitivity (different content, same firm label, one identity). **No fourth hole in this case.** Fixture constraint it adds, binding at the L4 cut: the 6.1 and 6.5 oracles must pin SAME-FIRM / DIFFERENT-RESOURCE and SAME-FIRM / DIFFERENT-CONTENT fixtures, or the negative halves are satisfiable by a cross-firm change that 6.3 already catches. The CONTENT-HASH case remains OPEN for a non-author. (vi) **PRD:** §6.1, 6.2, 6.5 each gain their negative half, and the §6 preamble sentence of 1g reads "…all five DISCHARGED, each on both halves, on one build" — **QUEUED to the same frozen-round PRD edit** (now five items: L1 table; 6.3 metric/view/population; 6.2 N; §6 preamble; the three negative halves). **Why now and not at L4:** every unset oracle between the L4 cut and the first scheduled night adds to the completion date one-for-one (6.2 is wall-clock), so the cost of declaring these is lowest today and highest the day L4 lands. **Cost:** none this wave — nothing in wave 3, the firm-carrying view or the 6.3 re-run changes. **Non-application:** no rectangle in certification cites §6.1/6.2/6.5; nothing here sets N or an L4 date.
