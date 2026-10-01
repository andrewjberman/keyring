# IRPT_BCKEND~P (Performance, shared auth/routes/IaC/packaging) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). **Mode FAST** until 2026-10-01T16:27Z: lease `IRPT_BCKEND~P`, re-armed 12:2xZ on `1.0.0_SA_CTO` RULINGS
batch 84 item 5 (nine paths; the tool refused the producer directory and `holdings-performance/handler.py`, which two open
IRPT_DASHBD orders name in `<paths>`). Andrew's word of ~04:2xZ:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`.
Loop: `/canonical-drive 10m` (LIVE_ARMS RELAUNCH row). IRPT_DASHBD workstream B stays FULL. As of 2026-10-01 ~13:2xZ. Earlier forms
are in git (the 09:4xZ form @154651fcb7).

## Standing Andrew words that govern this workstream (read first)

- **2026-09-28 ~22:2xZ call 3 and ~22:4xZ:** performance is end-of-day holdings only, every firm in ONE consolidated gold shape.
- **2026-09-30 ~04:3xZ:** YCharts is `2.0.0_SA_COO~Y`'s (@fe6326f6b0). This seat does no YCharts or resident work.
- **The D2 hold on ADVI_PERFRP** stands until Andrew lifts it; FAST relaxes no hold and no never-widen sign-off.
- **No vendor call without Andrew's per-use word.** The adapter's one-use vendor plan is DISARMED (read 08:16Z; CTO 08:38Z).
- **An S3 delete needs Andrew's word.** None has been made today.

## Pins (served function -> live artifact)

| Function | Live CodeSha256 | Applied (Z) | What it runs | Packet / proof |
|---|---|---|---|---|
| irpt-performance-adapter | `cdbFZDJA...` | 10-01 08:20:26 | a retained vendor figure no longer reopens; "not yet on the holdings basis" answers `OBJECT_NOT_COVERED`; `holdings_gold.py` still the 49 Financial-only version at a595a14264 | packet 3 @d570f71aa1 (CTO @f94239ab13); row S249 |
| irpt-export-render, irpt-directory-search, irpt-holdings | `BIYEQ3PK...`, `AVSIaHEh...`, `TG8b/SEH...` | 10-01 06:24 to 06:31 | packet 2 | row S248 |
| irpt-holdings-performance-lambda | `gLRGHIyi...` | 09-29 14:42:51 | producer and `sources.json` pinned at 363dc1fda4: declaration 1.1, emission 1.1, 49 Financial daily | NOT moved; CLOUD is two changes ahead (below) |
| inf-ec2-launch-monitor | `t1QrzaDe...` | 09-30 16:19:48 | pr-242 | A1 closed @f080be46aa |

Data acts today, each under both halves where a served table moved:

| act | when (Z) | record |
|---|---|---|
| 49 Financial holdings gold `date=2026-09-29` minted (7,559 rows) | 07:13 | ledger closed @a7a6c3622f |
| NNA excusals for accounts 866, 769, 1096 on 2026-09-24 put on the runner | 10:27 | packet @1f898d7db9 (CTO batch 79); ledger leg D1 closed; **leg V1 OPEN** |
| silver `fact_positions/date=2026-08-06` admitted from its coerced file | 12:33 | packet @2a3c7e0feb (CTO @6f9fb8d201 part 1); leg A1 closed |
| silver `fact_positions/date=2026-09-29` admitted from its coerced file, on site Z's word | 12:50 | same packet, part 2 branch (a); **leg A2 OPEN** |
| Inflection holdings gold rebuilt (emission 1.2) | 11:40 onward | ledger `irpt-holdings-gold-inflection-rebuild-20261001`; **leg R1 RUNNING** (1,005 days landed at 13:18Z; about four chunks left) |

Rows closed today: S238 and S244's API half (S248); S247 (S249); S245 (S254, on the CTO's read of the hand reproductions); S216 (S255).
Rows filed today and open: S250 (the coerced 2026-07-02 file differs from its raw file), S251 (the ETF ownership producer writes no
staleness determinations), S252 (Cottonwood's lagged price minority).

## Source on CLOUD ahead of what is served (nothing below is built or applied)

- `sources.json` 1.2 and the producer @de3d423dce: per-source `partition_close` segments (OWN_DATE, PRIOR_TRADING_DAY,
  NO_SINGLE_CLOSE; measured over 555 Inflection trading-day partitions), `link_across_gaps` (Inflection only), emission 1.2 with
  `span_trading_days`. 60 producer tests.
- `performance/holdings_gold.py` @89b5a85abe: a linked row is chained and disclosed; a window edge inside linked days is marked.
  237 performance tests.
- The one admission path: `IRPT_MVP_P/admit_coerced_positions.py` (two dates in its table; every other date refused).

## Write claims

- `2.0.0_SA_COO~P`: the `lambda-source-map.json` rows of irpt-performance-adapter, irpt-export-render, irpt-directory-search,
  irpt-holdings, irpt-narrative and irpt-holdings-performance-lambda; `_authz/served.py`; `performance/retained.py`, `entry.py`,
  `holdings_gold.py`; `data/assets/scripts/gold/irpt_holdings_performance/`; `data/inf/scripts/gold/lib/nna_coverage_excusals.json`
  (exact-file grant, lane IRPT_BCKEND_FAST_P_INF_NNA); this file.
- The private worktree DIR `C:\Users\AndrewBerman\Desktop\coo-p-pr275` is the rebuild's code pin while leg R1 runs: its producer
  directory is not edited until the run ends.

## Next, in order

1. **Close the three open legs** (each is a read, no new act):
   - NNA V1: the chain `chain_full_20261001_113344` passed INF_C_01 (09-24 partition: 6 rows, the packet's AFTER totals, read
     12:44Z). Owed: its own log at chain end (three EXCUSED lines; every step after INF_C_01 read; failures reported the same hour),
     then the row that disarms W97-S3.
   - Admission A2: after the 15:00Z `inf-etf-ownership-daily` run, list every key under `opal-data-etfs/daily/inflection/` with its
     size, say which one the admission caused (expected three: 2026-09-29 from this act, 2026-09-30 and 2026-10-01 on their own),
     and hand the listing to `0.0.0_AB_MSTR` for site Z with the CTO copied by path.
   - Rebuild R1 then V1: list what landed today against the trading days; name every partition still holding the 2026-09-29 build.
2. **The stale gap-day partitions** (2026-05-11, 2026-06-30, 2026-08-10: rows of the old build that no reader may see). Removing
   them is an S3 delete; the alternative is a zero-row overwrite, which changes what the adapter does for a window ending on the
   gap day. One ask to `1.0.0_SA_CTO` when R1 ends.
3. **IB-pr-221's served move** (batch 63 item 3e; PRD ruling 23 arrives in the CTO's addendum): the adapter takes the firm-agnostic
   `holdings_gold.py` with the linked-row handling, `installed.py` and the Inflection source, under its own packet; and the
   producer Lambda takes the 1.2 pair with one schedule entry for `orion` (item 7), which also moves 49 Financial's daily
   partitions to emission 1.2.
4. **The mirror items** (batch 63 item 6): blocker sent 13:18Z; the files are outside this lane's lease and paths.
5. **A named refusal for a directory search with no client firm** (`BucketUnmapped` answers `UNEXPECTED`): its own packet.

IRPT_DASHBD workstream B: contracts landed today, `account_return_daily` 0.2.0 @6a23aee53d and `dim_return_method` 0.1.0
@3f9acac3aa; `0.4.0_DS_ClientPlatform~S` reports DB-b-1 emitted with 3 of 3 criteria passing and flips its own status.

## Parked (owner; condition that un-parks it)

- The cause of the late 09-29 Schwab silver landing -- `0.6.2_AE_PartnerETL~C` (`TO-IB-pr-274`, parked); that lane registers LIVE.
- The served perfrp figure, rows W100-S2 / S237 / S239 -- base `2.0.0_SA_COO` on ADVI_PERFRP; Andrew lifts the D2 hold for that cell.
- `test_unguarded_census.py`, 6 failures since 2026-09-27 -- this lane; when irpt-export-render next takes its `entry.py`.
- `reports/tests/test_resident_installed.py::test_factory_returns_exactly_the_resident_shape_without_any_aws_call`, failing on CLOUD
  -- `2.0.0_SA_COO~Y`; its next resident change.
- A real vendor-path request's own `OBJECT_NOT_COVERED` log line -- this lane; the next Performance-tab walk by `2.0.0_SA_COO~D`.
- 2026-07-01's coerced positions file (not admitted; row S250) and Cottonwood's lagged prices (row S252) -- this lane; before
  either firm's holdings gold is served.
- The six export and adapter A1 legs from 09-27/28 and `irpt-adapter-holdings-gold-49f-r3-20260929` A1 -- this lane; a live walk.
- Scratch for a human to delete: DIR `C:\r27c`, DIR `C:\r27d`.

## Limits

- No scripted authenticated human request exists here. Served checks use `lambda invoke` with a NON-EXISTENT user, log reads, a
  service-level harness on the DEPLOYED bytes, `2.0.0_SA_COO~Y`'s service-principal run and `2.0.0_SA_COO~D`'s signed-in walker.
- A sample of partitions is not the history: the 2026-07 irregular week was invisible to the seam read and thirteen anchor days,
  and a weekend sweep cannot see a weekday. A basis is called measured only where every trading-day partition was graded.
- A full local dry run of an INF gold step refuses off its runner (the dispatch pins the resolution's mode and source digest);
  the guard's own rule was exercised on the exact file instead.
- This network drops S3 body reads: long reads here retry whole objects, and the rebuild re-runs a crashed chunk whole.
