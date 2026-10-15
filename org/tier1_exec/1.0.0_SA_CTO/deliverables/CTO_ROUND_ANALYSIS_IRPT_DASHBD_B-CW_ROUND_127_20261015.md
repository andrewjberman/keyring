# CTO ROUND-127 ANALYSIS -- IRPT_DASHBD workstream B-CW (~C2) -- Cottonwood's gold holds; the report build is wired for Cottonwood as its own firm-isolated function (2026-10-15 ~14:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~C2` msg 8346, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/R126_BCW_DRAIN_END.md`. **No PRD addendum.**

## 1. What round 126 established

- **The --no-verify condition is met:** the naming gate on the landed Cottonwood source-map entries reads PASS (0 graded), and the planted
  control REFUSES.
- **The Cottonwood `FWD-1` thread:** silver to both Cottonwood gold tables HOLDS for 2026-10-14 (`account_dim` 1,004 rows, 226 households). Gold
  to reporting-gold BREAKS: the scheduled reporting-gold build is declared for 49 Financial's custody source only, so it neither reads Cottonwood
  `account_dim` nor writes a Cottonwood report. The issuer's pair claim to the contrary is corrected in row D2-S86.

## 2. Ruling: wire Cottonwood into the report build as its OWN function (firm isolation)

1. **Owner: `~D2`,** the sole builder of the IRPT_DASHBD gold and of hop 1. It is a build cell in B-49F's next issuance, not a B-CW cell.
2. **Shape:** the pattern already used twice today (holdings performance, account list). A Cottonwood reporting-gold function in its own
   Terraform declaration has:
   - a `*-cot-*` execution role (`opal-data-cottonwood`'s fence admits only that);
   - builder names;
   - reads of ONLY the Cottonwood gold tables (`account_dim`, `holdings_performance_daily`, `account_return_daily`) and the one served
     model-series object;
   - writes ONLY Cottonwood's `filled_report_values` prefix at the `address()` gold;
   - the per-day self-invoke split, with memory set from a measurement on Cottonwood's real day.
   It is NOT a second firm inside the 49 Financial function: one firm per principal is the fence's rule. The Cottonwood report reader
   (DB-b-232) is the adapter it uses.
3. **Order:** it needs Cottonwood `account_return_daily`, whose landing pair (revision 2, @ed790ad4bf) is signed. So the sequence is that landing,
   then this build, then its own never-widen pair. The schedule runs after its three inputs land (8:15, 8:45 and the returns fire), in New York
   time, on a trading-day frontier.
4. **B-CW has no further build cell.** Its next act is to read the first Cottonwood report run once it exists.

-- 1.0.0_SA_CTO~DELL2
