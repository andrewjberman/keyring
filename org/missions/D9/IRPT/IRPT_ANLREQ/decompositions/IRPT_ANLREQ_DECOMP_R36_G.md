# IRPT_ANLREQ round 36, workstream ~G (ENGINE) -- decomposition: the door checker reads a symbol yfinance has no data for as NOT_KEPT, not CHECK_FAILED

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** AQ2's read-only record `CHECKFAIL_READ.txt` (round 35, AR-g-120, commit 51686af530) refuted all three environment hypotheses; the cause was read from the yfinance 1.2.0 wheel: with `hide_exceptions` False (which `default_history` sets), `history()` RAISES `YFTzMissingError` or `YFPricesMissingError` (both subclasses of `YFTickerMissingError`) for a symbol Yahoo has no data for (`scrapers/history.py` lines 98-99 and 273-274), and `default_history` lets the exception out, so `_failure_reason` files EXCEPTION and the door says CHECK_FAILED instead of NOT_KEPT. SPY passes; an unknown or delisted symbol can never read NOT_KEPT. CTO msg 9291 (diagnosis accepted): cut r34d under its own pair with its own names; ONLY `YFTickerMissingError` and its subclasses map to no rows; every other exception (HTTP 401, 403, 429, a connection error, a timeout, any other class) stays CHECK_FAILED; tests on both sides with the real classes; proof is a V2 run in the service's own environment with SPY KEPT and ZQXWVK NOT_KEPT.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The rule is by class name in the exception's MRO** (`YFTickerMissingError`), not by message text and not by substring, so it holds whether yfinance is imported or faked, and a lookalike class name stays CHECK_FAILED.
- **The real classes** are the yfinance 1.2.0 wheel's own `yfinance/exceptions.py` (sha256 `16241e89d10c6317825d3387fa96cb5f20b4dd0a2a15636fa41d28ae9c8e48e3`, 1733 bytes, pure Python, no imports), copied into the issuer's checks folder and into the worker's test fixture; the worker's tests load it, so no test invents an exception.
- **Known limit, named:** a transient Yahoo "no price data" for a real symbol raises the same class and now reads NOT_KEPT. The CTO's condition accepts the class as the line; the old hidden-error-frame path (no raise) is untouched and stays CHECK_FAILED.
- **Scope of this round:** the source fix and its tests (one worker cell). The r34d rebuild, its packet and the AQ2 apply order are the next round's cells, after this merges.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-121` | `intake/yfinance_check.py` `default_history` returns `[]` for a ticker-missing exception and re-raises everything else; the test fixture (the real exceptions module) and the new tests in `intake/tests/test_yfinance_check.py` | the checker, its test file, its fixture, the worker's folder, the order, the channel file | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed) |

## Edges and chains

- ONE chain. The r34d rebuild consumes this cell's merged bytes.

## Four-postulate record

(i) Domain: the exception classes `history()` can raise for the three symbol states (known, no data, outage). (ii) One class per outcome. (iii) One intent: an outage never reads as "ticker does not exist". (iv) What this cut does NOT move: the resident release, the host, the hidden-error-frame path, the cap and pace, the Lambdas.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 258).
