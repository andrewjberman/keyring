# TWO-GRAIN TOOLSCAPE — UNIVERSE AUDIT (step 1 of the ruled sequencing)

**Author:** 1.0.0_SA_CTO
**Date:** 2026-08-04 (~13:1xZ)
**Program:** Two-grain toolscape consolidation (Andrew design direction @6b6e68455d; START WORD
Andrew-direct ~1300Z at the CVO terminal, record @74451794ee amended @d5dd45fd1).
**Sequencing (ruled):** UNIVERSE AUDIT (this doc) -> dial program as inventory (CVO) -> CTO PRD ->
Andrew ratifies.
**Umbrella:** this program is the registered umbrella for the comp-blast Part-2 PRD (CTO log
2026-08-04 0540-0631Z item 7).

## 0. The design being audited for (verbatim anchor)

Andrew, CVO terminal 2026-08-04 ~06:3xZ (@6b6e68455d, full verbatim in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DESIGN_DIRECTION_two_grain_toolscape_20260804.md`):
two grains — **Grain 1 = NODE navigation** (one broad comp-trace-style tool over the resource
graph: walk/up/down/paths/blast), **Grain 2 = CODE drill** (at any node backed by executable code,
descend to comp-pipescript-style assessment: io registry, dependencies, deploy state). Effect:
most navigation + drill comp-tools consolidate into clean navigation + high-fidelity detail on
demand.

## 1. The tool universe — denominator (gate-maintained, re-verified this session)

`comp-manifest-check completeness` run 2026-08-04 ~13:0xZ (this session), PASS:

- **87 tracked+committed `.tools/comp-*` executables**, all accounted:
  **69 tools_index (routable)** + **18 excluded-with-reason** (gates, search primitives,
  session-context setters, producers — `graph-call-manifest.yaml:33`).
- Coverage-map ledgers 90; 5 retired aliases all disjoint from live (incl. the deleted
  `pipescript` / `comp-semantic-estates` / `comp-opalbizsem` forms).
- Output contracts: **20 of 69 declared + 49 pending**; stage-2 vocab (rail/grain/plane/scope in
  canon enums): **23 declared**.
- 12 tools carry standing subcommand drift (reported, non-blocking, backfill pending).

**Consequence for the PRD:** the universe is GATE-MAINTAINED (registration invariant blocks
unregistered executables), so the consolidation's denominator is stable and checkable — the PRD
can bind to the invariant, not to a frozen digit.

## 2. First-pass two-grain partition of the 69 routable tools

Classification basis: each tool's `does:` line in `graph-call-manifest.yaml` tools_index
(:1439-1511) + declared grain in `comp-output-contracts.yaml` / `comp-coverage-map.yaml` where
present. Rows grounded ONLY on the `does:` line are first-pass CTO reads — the dial program
(next step) is the instrument that confirms or moves them. Marked **[INFERRED]** where so.

> **VOCAB CORRECTION (Andrew-direct ~150xZ via CVO, BINDING FORWARD):** no grain-explicit
> terminology on the tool-classification side — coordinates are **C(N)/D(N) only**, the two
> surfaces are **NAVIGATE** (breadth) and **DRILL** (depth). The headings below are re-headed
> accordingly (original "Grain-1/Grain-2" wording retired; the word *grain* survives only in the
> ratified graph-side homes — grain_contract, D1 value rail — per the honestly-surfaced boundary).
> The PRD must inherit THIS vocabulary, not the original headings.

### A. NAVIGATE-SURFACE CANDIDATES — breadth, node navigation over the graph (16)

`comp-trace` (dependency walk) · `comp-blast` (blast radius) · `comp-diff` (change->blast) ·
`comp-depth` (grain-coordinate scope/drill/rollup — see §3) · `comp-platinum` (fullstack
component->gold) · `comp-cluster` (page->panel->drilldown) · `comp-routes` (serving path) ·
`comp-estate` (named-thread traversal + ontology views; FIRST CONTACT) · `comp-kuzu` /
`comp-kuzu-full` / `comp-kuzu-inc` (the raw query engine + refresh variants) · `comp-describe`
(one node synthesized) · `comp-similar` (nearest-by-purpose) [INFERRED — similarity, not
traversal; may be C] · `comp-xref` (symbol cross-ref) [INFERRED] · `comp-pydeps` (compiler-layer
reference graph) · `comp-toolgraph` (the tool suite as a graph) [INFERRED — meta-plane].

### B. DRILL-SURFACE CANDIDATES — depth, code/executable drill at a node (10)

`comp-pipescript` (the archetype: io/dag/deployed/postdeps per gold script) · `comp-symbols`
(intra-file AST inventory) · `comp-dispatch` (orchestration-DAG, chain grain — declared sibling
of pipescript's per-script grain) · `comp-dataflow` (value-origin + canonical-source at the
read-site) · `comp-gitdrill` (TIME axis: producer git history) · `comp-icedrill` (VINTAGE axis:
artifact version/partition history) · `comp-lambdamap` (deployed-SHA vs live per lambda) ·
`comp-iam service` (per-lambda permission view — the SERVICE subcommand only; the rest of
comp-iam is C) [INFERRED split] · `comp-validate` (per-script artifact invariants) [INFERRED —
QA-gate flavor] · `comp-freshness script` (per-script run-readiness) [INFERRED — same].

### C. NOT CONSOLIDATION TARGETS — distinct jobs the two-grain surface must not absorb (43)

- **Write-paths / producers (never navigation):** `comp-aws` (cloud-graph derive+cert),
  `comp-build` (trace cache rebuild), `comp-graph` (freshness status/clear).
- **Estate census/ledger instruments (standing dimensions, verdict-bearing):** `comp-pulse`,
  `comp-axes`, `comp-heat`, `comp-xray`, `comp-dups`, `comp-clobber`, `comp-debris`,
  `comp-legacywriter`, `comp-assets`, `comp-keys`.
- **Security/permission forensics:** `comp-iam` (gaps/simulate/census), `comp-iam-usage`,
  `comp-secrets`, `comp-whoread`, `comp-deadgrant`, `comp-denytest`, `comp-tagauthz`,
  `comp-firmsep-sweep`, `comp-pii`.
- **Pipeline QA / parity:** `comp-parity`, `comp-incrparity`, `comp-chainrun`,
  `comp-constants`, `comp-drift` (seam orchestrator), `comp-trigger`.
- **FE contracts:** `comp-transform`, `comp-cache`, `comp-types`, `comp-tooltip`.
- **Org/meta:** `comp-state`, `comp-registry`, `comp-coverage`, `comp-shell`, `comp-honesty`,
  `comp-fedobs`, `comp-learns-status`, `comp-learns-score`, `comp-tool-health`, `comp-system`,
  `comp-genesis`, `comp-ontolint`.

Partition check: 16 + 10 + 43 = 69. EXHAUSTIVE over tools_index; the 18 excluded executables are
out of scope by construction (gates + primitives, not graph-query tools).

**First-pass consolidation surface: 26 of 69 tools (A+B).** The PRD's job is NOT to merge 26
tools into 2 binaries — it is TYPED DISPATCH over the existing engines (banked constraint #1),
i.e. one navigation surface + one drill surface that ROUTE to these engines, with each engine's
declared limitations riding the output (banked constraint #3).

## 3. Existing substrate the design lands on (this is further along than the direction assumed)

1. **The stable-grain contract is already ratified law** (CTO reconciliation, ratified
   2026-06-30T20:52Z; `comp-coverage-map.yaml:130-171` + grain_contract): grain is a DECLARED
   ATTRIBUTE (`level`) on a stable edge/node type, never a per-depth re-typing; ONE CONTAINS
   ladder; drilldown_seams cross the resource<->compute<->object strata via stable
   RUNS/CONTAINS/OWNED_BY edges. **Andrew's two-grain model is the TOOL-SURFACE expression of
   this already-ratified graph model.**
2. **The compute CONTAINS ladder is declared:** container (`pipeline:<firm>:<tier>`) -> file
   (script) -> function (`comp-coverage-map.yaml:319-330`). Grain-1 navigation bottoms onto
   grain-2 drill exactly at the `file` level of this ladder.
3. **`comp-depth` already implements the grain coordinate** (NFRA_GRAPHDEPTH P3): grains/scope/
   drill/rollup/blast-at-grain over the marker-head graph, grain-calibrated by grain_contract.
   The Grain-1 surface likely COMPOSES comp-depth + comp-trace/blast + comp-estate rather than
   being new.
4. **A per-tool grain/plane vocabulary exists and is gate-checked** (stage-2 vocab invariant,
   23/69 declared; `comp-output-contracts.yaml`). The consolidation can REQUIRE the declaration
   for every A+B tool — turning the 49-pending backlog into a scoped, motivated worklist.

## 4. The COVERAGE universe — what the consolidated surface can actually see (the audit's second axis)

A consolidated surface inherits every engine's universe, and today those universes are unequal
and partly undeclared:

- **comp-pipescript models 4 of 10 trees, undeclared** (dial SEV-HIGH F2, @7900435cbe). The
  UNIVERSE NAMING ACT IS AT ANDREW — this audit carries it forward as the program's first
  sovereign dependency. A Grain-2 drill that silently answers from a 4-of-10 universe reproduces
  the F1/F2 false-clean class at consolidation scale.
- **Producer plane and serve plane are DISJOINT sub-graphs** — 0 cross edges population-wide,
  0 at 2-hop (CVO assessment @655e3f5513, Andrew-directed via ~B @29ce04be87: the estate models
  served artifacts TWICE under two identities that never reference each other). Grain-1
  navigation MUST either bridge or loudly declare this seam (banked constraint #2:
  topology-vs-applied plane discipline); fixes routed census-layer + 2 honest comp-blast edits.
- **Declared grain gaps** (`comp-coverage-map.yaml:552-554`): container grain has NO dedicated
  tool (comp-aws is resource-grain) [medium]; statement grain none [low, bounded-materialization];
  **the entire MS-CLOUD surface has no comp-tool at ANY grain** [high].
- **json/ tier gap:** the F1 signature is invisible at the json tier (same CVO assessment) —
  named residual for the PRD's plane model.

## 5. Banked PRD constraints (carried from the 2026-08-04 dial close + design direction)

1. **Typed dispatch over existing engines** — no engine rewrites; the two surfaces route.
2. **Topology-vs-applied plane discipline** — a graph answer (DESIRED/topology) is never
   presented as an applied/live answer; plane labeled on every output.
3. **Declared limitations ride the drill** — each engine's known blindnesses (per-tool dial
   findings) print with its answers, not in a doc nobody reads.
4. (This audit adds:) **Universe declarations are load-bearing** — every A+B engine declares its
   tree/plane/surface universe before the consolidated surface routes to it; undeclared =
   unroutable. Grounded by F2 and by comp-estate's fail-loud header contract as the reference
   implementation.

## 6. What feeds the next step (dial program as inventory — CVO lane)

- CVO's dial queue next subject: **comp-blast re-dial incl. the two honesty edits on landing**
  (CVO start-gated on the same Andrew word; their 130231Z relay).
- Dial priority from this audit's partition [CTO recommendation, CVO's lane to sequence]:
  the A-list core (trace/blast/depth/estate/kuzu) + the B-list archetype (pipescript, closed
  2026-08-04) cover the consolidation surface's spine; C-list tools need no dial for THIS
  program.
- ~B's checker-class harvest (predicate: live + killed-but-git-preserved) remains a named input
  to the universe axis when it lands.

## 7. Residuals / open items on this audit

- The **"something else"** in Andrew's start word (second Next-Steps item at the CVO terminal) is
  UNRESOLVED — CVO clarifying with Andrew; this audit does not guess at it.
- Rows marked [INFERRED] in §2 await dial-grade confirmation; contested rows: comp-similar,
  comp-xref, comp-toolgraph (A vs C), comp-validate, comp-freshness, the comp-iam service split
  (B vs C).
- The F2 universe naming act (at Andrew) and the ms-cloud surface gap (high) are the two
  coverage-universe items that shape PRD scope hardest.

## R-1 — CTO RULING (2026-08-04 ~13:2xZ): comp-pipescript is ABSORBED, not retired

**Trigger:** Andrew at the COO terminal ~1314Z (record @ea609ab28), verbatim: *"…we are about to
make two layer grain broad and deep search, and may no longer need com-pipescript when we're done
here"* / *"unless comp-pipescript becomes the script-grain and comp-trace becomes the node-grain
(deep, and broad, respectively) of the two-grain initiative"*. COO held the staged F1/F9 GOs
(@606d3d1f4) and routed the absorption question here as umbrella owner.

**Ruling:** Andrew's second sentence IS the design of record — it restates his own 06:3xZ design
direction (@6b6e68455d: *"a broader, node 'comp-trace' style tool for nodes… then at any given
node with executable code they can go to 'comp-pipescript' code level"*) and this audit's
partition (§2.B: comp-pipescript = the Grain-2 archetype). Under banked constraint #1 (typed
dispatch over EXISTING engines — the surfaces route, they do not rewrite):

- **The ENGINE survives as the script-grain (deep) of the two-grain surface.** comp-trace-class
  navigation is the node-grain (broad).
- **What may retire at consolidation is the standalone SURFACE** — the separately-learned
  13-subcommand entry point folds into the Grain-2 face. That is a routing change, not an engine
  retirement.
- **Therefore F1/F9 are investments in the surviving engine — COO fires the GOs.** Reinforcing,
  independent of the future: the F1 double-false-clean is LIVE today on the $22M-class ad-hoc-run
  guard, and comp-pipescript remains that guard through any interim — the hold traded a live
  hazard against at most two files of build waste.

**Boundaries:** this ruling does not pre-decide MDPF_CANRTE fork F-3 (consistent either way —
both want the engine healthy, and C-2 there already carries the cross-tree blindness fix), and
does not touch the F2 universe naming act (at Andrew).

**SOVEREIGN-RATIFIED ~1347Z (CVO terminal, record @b80bbaab7), verbatim:** *"I thought about it
and I like the idea of comp-trace for breadth, comp-pipescript for script io/detail, because
there may be other script-level grain tools for non-executables so probably makes more sense to
keep that segmented and that way we dont have to do renames."* Consequences absorbed into the
PRD frame: both tools KEPT under their names (no-renames extends banked constraint #1 into a
NAMING constraint); **Grain-2 is a SEGMENTED FAMILY, not a monolithic drill** — §2.B becomes an
open family with comp-pipescript as first member, with room for script-level tools over
NON-EXECUTABLES (his stated reason).

## Compiler Tools (this audit's evidence)

| tool / probe | result | use |
|---|---|---|
| `comp-manifest-check completeness` | PASS, 87=69+18 accounted, contracts 20+49, vocab 23 | §1 denominator (gate-maintained, run this session) |
| `graph-call-manifest.yaml` tools_index read (:1439-1511) | 69 rows enumerated | §2 partition basis |
| `comp-coverage-map.yaml` grain rows (:130-171, :319-330, :552-554, :831) | grain_contract + ladder + gaps + comp-depth concern | §3/§4 substrate + coverage gaps |
| CVO records @6b6e68455d @74451794ee @7900435cbe @655e3f5513 (git show) | verbatim + dial + seam grounding | §0/§4/§5 anchors |
