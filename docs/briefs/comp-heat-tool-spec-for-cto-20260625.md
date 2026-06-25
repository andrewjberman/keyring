# comp-heat -- comp-tool spec (NFRA_HEATMAP_OBJECT surface) -> CTO for registry implementation

**Author:** 0.4.0_DS_ClientPlatform - **For:** 1.0.0_SA_CTO (comp-tool registry owner)
- **Date:** 2026-06-25 - **Andrew-direct:** "make sure there is a comp-tool associated with these
functions; spec it + send to CTO for implementation in the comp-tool registry."

## Why a comp-tool (the rail principle)

"What's stale / safe to archive?", "what have I written that isn't committed?", "is this code
committed-but-undeployed?" are **estate-cognition** questions. Per Rule 21 they should route
through a relationship-aware tool, NOT raw `git status` / `git log --name-only` / `find -mtime`
(text-local, connection-blind). `comp-heat` is the canonical surface over the NFRA_HEATMAP_OBJECT
engine (Strand-C of NFRA_EXPAND).

## Backing engine (already built; commit pending a lane grant)

`org/modules/heatmap/` (0.4.0_DS, NFRA_EXPAND Strand-C S0+O1):
- **`heat_map.py` (S0)** -- shared primitive: `recency_score` (exp-decay), `classify_band`
  (hot/warm/cold), `score_items(items, now_ts, HeatParams)`, `cluster_by_locality(scores,
  locality_fn)`, `summarize`. Pure lib, deterministic, domain-parameterized via `HeatParams`.
- **`object_freshness.py` (O1)** -- `build(root, p, now_ts)` (git-history tracked + mtime
  untracked -> per-path heat), `uncommitted_writes(root, now_ts)` (writes-not-in-commit drift),
  and a CLI (`--top/--half-life/--json/--drift`).
- NOTE: the module commit is blocked on the `org/modules/` ANY_EXEC owned-paths grant (RAVC'd to
  COO 2026-06-25). comp-heat implementation should land AFTER the module is committed.

## Proposed CLI surface

`comp-heat <subcommand> [args]` -- a thin `.tools/comp-heat` wrapper over the O1 engine
(read-only; ADVISORY-ONLY).

| Subcommand | Maps to | Answers |
|---|---|---|
| `comp-heat freshness [path] [--half-life N] [--json]` | O1 `build` + freshness report | per-path hot/warm/cold + ranked COLD SUBTREES = archive candidates ("what's dead/stale here?") |
| `comp-heat drift [--json]` | O1 `uncommitted_writes` | WRITES NOT IN A COMMIT (untracked + modified working-tree, freshest-first) -- the local->git layer ("what have I written that isn't committed?") |
| `comp-heat score <id> --age-days N [--half-life N]` | S0 `score_item` | ad-hoc heat score for one item (diagnostic / for other tools to import S0) |

**Composition (do NOT duplicate):** the GIT->DEPLOY drift layer (committed code whose served
artifact is older = undeployed) is already `comp-pipescript deployed` (MATCH/STALE/MISSING) +
`comp-freshness`. `comp-heat drift` covers LOCAL->GIT only; the help text should cross-reference
the deploy-layer tools so the two hops are discoverable together.

**Name note:** distinct from the existing `comp-freshness` (that is DATA-PIPELINE freshness --
S3/DDB chain/artifact staleness for gold runs). `comp-heat` is REPO/ESTATE OBJECT write-freshness
+ hygiene. Keep them separate; cross-link in both help texts.

## Registry changes requested (CTO to implement)

1. **`.tools/comp-heat`** -- the CLI wrapper (Git-Bash 3.6.7-safe per Rule 16; PATH-installed),
   shelling `python org/modules/heatmap/object_freshness.py` with the subcommand mapping above.
2. **`org/modules/graph/graph-call-manifest.yaml`** -- a `tools_index` entry + situation->command
   rows: "what's stale/safe to archive?" -> `comp-heat freshness`; "what have I written that isn't
   committed?" -> `comp-heat drift`.
3. **`org/modules/graph/comp-tools.yaml`** -- a `comp-heat` block with `use_cases` (the table above).
4. **comp-which routing** -- NL phrases ("stale files", "dead directories", "archive candidates",
   "uncommitted changes", "writes not committed", "repo hygiene", "what's cold") -> `comp-heat`.
5. **NFRA_TOOLHUD nudge** -- a raw Bash `git status` / `git log --name-only` / `find ... -mtime` /
   `ls -t` used for STALENESS/archive/uncommitted intent -> nudge to `comp-heat` (advisory, like
   the existing aws/grep nudges; operational git stays free).

## Guardrails (carry into the tool)

- **ADVISORY-ONLY** -- comp-heat SCORES/CLUSTERS/FLAGS; it never recommends-to-delete (that's O3,
  separately guardrailed) and never auto-acts. Inherits the NFRA_DEBTSCAN never-auto-delete +
  blast-radius verify-before-recommend doctrine.
- **Read-only** -- no writes to the repo or any store; the snapshot is derived-on-demand from git
  (git IS the write-history), not a new persisted store.

## Sequencing

Build-order: org/modules/heatmap/ commits (COO lane grant) -> `.tools/comp-heat` wrapper + registry
entries (CTO) -> comp-which/HUD wiring (CTO). O2-O4 (clustering/recommendation/report) extend the
engine later; comp-heat subcommands grow with them (e.g. `comp-heat recommend` at O3, still advisory).

RAVC: ping 0.4.0_DS on registry-landed so I verify the routing + the engine wiring end-to-end.
