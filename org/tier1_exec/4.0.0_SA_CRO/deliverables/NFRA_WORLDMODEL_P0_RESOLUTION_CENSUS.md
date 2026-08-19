# NFRA_WORLDMODEL P0 — THE RESOLUTION CENSUS (working document)

**Author:** 4.0.0_SA_CRO · **Opened:** 2026-08-19 · **Status:** OPEN — skeleton + pre-seeded rows; scoring passes land incrementally, each script-verified.
**Charter:** PRD v1.1 §4 P0. Doubles as the program's ground-truth atom_decomp run (08-14 standing law) — **the COO decomposition package issues only WITH this document scored.**
**The predicate (Andrew-ruled, R1 Q3):** a coverage universe RESOLVES when **(a)** its population derives by running a named tool — no hand lists; **(b)** derived count = declared count; **(c)** a drift gate blocks divergence. Hand-RULED membership is legal only through a naming-act register; hand-COPIED is the defect. His verbatim bar: *"compilable not just conceptual or hand-drawn … every square inch of our estate at every layer of granularity C(N) and D(N)."*
**Seam (PRD §5):** census rows CITE registry terms; they never re-define them.

## Verdict vocabulary
`RESOLVES` (a+b+c all hold) · `FAILS-a` (no deriving tool / hand list) · `FAILS-b` (count mismatch) · `FAILS-c` (no drift gate) · `UNDECLARED` (no declared count/universe to check against) · `PARKED-INPUT` (universe defined by a parked limb's output; scored when named).

## A. LEVEL ROWS (the ladder, per substrate where the level materializes)

| # | Universe | Declared (source) | Deriving tool | Derived | Verdict | Notes |
|---|---|---|---|---|---|---|
| A1 | Registry terms (the definitions layer itself) | 68 entries (SYSTEM_DEFINITIONS v3.2) | `check_system_definitions.py` | 68 (form only) | **FAILS-c partial** | The checker validates entry FORM, not population derivability; which of the 68 are COVERAGE UNIVERSES is itself un-enumerated → row A1a |
| A1a | The coverage-universe subset of the 68 | UNDECLARED | — | — | **UNDECLARED** | First scoring task: classify all 68 terms universe/not-universe; the classification is a naming-act proposal (routes per seam) |
| A2 | Substrate values | 4 (aws, portal, codebase, ms — registry v1.9) | graph node census (`comp-kuzu`) | aws/portal/ms populated; **codebase = 0 nodes** | **FAILS-b** | The declared universe exceeds the materialized one; S0 rename half-landed (80 `layer` vs 27; `pipeline` 1,337 nodes retired-but-present, `semctl` 23 dropped-but-present) |
| A3 | C0/C1 (nodes/interactions per substrate) | graph-derived | derive_runner → Nessie/Iceberg → Kuzu | 20,639 nodes / 41,253 edges (08-12 build) | **FAILS-c** | Derivable + counted, but ONE label (CloudNode) and no declared-count parity check; freshness rides the nightly derive — gate exists for aws, absent for the dark substrates |
| A4 | C2 motif families | 12 (canonical yaml) | census classification (135→138 chains) | 117 classified / 18 residue (pre-adjudication census) | **FAILS-b/c** | Census predates the 07-30 naming acts; residue counted-not-dropped (honest) but no regen path (W-16) |
| A5 | C3.i deterministic structures | 14 (canonical yaml, "DISCOVERED via union-find") | `NFRA_MOTIF_P2_c3_emergence.py` | **4 materialized** | **FAILS-b, provenance defect** | The 14 is a LEGISLATED vocabulary presented as discovered (C3II scan §5b, Andrew-challenged 08-11); needs either an honest re-derivation or a provenance re-label via naming act |
| A6 | C3.ii semantic verticals | **28 ratified** (08-07 merge) vs **29 materialized** (yaml/resolver/matrix) | resolver + comp-estate --matrix | 29 | **FAILS-b → fix landing** | W-15 staffed at 0.8.0, Wave-1 08-20; re-score after it lands |
| A7 | C4 grid (Subject × Function) | 3×4 ratified (build collapsed 08-19) | **ZERO code reads the grid** | — | **FAILS-a** | W-09/B1: the grid resolver is specified, unbuilt — a P1 build |
| A8 | C4 segments | 5 (canonical) | comp-estate --segments | 5 | **FAILS-c** | Serves the declared 5; no drift gate binding segments to grid rows/columns (the 08-12 measured-block is hand-maintained prose) |
| A9 | D1–D3 rails | rule bank (NFRA_VELOCITY CORE) | — | — | **UNDECLARED at this seat** | Scoring requires the rule bank's own declared counts; census cites, never re-derives — coordinate with CORE before scoring |
| A10 | The 138-chain ground set | 138 (resolver, vintage 07-30) | `estate-coverage-resolver.json` regen | **frozen**; `--refresh` REGRESSION (W-16: hardcodes last_review) | **FAILS-c, the type specimen** | Limb B's exact target; the cardinal rule's origin case (frozen census JOIN). P1: defrost per the v0.1 design |

## A1a — THE COVERAGE-UNIVERSE CLASSIFICATION OF THE 68 REGISTRY TERMS (scored 2026-08-19, pass 1)

**Method:** every term classified UNIVERSE (extension = an enumerable member set instruments can
scope to) vs NOT (rule / discipline / operator / meta / field / deprecated). Denominator: 68 terms
(registry v3.2, script-enumerated). **This classification is a PROPOSAL** (seam: census cites,
never re-defines) — the universe/not axis routes to the legislature with the P0 report.

**UNIVERSES — 26:** Estate (degenerate whole; derives iff Substrate does) · Substrate (the Q3 type
case; 4 values) · C0 · C1 · C2 · C3 (via projections) · C3.i · C3.ii · C4 · Segment (5) ·
Vertical (=C3.ii grain) · System (=C3.i grain) · Motif (=C2 grain) · Chain (=D2 instances, 138) ·
Subject (3 rows, partitions verticals) · Function (4 columns, span sets) · Domain (4 values over
the C3.i anchor cover) · Deploy_State (2 states over code copies) · D1 · D2 · D3 (instance
grains) · Estate_Contracts (the D3 store) · Contract_Record · Role (14-value lens on C0) ·
Relation (10-value lens on C1) · Name_Variant (A_07 population rows — DATA-grain, scores at the
instrument pass).
**Value-slices counted under their axis (4):** Api_Serving / Artifact_Serving / Observability /
Ui_Dataflow (Domain values).
**META-VOCABULARY (1):** Scope — its VALUES name universes (estate…single-artifact); the term
itself is the enum, not a census target.
**NOT UNIVERSES — 37:** the verification/discipline family (Plane, The_Ceiling,
Boundary_Declaration + its 4 parts, Known_Negative, Denominator_Grain,
Honesty_Read_As_Completeness, Reconciliation_Point, Subordination_Clause, Limitation_Class_Form,
Observation_Not_Assertion, View_Time_Compiled, Intent_Denominator, Intent_Source, Variance,
World_Model [the assembled view], Map, Federation, Surface, Homeless, Lifecycle_Class,
Lifecycle_Value [contested], UNDECLARED, Cascade [axis over C3 coverage — its denominator IS
C0's, deliberately not a second universe], Atom [method-run grain, not estate grain], Canon,
Cross_Fabric_Term_Ownership, Alias_Set_Carry, Alias_Set_Fallback, Unreconciled_Aua,
Alias_Key_Expansion, Semantic_Estates [deprecated], Substrate_Side [deprecated], Territory
[retired]). *(26 + 4 + 1 + 37 = 68 — the classification carries its own parity check.)*

**Per-universe tooling verdicts (pass 1 — extends the A-rows):**

| Universe | Deriving tool today | Verdict |
|---|---|---|
| Substrate, C0, C1, D1 | comp-kuzu over the live graph | RESOLVES-a for aws/portal/ms; **FAILS-b on codebase (0 nodes)**; FAILS-c (no declared-count parity gate) |
| C2, Chain/D2 | frozen census/resolver | **FAILS-c** (A4/A10 — the defrost target) |
| C3.i / System | emergence script vs hand list | **FAILS-b** (A5, 14-vs-4 provenance) |
| C3.ii / Vertical | resolver | **FAILS-b → W-15 landing 08-20** (A6) |
| C4 / Segment | comp-estate --segments | FAILS-c (A8) |
| Subject, Function (the grid) | **no reader — B1 unbuilt** | **FAILS-a** (A7); the W-24 placement is RULED membership awaiting its register (B3) |
| Domain (+4 values) | none declared at this seat's knowledge | **UNDECLARED-tooling** — resolve at the B-pass |
| Deploy_State | none (git branch-vs-tree diff is the natural tool) | **FAILS-a** — divergence tracking is the axis's PURPOSE and has no instrument |
| D3 / Contract_Record / Estate_Contracts | store exists; ls+schema is derivable | **UNDECLARED** (no declared count to check) |
| Role, Relation | rule-bank vocabularies (CORE) | **A9-coordinate** — census cites, never re-derives CORE |
| Estate | union of Substrate | inherits Substrate's verdicts |

## B. INSTRUMENT ROWS (each comp-tool's declared coverage universe — inventory pass to follow)

**PASS 1 SCORED 2026-08-19 (registry grain — each tool's REGISTERED declaration, not its
docstring; per-tool drill-down = pass 2).**

**The denominator, four-way, reconciled by the gate:** on-disk `.tools/comp-*` executables = 91 ·
manifest live names = 93 · `tools_index` registered = **76 (the declared layer this pass scores)** ·
`comp-tools.yaml` reference rows = 38 (a DOC subset, not a registry — flagged: a second,
smaller hand-list beside the gate-maintained one is itself a two-homes shape).
`comp-manifest-check completeness` = **PASS over 76** (registration + placement + self-routes +
existence; output contracts 32 declared + 44 pending; stage-2 vocab 34 declared all-canon;
7 retired aliases disjoint; 28/76 subcommand-establishable, 10 standing drift, backfill pending).

**Classification of the 76 declared coverages (pass-1 verdicts):**
- **ONTOLOGY-TERMED (~14)** — universe stated in registry terms (graph/estate/segment/rule-bank/
  tool-universe): comp-estate, comp-kuzu(+full,+inc), comp-aws, comp-toolgraph (the tool suite AS
  C0/C1), comp-depth, comp-describe, comp-cluster, comp-ontolint, comp-manifest-check,
  comp-system, comp-drift, comp-pulse, **comp-genesis**.
- **CONCRETE-SCOPED (~60)** — universe stated clearly but in NON-ontology terms (repo, S3
  prefixes, IAM principals, CloudFront, git history, org records). NOT a defect per se — but
  under the ruled predicate these universes tie to registry terms only via unstated mappings
  (e.g. "the repo" ↔ substrate:codebase). **The pass-2 question: give each a
  `coverage: {term}: {value}` line, compilable, or record why its universe is legitimately
  outside the ontology.**
- **UNDECLARED: ~2 borderline** (cache-maintenance verbs whose universe is their own cache).
- Standing seeds confirmed in-class: comp-estate (priors-under-test, frozen A10 universe),
  comp-find (line grain, self-declared), comp-iam (`(action)` not `(action,resource)` —
  declared-not-compilable on the resource axis BY DESIGN, law-recorded).

**⭐ PROGRAM FINDS (B-pass yield beyond scoring):**
1. **`comp-genesis` EXISTS: "SPIN UP a NEW company: bootstrap its graph + ontology-binding +
   closed learning loop."** Build-ladder rung 2 fires on the crown jewel itself — P4's derivation
   engine assesses/extends comp-genesis before writing anything new. Investigate at P4 spec time:
   what it provisions today, on which canonical forms, and the delta to ONBOARD-ZERO.
2. **`comp-tool-health`** (3-axis per-tool health) + **`comp-toolgraph`** (the suite as C0/C1) are
   the natural instruments for pass 2 of THIS section — the B-pass should ride them, not re-derive.

## C. FOUNDING EVIDENCE (the class, measured on the program itself)

- **@ef191fa (2026-08-19):** this program's own registration minted `NFRA_WORLDMODEL` without
  compiling the codes-in-use set — a 30-second `grep org/projects/` would have caught it; the
  risk-reflex HOLD fired on REGISTRY.md and was misread as noise. Restored @f0b48b39b6. **The
  failure the predicate exists to kill, produced while registering the program that kills it.**
  Remedy candidate for P1: project-registration gate — deny a new `org/projects/{CODE}.json` whose
  CODE already exists in the registry (trivially compilable; would also have fired on the row).

## D. SCORING LOG

- 2026-08-19: skeleton opened; rows A1–A10 pre-seeded from session-grounded evidence (each count
  carries its source in-row; A2/A3 figures are 08-12-build vintage — re-derive live at scoring).
- 2026-08-19 (later): **evidence home moved** — Andrew-direct fold @6096e11d95 lands the
  OPAL_WORLD_MODEL content at `infra/system/ontology/worldmodel/`; `10_census/` is this census's
  declared SEED + DIFF BASE (07-31 vintage snapshot, marked so — never a live read). Observed
  vintage delta at fold-verify: `20_rulings/RULINGS_LEDGER.jsonl` = **121 rows live vs 118
  declared in PRD v0.1** — the census predicate applied to its own seed (FAILS-b shape, almost
  certainly 3 rulings landed after v0.1 was written; adjudicate the 3-row provenance at the first
  Limb-A-adjacent scoring pass, do not silently re-declare). Fold-verify counts: subtree find =
  **68 files** vs the relay's "62" — classify at the same pass (dir-grain vs file-grain or
  post-fold additions; both counts recorded so the delta cannot vanish).
