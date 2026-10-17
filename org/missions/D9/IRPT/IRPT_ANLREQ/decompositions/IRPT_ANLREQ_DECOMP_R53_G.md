# IRPT_ANLREQ round 53, workstream ~G (ENGINE) -- decomposition: the YCharts price tier on the estate's working form (r34j)

Issuer `2.0.0_SA_COO~G2`, 2026-10-17.

**Input:** IB2's one SPY request with the estate client's form (`PRICE_FORM_READ.txt` @52f06c5aa9): HTTP 200, 1,256 points, the existing `price_adapter_ycharts` reader parses them (445.87 to 763.08, a PRICE return). The CRO's research `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261016_YCHARTS_SINGLE_TICKER_PRICE_SERIES_FORM.md` @c9f3005376: `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py:219-249`, `fund_data()`, the full quote-page form of 41 parameters, `calcs=id:price` for a security or ETF and `id:level` only for a `^` index; 67 of 67 HTTP 200 in May. r34i (tiers back to [estate, yfinance], applied by IB2 under its own pair) is the state this round starts from. CTO msgs 10040 and 10070: r34j re-adds the tier, by CALLING the estate client's builder, own pair, offline tests first.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The estate builder is called unchanged, and nothing is sent through the estate client's own path.** `fund_data()` builds its dict and then sends through the client's OWN credentials secret, cookie header and `urllib` path: calling it as it stands from the resident would bypass the provider lease and the host budget (6 calls per 390 s) that every YCharts call from this host must share. So a thin module (`ycharts/research/price_form_ycharts.py`) subclasses `YChartsClient` with `__init__` skipped (no secret read) and `_request` returning the URL it was handed; calling the client's own `fund_data(symbol, calc)` on that subclass yields the exact URL the estate client would send. The module hands the URL's path-and-query (the client's `BASE` stripped) to the existing lease transport (`price_transport_ycharts`), which sends it unchanged because it takes a path with no params. No estate file is edited, no parameter is copied, no drift is possible. `ycharts_client.py` joins the resident package as ONE added member, mapped from the pin (`--member ycharts/research/ycharts_client.py=infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py`). The module finds the client by `import ycharts_client` and, in the repository layout where it is not on the path, falls back to the sibling Lambda directory.
- **Calc by symbol.** A symbol that starts with `^` gets `calc="level"`, every other symbol `calc="price"` (the estate rule, `ws1_surface_pull.py:246-260`, `yalp_mdsrc_c2_prestage.md:20`).
- **The series is a PRICE return.** `format=real` returns price levels; the adapter's base-100 chain over them is a price return, not a total return (the SPY read: 445.87 to 763.08 = 171.1). The adapter's docstring says so. Whether a report line must carry a "price return" basis next to `source: ycharts` is a PRD question for the CTO (C-PRICES says every price carries its source as a claim field; it says nothing of the return basis); this cut does not change `price_source`.
- **Not in this cut:** the signed-out call (unmeasured; the tier uses the session-bearing acquire), symbols other than SPY (one sample), a total-return calc, the budget number, the price pages of the Opal report (Andrew's hold, C-V1).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-155` | the new module `price_form_ycharts.py` (the URL builder over the estate client, calc by symbol), the adapter sending that path with no params, a test file for the module, and the two existing tests that assert the old form moved | the module, the adapter, three test files | WORLD (the floor of an infra path; code and tests only, nothing deployed) |
| `AR-g-156` | the r34j release: bindings tiers back to [estate, yfinance, ycharts]; the adapter changed and `price_form_ycharts.py` and `ycharts_client.py` added; build, packet, both halves, apply by IB2, V2 with the tier check on the new form | the release tooling, the applier's `deliverables/`, the ledger | WORLD (S3 write, a host root, a restart; rollback the r34i root) |

## Edges and chains

- ONE chain: `AR-g-155` feeds `AR-g-156` (the build pins the trunk that holds the merged cell).

## Four-postulate record

(i) Domain: one URL builder, one adapter, one tier. (ii) One grain: a request. (iii) One intent: make the tier's first call a call YCharts answers, without a second path to YCharts. (iv) What this cut does NOT move: the lease, the budget, the transport, the door, the price chain order, the YCharts recipe path, the estate client.

fanout: 1 of 1 chains, cap 8, reason: AR-g-155 is the one worker cell; AR-g-156 is the issuer's release and the applier order to IB2.
