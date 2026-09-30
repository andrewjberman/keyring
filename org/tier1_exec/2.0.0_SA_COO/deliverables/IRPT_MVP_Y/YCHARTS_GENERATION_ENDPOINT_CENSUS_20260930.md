# YCharts report-generation endpoint census -- from Andrew's own three-route HAR (2026-08-21)

Author `2.0.0_SA_COO~Y`, 2026-09-30 ~07:1xZ. **Andrew-direct ~06:5xZ:** *"record HAR and identify the endpoints that
appear in that recording ... see if we can just call those in order and assemble with a script."* Record
`ANDREW_DIRECT_20260930_065xZ_NO_DAYPASS_PROVE_3_VARIANTS_RECORD_HAR_THEN_ENDPOINT_REPLAY.md` @51edcd3ee6.

## The instrument, and why no new capture was needed for this half

**A HAR of all three variants already exists**, recorded by Andrew himself:
`.runtime/codex-seats/4.0.0_SA_CRO/ycharts-recon/YCharts HAR Handoff - Andrew/hars/01 All three routes - Overview + Comparison + MultiComp (2026-08-21).har`

220 entries; hosts: `ycharts.com` 122, then LinkedIn/HubSpot/WAF/Stripe/cookieyes noise. Filtered to `ycharts.com`,
non-static (no js/css/png/svg/woff/ico/gif/jpg/map): **35 unique (method, path) pairs.** Method, count, status and
MIME are from the HAR; nothing inferred. Values, cookies and bodies were not read.

## THE ANSWER TO THE FIRST QUESTION: generation is REST, not a browser crawl

Per variant the vendor's own web app does **four JSON calls and one PDF GET**, and the template ids match
`templates.json` one-to-one (OVERVIEW 14141822, COMPARISON 14141824, MULTI 14141847):

| step | method | path | status | MIME |
|---|---|---|---|---|
| 1 | GET | `/custom_pdf_reports/generate/<template_id>` | 200 | json |
| 2 | POST | `/custom_pdf_reports/validate_report_securities/<template_id>` | 200 | json |
| 3 | POST | `/custom_pdf_reports/<template_id>` | **201** | json |
| 4 | GET | `/compliance_reports/pdf_report_<...>.pdf` | 200 | **application/pdf** |

**The browser is needed only to obtain the session (login, WAF, cookies). Generation itself is a session-cookie REST
sequence** -- which is Andrew's canonical pattern, and which the resident's `transport.py` already replays in Python.
So *"YCharts native generation"* (V1) and *"call those in order and assemble with a script"* (V2) share the same four
calls; V2's delta is what happens to the PDF and the data afterwards, not how they are obtained.

## The full ordered sequence, one row per unique (method, path), first-seen index from the HAR

| # | method | n | st | MIME | path | what it is |
|---|---|---|---|---|---|---|
| 9 | GET | 1 | 200 | html | `/model_portfolios/fixed/client/new/` | the "new client portfolio" page |
| 10 | GET | 2 | 200 | json | `/accounts/preferences` | user preferences read |
| 11 | GET | 2 | 200 | json | `/accounts/client_group_preferences` | |
| 12 | GET | 8 | 200 | json | `/securities/securities_info` | ticker resolution during upload |
| 14 | GET | 2 | 200 | json | `/notifications/collection` | noise |
| 15 | GET | 2 | 200 | json | `/background_jobs/in_progress` | polling |
| 42 | POST | 2 | **400** | json | `/model_portfolios/fixed/holdings_upload/client` | **holdings upload -- 400 TWICE in Andrew's own run** |
| 50 | PUT | 5 | 200 | json | `/accounts/preferences` | preference writes (the `global_preference_put_census` in the offline suite watches these) |
| 51 | POST | 1 | **201** | json | `/model_portfolios/fixed/` | **portfolio created** |
| 53 | GET | 1 | 200 | html | `/model_portfolios/list/` | |
| 59 | GET | 26 | 200 | json | `/integrations/schwab/status` | polling noise |
| 62 | GET | 1 | 200 | json | `/integrations/collection/active` | |
| 64 | GET | 1 | 200 | json | `/data_templates/library_menu/model_portfolio` | |
| 65 | GET | 1 | 200 | json | `/model_portfolios/transition_analysis/list` | |
| 66 | GET | 1 | 200 | json | `/security_lists/dynamic_menu` | |
| 67 | GET | 1 | 200 | json | `/model_portfolios/` | |
| 68 | GET | 22 | 200 | json | `/model_portfolios/collection_status` | polling |
| 81 | GET | 25 | 200 | json | `/integrations/hartford/status` | polling noise |
| 153 | GET | 1 | 200 | json | `/custom_pdf_reports/generate/collection` | report menu |
| 155 | GET | 1 | 200 | json | `/custom_pdf_reports/generate/14141822` | **OVERVIEW step 1** |
| 160 | POST | 1 | 200 | json | `/custom_pdf_reports/validate_report_securities/14141822` | OVERVIEW step 2 |
| 161 | GET | 1 | 200 | json | `/accounts/share_groups/report_branding/` | branding read |
| 164 | GET | 3 | 200 | json | `/model_portfolios/2284714/status` | the client portfolio's status |
| 165 | POST | 1 | **201** | json | `/custom_pdf_reports/14141822` | **OVERVIEW generated** |
| 168 | GET | 1 | 200 | **pdf** | `/compliance_reports/pdf_report_P_2284714_08-21-2026.pdf` | **OVERVIEW PDF** |
| 174 | GET | 1 | 200 | json | `/custom_pdf_reports/generate/14141824` | **COMPARISON step 1** |
| 176 | GET | 3 | 200 | json | `/search/suggest/report_securities` | comparison picker |
| 181 | POST | 1 | 200 | json | `/custom_pdf_reports/validate_report_securities/14141824` | COMPARISON step 2 |
| 185 | GET | 1 | 200 | json | `/model_portfolios/1728413/status` | the comparison model's status (`opal_long_term`) |
| 186 | POST | 1 | **201** | json | `/custom_pdf_reports/14141824` | **COMPARISON generated** |
| 190 | GET | 1 | 200 | **pdf** | `/compliance_reports/pdf_report_P_2284714_vs_P_1728413_08-21-2026.pdf` | **COMPARISON PDF** |
| 196 | GET | 1 | 200 | json | `/custom_pdf_reports/generate/14141847` | **MULTI step 1** |
| 206 | POST | 1 | 200 | json | `/custom_pdf_reports/validate_report_securities/14141847` | MULTI step 2 |
| 211 | POST | 1 | **201** | json | `/custom_pdf_reports/14141847` | **MULTI generated** |
| 213 | GET | 1 | 200 | **pdf** | `/compliance_reports/pdf_report_08-21-2026_2KyzONQ.pdf` | **MULTI PDF** |

## Three things the census says that were not known before tonight

1. **Andrew's own successful run hit `400` twice on the holdings upload** before the portfolio POST succeeded. The
   resident's `TransportRefused` / retry logic around that call should be read against this: a 400 on
   `holdings_upload/client` is evidently part of the vendor's normal flow, not necessarily a failure.
2. **Two `PUT /accounts/preferences` writes per variant, five in total.** The offline suite's
   `global_preference_put_census` exists because these are *global* account-state writes that a replay can leak.
3. **The comparison model's status is read by id** (`/model_portfolios/1728413/status` = `opal_long_term`) between
   validate and generate. That is the one place the catalogue's `security_id` meets the vendor.

## What this census does NOT establish

- Request or response BODIES. The HAR has them; this census deliberately reads method/path/status/MIME only.
  Body shapes for V2 replay are the next read, and `recipe.py` already encodes the POST body for step 3.
- Whether these endpoints are stable or versioned. They are the web app's internal API; YCharts publishes no contract
  for them. That is V2's standing risk and it is named here rather than discovered later.
- A fresh HAR from tonight's canonical-identity run. Andrew asked for one; this file is the census of the recording
  that already existed, so the walk's own recording can be DIFFED against it rather than censused from scratch.

## For V2 -- what "assemble with a script" would take

The four calls per variant plus the upstream portfolio create. `deck_generation/dev/scripts/` holds a compose engine
(`engine.compose.Deck`, e.g. `opal_firm_overview_build.py`) that builds Opal-branded `.pptx` from a slide library --
plausibly the script Andrew means by *"Alyssa's"*; authorship not confirmed here. Its input is content, so V2's
missing piece is the DATA behind the vendor's PDF, which is what the step-1 `generate/<template_id>` JSON and the
section extraction (`ycharts/extract/`) already carry.
