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

## 4. ROUND 117, WORKSTREAM B-CW (2026-10-15 ~04:3xZ, issuer 2.0.0_SA_COO~C2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-CW_ROUND_117_20261015.md` @14dad61fa3, msg 8038; round 116 closed MAY-CLOSE, the CTO's exercised read of DB-c-7 PASS)

**The CTO's rulings this round cuts on:** (1) the apply order to `0.7.0_AE_CloudOps~DB2` in the signed pair's sequence (blob `ad049d506c`): step 0 the planned execution role's name matches `role/*-cot-*` (else the bucket's `DenyForeignFirmPrincipals` refuses the producer's writes) and the 49 Financial and Inflection roles already carry the gold-listing grant; `terraform fmt`, `validate` and `plan` under `safe-apply`; the plan reads only the Cottonwood adds and code updates on the 49 Financial and Inflection functions (they share the zip), anything else a STOP; the shared zip is named in the NEVER-2 ledger; then the 12-date catch-up (36 keys read ABSENT first), the after-read, the 1.1+1.2 reader check, and only then the one-line change to ENABLED; rollback deletes are Andrew's, registered as one call only if needed. (2) No frontier log change (W404-S2). (3) Cottonwood's `account_return_daily` after 2026-06-22 is computed from Black Diamond values and flows by the one estate method; it is an ASK from this seat to `~D2` (the writer), not a B-CW cell.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-9` | The APPLY of the signed pair: build and upload the shared zip, plan, one `safe-apply`, the 12-date catch-up by the handler event, the after-read, the 1.1+1.2 reader check, the planted listing test, then the schedule ENABLED. Applier `0.7.0_AE_CloudOps~DB2` under its own NEVER-2 ledger | FWD-2, FWD-11 | WORLD (a deploy; the CTO class SERVED for the new gold, the gate floor and the act read WORLD) | none | C-F |
| `DB-c-10` | The ASK to `~D2`: Cottonwood `account_return_daily` after 2026-06-22 from Black Diamond values and flows, with the DB-c-8 table list. The issuer's own direct act (a file and one message), no worker | FWD-11, FWD-15 | LOCAL | none | issuer |

**Decisions inside this decomposition (the issuer's, stated).** (a) The order's surface is the applier's: its deliverables folder, the change-management ledger and sentinel, the investigation file and one repo file, `schedule.tf`, edited once (the `state` line) for the ENABLE step. No other repo file moves. (b) The role count: the CTO's analysis says three new roles; the build declares two roles (the execution role and the scheduler role) with two role policies, one function module, one DISABLED schedule; the order grades the plan by the Cottonwood labels, not by that count, and a third role or any add outside `irpt_holdings_performance_cot*` is a STOP. (c) `terraform fmt -check` on the root reports two PRE-EXISTING misformats in the Inflection copy (`lambda.tf` lines 74 and 75, `locals.tf` lines 114 and 115; read by this seat before the cut); none is in the Cottonwood additions, so the order names those two hunks as expected and any other hunk as a STOP. The applier does not run `fmt` to rewrite. (d) The catch-up covers silver trading days to the packet's as-of date 2026-10-13 less 2026-06-09; the 2026-10-14 day lands at 07:46 New York and is the first scheduled fire's, so a later silver day is NOT written by this order. (e) The CVO-graded limbs: none (0 judgment criteria); the CTO's exercised read of the live state is the act's close read.

**fanout:** 1 of 1 chains, cap 8, reason: the apply is one sequential act under one ledger, with `DB-c-10` the issuer's own direct act. The applier is a Tier-2 seat (`0.7.0_AE_CloudOps~DB2`), not a worker slot.

## Cells (round 117)

| cell id | owner |
|---|---|
| DB-c-9 | 0.7.0_AE_CloudOps~DB2 |
| DB-c-10 | 2.0.0_SA_COO~C2 |

## 5. ROUND 118, WORKSTREAM B-CW (2026-10-15 ~04:5xZ, issuer 2.0.0_SA_COO~C2, on the STOP of the apply order `DB-c-9` by `0.7.0_AE_CloudOps~DB2`, msg 8042)

**What happened (measured by this seat after the STOP, read only).** `DB-c-9` steps 0 to 5 ran: the shared zip was rebuilt and landed (S3 version `vrBQAr57i...`, `handler.py` the only member that differs from the previous zip), ONE `safe-apply` read 7 to add, 2 to change, 0 to destroy, and all three functions (49 Financial, Inflection, Cottonwood) now run `CodeSha256` `OawCMaEq...`; the Cottonwood execution role, scheduler role and schedule exist, the schedule is `DISABLED`; the gold listing is unchanged (75 daily and 150 manifest objects, newest write 2026-09-29). Step 6, the first catch-up invoke (2026-09-28), was REFUSED by the producer: `registry lookup('z09') failed: KeyError`. Cause, reproduced by this seat in the extracted live zip: the zip carries `infra/logic/registry/scopes.json` at the PIN in `infra/aws/lambda/ci/lambda-source-map.json` (commit `14b52ca13a`, 15,565 bytes, 11 scope rows, no `z09` row); HEAD's `scopes.json` (20,150 bytes, 14 rows) adds `z09`. The producer derives the Cottonwood firm from the registry (`firm_scope()`, `lookup("z09")`), so the shared zip cannot serve Cottonwood until `scopes.json` is re-pinned. With ONLY `scopes.json` replaced by HEAD's blob the extracted tree resolves `blackdiamond_z09` to `cottonwood`, and `orion` and `schwab_08335338` resolve to `inflection` and `49financial` exactly as before. The signed pair covered a zip whose members differ from the live one by `handler.py` only; re-pinning a registry member is a second zip upload, so it needs a new signed act (the applier's STOP, correct). The defect is the issuer's: DB-c-7's build did not read that the Cottonwood firm derivation needs a registry row the staged pin lacked.

**The state the STOP left is consistent and nothing served moved**: no Cottonwood gold key was written; the 49 Financial and Inflection functions run the loud-failure handler (they carry the listing grant) and their registry derivations are unchanged; the schedule is DISABLED; the ledger `irpt-dashbd-cottonwood-holdings-performance-20261015` is open with legs L5 to L8.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-11` | The READ and the ADDENDUM PACKET: the live zip's seven registry members against their pins and HEAD, `scopes.json`'s row diff, the differential of the producer's own firm derivation for the three declared channels in the extracted live zip tree versus the tree with the minimal re-pinned members, and the unsigned addendum packet for the second zip (member diff, the plan, the resume at the catch-up, both branches, rollback, the CTO's questions) | FWD-2, FWD-11 | LOCAL (a read and a packet; the act it prepares is WORLD under a new signed pair) | none | C-G |

**Decisions inside this decomposition (the issuer's, stated).** (a) One worker cell, one chain, slot `~406`: the record and the packet come from one run. (b) The addendum is a NEW signed act; nothing here re-uses the first pair for the second upload. (c) The fix to be proven minimal is re-pinning `scopes.json` alone (the issuer's measurement); the cell tests that and any further member the producer's derivation needs, and states the smallest set. (d) The apply order that resumes at step 6 is cut after both halves of the addendum are signed, to `0.7.0_AE_CloudOps~DB2`, which holds the open ledger.

**fanout:** 1 of 1 chains, cap 8, reason: the read and the packet are one chain (the packet's re-pin set is the read's output). Worker `0.9.0_WK_IRPT_DASHBD~406`.

## Cells (round 118)

| cell id | owner |
|---|---|
| DB-c-11 | 0.9.0_WK_IRPT_DASHBD~406 |

## 6. ROUND 119, WORKSTREAM B-CW (2026-10-15 ~05:2xZ, issuer 2.0.0_SA_COO~C2, on the CTO's conditions for the addendum, msg 8055; round 118 closed on `DB-c-11` PASS 2 of 2, merged @ad799ad40b)

**The CTO's conditions** (msg 8055): (1) re-pin `scopes.json` to HEAD's registry as the build input, not a hand edit, and add a build-time test that the zip's `scopes.json` resolves each function's registry key (49 Financial, Inflection, `z09`): one test, no monitor; (2) the plan shows only the three code updates from the same zip, and after the upload the 49 Financial and Inflection derivations are read unchanged before their next 08:15 New York fire; (3) the catch-up then resumes from date 1 under the signed DB-c-5 sequence. `DB-c-11` proved the re-pin: `scopes.json` alone, to `69679b90e3dc52b670d33fddd96d06be1deaac90` (sha256 `6ce64167c26588521fded21330dc59e0109450e9a01c92e0f6ca9aa90b53cfae`), leaves every value the 49 Financial and Inflection channels derive (firm, prefixes, gold addresses, names) identical.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-12` | The BUILD INPUT for the second zip, repo files only: the source-map re-pin (the `pin` and `sha256` of the `scopes.json` entry, in the two holdings-performance function entries, nothing else) and the build-time test that the staged registry resolves the 49 Financial, Inflection and `z09` keys, with a planted negative control. Nothing is built, uploaded, planned or applied | FWD-2, FWD-11 | WORLD by the gate's path floor (`<paths>` names the source map under `infra/`; repo files only, no deploy) | none | C-H |

**Decisions inside this decomposition (the issuer's, stated).** (a) The edit is a committed change to the source map the build reads, never a patch of a zip. (b) Both function entries that stage the registry for this zip (`irpt-holdings-performance-lambda`, whose entry the build uses, and `irpt-inf-holdings-performance-lambda`, which mirrors it) get the same new pin so the two entries stay equal. Other functions' entries are not touched. (c) The test reads the staged pins, materializes the zip's members at those pins into a scratch tree, and runs the producer's `firm_scope()` for the three channels in a fresh process; an environment variable `HP_REGISTRY_SCOPES_PIN` overrides the `scopes.json` pin so the planted negative control (the old pin) can be shown to FAIL. (d) The applier runs the test after the build and before the upload; a failure is a STOP. (e) The addendum packet (`DB-c-11`) is signed by both halves over this cell's merged commit as well as its own bytes; the resume order to `~DB2` follows.

**fanout:** 1 of 1 chains, cap 8, reason: the re-pin and the test are one small chain on one worker (the test's expected value is the re-pin). Worker `0.9.0_WK_IRPT_DASHBD~407`.

## Cells (round 119)

| cell id | owner |
|---|---|
| DB-c-12 | 0.9.0_WK_IRPT_DASHBD~407 |

## 7. ROUND 120, WORKSTREAM B-CW (2026-10-15 ~06:0xZ, issuer 2.0.0_SA_COO~C2, on the signed addendum: CTO half @05472e30fc msg 8114, COO half @bd00e9cd11 amended; rounds 118 and 119 closed MAY-CLOSE, DB-c-11 @ad799ad40b and DB-c-12 @eae8170b22 merged)

**What the signed addendum covers (blob `1a7a8c68bb`):** the second upload of the shared holdings-performance zip with `scopes.json` re-pinned to `69679b90e3` (the committed re-pin and the registry test are merged), the 0-to-add 3-to-change plan on the three functions, and the resume of the open apply ledger: the registry test on the BUILT zip before upload, the printed 49 Financial and Inflection schedule states, the post-apply read that their derivations are unchanged, the first pair's twelve-date catch-up from date 1, the after-read and 1.1+1.2 reader check, then the schedule ENABLED. The CTO's condition 6 adds the Cottonwood function's source-map row (D2-S59) before the upload.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-14` | The RESUME of the apply by `0.7.0_AE_CloudOps~DB2` under the signed addendum and the first pair | FWD-2, FWD-11 | WORLD (a deploy and gold writes) | none | C-I |

**Decisions inside this decomposition (the issuer's, stated).** (a) One cell for the applier: the source-map row, the build with the registry test on the built zip, the upload, the plan and apply, the catch-up, the checks and the enable are one sequential act under one continued ledger. (b) The catch-up is exactly the first pair's twelve dates; the checker pins the dates to `PACKET_FACTS_R115.json`. (c) The `account_dim` writer (the CTO's msg 8103: a scheduled producer on the 49 Financial pattern, a build cell first reading that pattern) is the next cell, cut after this order is in the applier's hands; it is not part of this act.

**fanout:** 1 of 1 chains, cap 8, reason: the resume is one sequential act by one Tier-2 AE lane under one ledger.

## Cells (round 120)

| cell id | owner |
|---|---|
| DB-c-14 | 0.7.0_AE_CloudOps~DB2 |

## 8. ROUND 121, WORKSTREAM B-CW (2026-10-15 ~06:1xZ, issuer 2.0.0_SA_COO~C2, on the CTO's rulings msgs 8099 and 8103: the Cottonwood `account_dim` is a SCHEDULED producer on the 49 Financial pattern, a build cell first reading that pattern)

**The CTO's ruling (msg 8103):** "A one-shot gold write is not a production producer: production must be scheduled ... account_dim changes as accounts open and close. The build cell first reads how 49 Financial's gold account_dim is written (its function, schedule and role) and copies that pattern for Cottonwood under a *-cot-* builder-named role, scheduled after its Black Diamond silver inputs. If no 49F writer exists, add an account_dim emit to the Cottonwood holdings-performance function, with one more gold write grant, by an addendum to its pair. Not a new one-shot path. Cut it the round after the addendum resumes."

**Read first, build after.** The read touches no file the resume order (`DB-c-14`) edits, so it is cut now; the BUILD cell (Terraform and code in the holdings-performance root, which the applier is changing) is cut only after the resume order drains. The issuer's own LIST at the cut read 0 `account_dim` partitions at the builder address for all three firms (49 Financial, Inflection, Cottonwood), so the 49 Financial pattern may not exist where the packet assumed; the cell finds out.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-15` | The READ: each firm's gold `account_dim` state, the repo code that writes an account dimension, the function, role and schedule that run it, the Cottonwood adapter's inputs and what it lacks for a scheduled run; the verdict on the CTO's two branches | FWD-2, FWD-11, FWD-15 | LOCAL (a read) | none | C-J |

**Decisions inside this decomposition (the issuer's, stated).** (a) A read cell, one worker (`~408`), no edits. (b) The BUILD cell and the refreshed pair follow this read and the drain of `DB-c-14`. (c) The 2026-10-12 partition choice of the round-104 packet is superseded by the scheduled design (the producer computes its own date).

**fanout:** 1 of 1 chains, cap 8, reason: one read cell. Worker `0.9.0_WK_IRPT_DASHBD~408`.

## Cells (round 121)

| cell id | owner |
|---|---|
| DB-c-15 | 0.9.0_WK_IRPT_DASHBD~408 |

## 9. ROUND 122, WORKSTREAM B-CW (2026-10-15 ~07:xxZ, issuer 2.0.0_SA_COO~C2, on the CTO's decision C, msg 8167: a firm-isolated Cottonwood `account_dim` Lambda on the Inflection pattern; round 121 closed MAY-CLOSE, DB-c-15 merged @d87a3c60cb)

**The read's finding (`ACCOUNT_DIM_WRITER_PATTERN_R121.json`, verdict `PATTERN_EXISTS_FOR_49F`):** 49 Financial's account dimension is `dim_account`, written by a host runner over an SSM chain; Inflection's is a vendor-puller Lambda; Cottonwood has no writer. The CTO chose C: its own package, a `*-cot-*` role, builder names, reads only the Black Diamond silver inputs, writes only its own `account_dim` gold prefix, scheduled in America/New_York after the silver lands (about 11:46Z), trading-day frontier, first run a catch-up read ABSENT first, the pair carries both branches, no delete.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-16` | The producer CODE: the adapter's one-key upload (refuses a non-empty partition), the Lambda entry point `account-dim-cot/lambda_function.py` (T-1 trading-day frontier, fail loud on absent silver, no write when already landed), and their tests | FWD-2, FWD-11, FWD-15 | WORLD floor (a path under infra/aws/lambda; repo files only) | none | C-K |
| `DB-c-17` | The PACKAGE: Terraform (function, `*-cot-*` role scoped to the two silver reads and the one gold prefix, schedule created DISABLED) and the source-map package entry, in the holdings-performance root or a sibling root | FWD-2, FWD-11, FWD-15 | WORLD floor (infra/), repo files only; nothing planned or applied | `DB-c-16` merged (the adapter pin) | C-K |
| `DB-c-18` | The unsigned NEVER-widen PACKET (both branches, catch-up read ABSENT first, rollback per key, no delete) | FWD-2 | LOCAL (a record) | `DB-c-17` merged | C-K |

**Decisions inside this decomposition (the issuer's, stated).** (a) One key per partition, `data.parquet`: the contract names no manifest for a dimension, so none is written (YAGNI; fewer keys in the blast radius). (b) The partition date is the T-1 trading day, the silver partition dates it reads; the Lambda computes no catch-up range, a manual or catch-up day is the event's `date`, one invoke per day, so the first-run catch-up is the applier's counted list of dates. (c) The handler writes new keys only and returns `TARGET_ALREADY_LANDED` on a landed partition (the holdings handler's rule), so a re-fire is a no-op. (d) `DB-c-17` and `DB-c-18` are cut after `DB-c-16` drains: the package pins the adapter at a commit, and the packet names the pinned bytes.

**fanout:** 1 of 1 chains, cap 8, reason: the three cells are one dependency chain and only `DB-c-16` is cut this round. Worker `0.9.0_WK_IRPT_DASHBD~409`.

## Cells (round 122)

| cell id | owner |
|---|---|
| DB-c-16 | 0.9.0_WK_IRPT_DASHBD~409 |

## 10. ROUND 123, WORKSTREAM B-CW (2026-10-15 ~07:5xZ, issuer 2.0.0_SA_COO~C2, on the CTO's decision C, msg 8167; round 122 closed MAY-CLOSE, DB-c-16 merged @c4d2b97165)

**Supersedes the cell list of section 9 for the cells after `DB-c-16`** (the issuer's own decomposition; stated here, nothing else moved): the package and the Terraform have disjoint write surfaces and no data dependency (the Terraform derives the artifact key from the builder's function name, not from the package entry), so they are two parallel cells, and the packet is the third and last cell.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-17` | The PACKAGE: one new source-map entry `irpt-cot-account-dim-lambda` (15 files, 14 staged rows at pins, sha256-verified, the 13 shared members copied from the holdings entry) and a build-time test that the staged package resolves the silver locations, with a planted old-pin control | FWD-2, FWD-11, FWD-15 | WORLD floor (infra/aws/lambda; repo files only) | `DB-c-16` merged | C-L |
| `DB-c-18` | The TERRAFORM ROOT `account-dim-cot`: function, `*-cot-*` role (two silver reads, one gold prefix, nothing else), scheduler role and a daily schedule created DISABLED; files only, validate only | FWD-2, FWD-11, FWD-15 | WORLD floor (infra/) | `DB-c-16` merged | C-M |
| `DB-c-19` | The unsigned NEVER-widen PACKET (both branches, catch-up read ABSENT first, rollback per key, no delete) | FWD-2 | LOCAL (a record) | `DB-c-17` and `DB-c-18` merged | C-L then C-M |

**Decisions inside this decomposition (the issuer's, stated).** (a) A NEW Terraform root, not more blocks in the holdings root: one root per boundary, one state key, so a plan shows only this function's resources and the holdings root's state is not touched. (b) The schedule fires at 08:45 America/New_York, after the 08:15 holdings fire and after the silver lands (about 11:46 UTC); created DISABLED, enabled by a later one-line change after the catch-up's after-read, as the holdings Cottonwood schedule was. (c) Layer and sizing copied from the holdings Cottonwood function (the producer imports the same pandas and pyarrow stack). (d) The packet (`DB-c-19`) is cut after both merge, so it names the pinned bytes and the real `terraform validate` result.

**fanout:** 2 of 2 chains, cap 8, reason: the package and the Terraform root are independent chains with disjoint write surfaces; the packet follows both. Workers `0.9.0_WK_IRPT_DASHBD~410` (`DB-c-17`) and `0.9.0_WK_IRPT_DASHBD~411` (`DB-c-18`).

## Cells (round 123)

| cell id | owner |
|---|---|
| DB-c-17 | 0.9.0_WK_IRPT_DASHBD~410 |
| DB-c-18 | 0.9.0_WK_IRPT_DASHBD~411 |

## 11. ROUND 124, WORKSTREAM B-CW (2026-10-15 ~08:5xZ, issuer 2.0.0_SA_COO~C2, on the CTO's decision C, msg 8167; round 123 closed MAY-CLOSE, DB-c-17 @f54c662ab0 and DB-c-18 @a5929fb06e merged)

The one-issuance rule is keyed to the round (the gate refused a second issuance in round 123), so the packet cell of section 10 is the single cell of round 124. Its dependencies are met.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-19` | The unsigned NEVER-widen PACKET for the Cottonwood account_dim (change set, the catch-up first with its read-ABSENT, the one key written, both branches, rollback per key, questions for the CTO's half), from read-only measurements | FWD-2 | LOCAL (a record; read-only AWS calls) | `DB-c-17` and `DB-c-18` merged | C-N |

**Decisions inside this decomposition (the issuer's, stated).** (a) The first write is ONE partition, the newest date present in both silver tables, because a dimension is a state snapshot and no consumer is known to need earlier dates; history is a question in the packet for the CTO's half. (b) The worker reads AWS with python boto3 list/get/describe calls only (no put, delete, create, invoke or secret read), so the packet's ABSENT claims are measured. (c) The checker re-reads the S3 plane itself and refuses a packet whose pinned date or empty-prefix claim differs from a fresh LIST.

**fanout:** 1 of 1 chains, cap 8, reason: a single record cell. Worker `0.9.0_WK_IRPT_DASHBD~412`.

## Cells (round 124)

| cell id | owner |
|---|---|
| DB-c-19 | 0.9.0_WK_IRPT_DASHBD~412 |

## 12. ROUND 125, WORKSTREAM B-CW (2026-10-15 ~09:5xZ, issuer 2.0.0_SA_COO~C2, on the signed pair DB-c-19: CTO half @055825367e msg 8218, COO half @d405648eff, both at packet blob ed09e2768f; round 124 closed MAY-CLOSE, DB-c-19 merged @a4a8375b21)

The CTO's decision C (msg 8167) ends with "Cut the build cell and the packet": the build cells are merged (DB-c-16, 17, 18) and the packet is signed by both halves, so the APPLY is the single cell of round 125, issued to the AE lane the CTO half names (answer 1: `0.7.0_AE_CloudOps~DB2`).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-20` | The APPLY of the signed pair: step-0 live reads (bucket fence, layer), the ledger, BUILD_ONLY zip and package test on that zip, the upload, the plan (7 adds, 0 change, 0 destroy), ONE `safe-apply` creating the function, roles and a DISABLED schedule, ONE invoke for 2026-10-13, the after-read of the one key, then the schedule ENABLED by a one-line change | FWD-2, FWD-11, FWD-15 | WORLD | the pair signed at blob ed09e2768f; DB-c-16..19 merged | C-O |

**Decisions inside this decomposition (the issuer's, stated).** (a) The order repeats the precedent of `DB-c-9` and `DB-c-14` (one ledger left OPEN for the first scheduled fire; the issuer closes the last leg) with the CTO half's added step 0. (b) The ENABLE edit is the one line in the new root's `schedule.tf`; the order's paths name that file and the source map (the build script records `artifact_sha256` for the one new entry) and nothing else outside the AE folder, the ledger and the channel. (c) The checker (`p125`) recounts from fresh Lambda, scheduler, IAM-free S3 reads and the repo, and recomputes the parquet's schema hash against the contract's.

**fanout:** 1 of 1 chains, cap 8, reason: a single WORLD apply cell; it is the Tier-2 AE lane's act, not a worker's.

## Cells (round 125)

| cell id | owner |
|---|---|
| DB-c-20 | 0.7.0_AE_CloudOps~DB2 |

## 13. ROUND 126, WORKSTREAM B-CW (2026-10-15 ~14:3xZ, issuer 2.0.0_SA_COO~C2, on the CTO's analysis answering rounds 117 to 125, msg 8325 @46345ab631 section 3: ONE cell, the Cottonwood FWD-1 trace)

The CTO's ruling 2: a read-only trace from Black Diamond silver to the Cottonwood gold (`holdings_performance_daily`, `account_dim`) to the reporting-gold build, which takes the NEWEST `account_dim` partition; it reads whether the next reporting-gold run builds Cottonwood households from the 2026-10-14 partition and what that run's Cottonwood output is (counts, the absent kinds in words); no write, no manual invoke. Ruling 1's condition (re-run the naming gate on the LANDED Cottonwood source-map entries and record the PASS) is the issuer's act and is recorded in this round's drain-end packet; ruling 6: the checker states its base as the branch point and scopes its diff to the worker's own commits (done in `p126`).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-21` | The Cottonwood FWD-1 TRACE: silver and gold counts, the `account_dim` household count and the account crosswalk to the holdings gold, the reporting-gold build's households source and next-run partition, whether the build is scheduled for Cottonwood, its Cottonwood output LIST, the four absent kinds in words, and a verdict per hop | FWD-1, FWD-2 | LOCAL (a record; read-only AWS calls) | none | C-P |

**Decisions inside this decomposition (the issuer's, stated).** (a) The only execution allowed is the reader's own `households()` called through a read-only reader class: it is what the build calls, and it writes nothing. (b) The checker recounts the silver, gold, household and crosswalk figures from a fresh S3 read, so the record cannot disagree with the plane; the counting rules are in the order. (c) A hop that does not hold is a finding with words, never a repair; any repair is a later round by the CTO's word.

**fanout:** 1 of 1 chains, cap 8, reason: a single read cell. Worker `0.9.0_WK_IRPT_DASHBD~413`.

## Cells (round 126)

| cell id | owner |
|---|---|
| DB-c-21 | 0.9.0_WK_IRPT_DASHBD~413 |

## 14. ROUND 145, WORKSTREAM B-CW (2026-10-15 ~23:5xZ, issuer 2.0.0_SA_COO~C2, on Andrew's go for the IRPT suite parallelization through the CTO's ruling `CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 2, msg 8741): FWD-10, Cottonwood first

**The outcome (PRD FWD-10, F8, surface row S07, C-COVERAGE, C-HONESTY):** "A person can always tell what they are looking at: where the data starts, which days could not be measured, when a figure is a fallback, and how current the data is." EXERCISED, read from the screen alone: a partial-history account, a day that could not be measured, a fallback day and a window before the news data starts are each explained on screen in a sentence; no state is hidden inside an average. The CTO's order of work: Cottonwood first (the 07-10 floor, the 3 absent days, the 12-day gap, all measured), then 49 Financial and Inflection. Write surface: the coverage readers and `MethodAndSources` (S07) and the coverage vocabulary.

**Measured by this seat before the cut (read-only, 2026-10-15 ~23:4xZ, so the cells can be graded against them):** Cottonwood `filled_report_values` holds 65 partitions from 2026-07-10 to 2026-10-14, written in one hour on 2026-10-15 (a backfill by another lane, not the scheduled run); 3 of the 68 trading days since 2026-07-10 are absent (2026-08-19, 2026-09-24, 2026-09-25); `account_return_daily` holds 3390 partitions from 2013-04-03 with a run of 12 absent trading days, 2026-06-23 to 2026-07-09 (the days between the last pre-July partition and the floor), plus the same 3 absent days; `holdings_performance_daily` runs 2026-06-10 to 2026-10-14 with no absent day; `account_dim` holds 2026-10-13 and 2026-10-14. The census cell re-measures all of it and adds the reasons and the account histories; the checker recounts every figure from a fresh read.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-22` | The COVERAGE CENSUS (read only): for the four Cottonwood gold tables the first and last day, the absent trading days and runs; the floor and why (the empty Black Diamond `fact_allocations` partitions); the 12-day gap; the partial-history accounts; the coverage column's values | FWD-10 | LOCAL (a record; read-only AWS calls) | none | C-Q |
| `DB-c-23` | WHAT THE PAGE SAYS TODAY (read only): for the four ACCEPT cases and the eight C-COVERAGE members, the code path from the data to the sentence on screen (or its absence) with file and line evidence; the wrong label of S07 | FWD-10, FWD-8 | LOCAL (a record; file reads) | none | C-R |

**Decisions inside this decomposition (the issuer's, stated).** (a) Round 145 is two independent read cells, one fact-finding per side of the join (what the data holds; what the page says); the BUILD cells (the coverage readers, the sentences, the label correction under the S07 write surface, a test that opens the page) are cut at the round-146 analysis from these two records, because their size and files are not known until the records exist (the spec and the decomposition freeze mid-round, so I do not cut a build cell I cannot size). (b) The records carry counts, dates and words only; the checker re-reads every cited line and recounts every S3 figure, so a record cannot disagree with the plane or the code. (c) This round reads Cottonwood only; 49 Financial and Inflection follow the CTO's order once the Cottonwood pattern is built. (d) The portal is read in the worker's own portal worktree (cut at the portal DEV head), read only.

**fanout:** 2 of 2 chains, cap 8, reason: the data census and the page read are independent chains with disjoint write surfaces (two worker folders). Workers `0.9.0_WK_IRPT_DASHBD~414` (`DB-c-22`) and `0.9.0_WK_IRPT_DASHBD~415` (`DB-c-23`).

## Cells (round 145)

| cell id | owner |
|---|---|
| DB-c-22 | 0.9.0_WK_IRPT_DASHBD~414 |
| DB-c-23 | 0.9.0_WK_IRPT_DASHBD~415 |

## 15. ROUND 146, WORKSTREAM B-CW (2026-10-16 ~00:3xZ, issuer 2.0.0_SA_COO~C2, on the CTO's round-145 answer msg 8788 and msg 8795, PRD ADDENDUM v0.15 and v0.16 admitted, `prd-signoff` ADMITTED at v0.16 @72ffcc4be2, msg 8800): FWD-10's Performance-tab cells (b) and (c)

The CTO's list: (a) the unreported-days sentence for any window holding one, read from the report-build output; (b) "Returns from July 10, 2026" as the partial-history sentence, no cause stated; (c) remove C-HONESTY's fallback footnote. The carrier ruling (msg 8795): `~D2` adds `unreported_trading_days` and `unreported_trading_days_basis` to the series contract with its first writer in ONE drain, `~S2` makes the first Cottonwood series publish under its own pair, and `~C2` builds (a) against a fixture GENERATED by the contract's writer.

**Measured before the cut:** the series contract and the portal have no `unreported_trading_days`; the contract's writer does not yet exist (the field is only in the PRD addendum); the portal prints a partial-history note from `coverageSentence('history_scope', ...)` in `performanceView` (`DashboardPerformance.tsx` about line 147) and has no fallback footnote or sentence (round 145).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-24` | (b) the partial-history note becomes exactly `Returns from <first data date>.` with no cause, and (c) a bun test pins that no fallback sentence or footnote exists anywhere on the tab; portal source edit in `DashboardPerformance.tsx` plus one new test file | FWD-10 | LOCAL (a worker branch; no push, no deploy) | none | C-S |

**Decisions inside this decomposition (the issuer's, stated).** (a) Cell (a) is NOT cut in this issuance: the CTO's own rule is that its fixture is generated by the contract's writer (the B-IN feed-writer rule), and the writer lands with `~D2`'s drain; a hand-written fixture would pin a shape nobody has produced. It is cut as the single cell of the next round (147) the tick after that drain, against the writer's fixture, and exercised on the first Cottonwood publish. The CTO's message asked for (a), (b) and (c) in one issuance; the dependency is unmet, and the order of the rule is the CTO's. (b) The note replaces the generic history-scope note in this one place and leaves `COVERAGE_WORDS.PARTIAL_HISTORY` untouched, so the parity pin `iv-e-120` stays true. (c) The footnote is removed in practice already (round 145 found none in the portal); the cell pins it, and the PRD text was restated by the CTO in v0.15 and v0.16. (d) The portal change stays on the worker's portal branch; reaching DEV is the portal merge-forward law's, not this order's.

**fanout:** 1 of 1 chains, cap 8, reason: one portal cell; (a) is blocked on `~D2`'s drain and is the next round's cell. Worker `0.9.0_WK_IRPT_DASHBD~416`.

## Cells (round 146)

| cell id | owner |
|---|---|
| DB-c-24 | 0.9.0_WK_IRPT_DASHBD~416 |

## 16. ROUND 147, WORKSTREAM B-CW (2026-10-16 ~04:3xZ, issuer 2.0.0_SA_COO~C2, on the CTO's round-145 answer msg 8788 cell (a) and the carrier ruling msg 8795, unblocked by `~D2` msg 9020: series contract 0.3.0 and its writer landed on box/dell2 in drain `220c9c63f3`): FWD-10 cell (a), the unreported trading days on the Performance tab

The carrier ruling made the contract's WRITER the source of cell (a)'s fixture; round 146 held the cell for it; msg 9020 names the writer (`publisher.py` `build_series(rows, present_dates=..., calendar=lib/trading_calendar)`, `reporting-publish`, series contract 0.3.0) and the mirror the page takes on: `SERIES_OPTIONAL` gains `unreported_trading_days` and `unreported_trading_days_basis` (five names), the income array becomes `(number|null)[]`, and `iv-e-124` follows the contract file.

**Measured before the cut:** `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` reads `contract_version` 0.3.0 and its `series.optional` holds the five names; the contract's field text says the list is the ISO dates of trading days after `first_data_date`, up to `as_of`, not in `date`, `[]` when none, present on a series from a source that carries the report-build statement, absent otherwise (no statement is made). The portal (DEV head `03f92d82c2`, the round-146 merge) has no `unreported_trading_days`, `SERIES_OPTIONAL` holds three names, `income` is typed `readonly number[]`, and `performanceView` ends its notes with the excluded-days note, the per-state counts and `Returns from <date>.`.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-25` | the page mirror (five optional names, nullable income, `iv-e-124`), and `performanceView` printing "N trading days not reported by the source: <dates>." for any window that holds one, read from the field (never computed in the portal), against three fixtures GENERATED by the contract's writer; portal edits in `DashboardPerformance.tsx` and `seriesContract.ts` plus one new test file and the fixtures | FWD-10 | LOCAL (a worker branch; no push, no deploy) | none (the writer is on trunk) | C-S |

**Decisions inside this decomposition (the issuer's, stated).** (a) The fixtures are made by the issuer's generator `checks/r147/gen_fixture_r147.py`, which calls the contract writer over made-up rows and the real trading calendar; the worker RUNS it and writes nothing by hand, and the checker regenerates and compares bytes, so a hand-shaped fixture fails. (b) The sentence is `<N> trading day(s) not reported by the source: <dates>.` with the dates in the page's existing `dateWords` form and joined "a, b and c"; it counts only the listed days that fall inside the window shown, an absent field or `[]` prints nothing, and the portal names no calendar. The CTO's wording is "N trading days not reported by the source (dates)"; the exact string is the issuer's, for the CTO to read at the round-147 analysis. (c) The new note sits right after the excluded-days note and before the per-state counts, away from the `Returns from` line, so the change cherry-picks onto a PROD-based candidate cleanly, and it uses `dateWords` (present on PROD) rather than the round-146 month-name helper (DEV only). (d) Exercising it on a real Cottonwood publish waits on the publish pair (CTO half signed, msg 9022) and the report-build run, and the CTO allows a test read of the prefix after Act 4; that read is the parked item, not this cell. (e) The portal change stays on the worker's portal branch; reaching DEV is the portal merge-forward law's.

**fanout:** 1 of 1 chains, cap 8, reason: one portal cell. Worker `0.9.0_WK_IRPT_DASHBD~417`, portal ref `03f92d82c23fc270e1115c15989e7637f430e16d`.

## Cells (round 147, workstream B-CW)

| cell id | owner |
|---|---|
| DB-c-25 | 0.9.0_WK_IRPT_DASHBD~417 |

## 17. ROUND 148, WORKSTREAM B-CW (2026-10-16 ~06:0xZ, issuer 2.0.0_SA_COO~C2, on the CTO's msgs 9056, 9061 and 9101 and `~D2` msg 9108: series contract 0.3.1 is on trunk @eb5705f56f and the Cottonwood series are published at `irpt/cottonwood/platinum/reporting/`): the one-name page mirror, and the labelled test read of the real publish through the page

**Measured before the cut:** `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` reads 0.3.1 and its `series.optional` holds six names (`income_claim` last); the manifest optional list holds `calendar_source`; `unreported_trading_days_basis` is const. The publisher does not write `income_claim` or `calendar_source` yet (`~D2`, a later cell), so the writer-made fixtures are unchanged. `iv-e-124` is red against the five-name mirror of round 147. A read-only list of the published prefix returns manifest and series objects per account (the account folder key is an account id; ids are never recorded here). No portal surface prints the series' income (round 147 measurement).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-26` | the page mirror takes on contract 0.3.1: `SERIES_OPTIONAL` equals the six names in order, `SeriesDocument` gains `income_claim?`, `ManifestDocument` gains `calendar_source?`; `iv-e-124` and the round-147 test stay green; portal edit in `seriesContract.ts` only | FWD-10, CTO msg 9056 | LOCAL (a worker branch) | none (the portal base is the round-147 worker branch `wk-IRPT_DASHBD-417-portal` @dd417a1055e5754182391e79cb941aeab07abfbe) | C-M |
| `DB-c-27` | the labelled TEST READ of the real Cottonwood publish through the page's own reader and `performanceView`: counts only (documents, refusals, pair present, accounts with a non-empty list, accounts printing the sentence, income all-null, `income_claim` present); read-only S3 get; no value or id recorded | FWD-10 (the exercise of cell (a) on the first Cottonwood publish; CTO msg 9022 condition) | LOCAL | none (the page code is merged; the data is published) | C-T |

**Decisions inside this decomposition (the issuer's, stated).** (a) The mirror cell is one line of list plus two optional members; it is NOT a direct-act (a portal edit with a parity test, so a worker with the full limbs). (b) The test read is a separate chain because it needs no portal edit and a different grant (S3 read) than the mirror. The harness imports the page's `readSeries` and `performanceView` from the worker's portal tree and writes counts only; the downloaded objects live in a temporary folder outside the repository and are deleted by the worker. (c) The PROD-based candidate (row `92c0`, `cand/dell2/irpt-fwd10-unreported-days-sentence`) must carry the mirror cell too, so `iv-e-124` is green on the merged tree (CTO msg 9056); I cherry-pick the cell's commit onto the candidate and re-register the row after the drain. (d) The income sentence of CTO msg 9061 still has no page surface to bind; not cut. (e) The 49 Financial FWD-10 census is the next round's cell after the CTO's answer to this round.

**fanout:** 2 of 2 chains, cap 8, reason: the mirror edit and the test read are independent chains with disjoint write surfaces. Workers `0.9.0_WK_IRPT_DASHBD~418` (DB-c-26) and `0.9.0_WK_IRPT_DASHBD~419` (DB-c-27), portal ref `dd417a1055e5754182391e79cb941aeab07abfbe`.

## Cells (round 148, workstream B-CW)

| cell id | owner |
|---|---|
| DB-c-26 | 0.9.0_WK_IRPT_DASHBD~418 |
| DB-c-27 | 0.9.0_WK_IRPT_DASHBD~419 |

**Amendment 1 to section 17 (2026-10-16 ~06:5xZ, issuer 2.0.0_SA_COO~C2; gate limb that graded the amendment: none stated).** `DB-c-28` (chain C-P) is an applier order to `0.4.0_DT_ClientPlatform~DELL2` (`TO-PROMOTE-UD`): the PROD promote of `cand/dell2/irpt-fwd10-unreported-days-sentence` @9c24c7bdac (four commits, six files), on Andrew's word "approve 92c0" and the CTO's msg 9125, with a fixture-only labelled page read. It shares no write surface with `DB-c-26` or `DB-c-27`; the sixth optional name of contract 0.3.1 (`DB-c-26`) is NOT in the approved head and not in this promote.

| cell id | owner |
|---|---|
| DB-c-28 | 0.4.0_DT_ClientPlatform~DELL2 |

## 18. ROUND 149, WORKSTREAM B-CW (2026-10-16 ~08:2xZ, issuer 2.0.0_SA_COO~C2, on the standing order of work of the CTO's msg 8741 (Cottonwood first, then 49 Financial and Inflection) now that the Cottonwood FWD-10 cells (a), (b) and (c) are built, merged and promoted): FWD-10 for 49 Financial, the coverage census and the labelled test read of the published series through the page

**Measured before the cut (counts only, this seat's own one-off reads):** 49 Financial gold `account_return_daily` holds 571 date partitions from 2024-07-08 to 2026-10-14 and `holdings_performance_daily` 570 from 2024-07-09 to 2026-10-14, with no absent trading day in either; 49 Financial has no `account_dim` and no `filled_report_values` in gold. The published series prefix `irpt/49financial/platinum/reporting/` holds 6,949 accounts' `series.json.gz` and `manifest.json` and 4,344 `summary.json`; every series carries `history_scope` `PARTIAL_HISTORY`, none carries the unreported-days pair (the 49 Financial source makes no such statement, so the page says nothing about unreported days for it, by the contract's own rule), 6,946 of 6,949 end on 2026-10-14, and the day-quality day totals are MEASURED 2,578,713, NOT_MEASURABLE 57,492, FLOW_UNRECONCILED 6,139 and LARGE_FLOW 44,505. These are the issuer's first reads; the worker's record is the census and the checker re-measures it.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-29` | the 49 Financial FWD-10 census: the two gold tables' first and last day, absent trading days and runs; and the labelled TEST READ of every published 49 Financial series through the page's own `readSeries` and `performanceView` (documents, refusals, the notes the page prints); read-only S3; counts only; no portal edit | FWD-10 | LOCAL | none | C-F |

**Decisions inside this decomposition (the issuer's, stated).** (a) One cell, one worker: the gold census and the page read share the one record and the one checker; it reuses the round-148 harness (`page_read_r148.ts`, `read_publish_r148.py`) by copying. (b) The census records counts and dates only: a 49 Financial account id is a client identifier and never appears in a record, a note or a row. (c) It is read-only: it changes no 49 Financial pipeline, no series and no page; the series' producer is `~D2`'s (workstream B-49F). (d) Inflection has no data yet and is not in this cell. (e) A finding the census may surface (for example the 3 accounts whose series ends before 2026-10-14, or every series reading `PARTIAL_HISTORY`) goes to the CTO in the packet, not into a build cell.

**fanout:** 1 of 1 chains, cap 8, reason: one read-only census and page read. Worker `0.9.0_WK_IRPT_DASHBD~420`, portal ref `34a6baf8657bb166676dc3b8c3eec97ee8d3e585` (portal DEV, the round-148 merge).

## Cells (round 149, workstream B-CW)

| cell id | owner |
|---|---|
| DB-c-29 | 0.9.0_WK_IRPT_DASHBD~420 |

## 19. ROUND 150, WORKSTREAM B-CW (2026-10-16 ~11:0xZ, issuer 2.0.0_SA_COO~C2, on the CTO's msg 9056 (the page mirror is this seat's cell, `iv-e-124` green on the merged tree) and the CTO's rulings on row `D2-S113` (msgs 9226 and 9227), measured at the tick): the page mirror takes on series contract 0.3.3

**Measured before the cut:** `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` reads 0.3.3 (`~D2`, drain `40476cbde7`): `series.optional` holds eight names, the last two `history_scope_claim` and `history_scope_basis`; `series.required`, `array_keys` and `manifest.required` are unchanged and equal to the page's. The page mirror at portal `origin/DEV` `34a6baf865` lists six optional names, so `iv-e-124` is red on trunk. `~D2` has not messaged the landing; this seat measured it.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-c-30` | `SERIES_OPTIONAL` equals the contract's eight names in order; `SeriesDocument` gains `history_scope_claim?` and `history_scope_basis?`; `iv-e-124` and the round-147 test stay green; portal edit in `seriesContract.ts` only | FWD-10, CTO msg 9056 | LOCAL (a worker branch) | none | C-M |

**Decisions inside this decomposition (the issuer's, stated).** (a) The page prints nothing for the two new names: the CTO's ruling makes `Returns from <date>.` print for `history_scope` other than `FULL`, which the page already does, so no sentence changes. (b) Class by the CTO's ruling (msg 9136): the built bytes of the candidate are compared with the build without it; I measure that after the drain. (c) It stacks on the round 148 mirror (merged to DEV), so the PROD candidate carries both commits.

**fanout:** 1 of 1 chains, cap 8, reason: one portal cell. Worker `0.9.0_WK_IRPT_DASHBD~421`, portal ref `34a6baf8657bb166676dc3b8c3eec97ee8d3e585`.

## Cells (round 150, workstream B-CW)

| cell id | owner |
|---|---|
| DB-c-30 | 0.9.0_WK_IRPT_DASHBD~421 |

**Amendment 1 to section 19 (2026-10-16 ~11:4xZ, issuer 2.0.0_SA_COO~C2; gate limb that graded the amendment: none stated).** `DB-c-31` (chain C-P) is an applier order to `0.4.0_DT_ClientPlatform~DELL2` (`TO-PROMOTE-M33`): the PROD promote of `cand/dell2/irpt-series-mirror-contract-033` @831f974aa1 (two commits, one file, type-only), on the CTO's approval of row `6099` (Opal-internal, msgs 9296 and 9297) and the measured built bytes (`deliverables/2.0.0_SA_COO~C2/prod_promote/DB_C30_BUILD_BYTES_R150.md`); its page check is "chunks identical, no visible change". It shares no write surface with `DB-c-30`.

| cell id | owner |
|---|---|
| DB-c-31 | 0.4.0_DT_ClientPlatform~DELL2 |
