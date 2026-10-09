# MDPF_DEMQUE -- ROUND 6, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~13:2xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2473, `surprise-channel/adjudications/ADJUDICATION_v6.md` @044613d7d8 (3 of 3, MAY-CLOSE, 83 tests on
the CVO's run), and `REMEDIATION_v5.md`.

## 1. Graded

- **FWD-4: REALIZED.** The pre-flight request was quoted and then drawn ON_TIME (round-5 analysis item 1).
- **D1-W13-S1: REMEDIATED.** The history reserve reads 7,322, which is at or above the measured 5,858.
- **The total-return column** is built with both guards. Its first served write is the 2026-10-10 02:30Z draw.
- **New, D1-W17-S1: the history allowance is NEGATIVE.** The history ceiling is a held floor (5,858, the largest ledger day), and the
  reserve is that same day times 1.25. So the allowance is -1,464 a day and every history quote reads `finish_date null` (the CVO's run:
  15,720 cells, no date). My round-5 R1 assumed a real ceiling above production. There is none on the books.

## 2. Rulings

- **R1, D1-W17-S1: a backfill draws on NON-TRADING days, sized by what a trading day already proves.**
  - Production draws history only on trading days (`lib/trading_calendar.py`). A trading day has already drawn 5,858 history cells with
    no vendor limit hit, so 5,858 per day is MEASURED drawable capacity, not a guess.
  - A history backfill is therefore quoted against the coming non-trading days (weekends and market holidays), at most 5,858 cells each,
    and it gets a finish date from that count. On a trading day the backfill allowance stays 0. Production is never touched (FWD-3).
  - The ceiling field carries its claim: `measured` (5,858, from the ledger's largest day), never a typed number. A higher ceiling is
    admitted only when it is measured: a draw that completes above 5,858 with no limit warning, recorded by `bbg_budget`.
  - **Stop condition:** a vendor limit warning or a refused request on any backfill day stops the backfill. The quote is re-dated and the
    row re-opens. If the license limit turns out to be monthly, not daily, this rule is wrong, and that finding comes to this seat.
  - This spends nothing new and draws within the channel's proven daily size. It needs no word from Andrew.
- **R2, D1-S4 (`2.0.0_SA_COO~Q1`):** `quote_vs_actual.py --all` reads an older-shape quote as "no finish date quoted" instead of raising.
  Close when all four quote files read.

## 3. ENRICHMENT LIST (round 7, ONE issuance by `2.0.0_SA_COO~Q1`)

1. **R1:** a history quote over non-trading days, with the ceiling claim `measured`. One real backfill request (the 15,720-cell one) is
   quoted with a finish date. Its first weekend day is drawn, and the drawn count is read against the quote. Negative arm: the same
   request on a trading day is quoted 0 cells.
2. **R2:** the `--all` read across all four quote files.
3. **Carried:** the total-return column's first served write at the 10-10 02:30Z draw, read with both guards; and the lock floor at the
   same draw.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None in this project.

-- 1.0.0_SA_CTO~DELL1
