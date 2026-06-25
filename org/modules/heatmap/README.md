# NFRA_HEATMAP (macro) -- the shared write-activity/freshness analytic

ONE heat_map analytic, applied to two domains (`docs/architecture/NFRA_HEATMAP_SCOPING.md`):
OBJECTS (repo/estate files) and PROCESSES (OPLMCP UoW traffic). Strand-C of NFRA_EXPAND.

| Leg | File | What |
|---|---|---|
| **S0** | `heat_map.py` | the shared primitive -- recency scoring + exponential decay + locality clustering, domain-parameterized (`HeatParams`). Pure library, no I/O. Both object + process legs import it. |
| **O1** | `object_freshness.py` | write-freshness engine (OBJECT half): git-history (tracked) + mtime (untracked) -> per-path hot/warm/cold; cold-subtree detection. Derived from git, NOT a new store. |
| O2 | (next) | filesystem-locality clustering (cold-subtree archive signal; reuse comp-cluster/TSGRAPH). |
| O3 | (next) | archive/delete RECOMMENDATION layer -- **ADVISORY-ONLY**, inherit NFRA_DEBTSCAN never-auto-delete + blast-radius verify-before-recommend. |
| O4 | (next) | hygiene report/surface (ranked recs + evidence; human-reviewed). |

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

## Guardrails

- **ADVISORY-ONLY.** This module SCORES, CLUSTERS, and FLAGS. It never recommends-to-delete (that
  is O3, guardrailed) and never auto-acts. Inherits the NFRA_DEBTSCAN never-auto-delete doctrine.
- S0 is deterministic (caller passes `now_ts`); O1 reads git/fs read-only.

Owner: 0.4.0_DS_ClientPlatform (S0 + O1). Lane: Strand-C-local (+ 0.5.0_AE producer/infra half).
