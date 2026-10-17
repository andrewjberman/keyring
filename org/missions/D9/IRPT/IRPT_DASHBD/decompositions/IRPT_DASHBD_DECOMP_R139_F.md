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
