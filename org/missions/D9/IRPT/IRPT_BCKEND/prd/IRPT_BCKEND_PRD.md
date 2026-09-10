# IRPT_BCKEND -- Investor Reporting backend: ingestion, multi-tenant scoping, provider normalization, generation and execution

```json
{
 "project": "IRPT_BCKEND",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/investor-reporting-ir-bk-brief-20260910.md@2acf23d8fd",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11"],
 "status": "RATIFIED"
}
```

Brief: `docs/briefs/investor-reporting-ir-bk-brief-20260910.md` @`2acf23d8fd`, 57,608 bytes, 28 sections + 9 mapped sources. Counterpart: `IRPT_FNTEND` (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`). Endpoint of record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md`. Two projects, two decompositions, two task-order sets, two adjudications; no cell is jointly owned. This project OWNS the grade on FWD-2, FWD-7, FWD-9, FWD-10 and CONTRIBUTES the data, parity, entitlement and execution half to FWD-1, 3, 4, 5, 8, 11, which the counterpart owns and whose grades read both halves.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An advisor finds an authorized client and opens its relationship and accounts without waiting for a vendor report
         DONE WHEN  EXERCISED -- an advisor who has never used the workspace has searched, selected, and been shown the relationship and its permitted accounts
         ACCEPT     from the header, a search by client name returns an unambiguous selection; the workspace immediately shows the relationship, its permitted underlying accounts, cached context and the directory's as-of; the choice survives a tab switch; an unmapped client stays VISIBLE to an authorized viewer with an explicit capability gap rather than silently missing
         PROOF      a fixture directory carrying duplicate names, an account-only entry and multiple relationships, compared against the expected authorized set; cold and warm timings recorded against the whole captured firm-directory denominator; VENDOR REQUEST COUNT DURING SEARCH IS ZERO. No latency target is invented at L2
         OWNER      IRPT_FNTEND.  THIS PROJECT: the directory keyed to the signed-in firm and advisor; resolution of a selection to the exact permitted account set BEFORE any report is fetched; the directory as-of; zero provider calls per keystroke
         CONSTRAINT terminated clients STAY VISIBLE, marked terminated, access governed by entitlement; disappearance from search is never revocation
         PIN        58266dab2d

  FWD-2  A restricted advisor can use every tab and export ONLY within their permitted client population
         DONE WHEN  EXERCISED -- an unauthorized request has been replayed and revealed nothing
         ACCEPT     firm and advisor rights govern suggestions, selected-account membership, report retrieval, job polling, cached results AND PDF download; a relationship containing an account outside the viewer's permitted population NEVER silently grants that account or its value; a firm-authorized viewer gets the firm's population under the same rules
         PROOF      replay authorized and unauthorized requests with SWAPPED firm, advisor, account, relationship, report and PDF identifiers, INCLUDING A REVOKED GRANT AGAINST A WARM CACHE; the negative requests reveal no protected data
         OWNER      IRPT_BCKEND.  CROSSES: IRPT_FNTEND handles the refusal -- no protected stale display, honest permission states, negative fixtures
         CONSTRAINT highest blast radius in the set: a defect is a CROSS-FIRM EXPOSURE; the estate's cross-firm rule is substrate-shaped, both shapes live (bucket-scoped Deny; key-prefix + IAM condition); graded on its own, never as a side effect of FWD-1. The same rule binds at ingestion (FWD-10) and is GRANTED to the Opal-user class (FWD-11)
         PIN        58266dab2d

  FWD-3  An advisor reads the provider's performance result in an Opal report and exports the same result
         DONE WHEN  EXERCISED -- a captured provider response has been carried to a rendered view and a PDF at one report revision, for each supported partner and scope
         ACCEPT     for the selected account or relationship and period, vendor-calculated performance appears in a common Opal layout and the PDF carries the SAME scope, returned dates, values, method basis, source attribution and approved disclosures; the UI distinguishes TWR/MWR, net/gross, cumulative/annualized, UNITS and UNAVAILABLE fields; a deliberately incomplete provider mapping yields a PARTIAL or UNSUPPORTED result rather than a full-client claim
         PROOF      compare captured request/response, normalized report, rendered view and PDF at one revision per partner and scope; relationship return uses a VENDOR CALCULATION for the exact selected account set -- summing or averaging account returns is not a substitute and a fabricated aggregate fails this outcome
         OWNER      IRPT_FNTEND.  THIS PROJECT: canonical meaning, UNITS, dates, the vendor-calculation-only rule, the normalized PerformanceReport; the PDF runs in this project's worker
         CONSTRAINT UNITS ARE PART OF A NUMBER'S MEANING: Orion summary `calculated-performance.performance` is DECIMAL, daily breakdown `performance` is PERCENTAGE, daily `factor` links as product minus one; a normalizer treating both as one unit is wrong by 100x and renders correctly. A normalizer does not change a provider's methodology to make two numbers look comparable
         PIN        58266dab2d

  FWD-4  An advisor obtains a YCharts sensitivity analysis in the same client context and exports it
         DONE WHEN  EXERCISED -- an approved report variant has been replayed from an analyst-approved input through its captured request/job/result chain to the tab and the PDF
         ACCEPT     the advisor selects a supported variant, reviews the holdings or saved-portfolio mapping and comparison model it will use, and receives an Opal-branded analysis and matching PDF preserving the input snapshot, configuration, data dates, limitations and vendor attribution; a MODELED comparison is described as modeled; unsupported variants are VISIBLE as unsupported
         PROOF      replay each approved variant end to end
         OWNER      IRPT_FNTEND.  THIS PROJECT: the chain from validated input through captured request, job and result to a certified section; the release state behind "unsupported VISIBLE as unsupported"
         CONSTRAINT the request arrives by EMAIL (the intake is FWD-9); UNSUPPORTED POSITIONS ARE NOT SILENTLY REMOVED to obtain a successful report; clear inputs proceed PROGRAMMATICALLY, review is the exception path; NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; native section/export parity needs ACTUAL three-variant PDFs and the upload multipart body, both still missing (also on FWD-8); the runner is the BDAPI-with-Kimi browser-runner STYLE with NO OTP BRANCH -- fixed, not a build choice
         PIN        58266dab2d

  FWD-5  An advisor sees current holdings organized by models, with the underlying securities and unassigned assets preserved
         DONE WHEN  EXERCISED -- dated holdings and model snapshots have been replayed for all three registry client firms
         ACCEPT     the view starts at the model breakdown and drills into accounts and securities; ACTUAL CUSTODY HOLDINGS REMAIN THE TOTAL-VALUE BASIS; SmartX (49F), Eclipse (INF) or BD Rebalancer (COT) supplies the overlay; target weights, actual sleeve values and inferred estimates are DISTINCT; missing attribution stays VISIBLE without double-counting or redistributing the residual
         PROOF      replay across all three firms including an unassigned account, an unmatched join, a blended model and a multi-relationship membership; UNIQUE UNDERLYING HOLDINGS RECONCILE BEFORE AND AFTER THE OVERLAY; coverage and join exceptions carry DENOMINATORS
         OWNER      IRPT_FNTEND.  THIS PROJECT: join correctness, the reconcile-before-and-after control, the denominators, the revision-bound HoldingsSnapshot
         CONSTRAINT MODEL TARGETS MUST NOT MASQUERADE AS OBSERVED HOLDINGS; a residual silently redistributed into sleeves fails this outcome even when every total ties; no model's global AUM is a client's holding
         PIN        58266dab2d

  FWD-7  The client directory cannot go quietly stale, and its ceiling belongs to the system rather than to the advisor's diligence
         DONE WHEN  EXERCISED -- a DRIVEN exercise on a CONTROLLED CLOCK against source fixtures, covering the FAILURE arms, with NO REAL-CALENDAR WAIT anywhere in it
         ACCEPT     a client added, or whose eligibility changes, in the source becomes visible or ceases to be offered within the declared refresh window WITHOUT anyone asking for a refresh; a MISSED TRIGGER and a FAILED REFRESH each read DIFFERENTLY from a completed one; a request served from an OVER-AGE directory hits the declared expiry/fallback behavior rather than being answered silently; the oldest directory an advisor can be served is set by the SCHEDULE, not by whether they noticed the as-of
         PROOF      controlled-clock / source-fixture exercise driving ALL FIVE arms: an added client, a changed eligibility, a MISSED trigger, a FAILED refresh, and an OVER-AGE directory request
         OWNER      IRPT_BCKEND.  CROSSES: IRPT_FNTEND shows the as-of and the capability gap
         CONSTRAINT directory freshness and eligibility only; revocation is FWD-2's, independently; terminated clients stay visible under entitlement
         PIN        58266dab2d

  FWD-8  An advisor exports a BRANDED Opal report whose narrative page states what was happening in the market at the account's dramatic moves -- as CONTEMPORANEOUS CONTEXT, never as a cause of the return
         DONE WHEN  EXERCISED -- a KNOWN drawdown window has been replayed against the dated topic history and the same inputs selected the SAME inflection points twice
         ACCEPT     the dashboard stays the DEFAULT view and the export is a separate act; the export renders the Opal template from the deck-generation brand guidelines at the SAME performance revision the advisor reviewed, with advisor logo and information as an OPTIONAL input; the narrative page shows the performance time series and, at the max drawdown and other dramatic moves, the Trending Topic and Topic Cloud terms DATED TO THAT WINDOW, with the other sentiment signals as supporting context; inflection-point selection is DETERMINISTIC -- the same series and the same history select the same moments, every run
         PROOF      replay one known drawdown window twice and diff the selected moments; replay a window that PREDATES the news history and confirm it renders MISSING HISTORY rather than an empty topic list
         OWNER      IRPT_FNTEND.  THIS PROJECT: the lambda -- deterministic inflection selection, dated evidence and prose validity, the frozen ExportBundle, execution of the counterpart's RenderPackage, the ExportReceipt; the topic/sentiment retrieval is a new seam whose owner is named at L5
         CONSTRAINT the causal line is IN THE ACCEPT: the artifact must SAY it is contemporaneous context and must not assert, imply or rank causes; MISSING HISTORY IS AN ANSWER, NOT AN EMPTY STATE; NOT A BI SURFACE -- a bounded read of dated signals for the selected account's own periods; the high-definition advisor logos are PENDING INPUT, neither invented nor scraped
         PIN        58266dab2d

  FWD-9  A forwarded holdings email becomes a durable, correctly scoped analysis request without anyone re-keying it
         DONE WHEN  EXERCISED -- a real forwarded message with its attachment has become a request an advisor can see and correct
         ACCEPT     an advisor forwards a client's holdings by email during the working day and, within a short time, sees it in Opal as a request with the holdings read out of the attachment, attributed to the right advisor and client, and with anything the system could not read flagged for correction rather than guessed; forwarding the same email twice does not create two requests, and a genuinely new request that happens to carry the same holdings is not thrown away as a duplicate
         PROOF      representative forwarded messages with real attachments, retries, a restart while an attachment is being saved, checkpoint recovery, a repeated forward, a new request with identical holdings, an unresolved owner, ambiguous positions
         OWNER      IRPT_BCKEND.  CROSSES: IRPT_FNTEND consumes the correction state
         CONSTRAINT the request's FIRM is fixed by the sender's domain the moment the message arrives and cannot change after; it bounds which advisors and clients the attribution may resolve to (which advisor within the firm, and which client, are resolved by the cells below, not by the domain); the 15-minute poll 08:00-23:45 America/New_York is the brief's proposal, measured then declared, not ratified here; its proof is DRIVEN
         PIN        2dcd88091f

  FWD-10 A request can only ever land in its own firm's storage, because its firm is fixed from the sender's email the moment it is ingested -- so corrupting another firm's result is IMPOSSIBLE BY CONSTRUCTION
         DONE WHEN  EXERCISED -- a request has been ingested, bound to its firm from the sender's domain, and every failure mode driven with no effect on a second firm
         ACCEPT     the moment a request arrives, the firm it belongs to is decided from the sender's email address and cannot be changed later; that request, and everything produced from it, can only be stored in that firm's own locations, which are written down as a fixed list before the first request ever arrives; when something goes wrong for one firm, the person running the system can see what failed and fix it, and no other firm's results can have been touched, because there is no path by which they could be; a failed run never publishes a report that looks complete but is not, never overwrites a newer result with an older one, and never brings back a permission that was taken away
         PROOF      ingest a request from each firm's domain and confirm it lands only in that firm's enumerated locations; attempt to write a bound request into a second firm's location and confirm refusal; then the failure arms -- a failed source partition, a stale model map, a duplicated event, an expired lease, a queue replay, a worker restart, a revocation during a job -- each shown to touch no second firm; a manifest names every upstream dependency and its owner
         OWNER      IRPT_BCKEND.  CROSSES: IRPT_FNTEND surfaces partial, stale and unavailable states through the StatusEnvelope
         CONSTRAINT the enumerated-locations list (FirmDestinationPolicy) is a maintained artifact with a named OWNER -- a new firm name is a GATE EDIT; the recovery arms are the PROOF of impossibility, not the outcome; FWD-2 grades who may SEE, this grades where a request may LAND and what a failure may not touch
         PIN        2dcd88091f

  FWD-11 An Opal user can run reports and analysis on ALL firms from one Global view, the way Model Portfolios already does it
         DONE WHEN  EXERCISED -- an Opal user has opened the global view, picked a client at a second firm, and run a report and an export
         ACCEPT     someone at Opal, signed in as Opal rather than as any firm, can pick any client from any firm and use every tab and export on them; a firm's advisor can never reach that view or see a second firm through it; the global view shows the same numbers that firm's own advisor would see for that client, never a recomputed or blended one; which firm each result belongs to is always visible
         PROOF      an Opal user opens the global view, selects clients at two different firms, runs a report and an export on each; replay the same requests as a firm advisor and confirm refusal; compare the global-view figures to the firm-scoped figures for the same client and revision
         OWNER      IRPT_FNTEND.  THIS PROJECT: the cross-firm entitlement CLASS (the same rule as FWD-2 and FWD-10, GRANTED to an Opal principal), the permitted-firm catalogue in ResolvedScope, and the multitenant `api/scoped/` routes
         CONSTRAINT the multitenant `api/scoped/` layout is the pattern -- fixed, not a build choice; Global never rebinds an email request's firm and never mixes firm data or destinations in one report; no new all-firm financial aggregate is authorized
         PIN        2dcd88091f
```

## CELL CANDIDATES

One row per candidate cell. The decomposition at L5 is the COO lane's and may split, merge or re-sequence these; every brief section a row consumes is cited by heading so the coverage map below can be checked against it.

| cell | serves | brief sections consumed | contracts (P=produces, C=consumes) | paths: reuse | paths: new home | fixtures / evidence | acceptance clause draft |
|---|---|---|---|---|---|---|---|
| B1 directory ingestion + viewer-scoped projection + search service | FWD-1 (contrib), FWD-7 (own) | O1; IV.2 identity table, daily-movement paragraph, business-date paragraph | P `DirectoryEntry` | `data/assets/scripts/silver/silver_registry.py`, `mirror_schemas.py`, `rebalancer_schemas.py`, `bd49f_dim_conversion.py`; `runners_49f/a01_dim_relationship.py`, `a06_dim_identity_crosswalk.py`, `d08_firm_ownership_map.py`, `bd49f_dim_portfolio_group.py`; `runners_inf/a00_dim_account.py`, `a01_dim_relationship.py`, `runner_common.py`; `runners_cot/a01_dim_relationship.py`; `data/firm_registry.json`; `lib/trading_calendar.py` | `data/assets/scripts/gold/investor_reporting/` (directory runner); publisher output in `opal-data-portal-v2` | split evidence manifest; 49F crosswalk `match_method`/`match_as_of`/`in_0833_universe`; INF 874-of-953 identity fixture | duplicate names, account-only entry, multiple relationships, terminated-but-entitled client resolve to the expected authorized set; provider calls during search = 0; as-of and source completion date carried on every entry |
| B2 identity resolution + permitted account set (`ResolvedScope`) | FWD-1 (contrib), FWD-2 (own), FWD-11 (contrib) | O1; O8; IV.2 auth-validator paragraph, Global/scoped integration sources | P `ResolvedScope` | `infra/aws/lambda-edge/auth-validator-edge/index.mjs`; partner `roles.ts` x3 (vocabulary only, never grants) | `infra/aws/lambda/investor-reporting/` (scope resolver) | 49F 201-group overlap fixture (no double-count, no manufactured primary credit); INF 79-unmapped-accounts reason list | a partly permitted relationship resolves to the exact allowed subset or an explicit unsupported scope, never the whole with rows hidden after; fingerprint identical on every downstream call |
| B3 authorization enforcement on every route, warm-cache revocation | FWD-2 (own) | O1 enforcement paragraph; II.3 cache/idempotency-key paragraph | C `ResolvedScope`; keys per II.3 | `infra/aws/terraform/partners-api/api-gateway.tf` (CUSTOM authorizer pattern) | `infra/aws/terraform/investor-reporting/` | negative integration fixtures (swapped firm/advisor/account/relationship/report/PDF ids; revoked grant vs warm cache) | every negative request reveals no protected data; a cached result or artifact is reauthorized before serving; client names are never cache keys |
| B4 directory refresh schedule, expiry/fallback, controlled-clock harness | FWD-7 (own) | O1 refresh; O7 clocks/manifests; IV.2 business-date paragraph | P `DirectoryEntry.revision`; P `StatusEnvelope` (stale) | `lib/trading_calendar.py`; each source's completion manifest | `infra/aws/terraform/investor-reporting/` (scheduler) | source fixtures for the five arms | all five arms driven on a controlled clock: added client, changed eligibility, MISSED trigger, FAILED refresh, OVER-AGE request -- each reads differently; no real-calendar wait |
| B5 `FirmDestinationPolicy`: sender/domain-to-firm mapping, enumerated destinations, quarantine, immutable binding | FWD-10 (own), FWD-9 (own, the binding), FWD-2 | O7; IV.2 sender gate paragraph + verify-original-sender paragraph; IV.4 records paragraph | P `AnalysisRequest.ingestion-gate/destination-policy revision` | `data/firm_registry.json` | policy document under `infra/aws/terraform/investor-reporting/`; proposed prefixes `firms/49financial/`, `firms/inflection/`, `firms/cottonwood/` in the proposed `opal-data-ycharts` bucket; a separately enumerated quarantine location; per-firm role/prefix permissions | -- | a request from each firm's domain lands only in that firm's enumerated locations; a write to a second firm's location is refused; unknown, spoofed or contradictory origin never becomes a firm request; an Opal-origin mail with no target-firm rule stays unresolved; the policy has a named OWNER and a version; a new firm is a policy edit |
| B6 mailbox intake: Graph delta, attachments, checkpoint, lease, outbox, idempotency | FWD-9 (own) | O3; IV.4 mailbox paragraph | P `AnalysisRequest` (original-message/attachment refs, sender evidence) | `infra/aws/lambda/ycharts-session-capture/index.mjs` (Graph/cert pattern reference) | `infra/aws/lambda/investor-reporting/` (intake handler); scheduler `cron(0/15 8-23 * * ? *)` America/New_York -- the brief's proposal, measured then declared | real forwarded-message/holdings specimens (STILL MISSING -- proof gap); mailbox `requests@opalinvest.com` forwarding into `opalbloomberg@opalinvest.com` | attachment + receipt persisted BEFORE the checkpoint advances; restart mid-attachment recovers; repeated forward = one request; new request with identical holdings = a new request; Retry-After and delta resync defined; original sender verified through the forwarding arrangement, not display From |
| B7 holdings parse + validate + correction state | FWD-9 (own), FWD-4 (contrib) | O3 parse paragraph; IV.4 parse paragraph | P `AnalysisRequest.normalized holdings / findings / corrections`; P `StatusEnvelope.needs-correction` | -- | `infra/aws/lambda/investor-reporting/` (parser) | supported CSV/XLSX specimens; `$:CASH`; share-class mapping cases | deterministic parse keeps units, source cells, totals, grouping and cash; unmatched holdings are never discarded or silently substituted; approved substitutions captured explicitly; uncertain items enter the correction state; `management_fee=0.003` is the recorded current setting |
| B8 YCharts session library + browser runner | FWD-4 (contrib) | O4 session paragraph; IV.4 session pattern and paths, Secrets paragraph | -- | `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js`, `run-bd-auto-login.sh`, `package.json`; `infra/aws/terraform/bd-49f-auto-login/{iam,instance,main}.tf`; `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py`; Secrets `ycharts/login/credentials` (existing), `ycharts/session/current` (proposed), `astn/kimi/api-key` | separate YCharts host/role (never the BD host) under `infra/aws/terraform/investor-reporting/` | six transcripts + manifest + three HARs (private packet, offline profile `docs/research/investor_reporting_ycharts_20260910/profile_handoff.py`) | BDAPI-with-Kimi runner style adapted: `getSession`/`probeSession`/`acquireSession`/`persistSession`/`withAuthenticatedPage` with lease/fencing; success predicate is identity/cookie/authenticated-probe, NO OTP branch; an unexpected challenge is an explicit failure; bounded reacquisition after eviction; no credential in any artifact |
| B9 YCharts generation chain | FWD-4 (contrib) | O4; IV.4 captured retrieval recipe steps 1-7 | P `AnalysisReport` (attempt, vendor artifact hash) | endpoints per recipe: `/search/suggest/report_securities`, `/securities/securities_info`, `/model_portfolios/fixed/holdings_upload/client`, `/model_portfolios/fixed/`, `/model_portfolios/{id}/status`, `/custom_pdf_reports/generate/collection`, `/generate/{template_id}`, `/validate_report_securities/{template_id}`, `/custom_pdf_reports/{template_id}`; templates 14141822 / 14141824 / 14141847 (captured configuration, not constants) | `infra/aws/lambda/investor-reporting/` (generation job) | HAR evidence; comparison field census; 34-key vs 33-key body shapes | upload uses the observed browser upload (multipart names NOT captured -- do not invent); opaque deterministic portfolio name, checkpoint intent before submit, reconcile uncertain creates by owned identity, never adopt the newest row; SUBMITTING persisted before the side effect; short-lived URL downloaded immediately over TLS, signed params never logged; PDF content and hash verified; owned encrypted artifact retained |
| B10 section extraction + certification against paired PDFs | FWD-4 (contrib), FWD-3 (contrib, parity) | O4 certification paragraph; IV.4 records paragraph; IV.1 S8 | P `AnalysisReport.typed sections with units/dates/source coordinates` | -- | `infra/aws/lambda/investor-reporting/` (extractor) | ACTUAL three-variant PDFs (STILL MISSING -- proof gap, named on FWD-4 and FWD-8) | text/table extraction certified with units, dates, page/coordinates; charts need reliable underlying data or an identified source-chart representation; no number inferred from a visual guess |
| B11 performance adapters: Black Diamond (49F, COT separately), Orion (INF); normalizer | FWD-3 (contrib) | O2; IV.3 | P `PerformanceReport` | BD `POST /portfolioreporting/api/performance/performancePeriod` + `performanceSeries`; Orion `POST /api/v1/Reporting/Scope`; `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py` (bounded helpers); `inf-performance-daily/pull_inflection_performance_dim.py` (prior art only) | `infra/aws/lambda/investor-reporting/` (adapters) | `docs/research/investor_reporting_performance_20260910/probe_performance.py` (offline); BD/Orion teardowns; nine-outcome September 10 evidence | native date/cumulative arrays preserved; one hierarchy chosen, overlapping levels never summed; period `timeWeightedReturns.return` decimal; Orion units per FWD-3 constraint; nodes identified by group path + `$type` + calculation id together; `startValue + valueChange` is NOT a dollar-history shortcut; compact `cumulative=false` shape; missing facts stay absent with reasons |
| B12 partner holdings joins (SmartX/49F, Eclipse/INF, BD Rebalancer/COT), taxonomy, denominators, `HoldingsSnapshot` | FWD-5 (contrib) | O5; IV.5 both tables and the four paragraphs after | P `HoldingsSnapshot` | `runners_49f/b04_account_model_membership.py`; `opal-assets-silver-smartx/smartx_conversion.py`; `INF_E_00.eclipse_model_portfolios.py`; `build_dim_model_portfolio.py`; `build_cottonwood_mdpf_pair.py`; `mdpf_category_registry.py`; D1 / D3 PRDs as prior art | `data/assets/scripts/gold/investor_reporting/` (holdings publisher) | 23 Parquet objects, 15,753,977 bytes (source-list.json, model-overlay evidence, `profile_snapshot.py`) | 49F universe 08335338 only, eight-to-ten-digit zero-pad join, 7,431 joined of 7,453; INF 658 of 663 assignments, 13 multi-account full portfolios not repeated per account; COT `external_id`-to-AccountID join, 946 of 950, custody x recursive weights is TARGET attribution; unique custody population is the denominator; observed / assigned / target bases never spliced; unknown classification is an explicit state, not Client; unique holdings reconcile before and after overlay |
| B13 event detection + dated news/topic retrieval + prose validation (`NarrativePacket`) | FWD-8 (contrib) | O6 narrative paragraph; IV.6 event paragraph, history paragraph, prose paragraph | P `NarrativePacket` | `infra/aws/lambda/news_layer3_curation/lambda_function.py`, `news_trending_analysis/lambda_function.py`, `keyword_drilldown_generator/lambda_function.py`; DynamoDB `opal-news-trending-daily`, `opal-news-articles`; `s3://opal-data-news-v2/trending_reports/YYYY/MM/DD/trending_report_HHMMSS.json` | `infra/aws/lambda/investor-reporting/` (narrative adapter -- the new seam named at L5) | export/narrative evidence | events on verified daily cumulative TWR (growth, running peak, drawdown, peak/trough/recovery), overlapping episodes merged, declared materiality policy; same series + same history select the same moments twice; publication/cutoff timezone verified; a window predating the history renders MISSING HISTORY; prose cites selected evidence ids only, states contemporaneity, never causation; news text is data, not instruction |
| B14 asset ingestion, `ExportBundle` freeze, render worker executing the counterpart's `RenderPackage`, `ExportReceipt`, protected download | FWD-8 (contrib), FWD-3 (contrib) | O6 export paragraph; IV.6 logo/bundle paragraph and execution paragraph | C `RenderPackage`; P `ExportBundle`, `ExportReceipt` | brand sources `deck_generation/brand/opal_brand_guidelines.pdf`, `brand_spec/brand.json`, `engine/brand.py`, official logo SVG | `infra/aws/lambda/investor-reporting/` (export job + browser runtime); protected artifact storage | `docs/research/investor_reporting_export_20260910/{profile_export_capture.py,build_export_review.py,performance-export-review.pdf,FONT_LICENSE.txt}` | bundle pins scope, report, asset, renderer/template/disclosure and narrative policy versions; retry reuses the bundle, no vendor call during render; branding change = new export revision without recalculation; logos verified for binding, type, dimensions, checksum, safe SVG, resolved before render, no arbitrary URL fetch; download reauthorized even when the artifact exists |
| B15 Global entitlement class + `api/scoped/investor-reporting/...` routes + permitted-firm catalogue | FWD-11 (contrib), FWD-2 (own) | O8; IV.2 Global/scoped integration sources | P `ResolvedScope.principal class / permitted-firm catalogue` | `infra/aws/terraform/partners-api/api-gateway.tf` (`/api/scoped/advisor-intelligence/` CUSTOM auth); `infra/aws/lambda-edge/auth-validator-edge/index.mjs`; `portal/src/pages/ModelPortfolios.tsx` (pattern reference only) | `/api/scoped/investor-reporting/...` routes under `infra/aws/terraform/investor-reporting/` | -- | an Opal principal reaches clients at two firms through scoped routes; a firm advisor replaying the same requests is refused; same client + revision gives identical values Global vs firm-scoped; revoking Global permission takes effect; the actual authorizer, handler and storage enforcement are traced before implementation -- the MP demo-to-global translation and missing-claim fallback are NOT copied |
| B16 operations: `StatusEnvelope`, manifests, clocks, leases, retries, traces, per-tenant recovery | FWD-10 (own, the proof arms), FWD-6 (contrib), FWD-7 | O7 operations paragraph; IV.2 BRONZE-SILVER-GOLD-PLATINUM paragraph; IV.7 path-manifest requirement | P `StatusEnvelope` | -- | `infra/aws/lambda/investor-reporting/`; `infra/aws/terraform/investor-reporting/` (queues, leases, DynamoDB keys, outbox) | -- | failed source partition, stale model map, duplicated event, expired lease, queue replay, worker restart, revocation mid-job -- each recovers one provider or tenant with unaffected functions available and NO second-firm effect; failed work cannot publish a false-complete snapshot, overwrite newer output or resurrect a permission; every published snapshot reconciles to its input lineage; a path manifest names each dependency and owner |
| B17 tenant-scoped storage and keys: DynamoDB tenant/request keys, immutable revisions, S3 evidence layout, cache/idempotency keys | FWD-10 (own), FWD-2 (own), FWD-9 | IV.4 records + DynamoDB paragraphs; II.3 keys paragraph | -- | -- | proposed `opal-data-ycharts` SSE-KMS bucket (absent at inspection) with `firms/{firm_id}/intake|requests|generations/...` under enumerated prefixes | -- | queues carry ids not attachments; S3 holds immutable evidence, never locks; keys include tenant, account-set fingerprint, source/schema/config revisions and operation parameters; once bound the firm is immutable |
| B18 infrastructure homes, IAM/KMS/secrets, release manifests | all | IV.7 proposed homes paragraph; V | -- | existing protected transport/publisher infrastructure where its contract fits | `infra/aws/lambda/investor-reporting/`, `infra/aws/terraform/investor-reporting/`, `data/assets/scripts/gold/investor_reporting/` | -- | every concrete read/write path and owner registered during implementation; no silent dependency on another page's Gold output; reusing a helper never widens its deployment or IAM role; `safe-apply` only; no `aws lambda update-function-code` |

## CONTRACTS

Source: brief II.3, eleven contracts, proposed canonical, versioned. BK owns identity, economic meaning, units, dates and wire compatibility; FE owns formatting, interaction and consumer fixtures. Server-only credential and vendor-routing fields never reach the browser. A change needs matching producer and consumer fixtures.

| contract | producer | consumer | cell | required meaning / fields (from II.3) |
|---|---|---|---|---|
| `DirectoryEntry` | BCKEND B1 | FNTEND | B1 | opaque firm/client/relationship/account ids; display name + masked discriminator; permitted scope/capabilities; termination indicator SEPARATE from access; directory/source revision |
| `ResolvedScope` | BCKEND B2/B15 | FNTEND | B2, B15 | viewer policy, principal class, entitlement revision; permitted-firm catalogue/selection for Global; verified request firm; unique permitted account set + fingerprint; requested vs resolved scope + partial reason; vendor ids server-side |
| `PerformanceReport` | BCKEND B11 | FNTEND | B11 | source/provider/tenant lineage; requested and actual dates; currency/method/fee/accrual/annualization; summary/period returns, daily cumulative series, account detail; optional benchmark/value facts only when supported |
| `AnalysisRequest` | BCKEND B5/B6/B7 | FNTEND | B5, B6, B7 | immutable tenant/request/revision + ingestion-gate/destination-policy revision; verified original-sender evidence; message/attachment refs; normalized holdings with source fields and units; variant + ordered comparisons; settings; findings/corrections; stage + release policy/state |
| `AnalysisReport` | BCKEND B9/B10 | FNTEND | B9, B10 | request/attempt + vendor artifact hash; effective inputs/settings; typed sections with units/dates/source coordinates; disclosures; extraction validation; released revision + protected PDF reference |
| `HoldingsSnapshot` | BCKEND B12 | FNTEND | B12 | scope + source-set revision; business/as-of clocks; unique custody totals; node hierarchy; namespaced model/security ids; observed/assigned/target basis; amount + denominator; parent/total percentages; provenance; coverage/remainders; drill refs |
| `NarrativePacket` | BCKEND B13 | FNTEND, B14 | B13 | performance revision; event policy/version; dated peak/trough/recovery/movement events; cited historical evidence with cutoffs; validated prose; coverage; generation/model/prompt versions |
| `ExportBundle` | BCKEND B14 | B14 render; FNTEND F8 (preview -- a preview never calls the vendor again) | B14 | immutable authorized report revisions + selected sections; narrative packet; approved asset hashes; template/renderer/disclosure versions; render options; no live vendor request during render |
| `ExportReceipt` | BCKEND B14 | FNTEND | B14 | export/bundle hash; artifact hash/location server-side; page/validation facts; created/released timestamps; job state; authorized download route; no vendor signed URL in FE |
| `StatusEnvelope` | BCKEND B16 | FNTEND | B16 | operation + revision; queued/running/ready/partial/stale/unavailable/needs-correction/uncertain/failed; source dates; safe retry/recovery actions; public reason code; internal correlation id |
| `RenderPackage` | FNTEND | BCKEND B14 | B14 (consumer) | supported contract/template versions; deterministic screen/print components; fonts/assets requirements; print entry point; visual fixtures -- BK packages and executes the compatible version |

Supervision and billing cohort semantics -- the original brief's independent supervision/billing concepts and their hierarchy, and Holdings' alternative Client partitions (Opal Supervised/Unsupervised as fee-taking status; Advised/Residual as advisory status; vendor AccountSupervised is NOT Opal fee-taking) -- ride two contracts and are carried explicitly here because no single row above names them: `DirectoryEntry` carries the cohort/capability facts for the selected scope; `HoldingsSnapshot` carries the classification partitions per node. Both only when authoritative; an unknown value is an explicit unknown state, never false and never Client. Produced by B1 and B12; consumed by F2 and F6. Source: BK brief II.2 and IV.5 registry paragraph; FE brief II.3.

## PATHS

| kind | path | cell | use |
|---|---|---|---|
| reuse | `data/firm_registry.json` | B1, B5 | 49F/COT/INF tenant vocabulary; excludes test/demo |
| reuse | `infra/aws/lambda-edge/auth-validator-edge/index.mjs` | B2, B15 | server-derived JWT/firm/advisor policy; the scope-check integration source |
| reuse | `data/assets/scripts/silver/silver_registry.py`, `mirror_schemas.py`, `rebalancer_schemas.py`, `bd49f_dim_conversion.py` | B1 | typed daily source catalogue |
| reuse | `data/assets/scripts/gold/runners_49f/a01_dim_relationship.py`, `a06_dim_identity_crosswalk.py`, `d08_firm_ownership_map.py`, `bd49f_dim_portfolio_group.py` | B1 | 49F relationships and identity |
| reuse | `data/black_diamond/scripts/bronze/build_schwab_bd_account_xref.py` | B1 | reconciliation prior art only, never an authorization rule |
| reuse | `data/inf/scripts/gold/runners_inf/a00_dim_account.py`, `a01_dim_relationship.py`, `runner_common.py` | B1 | Inflection identity |
| reuse | `data/cot/scripts/gold/runners_cot/a01_dim_relationship.py` | B1 | Cottonwood relationships; placeholder roles prove no book |
| reuse | `portal/src/pages/AdvisorIntelligence/_partners/{49financial,inflection,cottonwood}/roles.ts` | B2 | presentation vocabulary, not grants |
| reuse | `lib/trading_calendar.py` | B1, B4 | business-date selection |
| reuse | `infra/aws/terraform/partners-api/api-gateway.tf` | B3, B15 | `/api/scoped/advisor-intelligence/` CUSTOM-auth route pattern |
| reuse | `portal/src/pages/ModelPortfolios.tsx`, `portal/src/components/ui/PageSurfaceControl.tsx` | B15 | Global/scoped UI pattern reference (FE implements) |
| reuse | `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py` | B11 | bounded BD helpers |
| reuse | `infra/aws/lambda/inf-pipeline/inf-performance-daily/pull_inflection_performance_dim.py` | B11 | saved-query prior art, not the scope endpoint |
| reuse | `docs/research/bd_dashboard_teardown/BD_DASHBOARD_HAR_TEARDOWN_20260721.md`, `docs/research/competitive_recon/orion_20260722/ORION_TEARDOWN_20260722.md` | B11 | reconnaissance |
| reuse | `infra/aws/ec2/bd-49f-auto-login/{bd_49f_auto_login.js,run-bd-auto-login.sh,package.json}`; `infra/aws/terraform/bd-49f-auto-login/{iam,instance,main}.tf` | B8 | the runner pattern to adapt (separate host/role for YCharts) |
| reuse | `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py`, `infra/aws/lambda/ycharts-session-capture/index.mjs`, `infra/aws/terraform/ycharts-pipeline/` | B6, B8 | existing YCharts consumers; the older client assumes status 200 |
| reuse | Secrets Manager `ycharts/login/credentials` (existing), `ycharts/credentials` (legacy, untouched), `ycharts/session/current` (proposed), `astn/kimi/api-key` (existing) | B8 | no value ever in brief, log or repo |
| reuse | `data/assets/scripts/gold/runners_49f/b04_account_model_membership.py`; `infra/aws/lambda/opal-assets/opal-assets-silver-smartx/smartx_conversion.py` | B12 | 49F membership + SmartX join/status logic |
| reuse | `data/inf/scripts/gold/INF_E_00.eclipse_model_portfolios.py` | B12 | Eclipse grains and managed/excluded meaning |
| reuse | `data/assets/scripts/gold/build_dim_model_portfolio.py`, `build_cottonwood_mdpf_pair.py` | B12 | target recursion inspection only |
| reuse | `data/mdpf/scripts/gold/mdpf_category_registry.py` | B12 | canonical taxonomy |
| reuse | `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md`, `docs/architecture/D3_ACCOUNT_MODEL_OVERLAY_PRD.md` | B12 | prior art |
| reuse | `infra/aws/lambda/news_layer3_curation/lambda_function.py`, `news_trending_analysis/lambda_function.py`, `keyword_drilldown_generator/lambda_function.py` | B13 | news production; ownership stays with its producers |
| reuse | `infra/aws/lambda/portal_data_proxy/lambda_function.py`; `infra/aws/lambda/v2_portal/01_market_overview/lambdas/trending-topics-portal-publisher/lambda_function.py`; `portal/src/api/{portal-proxy.ts,endpoints/market.ts,endpoints/sentiment.ts,endpoints/trending.ts}` | B13 | current serving boundaries; historical narrative data comes from B13, not these fallbacks |
| reuse | DynamoDB `opal-news-trending-daily`, `opal-news-articles`; `s3://opal-data-news-v2/trending_reports/YYYY/MM/DD/trending_report_HHMMSS.json` | B13 | primary history; publication/cutoff timezone verified |
| reuse | `deck_generation/brand/opal_brand_guidelines.pdf`, `deck_generation/brand_spec/brand.json`, `deck_generation/engine/brand.py`, `deck_generation/brand/logo_package/Opal-Capital-Logo-Package/Full Logo/Full Color/Opal-Capital-Logo-Full-Color.svg` | B14 | brand authority; official logo |
| new | `infra/aws/lambda/investor-reporting/` | B2-B17 | feature-specific service modules; handlers/queues separated by directory, performance, intake/generation, holdings, narrative, export as boundaries warrant |
| new | `infra/aws/terraform/investor-reporting/` | B3, B4, B5, B8, B15, B16, B17, B18 | deployment definitions; `safe-apply` only |
| new | `data/assets/scripts/gold/investor_reporting/` | B1, B12 | isolated derived-data runners; PLATINUM JSON via the publisher into `opal-data-portal-v2` |
| new (proposed, absent at inspection) | `opal-data-ycharts` SSE-KMS bucket; `firms/{firm_id}/intake/YYYY/MM/DD/{id}/...`, `firms/{firm_id}/requests/{id}/revisions/{r}/...`, `firms/{firm_id}/generations/{id}/attempts/...` then `vendor/report.pdf`, `sections/report.json`, `exports/{revision}/report.pdf`; a separately enumerated quarantine location | B5, B17 | opaque-id paths; source read permission does not grant writes |
| new | `/api/scoped/investor-reporting/...` | B15 | follows the partners-api scoped layout |

## FIXTURES AND EVIDENCE

| artifact | cell | proves / limits |
|---|---|---|
| `docs/briefs/sources/INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json` | all | path existence; nine source hashes |
| `docs/briefs/sources/INVESTOR_REPORTING_LIGHTWEIGHT_EVIDENCE_20260910.json`; `INVESTOR_REPORTING_UNIFICATION_PROPOSAL_20260909_extracted.txt` | B1, B2 | original lightweight and unification evidence |
| `docs/briefs/sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json`; `docs/research/investor_reporting_performance_20260910/probe_performance.py` | B11 | nine HTTP outcomes, two 401s, seven successes; does NOT establish 49F live parity, multi-account BD aggregation, Orion subset exclusion, all annualization/accrual/currency/benchmark cases, full history |
| `docs/briefs/sources/INVESTOR_REPORTING_EXPORT_NARRATIVE_EVIDENCE_20260910.json`; `docs/research/investor_reporting_export_20260910/{profile_export_capture.py,build_export_review.py,performance-export-review.pdf,FONT_LICENSE.txt}` | B13, B14 | 139-entry BD export capture, 15-page sample, queued package chain NOT captured; the four-page PDF is synthetic prior art |
| `docs/briefs/sources/INVESTOR_REPORTING_YCHARTS_SOURCE_EVIDENCE_20260910.json`; `INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json`; `YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`; private packet (six transcripts, manifest, three HARs, 1,085 entries, six POST/GET pairs); `docs/research/investor_reporting_ycharts_20260910/profile_handoff.py` | B8, B9, B10 | three generation routes; PDF bodies ABSENT; upload multipart body NOT captured; real forwarded-message/holdings specimens and effective mailbox grant STILL NEEDED |
| `docs/briefs/sources/INVESTOR_REPORTING_MODEL_OVERLAY_EVIDENCE_20260910.json`; `docs/research/investor_reporting_model_overlay_20260910/{source-list.json,profile_snapshot.py}` | B12 | 23 Parquet objects, 15,753,977 bytes; joins measured per IV.5; bounded, not permission to infer complete attribution |

## BRIEF COVERAGE

Denominator: 28 sections of the brief at `2acf23d8fd` + 9 source documents = **37 entries**. Every entry maps to a cell and outcome or carries `NOT CONSUMED` with its reason. Unmapped entries: **0**.

| # | entry | consumed by | outcome |
|---|---|---|---|
| 1 | title / preamble (ownership paragraph, v1 exclusions) | B18 (boundaries); v1 exclusions carried as NOT-IN-SCOPE constraints on every cell | all |
| 2 | PART I heading | structural | -- |
| 3 | O1 permitted clients, authorized population | B1, B2, B3 | FWD-1, FWD-2 |
| 4 | O2 comparable performance, vendor semantics | B11 | FWD-3 |
| 5 | O3 holdings email becomes a scoped request | B5, B6, B7 | FWD-9 |
| 6 | O4 correct YCharts variant, recoverable generation | B8, B9, B10 | FWD-4 |
| 7 | O5 current custody holdings, model percentages | B12 | FWD-5 |
| 8 | O6 branded reproducible export, evidence-backed context | B13, B14 | FWD-8 |
| 9 | O7 bound to its firm at ingestion; operations | B5, B16, B17 | FWD-10, FWD-7 |
| 10 | O8 Opal user across every firm | B15, B2 | FWD-11 |
| 11 | PART II heading | structural | -- |
| 12 | II.1 what this team owns / crosses to FE | every cell's CROSSES column; the ownership split above | all |
| 13 | II.2 shared owners and limits | B18 (coordinate with OPAL_ASSETS/D10, D1_CATVIEWS, ASSETCLASS_TAXONOMY, D3_MODELOVERLAY, ADVI_ECLDAT, WSE_COTMDL, MDPF3FIRMS, PORTAL_AUTHHARD/ADVI_ROLGAT, ADVI_BDAPIMIG.P1, YALP_MDSRC, OPAL_ADVIPOINTERS -- reuse never widens deployment or IAM) | all |
| 14 | II.3 shared contract inventory | CONTRACTS table; B3 keys | all |
| 15 | PART III qualitative bar | the ACCEPT lines of the ENDPOINT section are the bar in plain English | all |
| 16 | PART IV heading | structural | -- |
| 17 | IV.1 four briefs + five supporting documents | entries 30-38 below | all |
| 18 | IV.2 identity, tenant scoping, daily movement | B1, B2, B4, B5, B15, B16 | FWD-1, 2, 7, 10, 11 |
| 19 | IV.3 performance adapter recipe and limits | B11; FIXTURES row 3 | FWD-3 |
| 20 | IV.4 YCharts intake, session library, retrieval | B6, B7, B8, B9, B10, B17 | FWD-4, FWD-9, FWD-10 |
| 21 | IV.5 partner joins, classifications, paths | B12 | FWD-5 |
| 22 | IV.6 narrative evidence, brand assets, export execution | B13, B14 | FWD-8 |
| 23 | IV.7 evidence artifacts and new code homes | FIXTURES table; PATHS new rows; B18 | all |
| 24 | IV.8 required detail coverage in the backend PRD | this table | -- |
| 25 | PART V what must be true | B18 dependency register: auth/identity contracts and tested tenant routing; provider credentials per tenant; actual YCharts PDFs, upload specimens, forwarded-mail form, mailbox grant, session compatibility; source completion semantics and missing mappings/units; historical news evidence policy; FE RenderPackage + fixtures; register representation (done) | all |
| 26 | PART VI status | NOT CONSUMED: not outcome-bearing; records compilation clock and source hashes, which FIXTURES row 1 already carries | -- |
| 27 | PART VII what this brief does not claim | NOT CONSUMED as work: it bounds claims (no production backend, no release policy, no export service, no fresh permission result, no native fidelity certified by assembly); carried as the NOT-CLAIMED list every cell's acceptance is read against | -- |
| 28 | REFS TO CARRY | NOT CONSUMED as work: a link list; each referent is consumed through the entry that cites it | -- |
| 30 | S1 original unification brief | B1, B2, B16, B18 (identity/cohort semantics, provider common shape, business clocks, path manifests, future boundaries) | FWD-1, 2, 7, 10 |
| 31 | S2 lightweight brief | B1, B2, B3, B11, B9, B12, B16, B13 | FWD-1..8 |
| 32 | S3 YCharts brief | B6, B7, B8, B9, B10 | FWD-4, FWD-9 |
| 33 | S4 model-overlay brief | B12, B16 | FWD-5 |
| 34 | S5 lightweight design | B1, B2, B11, B14, B17 (identity/provider maps, normalizer and serving boundaries, cache/export semantics, 31-path index) | FWD-1, 2, 3, 8 |
| 35 | S6 performance review | B11 (exact BD/Orion endpoints, units, response traps, proof gaps) | FWD-3 |
| 36 | S7 export/narrative specification | B13, B14 (logo option, deterministic events, dated evidence, frozen bundle) | FWD-8 |
| 37 | S8 YCharts design | B6, B7, B8, B9, B10, B17 (mailbox/checkpoint/parse, runner and secrets, endpoint/body recipe, storage/jobs, section shape, missing specimens) | FWD-4, FWD-9 |
| 38 | S9 model-overlay design | B12 (source grains, partner joins, taxonomy/denominators, ETL/publisher boundary, offline recipe) | FWD-5 |

(Entry numbering skips 29 so the source rows read S1..S9 as 30..38; the count is 28 + 9 = 37.)

## SURFACE MANIFEST

Surfaces this project writes, reads or executes. Every new surface is registered with its owner during implementation; nothing here is deployed by this document.

| surface | kind | cell | owner |
|---|---|---|---|
| `infra/aws/lambda/investor-reporting/` | new code home | B2-B17 | IRPT_BCKEND |
| `infra/aws/terraform/investor-reporting/` | new deployment definitions | B3, B4, B5, B8, B15, B16, B17, B18 | IRPT_BCKEND; `safe-apply` only |
| `data/assets/scripts/gold/investor_reporting/` | new derived-data runners | B1, B12 | IRPT_BCKEND (DS lane rules apply to gold scripts) |
| `opal-data-portal-v2` PLATINUM JSON via the publisher | write | B1, B12 | existing publisher owner; this project's keys registered |
| `opal-data-ycharts` (proposed) with per-firm prefixes and a quarantine location | new bucket + layout | B5, B17 | IRPT_BCKEND; `FirmDestinationPolicy` owner named at L5 |
| `/api/scoped/investor-reporting/...` | new routes | B15 | IRPT_BCKEND under the partners-api authorizer owner |
| DynamoDB tenant/request tables, queues, outbox, leases | new | B16, B17 | IRPT_BCKEND |
| Secrets `ycharts/login/credentials`, `astn/kimi/api-key` (read); `ycharts/session/current` (proposed write) | read / proposed write | B8 | existing owners; no widening of any role |
| Black Diamond and Orion performance endpoints; YCharts endpoints per B9; mailbox `requests@opalinvest.com` -> `opalbloomberg@opalinvest.com` | external, read | B6, B9, B11 | NO LIVE CALL authorized by this document -- each per-use on explicit word |
| Silver/Gold sources named in PATHS reuse rows | read | B1, B12 | their existing owners; manifest-declared dependencies |
| news DynamoDB tables and `opal-data-news-v2` | read | B13 | news producers; ownership unchanged |
