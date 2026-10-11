# MDPF_DEMQUE -- ROUND 7, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~04:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3478, `surprise-channel/adjudications/ADJUDICATION_v7.md` (3 of 3, MAY-CLOSE, every criterion
re-run green on the CVO's run), and `surprise-channel/remediations/REMEDIATION_v6.md` @9b4a3a9a86 (6 rows graduated INERT). Calendar per
`lib/trading_calendar.py`: 2026-10-09 Fri trading, 2026-10-10 Sat and 2026-10-11 Sun non-trading, 2026-10-12 Mon trading.

## 1. Graded

- **FWD-3: APPLIED, not yet REALIZED.** The t24 backfill drew 5,858 of 5,858 cells on Saturday 2026-10-10, a non-trading day, at
  the measured ceiling (receipt DRAWN, 0 diagnostics over 38 chunk attempts). A trading day quotes 0. The ACCEPT's next-morning
  production read is Monday 2026-10-12, so FWD-3 grades on that read.
- **FWD-4:** REALIZED at round 6; unchanged.
- **FWD-1, FWD-2, FWD-5 to FWD-9:** not graded this round; the round-6 reads stand.
- **C-PRICES (Andrew-direct v0.5, total return on every price table):** served is 109 of 141. 32 files still carry the original 3
  columns (all last-modified 2026-10-09), so C-PRICES is NOT met (row D1-S8). No FWD graded this round reads those 32.
- REMEDIATION_v5 D1-W17-S1 and D1-S4 are REMEDIATED.

## 2. Rulings

- **R1, D1-W19-S1 (this seat): the non-trading-day walk depends on the request's TIER, not on claim states.**
  - Today the walk runs only when the history ceiling's claim is `measured` and the reserve's is not
    (`data/mdpf/scripts/demque/bbg_quote.py:240`). Measuring the reserve would silently send backfills back to the weekday rule,
    and they would then draw on trading days. That contradicts round 6's R1, which keeps production untouched on a trading day
    (FWD-3).
  - **The rule:** a history request of tier 2 or above (a backfill) is ALWAYS quoted over non-trading days, at the measured ceiling,
    whatever the reserve's claim. A tier-1 history request (production) draws against the reserve on any day, which is D1-S5's
    remedy, and the two rows are cut as ONE change to that branch.
  - A backfill whose ceiling is NOT `measured` gets no finish date: `finish_date null` with the reason "ceiling not measured". It
    never falls back to the weekday rule, because the ceiling is only ever a measured figure (round 6 R1).
  - `test_demque_bbg.py`'s weekday expectation for a backfill is amended to match.
- **R2, D1-C-S17 (this seat): a quote frozen before a rule change is RE-FROZEN under the rule in force, and the old one is kept.**
  - The TR request was frozen @70379bb41d under the retired weekday rule (finish 2026-10-13). The rule in force is round 6's R1.
    Grading LATE against a rule this seat retired would measure the retired rule, not the pacer.
  - **The re-freeze** happens at round 8's issuance. It writes the new quote beside the superseded one, which is never deleted: the
    superseded quote is printed with the reason "rule changed, round 6 R1" and its date. `quote_vs_actual` grades the re-frozen
    quote and prints both.
  - **A quote promises only days a drawer will draw.** The walk counts a non-trading day only when a scheduled drawer runs on it. A
    finish date that assumes a weekend nobody draws is a false promise; that is how 2026-10-11 would be counted today.
  - **The drawer is the queue's own, and it is STANDING.** A scheduled drawer runs on every non-trading day, where t24 ran (site Z,
    the Bloomberg terminal box). It draws open backfill requests in rank order up to the measured ceiling, stops on a vendor limit
    warning or a refused request (round 6 R1), and writes the receipt and the `BBG_ACTUALS.jsonl` line t24 wrote.
    - It is a production schedule, not a one-shot, because production pipelines are scheduled (CLAUDE.md section 5).
    - It is not a second pipeline: it is the queue's existing draw step (S09) on its own clock.
    - Bloomberg pulls through this queue need no per-use word (CLAUDE.md Agent Autonomy). The derived layer stays current-day-only
      (`integrations/bloomberg/READ_HERE.md`).
  - The remaining 9,862 cells draw on the drawer's first two scheduled non-trading days: 5,858, then 4,004.
- **D1-S8 placed (`2.0.0_SA_COO~Q1`): the 32 files are RE-DRAWN, not re-written from stored rows.** A 3-column file holds no
  dividend or adjustment data, so total return cannot be derived from it. The 32 symbols are enqueued for one paced Yahoo re-draw
  through the shared pacer (C-YAHOO); Yahoo needs no per-use word. The row closes on a served read of 141 of 141 files with seven
  columns.

## 3. ENRICHMENT LIST (round 8, ONE issuance by `2.0.0_SA_COO~Q1`)

1. **R1 + D1-S5, one change to `quote()`'s history branch.** Criteria:
   - (a) a tier-2 history quote with BOTH ceiling and reserve claims `measured` still walks non-trading days only;
   - (b) a tier-1 history request quoted for Monday 2026-10-12 reads a positive `allowance_today` and finishes that day;
   - (c) a tier-2 quote with the ceiling not `measured` reads `finish_date null` with its reason. Negative arm: the same tier-2
     request on a trading day quotes 0.
2. **R2, the standing non-trading-day drawer at site Z,** under its own never-widen pair, cut as an XB order to the site-Z CloudOps
   seat that ran t24. Criteria:
   - (a) the schedule reads one fire per non-trading day for the next 14 days (`lib/trading_calendar.py`);
   - (b) its first scheduled fire draws, writes the receipt and the ledger line, and the drawn count equals the quote's day share;
   - (c) the TR request is re-frozen with the superseded quote kept, and `quote_vs_actual` grades the re-frozen quote.
3. **D1-S8:** the 32 symbols re-drawn through the pacer. Criterion: the served read reads 141 of 141 with seven columns.
4. **D1-S6 (`~Q1`):** `bbg_ledger_upload.py` resolves a Name-to-literal assignment before `literal_eval`. Close as the row states.
5. **D1-S7 (`~Q1`):** `land_cot.py` reads the consumer's key through the `lib/opal_naming` legacy address. `pytest
   data/mdpf/scripts/demque` collects with no INTERNALERROR. This is repo-wide hygiene: it rides the drain, not a build criterion.
6. **Carried, a read only:** FWD-3's Monday 2026-10-12 morning production read grades FWD-3.

**Expected next demand:** AMGT_RESAPP files one reference request for CRNCY over its scanner universes (its round 90). It enters
the queue like any request and is ranked and quoted. It is not a cell of this project.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None in this project.

-- 1.0.0_SA_CTO~DELL1
