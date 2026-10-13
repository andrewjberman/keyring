# ADVI_BDPRCE -- ROUND 1, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~19:3xZ)

**Input:** `3.0.0_SA_CVO` slug msg 5102, `surprise-channel/adjudications/ADJUDICATION_v1.md` and `remediations/REMEDIATION_v1.md` @4d3a201022. MAY-CLOSE.
- All four read-only orders hold on the CVO's own runs:
  - BP-a-1: writers = 6, unidentified = 0;
  - BP-a-2: trace selftest, 7 arms;
  - BP-a-3: served 1,657, equal 1,148, explained 429, unexplained 64;
  - BP-a-4: the thread, 4 trades, equal.
- 27 rows: 7 ARMED graduated (disarm owner `2.0.0_SA_COO~K1`), 8 INERT graduated, 12 dismissed.
- **Nothing served moved in round 1, and nothing moves in round 2 without Andrew's before/after review (FWD-7).**

## 1. Graded

| FWD | Verdict | Read |
|---|---|---|
| FWD-1 | NOT YET | The thread re-reads live (168.94 from ONE transaction_id), but its exemplar is not truly unlisted (W4-S9, a ticker-mapping gap) and the served tie is unruled (W4-S5). Item 3 below. |
| FWD-2 to FWD-9 | OPEN | Round 1 was read-only. THE rule is written (`ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md` @cd65a96bb6) but not built. |

## 2. Rulings on the rows sent to this seat

- **W3-S3, "which rule is THE rule": ANSWERED by R1** (@cd65a96bb6):
  - the median of DISTINCT trades (each `transaction_id` once);
  - trades only, at the executed price;
  - dividends and every non-trade row excluded;
  - ties broken by SOURCE_RANK, then a stable sort.
  Nothing new is ruled here.
- **W3-S4, cash-dividend rows set a per-unit price of 1.0 and dominate the median:** this is exactly what R1 excludes. Building the rule (item 1) removes it from every price
  it touches, and the before/after list shows each one.
- **W2-S3 / W4-S3 / W4-S5, same-date daily-versus-canonical disagreements, and the ESTIMATED prices on served rows** (`linear_interpolation` in canonical, `carry_forward` in
  the daily file). Under Andrew's "any estimation is highly risky for performance reporting that needs to be exact":
  - **Interpolation is BANNED.** No served price is a value no trade produced.
  - **Carry-forward is permitted ONLY as what it is:** the last observed rule price, carried with its own observation date ("last traded <date>"), never presented as that
    date's own price. A date with no trade in the window has no new price; it shows the last one with its date.
  - The daily file and canonical are reconciled by building ONE rule in ONE place (FWD-2), not by choosing a side per row. The S33 re-read is folded into item 1's replay.
- **W4-S2, 61 of 586 sampled untickered lots priced off no canonical row:** a full read-only census over all 3,509 objects is item 2.
- **W3-S2, daily price files missing on six trading days (all Mondays or Tuesdays), and W4-S1, served detail objects one trading day behind T-1** (confirmed with
  `lib/trading_calendar.py`): the cause is read and named before any fix (item 5). The trading-day pattern points at the post-weekend run, but that is not yet measured.
- **W4-S6, the trace instrument reads the daily row while the served lot reads canonical:** the trace must read what the served object read, or FWD-3 cannot be graded
  (item 4).
- **W4-S9, the exemplar is not truly unlisted:** FWD-1's thread is re-drawn on a holding with no ticker in ANY source (item 3).

## 3. ENRICHMENT LIST (round 2, ONE issuance by `2.0.0_SA_COO~K1`)

1. **BUILD THE RULE in ONE place (FWD-2, FWD-4, FWD-5, FWD-6), with NO served write.**
   - One function implementing R1 exactly, on trade_date (DEC-6).
   - Replayed over every served 49F price (the 1,657) to produce the BEFORE/AFTER LIST: each price that would change, from what to what, and why (the trades), with
     W3-S4's dividend rows and W2-S3/W4-S5's estimated rows called out.
   - Determinism arm: two runs, byte-equal. Past-date arm: a date's figure reads that date's trades.
   - The list is what Andrew sees for FWD-7. Nothing is served until he has seen it.
2. **THE W4-S2 CENSUS:** all 3,509 untickered objects, each priced from a canonical row or named as not, read only.
3. **FWD-1's THREAD on a truly unlisted holding** (no ticker in any source; W4-S9). Its served price is traced to R1 and its distinct trades, with the W4-S5 tie ruled by R1's
   tie order.
4. **THE TRACE INSTRUMENT reads what the served lot reads** (W4-S6), with a negative arm: the daily row and the canonical row disagree, and the trace follows the served one.
5. **THE MISSING DAILY FILES (W3-S2) AND THE ONE-DAY-BEHIND DETAIL OBJECTS (W4-S1):** the cause read from the producer's own schedule and logs against the trading calendar.
   No re-run; the fix is a later cell once the cause is named.
6. **EXACT LOT UNITS AND COST (FWD-9):**
   - turn on `Units` (column 15) and `Cost Basis` (column 16) in 49 Financial's Black Diamond unrealized export template
     (`data/black_diamond/scripts/bronze/templates/unrealized.json`, today `isSelected: false`; Cottonwood's template already has them `true`);
   - it is an additive bronze change under its own never-widen pair;
   - the first export's lots are read against the custodian's exact lots (Schwab ULN/RLD) on a sample.
   Until it lands, the capped lots stay UNVERIFIED (Andrew 2026-10-13).

## 4. ACTS ONLY ANDREW CAN DO (cited)

- **FWD-7:** his read of the before/after list (item 1), before any served price moves. Not yet: the list is round 2's output.

-- 1.0.0_SA_CTO~DELL1
