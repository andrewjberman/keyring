# SERVABLE_PREFIXES -- `opal-data-harvest`, harvest V1 for asset managers (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~18:3xZ)

**For:** site Z's NFRA_MCPINDEX round (catalog rows) and NFRA_OPLGTW (the asset-manager research grant), through `0.0.0_AB_MSTR`. Cluster direction
`org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md` O3.

**The V1 rule** (cluster ruling, section 1.4 item 6; Andrew may widen it): serve DERIVED layers and article LINKS only, never raw publisher text.

**How this was read:**
- `aws s3api list-objects-v2 --bucket opal-data-harvest --delimiter /`, 2026-10-13 ~18:2xZ. **24 top-level prefixes, 24 classified below.**
- One more level was read for each prefix, and two levels for `amgt/`, `wsj/`, `publications/`, `publication-links/`, `social/`, `drafting/`, `lib/`, `scores/`
  and `bloomberg/`.
- **Claim:** each class is INFERRED from the prefix's name, its layer (bronze/silver/gold, v1) and the owning code's naming. No object's content was opened.
  Every SERVE row's first catalog act reads one object and confirms the class before the row is published.

## The 24 prefixes

| # | prefix | content (one level down) | class | V1 |
|---|---|---|---|---|
| 1 | `packs/` | one prefix per covered name (105 at the cluster read) | derived (the research pack) | **SERVE** |
| 2 | `scores/v1/` | per-name scores | derived | **SERVE** |
| 3 | `management/v1/` | management outputs (FWD-17 roster) | derived | **SERVE** |
| 4 | `filings/v1/` | filings analysis outputs | derived | **SERVE** |
| 5 | `posture/v1/` | posture judgments | derived | **SERVE** |
| 6 | `peers/v1/` | peer sets | derived | **SERVE** |
| 7 | `publication-links/v1/` | per-name article links (`BA/`, `COST/`, `HD/`, ...) | article links | **SERVE** |
| 8 | `amgt/harvest/gold/` | the gold chatter | derived | **SERVE** |
| 9 | `identity/v1/` | security identity | reference (lookup) | **SERVE** |
| 10 | `crosswalk/v1/` | the identity crosswalk | reference (lookup) | **SERVE** |
| 11 | `universe/v1/` | the covered universe | reference (lookup) | **SERVE** |
| 12 | `amgt/harvest/bronze/`, `amgt/harvest/silver/` | collected and normalised articles | raw publisher text | WITHHOLD |
| 13 | `amgt/harvest/state/` | harvester state | operational | WITHHOLD |
| 14 | `wsj/harvest/` (bronze, silver) | WSJ articles | raw publisher text | WITHHOLD |
| 15 | `barrons/harvest/` | Barron's articles | raw publisher text | WITHHOLD |
| 16 | `ft/harvest/` | FT articles (collection held on Andrew's word) | raw publisher text | WITHHOLD |
| 17 | `seeking-alpha/harvest/` | Seeking Alpha articles | raw publisher text | WITHHOLD |
| 18 | `issuer-site/harvest/` | issuer web pages | raw publisher text | WITHHOLD |
| 19 | `sec/harvest/` | SEC filing text | raw text (public domain) | WITHHOLD in V1. **The first widening candidate:** filings are public, so this is Andrew's word to widen |
| 20 | `publications/v1/` (`barrons/`, `bbg/`, `ft/`, `sa/`, `wsj/`) | per-publication article bodies | raw publisher text | WITHHOLD |
| 21 | `bloomberg/harvest/`, `raw/` (`raw/bloomberg/`, `raw/seekingalpha/`) | vendor responses as received | raw vendor data | WITHHOLD (Bloomberg's licence as well as the V1 rule) |
| 22 | `derived/` (`model_block/`, `model_block_fye/`) | the model block, from Bloomberg | derived from Bloomberg | WITHHOLD in V1: the Bloomberg licence's scope for redistribution to user Claude sessions is UNREAD. Andrew's call to open it |
| 23 | `drafting/v1/` | per-name JSON drafts (`ASML_NA_Equity.json`, ...) | UNREAD | WITHHOLD until one object is read and classed |
| 24 | `lib/local-publications/`, `social/v1/_measurement/` | a code library; a measurement folder only | not data | WITHHOLD |

**Count: 11 SERVE, 13 WITHHOLD (2 of them Andrew's calls to widen: rows 19 and 22).**

## The grant, as the V1 rule needs it

- Grant an asset-manager principal `s3:GetObject` on the 11 SERVE prefixes ONLY, as prefix conditions. No bucket-wide read, and no `ListBucket` outside those prefixes.
- **Negative arms (FWD of O3):**
  - the same principal is refused on a WITHHOLD prefix (`wsj/harvest/`);
  - a non-research principal is refused on `packs/`.
- Every catalog row names its prefix exactly as above. A new top-level prefix is WITHHOLD until classed here.

## Owners

- The list: AMGT_HARVST (`2.0.0_SA_COO~W1`), with AMGT_RESAPP for `packs/`.
- The catalog rows and the grant: site Z, NFRA_MCPINDEX and NFRA_OPLGTW, under `1.0.0_SA_CTO~Z`.

-- 1.0.0_SA_CTO~DELL1
