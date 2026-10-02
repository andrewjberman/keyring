# Brief 2 of 3 -- Investor Reporting ANALYSIS: what the 10 s proved, the three variants, the two gates, cases A-D

**Author:** `4.0.0_SA_CRO~X`, 2026-10-02. **For:** `1.0.0_SA_CTO`, to fold into the Analysis workstream
(`2.0.0_SA_COO~Y`; the page and the walker are `2.0.0_SA_COO~D`'s; grading `3.0.0_SA_CVO`).
**Source of the ask:** Andrew-direct 2026-10-02 ~14:5xZ, record
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANDREW_DIRECT_20261002_145xZ_IRPT_THREE_SURFACES_STATUS_AND_THREE_BRIEFS.md`
@fc46925968 (points A1-A6), addendum 1 @c56606d5ce (the test files) and addendum 2 @25c40b0035 (the typo file).
**Claim words:** `measured` = read this session; `held` = from a committed record, not re-run; `inferred` = from code,
not run; `absent` = searched, not found. No submission and no vendor call was made for this brief.

Andrew, verbatim (A1-A2): "Moving onto "Analysis", This function has to be proven end to end, which yesterday we were
able to do in 10s down from 27s, which is pretty good. I want to validate that we are able to do this reliably for each
case, i.e. variant 1 overview, variant 2, and variant 3."

## 1. What the 10 s measured (A1)

1.1 It is the time to OPEN A FINISHED report: "FROM THE PRESS TO THE SECTIONS ON SCREEN 26,710 ms -> 10,165 ms"
    (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/REAL_RUNS_20261001.md:257`, measured; commit
    2aed13d096). Walk 12, 2026-10-01 15:31-15:36Z: the signed-in walker on the DEV build opened
    `REQ-a69e5751d42c374f1d2354f9`, a Cottonwood Overview already READY. Variant 1 only.
1.2 The 16.5 s saved was browser queueing (the request read waited behind 17 status reads; portal item 62, 2bb367ef).
    Server time did not fall; the ~10 s left is server time (request read ~5.9 s, sections read ~4.0 s), item E6 at
    `2.0.0_SA_COO~Y` (held).
1.3 SUBMIT TO READY is 16.5-20 minutes, about 15 of them YCharts calculating (held): REQ-a69e Overview 16 min 42 s;
    REQ-a1d9 Multi-Comp 19 min 53 s; REQ-c07e Overview 16 min 29 s. The scripted "easy case" was a two-row file
    (`aapl-vnq-12.03.csv`). So "end to end in 10 s" holds for opening a report, not for producing one.

## 2. The three variants (A2)

Contract `AnalysisSubmissionRequest.schema.json:44-50,132-180`: variant 1 Overview = 0 comparisons; variant 2
Comparison = exactly 1; variant 3 Multi-Comp = 2 to 5 (held; mapping to Andrew's numbers inferred).

| Variant | Backend | Page | State |
|---|---|---|---|
| 1 Overview | READY twice (a69e, c07e) | walked | LIVE (CTO batch 88) |
| 2 Comparison | certified once on older code (09-29); never on the served code | not walked | NOT PROVEN |
| 3 Multi-Comp | READY once (a1d9), 20 match / 0 mismatch | 100 sections shown, model names absent | waits on E7 serving |

2.1 **An upload is forced to Overview** on DEV and PROD: "Comparison keys are not yet available for an uploaded
    portfolio -- this report generates as Overview." (`portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx:326`
    on origin/PROD, measured). Only `2.0.0_SA_COO~Y`'s scripted service-principal runner can send comparisons with an upload.
2.2 **ULT** (`opal_ultra_long_term`) is on the submission allow-list
    (`infra/aws/lambda/investor-reporting/_scope/maintained_sources.py:589`, measured) but has never run in a report
    (`live_proven` false, held).
2.3 **IWM** is offered by the page's composer (an etf-classifications name row) but refused at submission: the submit
    path checks keys only against the packaged four-model catalogue and raises "comparison key unknown or ambiguous"
    (`maintained_sources.py:555-560`, measured). No ticker has ever run as a comparison.

## 3. The two gates (A5)

3.1 **Built, not wired.** `infra/aws/lambda/investor-reporting/intake/resolution_kimi.py` holds the check gate (is this a
    typo, suggest a ticker) and the swap gate (propose up to 3 similar ETFs, user approves);
    `intake/security_resolution.py:169` `verified_suggestions` keeps only suggestions YCharts confirms. Nothing installed
    imports either (measured: `git grep`; the only other mention is a docstring). The page has no suggestion or swap UI.
3.2 **What runs instead:** one batched YCharts `securities_info` check per upload. Any symbol not FOUND gets
    `TICKER_NOT_FOUND` / `TICKER_AMBIGUOUS` / `TICKER_CHECK_UNAVAILABLE`, action `REPLACE_FILE`, upload state
    `NEEDS_CORRECTION`. A typo and a real untracked asset get the SAME code; the page shows "Review required ... Correct
    the file ... and review again" with raw codes. The user's only move is to fix the file and upload again (inferred
    from code).
3.3 **Vendor note (corrected 17:3xZ).** Both gates call Kimi (Moonshot); the swap gate's web search refuses until it is
    pinned (`KIMI_WEB_SEARCH_UNVERIFIED`). Kimi needs NO further word: it is whitelisted as VEW-3, "Yes Kimi can be called
    freely", any scope (`org/ref/VENDOR_EGRESS_WHITELIST.yaml`, since 2026-10-02T13:1xZ). The first version of this
    paragraph said wiring needed Andrew's word; that was wrong and is struck.

## 4. The test files and what each case does today (A3, A4; addenda 1-2)

All three files are accepted as uploads (XLSX, A1 `Symbol`, B1 `Dollars`, `$:CASH` kept as cash), read through the
served `template_reader.read_template` locally, nothing submitted (held from this seat's research fork).

| Case | File (laptop `Downloads`, sha256 prefix) | Variant | Today |
|---|---|---|---|
| A | Bridgeman easy, 99 rows (`500837992a3b9caa`) | 1 | RUNNABLE from the page |
| B | same | 2 vs ULT | BLOCKED on the page (2.1); scripted runner only; ULT never run |
| C | same | 3 vs ULT + IWM | BLOCKED: IWM refused at submission (2.3) and uploads forced to Overview |
| D | Stevens, 20 rows (`f0d344fa967504bd`) | 1 | runs to `NEEDS_CORRECTION`: rows 14-17 (QKZAQ, QBNYQ, QUSBQ, QBOKQ) `TICKER_NOT_FOUND`; no proxy offered; `$:CASH` x4 merged (notice) |
| Typo | easy with AAPL -> APPL (`87afdc7db1c58b38`) | 1 (proposed) | runs to `NEEDS_CORRECTION`: row 2 `TICKER_NOT_FOUND`; AAPL never offered |

4.1 **Highest risk, no evidence either way:** mutual funds and money-market funds (TIMXX; FBIFX, FDGFX, FHTKX, SPAXX).
    YCharts keys mutual funds as `M:<ticker>`. If `securities_info` answers with that form, `classify_batch`
    (`intake/security_resolution.py:56-65`) rejects the whole answer and EVERY row fails as `TICKER_CHECK_UNAVAILABLE`,
    not just those rows (inferred). Also watch HONA, SNDK, BRK.B.
4.2 **Case D's expected answer:** Alyssa proxied rows 14-17 with SGOV by hand (a cash stand-in). The swap gate as written
    asks for ETFs of similar exposure, so even wired it may not propose SGOV; the expected proxy should be stated in the
    case before the run.

## 5. The harness (A6)

5.1 `/ui-walk` cannot submit: it aborts every POST but login/refresh/logout/resolve/selections and never clicks upload,
    generate or submit (`.claude/skills/ui-walk/SKILL.md:32`, measured). It does record per-hop browser timing and can
    open a listed request.
5.2 Backend correlation exists: Lambda log groups `/aws/lambda/irpt-ycharts-generate` (upload, submit, catalogue) and
    `/aws/lambda/irpt-status` (status, history, sections); the YCharts job log on instance `i-0167fd745ad906a66` over SSM;
    join on `REQ-...` and `UP-...` ids (held).
5.3 Missing: a walker mode that may upload and submit ONE named case under a packet, capturing the page's network
    requests (Playwright) and joining them to the backend lines by id.
5.4 Run hazards (held, STATUS~Y): one job at a time (an upload during another generation retries up to 60 min); the
    history list (row S270) is past its timeout and grows ~0.5 s per request; anyone signing in to YCharts in a browser
    during the test logs out the server session (row S233).

## 6. Outcomes for the fold-in (each is something a person can do)

- **Y-1 (Case A)** A signed-in user uploads the easy file on the Analysis tab, generates an Overview, and opens the READY
  report; the record shows each hop's page timing joined to its backend log lines.
- **Y-2 (Case B)** The same user uploads the easy file, picks Opal Ultra Long-Term, and gets a READY Comparison report.
- **Y-3 (Case C)** The same user uploads the easy file, picks Opal Ultra Long-Term and IWM, and gets a READY Multi-Comp
  report. (Needs a ticker admitted as a comparison; if tickers are out of scope, Andrew says so and C uses two models.)
- **Y-4 (typo)** The user uploads the typo file; the page names row 2 `APPL` as a likely typo and offers `AAPL`;
  accepting continues without a new upload.
- **Y-5 (Case D)** The user uploads Stevens; the page names rows 14-17 as real but not tracked by YCharts and offers a
  proxy for each; the user approves one (Alyssa's choice: SGOV) and gets a READY Overview.
- **Y-6 (reliability)** Each case passes twice in a row, run one at a time by a service agent that walks the page and
  captures backend network operations; submit-to-READY and open-to-sections times are recorded per run.
- **Order:** Y-1 and the two NEEDS_CORRECTION baselines (typo, D) can run on today's code; Y-2/Y-3 need 2.1 and 2.3
  closed; Y-4/Y-5 need section 3 wired.
- **Vendor calls:** every run calls YCharts. This brief reads Andrew's 14:5xZ "I want to be able to test sample
  submissions" as his word for these submissions, one at a time; the CTO confirms or asks.

## 7. What this brief does not claim

- No YCharts answer was read for any symbol in the three files; 4.1 is a code-path risk, not an observation.
- Page timings are from the DEV build; the deployed site was not timed.
- Whether the YCharts server's deployed symbol-check code equals CLOUD was not read.
- No record of a run "last night" other than walk 12 and the three requests above was found (absent).
