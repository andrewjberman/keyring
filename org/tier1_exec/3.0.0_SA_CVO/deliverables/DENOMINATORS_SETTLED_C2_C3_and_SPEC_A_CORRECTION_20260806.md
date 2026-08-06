# DENOMINATORS SETTLED: C2 = 12, C3.i = 14 — and my Spec A grounded on the SHADOW partition

**Seat:** `3.0.0_SA_CVO`. **Date:** 2026-08-06 ~23:15Z. **Andrew-directed:** *"let's proceed with
settling these denominators."*
⛔ **THIS CORRECTS `SPEC_grain_overlap_and_vertical_join_for_CTO_D_20260806.md` @137a047c1 BEFORE IT
IS BUILT.** Spec A's mechanism is wrong. Spec B stands and its priority increases.

## 1. SETTLED — the authority exists and I had not read it

`org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` (authored 2026-07-30, `schema_version: 1`,
`population_law: canon-first-debt-subset`) is the canonical catalog. Counted from the file:

| layer | **CANONICAL** | in the kuzu graph |
|---|---|---|
| **C2 motif families** | **12** (`c2_motif_families`) | **19** `C2Motif` |
| **C3.i deterministic structures** | **14** (`c3_deterministic_structures`) | **4** `C3System` |

**So `STATE_FRICTION_DESIGN` §1's "14 structures over 138 chains" is CORRECT and canonical, and
F1's `structures_touched: K of 14` is the right denominator.** The 4-vs-14 question is closed.

## 2. THE PART THAT MATTERS MORE THAN THE COUNTS

The canonical file's own words, verbatim (`:11-18`):

> *"C2 (motifs) and C3 (systems) are AGNOSTIC STRUCTURAL layers… **They are NOT debt concepts.** The
> six detector motifs (silent-display-fork, cross-firm-asymmetry, hardcoded-firm-literal,
> dead-component, orphan-endpoint, render-without-null-guard) are a **DEVIATION SUBSET**… They remain
> valid AS deviation motifs. **Presenting them as 'the C2 catalog' or their clusters as 'the C3
> systems' is the exact incoherence this file exists to kill: THE PRIMARY POPULATION OF C2/C3 IS THE
> CANONICAL CATALOG BELOW. A debt motif is a shadow; this file is the object."***

**THE KUZU GRAPH DOES EXACTLY THAT.** Measured:

- The 19 `C2Motif` nodes are 13 structural (`AAccessMotif`, `BIoMotif`, …) **plus the exact six named
  detector motifs** — `SilentDisplayFork`, `CrossFirmAsymmetry`, `HardcodedFirmLiteral`,
  `DeadComponent`, `OrphanEndpoint`, `RenderWithoutNullGuard`.
- The 4 `C3System` nodes are clusters over that set, `source: semctl-c2c3-materialize`. One of them
  is `system:firm-conditional-display`, whose `member_motifs` are **precisely**
  `silent-display-fork / cross-firm-asymmetry / hardcoded-firm-literal` — **a debt cluster
  materialised as a C3 system**, which is the named incoherence, verbatim, live in the graph.

**Positive-controlled:** `sys-*` (the canonical 14) returns **0 rows** from kuzu while `system:*`
returns **4** — so the query form works and the absence is real. **The canonical partition does not
exist in the graph at all.** It lives in the ontology file + `estate-coverage-resolver.json`.

## 3. WHAT THIS DOES TO MY SPEC A — it invalidates the mechanism

Spec A §A3 specified the roll-up as a graph traversal:
`C3System —CONTAINS→ C2Motif —CONTAINS→ C0`.

**That traverses the SHADOW partition.** Building it would deliver grain-overlap over debt-motif
clusters while printing `c3i` in a `DECLARED TERRITORY` block —

> **INSTITUTIONALISING, IN A TOOL, WITH DENOMINATORS ATTACHED, THE EXACT INCOHERENCE THE CANONICAL
> FILE WAS WRITTEN TO KILL. A doc that does this is wrong; a tool that does it is wrong at scale and
> carries provenance that makes it look settled.**

**I grounded on the graph, found a materialised hierarchy, and never asked whether it was the
canonical one.** The membership edges are real, the counts are real, the traversal would work — and
it answers a question nobody asked. *Same class as the parallel taxonomy this morning: correct
mechanics over the wrong subject.*

### What survives, and what changes

| | status |
|---|---|
| **Multi-grain overlap as a capability** | **STANDS.** Andrew's instinct is right and the B6 saturation defect is real and unchanged. |
| **c2/c3i keyed on the CANONICAL partition (12/14)** | **This is what to build.** |
| **c2/c3i keyed on the graph's `C2Motif`/`C3System`** | **DO NOT BUILD.** Shadow partition. |
| **Mechanism = graph `CONTAINS` traversal** | **WRONG.** The canonical partition is not in the graph. |
| **Mechanism = join through the ontology + resolver** | **CORRECT**, and it is the same join as Spec B. |
| **Sequencing "A before B"** | **REVERSED. B is now a PREREQUISITE for A** — both grains need the join. |

*(A separate, legitimate capability: overlap over the SHADOW partition as a **debt** lens — 6 detector
motifs, 4 clusters. That is a real question. **It is not C2/C3 grain and must never be labelled as
such.** Not spec'd here.)*

## 4. THE STANDING HAZARD — this will happen to the next agent too

**Two ontologies share the C2/C3 vocabulary over different substrates**, one canonical (12/14, in a
YAML + a snapshot) and one materialised (19/4, in the live graph an agent naturally reaches for). The
canonical file declares the second a shadow; **nothing in the graph says so.** A `comp-kuzu` query
returns `C3System` with full provenance and no marker that it is the deprecated population.

**I made this error within minutes of looking, holding the verification seat, on the day I filed two
other findings about parallel structures.** The next agent will make it too.

**Candidate remedies — PROPOSED, NOT IMPLEMENTED** (no gates, Andrew-direct 2026-08-06):
1. A `population: shadow` / `deprecated_as_c3: true` property on the materialised nodes, so a graph
   query carries the warning the YAML holds.
2. Rename the materialised layer off the C2/C3 tokens entirely — `DebtMotif` / `DebtCluster`.
   **Token collision is the mechanism; renaming removes it at the source.**
3. `comp-kuzu` prints a one-line notice when a query returns `C2Motif`/`C3System`, pointing at the
   canonical catalog.
**Routing: CTO owns the ontology surface; this is a naming act and therefore Andrew's to ratify.**

## 5. Denominators still open

- **138 chains (D2 / C2-motif instances)** vs the graph's 19 `C2Motif` — the same shadow/canonical
  split one layer down. Canonical count for the chain layer confirmed at **138** by comp-estate;
  not re-derived independently here.
- **926 vs 927 vs 847** across comp-blast modes (recorded in `S4b_…` @345552f04). Minor, still open.
- **`c3_ii_semantic_verticals: 5` in the canonical YAML vs 29 reported by comp-estate.** Noted, NOT
  settled — the YAML's 5 may be a worked-example subset rather than the roster. **Flagging rather
  than guessing; F1/F2/F4 are all scoped per-vertical so this one matters.**

-- `3.0.0_SA_CVO`
