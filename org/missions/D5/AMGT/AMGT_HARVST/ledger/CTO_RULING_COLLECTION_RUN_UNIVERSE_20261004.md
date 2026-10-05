# AMGT_HARVST -- CTO rulings (1.0.0_SA_CTO~Z, 2026-10-04 ~23:2xZ): the lifted run's universe, and the stale closer_contract

The round-45 analysis carries both rulings.

## 1. "Universe-scope" means the RANK's universe, 191 names (msg 29308, plan @29104786ce section 2) -- option (a)

**The finding** (`2.0.0_SA_COO~H`, read-only, 0 network calls): the driver's `universe_source` is RESAPP's 89-name `universe.json`.
- Its tickers resolve for 32 and reach about 30 of the rank's 191 (`universe/v1/2026-09-16.json`). At least 102 rank names are
  outside the driver's universe in any mapping.
- So a run over the 89 names leaves every publisher `PER_NAME_TRIALS_ONLY`, the declared set stays EMPTY, and FWD-7 stays HELD.

**Ruling: (a).** The one run per publisher covers the rank's universe, 191 names.
- **Andrew's word** (record @441338fdf7) is "ONE universe-scope run per publisher". The card it answered reasoned from FWD-7's
  empty ranking and the 9 collection outcomes. "Universe-scope" is the PRD's own term: `C-HV-RANK-DECLARED-SET` says "a publisher
  has universe-scope collection when the UNION of its jobs' targets ... covers the generation's universe".
- **No new mechanism:** the change is `universe_source` (config) and identity resolution, on the same driver and collector.
- **No recurring cadence:** one run per publisher.

**Conditions:**
1. **Resolution before any request.** The cell resolves all 191 names to the collector's job keys (the same `gold_security_key` the
   declared-set reader joins on, traced through `worker.py:467`) and prints 191 of 191. A name it cannot resolve is a STOP before
   the run, named in a row. A run that leaves any rank name uncovered cannot make the declared set non-empty, so it would spend
   vendor egress on a claim it cannot meet.
2. **The sa bound is stated before the GO.** It is printed beside the 89-name bound: 191 x (200 pages + 20 candidates) = 42,020
   requests at most, about 9.7 days at the 4,320/day pacing. The 2026-01-01 floor stops most names far earlier. Pacing, caps and the
   floor stay as configured; nothing is raised for speed.
3. **Order:** FWD-12 graded DONE (round 45), then the ar-1 silver write verified (CTO half @16eb97eae5 condition 1), then the run.
   It is cut in the round-45 analysis's enrichment list under its own never-widen pair: bronze and silver append through the
   uploader, plus run records.

## 2. Retire `closer_contract` on AMGT_HARVST (msg 29309) -- REMOVED in this commit

- **Why it stayed:** `HANDBACK_TO_CANONICAL_20260924.md` kept it ON only because H03 2a was mid-apply under ledger
  `amgt-h03-leadpanel-y-20260924`.
- **That entry CLOSED** @64df5daa18 (`3.0.0_SA_CVO~Z`, 2026-09-24 10:18Z), and rounds 39-45 ran canonically.
- The field now only puts HARVST in `/canonical-drive`'s skip set for a fresh COO session. It is removed from `project.json`.
