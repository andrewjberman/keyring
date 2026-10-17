# IRPT_DASHBD round 138 -- workstream F-SHIP (~F2) decomposition: the 49 Financial function-map file carries the re-staged state

Issuer `2.0.0_SA_COO~F2`, 2026-10-17 ~03:0xZ. Gate key of the first cell: `<round>138</round><workstream>F2PORT</workstream>`. Workstream label beside the round: **F-SHIP, round 138**.

**Answers:** the CTO's acceptance of the round 138 list in order (msg 10145; list item 3, "the source-map port") and his instruction of msg 10190: no lane change; one one-file order to the applier `0.7.0_AE_CloudOps~IB2`, which commits the corrected bytes; the check is BUILD_ONLY equal to `JgSV12Tz...` and `terraform plan` of reporting-gold reading No changes; landed before Monday's 11:41Z fire.

**The finding behind the cell (measured by this seat, 2026-10-17 ~02:35Z):** MSTR's drain (CLOUD's TO-CT-ca-1) landed the retirement of `lambda-source-map.json`; the ported file `function-map/irpt-49f-reporting-gold-lambda.json` was made from a base taken BEFORE IB2's re-stage commit `3ff444434e`. Against the retired map's last entry, exactly three fields differ: `artifact_sha256` (drained `SCt7IgN3..`, deployed `JgSV12Tz..`) and the pins of `lib/trading_calendar.py` (drained `b2b74886`, re-staged `f25618c0`) and `infra/logic/registry/systems.json` (drained `21c67202`, re-staged `fdecf020`). The drained file's BUILD_ONLY prints `SCt7IgN3..`, and the attribute-closure check (`p137_repin.py DBF137-1-AC2`) FAILS on it (the older `trading_calendar.py` pin lacks `first_trading_day_on_or_after`). With the three fields set, the whole entry equals the retired map's last entry and BUILD_ONLY prints `JgSV12Tz..`.

**Carried, not in this cell:** against HEAD today three other pinned members are no longer current by content (`org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`, `lib/opal_naming.py`, `infra/logic/registry/exemptions.json`: other lanes edited them after the re-pin). That is correct for this cell (the deployed bundle was built from the pinned blobs, and re-pinning them would change the bundle's hash); the round-137 content-currency check `DBF137-1-AC1` therefore reads FAIL on the trunk from now on, as the earlier rounds' checkers do after their rounds. The next rebuild of the bundle re-pins them by a cell.

## Cell (ONE order; WORLD, the infra/ floor)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The corrected `function-map/irpt-49f-reporting-gold-lambda.json` (pinned bytes, sha256 `51193ac1b91d`), committed by the applier under its lane, with the BUILD_ONLY and `terraform plan` reads recorded | `DB-f-2601` | FWD-5 | WORLD | the drain (landed); `DB-f-2204` (complete) | R138-A |

**Four-postulate record.** (i) Domain: one file of 241 in `function-map/`, three fields of it. (ii) Same grain: one entry. (iii) One intent: the file carries the state the deployed function runs. (iv) Not moved: the other 240 files, the function, its role, its schedule and every table; no AWS write (a plan is a read).

## Criteria (three mechanical; checker `checks/r138/p138_port.py`, selftest 9 arms; the pinned corrected bytes placed in the file make AC1 and AC2 PASS)

| criterion | invocation | base reading |
|---|---|---|
| DBF138-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_port.py . DBF138-1-AC1` | FAIL (the drained bytes, sha256 `fa6a4d9ec441`) |
| DBF138-1-AC2 | `python -I .../checks/r138/p138_port.py . DBF138-1-AC2` | FAIL (BUILD_ONLY prints `SCt7IgN3..`) |
| DBF138-1-AC3 | `python -I .../checks/r138/p138_port.py . DBF138-1-AC3` | FAIL (no record) |

Fan-out: 1 of 1 chains, cap 4. The remaining round 138 items (Cottonwood wiring and the Inflection pair's rest) are cut when the CTO's round-137 analysis is in hand.

## Cell 2 (added 2026-10-17 ~03:3xZ; ONE order; LOCAL, workstream `F2BOUND`): the Inflection launcher's bounded default

Answers the CTO's RULING B on the nightly block (msg 10145, item 4): without `--since` the launcher writes only the business days after the newest day already written at the target prefix, the 25 newest of them at most; an empty target takes the cap, not the history; an up-to-date target writes nothing; an explicit `--since` keeps its meaning (the applier's bounded range, no cap). Round 138 list item 4 (the Inflection pair), the first of its parts; no unmet dependency (the launcher is on the trunk since round 135).

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The launcher `data/inf/scripts/gold/INF_G_01.account_transaction_gold.py` gains the bounded default (newest written day read from the target prefix, the cap of 25), and its test file gains the tests | `DB-f-2602` | FWD-5 | LOCAL | none | R138-B |

**Four-postulate record.** (i) Domain: one launcher function path (`run`) and its CLI default; the producer, the bundle members, the dispatch script and the contract untouched. (ii) Same grain: a business day. (iii) One intent: the default is bounded. (iv) Not moved: `--since` semantics, the plan, the no-repeat guard over the FULL output, the S6 report, the bundle manifest and its pin (the launcher is not a bundle member).

**Measured at the cut (the issuer, 2026-10-17):** two bundle members drifted from the manifest at HEAD (`infra/logic/registry/exemptions.json`, `lib/opal_naming.py`, edited by other lanes), so `build_bundle` REFUSES and the launcher test file reads 2 failed, 7 errors (49 passed) on the trunk BEFORE this cell. They are not this cell's: the manifest and pin are re-cut on the release day (the CTO's order). The cell's own tests must pass; the 9 baseline items are named in the order and neither fixed nor worsened.

| criterion | invocation | base reading |
|---|---|---|
| DBF138-2-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_bounded.py . DBF138-2-AC1` | FAIL (an empty target wrote 43 days) |
| DBF138-2-AC2 | `python -I .../checks/r138/p138_bounded.py . DBF138-2-AC2` | FAIL (an up-to-date target was written again) |
| DBF138-2-AC3 | `python -I .../checks/r138/p138_bounded.py . DBF138-2-AC3` | FAIL (a dry run reports 43 days) |

Checker `p138_bounded.py` (selftest 7 arms); a reference implementation put into the launcher by the issuer makes all three PASS (positive control run and reverted).

## Cell 3 (added 2026-10-17 ~03:5xZ; ONE order; WORLD, the infra/ floor; workstream `F2INFIAM`): the runner policy gains S4, ListBucket on the Inflection gold prefix

**Found by the issuer while cutting Cell 2:** the bounded default reads the newest written day by LISTING the gold prefix, and the runner policy of `DB-f-2501` (merged @3e5d4896e2: S1 Get and S2 List on silver, S3 Put on gold) grants no List on the gold bucket, so the default would be AccessDenied on the runner. **The CTO ruled (msg 10239): YES**, `s3:ListBucket` on the Inflection gold bucket, conditioned on `s3:prefix` equal to `irpt/inflection/gold/account_transaction` and its children (builder output), no GetObject on gold, XA-a222 condition 2's form, and the simulate control gains S4 (ALLOW the list on that prefix, DENY a list of another prefix); it rides the Inflection pair (the packet names it).

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `inf-pipeline/iam.tf`: statement S4 (between S2 and S3) and the two gold list locals, by pure insertion into the block of `DB-f-2501`; S1 to S3 byte-for-byte | `DB-f-2603` | FWD-5 | WORLD | `DB-f-2501` (merged), CTO msg 10239 | R138-C |

**Four-postulate record.** (i) Domain: one inline policy of one role in one root; four statements after. (ii) Same grain: a statement. (iii) One intent: the runner may list its own output prefix. (iv) Not moved: S1 to S3, every other policy and file of the root, the role, its trust; nothing planned or applied.

| criterion | invocation | base reading |
|---|---|---|
| DBF138-3-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_inf_s4.py . DBF138-3-AC1` | FAIL (iam.tf unchanged from the pinned base) |
| DBF138-3-AC2 | `python -I .../checks/r138/p138_inf_s4.py . DBF138-3-AC2` | FAIL (S4 absent) |

## Cells 4 and 5 (added 2026-10-17 ~05:0xZ; the Cottonwood wiring, round 138 list item 1; WORLD, the infra/ floor; workstreams `F2COTTF` and `F2COTHD`)

**Authority:** the CTO's XA-20261016T224156Z-3c21 ruling (msg 10002): host (1), the landing function `irpt-cot-account-return-daily-lambda` (`account-return-daily`), CONDITIONAL on the issuer's sizing read, which is done (`R137_COTTONWOOD_SIZING_READ.md`: the role already lists and reads `fact_transactions` silver, so NO read grant; the scheduled fire read 10.7 s and 331 MB of 1,024 MB; the producer on one real day +70 MB and about 3 s); never the filled-report function. Conditions (i) any read grant scoped to Cottonwood's own prefix (none is needed), (ii) the stage runs AFTER the returns-day write is committed and its failure cannot alter the day's returns (the handler cell's planted-failure clause), (iii) the 80 percent read uses the last fires' REPORT lines with the denominator printed (done in the sizing read; the applier prints it again). Round 138 list item 1 accepted in order (msg 10145). Both cells are independent (disjoint files); the bundle cell (the function-map entry's members and pins, `DB-f-2606`) follows the handler's merge, because the pins name the handler-side producer files at a commit.

**Base drift fixed at the cut:** the retirement of the source map edited a comment and the artifact lookup in the root's `locals.tf` (sha256 `198bad3dd156..`); the round-137 TF checker's pinned base was stale and is re-pinned in `checks/r138/` (iam.tf, lambda.tf, main.tf and schedule.tf unchanged).

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `account-return-daily` Terraform root: `locals.tf` gains the table constant `irpt_arc_gold_table_transaction`, `iam.tf` gains the NEW statement `WriteTheAccountTransactionGoldPrefixOnly` (`s3:PutObject` on the one gold prefix), both by pure insertion | `DB-f-2604` | FWD-5 | WORLD | XA-3c21 | R138-D |
| The landing handler `account-return-daily/handler.py`: the guarded `account_transaction_cottonwood` import, `transaction_frame`, `emit_transactions` (never raises), the last stage of the scheduled/day/days path for the written days, a transaction-only event, and a new test file | `DB-f-2605` | FWD-5 | WORLD | XA-3c21 | R138-E |

**Four-postulate record.** (i) Domain: one Terraform root's two files (cell 4); one handler and one new test file (cell 5). (ii) Same grain: a statement; a day. (iii) One intent each: the function may write the new prefix; the function emits the day after the returns day. (iv) Not moved: every existing statement, the schedule, lambda.tf, main.tf (cell 4); the returns write, the rewrite path, every existing test (cell 5); nothing is planned, bundled or applied here.

| criterion | invocation | base reading |
|---|---|---|
| DBF138-4-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_tf.py . DBF138-4-AC1` | FAIL (both files unchanged from the pinned bases) |
| DBF138-4-AC2 | `python -I .../checks/r138/p138_cot_tf.py . DBF138-4-AC2` | FAIL (constant and statement absent) |
| DBF138-5-AC1 | `python -I .../checks/r138/p138_cot_handler.py . DBF138-5-AC1` | FAIL (no `transaction_frame`) |
| DBF138-5-AC2 | `python -I .../checks/r138/p138_cot_handler.py . DBF138-5-AC2` | FAIL (no `transaction_frame`) |
| DBF138-5-AC3 | `python -I .../checks/r138/p138_cot_handler.py . DBF138-5-AC3` | FAIL (no new test file) |

Checkers `p138_cot_tf.py` (selftest 9 arms) and `p138_cot_handler.py` (selftest 9 arms); the handler checker's positive control (a reference implementation in a scratch sibling directory) passes its source, behaviour and wiring clauses against today's handler; the base of the handler tests is 16 passed.

**Cell 6 (added 2026-10-17 ~06:0xZ; ONE order; WORLD, the infra/ floor; workstream `F2COTBN`): the Cottonwood landing function's bundle gains the transaction producer.** After `DB-f-2605` merged (92f40e64d9). `function-map/irpt-cot-account-return-daily-lambda.json` (16 files, 15 pins) gains five members, appended last and pinned: `account_transaction_cottonwood.py`, `account_transaction.py`, `account_return_daily.py` and `transaction_words.json` (all under `data/assets/scripts/gold/irpt_reporting/`) and `data/assets/scripts/lib/stream_parquet.py`. Measured by the issuer: with the five appended and the 15 existing pins UNMOVED, the attribute closure over the pinned blobs and the bundle smoke (the handler imports the producer in the packaged layout) both PASS, so no existing pin needs to move. This is the disarm evidence for `IRPT_DASHBD-D2-W2605-S1`.

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| the five new members and their pins in the Cottonwood landing function-map entry | `DB-f-2606` | FWD-5 | WORLD | `DB-f-2605` (merged) | R138-F |

| criterion | invocation | base reading |
|---|---|---|
| DBF138-6-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cotbundle.py . DBF138-6-AC1` | FAIL (files and pins absent) |
| DBF138-6-AC2 | `python -I .../checks/r138/p138_cotbundle.py . DBF138-6-AC2` | PASS at base (the closure over the unchanged entry); stays PASS with the members added |
| DBF138-6-AC3 | `python -I .../checks/r138/p138_cotbundle.py . DBF138-6-AC3` | FAIL (the handler's guarded import fails in the packaged layout) |

Checker `p138_cotbundle.py` (selftest 8 arms; a reference entry put into the file by the issuer makes all three PASS, run and restored). Four-postulate record: (i) one function-map file of 241; (ii) a member and its pin; (iii) the bundle carries what the handler imports; (iv) not moved: the 15 existing pins, every other key of the entry (including `artifact_sha256`, stamped by the applier at the build), every other file of the folder. AC2 passing at base is stated, not hidden: it guards against a re-pin that breaks the closure.

**Cell 3, closing note:** checker `p138_inf_s4.py` (selftest 10 arms; the reference insertion makes both PASS, run and reverted). The round-137 criteria `DBF137-5-AC1` and `AC2` read the pre-S4 base; AC1 (a pure insertion) and AC2 (the actions and sids) still hold after S4.
