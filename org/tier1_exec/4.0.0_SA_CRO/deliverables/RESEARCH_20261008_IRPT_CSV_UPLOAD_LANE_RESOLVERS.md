# RESEARCH -- the Analysis CSV upload lane's resolvers: retire the lane, not build its resolvers

**archetype:** EXPLORE
**Author:** 4.0.0_SA_CRO~DELL2, 2026-10-08
**Ask:** 1.0.0_SA_CTO~DELL2 msg 1599 ([SELF-DRIVE dell2] design fork): `intake/upload_resolution.py:106-111` and
`uploads.py:320-337` need parse_mapping, resolve_security and resolve_prices for the CSV lane; how does the template lane
resolve without a vendor call, can the CSV lane reuse it, and where do prices come from? Recommend one design.
All paths below are under `infra/aws/lambda/investor-reporting/`, read at HEAD of `box/dell2` on 2026-10-08.

## Recommendation (one design)

**Retire the legacy `csv_base64` lane, and send every CSV through the template lane, which already reads CSV.**
- Build no producer for `parse_mapping` or `resolve_security`.
- Keep the one real gap, the price for a SHARES-basis upload, as a single resolver that both lanes would have needed
  anyway (section 3).

## 1. Correcting the premise: the template lane does call a vendor, just not from the Lambda

The upload POST never reaches the vendor: `deferred_upload_service` (`intake/upload_resolution.py:102-113`) retains the
file and sends one `resolve_upload` message. The **resident** then resolves the symbols through its own YCharts session:
one batched `securities_info` GET of at most 200 symbols (`intake/upload_resolution.py:1-10`;
`intake/resolution_broker.py` ROUTE `/securities/securities_info`; `uploads.py:480`
`self.resolve_template(principal, owner, symbols)`). So "without a vendor call" holds for the Lambda, not for the
lane. The pattern to reuse is **deferral to the resident**, not a vendor-free lookup.

## 2. The CSV lane is already served by the template lane

| fact | evidence |
|---|---|
| A template upload may itself be a CSV | `uploads.py:100-112`: `template = "file_base64" in payload or "file_type" in payload`; `file_type in ("csv","xlsx")` |
| The template reader parses CSV | `intake/template_reader.py:146-167` `read_template(data, file_type)`, `_csv(data)` for `file_type == "csv"` |
| The legacy lane is the `csv_base64` payload only | `uploads.py:103` (required `{"upload_token","filename","csv_base64"}`), `uploads.py:319-337` (`parse_mapping` then `parse_holdings` then `freeze_parsed_portfolio(... self.resolve_security ...)`) |
| The portal no longer sends `csv_base64` | `portal/src/pages/InvestorReporting/tabs/analysis/prospect.ts:83-119`: the request is `file_base64` + `file_type` and the comment names the `csv_base64` bridge "retired"; the wire type `contracts/wire/AnalysisUploadRequest.ts:15,28` still admits `csv_base64` |
| Its three hooks have no producer outside tests | `upload_resolution.py:110-112` and `131-133`: `_not_composed("CSV_LANE_NOT_COMPOSED")` in both the Lambda and the resident services |

So the lane the self-drive tick asks to compose has no sender in the product. Composing it would build a second CSV
parser (`parse.py`, 1,251 lines, free-form columns plus a mapping) beside the template reader, with a second resolver
path. The build ladder's rung 1 (YAGNI) and rung 2 (the estate already has it) both point to retiring it.

**The retirement, as acts** (for the PRD addendum, not done here):
1. `validate_upload` refuses a `csv_base64` payload by name (for example `CSV_LANE_RETIRED`) instead of
   `CSV_LANE_NOT_COMPOSED` later in the flow.
2. `AnalysisUploadRequest` drops the `csv_base64` arm from the wire contract (regenerated, with its test).
3. `UploadService` drops `parse_mapping` and `resolve_security` from its required callables. `parse.py` stays where the
   mail lane uses it; a census of its other callers comes first (not run here).

What the free-form lane offered that the template does not: arbitrary column layouts with a mapping, plus share-class
**proposals** (`parse.py` header). The template lane already has corrections (`options["corrections"]`, Y-5) and
suggestions (`suggest=`), which cover the proposal role. Whether advisors need arbitrary layouts is a product question
for Andrew's frontend mapping session; this research does not answer it.

## 3. Prices: the one gap both lanes share

`resolve_prices` is unconsumed in both lanes: `uploads.py:332` (CSV) and `uploads.py:488` (template, SHARES basis only),
both `_not_composed("SHARES_PRICE_SOURCE_NOT_COMPOSED")`. A test pins the refusal
(`intake/tests/test_deferred_resolution.py:161-162`). Today a SHARES template answers NEEDS_CORRECTION by name; dollar and
weight templates need no price.

| source | fit for a prospect's arbitrary holdings |
|---|---|
| Opal-served stores (per-firm canonical prices; MDPF_SECHIST's series) | Poor. They hold what Opal's clients hold. A prospect's securities are arbitrary. The per-firm stores are barred across firms (CLAUDE.md NEVER rule; the ADVI_COTBKF price census found 5 of 40 buckets BARRED and a 13.7% union coverage even for a known book). The series is not yet served for arbitrary tickers. |
| The resident's own YCharts session, in the same batch as `securities_info` | Good fit. Same lease, same deferral, same 200-symbol bound, no new egress or credential. **Unmeasured:** whether the broker boundary exposes a price read on a given date. `resolution_broker.py` names only `securities_info`, and `security_resolution.py` validates identity fields, not prices. |
| Yahoo (yfinance) | Dell egress is allowed (Andrew ~19:1xZ), but the resident runs in AWS, and `README.md:51` says no live vendor call without Andrew's word. A second vendor for one number is not the minimum. |

**Recommended:** compose `resolve_prices` in the **resident**, as a price read on `price_date` through the same YCharts
operation boundary, carrying its claim (`measured`, with as-of date and source) on each price. Until that read is
measured to exist, the SHARES refusal stays as it is; it is correct, named and tested. If no such route exists, the
fallback is to keep SHARES refusing and ask the advisor for dollars or weights, rather than add a vendor.

## 4. What the CTO rules

1. Retire the `csv_base64` lane (section 2) instead of composing its three resolvers. Recommended.
2. SHARES prices: the resident's YCharts session as the one source, gated on measuring the route; until then the named
   refusal stands. Recommended.
3. Arbitrary-layout CSVs: deferred to Andrew's frontend mapping session (DSGN_IRPTV2 / COO~U2), not decided here.
