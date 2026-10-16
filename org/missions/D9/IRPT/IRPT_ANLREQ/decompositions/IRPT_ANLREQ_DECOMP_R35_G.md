# IRPT_ANLREQ round 35, workstream ~G (ENGINE) -- decomposition: why the served door checker answered TICKER_CHECK_FAILED

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO ruling on msg 9281 (msg 9283): HOLD FWD-1 run 3; `2.0.0_SA_COO~G2` owns a READ-ONLY diagnosis of the served checker. The probe window 10:2x-10:32Z produced `TICKER_CHECK_FAILED` while V2 (r34c close, AQ2 msg 9265) read SPY KEPT in a shell. Name the exception behind it. Hypotheses to test first, in the CTO's order: (1) the service's import path or environment lacks pydeps; (2) yfinance's cache directory is not writable for the service user; (3) the service's network egress differs from the shell's. The fix is a SEPARATE small pair, and its proof is a V2 run INSIDE the service's own environment, not a shell.

## What the issuer read first (code, no host)

- `intake/yfinance_check.py`: `CheckerUnavailable` (yfinance not importable) PROPAGATES out of `check()`; it is not a per-symbol verdict. A `TICKER_CHECK_FAILED` finding (`intake/portfolio.py:523`) needs a per-symbol `CHECK_FAILED` result with reason EXCEPTION, TIMEOUT, PUSHBACK or ERROR_FRAME, so the checker RAN and yfinance imported. That makes hypothesis (1) less likely unless the caller catches `CheckerUnavailable` and maps it to the same words; the read below settles it. The per-symbol reason is swallowed (`_check_one` keeps only the reason code), so the journal may carry no exception text: the order says so if it does not.
- Hypothesis (2) fits a service with `ProtectHome` or no writable HOME: yfinance 1.2.0 keeps a timezone cache under the user cache folder and a failure there surfaces as a generic exception (reason EXCEPTION).
- Hypothesis (3) is tested by reading the unit's network sandbox properties; no network call is made by the read.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-120` | one read-only record of the resident unit's sandbox, process environment, cache folders, import path wiring and the probe-window journal (10:15-10:40Z), enough to name the exception or to say the journal does not carry it | the applier's `deliverables/irpt_anlreq_r34/` and the order | WORLD (a production host is read; nothing is written there, no vendor call) |

## Edges and chains

- ONE chain. The fix cell (own small pair, own order) is cut AFTER this record, on its finding; it is not cut now because its content is the finding.

## Four-postulate record

(i) Domain: one resident unit, one probe window, three named hypotheses plus whatever the journal names. (ii) One read, one record. (iii) One intent: name the exception. (iv) What this cut does NOT move: the host, the unit, S3, the Lambdas, any vendor call, run 3's window (unspent).

fanout: 1 of 1 chains, cap 8, reason: one applier read order (a CloudOps read, not a worker cell).
