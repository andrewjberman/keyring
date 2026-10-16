# NFRA_MCPINDEX -- decomposition addendum, ROUND 18, workstream RESEARCH (2.0.0_SA_COO~MI2)

**archetype:** COORDINATE

Companion to `NFRA_MCPINDEX_DECOMP.md` (workstream ASSETS and the earlier rounds are `2.0.0_SA_COO~MI`'s there). One project, two index workstreams with disjoint row files (CLAUDE.md rule 27; PRD v0.17 @532d1e68bb). The pipeline gate keys the round on (workstream, round), so this issuer's round 18 is `RESEARCH` and does not collide with `ASSETS`. Spec-frozen once issued.

Source: PRD v0.17 addendum (CONTRACT C-GROUP; Andrew-direct ~18:4xZ and GO ~19:2xZ 2026-10-15, verbatim in the PRD), CTO msgs 34559 and 34580, the CTO round-17 analysis `ledger/ROUND_ANALYSIS.round17.md` @c7e130a7b2 (ruling 1: Z-C-S61 curated tags, each workstream on its own files), CRO plan `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_FINISH_PLAN_EOD_20261016.md` @6cc033c818, and the ASSETS issuer's round-18 cut `@257da358d8` (msg 34584: `MX-c-21` gives the emitter `bucket` on every row and `--group-map`, one emitter run at `MX-r-15` about 17:00Z 2026-10-16). Done by 2026-10-16 ~22:00Z: every in-scope row carries C-GROUP and a `read_tool` naming a live tool.

## R18-RES.1 MEASURED STATE (catalog v0.5 as committed at 5858411c5c; emitted `DATA_CATALOG.yaml`; rows from `workflows/atom_decomposition/catalog_entries/`)

The RESEARCH set is 180 emitted rows: 78 harvest, 5 `portal_datasets` and 97 silver (36 etfs, 7 mdpf, 3 news, 41 portal-v2, 10 dynamodb). Needs (35), tool_index (99), assets, bd, schwab and blackdiamond rows are not in it.

| item | measured | what C-GROUP / Z-C-S61 still needs |
|---|---|---|
| `bucket` present | harvest 78/78, etfs 36/36, mdpf 7/7, portal-v2 41/41, news 3/3 | nothing: already the S3 bucket name read from the row's own address |
| `bucket` prose or absent | 10 dynamodb rows carry prose; the 5 `portal_datasets` rows carry none | the ASSETS emitter (`MX-c-21`): DynamoDB wording becomes `dynamodb`; a `portal_datasets` row takes the catalog's `bucket`. Graded by the drain check `c30.DRAIN.sh` |
| `read_tool` present | harvest 78/78; etfs 7/36; portal-v2 16/41; mdpf 0/7 in silver (5 in portal_datasets); news 1/3; dynamodb 3/10 | see R18-RES.2 (`MX-c-31`, `MX-c-32`) |
| `nl_tags_basis: inferred` | 37 RESEARCH rows: 32 harvest, 5 `portal_datasets` (the other 7 inferred rows are ASSETS') | curated plain-words tags (`MX-c-34`..`-37`) |
| out of scope | 2 `platinum/advi/49financial/` rows (perfrp, twins); no row under `platinum/irpt/` | drop (`MX-c-30`) |

**Rulings recorded here (the issuer rules inside its own decomposition, rule 7):**
1. **Needs carry no `bucket`.** A need is a gap row (a question with an owner and a tool), not a dataset; the display groups tools. C-GROUP item 1 reads "catalog row and tool_index row"; the tool_index is `MX-c-21`. The CTO is told in the record, not asked.
2. **The third "advi/irpt" row the plan named ("1 mdpf row to re-check") stays.** The scope rule is by surface prefix: only `platinum/advi/` and `platinum/irpt/` drop. The two candidates (`opal_data_portal_v2_platinum_mdpf_cottonwood_account_units`, `..._mdpf_manifests_and_archive`) sit under `platinum/mdpf/`, the model-portfolio surface; the cell's record lists both with their prefix so the reading is checkable.
3. **This issuer does NOT touch the emitter.** The first draft of this cut carried a `bucket` function in the generator, a `portal_datasets` writer line in the emitter and a curated-tags loader (`MX-c-33`). The ASSETS issuer's `MX-c-21` ships all three in the emitter (`bucket` on every row, DynamoDB normalised, `--group-map` with `nl_tags` replacing the inferred ones), and asks that this workstream use it (msg 34584). Two writers of one function would collide at the merge, so `MX-c-33` was never cut, `MX-c-30` keeps only the scope drop, and the tag slices are written in that map's format.

## R18-RES.2 THE CELLS

| cell | what | write set | risk | serves | state |
|---|---|---|---|---|---|
| `MX-c-30` | The two advisor-intelligence rows out: a `scope_exclusions.json` the generator reads, so a regeneration does not bring them back; the two row files removed | `gen_silver_rows.py`, `scope_exclusions.json`, `catalog_entries/` (2 removed), `tests/` (1 new file) | LOCAL | FWD-22 | CUT this issuance |
| `MX-c-34` | Z-C-S61 data. Curated tags for harvest rows slice h1 (11 rows that carry `inferred`), one `--group-map` JSON | `deliverables/0.9.0_WK_NFRA_MCPINDEX~52/research_group_map_h1.json` | LOCAL | FWD-22 (Z-C-S61) | CUT this issuance |
| `MX-c-35` | Z-C-S61 data. Curated tags for harvest rows slice h2 (11 rows), one `--group-map` JSON | `deliverables/0.9.0_WK_NFRA_MCPINDEX~53/research_group_map_h2.json` | LOCAL | FWD-22 (Z-C-S61) | CUT this issuance |
| `MX-c-36` | Z-C-S61 data. Curated tags for harvest rows slice h3 (10 rows), one `--group-map` JSON | `deliverables/0.9.0_WK_NFRA_MCPINDEX~54/research_group_map_h3.json` | LOCAL | FWD-22 (Z-C-S61) | CUT this issuance |
| `MX-c-37` | Z-C-S61 data. Curated tags for the 5 `portal_datasets` rows (`portal_index` tools) | `deliverables/0.9.0_WK_NFRA_MCPINDEX~55/research_group_map_p1.json` | LOCAL | FWD-22 (Z-C-S61) | CUT this issuance |
| `MX-c-31` | Read links (the held R1 cells `MX-c-31` etfs and `MX-c-32` portal/mdpf, MERGED into one cell and cut). The generator's `--read-links FILE` (the file is in the issuer's round-18 deliverables folder, outside the naming gate's `workflows/` domain): 27 RESEARCH rows get the one tool that reads them, each link taking effect only when its tool is in the deployed list. 6 portal/mdpf rows are linked now (their tools are live today); the 21 later links (7 built-not-released etfs/mdpf rows and the 14 rival-fund rows) stay inert until the issuer regenerates with the released tools in the list. Mapping from NFRA_OPLGTW's own classification files and the OG-rv-1/rv-2 definitions. | `gen_silver_rows.py`, `catalog_entries/` (6 regenerated), `tests/` (1 new file) | LOCAL | FWD-22 | CUT this issuance (R18-RES.2a) |
| `MX-c-32` | (merged into `MX-c-31`; the id is not used) | -- | -- | -- | MERGED |
| `MX-r-15` | the catalog release carrying the ASSETS and RESEARCH cells (the ASSETS issuer runs the one emitter, about 17:00Z 2026-10-16), then the links release after `MX-c-31`/`-32` | `0.7.0_AE_CloudOps~MI` | WORLD | FWD-22 | the ASSETS issuer's; not cut here |

`MX-c-31` (which absorbs the held `MX-c-32`) was cut at the first drive tick rather than held: see R18-RES.2a. The 34 DEFERRED etfs/portal/mdpf rows and the 9 dynamodb/news rows have no tool planned and no cell serves them; they stay `gap_owner` rows pending the CTO's ruling on the finish line.

### R18-RES.2a WHY `MX-c-31` WAS NOT HELD (2026-10-16 ~01:xxZ)

The held cells were waiting on NFRA_OPLGTW's releases. Its two classification files (`deliverables/0.9.0_WK_NFRA_OPLGTW~109` and `~110`, `CLASSIFICATION.json`) show what the 47 etfs and portal-v2/mdpf rows OPLGTW targets actually need: 6 COVERED by tools live today, 7 BUILT (merged, not released), 34 DEFERRED with no tool planned. The 14 rival-fund rows are the unreleased OG-rv-1/rv-2 tools. A link is inert until its tool is in the deployed list, so the cell does not depend on the release: it lands the 6 now and carries the 21 as data. **The finish-line gap, measured:** 34 DEFERRED rows plus 9 DynamoDB/news rows (43 of 180, 24 percent) have no tool planned, so "a live `read_tool` on every in-scope row" cannot be met by 22:00Z without new tools or a ruling that an indexed row with a named gap owner counts; asked of the CTO.

## R18-RES.3 CHAINS AND FAN-OUT

Five chains in the first issuance (`MX-c-30`, `MX-c-34`..`-37`) and a sixth, `MX-c-31` (order workstream `RESEARCH-LINKS`: the gate keys one issuance per workstream and round), cut at the 2026-10-16 ~01:xxZ drive tick (write set: `gen_silver_rows.py`, six row files; independent of the others, all merged), all independent by write set: `MX-c-30` (the generator and two removed rows) and the four data slices `MX-c-34`..`-37` (each writes one new JSON file in its own worker folder; none reads another's output, and none depends on `MX-c-30` or on the ASSETS emitter: the check grades the file's form against the map's rules and the issuer joins them at the emitter run). `MX-c-30` and the ASSETS cell `MX-c-23` both edit `gen_silver_rows.py` (different functions: their `--unskip` and labels, this cell's `--scope-exclusions`), so the issuer merges them in sequence.

## R18-RES.4 BATTERY (base HEAD 5858411c5c; `deliverables/2.0.0_SA_COO~MI2/round18/checks/`)

Base dry-runs 2026-10-15: `c30.AC1` FAIL (the generator writes 216 and recreates both files; the difference control reads 0 differ), `c30.AC2` FAIL (the test file is absent), `ct.h1`..`ct.p1` FAIL (the files are absent). Planted arms (standing battery clause 1): `plant_ct.py` 12 of 12 (a good group-map file passes; fewer than 4 or more than 6 tags, a symbol, an uppercase tag, a one-word tag, a missing entity, an extra entity, an extra key beside `nl_tags`, a repeated tag, copied derived tags and tags with no word from the row each fail); `plant_c30.py` 7 of 7 for the drain check `c30.DRAIN.sh` (the RESEARCH rows' `bucket`: a good catalog passes; a prose dynamodb bucket, a portal row without bucket, a changed etfs spelling, an assets row changed outside the ASSETS keys, a changed non-bucket field and a changed top-level section each fail). `c30.AC1` and `c30.AC2` grade the real tree (a fresh generator run and the new tests), so their PASS arm is not plantable and the base FAIL is their arm.

Drain checks (the issuer's, once the slice files and `MX-c-30` are merged and the ASSETS emitter has run): `c30.DRAIN.sh` (bucket on the 180 RESEARCH rows), and a catalog count of `nl_tags_basis: inferred` on the 37 RESEARCH rows equal to 0. Quality of the words is read by the issuer on a sample at the drain and by the CTO at the Z-C-S61 close; no judgment criterion is declared, so no round-close waits on an L9 grade.

## R18-RES.5 WHAT THIS CUT DOES NOT CLAIM

It does not link any `read_tool`, and the displayed grouping needs `vendor`/`firm` on assets and bd rows only (ASSETS). It does not release anything and does not touch the emitter. It does not widen any access: `bucket` is a grouping label.
