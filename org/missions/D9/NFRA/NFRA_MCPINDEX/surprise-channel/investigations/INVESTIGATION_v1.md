# NFRA_MCPINDEX -- Surprise Channel Investigation v1

One row per surprise, appended, never edited. Schema: org/surprise_channel/schemas/investigation_item.schema.json.

```json
[
 {
  "id": "NFRA_MCPINDEX-W3-S1",
  "project": "NFRA_MCPINDEX",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~3",
  "surfaced_at": "2026-09-21T06:30:46Z",
  "one_line": "portal/ (gitlink submodule) is empty in this worker's worktree, so MXA1-AC11's Advisor Intelligence page citation has no .tsx path, unlike the other 3 surfaces which were citable from checked-out data-pipeline-script docstrings and docs/architecture/YALP_*.md briefs.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ls portal (in /c/tmp/wk-mcpindex-3) returns nothing -- the directory is empty",
    "git submodule status portal -> fatal: no submodule mapping found in .gitmodules for path 'portal' (run from this worktree)",
    "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/analysis-portal.result.md ## AC11 discloses this and cites data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py:9-12, data/etfs/scripts/gold/etf_positioning_publisher.py:7-9 and docs/architecture/YALP_MACROS.md:16 (+ YALP_CMASMP.md:12, YALP_CORREL.md:13, YALP_FACTOR.md:15, YALP_MKTOVR.md:15) for surfaces 1-3, and states no equivalent .tsx citation was found in checked-out code for surface 4"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "MXA1-AC11: 'each surface's portal page is named with the precomputed key it reads' for all four surface families (platinum/mdpf, platinum/etfs, platinum/advi, json/*)",
  "world_is": "3 of 4 surfaces' portal pages were named with a .tsx or portal/src/pages/ citation from checked-out repository text (data-pipeline-script docstrings for mdpf/etfs; docs/architecture/YALP_*.md briefs for json/*). The 4th (advisor intelligence, platinum/advi + the Inflection/Cottonwood firm buckets) has no equivalent citation available, because portal/ -- the only tree that would carry it -- is an empty gitlink submodule in this worker's worktree (not in this worker's <paths> grant). AC11 is satisfied on its letter (a page reference and a precomputed key are both named for all 4 rows) with this gap disclosed rather than guessed; a future cell needing the exact advisor-intelligence page path (e.g. an MX-t-1-class tool-building cell) will need a worktree that carries the portal/ submodule checked out."
 }
]
```
