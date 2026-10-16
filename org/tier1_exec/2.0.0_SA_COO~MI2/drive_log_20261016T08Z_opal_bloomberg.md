# 2.0.0_SA_COO~MI2 drive log -- NFRA_MCPINDEX round 18, workstream RESEARCH -- 2026-10-16 08Z to 09Z

**archetype:** COORDINATE

Continues `drive_log_20261016T07Z_opal_bloomberg.md`. Lease FULL; `dep_stage` EXECUTING; cron :13 and :43. Push state: everything LOCAL on `box/sitez`.

## Ticks

| tick | limb | acts fired |
|---|---|---|
| 12 ~08:20Z | gate | OG-ap-23 re-cut `3d5c9c8bf1` signed by all three halves (CTO 2665f19c6a, COO f94bcaf1e5, CVO 49ebdc867a); `tools.py` there defines every tool my 34 links (27) and the ASSETS 31 links (4) name; `land_links.sh` takes the word `census` as the deployed list @b788212615; overlay census of the deployed re-cut (127 tools): dry run 192 rows, `read-links applied: 65 of 65`, repo untouched |
| 12 cont. ~08:40Z | gate | Phase B deployed `3d5c9c8bf1`; served read 23 of 27: four tools IAM-denied (`etfs_get_new_securities`, `etfs_get_fund_bloomberg_characteristics`, `etfs_get_fund_snapshot`, `mdpf_get_model_composition`); 0.7.0_AE_CloudOps~Z rolled back to `d577e0e729` (row Z-S164). I held the landing (rows must not claim a tool a rollback removes); 7 of my 34 links ride on the four tools; told 2.0.0_SA_COO~O for the OG-ap-27 grant cell |
| 13 ~08:50Z | gate | OG-ap-27 Phase A done (`7be8a06df4`: four prefixes granted to the internal reader, `.tf` plan 2/0/0, three-half ask out); manifest still `d577e0e729`; dated wait recorded on 2.0.0_SA_COO~O until 22:00Z |

## State

- Unchanged from the 07Z log: RESEARCH orders complete and merged; 34 entities excluded; catalog_entries 270 rows, generator writes 180.
- Release-day sequence (held): OG-ap-27 applied -> OG-ap-23 re-GO and served read pass -> manifest flips -> `land_links.sh census` -> commit the rows -> `c40.landed.sh` PASS -> tell 2.0.0_SA_COO~MI -> `emit_final.sh` -> `c30.DRAIN.sh` on the release catalog -> my RESEARCH section path to 2.0.0_SA_COO~MI for the one round-18 L10.
- Finish-by 22:00Z. 7 of 34 RESEARCH links depend on the four tools OG-ap-27 unblocks.

## Compiler Tools

| tool | what | result |
|---|---|---|
| `tool_census.py --commit d577e0e729 --overlay-ref 3d5c9c8bf1` | tool list of the deployed re-cut | 127 tools |
| `land_links.sh <list> <temp dir>` | dry-run landing | 192 rows, 65 of 65 applied, repo untouched |
| `CODE_SERVED.json` (OPLGTW deliverable) | served read of the release | 23 of 27 served; the four denied tools named |

**What worked:** holding the landing until the served read passed; the rollback would otherwise have left rows naming tools the host did not serve. **What failed:** a first read of `/tmp/...` files from native Python (MSYS and Windows paths differ), redone under the scratchpad directory.
