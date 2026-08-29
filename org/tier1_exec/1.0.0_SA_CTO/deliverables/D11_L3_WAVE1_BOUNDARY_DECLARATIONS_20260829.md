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

**None of the four declarations discharges a PRD §6 falsification test.** §6.3's input (firm-carry per bridge) and §6.4's exclusions (FLOW, SEMANTIC = NOT-DELIVERED-AT-L2) are supplied by wave 1; **6.3 runs at wave 2, 6.1 / 6.2 / 6.5 at L4.**
