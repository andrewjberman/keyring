# IRPT_ANLREQ round 59, workstream ~G (ENGINE) -- decomposition: repair what the price-page merge left on trunk (CTO msg 11012, ~Y2 msg 11010)

Issuer `2.0.0_SA_COO~G2`, 2026-10-19.

**Input.** CTO msg 11012 (ruled): trunk's `opal_producer.py` carries the AR-g-166 code that reads `layout_overview.PRICE_TABLE` and calls `compute_all(..., prices=prices)`; a build that takes the producer without the price-page layout raises at report time. Disarm by guarding the read or by landing the layout with it; the price pair ships `opal_producer.py`, `layout_overview.py` and the map together. ~Y2 msg 11010: on trunk HEAD 5 of 11 tests in `test_opal_producer_not_in_this_version.py` fail. Measured here at the base: those 5 fail, and so do 3 of the round-57 tests in `test_price_pages_table.py`, `test_price_pages_series.py` and `test_price_pages_text.py`, because AR-y-408 (the report document drops every NOT_IN_THIS_VERSION entry and counts them in one NOT_SHOWN disclosure) merged after those tests were written. Both are tests of built work; the issuer owns them.

**Route chosen: GUARD.** Landing the layout is the price pair's release, which Andrew's pause holds; the guard is a producer-only change that makes the producer run against a layout that lacks the price pages. It changes no behaviour when the layout has them.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-170` | (a) the producer reads `PRICE_TABLE` and the `prices=` keyword only when the layout has them; (b) the 8 stale tests repaired to the AR-y-408 rule, intent kept | `opal_producer.py`, 4 existing test files, 1 new test file, the worker's folder | LOCAL (code and tests; no deploy, no AWS call) |

## Edges and chains

ONE chain, no dependency. `fanout: 1 of 1 chains, cap 8`.

## Four-postulate record

(i) Domain: the 8 tests that fail at the base, printed by a pytest run of the four files (8 failed, 24 passed). (ii) One grain: a test or a producer read. (iii) One intent: trunk's producer and its tests agree with the layout it runs against, held or landed. (iv) What this cut does NOT move: the layout, the map, any resident pin, any release, the price pair's ship.

fanout: 1 of 1 chains, cap 8, reason: one LOCAL repair cell.
