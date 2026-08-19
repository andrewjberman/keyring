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

## B. INSTRUMENT ROWS (each comp-tool's declared coverage universe — inventory pass to follow)

Method: for every registered comp-tool, read its declared coverage (boundary_report / docstring /
registry row) → classify `declared-and-compilable` / `declared-not-compilable` / `UNDECLARED`.
Denominator = the gate-maintained registration count (~97 executables, registries authoritative).
**Not yet scored — first pass next session window.** Known seeds: comp-estate (topology/served-name
claims = priors under test, Rule 21 — its universe is the frozen A10 resolver); comp-find (line
grain, not AST — declared honestly in its own banner); comp-iam (models `(action)` not
`(action, resource)` — declared in law, so `declared-not-compilable` on the resource axis by design).

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
