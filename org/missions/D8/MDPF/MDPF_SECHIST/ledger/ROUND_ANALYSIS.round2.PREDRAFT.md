# MDPF_SECHIST round 2 -- the CTO's L10 answer, PRE-DRAFT in two branches (NOT ISSUED)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:1xZ, under fold `CTO_FOLD_UNBLOCK_RIVALS_CORPUS_SECHIST_20261009.md` section 3
(UB-20261009T035455Z-cbf8). **Status: DRAFT.** It is issued as the round-2 analysis only after TO-SH-t3 and TO-READ-R2-L3 are terminal
and the CVO's slug arrives. The branch that applies is chosen by that slug, never by this draft. Base: PRD v0.2 section 3, round-1
analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECHIST_ROUND_1_20261008.md`.

## Branch selection (one read)

The 2026-10-09 07:00 ET (11:00Z) scheduled pull ran unassisted and the TO-SH-t3 reader graded every FWD-1 hop (class, sector, clean
name, windows) on one security an Opal ETF bought the day before: **PASS**. Anything else: **FAIL**, with its cause named (A or B below).

## PASS -- FWD-1 REALIZED; round 3 enriches

Coverage: FWD-1 REALIZED. FWD-7 graded from TO-READ-R2-L3's run record (the rows drawn beside the bbg_budget remainder). FWD-2 stays
NOT STARTED: card A is Andrew's named hold ("I will handle that with sitez").

Round-3 enrichment list, ONE issuance by `2.0.0_SA_COO~H1`, at most three mechanical criteria per build order:
1. **FWD-4 + FWD-5, the gap record and blank-over-gap** (backlog item 1). The stored range, the required range and the missing days
   per tracked security. A window over an unfilled gap serves blank. The next run fetches the missing days through the queue.
   Negative arm: one planted gap read blank, then read filled.
2. **FWD-3, where each security entered** (backlog item 2, entry half only). Each source (Opal ETF, client account by firm, rival fund)
   and its required depth, with the deepest rule shown governing. The depth BACKFILL (FWD-2) is not cut: card A is held, and
   Cottonwood waits on ADVI_COTBKF.
3. **FWD-6, non-ticker instruments** (backlog item 3). The key forms the table holds that are not tickers, each resolved to one
   identity or listed as unresolved.
4. **FWD-9, the money-market rule** (backlog item 5). The vendor's daily-return field is empty on the week's first trading day.
   The rule states what is served on that day, and Monday 2026-10-12 is its live read.
5. **FWD-7, the budget ledger over the history legs** (backlog item 4), only if round 2 graded FWD-7 below REALIZED.

Not in round 3: FWD-8 (backlog item 6) goes with MDPF_SECCLASS FWD-5 and is cut when that lands. FWD-2 waits on Andrew's card A.
Every Bloomberg draw in any cell goes through MDPF_DEMQUE's queue (law 4d77a9c3ea).

## FAIL -- FWD-1 NOT REALIZED; no enrichment

- **Cause A, the pull did not reach Bloomberg** (Terminal signed out, session failure, exit 97). Re-arm TO-SH-t3 on the next
  scheduled pull, Monday 2026-10-12 07:00 ET (`lib/trading_calendar.py`; 10-09 is a Friday). Run the site-Z sign-in pre-flight
  before it, as in the fold's section 0. No ad hoc pull counts (ruling cb6fb2a52c). No round-3 cell.
- **Cause B, the pull ran but a FWD-1 hop failed.**
  - A name hop failure is a MDPF_SECCLASS row: TO-SC-e74's `clean_name()` landed @418afb65e4. A legacy form token such as
    "Lenovo Group LTD" goes there if the TO-SH-t3 reader rules it non-clean.
  - A class, sector or window failure is ONE SECHIST repair cell on that hop, at most three criteria, re-read on the next scheduled
    pull.
  - Round 3 then carries that cell only.

Either FAIL cause: FWD-3..9 keep waiting, because each round enriches only once the thread runs (spine v3.16-3.18).

## DRAFT AMENDMENT 1 (~04:2xZ) -- on the CRO's substrate note (`4.0.0_SA_CRO~DELL1` msg 1673, @47baa5efca, section 5)

- **FWD-9 takes route 2a.** C-MMF's ratified text stands, and the pull gains the field. FWD-5 and FWD-9 stay two cells. Route 2b would
  change ratified text for one fewer cell, which is not worth reopening a signed half.
- **FWD-6 (PASS item 3) is cut as a read-only census first.** It records which writer mints `NAME::` keys, the population per writer
  (5,673 today) and whether any hop carries such a key to the pull label or the join. Whether `NAME::` is a canonical key form is an
  MDPF_SECCLASS ruling this seat makes on that census. FWD-6's build cell follows that ruling and is not cut before it.
- **FWD-2's Cottonwood id join** (read-only, not under card A's hold) may be cut as one read cell in PASS item 2. Card A's Bloomberg leg
  stays held for Andrew.
- **Casing (`2.0.0_SA_COO~H1` msg 1635):** a legacy form token such as "LTD" is clean for FWD-1. Casing across screens goes with FWD-8
  and MDPF_SECCLASS FWD-5, as above.

## DRAFT AMENDMENT 2 (~04:3xZ) -- open call dell1-20261009T042652Z-813c (`2.0.0_SA_COO~H1`): may round 3 modify the daily pull?

**Yes, both, as two cells under the PASS branch:** (a) the FWD-5 gap record plus the widened next-run request, and (b) the one added
total-return level field (FWD-9 route 2a). Conditions:
- `integrations/bloomberg/pipeline/etf_daily_pull.py` is a site-Z producer path, so each cell's deploy carries a never-widen pair with
  `1.0.0_SA_CTO~Z`'s half. The apply runs where the producer runs; site-bound applies go through `~ZQ`/`~ZV` per ADDENDUM 2 of the
  dell1-deploys record.
- The widened request and the added field each change the day's Bloomberg draw, so each is quoted on MDPF_DEMQUE's books before its
  first run, and the pair names the per-run row and field delta.
- Neither cell is cut before the round-2 FWD-1 read (PASS branch only).
