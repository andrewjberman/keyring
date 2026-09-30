# IRPT_BCKEND decomposition -- ROUND 29, WORKSTREAM ~M (2026-09-30, 2.0.0_SA_COO~M, on CTO RULING 103169)

**Cut on:**
- 1.0.0_SA_CTO RULING 103169 (relayed by 2.0.0_SA_COO~D as 103170), on Andrew-direct ~05:0xZ: "PHYS is Commodities /
  Metals but it continues displaying in Alternatives". The CTO admits a NARROWED release: the IR Holdings producer
  reads class and sub-asset from etf-classifications for the tickers the table holds, with bd-securities as the
  fallback. ~M owns the act.
- An issuer measurement at 05:2xZ: CLOUD's investor_reporting suite reads SUITE-BROKEN (30 failed, 268 passed, 16
  errors, @874ab56b33). holdings_snapshot.py `canonical_classifier` / `_classifier_basis` read the private
  `_ticker_map` / `_name_map` of `data/black_diamond/scripts/gold/lib/etf_classifier.py`, and the MDPF_SECCLASS
  thread drain @ae7aa281b0 (SC-t-1) removed them. Served Holdings are unaffected (packages minted 2026-09-29 16:21Z
  from the older library). A Holdings re-mint from CLOUD would fail. Row MDPF_SECCLASS-S3.

**CTO conditions:**
1. The fallback is a DECLARED FWD-6 exception: owner 2.0.0_SA_COO~M, a stated reason, and a sunset when MDPF_SECCLASS
   E8 and E9 land.
2. A pre-release census lists the class-changing tickers with weight, and the count moving to unclassified reads 0
   with its denominator.
3. Its own new CTO and COO halves, separate from IB-mr-251..272 (held).
4. In the after-read, PHYS, GLD and VXX come from the table.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mr-291` | Holdings classifies canonical-first through the one client, falling back to a declared bd-securities exception module carried in investor_reporting (the pre-thread library logic, verbatim; its sunset is E8+E9); Holdings stops importing the BD library; closure + IAM (desired); suite whole; census at three firms; the new half | FWD-5 (Holdings classes) | WORLD | none (built on CLOUD, not on the held branch) |

Chains: A = 291, slot `0.9.0_WK_IRPT_BCKEND~93` (S197: 1 + max over authors, issued_to and branches = 92, so 93).
The held chain 251->272 stays held (CTO 103137). This cell supersedes its release for now and does not merge it.
