# ANDREW-DIRECT 2026-10-09 ~06:0xZ -- the holdings NO-WORSE check becomes a publish gate in the producer, for ~P2

Channel: dell2 terminal of 4.0.0_SA_CRO~DELL2, in-session.

VERBATIM:

> I like your approach of checking if things get "worse" but i need to understand exactly what that means and how that is
> maintained over time

> Yes I like that idea, run that over to CTO for fold in for ~P2 workstream

"That idea" is the gate this seat described in-session, specified below for the fold.

## What exists (measured)

- **The check today:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/e62e56_post_fire_read.py`, a manual pin/read
  pair around each weekday 10:15 ET `irpt-holdings-snapshot` fire. It was written for the SECCLASS e62/e56 release (CTO
  AMENDMENT 2 and 2.1). The CTO ruling `CTO_RULING_IRPT_BCKEND_M2_UNBLOCK_UB_32d8_20261009.md` AMENDMENT 1 reads it once
  more on 2026-10-09 14:15Z and then RETIRES it.
- **"No worse" (Branch A, per firm):**
  1. reconcile difference <= 0.01;
  2. 0 `multi_asset`;
  3. 0 classes outside the six (cash, fixed_income, equity, structured, alternatives, commodities);
  4. no security classified at the pin is unclassified after the fire.

  New unclassified positions are listed, not graded. A firm that did not move reads NOT-MOVED. A failure is Branch B: a
  person re-points the firm to its pin.
- **The producer** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` refuses bad input on every run
  (for example "reconciliation tolerance exceeds 0.01 USD", the account-census ties, "unknown is not zero"; `:381-515`).
  It does not compare a new publication with the one it replaces. So run-over-run "no worse" is not maintained over time.

## The gate (for the CTO to fold into `2.0.0_SA_COO~P2`)

1. **Where:** in the producer's publish step (`HoldingsPublication`, the `current/manifest.json` re-point), before the index
   moves. It is a gate on the producer's own write, not a monitor or alert (CLAUDE.md moratorium: findings land as gates).
2. **Compare:** the candidate publication against the one the firm serves now (the current index's VersionId), on the four
   Branch A conditions per firm.
3. **Pass:** re-point as today.
4. **Fail:** do NOT re-point. The firm keeps serving its last good publication. The producer writes one refusal record per
   firm, naming the failed condition and its count (for example "3 securities lost their class: <ids>"). The record sits
   beside the manifest, under a builder-produced address (rule 30), where the Holdings read and the CVO can see it. The
   other firms publish independently.
5. **Kept as today:** new unclassified positions are listed, not refused. A first publication (no prior) passes on the
   absolute conditions 1-3 only.
6. **Optional, Andrew's call:** two more "worse" conditions the current check does not cover, an account present at the
   prior and absent now, and a stale source date (a trading-day frontier older than the prior's, `lib/trading_calendar.py`).
   Recommended to include.
7. **Proof (seat-driven, no wait):** a QA run (`--qa`) fed a candidate that drops one classified security's class is
   refused and keeps serving the prior; the same run with the class restored re-points. Both in one trace.
8. **Retires:** S392's manual pin/read (`e62e56_post_fire_read.py`), whose four conditions the gate now holds on every fire.
   Moving served output still needs the never-widen pair for the producer change itself.
