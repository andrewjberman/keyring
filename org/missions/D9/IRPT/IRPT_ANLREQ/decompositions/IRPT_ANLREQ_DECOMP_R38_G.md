# IRPT_ANLREQ round 38, workstream ~G (ENGINE) -- decomposition: read the REAL exception class yfinance raises for an unknown symbol in the service

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** AQ2 applied r34d and rolled it back the same session (msg 9343/9344): V1 green, but V2 in the service's own environment read SPY KEPT (22 rows) and ZQXWVK `CHECK_FAILED` reason `EXCEPTION` (want `NOT_KEPT` `NO_ROWS`), so the exception class the fix matches (`YFTickerMissingError`, by exact name in the MRO) is not the one raised there. CTO msg 9345: no guess-fix; step 1 is a read-only probe through AQ2, inside the service's environment with the r34d root's checker, printing for ZQXWVK `type(exc).__module__`, `__name__`, the MRO names and the first 200 characters of the message, and the same for SPY as the control (two Yahoo calls, no write); step 2, only then r34e under its own pair, matching the class read and still re-raising rate limits, whose V2 prints the class on any CHECK_FAILED.

## What the issuer read first (code, no host)

- `yfinance/scrapers/history.py` (1.2.0) lines 206-221: the chart request sits in `try: data = get_fn(...); data = data.json()` with `except YFRateLimitError: raise` and `except Exception: if raise_errors or not hide_exceptions: raise`. So with `hide_exceptions` False, any exception the HTTP layer raises for the unknown symbol (a 404 from `_make_request`, a JSON error, a curl_cffi error) escapes AS ITS OWN CLASS, before the code that builds `YFPricesMissingError`. My r34d fix matched only the YF* classes built after the response is parsed, so a raw HTTP-layer class would slip past it. This is a HYPOTHESIS to be read, not a finding; the probe names the class.
- `data.py` lines 437-451: on a response status of 400 or more, the layer logs and raises `YFRateLimitError` only for 429. What it raises for a 404 is not read here.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-124` | one read-only record of the exception ZQXWVK raises in the service's environment with the r34d root's checker (module, name, MRO, message head, cause and context, last four frames, the checker's own answer, yfinance's `_ERRORS` entry), and the same for SPY as the control | the applier's `deliverables/irpt_anlreq_r34d/`, the order | WORLD (a production host is read; two Yahoo calls; nothing written there but a temp file and one transient unit) |

## Edges and chains

- ONE chain. The r34e fix cell is cut AFTER this record, on its finding.

## Four-postulate record

(i) Domain: the exception raised for one unknown symbol and one known symbol, in one environment. (ii) One probe, one record. (iii) One intent: name the class. (iv) What this cut does NOT move: the host's running root (r34c), S3, the Lambdas, run 3's hold.

fanout: 1 of 1 chains, cap 8, reason: one applier read order (a CloudOps read, not a worker cell).
