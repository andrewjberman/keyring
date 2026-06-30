# NFRA_COMPDRIFT — Macro-Project Brief

**A first-class, estate-wide drift compiler that owns the canonical propagation topology.**

- **Type:** macro_project (`NFRA_COMPDRIFT`)
- **Origin:** Andrew-direct 2026-06-29 (live design session with MSTR). Andrew's framing, verbatim intent:
  *"comp-drift is too important of a function to be relegated as a side function of another script — it
  really should be its own thing, and we really assess where the drift points are expected, i.e., between
  local to git to cloud to kuzu/nessie to iceberg, etc."* Plus: *"And of course Trino now that we're making
  that federated surface."*
- **Author:** 0.0.0_AB_MSTR (scope) | **Issued to:** 1.0.0_SA_CTO (PRD authoring + arch-gate + TO decomposition)
- **Build lane (recommended):** 0.7.0_AE_CloudOps (+~B — owns `comp-lambdamap`/`classify_reconcile` engine) | **Verify:** 3.0.0_SA_CVO
- **Status:** brief → CTO PRD. Register the macro on PRD landing (Andrew blessed the `NFRA_COMPDRIFT` macro name).

---

## 1. The problem — drift is real but ownerless

Drift detection in this estate is **scattered as side-functions across whatever tool happened to own one
seam.** Today we have, in pieces:

| Existing tool | Drift class it owns | Seam |
|---|---|---|
| `comp-heat drift` | uncommitted writes (untracked + modified) | LOCAL → GIT |
| `comp-pipescript deployed` | local script vs deployed S3 ETag | GIT → CLOUD (scripts) |
| `comp-lambdamap parity` (CVO spec 2026-06-29; engine `classify_reconcile` exists) | source-map ↔ live CodeSha256 ↔ S3-artifact sha (3-leg) | GIT → CLOUD (Lambda) |
| `comp-iam reconcile` | TF-desired vs live-AWS IAM | IaC → CLOUD (IAM) |
| `comp-registry sync` | REGISTRY ↔ JSON ↔ PRD narrative | record ↔ record |
| `comp-transform schema-check` | adapter contract vs live S3 envelope | component → SERVED data |
| `comp-freshness` | S3/DDB artifact + chain staleness | producer → SERVED |
| `comp-incrparity` (built) | full-rebuild vs incremental gold parity | data-correctness |
| `comp-parity` (DATA_SSOTMG TO-4) | canonical-build vs BD-served | DATA parity (cutover gate) |
| `drift_producer.py` (NFRA_INFRPT.P1) | repo/infra checks → `drift_state.json` for the infra-monitor Lambda | infra-dashboard producer |

**The symptom of the fragmentation:** CTO had to run a naming-disambiguation arch-gate on 2026-06-29 just to
keep three different "parity" concepts from being conflated. Drift is a **cross-cutting property of the whole
propagation chain**, but nothing owns the chain. The consequences:

1. **No coverage map.** Nobody can answer "is the *entire* estate in parity, end-to-end, right now?" — only
   "is this one seam OK." Hops with **no checker at all** are invisible (you can't see the gap you have no
   tool for).
2. **Inconsistent semantics.** Each tool invented its own verdicts and exit codes. STALE-RECORD vs
   HALF-LANDED vs BEHIND vs UNVERIFIABLE mean different operator actions, but there's no shared schema.
3. **Retrofit, always.** Every checker was bolted on *after* its seam already existed — so each one was an
   audit, never a design input.

## 2. The thesis — comp-drift owns the propagation topology

`comp-drift` is **not** an aggregator that loosely wraps the tools above. It is a **first-class tool that owns
a declared propagation topology** — the canonical sequence of stores an artifact flows through — and enforces
the single invariant that **each hop must be in parity with the stage before it.**

- The existing seam-checkers become **engines `comp-drift` calls** to evaluate individual hops. It does NOT
  re-implement their boto/parse/read logic (the same "don't duplicate the engine" lesson the
  `comp-lambdamap parity` spec already learned).
- The **new, first-class thing** `comp-drift` introduces is the **topology map + the coverage ledger + a
  normalized cross-seam drift-record.** That is the deliverable that does not exist today and is the entire
  point of the project.

## 3. The canonical propagation topology

The chain Andrew named, made explicit. Each row = a STAGE (a store); each `│ seam-N` = an expected-equality
invariant between adjacent stages, plus the engine that checks it (or `GAP` where none exists today —
**surfacing these gaps is the highest-value early output**).

```
STAGE          the store                                  seam invariant (the expected-equality)      engine / status
─────          ─────────                                  ──────────────────────────────────────      ───────────────
LOCAL          working tree (scripts / .tf / src)
   │  seam-1   every commit-worthy write is committed                                                 comp-heat drift            [COVERED]
GIT            CLOUD / DEV / PROD committed
   │  seam-2   deployed artifact == committed source      (scripts)                                   comp-pipescript deployed   [COVERED]
   │                                                       (Lambda 3-leg sha)                          comp-lambdamap parity      [COVERED*]
   │                                                       (TF IAM → live)                             comp-iam reconcile         [COVERED]
CLOUD          S3 artifacts / Lambda / EC2 code / DDB config
   │  seam-3   the graph reflects the LIVE estate                                                     globgrph derive marker-    [PARTIAL]
NESSIE         canonical versioned graph (CloudNode/Edge = SSOT)                                       oracle (comp-kuzu header)
   │  seam-4   query DB == latest Nessie HEAD                                                          comp-kuzu HEAD-advance     [SELF-HEAL,
KUZU           query surface (the estate read model)                                                  auto-refresh                NOT ASSERTED]
   │  seam-5   lakehouse tables == canonical parquet / graph source                                   ???                        [GAP]
ICEBERG        lakehouse tables (aws / portal / ms / pipeline assets)
   │  seam-6   Trino catalog binding == backing source schema (PER federated catalog)                 ???                        [GAP — design IN]
TRINO          FEDERATED query surface (the unified heat_map / analytics; fan-in)
   │  seam-7   served heat view == Trino federation result                                            comp-freshness + heat-view [PARTIAL]
SERVED         platinum/firm JSON → portal CDN / heat_map / dashboards
```

`*` `comp-lambdamap parity` is spec-complete with the engine live; the read-surface promotion is in flight.

**The coverage ledger falls straight out of this table.** Authoring the topology *forces* the question Andrew
asked — "where are the drift points expected?" — and immediately exposes the **uncovered seams**: seam-5
(Iceberg vs canonical source) and seam-6 (Trino catalog vs backing) have no checker today, and seam-3/4/7 are
partial or self-healing-but-unasserted. Those gaps are invisible right now *precisely because* drift lives as
side-functions. The first deliverable below turns "we think it's fine" into "this seam has no checker — that
is a finding."

## 4. Trino — the fan-in federation special case (Andrew-flagged)

> **[CORRECTION 2026-06-30, COO~B grounding]** The "4 iceberg catalogs (aws/portal/ms/pipeline)" framing
> below is a LAYER-vs-TABLE mismap. Ground truth (memory `project_trino_federation_layer_live`, verified
> the 2026-06-29 federation build; aligns CTO fix `adc20b328`): aws/portal/ms are a `layer` COLUMN on a
> SINGLE `graph_nodes` table — 3 physical iceberg tables total (`graph_nodes`/`graph_edges`/`graph_contracts`).
> The live Trino fan-in is 2 catalogs (iceberg + code_heat), soon 3 (+ tool_activity), NOT N per-layer
> catalogs. Model the fan-in + the topology manifest on PHYSICAL catalogs so it carries no phantom per-layer
> seams. (Fully corrected at COMPDRIFT-PRD time.) Related: the §4.3 "design-in window" is largely already
> USED — the 06-29 federation shipped with seam-6 parity (code_heat_parity) — so this is less time-pressured
> than framed below; COMPUNIFY-schema-first sequencing stands.

Trino is **not a linear hop** like the others, and that changes how `comp-drift` must model it:

1. **Fan-in, not a single seam.** Kuzu has one backing store (Nessie); Trino **federates many** — the Iceberg
   assets (aws / portal / ms / pipeline) **plus the git-native code-heat, which is read live and never
   materialized.** So Trino's drift check is a **per-catalog sweep**: each federated source is its own parity
   edge into Trino, each independently `MATCH / STALE / UNVERIFIABLE`. The git-code-heat binding is a special
   case — a live-read, so its "freshness" is a HEAD-pointer check, not a table-schema check. The topology
   manifest models Trino as a **node with multiple inbound seams.**
2. **Federations drift silently at the binding layer.** A backing Iceberg table can re-partition or
   schema-evolve and Trino keeps serving against a stale catalog definition with no error — just wrong or
   missing columns. This is the `comp-transform schema-check` failure mode (adapter↔envelope) generalized to
   **every federated catalog.** comp-drift's Trino engine is conceptually "schema-check, per federated
   catalog."
3. **Design-in, not retrofit — the leverage point.** The heat-federation (Trino over Iceberg) is being
   **built this session** (NFRA_GLOBGRPH heat design + NFRA_EXPAND, both arch-gated, not yet materialized).
   The reason the existing drift tools are scattered is that every checker was bolted on *after* its seam
   existed. **Trino is the one hop we can do right the first time.** Make "every federated catalog emits a
   checkable parity signal" an **acceptance criterion of the heat-federation build itself**, so seam-6/seam-7
   ship `COVERED` rather than landing in the manifest as another `GAP`. This is the single strongest reason to
   commission NFRA_COMPDRIFT **now** rather than after the federation lands: the topology manifest becomes a
   **design input** to in-flight work instead of an audit three weeks late.

## 5. Design principles (carry into the PRD)

1. **Orchestrator, never re-implementation.** comp-drift calls the existing engines (`comp-heat`,
   `comp-lambdamap parity`, comp-kuzu's oracle, comp-freshness, schema-check, etc.). The novelty is
   topology + normalization, not new check logic. Precedent already in-repo: `drift_producer.py` runs
   comp-manifest-check + comp-surface-check + tf-plan and writes one `drift_state.json` — comp-drift
   **generalizes that pattern to the whole chain.**
2. **Normalized drift-record + tri-state exit** (adopt the `comp-lambdamap parity` contract wholesale — it is
   the right model): per hop → `{stage_from, stage_to, target, verdict, severity, operator_action}`.
   - **exit 0** = clean / dispositioned (incl. STALE-but-consistent).
   - **exit 1** = true integrity break (half-landed, deployed ≠ committed, schema mismatch).
   - **exit 2** = UNVERIFIABLE (could-not-read the seam) — a FINDING, kept SEPARABLE from "broken."
3. **NEVER silently MATCH a seam you couldn't actually read.** An uncheckable hop is `UNVERIFIABLE`, never
   folded into "clean." This is the exact false-clean class killed in the to-check parser on 2026-06-29
   (a status parser that mis-rendered done-as-active, and earlier the [??]-misread orphans) — generalize the
   lesson: **errs toward false-OPEN / surfaced, never false-CLOSE / hidden.**
4. **Per-hop verdicts stay DISTINCT.** comp-drift must NOT collapse STALE-RECORD, HALF-LANDED, BEHIND, and
   SCHEMA-DRIFT into one "DRIFT" — the operator response differs per hop (reconcile the record vs investigate
   a deploy vs wait-for-self-heal vs refresh a catalog). It carries the seam-specific verdict through; the
   topology is what makes them comparable WITHOUT conflating them.
5. **Cost-guard.** Cheap checks first (local diff, sha compare — no network), then network/S3-head/catalog
   reads only on the non-clean subset. Never head-object or full-catalog-scan the whole estate per run.
6. **Grounding discipline (CLAUDE.md Rule 22).** Each seam verdict cites its grounding (the live read it
   rests on). A could-not-verify is a finding, never a silent pass.

## 6. Management model

- **Deliverable #1 — the topology manifest** (`org/modules/graph/drift-topology.yaml`): every stage, every
  hop, the invariant, the engine that checks it (or `UNCOVERED`). This single file IS the spec AND the
  coverage ledger. Adding a store (a new custodian, a new graph layer, a new federated catalog) = one manifest
  entry; any uncovered hop is loud by construction. This deliverable alone — authored before any new check
  code — produces the "where are the drift points expected, and which are unguarded" map Andrew asked for.
- **Two surfaces:**
  - `comp-drift <target>` — walk one artifact's **full chain** (local → … → served): "did my gold script /
    my Lambda / my graph node actually propagate all the way, intact?"
  - `comp-drift sweep` — fan out across **every hop in the manifest** and render one unified board with the
    coverage line (how much of the chain the verdict actually covers).
- **comp-which-routable + NFRA_COMPRAIL on-rail.** Register in the tools_index so "is my estate in parity /
  where did X drift" routes to comp-drift.
- **CI mode.** `--json` + the tri-state exit for pipeline gates; a `sweep` can run as a standing
  estate-parity check (cost-guarded), the way `drift_producer.py` already feeds the infra-monitor.

## 7. Relationship to existing tools

comp-drift **subsumes the *orchestration and reporting*** of drift, not the per-seam engines. Concretely:
- The seam-checkers (`comp-heat`, `comp-lambdamap parity`, `comp-iam reconcile`, `comp-registry sync`,
  `comp-transform schema-check`, `comp-freshness`, `comp-incrparity`) **stay as-is** — they remain
  independently callable and keep owning their seam's logic. comp-drift calls them.
- `comp-parity` (DATA_SSOTMG data parity) and `comp-lambdamap parity` (deploy parity) remain distinctly
  named (per CTO's 2026-06-29 disambiguation); comp-drift *consumes* their verdicts as seam-2 / data-seam
  inputs, it does not rename or replace them.
- `drift_producer.py` is the existing baby-pattern; CTO to rule whether it folds under comp-drift as the
  infra-monitor's producer leg or stays a separate consumer of the same manifest.

## 8. Lane / governance / build path

This is a real tool-build and an Andrew-direct architectural macro — not an MSTR self-close. The path:
- **MSTR** — this brief (scope + topology + principles). Done.
- **CTO (1.0.0_SA_CTO)** — author the `NFRA_COMPDRIFT` PRD; stand up the macro project (JSON + REGISTRY);
  arch-gate the hard calls (below); decompose into TOs.
- **AE (0.7.0_AE_CloudOps + ~B)** — build (owns the `comp-lambdamap`/`classify_reconcile` engine + the
  cost-guarded read flows). Natural builder.
- **CVO (3.0.0_SA_CVO)** — verify each seam's read-surface against live (the way it co-verified the
  `comp-lambdamap sha` increment); ratify the never-false-clean / UNVERIFIABLE-honest contract.

**Cross-dependency (must be in the PRD):** NFRA_COMPDRIFT seam-6/seam-7 (Trino/Iceberg) carry a hard
dependency on the **live NFRA_GLOBGRPH heat-federation build.** The PRD must thread the "every federated
catalog emits a checkable parity signal" requirement as an **acceptance criterion on the heat-federation
work** so it ships covered, not retrofitted. Coordinate with the NFRA_GLOBGRPH/NFRA_EXPAND owners (CTO +
0.8.0_AE_CloudComp) before their federation materializes.

## 9. Suggested phasing (CTO refines)

- **P1 — the topology manifest + coverage ledger.** Author `drift-topology.yaml`; classify every seam
  COVERED / PARTIAL / SELF-HEAL / GAP against the existing engines. **Output = the estate drift coverage map**
  (the highest-value, lowest-cost deliverable; it tells us what's unguarded *today*).
- **P2 — the comp-drift orchestrator shell.** `comp-drift <target>` (full-chain walk) + `sweep`, calling the
  already-COVERED engines, normalized drift-record + tri-state exit + comp-which registration. No new check
  logic — pure orchestration over what exists.
- **P3 — close the GAP seams,** prioritized by the manifest: seam-5 (Iceberg vs canonical) and **seam-6
  (Trino per-catalog) co-designed INTO the heat-federation build** (the design-in window), seam-3/4/7
  hardened from PARTIAL/self-heal to asserted.
- **P4 — standing estate-parity sweep** (CI-gated, cost-guarded), folding `drift_producer.py`'s infra leg.

## 10. Asks to CTO

1. **Author the NFRA_COMPDRIFT PRD** from this brief; stand up the macro project (JSON + REGISTRY row).
2. **Arch-gate the hard calls:** (a) the topology-manifest schema + where it lives; (b) the
   orchestrator-vs-reimplementation boundary (confirm comp-drift never re-implements a seam engine);
   (c) the normalized drift-record schema + the tri-state CI contract; (d) the Trino fan-in model
   (node with N inbound catalog seams); (e) the cross-dependency mechanism that makes the Trino
   drift-signal an AC on the heat-federation build *before* it materializes.
3. **Decompose into TOs** along the phasing (or your refinement); assign build to AE, verify to CVO.
4. **Coordinate the cross-dependency** with the live NFRA_GLOBGRPH/heat-federation owners now, while their
   federated surface is still pre-materialization — this is the one-time design-in window.

---

*Brief authored 0.0.0_AB_MSTR 2026-06-29 (Andrew-direct). For 1.0.0_SA_CTO: PRD + arch-gate + TO decomposition.
Macro name NFRA_COMPDRIFT (Andrew-blessed). The core insight: drift is a property of the whole propagation
chain — local → git → cloud → nessie → kuzu → iceberg → trino → served — and deserves a first-class tool that
OWNS that topology, not a side-function of whatever script happened to touch one seam.*
