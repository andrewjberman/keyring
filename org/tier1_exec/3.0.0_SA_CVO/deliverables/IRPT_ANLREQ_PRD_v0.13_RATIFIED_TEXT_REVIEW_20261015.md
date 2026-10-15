# IRPT_ANLREQ PRD v0.13 -- L4-R review, ratified-text half

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-15 ~15:2xZ. **Delivery:** msg 8386. **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @43c7157f1f (half_hash 912c1533c941). **Compared against:** v0.12 @cea3f6d497.
This seat's note on v0.12 is msg 8382.
**Authority read:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_175xZ_PRICE_ORDER_YAHOO_THEN_YCHARTS_THEN_REPLACEMENT.md`
("we use Yahoo as first round pick, we use Ycharts as second round pick ... then we generate the report without the missing security"),
and the CTO price ruling ADDENDUM 2 @ac60268494.

**Verdict: SIGN, with one point owed at the next bump.**

- **FWD-7** now states Andrew's 10-14 17:5xZ order per security:
  - the estate's stores;
  - Yahoo, cut at T-1;
  - YCharts through the stored session, one symbol per call;
  - the backend replacement C-SWAP;
  - else the report runs without the security and says so.

  Bloomberg is out of the chain, and there is no YCharts report, figure or PDF. ACCEPT checks that each price carries its source and that
  an unpriced security is named. A build to the CTO's ruling can now meet FWD-7.
- **The C-PRICES row** says the same, step for step, with its source as a claim field. It now agrees with FWD-7.
- **C-FILING-HINT** has its table row:
  - ONE suggestion;
  - exact CUSIP or ISIN first, then ticker edit distance, then name;
  - nothing is replaced without the filer's click;
  - swaps are never on the form;
  - no new vendor call at filing.
- **Unchanged:** FWD-1 to FWD-6 and every other CONTRACTS row are byte-equal to v0.12.

**Owed at the next bump (not a reason to refuse).** FWD-7's SOURCE still reads only "relaxed for pricing data by Andrew-direct 2026-10-14
~15:5xZ ('I am ok with a single data call to YCharts for pricing data.')". That quote now contradicts the DONE WHEN, which makes one
YCharts call per symbol. The word the new text rests on, 10-14 ~17:5xZ, is not cited there; the C-PRICES row cites it. Add the 17:5xZ quote
to SOURCE, and mark the 15:5xZ "single call" as superseded on the call count.

-- 3.0.0_SA_CVO~DELL2
