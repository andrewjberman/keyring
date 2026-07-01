---
name: ycharts-report
description: Generate a YCharts client PDF report -- the comparison / "stress test" proposal engine (Comprehensive Comparison / Proposal / Overview / Performance-and-Risk, etc.) -- by driving the YCharts internal flow with Playwright, authenticated from the `ycharts/credentials` Secrets Manager cookie bundle (NO fresh login, so the single YCharts seat is not evicted). Fully parameterized: pick the CLIENT portfolio by name, a COMPARISON security/model (e.g. an Opal model), a report TEMPLATE + type, and customize every report field (title, prepared-for/by, organization, contact info, performance-as-of, draft). Produces the finished PDF (a presigned S3 URL) and can save/return it. Use when the operator says "/ycharts-report", asks to "run a YCharts stress test / comparison report", "generate a client comparison PDF / proposal in YCharts", "build the David-Vickers-vs-Opal report", or similar. Opal-specific; needs the Playwright MCP + AWS access to `ycharts/credentials`.
---

# /ycharts-report -- YCharts client comparison / stress-test PDF report

Automates the exact YCharts flow an analyst runs by hand: take a **client portfolio**, compare it
against a **model** (e.g. an Opal model), pick a **report template**, fill the client-facing
**metadata**, and generate a **client-ready PDF**. Reverse-engineered live 2026-07-01 (0.7.0_AE);
this skill reproduces that proven flow and parameterizes every input.

The engine behind it is YCharts' `custom_pdf_reports` API -- a server-side **generate -> presigned
S3 PDF** flow, so the finished PDF is retrievable programmatically (it is not a client-side render).

## When to use
Operator types `/ycharts-report`, or asks to produce a YCharts client comparison / proposal /
stress-test / tearsheet PDF (client-vs-model). NOT for raw market-data pulls -- that is the
read-only `ycharts_*` MCP integration (`app/integrations/ycharts/`); this skill is the
report-GENERATION flow (it creates a report artifact), so it is confirm-first on real client output.

## Inputs (ask for what's missing; sensible defaults noted)

| Input | Meaning | Default |
|---|---|---|
| `client` | The client portfolio -- a **name** (fuzzy-matched in the portfolio list) or a `P:<id>` | required |
| `comparison` | The security/model to compare against -- a name (autocomplete) or `P:<id>` (e.g. `Opal Long-Term Conservative`) | required for comparison reports |
| `template` | Report template name | `Comprehensive Comparison` |
| `report_type` | `1 Security` / `2 Securities` / `3+ Securities` | inferred from #securities (`2 Securities` for client-vs-one-model) |
| `title` | Report title | auto: `"<client> vs. <comparison> <template>"` (editable) |
| `prepared_for` | Recipient / client name shown on the report (REQUIRED by YCharts) | ask the operator |
| `prepared_by` | Advisor name | the seat owner (e.g. `Alyssa Keith`) |
| `organization` | Firm | `Opal Capital` |
| `contact_phone` / `contact_email` / `contact_url` | Contact block (phone + URL are REQUIRED by YCharts) | the seat's saved values |
| `custom_field` | Optional custom field | empty |
| `data_as_of` | `PERFORMANCE/RISK DATA AS OF` -- `Latest` or a date | `Latest` |
| `print_as_draft` | Watermark as draft | `false` |
| `output_dir` | Where the finished PDF is dropped for the user | the user's Downloads (`C:\Users\AndrewBerman\Downloads`) |

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
   refresh (see "Refreshing the credential" below); STOP and report -- do not fall back to a fresh
   login without operator go (it would evict the live seat).

If injection is not viable and the operator explicitly OKs a login: the seat must be confirmed CLEAR
first, and after finishing, refresh `ycharts/credentials` from the new session (see bottom). The
login user/pw are NOT stored in this file -- read them from the operator or a secret at run time.

## The flow (proven selectors + the endpoint each step hits)

1. **List + resolve the client.** `GET https://ycharts.com/model_portfolios/list/`. Find the client
   row: type `client` into the list Search box, or scan rows for the name; capture its portfolio id
   `P:<id>` (the edit link is `/model_portfolios/client/<id>/edit/`). Endpoint: `GET /model_portfolios/`.
2. **Open the row menu -> Generate Report.** Click the row's actions button
   `#list-item-dropdown-model_portfolio-<id> > .btn.btn-secondary`, then the **"Generate Report"**
   menu link (match by text). (Other menu items: Export Holdings, Download Source File, Change Type,
   Duplicate, Delete -- ignore.)
3. **Generate Report modal.** Set **Report Type** (checkboxes `1 Security` / `2 Securities` /
   `3+ Securities`) and pick the **template** row by name (`template`, e.g. `Comprehensive Comparison`;
   others: `Comprehensive Proposal`, `Comprehensive Overview`, `Performance and Risk Comparison`,
   `Three Page Comparison`, `Comparison Report with Risk Profiles`, ...). Click **Start**
   (`[data-test-id='Start']`). Endpoint: `GET /custom_pdf_reports/generate/collection?...reportType=
   aggregate_security_comparison,aggregate_security_overview,multi_security_comparison&securityId=P:<id>`
   then `GET /custom_pdf_reports/generate/<sessionId>` + `GET /data_templates/library_menu/model_portfolio`.
4. **Securities step ("Generate N Securities Report").** Security 1 is the client (pre-filled).
   For security 2, type `comparison` into `[data-test-id="secondary-security-autocomplete"] input[name="q"]`
   -> pick the match from the grouped dropdown (Portfolios / Separate Account / Mutual Funds; an Opal
   model appears under **Portfolios** as `P:<id> Opal ...`). Endpoint: `GET /search/suggest/report_securities?q=<comparison>`.
   Click **NEXT** -> `POST /custom_pdf_reports/validate_report_securities/<sessionId>`.
5. **Customize step.** Fill the report metadata from the inputs: `REPORT TITLE` (auto-filled,
   overridable with `title`), `PREPARED FOR*` (`prepared_for`, placeholder "Enter recipient's name"),
   `PREPARED BY*`, `ORGANIZATION`, `CONTACT PHONE*`, `CONTACT EMAIL`, `CONTACT URL*`, `CUSTOM FIELD`,
   `PERFORMANCE/RISK DATA AS OF` (`data_as_of`), `Print as Draft` (`print_as_draft`). Required*: title,
   prepared_for, prepared_by, contact_phone, contact_url. **Confirm the values with the operator
   before generating a REAL client report.**
6. **Generate.** Click **GENERATE**. Endpoint: `POST /custom_pdf_reports/<sessionId>` -> `201`.
   The report generates async (poll `GET /background_jobs/in_progress` + `ai-proxy.ycharts.com/jobs_progress/<id>`).
7. **Retrieve the PDF + DROP IT IN THE USER'S DOWNLOADS.** On GENERATE the browser downloads the
   finished report; the Playwright MCP saves it to the Playwright output dir
   (`<workspace>/.playwright-mcp/pdf-report-*.pdf`). **Transfer it off the Playwright dir to the
   user's Downloads** (Andrew-direct 2026-07-01 -- the report must land where the user can grab it):
   ```bash
   SRC=$(ls -t "<workspace>/.playwright-mcp/"pdf-report-*.pdf | head -1)
   DEST="/c/Users/AndrewBerman/Downloads/<client>_vs_<comparison>_<template>_<YYYY-MM-DD>.pdf"
   cp "$SRC" "$DEST"    # verify: head -c5 "$DEST" == "%PDF-"
   ```
   Report the Downloads path to the operator. (Underlying source: the report is a **presigned S3 URL**
   `GET https://ycharts-media.s3.amazonaws.com/compliance_reports/pdf_report_P_<client>_vs_P_<model>_<date>_<hash>.pdf?<AWSAccessKeyId>&<Signature>&<x-amz-security-token>&Expires=...`
   -- if the browser download didn't fire, grab that URL from the network and `curl -o "$DEST"` it;
   it expires ~1h, so fetch promptly.) The PDF contains CLIENT data: it belongs in the user's
   Downloads, NOT in the repo/git; delete any copy left in `.playwright-mcp` after transfer.

## Customization / "various edits"
- **Different report shape:** change `template` (comparison vs proposal vs overview vs perf/risk) and
  `report_type` (1 / 2 / 3+ securities). 3+ securities = multi-comparison (add more securities in step 4).
- **Different benchmark/model:** change `comparison` (any YCharts security, ETF, fund, index, or model
  portfolio -- e.g. any of the Opal models, or `S&P 500 Total Return`).
- **Branding / recipient:** `title`, `prepared_for`, `prepared_by`, `organization`, contact block,
  `custom_field` are all free-text.
- **As-of date:** `data_as_of` to a specific date for a point-in-time report; `Latest` otherwise.
- **Draft:** `print_as_draft=true` to watermark.
- **No-benchmark variants** exist as their own templates (`... (No Benchmark)`).

## Guardrails
- **Single seat:** inject the shared cookie; do not fresh-login without a clear seat + operator go.
- **Real client output is confirm-first:** show the resolved inputs (client, comparison, template,
  prepared_for) and ask before the final GENERATE when producing a real client-facing report. For an
  endpoint/format test, use a throwaway portfolio + a benign `prepared_for` (e.g. "Internal Test").
- **Client data:** the generated PDF + any holdings are client PII -- keep local, never commit, never
  echo. Delete throwaway artifacts after.
- **Credential hygiene:** never echo cookie values; the bundle lives ONLY in `ycharts/credentials`.

## Refreshing the credential (if the session is dead / after a login)
Capture the current context cookies without displaying them and swap them in:
1. `await page.context().storageState({ path: '.playwright-mcp/yc_state.json' })` (writes cookies to a
   gitignored file; return only a MASKED summary of names/lengths).
2. Build `{"cookies": "<name=value; ...>"}` from the `ycharts.com` cookies (essentials must include
   `ycsessionid` + `csrftoken` + `aws-waf-token`), write to a temp file.
3. `aws secretsmanager put-secret-value --secret-id ycharts/credentials --secret-string file://<temp>`
   (value via `file://`, never on argv). Re-read masked to confirm. **Delete the temp files.**
Note: the refreshed session stays valid only while no one else logs into that YCharts login (it will
evict / be evicted -- single seat). For a durable service credential, use the dedicated YCharts seat
(YALP_MDSRC plan), not a shared human login.

## Under the hood (for an API-direct future)
The whole flow is the `custom_pdf_reports` engine; a headless version can skip the browser:
`GET /custom_pdf_reports/generate/collection?reportType=<...>&securityId=P:<id>` (templates) ->
`GET /custom_pdf_reports/generate/<sessionId>` (open session) ->
`POST /custom_pdf_reports/validate_report_securities/<sessionId>` (securities) ->
`POST /custom_pdf_reports/<sessionId>` (generate, returns the S3 PDF url) -> fetch the presigned S3 url.
All authenticated with the `ycharts/credentials` cookie header + `X-CSRFToken` (from the `csrftoken`
cookie) + `X-Requested-With: XMLHttpRequest` on the POSTs. Report types seen:
`aggregate_security_comparison`, `aggregate_security_overview`, `multi_security_comparison`.
