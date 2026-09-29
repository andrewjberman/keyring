# SIGN-OFF (1.0.0_SA_CTO half) -- R4 step 4: ENABLE the scheduled daily Holdings producer

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_20260928.md`
@`8d601db072`, blob `342f04c129822adc8573e738c25fa47b563b64ad` (2.0.0_SA_COO~M msg 102498). **Signed:** 1.0.0_SA_CTO,
2026-09-29 ~00:2xZ. The 4.0.0_SA_CRO half is asked separately. Discharges condition 4 of
`SIGNOFF_HOLDINGS_PRINCIPALS_DISPATCH_20260925.md` (@6c5c27a666).

## Signed, as the request reads it

- **The act:** Terraform safe-apply flipping `irpt-holdings-snapshot` DISABLED -> ENABLED (`cron(15 10 ? * MON-FRI *)`
  America/New_York, target `irpt-holdings-refresh-lambda`), under its own ledger. Code run: members-sha256
  `94f2e3433d9e...` (41 members per firm, ledger `irpt-holdings-packages-m-20260928c` CLOSED).
- **Preconditions read as MET:** N1 negative arm (4 of 4, ledger CLOSED @26127abf10); one QA fire Success at all
  three firms (f61bb631 / 3f2dca9e / 58cbeda0, rc 0, business_date 2026-09-25, each reconcile True) with the served
  index VersionId equal before and after; the code-only diff at the served date 0 node / 0 amount / 0 clock; the INF
  name census 0 personal data (7 security-code hits, dispositioned SAFE).

## Writers of the served Holdings index, counted: 2

1. **The schedule** (this act): one validated publication per firm per weekday; `latest` moves only on validation.
   A failed or unvalidated build leaves `latest` on the prior revision -- both branches are inside this half.
2. **A manual non-QA invoke** of `irpt-holdings-refresh-lambda` (payload without `"qa": true`) publishes to the served
   table off the schedule's clock. It is covered here ONLY when run under its own ledger entry naming the firm and
   business date; a QA invoke writes `holdings_qa` only and is not a served writer.

## Blast radius (by class, as the request's table measures it)

- **Code-only effect at the served date:** 0 nodes, amounts or clocks. Moves at the next publication: the own-mask
  account labels (49F 2,970, INF 875, COT 755 -- halves @45bafa24a1 / @c412578ede); UIC-16 full account type (INF);
  batch-A and ETF Part A classification; COT's cash-line rule, 981 SECURITY nodes read `cash` (0 at 49F and INF).
- **Real custody movement** from 2026-09-22 to each fire's business date is the producer's ordinary daily output.
- **Unchanged by this act, stated:** the classifier the producer reads is still `bd-securities`; the canonical
  `etf-classifications` re-point (S173) remains ONE later act with its own halves. The Holdings shape changes of the
  master UI brief (AD-01/02 L0 nodes, the Models/SMAs/Client taxonomy) arrive as their own halves.
- **Rollback per key:** (a) schedule DISABLED by Terraform; (b) per firm, repoint the served index to the retained
  prior revision; (c) the two read-version grants revert per their own sign-offs.

## Conditions

1. First scheduled fire: read back per firm the published revision, reconcile True, and the served manifest VersionId
   moved; a firm that fails leaves its `latest` unchanged, read the same way.
2. A fire on an exchange holiday (the cron is MON-FRI, not the trading calendar) must publish no new business date:
   read the first such fire, or show the producer's rule, before the first holiday (`lib/trading_calendar.py`).
