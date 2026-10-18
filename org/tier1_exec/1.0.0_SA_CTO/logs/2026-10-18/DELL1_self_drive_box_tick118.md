# /self-drive dell1 box -- ticks 117-118 (`1.0.0_SA_CTO~DELL1`, 2026-10-18 11:48Z-12:48Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec.
Covers everything since the tick-116 log (@181c2475e4). Tick 117 (12:18Z) was quiet. **state: ARMED.**

## Inbox (0.8)

0 unread at 12:48Z. Read and acked: 8024, 8030, 8033.

## Acts taken

| project | act | hash |
|---|---|---|
| AMGT_HARVST r95 | CVO 8024 MAY-CLOSE: **W170-S3 REMEDIATED** (the CVO's raw-key reads of BP/ and NG/ come back whole). Ruled W171-S4: the split is NOT accepted. Writers use the canonical spelling; readers on the 8 path-component tools take the union, canonical winning; no rename or delete; census first. Round-96 list of 5 | 031ac46589 |
| MDPF_CANON S34 | CTO half (ADVI holdings dedup on asset_id), binds 81b5cfb1 @115f520d62. Read `cot_silver_merge.py` (HEAD 5a98df7a; b0a64fdc95's `_dedup_cols`). Option taken: ONE B_00 build with `--force-recent-days 20`. Added a guard: null asset_id rows must not collapse per account | a31cfe4289 |
| ADVI_COTBOOKS / Cottonwood R106 | C1 8033: C-1 graded on all 122 accounts, 0 flips, 0 dropped; the quarantine proven (14 skips at the 11:31Z silver run). R106 closed, no A_00 cell. The S34 sequence condition is met, and CRO~DDD and C1 are told | (msg 8034/8035) |

## Open calls (Step 1)

The list has 146 rows, 4 open:
- 3 are acts only Andrew can do;
- 1 is escalated: 48ae under XA-20261018T094750Z-cbaa, still OPEN at the laptop CTO.

## ACTS ONLY ANDREW CAN DO

- **0cf5:** confirm ADVI_COTBOOKS's 6 DONE WHEN lines. Citation: L2, rule 27.
- **89c9:** the SOC2_MSLOGS round-2 re-derive. Citation: it needs his MFA session.
- **e1ee:** restart the dell2 box manager. Citation: physical presence at the machine.
- **FWD-10 PROD push:** the page is client-facing. Citation: the portal PROD exception.
- **Upcoming:** the SECCLASS partners-data apply, once its pair is signed. Citation: client-visible.

## Watch

- 13:30Z: the MDPF fire.
- S34 execution: deploy, then 13 scoped silver dates, then one B_00 build. Then the ADVI read: 10-16 = 524,463,230.11.
- XA-cbaa ruling.
- RESAPP round 119.
- HARVST round 96.
- The ms ack.

## Completion test

NOT DONE. Box projects are in flight.

## Compiler Tools

None run. Reads were the `cot_silver_merge.py` hash and `git show b0a64fdc95` of that file; no infra or code change from this seat.
