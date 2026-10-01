# IRPT_BCKEND~P (Performance, shared auth/routes/IaC/packaging) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). **Mode FAST** from 2026-10-01 04:31Z to 12:31Z: lease `IRPT_BCKEND~P`, `org/mcp/drive-mode.log` line 32,
on Andrew's word of ~04:2xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`
@c48af273cc). Loop: `/canonical-drive 10m` (LIVE_ARMS RELAUNCH row); each tick reads the lease and runs `/closer-drive`. IRPT_DASHBD
workstream B stays FULL. As of 2026-10-01 ~09:4xZ. Earlier forms are in git (the 06:5xZ form @5cd4c1d18b).

## Standing Andrew words that govern this workstream (read first)

- **2026-09-28 ~22:2xZ call 3 and ~22:4xZ:** performance is end-of-day holdings only, every firm in ONE consolidated gold shape.
- **2026-09-30 ~04:3xZ:** YCharts is `2.0.0_SA_COO~Y`'s (@fe6326f6b0). This seat does no YCharts or resident work.
- **The D2 hold on ADVI_PERFRP** stands until Andrew lifts it; FAST relaxes no hold and no never-widen sign-off.
- **No vendor call without Andrew's per-use word.** The adapter's one-use vendor plan is DISARMED (read 08:16Z and by the CTO 08:38Z).

## Pins (served function -> live artifact, read at each apply)

| Function | Live CodeSha256 | Applied (Z) | What it runs | Packet / proof |
|---|---|---|---|---|
| irpt-performance-adapter | `cdbFZDJA...` | 10-01 08:20:26 | packet 2's bundle with `retained.py` and `entry.py` at b15f0ed7df: a retained vendor figure no longer reopens; "not yet on the holdings basis" answers `OBJECT_NOT_COVERED` | packet 3 @d570f71aa1 (CTO @f94239ab13); ledger closed @a7a6c3622f; row S249 |
| irpt-export-render | `BIYEQ3PK...` | 10-01 06:24:06 | `served.py` 455cd77ea46e, `loaders.py` | packet 2 |
| irpt-directory-search | `AVSIaHEh...` | 10-01 06:26:24 | whole bundle at f9a00f732c | packet 2 |
| irpt-holdings | `TG8b/SEH...` | 10-01 06:31:21 | whole bundle at 21eca74f40 | packet 2 |
| irpt-ycharts-generate, irpt-status | (read `2.0.0_SA_COO~Y`'s status) | 10-01 06:51, 06:59 | whole bundles, `2.0.0_SA_COO~Y`'s | row S248 |
| irpt-holdings-performance-lambda | `gLRGHIyi...` | 09-29 14:42:51 (read 09:38Z) | producer and `sources.json` pinned at 363dc1fda4 in the source map (declaration 1.1: no close basis) | unchanged; the close-basis change below is source only |
| inf-ec2-launch-monitor | `t1QrzaDe...` | 09-30 16:19:48 | pr-242 | A1 observed and closed @f080be46aa |

Rows closed today: S238 and the API half of S244 (CTO row S248, six of six tenant-selecting functions refuse a foreign firm); S247 (row
S249: all three retained vendor-figure reports are refused on the deployed bytes; before the 08:20Z apply the reopen path DID return
them). 49 Financial holdings gold `date=2026-09-29` minted 07:13Z (7,559 rows) and its after-read exercised on the deployed reader.

## Write claims

- `2.0.0_SA_COO~P`: the `lambda-source-map.json` rows of irpt-performance-adapter, irpt-export-render, irpt-directory-search,
  irpt-holdings, irpt-narrative and irpt-holdings-performance-lambda; `_authz/served.py`; `performance/retained.py` and `entry.py`;
  `data/assets/scripts/gold/irpt_holdings_performance/` (the close-basis change, in the private worktree, not yet merged); this file.
- No Terraform root carries a pending plan from this lane (performance root re-planned `No changes` at 08:22Z).

## Next (the order `1.0.0_SA_CTO` ruled in batches 63, 66, 67; one item at a time)

1. **The Inflection date basis** (batch 63 items 2-3; row S245 ARMED, disarm owner the CTO at step d).
   - (a) DONE @bc19cd3e16: the seam is the partition dated 2026-05-05; Schwab and Black Diamond are own-date.
   - (b) IN HAND: `sources.json` 1.2 gains `partition_close` per source and the producer pairs the partitions that hold the two
     closes; 54 of 54 producer tests pass in the worktree. A whole-history sweep (701 discriminating pairs) then showed a second
     irregular stretch, 2026-07-01..07-17 (four partitions absent; one week not on either basis cleanly). That stretch is being
     graded against the Schwab anchor before the declaration's values are fixed. Not merged until it is.
   - (c) rebuild the Inflection gold over its whole history under one ledger; (d) three hand reproductions read by the CTO;
     (e) only then IB-pr-221's served move. The adapter stays member-wise until (d).
2. **NNA Branch A packet (row W97-S3, ARMED):** three date-scoped excusals (accounts 866, 769, 1096; partition 2026-09-24) in
   `data/inf/scripts/gold/lib/nna_coverage_excusals.json`, the packet as the decider record, both halves. A local dry run of
   `INF_C_01` (writes nothing) is reading which keys the guard refuses on today's silver, before and after the excusals.
3. **The mirror items** (batch 63 items 5-7; rows W99-S3, W99-S4): the coerced 09-29 parquet admitted only on a three-date
   equality; a second scheduled fire; an unknown key class as a counted SKIP; then one schedule entry for the `orion` source.
4. **A named refusal for a directory search with no client firm** (`BucketUnmapped` answers `UNEXPECTED`): its own packet.

IRPT_DASHBD workstream B: table contract 0.2.0 landed @6a23aee53d beside producer bb8f3bb2d1 (hash recomputed equal). Next there is
`0.4.0_DS_ClientPlatform~S`'s own run of TO-DB-b-1's criteria as amended (amendments 5 and 6).

## Parked (owner; condition that un-parks it)

- The cause of the late 09-29 Schwab silver landing -- `0.6.2_AE_PartnerETL~C` (`TO-IB-pr-274`, parked); that lane registers LIVE.
- The served perfrp figure, rows W100-S2 / S237 / S239 -- base `2.0.0_SA_COO` on ADVI_PERFRP; Andrew lifts the D2 hold for that cell.
- `test_unguarded_census.py`, 6 failures at CLOUD HEAD since 2026-09-27 -- this lane; un-parks when irpt-export-render next takes
  its `entry.py` (the live-byte pin is dropped in that move).
- `reports/tests/test_resident_installed.py::test_factory_returns_exactly_the_resident_shape_without_any_aws_call`, failing on CLOUD
  and in the worktree alike (read 07:5xZ) -- `2.0.0_SA_COO~Y` (the resident is that lane's); its next resident change.
- A real vendor-path request's own `OBJECT_NOT_COVERED` log line (none arrived in the ten minutes after the 08:20Z apply) -- this
  lane; the next walk of the Performance tab by `2.0.0_SA_COO~D`, read at the tick after it.
- The docstring of `RetainedVendorFigureRefused` still names `DEPENDENCY_UNAVAILABLE` (CTO half item 8) -- this lane; the file's
  next change.
- The six export and adapter A1 legs from 09-27/28 and `irpt-adapter-holdings-gold-49f-r3-20260929` A1 -- this lane; a live walk's
  read of each surface, and for r3 the first scheduled 49F producer fire that finds its silver.
- Scratch for a human to delete: DIR `C:\r27c`, DIR `C:\r27d`; the private worktree DIR `C:\Users\AndrewBerman\Desktop\coo-p-pr275`
  stays while this lane builds.

## Limits

- No scripted authenticated human request exists here. Served checks use `lambda invoke` with a NON-EXISTENT user (a refusal after
  enforcement), log reads, a service-level harness on the DEPLOYED bytes (`IRPT_MVP_P/retained_reopen_before_after.py`, authorize
  stubbed, vendor transport stubbed to refuse), `2.0.0_SA_COO~Y`'s service-principal run and `2.0.0_SA_COO~D`'s signed-in walker.
- A member list says nothing about a member's vintage. Before any served move: `IRPT_MVP_P/served_import_closure.py` (now with
  `--root`) and `IRPT_MVP_P/sibling_interface_check.py`, both on the uploaded zip, and the zip compared with a bundle assembled and
  rehearsed locally BEFORE the upload.
- A sample of partitions is not the history: the 2026-07 irregular stretch was invisible to the seam read and to thirteen anchor days.
