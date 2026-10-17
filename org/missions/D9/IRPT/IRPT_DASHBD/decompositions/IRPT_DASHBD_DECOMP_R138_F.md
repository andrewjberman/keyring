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
