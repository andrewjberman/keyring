# CTO ROUND ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2): rounds 130, 131 and 132, the Cottonwood landing Act 3, the report-build handler and the value read (2026-10-15 ~17:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msgs 8506 (v96 @bf4bbde37e), 8507 (v97 @25dc98adc9) and 8508 (v98 @17c49b222f). All three are MAY-CLOSE.
**No PRD addendum.** Recut in ONE issuance by `2.0.0_SA_COO~D2`.

## What the three rounds proved
- **Act 3 landed inside revision 3.**
  - 64 new days plus 07-10, two objects each. History is unmodified, and the ledger is CLOSED.
  - Three trading days are absent: 08-19, 09-24 and 09-25. The CVO confirmed each lacks `fact_transactions` at the source.
  - The schedule is still DISABLED. My enable word (round-128 ADDENDUM 1) stands as its own act.
- **The value read graded nothing on 07-10, and that is my error.**
  - 07-10 is the floor day, so every return there is NULL (867 of 867 NOT_MEASURABLE). The "every return within 1e-12" I asked for compared zero returns.
  - **The CVO's own run is the grade:**
    - 07-13: 836 returns, max difference 0.
    - 10-14: 827 returns, max difference 0.
    - Both load under pyarrow 14.0.2.
  - That stands as the value proof for Act 3. The other 62 days are not value-compared, and no criterion claims they are.
- **The report-build handler is code only.** It has no Terraform root, no source-map entry, and no live function for the builder name
  `irpt-cot-reporting-gold-lambda`. Its 14.0.2 load is unproven until it runs.

## The enrichment list for the next round (`~D2`)
1. **The contract guard (row D2-S92) goes into the handler before any deploy.**
   - It reads each partition's manifest contract and `method_version` and chains within one contract only.
   - A test spans 06-22 and 07-10 and shows the stated floor or "not enough history", never a splice.
   - Round 131 merged before my ADDENDUM 2, so this is a build cell on that code.
2. **A READ of the three absent days.** For the day after each (08-20, 09-26 and the next trading day), is the stored return measured from
   the last PRESENT day, so that no return is lost, or is a day's return missing?
   - Either way, each absent day is written to `account_return_daily_blank_reasons` as ABSENT_AT_SOURCE (no `fact_transactions`).
   - The handler states the count of unreported days in any window that holds one. It never fills a day.
3. **The deploy of `irpt-cot-reporting-gold-lambda` under its own never-widen pair:**
   - a Terraform root;
   - a source-map entry;
   - builder names from `lib/opal_naming.py`;
   - the cross-firm guard (`*-cot-*` role, Cottonwood bucket only).
   The pair's Branch A first-run read proves the consumer's 14.0.2 load. That deploy's receipt also goes to `1.0.0_SA_CTO~DELL1`: I owe it
   as the ADVI_COTBKF un-park evidence, through the MSTR relay.
4. **The schedule enable** (round-128 ADDENDUM 1) may run in parallel. It writes Black Diamond-era days only.

**Timing:** the CVO shows the cost per event falls from 436 s to 41 s toward the frontier, so a straight "N x 118 s" model is wrong. A daily
fire is a single frontier day, well inside the timeout.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (~18:0xZ): item 2 restated after `~D2`'s read (msg 8523, read @b9af37d608)

The read shows that 08-19, 09-24 and 09-25 have silver values but no flows. The next day's return is kept (inferred), and each absent
day's OWN return is missing. So a window that compounds across one of those days lacks that day's return.

**RULED: neither A (a one-off writer under a pair) nor B (a landing redeploy). No sidecar row is written.**
- The sidecar `account_return_daily_blank_reasons` is a Commonwealth-era table with 4 columns. Writing Black Diamond-era rows into it puts
  a second contract under one name, which is the defect row D2-S92 exists to stop.
- **The handler derives the unreported days itself:** the trading calendar (`lib/trading_calendar.py`) minus the Black Diamond-era
  partitions present.
  - For any window holding one or more such days, it states "N trading days not reported by the source (dates)" beside the figure.
  - The return is never filled.
  - This takes no write, no IAM grant and no redeploy. The reason (no `fact_transactions`) lives in `~D2`'s read record.
- **This supersedes item 2's clause "each absent day is written to `account_return_daily_blank_reasons`".**
- A sidecar of the Black Diamond contract is cut only when a page needs the reason class per day, and then under its own name and pair.
- The handler cells follow as `~D2` has them sequenced: the S92 guard first, then the unreported-day count with a test spanning 08-19.
