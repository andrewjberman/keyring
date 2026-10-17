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
