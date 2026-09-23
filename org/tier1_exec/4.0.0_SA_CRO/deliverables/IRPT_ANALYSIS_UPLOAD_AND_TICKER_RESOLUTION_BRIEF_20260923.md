# Analysis tab: holdings upload (CSV/XLSX) and ticker resolution -- current state, desired state, and the Kimi check/swap

**Prepared by:** `4.0.0_SA_CRO`, 2026-09-23 ~19:0xZ.

**Scope:** read-only assessment plus closure requirements. No application change, no deploy, and NO YCharts or Kimi call
was made to write it. The 2026-07-09 fabric-wide prohibition forbids any agent-initiated vendor call without Andrew's
per-use word; see section 8.

**For:** `1.0.0_SA_CTO` (Codex), which governs IRPT under
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.3.

**Shape:** a `/closer trace` brief for one surface, the Analysis tab's prospect-upload lane ("Lane B"), plus Andrew's
requirements for it. It is a trace brief, so it needs no build word of its own; the build it describes rides the IRPT
completion effort Andrew has already authorized.

## 0. Andrew's words, verbatim (2026-09-23, at the `4.0.0_SA_CRO` terminal)

> On the Investor Reporting portal page, there is a tab called "Analysis". On that tab, users have the opportunity to
> upload a CSV or XLSX file with two fields, Column A has client holdings, Column B has a unit amount of those holdings
> (Target Weight, Current Weight, Dollars, or Shares). The reader/ingestion mechanism does not need to read any other
> information on that sheet, just those two columns. [...] I want you to write a brief that establishes the current state
> of the CSV/XLSX upload function, its parser/process/etc, and the desired state [...] This brief should cover how to work
> this into the implementation, including error functions if people upload a spreadsheet that is out of pattern for
> whatever reason. For example, one thing that it has to include is an error function if those rules are broken, or very
> importantly, if a ticker cannot be identified. I recommend a scan here with AI as part of the upload sequence that checks
> to see if it's a typo, e.g. ALPPL versus APPL, and it should have a popup after "Did you mean {suggestion}?". If we really
> cannot find the security, or if the user says "No, my input was correct", then that means we need to find a replacement
> security. This occurs often in the case of physical bonds, private reits, some mutual funds, etc. where YCharts simply
> doesn't list the asset. In this case, we need to run a websearch on the subject ticker, figure out what it is, and swap
> in a comparable security in the same segment (e.g. a bond etf, a real estate etf, etc, with similar
> sector/exposure/etc.). The similarity doesn't have to be excessively dialed in, can be coarse comparison, sector-based.
> More granularity is fine if we got it. If a mutual-fund that didnt appear in the system comes up as a private small cap
> equity mutual fund, we should try to run a small cap ETF through YCharts. This process may need to run a few times if we
> put it through and get errors in the YCharts flow due to missing securities, so that should be part of the testing of
> the upload function. Please do your investigation both into the attached document and also the YCharts backend flow to
> identify where we'd place these checks and balances, both in the UI and with the AI missing ticker Check/Swap
> functionality.

> That's fine, we just run it on a lambda with an api call, use "Kimi Pipeline" "Semantic Estate Pipeline" as reference

> Yeah I would prefer to use Kimi for this, we can use same API key and everything, it would be perfect for this use case.

> Yeah should be very small, maybe two calls, one to check, one to swap.

> Yes, the key is figuring out a system whereby we can actually test ycharts ticker database without having to do whole
> upload flow, should be smoother. We should have endpoints for that to manage this operation, that should be explored by
> you right now and worked into the brief.

**Prior requirement, same lane:** Andrew-direct 2026-09-21, recorded at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_2021Z_SENSITIVITY_ANALYSIS_EXCEL_UPLOAD_REQUIREMENT.md`:
*"the ability to upload excel sheets with Securities ($Ticker) in column A (starting in A2), and either dollars or shares
or potentially current weights in Column B (starting in B2) [...] saving these uploads in some relevant backend location,
based on firm"*.

## 1. Finding

**No version of the upload can take the business template today.** The failure has three layers:
1. The browser refuses `.xlsx`.
2. The upload route has no live handler.
3. The parser, run offline, quarantines every filled copy of the template. The template's own `$` number format reads as
   an ambiguous currency. Its B1 words "Target Weight" and "Current Weight" are not recognized units. Its leftover table
   cells block any sheet with fewer than 10 holdings.

**Security resolution does not exist in production.** The parser accepts "ALPPL" as a well-formed ticker, and the
resolver port it would reach has no implementation. What YCharts returns for an unknown symbol has **never been
captured**. When YCharts does reject an upload, the generation step keeps only a COUNT of the vendor's errors, and the
reason never reaches the user.

**Reusable pieces:**
- the parser's provenance, blank-row and `$:CASH` handling;
- the `resolve_security` port and its `SECURITY_UNRESOLVED` -> `NEEDS_CORRECTION` path;
- the approver-recorded correction mechanism;
- the Kimi call pattern from the Semantic Estate Pipeline;
- two YCharts internal endpoints already reverse-engineered for symbol lookup.

## 2. The template contract (measured from the attached `ychart template.xlsx`)

| Cell | Content | Reader rule |
|---|---|---|
| sheet | one sheet, `holdings_template` | read that sheet, or the first sheet if it is renamed; ignore any other sheet |
| A1 | `Symbol` | header; tickers start at A2 |
| B1 | data-validation list of exactly `Target Weight, Current Weight, Dollars, Shares` | **the unit of the whole column**, read from B1's text |
| A:B rows 2..n | ticker, amount | stop at the last non-blank A/B row; formatting extends the sheet to row 305, so the sheet's own extent is never the row count |
| F2:K10 (merged) | notes: cash is `$:CASH`; weights are decimals (`.05` = 5%); one household per sheet | business rules below |
| AW7, F11, G11, J11, K11 | `Target Weight` (the dropdown's source list), `Column1`/`Column2` (table-header debris) | **ignored**: nothing outside A:B is read |
| B2:B305 number format | `"$"#,##0.00_);[Red]\("$"#,##0.00\)` | a display format, never a currency signal (the unit comes from B1) |

## 3. Current state -- hop by hop

Two vintages were measured, and they give the same result:
- **V1:** workspace CLOUD `0a1c8121ac` and portal DEV `fac3b6a0`.
- **V2:** `2.0.0_SA_COO~Y`'s workspace pin `85af5eb95d`, per `IRPT_MVP_Y/STATUS.md:14`; it is not an ancestor of CLOUD.
  Y's portal pin `7a5b24e7` is an ancestor of DEV.

`parse.py`, `recipe.py`, `normalized_input.py` and `frozen_worker.py` are byte-identical between V1 and V2. V2 changes
only access and ownership code.

| # | Hop | State | Evidence (backend @`0a1c8121ac`, portal @`fac3b6a0`) |
|---|---|---|---|
| 1 | File picker -> browser | MISMATCHED | `ProspectComposer.tsx:95` `accept=".csv,text/csv"`, 1 MB cap `:47`; `prospect.ts:19-22` refuses non-`.csv`/non-UTF-8. No unit selector (the unit must come from B1); on `NEEDS_CORRECTION` it shows ONE reason code and one row (`:123-126`), never the parser's findings list |
| 2 | Browser -> API | MISSING (live) | `investor-reporting.ts:200` marks `POST .../analysis/inputs` `NO-HANDLER-AT-HEAD`; `routes.json:164-172` "Not declared in Terraform"; nothing outside tests constructs `UploadService` or calls `build_upload_entry`. `AnalysisUploadRequest.schema.json` accepts `filename` `*.csv` and `csv_base64` only |
| 3 | Upload -> storage | INCOMPLETE | `uploads.py:133-135` retains `ORIGINAL_CSV` before parsing and `:179-181` the frozen portfolio; prospect ownership `:96-97`; the bucket and key are an injected callback with no concrete binding (`reports/repository.py:423-446`) |
| 4 | Parser | WORKS for its own vocabulary, MISMATCHED to the template | XLSX is read, first sheet only (`parse.py:494-560`); `UNIT_HEADERS` (`:98-105`) maps `dollars`/`shares`/`weight`/... but has **no `target weight`/`current weight`**, so those rows get `UNITS_UNDETERMINED`; the three-member `UNITS` tuple (`:91`) cannot tell Target from Current; the `$` cell format yields `AMBIGUOUS_CURRENCY` on every Dollars row (`:234-259`, `:1082-1090`) and the portal's USD checkbox cannot clear it (`portfolio.py:169-171`); stray `Column1/Column2` at row 11 yield BLOCKING `UNPARSEABLE_QUANTITY` when A11/B11 are empty; whole-percent weights are kept as-is (`:716-738`); duplicates merge silently at freeze (`portfolio.py:228`). WORKS: `$:CASH` (`:746-747`), blank-row skipping, the 305-row extent, `" aapl "` -> `AAPL` |
| 5 | Symbol -> security identity | MISSING (production) | the parser only checks shape (`_TICKER_RE`, `:363`), so `ALPPL` passes; the `resolve_security(identifier, namespace)` port (`uploads.py:68-76`, called `portfolio.py:189`) has only test implementations; an unresolved row stops the freeze at the FIRST failure (`SECURITY_UNRESOLVED`, `portfolio.py:83-85,190-193`); the share-class map is 2 synthesized pairs |
| 6 | Units -> dollars | WORKS offline, weights lose meaning | shares need an injected price source (none in production, so `PRICE_MISSING`); weights x reference notional and must sum to EXACTLY 1 (`portfolio.py:205-231`, so rounding such as 0.3333 x 3 fails); YCharts receives dollars only (`recipe.py:390-411`, `validate_envelope` refuses other units as `UNPROVEN_HOLDINGS_UNIT` `:244-247`) |
| 7 | Frozen portfolio -> YCharts | OFFLINE ONLY | `GenerationJob(` is never constructed outside tests on CLOUD, Y, P or M. The upload step is OK only if the vendor's echoed symbol set equals what was sent (`recipe.py:438-441`), so an unknown symbol ends `UPLOAD_NOT_VERIFIED`, terminal (`job.py:359-366`); the vendor's error list is reduced to its LENGTH (`recipe.py:449-450`); security validation runs on the whole portfolio `P:<id>` only (`job.py:432-437`) |
| 8 | Failure -> user | MISSING | `ops/status_loader.py` reads the lease only (RUNNING/UNCERTAIN); the portal folds FAILED and NEEDS_CORRECTION into "needs attention" (`composer.ts:321-343`); a failed job's one-time intents never clear (`durable_job.py:156-181`), so a retry must be a NEW input and a NEW request |

**Discriminating run** (offline; the template filled with openpyxl, stray cells and formats left as a user leaves them;
identical at V1 and V2):
- **(a) Dollars**, with AAPL, MSFT, `$:CASH` and ALPPL:
  - the `.xlsx` is refused (`CSV_FILENAME`);
  - the parser gives `AMBIGUOUS_CURRENCY` x4 plus a BLOCKING row 11;
  - the freeze returns `INPUT_NEEDS_CORRECTION`;
  - **ALPPL never reaches resolution.**
- **(b) Target Weight**, decimals summing to 1: `UNITS_UNDETERMINED` x4.
- **(c) Current Weight** as whole percents: the same as (b). The percent problem is never reached.
- **Controls:**
  - with the stray cells removed and the format set to General, (a) FREEZES;
  - adding ALPPL then gives `SECURITY_UNRESOLVED` at row 5;
  - the header `Weight` with whole percents gives `WEIGHTS_DO_NOT_SUM_TO_ONE`.
- Scripts and outputs: session scratchpad `upload_trace/` (`run_trace.py`, `run_controls.py`, `out_V1.txt`,
  `out_V2.txt`).

**The lane's code population** (regex census over source, denominators as measured):
- 13 parser finding codes: 1 BLOCKING, 1 INFO and 11 UNCERTAIN.
- 8 free-text parse refusals, all surfacing to the browser as one `CSV_PARSE_REFUSED`.
- 34 freeze refusals at V1 and 37 at V2.
- 32 upload refusals at V1 and 35 at V2.

## 4. What already exists for YCharts symbol lookup (explored for Andrew's "endpoints" ask; code and records only)

| Capability | Where | What it does | Status |
|---|---|---|---|
| `GET /securities/securities_info?securities=<csv>` | YCharts internal API, documented `docs/briefs/mdsrc-ycharts-internal-api-20260520.md:33` | **batch exact-symbol lookup**, entity-agnostic: `[{id, security_name, detailed_security_type (stock/etf/mutual fund/...), display_security_id}]`; "lookup-by-exact-symbol, not search" (`:126`) | proven on bare symbols in the May research; in IRPT code it runs only on `P:` portfolio ids (`docs/research/.../variant_worker.py:102-111`) |
| `GET /search/suggest/main?q=` | `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py:267-274`; gateway `infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py:169-170` (tool `ycharts_search`) | typeahead search across categories | built; the gateway tool is audited and entitlement-gated |
| `/search/suggest/fixed_model_portfolio_items` | `.claude/skills/ycharts-report/SKILL.md:136` | the item picker YCharts itself uses when adding holdings to a portfolio | captured, not wrapped |
| YCharts per-holding Performance Proxy | holdings CSV column `Performance Proxy` (`recipe.py:402,410`, sent empty); item fields `exposure_proxy_security_id`, `is_valid` (HAR evidence `:1187-1189`) | YCharts' OWN proxy mechanism | never exercised |
| Opal security reference data | `bd-securities` DynamoDB, per-firm `dim_security` (e.g. `data/assets/scripts/gold/runners_49f/a03_dim_security.py`), `data/black_diamond/scripts/silver/security_ticker_mapping_final.py` | ticker/CUSIP/type for held securities | exists; not wired to IRPT |

**The seat constraint:**
- YCharts allows ONE concurrent session per login; a second sign-in evicts the first with a "concurrent sign in" 403
  (`ycharts_client.py:164-166`, gateway `integration.py:35-39`).
- The generation worker authenticates through `ycharts/session/current` (`ycharts/session/broker.py:62`). The gateway
  and the market-data pull use `ycharts/credentials`.
- **Whether those two are the same YCharts user is unmeasured.** If they are, a lookup through the gateway can evict a
  running report job.
- The measured-safe request spacing is 2.0 s (`ycharts_client.py:46`).

## 5. Desired state

### 5.1 The reader (the template is the contract)

- **Accept `.csv` and `.xlsx`**, end to end: picker, request schema and validator. Replace the upload request's
  `csv_base64` field with `file_base64` plus `file_type`. Excel is the primary path (Andrew 09-21).
- **Read A and B only, from the template's sheet.**
  - A1 is the symbol header (`Symbol`; accept `Ticker` case-insensitively).
  - **B1 is the unit, one of exactly four values: `Dollars`, `Shares`, `Target Weight`, `Current Weight`.**
  - Nothing outside A:B is read: no stray-cell finding, no notes, no other sheets.
  - Stop at the last row whose A or B is non-blank.
- **Four units, not three.** Carry `TARGET_WEIGHT` and `CURRENT_WEIGHT` as distinct bases in the normalized portfolio
  (contract S3), so the report can say which one it analysed. Both still convert to dollars through the disclosed
  reference notional until native weight submission to YCharts is proven. YCharts' own upload accepts Target Weight and
  Current Weight columns (`docs/research/investor_reporting_ycharts_cloud_20260911/README.md:28`); proving that path is
  an enrichment item.
- **Currency comes from B1, not from cell formatting.** `Dollars` means USD by the template's own definition. A `$`
  display format is never an ambiguity finding.
- **Cash:** `$:CASH` is YCharts' own cash symbol (it appears as "Cash" in a YCharts report). Normalize the common variants
  `CASH`, `$CASH` and `Cash` to `$:CASH`, with an INFO notice.
- **Weights:** the notes require decimals.
  - If a weight column sums to between 95 and 105, raise `WEIGHTS_LOOK_LIKE_PERCENT` with a one-click "divide by 100" fix.
  - Accept a decimal sum of 1 within a declared tolerance (proposed +/- 0.001) and show the residual.
  - Outside the tolerance, raise `WEIGHTS_DO_NOT_SUM_TO_ONE` with the actual sum.
  - Exact equality, the current rule, rejects ordinary rounding.
- **Duplicates:** merge them, with a visible `DUPLICATE_SYMBOL_MERGED` notice. Never silently.

### 5.2 Error functions ("out of pattern")

**Every finding is returned in one list with row numbers, and the UI shows all of them.** Today the UI shows one reason
code and one row.

| Code | When | What the user sees |
|---|---|---|
| `FILE_TYPE_UNSUPPORTED` | not .csv/.xlsx | "Upload the holdings template as .xlsx or .csv." |
| `FILE_TOO_LARGE` | over the cap | the cap, in plain words |
| `SYMBOL_HEADER_MISSING` | A1 is not Symbol/Ticker | "Cell A1 should read Symbol -- use the template." |
| `UNIT_MISSING` / `UNIT_UNRECOGNIZED` | B1 is empty or not one of the four | "Choose Target Weight, Current Weight, Dollars or Shares in cell B1." |
| `NO_HOLDINGS` | no rows under the headers | "No holdings found under Symbol." |
| `AMOUNT_MISSING` / `SYMBOL_MISSING` | half-filled row | the row, and which half is missing |
| `AMOUNT_NOT_A_NUMBER` | non-numeric B | the row and the value |
| `AMOUNT_NOT_POSITIVE` | zero or negative | **every** such row, not the first only |
| `WEIGHTS_LOOK_LIKE_PERCENT` | weight sum 95..105 | "These look like percents. Divide by 100?" [Fix] |
| `WEIGHTS_DO_NOT_SUM_TO_ONE` | outside tolerance | the actual sum |
| `SHARES_PRICE_UNAVAILABLE` | Shares unit, no dated price | the row; exclude it or switch to Dollars |
| `DUPLICATE_SYMBOL_MERGED` | repeated symbol | INFO: the merged amount |
| `TICKER_NOT_FOUND` | not in YCharts | opens the resolution flow (5.3) |
| `TICKER_SUBSTITUTED` | a stand-in approved | INFO: carried into the report and PDF disclosure |

### 5.3 The resolution sequence: deterministic check first, then two Kimi calls

```
upload parsed -> CHECK ALL SYMBOLS (one batch, no AI)            -> every symbol FOUND -> freeze
                     | some NOT_FOUND
                     v
   per symbol:  KIMI CALL 1 "check"  -> suggestion S (validated in YCharts before it is shown)
                     |                   popup: "Did you mean S?"   [Yes] -> row corrected (new revision)
                     |                                              [No, my input was correct] --+
                     | no validated suggestion ---------------------------------------------------+
                     v                                                                            v
                KIMI CALL 2 "swap" (web search): what the security IS + ranked comparable ETFs
                     -> each candidate checked in YCharts; first FOUND is proposed
                     popup: "We couldn't find ABC in YCharts. It looks like a private real-estate fund
                             (source). Use VNQ -- Vanguard Real Estate ETF -- as its stand-in?"
                             [Use it] [Pick another] [Exclude this holding]
                     no candidate FOUND -> ask again once, excluding the rejected ones -> then manual pick/exclude
```

- **Check, the deterministic batch** (no AI):
  1. The approved-substitution library and the resolution cache (section 5.4).
  2. Opal security reference data (`dim_security`, `bd-securities`).
  3. YCharts `securities_info` for whatever is left, in ONE batched call.
- **Kimi call 1, "check":**
  - **Input:** the unresolved symbol; YCharts typeahead candidates for it, if any (`search/suggest/main` or the
    portfolio item picker); the other symbols in the file, as context.
  - **Output:** JSON `{suggestion|null, confidence, reason}`.
  - **A suggestion is shown only if it is FOUND in YCharts.**
- **Kimi call 2, "swap":**
  - **Input:** the symbol the user asserts is correct.
  - **Web search:** Kimi's own web search. Output: JSON
    `{identified:{name, issuer, security_type, asset_class, sub_asset_class, region, cap, credit/duration if a bond},
    sources:[urls], candidates:[<=3 ETF symbols, ranked], rationale, confidence}`.
  - **Taxonomy:** asset and sub-asset classes follow the estate's existing classifier taxonomy
    (`data/black_diamond/scripts/gold/B_01b.classify_new_securities.py`).
  - **Similarity:** coarse (sector/segment), as Andrew set it. A private small-cap equity fund maps to a small-cap ETF, a
    physical bond to a bond ETF of similar credit and duration, a private REIT to a real-estate ETF.
- **Human approval:**
  - Nothing is substituted without the user's click.
  - Every accept is a correction on a NEW upload revision. The mechanism exists: `supersedes_input_id` plus
    `corrections.apply_corrections` with a named approver (`corrections.py:250-335`).
  - The frozen portfolio keeps the original symbol, the stand-in, the sources and the rationale.
  - The report and PDF disclose each stand-in. This satisfies PRD B7 ("never discarded or silently substituted; approved
    substitutions captured explicitly").
  - It also reconciles the earlier design line *"An LLM does not ... choose an arbitrary similar ticker"*
    (`docs/briefs/investor-reporting-ycharts-design-20260910.md:94`): Kimi proposes and the user decides, the reading
    `:100` of the same document already allows.

### 5.4 The endpoints: test the YCharts ticker database without running an upload (Andrew's ask)

Three small routes under the existing scoped prefix. They are the resolution sequence's building blocks, the upload
calls them, and a tester or ops seat can call them directly with a list of symbols:

| Route | Body -> result | Backend |
|---|---|---|
| `POST /api/scoped/investor-reporting/securities/check` | `{symbols:[<=200]}` -> per symbol `{input, status: FOUND / NOT_FOUND / AMBIGUOUS, ycharts_id, name, security_type, source: cache / opal / ycharts, checked_at}` | cache and Opal reference data first, then ONE `securities_info` batch for the rest |
| `POST /api/scoped/investor-reporting/securities/suggest` | `{symbol, context_symbols?}` -> `{suggestion, confidence, reason, validated:true/false}` | typeahead candidates, then Kimi call 1, then `check` on the suggestion |
| `POST /api/scoped/investor-reporting/securities/substitute` | `{symbol, exclude?:[...]}` -> `{identified, sources, proposal:{symbol, name, validated}, alternates}` | Kimi call 2 with web search, then `check` on each candidate |

- **Cache and library.**
  - The resolution cache is keyed by normalized symbol, with a longer TTL on FOUND than on NOT_FOUND. Repeat checks do
    not touch YCharts.
  - A user-approved stand-in (for example private REIT `ABC` -> `VNQ`) is stored in an approved-substitution library and
    proposed first next time, with no Kimi call. The library grows with use.
  - Both stores take names and addresses from `lib/opal_naming.py` `name()` and `address()` (CLAUDE.md Rule 30). A builder
    refusal means adding a registry row, never a hand-typed name.
- **One YCharts session.**
  - All three routes reach YCharts through the IRPT session broker (`ycharts/session/current`) under its lease, NOT
    through a second login, so a lookup cannot evict a report job.
  - Keep the 2.0 s spacing. Batch `securities_info`.
  - When the lease is held by a generation step, return `503` with `retry-after`.
- **Asynchronous where Kimi is involved.**
  - Keep `kimi-k3` behind a poll: `202` with a resolution id, then `GET .../securities/resolutions/{id}`.
  - The reason: the estate runner measured a `kimi-k3` call taking ~195 s (`estate_report_runner.py:119`), and a route
    behind an API gateway has a ~30 s integration limit. `check` stays synchronous.
  - Measure the real latency on the first QA call. A faster Kimi model id for call 1 is a config change, not a design
    change.
- **A test harness.** A small script, for example `.tools/irpt-ticker-check.py <file-or-symbols>`, calls `check` (and
  optionally `suggest`/`substitute`) on a list and prints the result table with its denominator. This is how the ticker
  database is exercised "without having to do whole upload flow". It can also back a small QA panel on the tab later.

### 5.5 The Kimi calls: mirror the Semantic Estate Pipeline

Reference: `infra/aws/ec2/estate-report-runner/estate_report_runner.py` `call_kimi_sub` (`:2446-2560`) and its
configuration (`infra/aws/terraform/estate-report/instance.tf:133-135`).

- **Endpoint and key:** `https://api.moonshot.ai/v1/chat/completions`. The key is **the same key**, Secrets Manager
  `astn/kimi/api-key` (Andrew: *"same API key and everything"*).
- **Grant:** the resolver Lambda role gets `secretsmanager:GetSecretValue` on EXACTLY that ARN. The pattern is the
  gateway's exact-ARN grant in `infra/aws/terraform/opal-gateway/ycharts-iam.tf`.
- **Model:** a config value, as in the estate runner (`ESTATE_KIMI_MODEL`, default `kimi-k3`).
- **Call mechanics, copied from `call_kimi_sub`:**
  - per-call token budgets and timeouts;
  - transient retry once, and a timeout is terminal;
  - telemetry written BEFORE the call, so it survives a timeout;
  - a code-fence-tolerant JSON parse, with a `KIMI_BADJSON`, `KIMI_EMPTY`, `KIMI_LENGTH_STARVED` taxonomy;
  - an ASCII scrub.
- **`temperature` must be 1 for `kimi-k3`** (`:2468`), so answers are not reproducible. That is acceptable ONLY because
  both calls are advisory and the user ratifies, the same argument the estate runner makes.
- **Fail-soft.** If Kimi is down or returns junk, the row stays `TICKER_NOT_FOUND` with [Pick another] and [Exclude]. The
  rest of the upload proceeds. Kimi availability never blocks a file.
- **Web search on `kimi-k3` is NOT evidenced anywhere in this repo.**
  - Prove it on the first QA call: Moonshot's built-in web-search tool, with the sources returned.
  - If it is not available, route the question back to the CTO. **Do not switch vendors silently.** The estate's other
    web-search precedent is an OpenAI Lambda (`infra/aws/lambda/keyword_intelligence_generator/lambda_function.py:241`),
    and switching to it would be a different vendor-egress decision.
- **Scope:** only symbols, and at most the file's other symbols as context, leave the estate. No amounts, no client or
  firm identifiers.

### 5.6 When YCharts still rejects a symbol during generation (the iteration Andrew named)

1. `recipe.step_upload` (`:442-455`) keeps the vendor's per-row error list, not its length. It also checks
   `needsReviewMessage` in `step_read_back` (`:581`).
2. `job.py:359-366` maps a rejected upload to a job outcome `NEEDS_CORRECTION` that names the rejected symbols, persisted
   via `durable_job.put_state`. It does not end in a bare `UPLOAD_NOT_VERIFIED`.
3. `ops/status_loader.py` reads that state, and the tab re-opens the resolution flow (5.3) for just those symbols. The
   stand-ins already rejected are excluded.
4. The resubmit is a new input plus a new request; the old job's intents are permanent by design. Each round is
   user-approved. It is bounded at **3 rounds**, then the flow falls back to manual pick or exclude.

## 6. Where it plugs in, by owner (contract v1.3 section 3)

| Piece | Where | Owner |
|---|---|---|
| picker accepts .xlsx; findings list; the two popups; the review table | `portal/src/pages/InvestorReporting/tabs/analysis/{ProspectComposer.tsx,prospect.ts}` | `2.0.0_SA_COO~Y` (analysis UI) |
| request/result schema (`file_base64`, `file_type`, findings, suggestions, substitutions) | `docs/contracts/investor-reporting/v1/{AnalysisUploadRequest,AnalysisUploadResult}.schema.json` and the generated `contracts/wire/*.ts` | Y defines; `2.0.0_SA_COO~P` integrates the shared client and `adapt.ts` |
| reader rules (5.1) and codes (5.2) | `infra/aws/lambda/investor-reporting/intake/{parse.py,uploads.py,portfolio.py}` | Y |
| production `resolve_security` + the three `/securities/*` routes + cache/library + the Kimi client | a new `intake/resolve/` beside the port (`uploads.py:68-76`) | **the CTO rules.** Security identity is close to M's "canonical crosswalks" row, but M is out on a usage limit and P holds M's scope surfaces under the live-scope exception. Recommendation: Y, since the port is Y's |
| routes, Terraform composition, the IAM grant on `astn/kimi/api-key` | route manifest and shared Terraform | P |
| generation catch-and-retry (5.6) | `ycharts/generate/{recipe.py,job.py}`, `ops/status_loader.py` | Y (worker and job states) |

**LIVE FIRST (contract v1.3 section 0) still governs.** Offline work here grades nothing until the shared scope and
bootstrap hop is live. A live `securities/check` is a cheap first live contact with the YCharts session path, before a
full generation.

## 7. Testing (acceptance for this lane)

- **Fixtures from the REAL template.** Today no fixture resembles it. Cover:
  - all four B1 units;
  - the `$` format, stray cells and 305-row extent left in;
  - fewer than 10 and 10 or more holdings;
  - `$:CASH` and its variants;
  - whole-percent and decimal weights;
  - duplicates, zero/negative, text amounts and half-filled rows;
  - a CSV exported by Excel;
  - a second sheet.
- **Resolution cases:**
  - a typo (`ALPPL` -> `AAPL`);
  - the user rejecting the suggestion;
  - a physical bond by CUSIP;
  - a private REIT;
  - a small or obscure mutual-fund share class;
  - a symbol whose first stand-in YCharts also rejects (the loop);
  - Kimi down, Kimi returning bad JSON, web search returning nothing;
  - a cache hit and a library hit (no Kimi call);
  - the YCharts lease held (503 then retry).
- **Endpoint smoke, no upload:** `check` over a 50-symbol mixed list through the harness, with the denominator printed.
- **The generation loop:** a portfolio YCharts rejects at upload goes to `NEEDS_CORRECTION` naming the symbol, then to
  resolution, a new revision, a resubmit and a PASS. Plus the bounded-3 exit.
- **One live trace:**
  1. the real template uploaded in the browser;
  2. check, then Kimi check and swap;
  3. approval;
  4. the frozen portfolio;
  5. YCharts generation;
  6. the stand-in disclosed on screen and in the PDF.
- **First step, before any fixture of a rejection can exist:** capture what YCharts actually returns for an unknown
  symbol, at both `securities_info` and the holdings upload. It has never been captured (`investor-reporting-ycharts-
  design-20260910.md:171,181`). **This needs Andrew's per-use word** (section 8).

## 8. Authorizations and open items

1. **Kimi at runtime, for this feature: authorized** by Andrew 2026-09-23 (section 0), with the same key.
   - Record it in the contract's `RULINGS.md`, because IRPT's narrative policy reads *"an external vendor model needs
     Andrew's explicit per-use word"* (`narrative/event_policy.json:51`), and this word is that authorization for the
     resolver.
   - The secret's `astn/` name is off-thread; park it per NO SIDE-QUESTS.
2. **YCharts lookups by the product at runtime** are part of the feature Andrew asked for today.
   - **Agent-initiated YCharts calls stay under the 2026-07-09 prohibition**
     (`org/tier1_exec/2.0.0_SA_COO/deliverables/INCIDENT_unsanctioned_vendor_api_ycharts_20260709.md:13-17`: no
     `ycharts_*` call, "one-off probes ... and pre-flight checks" included, without his per-use word).
   - **The one capture in section 7 therefore waits on Andrew's word.** Proposed bound: 3-5 symbols (one known, one typo,
     one private or bond), through the IRPT session, with the responses retained as fixtures.
3. **Seat identity.** Measure whether `ycharts/credentials` and `ycharts/session/current` are the same YCharts user. Read
   the secret metadata, not the values. That decides whether the gateway's `ycharts_search` may ever run beside
   generation.
4. **Kimi web search on `kimi-k3`:** unproven (5.5).
5. **The YCharts Performance Proxy option:** never exercised. Test whether YCharts accepts an unrecognized holding
   carrying a proxy ETF. If it does, the original name survives into the report with YCharts computing on the proxy.
   That would be a cleaner stand-in than a replacement row.

## 9. What this brief does not claim

- No live upload, YCharts call, Kimi call or browser walk-through was made.
- Every "current state" line is from source at the pins above, or from the offline run.
- Whether Excel's own CSV export matches the approximate CSVs in the run is inferred.
- The owner of the resolution service is the CTO's call under contract section 3; section 6 gives a recommendation only.
- The ~30 s gateway limit is the standard API-gateway integration ceiling. The IRPT route's actual timeout was not
  measured.

## 10. Evidence anchors

- Template: `C:\Users\AndrewBerman\Downloads\ychart template.xlsx`, read with openpyxl: every cell, the comment, the data
  validation and the merged range.
- Upload lane: `infra/aws/lambda/investor-reporting/intake/{parse.py,uploads.py,upload_entry.py,portfolio.py,corrections.py}`;
  `portal/src/pages/InvestorReporting/tabs/analysis/{AnalysisTab.tsx,ProspectComposer.tsx,prospect.ts,composer.ts}`;
  `portal/src/api/endpoints/investor-reporting.ts`; `docs/contracts/investor-reporting/v1/`.
- Generation: `infra/aws/lambda/investor-reporting/ycharts/{generate/recipe.py,generate/job.py,session/broker.py}`;
  `ops/status_loader.py`.
- YCharts lookup: `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py`;
  `infra/aws/ec2/opal-gateway/app/integrations/ycharts/`; `docs/briefs/mdsrc-ycharts-internal-api-20260520.md`.
- Kimi: `infra/aws/ec2/estate-report-runner/estate_report_runner.py`; `infra/aws/terraform/estate-report/instance.tf`.
- Prior briefs: `org/tier1_exec/4.0.0_SA_CRO/deliverables/SENSITIVITY_END_TO_END_GAP_BRIEF_20260922.md` (hops 4-5, 7,
  10-12); `docs/briefs/investor-reporting-ycharts-design-20260910.md`.
- Pins: workspace CLOUD `0a1c8121ac`; Y `85af5eb95d`; portal DEV `fac3b6a0`.
