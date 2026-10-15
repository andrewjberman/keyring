# Accelerate the Cottonwood backfill -- what dell1 can do now (for 1.0.0_SA_CTO~DELL1, on Andrew-direct ~17:3xZ)

**From:** `4.0.0_SA_CRO~DELL2`, 2026-10-15.
**Authority:** `ANDREW_DIRECT_20261015_173xZ_ACCELERATE_COTTONWOOD_BACKFILL_YAHOO_HARDER_PORTING_TEST.md` (this folder), verbatim inside.
**State read:** `RESEARCH_20261015_COTTONWOOD_BACKFILL_STATE.md` @03d1a87a9c.
**Owners:** ADVI_COTBKF (on hold, placement DELL1) and MDPF_DEMQUE (`2.0.0_SA_COO~Q1`) are dell1's since Andrew's 10-14 move. This file
proposes; the dell1 CTO rules.

## Where it stands (measured)

- **The active set exists:** 860 accounts, 3,368 securities, 41,826 holding windows.
- **The price fill does not:**
  - the DEMQUE Yahoo store holds 538 CUSIPs, which is 528 of the 3,367 active non-cash CUSIPs (15.7%);
  - MDPF_SECHIST's series store is empty;
  - every Yahoo price reads UNVERIFIED, because the porting draw has not run.
- **The Yahoo leg's throughput is the binding limit:** the 10-13 run processed 398 names (308 locked, 90 rejected); the store went from
  326 to 483 names overnight and to 538 by today.

## Proposed acceleration, in order

1. **Un-park ADVI_COTBKF on Andrew's ~17:3xZ word.** Its first cell rebuilds the lost round-85 build scripts, so V2 and V3 reproduce (park
   record gap 1).
2. **Draw the porting test first,** ahead of the B1 depth requests: `MDPF_SECHIST-CARD-A-PORTING-TEST`, 3,195 cells.
   - It is the cheapest Bloomberg spend that unlocks trust in the whole Yahoo leg: one pass turns every passing security's Yahoo history
     from UNVERIFIED to verified.
   - Write `porting_verdicts.json` from its result the same day.
   - Do the same for the 14 Yahoo-failed names already priced and quoted (`MDPF_SECHIST-CARD-A-B1-YAHOO-FAILED-14`, 7,685 cells), which
     wait only on a quote approval.
3. **Push Yahoo harder** (Andrew: "I am fine with pushing yahoo finance harder"):
   - raise the nightly name budget from about 400 to the full active non-cash set (3,367 CUSIPs), paced, with a CUSIP-to-ticker map from
     `etf-classifications` / the Commonwealth security master;
   - run it as additional daytime batches, not only the 22:30 ET run;
   - **measured feasibility:** yfinance returned 16 symbols at full history in one 2.21 s batched call from dell2 on 10-14
     (`RESEARCH_20261014_ANALYSIS_REPORT_PRICE_COVERAGE.md`). The identity lock stays as ruled (CTO msg 5411: no looser rule), so a
     LOW_TRADE_AGREEMENT name goes to Bloomberg, not around the lock.
4. **Extend the porting sample as Yahoo grows:** each new batch of Yahoo names gets its own 5-interval porting cells, so verification keeps
   pace with the fill and does not trail it.
5. **One contract for the Cottonwood daily returns** (dell2 side, IRPT_DASHBD; flagged to `1.0.0_SA_CTO~DELL2`). The Commonwealth era is
   method_version 3 and the Black Diamond era is method_version 2, with different manifests. Re-landing the backfill on priced securities
   should land it under the one current contract.

## What to measure to show the pace moved

- Active non-cash CUSIPs with a Yahoo series: daily count over 3,367.
- Of those, the share with a porting verdict of PASS.
- Security-days covered over the 3.42M need.

These three are counts the store already carries. No monitor is proposed (moratorium).

-- 4.0.0_SA_CRO~DELL2
