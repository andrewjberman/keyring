# CARRIED -- Andrew-direct, TWR pricing on every surface: the research price axis adds a total-return field (a SITE Z cell, for round 103's issuance)

**Received:** 2026-10-13 ~16:54Z, `2.0.0_SA_COO~R1` from `1.0.0_SA_CTO~DELL1` msg 4948, which relays the rule in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md` (census row A4). **This is an Andrew-direct standing rule, not an analysis item: it is carried verbatim and cut in the
NEXT issuance (round 102 is issued; one issuance per round).**

**The words (the CTO's relay, msg 4948):** "price_axis_pull.py pulls PX_LAST only. Add DAY_TO_DAY_TOT_RETURN_GROSS_DVDS (or the total-return index) to the daily pull, at the 5-trading-day window (Z5).
It is a site Z cell; the rankings stay on price until a PRD addendum says otherwise."

**The rule behind it (Andrew, verbatim in the queue form):** "STANDING RULE: TIME-WEIGHTED RETURN (TWR) PRICING ON EVERY SURFACE. Every price series a surface keeps must support a total-return (TWR)
reading: price plus distributions (dividends, interest), not price alone." And the incremental rule: once a need's backfill is complete, every daily pull asks for the last 5 trading days
(`lib/trading_calendar.py`), not a single day and not a long window; a gap wider than 5 trading days is a targeted refill for that gap only.

**What is measured (the queue form's own census, A4):** `integrations/bloomberg/research/price_axis_pull.py` pulls `PX_LAST` only; the research app uses it for each covered company's 30, 90 and
365-day price rankings and breakout flags; about 100 covered companies; **about 500 history cells a day at 5 days**; "a served change under its own pair" (the incremental window).

**How the issuer applies it at the cut:**
1. ONE worker cell, `<risk>` per its paths (a site-Z producer file and its test are LOCAL code; the SERVED effect is the producer's next daily run, so a pair is needed before the run changes what is
   stored): `integrations/bloomberg/research/price_axis_pull.py` and `integrations/bloomberg/research/tests/test_price_axis_pull.py`. No Bloomberg call by the worker; the run is the queue's, at site Z.
2. The field is `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` (the CTO's text allows "or the total-return index": the cell's face names which one the file's request shape takes, read from the
   queue form's A1 to A3 rows, which already pull it).
3. **`integrations/bloomberg/READ_HERE.md` is read FIRST** (the two-phase budgeted sign-in; a refusal names the surface; never mint `data/bloomberg/`), and the cell states its cells-per-day arithmetic
   against the allowance.
4. **The rankings stay on PRICE** (`PX_LAST`): the cell adds a stored series; it changes no served ranking. A switch of the rankings to total return waits on a PRD addendum (the CTO's words).
5. Its close is the producer's next daily run's stored cells (a read at the queue's ledger), not a local test alone.
