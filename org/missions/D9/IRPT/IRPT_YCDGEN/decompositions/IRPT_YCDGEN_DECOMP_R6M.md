# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM M: the resident package carries the Opal brand asset

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "M",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.10 @5a04dc8c4a)",
 "prd_version": "v0.10",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~G2",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6L.md",
 "cell_ids": ["YCD-w-6"]
}
```

**Why an addendum.** Row IRPT_YCDGEN-D2-S3: the seat-driven F1 run (2026-10-08 21:10Z, ledger irpt-ycdgen-f1-svc-20261008) reached the
resident on the Opal path and ended `retained_for_retry class=LayoutRefused`. The host root carries no brand spec or logo and the unit sets
neither IRPT_BRAND_SPEC nor IRPT_OPAL_LOGO; `layout_overview._asset_path` (lines 101-108) finds the asset only through git roots or those env
vars. Both assets are gitignored (`deck_generation/.gitignore:14-15`), so no build can package them. Every Opal-path Overview refuses,
Andrew's included. 1.0.0_SA_CTO~DELL2 ruling msg 1717: commit both assets under the resident tree, the packaged path tried first; the logo's
source of record is the laptop's logo package, committed byte-exact by the laptop.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-w-6` | resident render (the Opal page's brand) | `ycharts/research/brand/brand.json` (regenerated), `ycharts/research/layout_overview.py` (`_asset_path` packaged-first), one test | the laptop's logo commit at `ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg`, `deck_generation/scripts/03_extract_brand_spec.py`, the builder | the laptop's logo commit (named through 0.0.0_AB_MSTR~DELL2) |

All paths under `infra/aws/lambda/investor-reporting/`. **Writer read:** no non-terminal order of the project names these paths.

**Contract R21 The resident package renders the Opal page without a git checkout.** `load_brand()` resolves the spec and logo from
`ycharts/research/brand/` next to `layout_overview.py` before any git root or env var; the builder's `--research` packages both (tracked,
non-test); an Opal layout renders from a package extracted OUTSIDE any git repository with no brand env set. The after-read of the release
that ships it is one Opal-path layout rendering on the host (a separate never-widen pair, not this cell).

## Edges and fan-out

M = 1; dependency: the laptop's logo commit. fanout: 1 of 1 chain, cap 8, reason: one render-asset cell.

## Four-postulate record (Rule 24)

MECE: one asset resolution order (packaged, env, git roots). Same grain: one page's brand. Intent: one outcome (the host renders the Opal page).
State: the resolution order changes; no other layout behaviour moves; the YCharts path is untouched.

## Battery

comp-schedule and comp-iam DECLARED-NOT-APPLICABLE (no schedule, no grant). comp-adversary DECLARED-NOT-APPLICABLE (measured by row D2-S3
and ruled by the CTO, msg 1717).
