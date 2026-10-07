# BRIEF -- AI autosuggest for unrecognized securities: the check/swap operations and their UI (L1, midstream)

**Author:** `4.0.0_SA_CRO~DELL2`. **Asked by:** `1.0.0_SA_CTO~DELL2`, research ask
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RESEARCH_ASK_CRO_CHECK_SWAP_AI_AUTOSUGGEST_UX_20261007.md` @e6feb11bbc.
**Authority:** Andrew-direct ~08:0xZ 2026-10-07, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_080xZ_CRO_RESEARCH_ARM_AI_SWAP_AUTOSUGGEST_CHECK_SWAP_UX.md`
@1ea0796be2, VERBATIM: "I am more intrigued in AI functionalities for autosuggesting swaps of unrecognized securities and
associated frontend ops for that process. I will bring on 4.0.0_SA_CRO in to help assess the current check 1 swap 2
operations and how to make them more user friendly in UI UX."
**Mode:** research only. No build, cut, deploy, vendor call or YCharts call was made.
**Measured at:** workspace HEAD `30f94c3ab1`, portal `origin/DEV` `8ddfe409`, 2026-10-07 08:12Z.

---

## PART 0 -- How the midstream constraint was honoured, and where it bent

- This brief reads the SERVED code (intake modules at HEAD, the page at portal `origin/DEV`), the CTO rulings that shaped
  it, and IRPT_YCDGEN PRD FWD-16. It does not read IRPT_BCKEND or IRPT_YCDGEN task orders.
- **Where it bent:** the ask itself names Y-5 packet 2 and batch 218. Answering question 2 required reading the batch 218
  ruling and the `~Y` QA findings behind it, which is branch material. The packet 2 recommendation in section 4.1 is
  therefore NOT blind. The outcomes in Part I were written from the served page and Andrew's words, not from packet 2.
- **Correction to the ask's table:** the upload review card is `tabs/analysis/ProspectComposer.tsx` (541 lines), not
  `InputReview.tsx`. `InputReview.tsx` is the FE-s-6 inferred-input review for an `AnalysisRequest` and contains no
  suggestion code. Every Y-4 and Y-5 page change landed in `ProspectComposer.tsx` and `prospect.ts`
  (portal `c67c242f`, `c32ef52a`, `56b71adb`).

---

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1 shape):** one advisor uploads one prospect file through the Analysis tab. The file has one
mistyped ticker (APPL) and one fund the data provider cannot price (TIMXX). The advisor clears both rows on the review card
without editing the file and gets a report. This is the journey Y-4 and Y-5 already made work. The outcomes below make it
easier to use; they do not create it.

### O1 -- An advisor sees what a flagged ticker probably meant, and why, before accepting it
Today the row says "Did you mean AAPL?" and shows only a ticker. The advisor can judge a suggestion only if it shows the
security's name and the reason it was suggested.

### O2 -- An advisor fixes a typo in one action
Today accepting a suggestion takes two clicks ("Use AAPL", then "Review with this proxy") and then a new resolve wait.

### O3 -- An advisor picks a stand-in for an unpriceable fund from a short list instead of recalling a ticker
Today a gated or unknown fund offers only an empty "Ticker" box. The stand-ins the advisor could choose from already
exist in Opal's ETF table.

### O4 -- An advisor clears every flagged row in one pass
Today each row is handled separately. There is no "accept all suggestions" action.

### O5 -- A report reader can tell a corrected typo from a stand-in
Today an accepted typo fix is disclosed as "APPL is analysed as AAPL, a proxy you named". That wording is wrong for a typo.

### O6 -- An advisor whose ticker matches several securities picks the intended one
Today an AMBIGUOUS ticker produces a finding whose only action is to replace the file. The provider's candidates are
already in hand but are not shown.

### O7 -- An advisor is told plainly when the check could not run, and that the file is not at fault
Today `TICKER_CHECK_UNAVAILABLE` has no user-facing words, so the page shows the raw code, and its action tells the
advisor to replace the file.

---

## PART II -- WHERE THE BOUNDARY SITS

| Surface | Owner (per CTO rulings and the YCDGEN PRD) | Relation to this brief |
|---|---|---|
| Intake check gate, resolver, advisory (`intake/upload_suggestions.py`, `security_resolution.py`, `resolution_kimi.py`) | IRPT_BCKEND, `2.0.0_SA_COO~Y` lineage | Owns every backend change in Part IV section 4 |
| Wire contracts (`AnalysisUploadRequest`, `AnalysisUploadResult`), report disclosure wording | P lineage (public schema, wire, display, export) | O5 needs a wire field |
| Upload review card (`ProspectComposer.tsx`, `prospect.ts`) | IRPT_BCKEND page half (`~D` FAST history) | Owns every page change |
| Verification against Opal data; swap candidates by class (S31, S32) | IRPT_YCDGEN FWD-16 (C-RESOLVE, C-CLASSIFY) | Relied on. This brief does not re-own FWD-16 |
| `etf-classifications` table | MDPF_SECCLASS, `2.0.0_SA_COO~M` | Read-only dependency |
| Kimi model choice and vendor terms | Andrew | Pinned `kimi-k3` for both kinds (RULINGS.md:308) |

---

## PART III -- THE QUALITATIVE BAR

- An advisor never has to leave the page, open a search engine, or edit the spreadsheet to clear a typo.
- An advisor who sees a suggestion can tell from the row alone whether it is right, without opening YCharts.
- A stand-in offered for a fund is a security Opal already analyses, so the advisor never accepts one that fails later.
- Nothing is substituted without the advisor's explicit action. This bar is inherited (RULINGS.md:268, :292) and stays.
- The report's reader can distinguish "the client's file had a typo" from "this fund was modelled with a stand-in".

---

## PART IV -- THE SUBSTRATE: findings, each measured

### 4.1 Question 2 -- what the AI does and does not do

| | `check` (Y-4, LIVE) | `swap` (Y-5 packet 2, NOT LIVE) |
|---|---|---|
| Trigger | a `TICKER_NOT_FOUND` row only (`upload_suggestions.py`, `targets`) | would serve NOT_FOUND and gated rows (`resolution_action = CHECK_THEN_SWAP`, `security_resolution.py:151-154`) |
| Model and budget | `kimi-k3`, 16k tokens, 120 s per call; at most 6 rows per upload; 240 s total for the gate (`resolution_kimi.py:20-22`, `upload_suggestions.py:18-23`) | `kimi-k3`, 32k tokens, 240 s |
| Context sent | the symbol plus up to 20 other symbols from the file. No amounts, names or client data (prompt in `resolution_kimi.py:prompt_for`) | the symbol, context and up to 6 excluded symbols; asks for web search and up to 3 ETF alternatives with sources |
| Output | `{suggestion, confidence, reason}` | identified asset, 8 classification fields, sources, up to 3 candidates |
| Verification before showing | the suggestion must come back FOUND, as an exact match, from the same YCharts `securities_info` read, with a receipt (`upload_suggestions.py`, `verified`) | the schema requires sources, and every candidate would still pass the provider read |
| What reaches the page | `suggestion: {symbol, source, provider_receipt_sha256}` only. **`reason` and `confidence` are dropped**, and no security name is carried | nothing; every swap call returns `KIMI_WEB_SEARCH_UNVERIFIED` (`resolution_kimi.py`, `KimiAdvisory.call`) |
| Slow, refused or wrong | any failure, timeout or unverified answer leaves the finding exactly as the freeze wrote it. The page shows no sign that a check was tried | -- |

**Measured wait:** the Y-4 check gate took 15.6 s on the typo file (IRPT_BCKEND `STATUS~Y.md:27`, REQ-0d97252f). The
page polls the resolve every 3 s, up to 40 times (about 2 minutes), and then shows "Resolving the symbols is taking longer
than expected" (`ProspectComposer.tsx:261-270`).

**Y-5 packet 2 and batch 218.** Packet 2 is the `swap` call: the model web-searches an unavailable asset and proposes up
to three ETFs. Batch 218 (RULINGS.md:6533-6552, 2026-10-03) held it for these reasons:
- `~Y`'s QA (9 runs, `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y5P2/KIMI_WEB_SEARCH_QA_FINDINGS_20261003.md`)
  showed that `kimi-k3` requests `$web_search` but rejects the tool echo (400 "tokenization failed", 3 shapes). `kimi-k2.6`
  accepts the echo but answers outside the schema, and JSON mode fails with a 500 error.
- The user-named proxy (Y-5, served) already covers the case, so the convenience was YAGNI.
- The direction ruled for any later pickup is **(b): candidates from `etf-classifications` (same class and sub-class),
  verified by the same read. The model may rank or word them but never invents one.** Option (a), a two-model chain, was
  refused.
- IRPT_YCDGEN FWD-16 already carries direction (b) as S32, "swap candidates from `etf-classifications` by asset class and
  sub asset class, ETFs first" (PRD:326, C-RESOLVE PRD:200).

**Research view on packet 2 (for the CTO's re-rule; the CTO decides):** packet 2 as written needs model web search, which
the QA showed does not work on the pinned model. Andrew's new interest is served by the S32 design, not by packet 2. The
web-search swap should stay held, and the swap Andrew asks about should be built as S32.

### 4.2 Question 1 -- what the user sees today (the served page, read from code)

The walk was read from `ProspectComposer.tsx` at `origin/DEV` and its fixtures. It was not rendered; see Part VII.

| Step | What the user sees and does | Where they get stuck or must guess |
|---|---|---|
| 1. Choose a file, press "Review portfolio" | Status "Resolving symbols..." twice (the step label at `:367-368` and the line at `:396`). Button reads "Resolving symbols..." | Two identical messages. No count of symbols, and no hint that a typo check is running |
| 2. Wait | 15.6 s measured for the typo file; up to about 2 min before the page gives up | No progress shown |
| 3. NEEDS_CORRECTION | Amber line "Review required: <reason>. Correct the file or valuation options and review again, or name a proxy below for a security the data provider cannot price." | The first advice is to edit the file, although the page can now fix the rows itself |
| 4. Findings list | One bullet per finding, using the server's words, e.g. "Row 2: Our data provider does not recognize this ticker. Check it for a typo, or name a similar ticker to stand in for it (a proxy) ..." (`uploads.py:51-54`) | Says the same thing as the proxy rows below it. A finding without declared words prints its raw code (`:410`) |
| 5a. Typo row (APPL) | "APPL (row 2) is analysed as [Ticker]  Did you mean AAPL?  [Use AAPL]" | The input sentence ("is analysed as") is framed as a stand-in, not a fix. Only a ticker is shown, with no name, reason or confidence. "Use AAPL" only fills the box |
| 5b. Gated fund (TIMXX) | "TIMXX (row 100) is analysed as [Ticker]" with an empty box | The advisor must know a comparable ticker from memory. No list, no search, no class shown |
| 5c. Delisted or merged fund | Becomes `TICKER_NOT_FOUND`. The `check` prompt asks only "is this a typo", so at best it suggests a successor ticker labelled "Did you mean" (INFERRED from the prompt text; not exercised) | A successor fund is a substitution, not a typo, but it would be shown and disclosed the same way |
| 5d. Ambiguous ticker | `TICKER_AMBIGUOUS` with actions `["REPLACE_FILE"]` (`portfolio.py:444`). Not NAME_PROXY, so it gets no proxy row (`prospect.ts:60`) | Dead end: the advisor must edit the file. The provider's candidates are in the resolver result and are not shown |
| 5e. Provider outage | `TICKER_CHECK_UNAVAILABLE`, actions `["REPLACE_FILE"]`. No entry in `CORRECTION_WORDS` (`uploads.py:40-53`), so the page prints "TICKER_CHECK_UNAVAILABLE, row 3" | Raw code, and advice that blames the file |
| 6. "Review with this proxy" | Re-posts the same upload with corrections; a full resolve runs again (step 1) | A second wait for a one-ticker fix. No undo before it is sent |
| 7. Normalized | "APPL is analysed as AAPL, a proxy you named." (`:494`) | A typo fix is described as a proxy, and the same wording reaches the disclosure |

### 4.3 Question 3 -- past patterns

**In the estate:**
- RULINGS.md:268, :292 (2026-09-23): suggestions are advisory and need explicit user acceptance on a new revision, with
  disclosure on screen and in the PDF; holdings are never substituted automatically. These are binding constraints, not
  options.
- RULINGS.md:270, :292: check suggestions are shown only after a deterministic FOUND.
- RULINGS.md:308: Andrew pins `kimi-k3` for both kinds, and a faster model needs his new direction. This bears on the wait in
  step 2.
- RULINGS.md:318: a security the provider gates by entitlement enters the same check/swap path as a missing one, and
  provider outages stay UNAVAILABLE, never NOT_FOUND. The page today honours the first part of that ruling for proxies
  but not for suggestions.
- Batch 218 (above): web search refused; catalogue-first is the direction.
- **Prior art in the portal:** `src/pages/TradeSubmission/components/TickerAutocompleteInput.tsx` (179 lines) is a debounced
  (300 ms) ticker typeahead with an `onLookup` port. Its pattern fits the empty proxy box.
- **Prior art in the page:** the Analysis tab already fetches the `etf-classifications` catalogue for the comparison picker
  (`fetchCatalogue`, `comparisonCatalogue.ts`; the server reads `dynamodb:etf-classifications`,
  `_scope/maintained_sources.py:540`). A stand-in picker can read the same list with no new backend route.

**Outside the estate: NOT RESEARCHED.** Searching the web is egress off Opal infrastructure, which CLAUDE.md excludes from
agent autonomy. This brief therefore cites no external product. The patterns the ask names (confidence, reason,
side-by-side, bulk accept, undo) are carried as hypotheses in section 4.4, labelled model-prior, never as cited findings.
With Andrew's word, a cited external pass can be appended as section 4.3b.

### 4.4 Question 4 -- recommendations, ranked by user value against cost

Tags: **TODAY** works on today's YCharts intake; **FWD-16** needs Opal's own data (S31, S32); **VENDOR** needs a vendor
decision.

| # | Change | Serves | Page | Backend | Tag |
|---|---|---|---|---|---|
| R1 | Show the suggested security's NAME and the model's one-line reason beside "Did you mean". Keep the reason as text and do not show a numeric confidence until it is calibrated | O1 | small | `upload_suggestions.py` keeps `reason` and the provider's name for the verified symbol. Whether the provider row carries a name field was NOT checked | TODAY |
| R2 | Make the accept a single action: "Use AAPL" re-posts at once. Put "Accept all suggestions (n)" at the top of the card | O2, O4 | small | none; the re-post already takes 1-20 corrections (`prospect.ts:74`) | TODAY |
| R3 | Give `TICKER_CHECK_UNAVAILABLE` words ("the check could not run; nothing is wrong with your file; try again") and a RETRY action instead of REPLACE_FILE | O7 | none | one `CORRECTION_WORDS` entry, the actions change, and the locked copy test | TODAY |
| R4 | Give AMBIGUOUS rows a chooser listing the provider's own candidates | O6 | medium | the finding carries the candidates and the `SELECT_EXACT_IDENTITY` action the resolver already computes | TODAY |
| R5 | Turn the empty proxy box into a typeahead over the `etf-classifications` catalogue the page already loads (`TickerAutocompleteInput` pattern), showing each fund's name | O3 | medium | none | TODAY |
| R6 | Disclosure and copy distinguish "ticker corrected" (from an accepted check suggestion) from "stand-in" (a named proxy or swap) | O5 | small | the correction records its origin; the wire and disclosure belong to P (Part II) | TODAY |
| R7 | One row-centric list: remove the duplicate findings bullets for rows that have a control, and lead the summary line with "fix below" instead of "correct the file" | O1-O4 | small | none | TODAY |
| R8 | During the resolve, say what is happening ("checking 14 tickers; looking for likely typos") once, not twice | O1 | trivial | none (or a count in the RESOLVING answer) | TODAY |
| R9 | The `check` prompt returns a kind (`typo` / `successor` / `none`), and a successor is shown and disclosed as a stand-in, not as "Did you mean" | O1, O5 | small | prompt and schema in `resolution_kimi.py` | TODAY |
| R10 | Swap = ranked stand-ins of the same class and sub-class from `etf-classifications`, ETFs first, each verified; the model may rank or word, never invent (batch 218 (b) = S32) | O3 | medium (reuses the R5 control) | needs the gated fund's class from C-CLASSIFY, and S31 verification on Opal data | FWD-16 |
| R11 | Web-search swap (packet 2 as written) | O3 | -- | does not work on the pinned model (QA, 9 runs) | VENDOR -- not recommended |

**Order of value:** R2 and R3 give the most for the least (no new data, little code). R5 removes the worst stuck point
(the empty box) using data the page already has. R1, R6 and R9 make suggestions trustworthy. R10 is the "AI swap" Andrew
named, and it lands with FWD-16.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- R1 depends on whether YCharts' `securities_info` row carries a display name. If not, the name comes from C-MART or
  `etf-classifications`, and for a non-ETF security that is FWD-16 data.
- R6 depends on P's wire contract accepting an origin field on a correction, and on the disclosure renderer.
- R10 depends on C-CLASSIFY classifying the given (gated or unknown) security. Without its class, there is nothing to match
  on.
- Every page change needs portal `node_modules` and a 5174 build on the device that tests it.
- Any live Kimi call outside the feature's runtime authority (RULINGS.md:294), and every YCharts capture, needs Andrew's
  per-use word.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-07 08:12Z at workspace `30f94c3ab1` and portal `origin/DEV` `8ddfe409`.
- The check gate is served (Y-4 READY 2026-10-04 03:18:02Z). The user-named proxy is served (Y-5 READY 02:28:20Z).
- The swap is not live, and returns `KIMI_WEB_SEARCH_UNVERIFIED`. Packet 2 is HELD (batch 218); the CTO stop of 07:54Z
  was corrected to HELD by msg 104 (`STATUS~Y.md:72-74`).
- FWD-16 (S31, S32) is in the IRPT_YCDGEN PRD and is unmeasured.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **The page's text was rendered later** (Part IX, after msg 469). No 5174 build or `/ui-walk` was run, so pixels, layout and
  focus order are unverified.
- No external products were researched (section 4.3, egress).
- (Answered in Part VIII: `InputReview.tsx` is mounted, and the provider row carries a name.)
- The delisted/successor behaviour (5c, R9) is inferred from the prompt text and was not exercised.
- No costs are estimated beyond small/medium. No numbers are proposed for a confidence threshold.

---

## PART VIII -- FOLLOW-UPS (CTO~DELL2 msg 122, 08:15Z)

### 8.1 Does YCharts' `securities_info` row carry a display name? YES

- **Code:** the resolver refuses any row that lacks a string `security_name` (`security_resolution.py:44-49`,
  `_row_fields_complete`: `securitylist_security_id`, `security_name`, `detailed_security_type`, `features_needed`).
  Every FOUND candidate therefore carries a name and a type.
- **Recorded fixture:** `intake/tests/fixtures/lookup_capture/02_securities_info.json` (the CRO capture of 2026-09-23;
  no live call was made now). Rows: AAPL "Apple, Inc." (stock), VNQ "Vanguard Real Estate ETF" (etf), $:CASH "Cash" (cash).
- **Consequence for R1:** R1 needs no new data and is TODAY. The verified check in `upload_suggestions.py` already holds
  `check["candidates"][0]`, so it can keep `security_name` and `detailed_security_type` beside the symbol. The page then
  shows "Did you mean AAPL (Apple, Inc., stock)?". Part V's first bullet is answered: the dependency does not exist for a
  suggestion verified on YCharts. Under FWD-16 (S31), the name must come from Opal's data instead.

### 8.2 Is `InputReview.tsx` mounted on a reachable route? YES, a second correction surface

- **Mount chain at `origin/DEV` `8ddfe409`:** `tabs/TabShell.tsx:13,164` renders `AnalysisTab`, and
  `tabs/analysis/AnalysisTab.tsx:418` renders `<InputReview request={selectedRequest} ...>` whenever a request is
  selected (`:404`, `selectedRequest ? ...`).
- **What it shows:** every holding row with a free-text "Correct account grouping" box. Each `AnalysisRequest` finding
  gets its own free-text box, for example "Propose a substitution" for `UNRESOLVED_SECURITY` (`InputReview.tsx:32-43`).
  There are no suggestions, no verification and no catalogue.
- **Bearing on this brief:** an opened request offers a second, unassisted substitution path that is separate from the
  upload card's checked one. Two surfaces with two finding vocabularies (`reasonCode` versus the upload's `code`) can be
  expected to confuse a user.
- **Added recommendation R12 (TODAY, page only):** decide which surface owns substitution. Either route
  `UNRESOLVED_SECURITY` on an opened request back into the upload card's assisted path, or retire InputReview's
  substitution box. This is a product call for the PRD; this brief does not make it.
- **Not checked:** whether served requests reach that panel carrying `UNRESOLVED_SECURITY` findings. The panel's
  "Review required" line appears only when `request.findings` is non-empty. Reachability is measured from code, and the
  page was not rendered.

---

## PART IX -- THE CARD, RENDERED (2026-10-07 12:11Z, after msg 469 placed portal node_modules)

- **Instrument:** `ProspectComposer` was rendered server-side at portal `DEV` `8ddfe409` with the fixture adapter, using
  `bun --no-install`. The four findings were TICKER_NOT_FOUND with a suggestion (APPL), TICKER_DATA_NOT_ENTITLED (TIMXX),
  TICKER_AMBIGUOUS (BRK) and TICKER_CHECK_UNAVAILABLE (VTI), with the server's words where the server declares them. The page
  tests `upload-accept-suggestion` and `iv-e-153.upload-proxy` pass (5 pass, 0 fail).
- **Text as rendered, in order:**
  ```
  Review required: CURRENCY_CONFIRMATION_REQUIRED Correct the file or valuation options and review again, or name a proxy below ...
  Row 2: Our data provider does not recognize this ticker. Check it for a typo, or name a similar ticker ... (a proxy); ...
  Row 3: This holding is a real fund, but our data provider does not cover funds of this kind, ... Name a similar ticker ...
  TICKER_AMBIGUOUS, row 4
  TICKER_CHECK_UNAVAILABLE, row 5
  Name a proxy
  APPL (row 2) is analysed as [ ] Did you mean AAPL? [Use AAPL]
  TIMXX (row 3) is analysed as [ ]
  [Review with these proxies]
  ```
- **This confirms 4.2 steps 4, 5a, 5b, 5d and 5e as measured, not inferred.** BRK and VTI get a raw code and no control.
- **New, not in 4.2:** the summary line prints `result.reason` as a raw code ("Review required: CURRENCY_CONFIRMATION_REQUIRED"),
  because the fixture's top-level reason is a code. Whether served results carry a code or words there is not checked. Added
  to R7: the summary line needs words.
- **Still not checked:** layout, styling and focus order. This was text from static markup, not a browser screenshot.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/irpt-check-swap-ai-autosuggest-ux-brief-20261007.md
  PROJECT           IRPT_BCKEND (intake + page); IRPT_YCDGEN FWD-16 (S31, S32)
  EXISTING PRD      org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (FWD-16, C-RESOLVE, S31, S32)
  RULINGS           org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md :268 :270 :292 :294 :308 :318, batch 218 :6533
  SIBLING PROJECTS  MDPF_SECCLASS (etf-classifications), P lineage (wire/disclosure)
  PRIOR ART         intake/upload_suggestions.py, resolution_kimi.py, security_resolution.py, portfolio.py:318-330,444;
                    portal ProspectComposer.tsx, prospect.ts, comparisonCatalogue.ts, TradeSubmission/TickerAutocompleteInput.tsx;
                    Y5P2/KIMI_WEB_SEARCH_QA_FINDINGS_20261003.md
  MEASURED AT       2026-10-07T08:12Z, workspace 30f94c3ab1, portal origin/DEV 8ddfe409
```
