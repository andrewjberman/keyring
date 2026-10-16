# IRPT_DASHBD round 121 -- workstream F-SHIP (~F2) decomposition: the class-series reader

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~02:3xZ. Gate key: `<round>121</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 121**.

**Answers:** the CTO's open-call ruling 3596 (msg 8826, item 3: `~F2` builds only the reader and the tab). The CTO's round-120 analysis for F-SHIP (msg 8917) arrived AFTER this cut and names two further cells for "round 121": the FWD-5 words proposal and the `AssetClassSection` mount. The gate (ONE ISSUER PER ROUND, `to-pipeline-gate.py` GATE x) refuses a second order in a round that has an issuance, so those two cells are cut in the NEXT issuance (round 122): the mount after `DB-f-801` lands (it stacks on the reader's branch), and the words proposal in the same issuance. This is the cost of cutting before reading the analysis: the words cell, which depends on nothing, starts one drain later than it could have.

## What was measured at the cut

- The class model and section are built and unmounted (round 119, portal `7fa808c9`). The model reads `ClassDailyRow[]`; nothing produces those rows from a fetched document.
- `~D2` named the object (`class_series.json.gz`), the contract section (`class_object` 0.4.0, `~D2` sole writer) and the columnar shape (msg 8846); `~S2` named the route key (`which=class_series`, msg 8848) and will cut the `OBJECTS` member when the 0.4.0 file is committed. Nothing is served and the 0.4.0 file does not exist yet.
- So the reader is built against the NAMED SHAPE and refuses anything else (a partial or misaligned document is `null`, never a guess).

## Cell (ONE issuance; LOCAL)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The CLASS-SERIES READER and its tests: path, columnar-to-rows conversion, absent answers; new files only, not mounted | `DB-f-801` | FWD-3 | LOCAL | none | R121-A |

**Decisions inside this decomposition (the issuer's, stated):** (a) NOT mounted: the mount in `ReportingTab.tsx` waits until a route serves a sample and until the default-report candidate is re-cut (both touch the tab); (b) the portal worktree is cut from the class candidate, so the reader sits one commit above the model it feeds; (c) when `~D2`'s 0.4.0 file is committed this seat compares it with the shape in the order and amends the reader in a small change if they differ; (d) one cell of three or fewer mechanical criteria (two).

**Four-postulate record.** (i) Domain: one reader file and one test file. (ii) Same grain: one account's document. (iii) One intent. (iv) Not moved: the model, the section, the tab, every served file and the route.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 8 (the CTO's CPU budget holds `~F2` at 4 per issuance), portal_ref: `cand/dell2/irpt-asset-class-performance` @7fa808c949fbe5d9c9d4ea1aea3aa3006be7d2e8, reason: one independent cell, new files only. Worker `0.9.0_WK_IRPT_DASHBD~801` (`DB-f-801`).

| criterion | invocation | base reading |
|---|---|---|
| DBF121-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r121/p121_reader.py . DBF121-1-AC1` | FAIL (no test file) |
| DBF121-1-AC2 | `... p121_reader.py . DBF121-1-AC2` | FAIL (no change) |
