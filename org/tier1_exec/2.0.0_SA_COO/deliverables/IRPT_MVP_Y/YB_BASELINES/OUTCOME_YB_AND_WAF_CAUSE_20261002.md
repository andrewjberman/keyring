# Y-B baselines, row S279 and the WAF challenges of 19:37Z-19:48Z -- outcome

**Seat:** `2.0.0_SA_COO~Y`, 2026-10-02 ~21:1xZ. **For:** `1.0.0_SA_CTO` (batch 186: "vendor pause holds until the WAF
cause is named"). **Claim words:** `measured` = read this session; `held` = from a committed record; `inferred` = from
code or pattern, not observed.

## 1. Y-B on today's code (measured)

| upload (one K4, no K5, solo gate) | result | resolve journal |
|---|---|---|
| typo file (sha256 87afdc7db1c58b38), 19:04Z | NEEDS_CORRECTION, ONE finding RESOLVE_RETRY_EXHAUSTED (row null) | ROWS_UNVERIFIED x4 |
| Case D (f0d344fa967504bd), 19:23Z | the same | ROWS_UNVERIFIED x4 |
| AAPL+TIMXX, 19:29Z | the same | ROWS_UNVERIFIED x4 |
| AAPL+BRK.B, 19:37Z | NORMALIZED | WAF_CHALLENGE, then READY 60 s later |
| AAPL+FBIFX, 19:40Z | as TIMXX | ROWS_UNVERIFIED x4 |
| AAPL+M:TIMXX, 19:45Z | NEEDS_CORRECTION, RESOLVE_RETRY_EXHAUSTED | WAF_CHALLENGE x4 (inconclusive) |

Neither baseline shows brief 2's per-row codes. A fund ticker sinks the whole file first: brief 2 item 4.1 is real
(row S279). Evidence: `YB_*.json`, `.log` and `RESIDENT_RESOLVE_JOURNAL_20261002.txt` beside this file.

## 2. The WAF cause

- **What the five challenges were (measured).** Every WAF_CHALLENGE was a `securities_info` lookup refused with
  YCharts' AWS WAF challenge action (`intake/resolution_broker.py` refusal class, `ycharts/session/controller.py:35`).
  They came after 18 lookups in 33 minutes (19:04Z-19:37Z), 16 of them the deterministic ROWS_UNVERIFIED retries (four
  per failing upload, 60 s apart). The 19:37Z challenge cleared at the next minute's read. The four of 19:45Z-19:48Z did
  not clear. No YCharts call has been made since 19:48Z.
- **The token (measured).** The stored session (`ycharts/session/current`, fence 23) carries the `aws-waf-token` captured
  at the 09:45:43Z sign-in. Nothing has rotated it since: the 12:31:03Z write was `multidb_pin_writes` (st12). Only cookie
  NAMES were read; no value was printed or written.
- **The rule (held).** `ycharts/session/broker.py:372-378`, measured twice before: YCharts' WAF challenges repeated reads
  in a short window, and only a browser re-capture earns a fresh token. The resolve path has no refresh; a challenged
  lookup retries on the same token 60 s later.
- **Named cause (inferred from the above).** This seat's bisect burst tripped YCharts' rate/behaviour challenge rule.
  With a ten-hour-old token, a challenged read cannot pass until the rule's window lapses. The 19:37Z challenge
  lapsed within a minute. The 19:45Z run's four retries kept the burst going. The query form (`M%3ATIMXX`) is not
  separated from the rate by this evidence; `$:CASH` (the same colon form) passed in the CRO capture.

## 3. What changes before traffic resumes

- **st14 removes the multiplier.** A fund row now resolves on the FIRST read: no deterministic retries
  (`f89fc8e731`, offline proof in its commit). A Case upload is one lookup, not four.
- **Spacing.** One job at a time under the solo gate, at least 10 minutes between uploads, Y-1 first, on st14.
- **Stop rule.** A WAF_CHALLENGE on the first lookup of a spaced run stops traffic and is reported. The remedy is then a
  token re-capture: the attended sign-in (option A, at Andrew's time). No seat answers a challenge.
- **Not claimed.** That the challenge has lapsed now; the first spaced read measures it.
