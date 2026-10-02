# IRPT_BCKEND~P (Performance, shared auth/routes/IaC/packaging) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). **Relaunched 2026-10-02 ~01:5xZ** on `ANDREW_DIRECT_20261002_014xZ_BRING_EVERYONE_BACK_ONLINE_PER_REBOOT_RECORDS.md`.
**Mode FULL**: both FAST leases lapsed (`drive-mode.py read` 01:5xZ: `IRPT_BCKEND` FULL, `IRPT_DASHBD` FULL); a re-arm cites a CTO
ruling (batch 95 item 2 form). Loop: `/canonical-drive IRPT_BCKEND` 10m re-armed 01:5xZ from the LIVE_ARMS RELAUNCH row (stop:
IRPT_BCKEND closed or Andrew's stand-down). The 16:1xZ form of this file is @b57885d3bb.

**Since the brief:** `0.0.0_AB_MSTR` @a3866c3dfb put a DEPLOY-SERVE-HELD sentinel line on
`data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (batch 102 item 2(c)) so the CLOUD push did not
upload it. The serving packet's producer leg removes that line in its own commit carrying `SERVE-RELEASE-ACK: <reason>`.

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

Data acts today, each under both halves where a served table moved; every ledger below is CLOSED:

| act | when (Z) | record |
|---|---|---|
| 49 Financial holdings gold `date=2026-09-29` minted (7,559 rows) | 07:13 | @a7a6c3622f |
| NNA excusals for accounts 866, 769, 1096 on 2026-09-24 put on the runner | 10:27 | packet @1f898d7db9; rollback by version ends 2026-10-15 (@8773d27019) |
| silver `fact_positions` 2026-08-06 and 2026-09-29 admitted from their coerced files | 12:33, 12:50 | packet @2a3c7e0feb, correction @9b0d0cbd5a |
| Inflection holdings gold rebuilt at emission 1.2 (1,613 of 1,616 partitions) | 11:40 to 15:05 | @3cc5b831aa; three hand reproductions accepted |

Rows filed today and open: S250, S251, S252, S257 (ARMED: the Inflection schedule fires too early; fixed in source, disarms on its
first fire), S258 (the holdings-performance root did not plan; fixed in source @2d74e53d39, disarms at the serving packet).

## Source on CLOUD ahead of what is served (nothing below is built or applied)

- The producer @de3d423dce and `sources.json` 1.2 (close-basis segments, `link_across_gaps` for Inflection, emission 1.2).
- `performance/holdings_gold.py` @89b5a85abe (linked rows chained and disclosed).
- The holdings-performance root @2d74e53d39: plans with 0 errors, 7 to add (the Inflection function, roles, policies, schedule at
  14:00 UTC); 49 Financial's entry unmoved. **Nobody applies it before the producer artifact is rebuilt** (the serving packet).
- The mirror's stray-key skip and second schedule @2e00498347 (its own packet, after the serving packet).
- Held UNCOMMITTED in the worktree for the packet: the adapter's source-map re-pin and the role's read grant (`retained.tf`).

## Write claims

- `2.0.0_SA_COO~P`: the `lambda-source-map.json` rows of irpt-performance-adapter, irpt-export-render, irpt-directory-search,
  irpt-holdings, irpt-narrative and irpt-holdings-performance-lambda; `_authz/served.py`; `performance/retained.py`, `entry.py`,
  `holdings_gold.py`; `data/assets/scripts/gold/irpt_holdings_performance/`; `data/inf/scripts/gold/lib/nna_coverage_excusals.json`
  (exact-file grant, lane IRPT_BCKEND_FAST_P_INF_NNA); this file.
- The private worktree DIR `C:\Users\AndrewBerman\Desktop\coo-p-pr275` is the rebuild's code pin while leg R1 runs: its producer
  directory is not edited until the run ends.

## Next, in order

1. **The Inflection serving packet** -- DRAFT @9893683dc3
   (`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/DRAFT_NEVER_WIDEN_PACKET_INFLECTION_PERFORMANCE_FROM_HOLDINGS_GOLD_20261001.md`).
   ONE pre-condition open: the nine stale gap-day objects (Andrew's word on the delete, packet @3cc5b831aa; batch 92 item 6 has the
   CTO reopen the disposition if none). Then build both artifacts, fill the hashes, ask both halves, ledger, apply in the packet's order.
2. **The mirror release packet** (after 1): a real positions failure still stops the run; a stray key is a counted SKIP.
3. **A named refusal for a directory search with no client firm** (`BucketUnmapped` in `_authz/loaders.py` answers `UNEXPECTED`).

IRPT_DASHBD workstream B (this seat issues): DB-b-1 complete; DB-b-3 measured with both criteria passing, its flip is
`0.4.0_DS_ClientPlatform~S`'s now that the method contract 0.2.0 is landed (@9ff75db8f2); rows S10/S11 recommend against the 3.70
percent tolerance (judgment for the round analysis). DB-b-2 worker `0.9.0_WK_IRPT_DASHBD~1` first
spawned 16:1xZ and stopped before its first write for the reboot; RE-SPAWNED 2026-10-02 ~01:5xZ in DIR
`C:\Users\AndrewBerman\Desktop\wk-irpt-dashbd-1` (fast-forwarded to CLOUD @3eac28eae3; amendments 3 and 4 @25c6d2607d, @8ff819062e);
DB-b-4 queues on the same slot. PRD v0.6 (@aabc054e89, rulings 22-25: no tie-out tolerance, agreement only on like day sets) changes
no DB-b-2 or DB-b-4 criterion. L10 slug to the CTO when all four are terminal.

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
