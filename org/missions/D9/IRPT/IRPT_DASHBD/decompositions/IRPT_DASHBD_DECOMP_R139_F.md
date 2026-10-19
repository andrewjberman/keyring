# IRPT_DASHBD round 139 -- workstream F-SHIP (~F2) decomposition: the two apply pairs and the bundle manifest's pin split

Issuer `2.0.0_SA_COO~F2`, 2026-10-17 ~07:4xZ. Gate key of the one cell: `<round>139</round><workstream>F2SPLIT</workstream>`. Workstream label beside the round: **F-SHIP, round 139**.

**Answers:** the CTO's round-138 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_138_20261017.md` @aace591b52, msg 10373): round 138 CLOSES; no PRD addendum; round 139 runs in this order: (a) Monday 2026-10-19's 49 Financial first fire read, (b) the Inflection pair (packet REVISION 0.2), (c) the Cottonwood pair (packet REVISION 0), (d) the manifest pin split. One firm changes per fire day. Earlier history waits on a CVO sample per firm. The reader side of FWD-5 is round 140 or later (client-facing PROD promote waits on Andrew). The Cottonwood Income enrichment stays parked.

## The round's items, by kind

| # | item | kind | owner | gate |
|---|---|---|---|---|
| 1 | Monday's 49 Financial first scheduled fire (11:41Z) read: the whole fire's duration and peak printed on the open ledger `irpt-dashbd-49f-transaction-wiring-20261016`, which then closes or rolls back | an ACT (a read), not a cell | this seat (the rollback, if taken, is IB2's) | 2026-10-19 11:41Z; above 720 s or a timeout takes the rollback and nothing below proceeds |
| 2 | the Inflection apply pair: both halves signed on REVISION 0.2's final sha256, then the order to IB2 | packet + order, NOT a worker cell | this seat (the packet and the COO half), the CTO (his half), IB2 (the applier) | item 1 passes; the cell below merged (the release-day bundle re-cut uses it) |
| 3 | the Cottonwood apply pair: both halves on REVISION 0's sha256, then the order to IB2; its first write capped at 25 days | packet + order | as item 2 | item 2's receipt (one firm changes per fire day) |
| 4 | the manifest pin split | a worker cell, **`DB-f-2701`** | worker `~2701` | none |
| 5 | after items 2 and 3 write: a CVO sample per firm from the written prefixes | a judgment criterion | the CVO | items 2 and 3 |

**Why items 2 and 3 are not cut as orders in this issuance:** an apply order to IB2 binds to a packet sha256 and carries both signed halves (the 49 Financial order `TO-DB-f-2204` was cut after the halves were signed). The CTO signs each half "when its packet is final, against one sha256"; neither packet is final yet (the Inflection packet waits on this cell's mechanism for its release-day bundle receipt). They are cut the tick a packet is final and both halves read SIGNED.

## Amendment 1 (2026-10-17 ~08:2xZ): the Inflection apply order is cut

Both packets reached REVISION 1 and the CTO signed both halves (Inflection @028ec74371 on sha256 `ad67beeb8c5c`, msg 10388; Cottonwood @04175d4e4a on sha256 `c5b7d756c11e`, msg 10391). The CTO's word on the Inflection order: "Cut the IB2 order now; the apply waits for Monday's 49F read to pass." The order is **`DB-f-2702`** (workstream `F2INFAPPLY`, applier `0.7.0_AE_CloudOps~IB2`, WORLD, queued behind gate R0: it does nothing until the issuer's `GO` names the closed 49 Financial ledger).

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The apply of the signed Inflection pair: the role audit, ONE `safe-apply` (plan 1/0/0, four statements), the simulation, the release uploads (launcher, zip, receipt, dispatch script), the runner start with the flat-sync listing, a dry run, ONE bounded first write, the receipt | `DB-f-2702` | FWD-5 | WORLD | `DB-f-2501`, `DB-f-2602`, `DB-f-2603`, `DB-f-2701` (merged); both halves SIGNED; Monday's 49 Financial read PASSED | R139-B |

| criterion | invocation | base reading |
|---|---|---|
| DBF139-2-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_infapply.py . DBF139-2-AC1` | FAIL (no record) |
| DBF139-2-AC2 | `python -I .../checks/r139/p139_infapply.py . DBF139-2-AC2` | FAIL (no record) |
| DBF139-2-AC3 | `python -I .../checks/r139/p139_infapply.py . DBF139-2-AC3` | FAIL (no record) |

Checker `p139_infapply.py` (selftest 15 arms). **Four-postulate record.** (i) Domain: one role's inline policies (13 before, 14 after), four objects of `code/gold/`, one gold prefix of at most 25 day partitions. (ii) Same grain: a policy; an object; a day partition. (iii) One intent: the Inflection table is released and first-written, bounded. (iv) Not moved: the 13 other inline policies, the role, its trust, the schedule, every other table and every other firm. The Cottonwood apply order (`F2COTAPPLY`) is cut after this order's receipt and after `2.0.0_SA_COO~D2`'s two re-land pairs on the same function (the CTO's msg 10391).

## Amendment 2 (2026-10-17 ~09:0xZ): the Cottonwood apply order is cut, queued

The CTO signed the Cottonwood half (@04175d4e4a on sha256 `c5b7d756c11e`, msg 10391) with new conditions: this pair goes AFTER `2.0.0_SA_COO~D2`'s re-land events on the same function (D2 answered, msg 10438: its Jul 27 pair is withdrawn; its 7-day re-land pair is function events only on the live code, no bundle, and D2 messages when it closes); an open rewrite ledger on the root STOPS Act 2; a returns-only dry run follows Act 2 with rows equal to the landed day's. The order is **`DB-f-2703`** (workstream `F2COTAPPLY`, applier `0.7.0_AE_CloudOps~IB2`, WORLD, QUEUED behind gate R0 and the issuer's `GO TO-DB-f-2703`, which names the Inflection receipt and D2's closure).

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The apply of the signed Cottonwood pair: the bundle build and upload, ONE `safe-apply` (plan 0/2/0), a returns-only dry run, a transaction-only dry run, the first one-day write, a 25-day range | `DB-f-2703` | FWD-5 | WORLD | `DB-f-2604`, `DB-f-2605`, `DB-f-2606` (merged); both halves SIGNED; the 49 Financial read PASSED; `DB-f-2702`'s receipt; D2's re-land pairs closed | R139-C |

| criterion | invocation | base reading |
|---|---|---|
| DBF139-3-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_cotapply.py . DBF139-3-AC1` | FAIL (no record) |
| DBF139-3-AC2 | `python -I .../checks/r139/p139_cotapply.py . DBF139-3-AC2` | FAIL (no record) |
| DBF139-3-AC3 | `python -I .../checks/r139/p139_cotapply.py . DBF139-3-AC3` | FAIL (no record) |

Checker `p139_cotapply.py` (selftest 14 arms). **Four-postulate record.** (i) Domain: one function's code, one inline policy of one role (5 statements before, 6 after), one gold prefix of at most 25 day partitions. (ii) Same grain: a statement; a day partition. (iii) One intent: the Cottonwood table is first-written, bounded. (iv) Not moved: the five old statements, the schedule, the returns prefix, every other function and firm.

## Cell (ONE order; LOCAL: repo text and offline tests, no `infra/` path)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The bundle manifest's pin split: owned members pinned at cut as now; shared registry members listed without a cut pin; `build_bundle` compares a shared member against a RECEIPT pin; the runtime verifies the zip against the receipt beside it; the launcher test file green at HEAD | `DB-f-2701` | FWD-5 | LOCAL | none | R139-A |

**The mechanism (the issuer's design inside the CTO's ruling, for the cell):** the manifest marks each of the 14 shared members `"shared": true` with no `sha256` (the 5 owned keep theirs); `build_bundle(root, out_path, receipt=None)` takes an optional `{"shared_pins": {path: sha256}}` and compares a shared member against its receipt pin only when one exists; the launcher no longer carries `EXPECTED_BUNDLE_SHA256`; `bootstrap()` reads the expected bundle sha256 from `INF_G_01.bundle.receipt.json` beside the zip (a REFUSED when it is absent), written on the release day by the applier from a build, and the dispatch's flat sync (every object under the four code prefixes by basename, no extension filter) carries it beside the launcher with the zip. **Measured at the cut:** two shared members (`infra/logic/registry/exemptions.json`, `lib/opal_naming.py`) have drifted since the manifest was cut, so `build_bundle` refuses on the trunk and the launcher test file reads 2 failed, 7 errors, 59 passed.

**Four-postulate record.** (i) Domain: the manifest's 19 members split 5 owned and 14 shared (a subtraction over the printed list; no member is neither). (ii) Same grain: a bundle member. (iii) One intent: another lane's edit to a shared file no longer turns the launcher's tests red; an edit to an owned producer still refuses. (iv) Not moved: the producer modules, the contract, the dispatch script, the bundle's member list, any AWS object.

| criterion | invocation | base reading |
|---|---|---|
| DBF139-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_split.py . DBF139-1-AC1` | FAIL (2 failed, 59 passed, 7 errors) |
| DBF139-1-AC2 | `python -I .../checks/r139/p139_split.py . DBF139-1-AC2` | FAIL (the manifest is not split) |
| DBF139-1-AC3 | `python -I .../checks/r139/p139_split.py . DBF139-1-AC3` | FAIL (a planted edit to a shared member refuses) |

Checker `p139_split.py` (selftest 8 arms); a reference manifest and `build_bundle(receipt)` put into the tree by the issuer made AC2 and AC3 PASS and were restored. Fan-out: 1 of 1 chains, cap 4.

## Amendment 3 (2026-10-17 ~13:0xZ): route B for the Inflection pair -- a narrow role the runner assumes, and the launcher's flat-directory defect

**Why.** The Inflection bucket's `DenyForeignFirmPrincipals` does not admit the runner role `inf-gold-layer-ec2-role` (record `deliverables/2.0.0_SA_COO~F2/R139_INFLECTION_BUCKET_FENCE_FINDING.md` @e2c69d8f08); the signed pair would fail at its write. The CTO ruled route B (msg 10542): the four-statement policy moves to a NEW role whose builder-made name matches `role/*-inf-*`; the runner role gets ONE `sts:AssumeRole` on it; the launcher assumes it. The fence, the registry and the bucket policy are not touched. Item 2's pair is re-cut as REVISION 2 after both cells merge; `DB-f-2702` stays HELD until its amendment.
**A second defect, measured by the issuer:** in the runner's flat-directory layout `orion_prefix()` REFUSES ("the naming registry is read from the repo layout only") before the bundle is opened, so the release run cannot reach its first S3 call; the existing flat-directory test exercised only `plan()`. Cell `DB-f-2705` fixes it (the registry is read through the verified bundle) and adds a flat-directory dry run to its checks.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The Terraform of the new role: `iam.tf` gains the role name and assume-policy name modules, the session-name and role-ARN locals, the role (trust: the runner role only, fixed session name), the existing four-statement policy re-pointed at it byte for byte, and the runner's one-statement assume policy; plan will read 3 add / 0 change / 0 destroy | `DB-f-2704` | FWD-5 | WORLD (`infra/` path floor) | `DB-f-2501`, `DB-f-2603` (merged) | R139-D |
| The launcher assumes the role: `SESSION_NAME`, `assumed_s3_client(sts=None, client_factory=None)`, `main` uses it when no client is injected and prints the role and session, a failed assume REFUSES naming the role, the flat-directory naming refusal fixed, tests green | `DB-f-2705` | FWD-5 | LOCAL | `DB-f-2701` (merged) | R139-E |

| criterion | invocation | base reading |
|---|---|---|
| DBF139-4-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_inf_role.py . DBF139-4-AC1` | FAIL (iam.tf unchanged) |
| DBF139-4-AC2 | `python -I .../checks/r139/p139_inf_role.py . DBF139-4-AC2` | FAIL (no role) |
| DBF139-4-AC3 | `python -I .../checks/r139/p139_inf_role.py . DBF139-4-AC3` | FAIL (no assume policy) |
| DBF139-5-AC1 | `python -I .../checks/r139/p139_assume.py . DBF139-5-AC1` | FAIL (no `assumed_s3_client`) |
| DBF139-5-AC2 | `python -I .../checks/r139/p139_assume.py . DBF139-5-AC2` | FAIL (`main` builds a plain client) |
| DBF139-5-AC3 | `python -I .../checks/r139/p139_assume.py . DBF139-5-AC3` | FAIL (flat-directory naming refusal) |

Checkers: `p139_inf_role.py` (selftest 11 arms; its `reference()` made AC1 to AC3 PASS on the trunk and was restored) and `p139_assume.py` (selftest 8 arms; a reference launcher made AC1 to AC3 PASS and was restored with `git checkout`). **Four-postulate record.** (i) Domain: the inf-pipeline root's 47 files (46 untouched) and one launcher file with its test file. (ii) Same grain: a Terraform resource; a launcher function. (iii) One intent: the Inflection transaction write is made by a role the fence admits. (iv) Not moved: the four statements' text, the runner role's 14 other inline policies, the fence, the registry, the bucket policy, every other firm. Fan-out: 2 of 2 chains, cap 8.

**Amendment 3a (2026-10-17 ~13:3xZ): the session-name literal.** Both workers (rows D2-W2704-S4, D2-W2705-S1) were refused by the commit-time naming limb: the literal `inf-g-01-account-transaction` is a NEW hand-kept carrier of the `inf` scope token. The issuer rules inside its own decomposition: the fixed session name is `g01-account-transaction` (no scope token; the role name stays builder-made, so the fence still admits the role). Measured: the naming gate PASSes the new literal in `iam.tf` text and REFUSEs the old one. Changed in the two orders, the three checkers and the reference launcher; selftests 11, 18 and 8 arms PASS. Gate limb that graded the amendment: none (an order amendment before any work landed).

**Amendment 4 (2026-10-17 ~14:2xZ): the Inflection pair re-cut as REVISION 2; order DB-f-2702 re-pointed.** DB-f-2704 (merged @3dc5ee36ea) and DB-f-2705 (merged @beddfb340f) are complete. The packet is REVISION 2 (@b9b961b3da, sha256 `5bfd8e040939`): plan 3 add / 0 change / 0 destroy, the simulation of the new role WITH the live bucket policy, the runner assumes the role, a 40-minute stop on the dry run (one-hour credentials). The COO half is re-signed on those bytes; the CTO half must be re-signed (the REVISION 1 half does not cover them). `DB-f-2702` is amended in place (its criteria ids are unchanged; `p139_infapply.py` carries the REVISION 2 sha256 and the route-B clauses, selftest 18 arms) and stays HELD: no GO until the CTO half reads SIGNED at the new sha256 and Monday 2026-10-19s 49 Financial first-fire read has passed. Gate limb that graded the amendment: none (an apply order is not gate-graded on modification).

## Amendment 5 (2026-10-17 ~15:2xZ): the Cottonwood transaction stage reads the late-posting window (cell DB-f-2706)

**Why.** The CTO's msgs 10588, 10592, 10595 and 10597 (dell1 msg 7612; `2.0.0_SA_COO~D2`'s row S137): the Cottonwood fact_transactions silver is a rolling 14-day period pull. This seat's read-only census (`R139_COTTONWOOD_PARTITION_OVERLAP_FINDING.md` @16bd2e885d): 125 of 127 partitions hold a row of another business day (so the signed stage would skip nearly every day), a business day's rows repeat across about ten partitions, none of the 14 columns the producer reads varies across partitions for one TransactionID, and a day is complete at its D+14th trading day. The 49 Financial and Inflection stages read one daily file and one full snapshot respectively and are correct as built.
**The ruling (CTO msg 10597, item 1):** write day D only once its full D..D+14 window exists (100 percent), and write it once; the receipt names the newest writable day. The suspended Cottonwood pair (packet REVISION 1, @dc56f78c7d) is re-pinned by addendum after this cell merges and `2.0.0_SA_COO~D2`'s reader fix ships in the SAME code release (one function, one build, one apply).

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The window reader and the stage's own owed-day rule: `TX_WINDOW`, `trading_lag`, `window_end_day`, `window_complete`, `newest_writable_day`, `transaction_owed_days`; `transaction_frame` reads D..D+14 and dedups on `TransactionID` keeping the first (the earliest partition) and keeps the rows whose business date is D; `emit_transactions` writes a day once and only on a full window; the scheduled fire runs the stage on its own owed days (never on the returns days); `day`, `days` and `rewrite` events never run it; results carry `transaction_window`; the function-map entry re-pinned | `DB-f-2706` | FWD-5 | WORLD (`infra/` path floor) | `DB-f-2605`, `DB-f-2606` (merged) | R139-F |

| criterion | invocation | base reading |
|---|---|---|
| DBF139-6-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_cotwindow.py . DBF139-6-AC1` | FAIL (no `TX_WINDOW`) |
| DBF139-6-AC2 | `python -I .../checks/r139/p139_cotwindow.py . DBF139-6-AC2` | FAIL (no `transaction_owed_days`) |
| DBF139-6-AC3 | `python -I .../checks/r139/p139_cotwindow.py . DBF139-6-AC3` | FAIL (no `trading_lag`) |

Checker `p139_cotwindow.py` (selftest 5 arms); a reference handler (`p139_cotwindow_reference.py`) put into the tree by the issuer made AC1 and AC2 PASS and AC3's wiring clauses PASS (AC3 then fails only on the old tests, which the cell must bring to the new rule) and was restored with `git checkout`. **Four-postulate record.** (i) Domain: one handler file, its tests directory and one function-map entry; the window rule over 127 partitions, 120 business days. (ii) Same grain: a business day; a TransactionID. (iii) One intent: a Cottonwood transaction day is complete, deduped and written once. (iv) Not moved: the returns path (`run_day`, `owed_days`, the rewrite path), the producer's normaliser and writer, every other firm. Fan-out: 1 of 1 chains, cap 8. Coordination: `2.0.0_SA_COO~D2`'s reader fix edits the same function's adapter and the scheduled fire's rewrite step; on a merge conflict in `handler.py` the worker files a BLOCKING row and stops.

**Amendment 6 (2026-10-17 ~17:4xZ): the Cottonwood pair signed on REVISION 2; order DB-f-2703 re-pointed.** Packet REVISION 2 (@5cb1dc9403, sha256 `5d7350ea8a92`; the ONE code release, release commit `36da4e101f` = D2s TO-DB-b-334 on top of TO-DB-b-333 and this seat's DB-f-2706) is SIGNED by both halves (COO @967e9df46d, CTO @827bc0c17e, msg 10626; questions 1 to 3 accepted). The CTO added: Act 3(b) prints each settle day's rows, NOT_MEASURABLE share (at most 15 percent) and flow-account count, and either measure above 80 percent STOPS. The issuer's ruling inside the order: a scheduled dry run on the apply day usually owes no settle day, so the prints come from one DRY REWRITE per settle day of the FIRST scheduled fire plus the read-only tool `tools/settle_day_figures.py` (the same derivation, rows equal to the dry rewrite's). `DB-f-2703` is amended in place (criteria ids unchanged; `p139_cotapply.py` selftest 25 arms) and stays HELD on Monday's 49 Financial read, the Inflection receipt and the issuer's GO. Gate limb that graded the amendment: none (an apply order is not gate-graded on modification).

**Amendment 7 (2026-10-19 ~15:2xZ): the Inflection pair re-pinned by Addendum 1; order DB-f-2702 re-pointed and re-released.** Cause: `0.7.0_AE_CloudOps~FB1` (dell1, ADVI_FIRMBKTS FB-p-2) uploaded `code/gold/orion-gold-dispatch.sh` at 14:22:09Z (version `hK5vY2H31oT3...`, sha256 `9495cd56228b`), so REVISION 2's dispatch pin `7b206030bfc7` and its rollback version `0JwOjjCw...` would have reverted it (CTO msgs 10718, 10730; ruling `RULING_ORION_GOLD_DISPATCH_TWO_WRITERS_20261019.md`). Addendum 1 (`NEVER_WIDEN_PACKET_INFLECTION_TRANSACTION_RELEASE_ADDENDUM_1.md` @c5aeca1595, sha256 `115ba6e99cba`; the REVISION 2 packet bytes unchanged) re-pins the dispatch to `d2ff692abd23`, states the live pre-state `9495cd56228b` and the rollback target `hK5vY2H31oT3...`, and adds the pre-check `tools/dispatch_diff_check.py` (live to pin = the pair's own 145 lines). Both halves are SIGNED on it (COO @d958a06809, CTO @5404377480, msgs 10739 and 10740). The CTO ruled FB1's open ledger satisfied on the measured artifact (9bfa234989 an ancestor of CLOUD; `gold/meta/pipeline-complete.json` with no version newer than 14:22:09Z across a completed chain), which puts the pair's write acts after 14:15Z Tuesday. `DB-f-2702` amended in place (criteria ids unchanged; `p139_infapply.py` selftest 30 arms). Gate limb that graded the amendment: none (an apply order is not gate-graded on modification).
