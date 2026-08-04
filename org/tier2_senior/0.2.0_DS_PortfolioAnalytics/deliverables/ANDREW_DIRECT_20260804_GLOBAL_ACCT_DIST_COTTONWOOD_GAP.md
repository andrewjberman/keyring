# ANDREW-DIRECT — Global account-distribution.json missing Cottonwood; investigate + spec the fix

**Channel:** Andrew-direct, 0.2.0_DS_PortfolioAnalytics terminal, 2026-08-04 ~17:5xZ.
**VERBATIM:**

> "Another thing i need you to look into with DE is that the "Global" scope
> account-distribution.json and associated metrics are not including cottonwoods holdings
> count, and associated container metrics and bell curve data. We should be able to
> effectively get everything we need from that on a daily basis, so I do not understnad why
> that is not being aggregated for the "Global" account-distribution.json. Look into the
> dynamics around that, specifically how it is done for 49 Financial and Inflection, and
> spec the fix to get Cottonwood incorporated in there."

**Scope as received (surface, not adjudicate):** investigation + fix SPEC at this seat, "with DE"
— the Global-scope `account-distribution.json` (holdings/account count, container metrics, bell
curve data) excludes Cottonwood while 49Financial and Inflection are aggregated; the daily feed
should already carry everything needed. Deliverable = the dynamics (how 49F/INF are folded in,
why cottonwood is not) + the spec to incorporate Cottonwood.

**Broadcast:** COO + CTO + MSTR, same turn (this file committed alongside).
