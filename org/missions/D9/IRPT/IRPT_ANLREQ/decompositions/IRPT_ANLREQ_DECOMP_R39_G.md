# IRPT_ANLREQ round 39, workstream ~G (ENGINE) -- decomposition: the door checker reads Yahoo's 404 for an unknown symbol as NOT_KEPT (r34e)

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** AQ2's probe `EXCCLASS_READ.txt` (commit 6395c4000d, TO-READ-EXCCLASS, round 38), MEASURED in the service's own environment with the r34d root's checker: ZQXWVK raises `curl_cffi.requests.exceptions.HTTPError`, message `HTTP Error 404: `, MRO HTTPError, RequestException, CurlError, OSError; frames `quote.py:612 _fetch_info`, `quote.py:588 _fetch`, `data.py:463 get_raw_json`, `models.py:167 raise_for_status`; the r34d checker answered `_is_ticker_missing=False`, `_failure_reason=EXCEPTION`; SPY raised nothing (22 rows). So yfinance 1.2.0's INFO fetch (`GET https://query2.finance.yahoo.com/v10/finance/quoteSummary/<SYMBOL>`, `quote.py` line 588 and `const.py`'s `_QUOTE_SUMMARY_URL_`) 404s for an unknown symbol before any chart call, and with `hide_exceptions` False the HTTP error escapes as curl_cffi's own class, which the r34d fix (the YF* ticker-missing classes by name) never sees. In curl_cffi 0.13.0 `Response.raise_for_status` builds `HTTPError(f"HTTP Error {status}: {reason}", 0, self)`: the exception's `code` is 0 and the status and URL live on `exc.response` (read from the approved wheel's `models.py`).

CTO msg 9354 (rule APPROVED with one tightening): no rows ONLY for (a) `YFTickerMissingError` by name, or (b) a curl_cffi `HTTPError` whose `exc.response.status_code` is 404 AND whose response URL is Yahoo's quote/info endpoint naming THIS symbol (URL-decoded, exact segment match). Anything else stays CHECK_FAILED: no response object, another endpoint, 401, 403, 429, timeouts. Tests use curl_cffi 0.13.0's real classes plus a 404 on another symbol's URL that must read CHECK_FAILED. V2 prints the class and status on any CHECK_FAILED and keeps the SPY control. The Yahoo-wide-404 risk is accepted as named.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The endpoint is `quoteSummary`:** the host must be `finance.yahoo.com` or end in `.finance.yahoo.com`, and the URL path's last two segments (URL-decoded, case-insensitive) must be `quoteSummary` and the symbol. The chart endpoint, another host, a different symbol's URL, a missing URL and a missing response all stay CHECK_FAILED.
- **The class test is by name and module:** an `HTTPError` in the exception's MRO whose module starts with `curl_cffi`; a lookalike `HTTPError` from another module stays CHECK_FAILED.
- **The real classes:** the issuer's fixture `checks/curl_cffi_0_13_0/` holds the wheel's `requests/exceptions.py` and `const.py` BYTE-EXACT and the exact text of `class CurlError` (README names the sources and hashes); the worker copies it into the tests' fixtures and the tests import the real `HTTPError`, `Timeout`, `ConnectionError`, `DNSError` from it.
- **This round is the source fix and its tests (one worker cell).** The r34e tooling fork, the V2 script that prints the class, the build, the packet and the AQ2 apply order are the next round's cells, after this merges.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-125` | `intake/yfinance_check.py`: `_symbol_404` and `_is_ticker_missing(exc, symbol)`, `default_history` passes the symbol; the two test fixtures; new tests in `intake/tests/test_yfinance_check.py` | the checker, its test file, its fixtures, the worker's folder, the order, the channel file | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed) |

## Edges and chains

- ONE chain. The r34e rebuild consumes this cell's merged bytes.

## Four-postulate record

(i) Domain: the exception shapes `history()` can raise for the symbol states (known, no data via the info 404, no data via a YF class, outage, rate limit, network). (ii) One outcome per shape. (iii) One intent: an outage never reads as "ticker does not exist". (iv) What this cut does NOT move: the resident release, the host, the hidden-error-frame path, the cap and pace, the Lambdas.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 260).
