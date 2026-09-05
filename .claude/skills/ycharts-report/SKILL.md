---
name: ycharts-report
description: Generate a YCharts client PDF report (comparison / stress test / blended portfolio: Comprehensive Comparison, Multi-Comp, Overview, Proposal, Performance-and-Risk) by driving YCharts with Playwright from the `ycharts/credentials` cookie bundle (no fresh login). Modes: SELECT an existing client portfolio and compare it to a model, or BUILD a blend of N Opal models by weight. Every report field parameterized; produces the PDF (a presigned S3 URL) into Downloads. Use on `/ycharts-report` or asks for a YCharts comparison, stress test or proposal. Needs the Playwright MCP + AWS access.
---

# /ycharts-report -- YCharts client comparison / stress-test / blended-portfolio PDF report

Automates the exact YCharts flow an analyst (Alyssa) runs by hand: take (or BUILD) a **client
portfolio**, optionally compare it against a **model** (e.g. an Opal model), pick a **report
template**, fill the client-facing **metadata**, and generate a **client-ready PDF**.
Reverse-engineered live 2026-07-01 (comparison flow) + 2026-07-02 (blended/model-portfolio flow,
from Alyssa's "Blended walkthrough" HAR + audio); this skill reproduces both proven flows and
parameterizes every input.

The engine behind both is YCharts' `custom_pdf_reports` API -- a server-side **generate -> presigned
S3 PDF** flow, so the finished PDF is retrievable programmatically (not a client-side render).

**Research + design home:** `workflows/ycharts/stress-test/` -- `DECISION_TREE.md` (the fork model this
skill implements: a fixed spine + 8 modular forks) + `ENDPOINTS.md` (full reverse-engineered mechanics) +
the raw HAR/voice-memo sources. Read it when extending the skill; update it when a new fork/use-case appears.

## When to use
Operator types `/ycharts-report`, or asks to produce a YCharts client comparison / proposal /
stress-test / tearsheet / blended-portfolio PDF. NOT for raw market-data pulls -- that is the
read-only `ycharts_*` MCP integration (`app/integrations/ycharts/`); this skill is the
report-GENERATION flow (it creates a report artifact), so it is confirm-first on real client output.

## Two modes -- pick from the request

| Mode | Use when | Core work |
|---|---|---|
| **SELECT** | The client portfolio already exists in YCharts (imported / previously built) | Find it in the list -> Generate Report |
| **BUILD** | The request gives you portfolio *contents* to construct -- either a **blend of Opal models + weights** ("run a stress test on the following blend...") OR a client's **actual holdings as an Excel** ("stress-test these client portfolios", file attached) | **Create** a client portfolio from those contents (models = manual/API; Excel = `holdings_upload`), then Generate Report. See Fork 1a vs 1b. |

**The "blend" tell (Alyssa's rule):** if the requester says *"it would be helpful to see the following
**blend**"* / gives you a set of models with dollar amounts, they want a **mock blended portfolio** ->
Mode BUILD + a **Comprehensive Overview (No Benchmark)** report (a single-portfolio "stress test" whose
PDF dissects the allocation itself -- sector, drawdown, per-sleeve holdings, trend -- so no benchmark is
needed). Only add a benchmark / use a comparison template if they explicitly ask to compare it to
something.

## Report-template decision (the 3 templates Opal actually uses -- all "No Benchmark")

| The ask | Template (`report_type`) | #securities |
|---|---|---|
| "stress test on their portfolio" / a single blend | **Comprehensive Overview (No Benchmark)** (`aggregate_security_overview`) | 1 |
| "their portfolio **vs one** of our models" | **Comprehensive Comparison (No Benchmark)** (`aggregate_security_comparison`) | 2 |
| "**multiple** portfolios compared" (e.g. LTC vs Short-Term vs the client's portfolio) | **Comprehensive Multi-Comp (No Benchmark)** (`multi_security_comparison`) | 3+ |

"The other templates we don't really use." When the email is ambiguous, default to **Overview** for a
"blend"/"stress test" ask, and ask the operator if it's a comparison.

## Inputs (ask for what's missing; sensible defaults noted)

| Input | Mode | Meaning | Default |
|---|---|---|---|
| `blend` | BUILD | List of constituents: `[{model, weight}, ...]` -- each `model` a name (autocomplete, type `Opal` first) or `P:<id>`; `weight` a dollar amount (or %) | required (BUILD) |
| `weight_type` | BUILD | `Dollars` or `Percent` -- how the weights are expressed | `Dollars` (Alyssa's standard) |
| `benchmark` | BUILD | Benchmark symbol for the built portfolio | `^SPXTR` (S&P 500 TR); only surfaced in the PDF for comparison templates |
| `advisory_fee` | BUILD | Annual advisory fee on the built portfolio -- **always an explicit input** (the authoritative per-client fee comes from the operator / the intake form, NOT skill logic) | `0.01` (1%); confirm with the operator |
| `client` | SELECT | Existing client portfolio -- a **name** (fuzzy-matched) or `P:<id>` | required (SELECT) |
| `comparison` | both | The security/model to compare against (comparison/multi-comp only) -- a name (autocomplete) or `P:<id>` | required for comparison reports |
| `template` | both | Report template name | inferred from the ask (see decision table); else `Comprehensive Overview (No Benchmark)` |
| `report_type` | both | `aggregate_security_overview` / `aggregate_security_comparison` / `multi_security_comparison` | inferred from #securities |
| `name` / `title` | both | Portfolio name AND report title -- **the client's name** (or, for an advisor's mock, the advisor's name) | ask; see "Name & title rules" |
| `prepared_for` | both | Recipient shown on the report | **derived from the requester's email domain** (Opal->"Opal Capital", 49->"49 Financial", inflection->the firm); ask if unknown |
| `prepared_by` | both | Advisor/preparer name | the seat owner (`Alyssa Keith`) -- stays constant |
| `organization` | both | Firm | `Opal Capital` |
| `contact_phone` / `contact_email` / `contact_url` | both | Contact block (phone + URL required by YCharts) | the seat's saved values |
| `data_as_of` | both | `PERFORMANCE/RISK DATA AS OF` -- `latest` or a date | `latest` |
| `print_as_draft` | both | Watermark as draft | `false` |
| `output_dir` | both | Where the finished PDF is dropped | the user's Downloads (`C:\Users\AndrewBerman\Downloads`) |

### Advisory-fee reference (Alyssa-verbal -- confirm/source before a real run)
The standard advisory fee is **1%** (`0.01`). Alyssa noted a per-advisor exception -- **Dawson Moses ->
0.36%** (`0.0036`) -- but this is an UNSOURCED verbal note: treat it as operator-discoverable
REFERENCE, **not** skill logic. Do NOT bake in a client->fee map (brittle, drifts silently, won't
scale). Always take the fee as an input (default 1%) and CONFIRM it -- especially any exception -- with
the operator before a real client run. The authoritative fee comes from the operator / the intake form.

### Name & title rules (Alyssa)
- **Portfolio name = report title = the client's name.** If it's an advisor wanting a mock portfolio,
  use the advisor's name. "Whoever it's for is who the name goes to."
- **Strip the template suffix from the report title.** YCharts pre-fills the title as e.g.
  `"<name> Comprehensive Overview (No Benchmark)"`; Alyssa deletes everything but the client's name
  (looks messy otherwise). Final title = just the name (the HAR shows `"Louis Aquino "`).
- **Ambiguity to flag, not guess:** the source Excel/email title sometimes carries the advisor's last
  name AND the client's last name. If the requesting email's sender last-name == one of them, the
  OTHER is usually the client. When unsure, ask -- do not guess the client name.

## Auth -- inject the shared session (do NOT log in fresh)

YCharts allows ONE concurrent session per login; a fresh login **evicts** whoever holds the seat. So
this skill REUSES the shared session from Secrets Manager instead of logging in:

1. Read the cookie bundle: `aws secretsmanager get-secret-value --secret-id ycharts/credentials
   --region us-east-1 --query SecretString` -> JSON `{"cookies": "name=value; name=value; ..."}`
   (essentials: `ycsessionid`, `csrftoken`, `aws-waf-token`). NEVER echo the values.
2. Parse that header into Playwright cookie objects and inject BEFORE navigating:
   `await page.context().addCookies(cookies.map(c => ({name, value, domain: '.ycharts.com', path: '/'})))`.
   (Use `browser_run_code_unsafe` for `addCookies`; it can read a temp state file via
   `page.context().storageState({path})` on the way back out to refresh the secret if needed.)
3. **Freshness check:** navigate `https://ycharts.com/model_portfolios/list/` and confirm you are
   NOT bounced to `/login`. If bounced, the shared session is dead/evicted -> the credential needs a
   refresh (see "Refreshing the credential"); STOP and report -- do not fall back to a fresh login
   without operator go (it would evict the live seat).

If injection is not viable and the operator explicitly OKs a login: the seat must be confirmed CLEAR
first, and after finishing, refresh `ycharts/credentials` from the new session (see bottom).

---

## Flow A -- SELECT an existing portfolio, then report (proven 2026-07-01)

1. **List + resolve the client.** `GET https://ycharts.com/model_portfolios/list/`. Type `client`
   into the list Search box or scan rows for the name; capture `P:<id>` (edit link
   `/model_portfolios/client/<id>/edit/`). List data: `GET /model_portfolios/?...&sortColumn=user_modify_date&sortDirection=desc`.
2. **Row menu -> Generate Report.** Click the row actions button
   `#list-item-dropdown-model_portfolio-<id> > .btn.btn-secondary`, then the **"Generate Report"**
   menu link (match by text). (Other items: Export Holdings, Download Source File, Change Type,
   Duplicate, Delete -- ignore; "we do not use any of these other ones.")
3. Continue at **"The report-generation engine"** below (template pick -> securities -> customize -> generate).

---

## Flow B -- BUILD a blended mock client portfolio, then report (proven 2026-07-02)

A "blend" is a **client portfolio** (`label:"client_portfolio"`) built as a dollar-weighted mix of
Opal model portfolios. Two ways to create it; **B-API is preferred for automation** (exact body known,
no fragile multi-item DOM), **B-UI mirrors what a human does**.

**UI path (human reference / when driving the DOM):** Portfolios list -> **Create New** -> the "Create
blank portfolio" popup (4 options: Benchmark portfolio / Household / Model portfolio / **Client
portfolio**) -> pick **Client portfolio** -> the builder opens (`GET /model_portfolios/fixed/client/new/?targetFolder=`).
For each constituent: type `Opal` first (Opal models surface in autocomplete via
`GET /search/suggest/fixed_model_portfolio_items?q=Opal...`), pick the model, put the **dollar** amount
in the weight (commas don't work; the input dropdown must be set to **Dollars**). The builder allows
only **2 items at once** -- use **"Add item"** for the 3rd+. In the "Basic info" sidebar the ONLY field
changed is the **advisory fee**: none -> **annual**, **1%** (`0.36%` for Dawson Moses). Set the
portfolio **name** = client's name. **Save** -> it calculates (you can't generate until calc finishes)
-> click **update** to refresh the list.

**B1 (API-direct create -- preferred).** Via `browser_run_code_unsafe`, `fetch` the create endpoint
with the CSRF token (from the `csrftoken` cookie) as `X-CSRFToken` + `X-Requested-With: XMLHttpRequest`:

`POST https://ycharts.com/model_portfolios/fixed/` -- **`multipart/form-data`, two parts:**
- part **`portfolio`** (JSON):
  ```json
  {"name":"<client name>","description":"","benchmark_symbol":"^SPXTR","benchmark_creation_type":"custom",
   "historical_performance":null,"management_fee":0.01,"management_fee_frequency":"annually","service_type":null,
   "custom_level":null,"label":"client_portfolio","level_type":"auto","level_as_of_type":"prior_close",
   "level_as_of_date":null,"rebalance_frequency":"quarterly","reinvest_dividends":false,"show_avg_cost_basis":false,
   "show_exposure_proxy":false,"show_performance_proxy":false,"start_of_series":"oldest","series_start_level_date":null,
   "weight_type":"Dollars","tax_status":"non_qualified","imported_holdings_id":null,"uses_legacy_data":false,
   "rebalance_cash":true,"household_level_calc_method":null,"base_currency":null,"custom_field":null}
  ```
- part **`items`** (JSON array), one per constituent:
  ```json
  [{"name":"Opal Short-Term","security_id":"P:1728415","display_security_id":"P:1728415",
    "weighting":750000,"weight_text":"750000","target_weighting":null,"current_weighting":null,
    "dollars_weighting":null,"shares_weighting":null,"exposure_proxy_security_id":"","exposure_proxy_display_security_id":"",
    "exposure_proxy_name":"","avg_cost_basis":null,"ignores_period_rebalance":false,"isUnshared":false,"isNotOwned":false,"is_valid":true}]
  ```
  Returns **`201` with an EMPTY body and NO Location header** -- the new id is NOT returned here.
  (Known Opal model ids seen in the walkthrough: Opal Short-Term `P:1728415`, Opal Intermediate-Term
  `P:1728315`, Opal Long-Term Conservative `P:1728413`. Resolve any other model live via
  `GET /search/suggest/fixed_model_portfolio_items?q=Opal%20<...>`.)

**B1-upload (Fork 1b -- build from a client's Excel of ACTUAL holdings, instead of a blend of models).**
When the request gives you a client's real holdings as a file (not a set of Opal models to blend):
1. `POST /model_portfolios/fixed/holdings_upload/client` -- `multipart/form-data` with the Excel file.
   Returns `{"status":"ok","errors":[...],"rows":[{"security_id":"<TICKER>","display_security_id":"<TICKER>",
   "display_name":"<Name>","weighting":<amount>}, ...],"upload_record_id":<N>}` -- the parser resolves the
   sheet's tickers to YCharts security ids + reads the weights. Check `errors` is empty.
2. `POST /model_portfolios/fixed/` -- same shape as B1, but `items` = the returned `rows` (individual
   securities, not models) and the `portfolio` part carries **`"upload_record_id":<N>`** (the linkage;
   `imported_holdings_id` stays null). -> 201 empty.
Then B2 (resolve id) + the report spine, exactly as for a model-blend. Batch (Fork 8): loop upload->create
->report per client sheet (a walkthrough built 3 client portfolios + ran Overview on them in one session).

**B2 (resolve the new id).** Reload `GET /model_portfolios/?...&sortColumn=user_modify_date&sortDirection=desc&page=1`
(or re-navigate the list) -- the just-created blend is **row 1** (newest). Read its `P:<id>` (this is
the `securityId` for the report). Confirm calc is done: `GET /model_portfolios/<id>/status?` returns ready.

**B3 (optional recalc / edit).** To adjust weights after creation:
`PUT /model_portfolios/fixed/<id>?calculate=true` -- **JSON** (note: outer object wrapping `portfolio` +
`items`, NOT multipart): `{"portfolio":{...same fields, +"existing_portfolio_id":null,"household_level_calc_method":"traditional"},"items":[{...,"target_weighting":<pct>,"current_weighting":<pct>,"shares_weighting":<n>,"dollars_weighting":<n>}]}`.
Only needed if the operator changes the blend; the create + report path does not require it.

**B4.** Continue at **"The report-generation engine"** below with `securityId=P:<new id>`.

---

## The report-generation engine (shared by Flow A and Flow B)

Same `custom_pdf_reports` engine regardless of how the portfolio got there.

1. **Open the report menu for the security.**
   `GET /custom_pdf_reports/generate/collection?dataSource=legacy&reportType=aggregate_security_comparison:::true,,,aggregate_security_overview:::true,,,multi_security_comparison:::true&securityId=P:<id>`
   -> the template menu (folders of templates). Pick the row by **template name** (the 3 Opal uses:
   `Comprehensive Overview (No Benchmark)`, `Comprehensive Comparison (No Benchmark)`,
   `Comprehensive Multi-Comp (No Benchmark)`). Each template has an `id` (e.g. Comprehensive Overview
   (No Benchmark) = `14141822`, a YCharts public template) and a `report_type`.
2. **Open the template session.** `GET /custom_pdf_reports/generate/<templateId>`.
3. **Securities step.** For an Overview, the single security is the portfolio (pre-filled). For a
   Comparison/Multi-Comp, add security 2 (+ 3...) via `GET /search/suggest/report_securities?q=<comparison>`
   (an Opal model appears under **Portfolios** as `P:<id> Opal ...`). Validate:
   `POST /custom_pdf_reports/validate_report_securities/<templateId>` body
   `{"security_ids":["P:<id>", ...],"modules":null}` -> `200 {}`.
4. **Customize step.** Fill the metadata (title stripped to the client name; prepared_for from the
   email domain; prepared_by constant; contact block; `as_of_date_option`; draft). **Confirm the
   resolved values with the operator before a REAL client report.**
5. **Generate.** `POST /custom_pdf_reports/<templateId>` -> **`201`** -> `{"report_url":"https://ycharts-media.s3.amazonaws.com/compliance_reports/pdf_report_P_<id>_<MM-DD-YYYY>.pdf?AWSAccessKeyId=...&Signature=...&x-amz-security-token=...&Expires=..."}`.
   The generate JSON body (captured schema):
   ```json
   {"security_ids":["P:<id>"],"contact_email":"...","contact_phone":"...","contact_url":"...",
    "organization":"Opal Capital","prepared_by":"Alyssa Keith","prepared_for":"49 Financial",
    "custom_field":null,"report_title":"<client name>","as_of_date_option":"latest","designation_type":"deliverable",
    "hartford_client_id":null,"hartford_client_name":null,"hartford_firm_name":null,"hartford_model_names":null,
    "saved_hypothetical_id":null,"saved_analysis_plan_id":null,"risk_profile":null,"talking_points":{},"custom_texts":{},
    "serialized_transition_analyses":{},"naming_convention":"truncated","dollar_conversion_levels":[],
    "custom_security_labels":[],"export_type":null,"performance_disclosure_footnote":"<std footnote>","sections":[],
    "fund_chart_securities_choice":"saved_asset_securities_only","scatter_plot_securities_choice":"saved_asset_securities_only",
    "comp_table_securities_choice":"saved_asset_securities_only","timeseries_table_securities_choice":"saved_asset_securities_only",
    "generationModalsState":{"coverPageInfo":{...},"primarySecurity":{"securityId":"P:<id>","securityType":"model_portfolio"},
      "selectedReport":{"report_type":"aggregate_security_overview","id":<templateId>,"num_required_securities":1,...},
      "transitionAnalyses":{},"reportTitle":"<client name>","namingConvention":"truncated"},"reportState":null}
   ```
   The report generates async (poll `GET /background_jobs/in_progress` + `ai-proxy.ycharts.com/jobs_progress/<id>`),
   but the generate `POST` itself returns the `report_url` synchronously on `201`.

---

## Retrieve the PDF + DROP IT IN THE USER'S DOWNLOADS
On GENERATE the browser downloads the finished report; the Playwright MCP saves it to
`<workspace>/.playwright-mcp/pdf-report-*.pdf`. **Transfer it off the Playwright dir to the user's
Downloads** (Andrew-direct 2026-07-01 -- the report must land where the user can grab it):
```bash
SRC=$(ls -t "<workspace>/.playwright-mcp/"pdf-report-*.pdf | head -1)
DEST="/c/Users/AndrewBerman/Downloads/<client-name>_<template>_<YYYY-MM-DD>.pdf"
cp "$SRC" "$DEST"    # verify: head -c5 "$DEST" == "%PDF-"
```
If the browser download didn't fire, grab the `report_url` (presigned S3, expires ~1h -- fetch
promptly) from the generate response / network and `curl -o "$DEST"` it. The PDF contains CLIENT data:
it belongs in Downloads, NOT in the repo/git; delete any copy left in `.playwright-mcp` after transfer.

## Guardrails
- **Single seat:** inject the shared cookie; do not fresh-login without a clear seat + operator go.
- **Real client output is confirm-first:** show the resolved inputs (mode, blend/client, template,
  prepared_for, name/title) and ask before the final GENERATE for a real client-facing report. For an
  endpoint/format test, use a throwaway blend + a benign `prepared_for` (e.g. "Internal Test").
- **Client data:** the generated PDF + holdings + the client name are client PII -- keep local, never
  commit, never echo. Delete throwaway artifacts after.
- **Credential hygiene:** never echo cookie values; the bundle lives ONLY in `ycharts/credentials`.
- **Backtest range caveat:** the Opal models started ~April 2024, so reports can't show >5yr history --
  a short trailing window in the PDF is expected, not a bug.

## Refreshing the credential (if the session is dead / after a login)
Capture the current context cookies without displaying them and swap them in:
1. `await page.context().storageState({ path: '.playwright-mcp/yc_state.json' })` (gitignored file;
   return only a MASKED names/lengths summary).
2. Build `{"cookies": "<name=value; ...>"}` from the `ycharts.com` cookies (essentials: `ycsessionid`
   + `csrftoken` + `aws-waf-token`), write to a temp file.
3. `aws secretsmanager put-secret-value --secret-id ycharts/credentials --secret-string file://<temp>`
   (value via `file://`, never on argv). Re-read masked to confirm. **Delete the temp files.**
Note: the refreshed session stays valid only while no one else logs into that YCharts login (single
seat). For a durable service credential, use the dedicated YCharts seat (YALP_MDSRC plan), not a
shared human login.

## Under the hood (for an API-direct future)
The whole thing is server-side; a headless version can skip the browser entirely:
- BUILD: `POST /model_portfolios/fixed/` (multipart portfolio+items) -> reload
  `/model_portfolios/?sortColumn=user_modify_date&sortDirection=desc` to read the new `P:<id>`
  [-> `PUT /model_portfolios/fixed/<id>?calculate=true` to recalc].
- REPORT: `GET /custom_pdf_reports/generate/collection?reportType=<...>&securityId=P:<id>` (templates)
  -> `GET /custom_pdf_reports/generate/<templateId>` (open) ->
  `POST /custom_pdf_reports/validate_report_securities/<templateId>` (securities) ->
  `POST /custom_pdf_reports/<templateId>` (generate, returns the S3 PDF url) -> fetch the presigned url.
All authenticated with the `ycharts/credentials` cookie header + `X-CSRFToken` (from `csrftoken`) +
`X-Requested-With: XMLHttpRequest` on the POSTs. Report types: `aggregate_security_overview`,
`aggregate_security_comparison`, `multi_security_comparison`. Transition-analysis is a present-but-unused
surface here (`/model_portfolios/transition_analysis/list`, `serialized_transition_analyses`,
`transitionAnalyses`) -- wire it only if a request needs it.

## Roadmap intent (from Alyssa's walkthrough -- for the product owner, not this skill's runtime)
Alyssa's stated goal (twice) is a **front-end form** for advisors: they click exactly what they want
(client name, the models + weights, the report template) and the form auto-feeds this skill so Claude
generates the PDF -- replacing the fragile "advisor emails ambiguous free text" intake that doesn't
scale as more firms/advisors come through. This skill is the automation engine that form would drive;
the form itself is a separate frontend deliverable (flag to CTO/DE).
