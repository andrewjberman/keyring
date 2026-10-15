# IRPT_DASHBD -- decomposition, workstream B-CW (Cottonwood), issuer 2.0.0_SA_COO~C2

This file is the B-CW workstream's own decomposition. The shared file `IRPT_DASHBD_DECOMP.md` stays `2.0.0_SA_COO~D2`'s (workstream B), `IRPT_DASHBD_DECOMP_B-IN.md` is
`~I2`'s and `IRPT_DASHBD_DECOMP_R114_F.md` is `~F2`'s, so no two issuers append to one file. Cell ids here are `DB-c-<n>`; worker slots `~401` and up are this seat's
(`~D2` runs `~184` and up, `~I2` `~301` and up, `~F2` `~501` and up; the ranges do not meet). Authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (@a6d9baacaf) and msgs 7898, 7904. FWDs are
unchanged; no PRD change. `~D2` is the SOLE contract writer: this workstream proposes a contract member by a row or an ask to `~D2`, and edits no contract.

## 1. ROUND 114, WORKSTREAM B-CW (2026-10-15 ~01:5xZ)

**No CTO analysis answers this workstream yet** (the CTO's first analysis here follows this workstream's first slug). The cells below are cut on the ruling's write surface
(the Cottonwood adapter and gold partition, and its producer schedule within the 6 AM ET fold, in step with `~P2`) and on what the tree already records.

**Where B-CW stands (measured from the tree, not from a status word).**
- The Cottonwood `account_dim` and household-key adapter is built (`DB-b-196`, worker `~161`, complete). Its never-widen packet (`DB-b-200`, `~165`) is written and nothing is applied.
- `account_return_daily` holds 3,325 partitions, 2013-04-03 to 2026-06-22, all minted on 2026-10-11 by the `TO-CB-al-2` apply (`DB-b-201`, `~166`, record
  `deliverables/0.9.0_WK_IRPT_DASHBD~166/COTTONWOOD_RESUME_PACKET.md`). The Commonwealth input holds one partition, 2026-06-23, so the resume to 2026-10-12 (78 trading days) is BLOCKED on
  the input. The packet's section 8 names what it did not establish: the set of pages that read the table, the fallback calendar's equality with the package for this range, and the
  schedule's target and landing time.
- `holdings_performance_daily` (the Black Diamond channel `blackdiamond_z09`) has its newest gold date at 2026-09-25 and its newest silver input at 2026-10-13: 12 trading days behind
  (`DB-b-221`, `~178`, record `deliverables/0.9.0_WK_IRPT_DASHBD~178/RD_COTTONWOOD_PRODUCER_R110.json`, measured 2026-10-14). No schedule exists for the channel (declared: none; applied:
  none), no Cottonwood principal exists, and ONE landing time was measured. A fire writes served gold, so creating the schedule is a later act under a never-widen pair.
- The holdings table Cottonwood's account page reads is `~P2`'s (IRPT_BCKEND `IB-pr-532` packet, `IB-pr-539` packet v3; the apply `IB-pr-535` is cancelled): the Cottonwood side waits on that release.

**Round 114 is the three things the schedule act and the CTO's pair need and nobody has measured.** All three are LOCAL; two are reads and one is a packet; nothing is written to AWS.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-1` | The Black Diamond silver landing times and the gold frontier: the landing instant (New York time) of the Cottonwood silver partition on each of the last 15 trading days, the earliest fire time that clears the latest of them, the gold dates with a silver input and no gold (the catch-up set), each against the trading calendar | FWD-2, FWD-11 | LOCAL (a read) | none | C-A |
| `DB-c-2` | The never-widen packet for the Cottonwood `holdings_performance_daily` schedule, its principal and the catch-up run: names from the builders, the catch-up keys counted, both branches, rollback per key, the CTO questions. A packet; nothing is applied | FWD-2, FWD-11 | LOCAL (a packet; the act it proposes is WORLD and waits on the pair) | `DB-c-1` | C-A |
| `DB-c-3` | The READERS of the three Cottonwood gold tables (`account_dim`, `account_return_daily`, `holdings_performance_daily`) and the fallback calendar's equality for 2026-06-23 to 2026-10-13: which served code reads each table, and whether the calendar the producers use agrees with the package | FWD-11, FWD-15 | LOCAL (a read) | none | C-B |

**Decisions inside this decomposition (the issuer's, stated).**
(a) `DB-c-1` precedes `DB-c-2` because the packet's schedule time and catch-up key list are the read's outputs; the two share one worker's queue (slot `~401`). `DB-c-3` has no edge to
them and its write set is disjoint (slot `~402`).
(b) The packet covers `holdings_performance_daily` only. `account_return_daily` after 2026-06-23 has no input until a Commonwealth delivery or an input-contract amendment (`DB-b-201`
section 7, condition 3); that is the CTO's call and is carried, not cut. `DB-c-3` reports which page reads it, so the call can be weighed.
(c) Nothing here sets the fire time: `DB-c-1` measures landings, `DB-c-2` proposes a time with its basis, and the CTO's half accepts it. The 6 AM ET fold is `~P2`'s; this workstream reports
whether a landing falls after 06:00 New York and stops there.
(d) No contract member is proposed this round. If `DB-c-3` shows a page reading a Cottonwood table with no contract member, the record says so and the ask to `~D2` is the issuer's act after the drain.
(e) The enrichment after the CTO's ruling (the pair signed, the apply by a CloudOps seat, the catch-up run, the first scheduled fire read) is NOT cut now: it is a WORLD act under the pair.

**fanout:** 2 of 2 chains, cap 8, reason: chain C-A (`DB-c-1` then `DB-c-2`, one worker's queue) and chain C-B (`DB-c-3`) are dependency-independent with disjoint write sets (each its own worker folder).
Workers `0.9.0_WK_IRPT_DASHBD~401` (`DB-c-1`, then `DB-c-2`) and `~402` (`DB-c-3`).

## Cells

| cell id | owner |
|---|---|
| DB-c-1 | 0.9.0_WK_IRPT_DASHBD~401 |
| DB-c-2 | 0.9.0_WK_IRPT_DASHBD~401 |
| DB-c-3 | 0.9.0_WK_IRPT_DASHBD~402 |

## 2. ROUND 115, WORKSTREAM B-CW (2026-10-15 ~02:2xZ, issuer 2.0.0_SA_COO~C2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-CW_ROUND_115_20261015.md` @d514312c6d, msg 7940; round 114 closed MAY-CLOSE, 3 of 3 PASS)

**The CTO's rulings this round cuts on:** 08:15 New York is accepted with an input-frontier check (hold, log, write nothing when T-1's silver partition is absent); the schedule needs a function, so a LOCAL READ of what produced Cottonwood's gold to 2026-09-25 comes first (a function is adopted by Terraform import, otherwise a build cell makes it, WORLD under the pair); ONE never-widen pair covers the function, the schedule, the principal (write only the two gold tables' prefixes) and the catch-up, and the schedule starts ENABLED only after the catch-up's after-read; 2026-06-09 and the rewritten partitions 2026-09-23 to 09-25 are read, not re-run; the Cottonwood reader is `~D2`'s builder (sole contract writer), and this workstream asks `~D2` with the member sources; `account_return_daily` after 2026-06-22 is carried; W401-S1 is MSTR's (install the packages, then this seat re-runs the equality test).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-4` | The PRODUCER READ: what wrote Cottonwood's `holdings_performance_daily` gold to 2026-09-25 (a function, a host job or an ad-hoc run), its code path and last run, the manifest fields that say so; the 2026-06-09 prior-day input; the rewrite times of the silver partitions 2026-09-23 to 09-25 against the gold objects of those dates | FWD-2, FWD-11 | LOCAL (a read) | none | C-C |
| `DB-c-5` | The PAIR PACKET, finalized on `DB-c-4`: the function (adopted or to build), the schedule at 08:15 New York with the frontier check, the principal's write-only grants on the two tables, the 13-date-plus catch-up first and ENABLED after its after-read, both branches, rollback per key. A packet; nothing is applied | FWD-2, FWD-11 | LOCAL (a packet; the act is WORLD under the pair) | `DB-c-4` | C-C |
| `DB-c-6` | The ASK to `~D2`: the Cottonwood member sources the reader needs (the gold tables, their prefixes, the firm key, the readers found by `DB-c-3`), as a file and one line to `~D2`. The issuer's own direct act, no worker | FWD-11 | LOCAL (a file and a message) | none | issuer |

**Decisions inside this decomposition (the issuer's, stated).** (a) `DB-c-4` and `DB-c-5` are one chain on one worker slot (`~403`): the packet's function section is the read's output. (b) `DB-c-5` supersedes `DB-c-2`'s packet for the pair: it carries the as-of date of its catch-up set, which grows by a trading day each day silver lands, and the checker recomputes the set to that date. (c) The ENABLED-after-catch-up order and the frontier hold are written into the packet as the CTO ruled; the hold's code is a build item in the function cell the pair covers, not a change this round. (d) `DB-c-6` is mine: a worker cannot send, and the ask is a message plus a file. (e) The package install (W401-S1) is MSTR's; the equality re-run waits on it and is not cut.

**fanout:** 1 of 1 chains, cap 8, reason: `DB-c-5` consumes `DB-c-4`'s record, so the two are one chain on one worker's queue; `DB-c-6` is the issuer's direct act. Worker `0.9.0_WK_IRPT_DASHBD~403` (`DB-c-4`, then `DB-c-5`).

## Cells (round 115)

| cell id | owner |
|---|---|
| DB-c-4 | 0.9.0_WK_IRPT_DASHBD~403 |
| DB-c-5 | 0.9.0_WK_IRPT_DASHBD~403 |
| DB-c-6 | 2.0.0_SA_COO~C2 |

## 3. ROUND 116, WORKSTREAM B-CW (2026-10-15 ~03:4xZ, issuer 2.0.0_SA_COO~C2, on the CTO's signed half of the DB-c-5 pair, msg 7982, blob `ad049d506c` @80a6ca8dd9; round 115 closed MAY-CLOSE, 2 of 2 PASS)

**What the CTO ruled that this round cuts on** (`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_DB-c-5_R115_COTTONWOOD_HOLDINGS_PERFORMANCE_CTO_HALF.md`): the function does not exist (BUILD, from the builder); the order of acts is BUILD the function, create the principal, run the 12-date catch-up (36 keys read absent first), after-read it, and only then the schedule ENABLED at 08:15 New York; ship schema 1.2 with a 1.1+1.2 after-read by all three `holdings_performance_daily` readers; a refused listing FAILS the fire loud and one test plants it; the applier is an AE CloudOps lane `0.0.0_AB_MSTR~DELL2` seats; and `account_return_daily` after 2026-06-22 takes Black Diamond as its source, so a B-CW READ asks whether Black Diamond carries an account-level return series and at what grain ("next round"). The COO half is signed at the same blob (`219d7cb42d`).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-7` | The function BUILD, repo files only: the Cottonwood function, execution role and policy, scheduler role and the schedule (created DISABLED) as a third copy of the Inflection (IB-er-501) blocks in the 49 Financial Terraform root, plus the handler change (a refused listing raises) with its planted test. Nothing is planned, applied, uploaded or invoked | FWD-2, FWD-11 | WORLD by the gate's path floor (`<paths>` names the Terraform root; repo files only, no deploy; the act it prepares is the signed pair's) | none | C-D |
| `DB-c-8` | The Black Diamond READ: every layer and table under `blackdiamond/cottonwood/`, each table's partitions, newest date, columns and grain, and whether any carries an account-level return series | FWD-11, FWD-15 | LOCAL (a read) | none | C-E |

**Decisions inside this decomposition (the issuer's, stated).**
(a) The two cells are independent chains with disjoint write sets (`DB-c-7` the Terraform root, the handler and tests; `DB-c-8` its own record), so two workers (`~404`, `~405`).
(b) The handler `infra/aws/lambda/investor-reporting/holdings-performance/handler.py` is SHARED: its zip is the artifact the 49 Financial and Inflection functions also run (`lambda.tf` reuses one `artifact_key`). The build changes `_days_to_compute` only (the CTO's ruling 2), and the order forbids a rebuild or upload of the zip: those two functions carry the change only on a later apply, which the applier's pair names. This is stated in the order and graded by `DBC116-3-AC1` (no removed line in the four `.tf` files; `handler.py` changes only inside `_days_to_compute`).
(c) Two existing tests (`test_catch_up.py`, the unreadable-listing branch and the `S297` listing-failure case) encode the old single-day fallback; the build updates those cases to expect the loud failure and keeps the empty-landed case at `[T]`.
(d) The after-read of the 1.1+1.2 readers, the principal, the catch-up and the schedule are the applier's acts under the pair, not cut here.

**fanout:** 2 of 2 chains, cap 8, reason: `DB-c-7` and `DB-c-8` are dependency-independent with disjoint write sets (the Terraform root, the handler and its tests; a record in its own worker folder). Workers `0.9.0_WK_IRPT_DASHBD~404` (`DB-c-7`) and `~405` (`DB-c-8`).

## Cells (round 116)

| cell id | owner |
|---|---|
| DB-c-7 | 0.9.0_WK_IRPT_DASHBD~404 |
| DB-c-8 | 0.9.0_WK_IRPT_DASHBD~405 |
