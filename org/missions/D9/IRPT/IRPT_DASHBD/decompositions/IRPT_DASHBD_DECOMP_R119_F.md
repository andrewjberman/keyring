# IRPT_DASHBD round 119 -- workstream F-SHIP (~F2) decomposition: FWD-3 (asset-class performance and mix) and FWD-5 (transactions), the first round

Issuer `2.0.0_SA_COO~F2`, 2026-10-15 ~23:5xZ. Gate key: `<round>119</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 119**.

**Answers:** Andrew's go (`ANDREW_DIRECT_20261015_231xZ_PARALLELIZE_IRPT_SUITE_GO.md` @efdb6554ef; "stop waiting") through the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`,
Move 2 (msg 8740): `~F2` takes IRPT_DASHBD **FWD-3** (surface row S09: gold `account_class_daily`, the classes sum to the account) and then **FWD-5** (transactions browse, filter, sort, export); write surface: new portal tab sections plus their gold readers,
not the default-report files this seat already holds (`render/`, `export/`, the report mount and print). Each lane's first round is ONE issuance with its decomposition cells, fan-out cap 8. No CTO analysis answers these outcomes yet: the cuts follow the PRD
(`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` FWD-3, FWD-5, surface rows S09, S11) and what this seat measured at the cut.

## What was measured at the cut

- **FWD-3.** The gold table `account_class_daily` has a contract (`org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json` 0.1.0; columns `firm`, `account_id`, `business_date`, `asset_class` (7 classes), `market_value_eod`, `class_return_daily` (the class's CONTRIBUTION to the account's daily return), `method_version`, `coverage` (6 values)), a producer
  (`data/assets/scripts/gold/irpt_reporting/account_class_daily.py`) with tests and a prepared never-widen release (`deliverables/0.9.0_WK_IRPT_DASHBD~19/`, CTO half and COO half beside it); the contract still reads `served: false`, "no object of this table exists in any bucket"; the publisher's comment (`reporting-publish/publisher.py` line 6) says the served series
  carries no class keys; the portal holds the class vocabulary, order and colors (`tabs/holdings/assetClass.ts`). So the table is built and its apply is unmeasured; the served path and the portal section do not exist.
- **FWD-5.** `comp-find` for `account_transaction` finds no contract under `org/standards/` and no producer under `data/assets/scripts/gold/irpt_reporting/`; the PRD names the table (C-SHAPE) and the surface row S11 reads "unmeasured". The thread is unstarted.
- **PROD** is `e0e69da7766d87719571d7e6c0ccf59bf65fcae9` (read 23:5xZ). The class section is a SEPARATE feature from the default-report candidate (`cand/dell2/irpt-default-performance-report`): new files only, cut from PROD, its own candidate branch later.

## Cells (ONE issuance; every cell LOCAL)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The FWD-3 THREAD READ: the gold table's state (built, signed, applied), whether the served series carries class keys, the smallest route change, the portal's reuse, the hops from gold to the Performance tab with owner and risk each, a proposed served shape | `DB-f-601` | FWD-3 | LOCAL (a read) | none | R119-A |
| 2. The CLASS-WINDOW VIEW MODEL and SECTION: a pure model over one account's rows in the contract's columns (each class's contribution over a window, exactly summing to the account's return; the mix at two dates; the sum check; unclassified its own class; one sentence) and a section component; NEW files only; not mounted | `DB-f-602` | FWD-3 | LOCAL (portal branch only, never pushed) | none (it reads the contract's columns, not a served shape) | R119-B |
| 3. The FWD-5 THREAD READ: whether `account_transaction` has a contract, a producer, any served path; the sources and the vocabulary; the portal's reuse; the hops with owner and risk; a proposed served shape | `DB-f-603` | FWD-5 | LOCAL (a read) | none | R119-C |

**Decisions inside this decomposition (the issuer's, stated):**
(a) FWD-3 is cut as the THREAD (the spine's round 1): the read maps every hop from gold to the screen, and the build cell makes the one part that needs no server (the model and the section) so that the first served class document finds the page ready; the mount is the issuer's hookup, not cut;
(b) the model's window contribution is `sum over days of C_(t-1) * contribution_c,t` with `C` the account's cumulative factor before the day: it makes the classes' contributions add up to the account's window return EXACTLY (the PRD's "the classes add up to the account"), which a plain sum of daily contributions would not;
(c) a window with any non-measured day, or whose class values do not sum to the account at a mix date, prints words and no figure (the contract's coverage vocabulary; C-HONESTY): the model never imputes;
(d) `unclassified` is listed whenever non-zero and last in the class order (Andrew's order: Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, then Unclassified); (e) FWD-5 starts as a read because there is no contract or producer to build against: its first build is the CTO's analysis of the read;
(f) every worker holds one cell and one worktree; the two reads need no portal worktree; (g) the owners the reads find for the gold apply and the served path are other seats'; this seat does not edit the gold, the contract, the publisher or the route.

**Four-postulate record.** (i) Domain: FWD-3 and FWD-5 of IRPT_DASHBD on this seat's write surface (new files under `tabs/reporting/classes/`, two new tests, and two read records). (ii) Same grain: one account's window. (iii) One intent per cell. (iv) Not moved: the default-report branch, every contract, producer, route and served file, every existing portal file.

**Chain read.** M = 3 (no edges between the cells). N = 3.

fanout: 3 of 3 chains, cap 8, portal_ref: `origin/PROD` (e0e69da7766d87719571d7e6c0ccf59bf65fcae9) for slot ~602, none for ~601 and ~603, reason: the two reads and the build are dependency-independent with disjoint write sets (two read records; new portal files). Workers `0.9.0_WK_IRPT_DASHBD~601` (`DB-f-601`), `~602` (`DB-f-602`), `~603` (`DB-f-603`).

| criterion | invocation | base reading |
|---|---|---|
| DBF119-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r119/p119_fwd3.py . DBF119-1-AC1` | FAIL (no test file) |
| DBF119-1-AC2 | `... p119_fwd3.py . DBF119-1-AC2` | FAIL (no test file) |
| DBF119-1-AC3 | `... p119_fwd3.py . DBF119-1-AC3` | FAIL (no new file under classes/) |
| DBF119-2-AC1 | `... p119_fwd3.py . DBF119-2-AC1` | FAIL (no record) |
| DBF119-3-AC1 | `... p119_fwd3.py . DBF119-3-AC1` | FAIL (no record) |
