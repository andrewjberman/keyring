# NFRA_HEATMAP (macro) -- the shared write-activity/freshness analytic

ONE heat_map analytic, applied to two domains (`docs/architecture/NFRA_HEATMAP_SCOPING.md`):
OBJECTS (repo/estate files) and PROCESSES (OPLMCP UoW traffic). Strand-C of NFRA_EXPAND.

| Leg | File | What |
|---|---|---|
| **S0** | `heat_map.py` | the shared primitive -- recency scoring + exponential decay + locality clustering, domain-parameterized (`HeatParams`). Pure library, no I/O. Both object + process legs import it. |
| **O1** | `object_freshness.py` | write-freshness engine (OBJECT half): git-history (tracked) + mtime (untracked) -> per-path hot/warm/cold; cold-subtree detection. Derived from git, NOT a new store. |
| **O2** | `object_locality.py` | filesystem-locality clustering -- rolls O1 heat up the dir hierarchy; finds MAXIMAL cold subtrees (highest dir whose whole subtree is >=90% cold). Native tree-rollup. 20k files -> 223 maximal cold subtrees. |
| **O3** | `object_recommend.py` | archive RECOMMENDATION layer (the GUARDRAIL) -- **ADVISORY-ONLY**. verify-BEFORE-recommend: name-vs-edge git-grep inbound-ref check (auto) + comp-blast graph-dependents gate (cited mandatory). Conservative: any ref -> HOLD. NEVER acts. Live: top-12 cold subtrees = 0 recommend / 12 HOLD (all referenced). |
| **O4** | `object_report.py` | hygiene report surface -- renders O3 into a human-facing report (markdown), splitting RECOMMENDs into ORPHANED-archive vs AUDIT-TRAIL (logs; retention=policy call) vs HELD(ref'd). `--from-json` renders a prior O3 scan fast. ADVISORY-ONLY. |

## Usage

```bash
# freshness report (coldest paths + cold subtrees = archive candidates)
python org/modules/heatmap/object_freshness.py --root . --top 25 [--json snap.json] [--half-life 30]

# DRIFT: writes NOT connected to a commit -- untracked + modified working-tree (Andrew 2026-06-25)
python org/modules/heatmap/object_freshness.py --drift --top 25 [--json drift.json]
```

## Drift = "writes that didn't propagate" (two layers)

A WRITE with no downstream event is a hygiene/risk signal -- the inverse of cold (hot-but-orphaned):

1. **LOCAL -> GIT** (built, O1 `--drift` / `uncommitted_writes()`): a filesystem edit / new file on
   disk that is not in any commit (untracked, or tracked-but-modified). Ranked by mtime recency.
2. **GIT -> DEPLOY** (composes, not duplicated): a committed code change whose served artifact is
   older = an undeployed change. Use `comp-pipescript deployed` (MATCH/STALE/MISSING) + `comp-freshness`.

## Public API contract (the single surface; 3 consumers)

`object_freshness.py` is THE canonical O1 engine (COO-ruled, dac519c88). Three consumers build
against this stable surface -- NO re-implementation / parallel git-walk:
0.5.0_AE's producer/emitter - `comp-heat` (CTO) - my own O2/O3.

```
# S0  (heat_map.py) -- the scoring primitive
HeatParams(half_life_days=30.0, hot_days=7.0, warm_days=30.0, freq_weight=0.0)
score_items(items: Iterable[(id, last_ts_epoch[, freq])], now_ts: float, p=HeatParams) -> [HeatScore]
score_item(item_id, age_days, frequency=1, p=HeatParams) -> HeatScore
cluster_by_locality(scores, locality_fn) -> {key: {n, n_cold, cold_frac, mean_score, oldest_age_days, items}}
summarize(scores) -> {n, bands{hot,warm,cold}, cold_frac, mean_score}
HeatScore = {item_id, age_days, recency_score, frequency, score, band}

# O1  (object_freshness.py) -- the engine
tracked_last_write(root) -> {path: last_commit_epoch}    # one `git log --name-only --no-renames` pass
untracked_mtime(root)    -> {path: mtime_epoch}           # `git ls-files --others --exclude-standard`
uncommitted_writes(root, now_ts) -> [{path, class(untracked|modified), status, mtime_age_days}]
build(root, p: HeatParams, now_ts) -> (scores: [HeatScore], src: {path: 'git'|'mtime'})
```

**Snapshot schema** (the `--json` emit; what producers/consumers read):
`{generated_ts, root, half_life_days, summary, paths:[{path, age_days, score, band, source}],
cold_subtrees:[{dir, n, n_cold, cold_frac, oldest_age_days, items}]}`.

## Canonical estate universe (GROUNDED, COO-pinned 2026-06-25)

The hygiene universe is **git-respecting**: tracked (`git ls-files`) + untracked-not-ignored
(`--others --exclude-standard`) = **~20,085 files** (CURRENT tree). This is deliberate, not a gap.
Two distinct over-count mechanisms were ruled out (grounded; do not conflate -- Rule 22):

- **DELETED-HISTORICAL ghosts (the actual parallel-walk overcount, 0.5.0-authoritative):** a
  `git log --name-only` walk lists EVERY path ever committed -- 20,030 current + 28,721 deleted =
  ~48.8k. That is git-LOG history, not the filesystem. `build()` excludes these by filtering
  `line in (git ls-files)` and now asserts it (the ghost-guard). This was the real source of the
  20k-vs-48.8k delta.
- **Gitignored filesystem slop (a separate true fact, NOT the parallel overcount):** the full
  on-disk tree is ~226,623 files; the bulk over git-tracked is gitignored + regenerable
  (`.runtmp/*/node_modules` ~136K, build artifacts, caches). `.gitignore` governs these; they are
  not authored estate. This is a REASON the hygiene universe is git-respecting (a raw filesystem
  walk would swamp the cold-subtree signal) -- but it was not what inflated the parallel walk.
- **Submodules** (`portal/`): `git ls-files` lists the submodule POINTER, not its contents -- so
  portal's files are excluded. A `git log` of the superproject does NOT descend into a submodule
  either, so this reach was in NEITHER engine. It is a genuine FRESH enhancement on its own merit
  (portal = real authored estate): a future opt-in `--include-submodules` folds a submodule's own
  git-walk in (its `.gitignore` honored) as a separate sub-estate. (COO GO 2026-06-25, post-converge.)

## Guardrails

- **ADVISORY-ONLY.** This module SCORES, CLUSTERS, and FLAGS. It never recommends-to-delete (that
  is O3, guardrailed) and never auto-acts. Inherits the NFRA_DEBTSCAN never-auto-delete doctrine.
- S0 is deterministic (caller passes `now_ts`); O1 reads git/fs read-only.

Owner: 0.4.0_DS_ClientPlatform (S0 + O1). Lane: Strand-C-local (+ 0.5.0_AE producer/infra half).
