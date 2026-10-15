# ANDREW DIRECT -- active Cottonwood accounts get Bloomberg pricing exclusively; inactive accounts are fine with Yahoo (2026-10-15 ~17:3xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. It came minutes after his acceleration word
(`ANDREW_DIRECT_20261015_173xZ_ACCELERATE_COTTONWOOD_BACKFILL_YAHOO_HARDER_PORTING_TEST.md`), while this seat was routing it to dell1.

**Verbatim:**

> Active accounts should get BBG pricing exclusively, inactive accounts are fine with yahoo finance, that is probably the most reasonable way to handle these.

## What it sets (surfaced, not adjudicated)

- **Active Cottonwood accounts** (the 860-account active set V2): Bloomberg prices EXCLUSIVELY. No Yahoo price feeds an active account's
  backfill.
- **Inactive accounts** (former clients): Yahoo prices are acceptable.

## What it touches (for the owners to read; this seat does not widen or narrow it)

- **The 10-13 rule** "former Cottonwood clients are excluded from every vendor draw, not ranked last". That rule was ruled by the laptop CTO
  on Andrew's memo words ("we don't need to waste quota on this stuff"), and MDPF_DEMQUE `rank.py` P3 is "never drawn". This word admits a
  Yahoo draw for inactive accounts. His memo's concern was quota, and Yahoo has none, so it reads as compatible: Bloomberg stays closed to
  former clients.
- **ADVI_COTBKF PRD** C-BASIS and FWD-3 (the price population and source), and the 10-07 rec (Yahoo for equity/ETF/fund, Bloomberg for
  fixed income and other).
- **MDPF_DEMQUE:**
  - the Yahoo leg: today it writes Yahoo prices for active-set names;
  - the B1 request: 613 CUSIPs, clipped to active set V2;
  - the porting test: it verifies Yahoo for prices that, under this word, no longer feed active accounts.
- **Bloomberg budget:** the active set's full need at Bloomberg depth is not measured against the ~23,432 cells/day rate.

-- recorded by 4.0.0_SA_CRO~DELL2
