# IRPT_ANLREQ round 17, workstream ~G (ENGINE) -- decomposition: the resident switches its Opal reports to priced runs from an optional binding

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the price stage `AR-g-86` (merged `1c84d38bf4`: the `stores` keys `pricing`, `price_readers`, `as_of`), the readers `AR-g-81` (BBG history) and `AR-g-83` (Yahoo), the compose read `AR-g-54` q4 (the pricing-flag seam), the R11 host facts (the resident role holds `opal-data-etfs/bbg/*`; the DEMQUE bucket and `ycharts/credentials` are not granted; `lib/trading_calendar.py` is not in the tarball; pandas, pyarrow and yfinance are not on the host), the issuer's reference build.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Dormant until switched.** The wiring is an OPTIONAL bindings key `opal_pricing` `{"enabled": bool, "tiers": [...]}`. Absent or not enabled, every Opal job runs unpriced as today. The release cell ships the capability, and a later bindings edit (after the host has its libraries and the CTO has ruled the grants) turns it on. This keeps r32 from changing the report's content by itself.
- **Two tiers wired now.** `estate` (the BBG history reader on the host role's own S3 client) and `yfinance` (default fetch; the library imported only when a symbol is asked, so a missing library is an `ERROR:ImportError` attempt and the chain goes on). `ycharts` needs the session transport and `demque` needs a bucket grant: neither is wired, and the binding refuses them by name rather than ignoring them.
- **T-1 without the calendar module.** `lib/trading_calendar.py` is not in the resident tarball. `as_of` is the previous weekday before the UTC run date. That is never later than the true T-1, so no row of the run's own day is read; on an exchange holiday it is a day earlier than needed with no row of its own, and the chain's `<= as_of` cut takes the last row before it. A later cell may replace it with the calendar module when the release carries it.
- **Offline controls still win.** The pricing keys are merged before the existing `extras`.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-90` | `resident_installed.py`: `OPAL_PRICING_BINDING`, `PRICING_TIERS`, the binding's validation in `load_bindings`, `_t_minus_1`, `_pricing_extras`, the `pricing_extras` keyword of `make_opal_stores` and its call; `tests/test_opal_pricing_binding.py` (6 named tests) | those two files + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain. Round 16's cells (`AR-g-88` slot 188 in flight, `AR-g-89` merged `8762c03234`) edit other files.

## Not moved by this cut

`build_resident_package.py` and the shipped bindings (the release cell's); `opal_producer.py`; the YCharts and DEMQUE tiers; any grant or host library.

## Four-postulate record

(i) Domain: the tiers of the C-PRICES chain this resident can read. (ii) One binding, one factory. (iii) One intent: the resident can price, and does so only when told. (iv) What this cut does NOT move: the shipped bindings, the release, IAM, the host.

fanout: 1 of 1 chain, cap 8, reason: one installer file and one new test file; slot 190.
