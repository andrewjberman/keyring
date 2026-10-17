# IRPT_ANLREQ round 53, workstream ~G (ENGINE) -- decomposition: the YCharts price tier on the estate's working form (r34j)

Issuer `2.0.0_SA_COO~G2`, 2026-10-17. DRAFT until the CTO answers the A-or-B question below; nothing here is issued.

**Input:** IB2's one SPY request with the estate client's form (`PRICE_FORM_READ.txt` @52f06c5aa9): HTTP 200, 1,256 points, the existing `price_adapter_ycharts` reader parses them (445.87 to 763.08, a PRICE return). The CRO's research `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261016_YCHARTS_SINGLE_TICKER_PRICE_SERIES_FORM.md` @c9f3005376: `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py:219-249`, `fund_data()`, the full quote-page form of 41 parameters, `calcs=id:price` for a security or ETF and `id:level` only for a `^` index; 67 of 67 HTTP 200 in May. r34i (tiers back to [estate, yfinance], applied by IB2 under its own pair) is the state this round starts from. CTO msgs 10040 and 10070: r34j re-adds the tier, on that form, own pair, offline tests first.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The estate client cannot be called as it stands.** `fund_data()` builds its dict inline and sends it through the client's OWN credentials secret, cookie header and `urllib` path: calling it from the resident would bypass the provider lease and the host budget (6 calls per 390 s), which every YCharts call from this host must share. The form therefore reaches the resident as DATA: either (A) a pure function `fund_data_params(symbol, calc, max_points)` extracted in `ycharts_client.py` (a behaviour-free refactor of the estate Lambda's source; its package hash changes), or (B) the adapter carries the 41 parameters and a test reads the client's dict out of `ycharts_client.py` by AST and fails on any difference in key, order or value. **REC B** (asked of the CTO at 00:08Z on 2026-10-17): it touches nothing deployed elsewhere and the drift cannot go unseen. The cell is cut as B unless the CTO says A.
- **Calc by symbol.** A symbol that starts with `^` gets `id:level`, every other symbol `id:price` (the estate rule, `ws1_surface_pull.py:246-260`, `yalp_mdsrc_c2_prestage.md:20`).
- **The series is a PRICE return.** `format=real` returns price levels; the adapter's base-100 chain over them is a price return, not a total return (the CRO's INFERRED reading, confirmed by the SPY read: 445.87 to 763.08 = 171.1). The adapter's docstring says so. Whether a report line must carry a "price return" basis next to `source: ycharts` is a PRD question for the CTO (C-PRICES says every price carries its source as a claim field; it says nothing of the return basis); this cut does not change `price_source`.
- **Not in this cut:** the signed-out call (unmeasured; the tier uses the session-bearing acquire), AAPL and other symbols (the SPY read is one sample), a total-return calc, the budget number, the price pages of the Opal report (Andrew's hold, C-V1).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-155` | `price_adapter_ycharts.py` sends the estate client's 41-parameter form with calc by symbol; a drift test pins it to `ycharts_client.py`; the two tests that assert the old form move | the adapter, its tests, one new test file | WORLD (the floor of an infra path; code and tests only, nothing deployed) |
| `AR-g-156` | the r34j release: bindings tiers back to [estate, yfinance, ycharts]; the adapter is the one changed code member; build, packet, both halves, apply by IB2, V2 with the tier check on the new form | the release tooling, the applier's `deliverables/`, the ledger | WORLD (S3 write, a host root, a restart; rollback the r34i root) |

## Edges and chains

- ONE chain: `AR-g-155` feeds `AR-g-156` (the build pins the trunk that holds the merged cell).

## Four-postulate record

(i) Domain: one adapter, one request form, one tier. (ii) One grain: a request. (iii) One intent: make the tier's first call a call YCharts answers, without a second path to YCharts. (iv) What this cut does NOT move: the lease, the budget, the transport, the door, the price chain order, the YCharts recipe path.

fanout: 1 of 1 chains, cap 8, reason: AR-g-155 is the one worker cell; AR-g-156 is the issuer's release and the applier order to IB2.
