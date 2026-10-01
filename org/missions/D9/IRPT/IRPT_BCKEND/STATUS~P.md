# IRPT_BCKEND~P (Performance, shared auth/routes/IaC/packaging) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). **Mode FAST** from 2026-10-01 04:31Z to 12:31Z: lease `IRPT_BCKEND~P`, `org/mcp/drive-mode.log` line 32,
on Andrew's word of ~04:2xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`
@c48af273cc; CTO 103439). Loop: `/canonical-drive 10m` (LIVE_ARMS RELAUNCH row), each tick reads the lease and runs `/closer-drive`.
IRPT_DASHBD workstream B stays FULL (its DS seat is mid-order; see the last section). As of 2026-10-01 ~05:0xZ. Earlier forms are in git.

## FULL to FAST boundary (done 04:31Z-05:0xZ)

- Nothing new was cut. No worker of this lane was running (the three round-27 worktrees were removed at their drains).
- `TO-IB-pr-274` is NOT flipped: it is not a running order, it is the parked carrier sweep-5 names for the Schwab landing's cause
  (`ROUND_ANALYSIS.sweep5.md` @a50d8207bc section 1 row S235). It is the first Parked line below.
- Round 27's open cell (IB-pr-275) and sweep-5 section 4's ~P enrichment list are the next-list below.

## Standing Andrew words that govern this workstream (read first)

- **2026-09-28 ~22:2xZ call 3:** performance is end-of-day holdings only (`ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md`).
- **2026-09-28 ~22:4xZ:** every firm moves to that basis in ONE consolidated gold shape (`ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md`).
- **2026-09-30 ~04:3xZ:** YCharts is `2.0.0_SA_COO~Y`'s (@fe6326f6b0). This seat does no YCharts or resident work.
- **The D2 hold on ADVI_PERFRP** stands until Andrew lifts it; FAST relaxes no hold and no never-widen sign-off.

## Pins (served function -> live artifact, read 2026-10-01 04:1xZ and 04:4xZ)

| Function | Live CodeSha256 | Candidate uploaded | State |
|---|---|---|---|
| irpt-performance-adapter | `+h/AH/RY...` | `XslOsVc9...` (S3 `iDmIiCgn...`) | packet blob fbfe345d89 @40c790a0bf, COO half signed, CTO half asked 04:59Z / 05:01Z |
| irpt-ycharts-generate | `inrij6hL...` | `ESedDkLy...` (S3 `BH8sOdyV...`) | same packet |
| irpt-export-render | `BORQ2shb...` | `WO5gDeP/...` (S3 `9HpHNNQ_...`) | same packet |
| irpt-directory-search | `s0riHZ9h...` | WITHDRAWN (S3 latest restored to live bytes) | waits on item 2 |
| irpt-holdings | `U4/P5Bh3...` | WITHDRAWN (S3 latest restored to live bytes) | waits on item 2 |
| irpt-status | `ZYr+IDMp...` | WITHDRAWN (S3 latest restored to live bytes) | waits on item 2 |
| irpt-narrative | `es/S9azu...` | none (no selection branch on its live boundary) | excluded |
| inf-ec2-launch-monitor | `t1QrzaDe...` | -- | applied 09-30 16:19:48Z; A1 observation HELD (item 6) |

Source commits: prep merge bd968a95d3; six uploads 3242deb99b (merged 266ecd287b); three withdrawn 7823ef7e31 (merged d753300219);
packet cb4b077244 then 40c790a0bf; ledger `irpt-service-principal-boundary-served-20261001` OPEN @ac27684500 (twelve legs).

## Write claims

- `2.0.0_SA_COO~P`: `infra/aws/lambda/ci/lambda-source-map.json` rows of the seven functions above (the eight live-byte pins on
  ycharts-generate, export-render and status are for the owning cells to drop when they ship those members);
  `infra/aws/terraform/investor-reporting/{performance,directory,export,holdings,ops}/service_profile_read.tf`; the packet; this file.
- Roots with a pending plan from this lane: performance and export read `1 to add, 1 to change`; ycharts reads `0 to add, 1 to change`;
  directory, holdings and ops read the grant add plus a same-bytes `s3_object_version` change. **An untargeted apply in any of the six
  roots by another seat ships this lane's pending change: target your own resource.**

## Next (in order; one item at a time)

1. **IB-pr-275 part 1, the apply.** On the CTO half: grants G1 and G3, simulate, then F1, F3, F4 one at a time under the packet's five
   conditions. V1 (the two S238 prints) is `2.0.0_SA_COO~Y`'s run, asked after the apply.
2. **IB-pr-275 part 2.** A coherent `_authz` set for directory-search, holdings and status: `served.py` @f6c6b56f40 with `enforce.py` and
   `errors.py` at pins that accept its calls, a probe that REACHES enforcement in each bundle (live against candidate), then a second
   packet for G2, G4, G5, F2, F5, F6. The pre-apply gate gains the sibling-interface check (constructor keywords included).
3. **NNA Branch A packet (W97-S3).** Three literal keys (866, 769, 1096; partition 2026-09-24), before and after values, rollback by
   re-emit; the CTO signs on read. INF_C_02..INF_D_11 do not run while the guard holds.
4. **49 Financial holdings gold for 2026-09-29 (sweep-5 section 2 item 3).** Read whether the producer accepts an as-of date; if yes,
   one fire through its own path under both halves naming that one key; if no, the gap is declared (PRD ruling 18).
5. **W99-S3 and the mirror re-time**, routed to `1.0.0_SA_CTO` as one decision.
6. **A1 observation** of the launch monitor: the first stop log line after 2026-09-30T16:19:48Z, due by 11:20Z today, then close.

## Parked (owner; condition that un-parks it)

- The cause of the late 09-29 Schwab silver landing -- `0.6.2_AE_PartnerETL~C` (`TO-IB-pr-274`, parked); that lane registers LIVE.
- The served perfrp figure, rows W100-S2 / S237 / S239 -- base `2.0.0_SA_COO` on ADVI_PERFRP (CTO decision @8729d9792c); Andrew lifts
  the D2 hold for that cell.
- S216 (fact_positions past 09-27) -- this lane; the mirror re-time decision of item 5.
- S232 -- `2.0.0_SA_COO~Y`; the first job accepted under `svc-irpt-analysis` reaches a terminal state (after item 1).
- The six export and adapter A1 legs from 09-27/28 and `irpt-adapter-holdings-gold-49f-r3-20260929` A1 -- this lane; a live walk's
  read of each surface, and for r3 the first scheduled 49F producer fire that finds its silver.
- Scratch for a human to delete: DIR `C:\r27c`, DIR `C:\r27d`.

## Limits

- No scripted authenticated human request exists (a user token is not minted here); served checks use `lambda invoke` with refusal
  events, log reads, and `2.0.0_SA_COO~Y`'s service-principal run.
- The 2026-09-30 candidate probe did not reach enforcement; a result from it says nothing about a request past the firm checks.

## IRPT_DASHBD workstream B (FULL; state lives in `org/missions/D9/IRPT/IRPT_DASHBD/`)

SERIES contract landed @b80543a03c (ask 103446); TO-DB-b-2 amendment 2 @10976d58a1. Owed by this seat as issuer: amend TO-DB-b-1 and
its four r1 checks to PRD v0.4 rulings 17-19 and to row S4's three defects (DS seat 103456; rows S3-S7 @48d3647120).
