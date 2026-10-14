# L4-R review -- IRPT_ANLREQ PRD v0.9 @c642900a88, brief half -- SIGNED

**Reviewer:** `4.0.0_SA_CRO~DELL2`, 2026-10-14 ~16:0xZ. **Delivery:** msg 7735. **Half hash:** 477937dd940b.

- **The only ENDPOINT change is FWD-7.** It now admits at most ONE YCharts data call per request: batched, prices only, after
  MDPF_SECHIST and before yfinance. It carries Andrew's ~15:5xZ word verbatim in SOURCE (record @14360692df).
- **BRIEF COVERAGE is unaffected.** The rows reference no YCharts price. Row 4 (typo and swap) verifies against the registry and
  yfinance, unchanged. The denominator is still 14 of 14.
- **Noted, not refused:** ADDENDUM v0.9 item 2 reads Andrew's word NARROWLY where it is silent: one call per request, prices only, and
  its place in the order. It says he may widen it by one word. This reviewer recommended the same fallback placement to him in-session.
  The narrowing is stated in the PRD, not hidden.
- **R2 (the branded commentary PDF, row 8) is still open at Andrew,** as at v0.8.

-- 4.0.0_SA_CRO~DELL2
