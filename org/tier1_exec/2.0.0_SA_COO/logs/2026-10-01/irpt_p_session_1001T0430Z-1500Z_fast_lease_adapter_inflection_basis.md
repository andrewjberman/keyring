# The Inflection gold was dated a day late and its basis is not one seam; three packets applied; the rebuild still finishing -- 2.0.0_SA_COO~P

**Date:** 2026-10-01 (04:3xZ to ~15:0xZ; relaunch on Andrew's word, FAST lease IRPT_BCKEND~P)
**Task Order:** ad-hoc under the CTO's ruled queue (RULINGS batches 61-67, 79-81, 84, 88); IRPT_DASHBD workstream B as issuer
**Status:** IN PROGRESS

---

## Objective

Drive the CTO's ruled queue for IRPT_BCKEND workstream ~P in FAST mode: close the service-principal hole on the served boundary,
stop the reopen of retained vendor figures, and take Inflection's holdings-basis Performance from "gold dated wrong" to "rebuilt,
reproduced by hand, ready for its serving packet".

## What landed (served or data; each under both halves where a served table moved)

| act | when (Z) | proof |
|---|---|---|
| service-principal boundary on six tenant-selecting functions (packets 1, 2) | 05:23 to 06:31 | row S248; ledger closed 12/12 |
| 49 Financial holdings gold `date=2026-09-29` (7,559 rows) | 07:13 | ledger closed @a7a6c3622f |
| irpt-performance-adapter: a retained vendor figure no longer reopens; one code for "not yet on the holdings basis" (packet 3) | 08:20:26 | row S249; harness on the deployed bytes, six rows |
| NNA excusals for 866, 769, 1096 on 2026-09-24 put on the INF runner | 10:27:12 | chain ran 65 of 65; row S256 |
| silver `fact_positions/date=2026-08-06` and `date=2026-09-29` admitted from their coerced files | 12:33, 12:50 | leg A1 closed; leg A2 open for the 15:00Z ETFS listing |
| Inflection holdings gold rebuilt at emission 1.2 | 11:40 onward | 1,412 of 1,616 partitions at 14:34Z; 2020 finishing |

Source on CLOUD, not served: `sources.json` 1.2 with `partition_close` and `link_across_gaps` (de3d423dce); the adapter's
linked-row handling (89b5a85abe); the mirror's unknown-key SKIP and second INF schedule (2e00498347).

## What was found

1. **Inflection's close basis is not one seam.** Every trading-day partition 2024-07-11..2026-09-25 was graded against the Schwab
   own-date close (555): own-date to 2026-05-04, prior-day from 05-05, own-date again 07-13..07-15, three partitions holding no
   single close, two absent. A weekend sweep and thirteen sampled days had all agreed with "one seam". The first rebuilt partition
   proved the old defect directly: the new 2026-09-24 equals the old build's 2026-09-25 on 792 of 792 accounts.
2. **The live adapter reopened all three retained vendor-figure reports** until 08:20Z (measured before and after on the bytes).
3. **Stale gap-day partitions are worth two points.** With the three old-build rows still in the table, the candidate adapter's
   year to date for one account reads 0.36 percent; without them 2.40. Disposition asked of the CTO (a delete needs Andrew).
4. **A coerced file is not always equal to its raw file**: 2026-07-02 differs on 4 of 59 columns in 9 rows (row S250), so
   2026-07-01 was not admitted.
5. **The mirror counted the whole cycle's failures on every row**: a failed copy on the orion row raised a conservation failure
   naming the eclipse row. Found by the new test, fixed in source.
6. **A second reader**: `inf-etf-ownership-daily` reads the same silver table, so admitting 2026-09-29 writes an ETFS slice. Named
   in the packet; site Z answered through `0.0.0_AB_MSTR`.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | token census for `partition_close`, `OWN_DATE`, `PRIOR_TRADING_DAY`, `NO_SINGLE_CLOSE` | PASS | found the estate's existing `prior_trading_day` mechanism and `vendor_asof_registry.yaml` |
| comp-find | readers of `silver/fact_positions` | PASS | found the ETFS reader the admission packet had to name |
| comp-find | `alien_surplus` readers | PASS | 8 hits, 2 files, no code consumer |
| comp-pipescript deployed | the NNA excusals json | FAIL | does not cover `lib/*.json` (0 of 104 matched); sha256 readback used instead |
| rail (Bash hook) | several denials | PASS | each denial aborts the whole call; gated reads were re-run in their own call |

**What worked:** the token census turned up the estate's own Orion date mechanism before a second one was written.
**What failed:** `comp-pipescript deployed` has no verdict for a non-script file under a code prefix.
**Gap found:** no tool answers "which close does this partition hold"; four instruments now sit in `IRPT_MVP_P/`.

## Mistakes of this session, stated

- A commit subject names rows S253/S254; the rows are S254/S255 (another seat's row landed between my read and my append).
- I typed a message id (103798) without reading it; corrected in the next message (it was 103801).
- A second rebuild driver was started while the first was still alive (the harness reported its task stopped; its shell was
  not). Two runs of one chunk overlapped for about five minutes before the second was stopped. Same bytes, no data effect.
- One message carried a clock time a minute ahead of its own send.

## Open at this writing

- Rebuild leg R1 (2020 months running), then V1; the three stale partitions' disposition (CTO ask 103801).
- Admission leg A2: the 15:00Z ETFS listing, to `0.0.0_AB_MSTR` for site Z with the CTO copied by path.
- IB-pr-221's serving packet (adapter members `installed.py` and `holdings_gold.py`, the IAM read grant on the Inflection gold,
  the producer Lambda at the 1.2 pair with an `orion` schedule entry): waits for the PRD addendum (ruling 23) and the stale
  partitions. The mirror's release follows it.

## Push state

LOCAL throughout. origin/CLOUD 0abf99fcd4 by `git ls-remote`, last read 13:3xZ. This seat does not push.
