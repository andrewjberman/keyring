# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX rounds 13 and 14 cut; first reports; naming-gate repair -- 2026-10-14 12:2xZ-15:4xZ (host opal_bloomberg)

**archetype:** MIXED

## Ticks and events

| time | act |
|---|---|
| 12:2xZ | Relaunched on Sonnet 5.5. Watcher armed, cron `31dd41d8` (`/canonical-drive NFRA_MCPINDEX` hourly at :07). Tick 1 empty: MX-r-13 waits behind the gateway queue |
| 13:1xZ | CTO msg 34078: PRD v0.11 FWD-22 ADMITTED (CVO signed ratified-text). Round 13 = G1 harvest catalog at table grain |
| 13:3xZ-14:0xZ | Round 13 cut `bc6905342f` (fanout 2 of 2): MX-c-11 loader/tool index/v0.5/discover, MX-c-12 generator + 78 rows; checks + planted arms (plant_c12 14/14, plant_c11 4/4). Workers ~36, ~37 (haiku/high). MX-r-13 A2 `a60fffec88` |
| 14:0xZ-14:5xZ | PRD v0.12/v0.13 (G2 G4 G5 G6) -> round 14 cut `091f812b7b`: MX-c-14 generator + 174 silver table rows (worker ~38), MX-c-13 silver loader/writer/discover queued behind MX-c-11 on ~36. CTO told (msg to 34126): G3 + certified channel text -> round 15, CTO confirmed |
| 15:1xZ | Worker reports: ~36 MX-c-11 VALID (4 of 4); ~37 MX-c-12 criteria PASS by output but rows BLOCKED by the commit-time naming gate (78 `contract.id` strings read as S3 keys; 3 legacy hyphen prefixes). Gateway: OG-hv-2 closed, live `7c558b4e21`, harvest_list/harvest_read served |
| 15:1xZ | CTO msg 34135 (Andrew-direct): client data ONLY from opal-data-assets vendor silver; no opal-data-bd; account-grain MDPF feed not_served. Amendment `3d923863b5` (49F sentence) withdrawn by `0ccc003a99` |
| 15:3xZ | Amendment `0ccc003a99`: contract.id ':' for '/', 9 legacy registry keys (3 new), not_served rows, 5 red tests into MX-c-13 paths. Re-seats: ~37 on MX-c-12 A1 (branch `ff2710841f`), ~36 on MX-c-13 (branch `c78df77169`). A finished worker cannot be resumed (SendMessage: no transcript), so a slot is re-seated with a fresh worker and its inherited commits. ~38 still on the pre-amendment face |

Tick rows: `NFRA_MCPINDEX | L7 | 13+14 | TOs 4 new | cells 4/4 | thread none | DRIVE FORWARD`.

## Hand-off

- Pending reports: ~37 (MX-c-12 A1), ~36 (MX-c-13), ~38 (MX-c-14, re-seat on the amended face when it reports; put order + round14 checks on its branch first).
- Drain (decomposition R13.4/R14.4): merge per chain end through `safe-merge.sh`; flip MX-c-12/MX-c-14 `<status>` complete at the merge (the flip is outside a worker's grant); regenerate `DATA_CATALOG.yaml`; re-run c10/c11/c12/c13/c14 checks on the merged tree (the three new registry keys exist there); gateway suite delta; tighten `test_every_harvest_row_is_reachable...` to 78.
- Round 15 (G3 + certified channel text): needs 3.0.0_SA_CVO~Z's read on the decomposition BEFORE issuing (CTO msg to 34126). Shares DATA_CATALOG.yaml with 13/14: cut when they drain.
- MX-r-13 A3 at the PHASE A GO: ship round 13+14 catalog, r13.AC4 check to be written and dry-run first; queue OG-ap-18, OG-ap-17.

## Compiler Tools

- `naming-gate.py --diff <file> --enforce` on a hand-built all-new-files diff pre-checks a catalog change (a 78-file diff takes about 2.5 minutes). Run it BEFORE the cut for any order whose rows carry S3-looking strings; the failure cost a worker's whole run.
- `git show <pin>:<path>` for every contract file; planted arms (a reference generator, 14 to 20 one-defect mutations) found six check defects before any worker ran.
- Gap: a finished worker cannot be continued (SendMessage: no transcript); budget a re-seat for any amendment after a report.
