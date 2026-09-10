# Investor Reporting — YCharts Analysis intake and serving brief

**Author:** 4.0.0_SA_CRO. **Date:** September 10, 2026. **Mode:** NEW child brief within the existing Lightweight Investor Reporting umbrella, D9 Opal Workflows, WS3. This does not register another project. **Recon:** RCN-0008 follow-up. **Consumer:** CTO for endpoint formulation; umbrella coordinator for downstream workstream boundaries.

**Commission:** [Andrew's direction and subsequent clarifications](../../org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_YCHARTS_INTAKE_AND_SERVING.md). **Parent outcome:** O4 in the [umbrella brief](investor-reporting-lightweight-brief-20260910.md). Child outcome numbers below are local to this brief; they do not replace parent or permanent endpoint numbers.

An advisor sends a request with actual holdings attachments to **requests@opalinvest.com**. The forwarder delivers it to the internal **opalbloomberg@opalinvest.com** mailbox. A cloud service collects new requests every 15 minutes, every day, from **08:00 through 23:45 America/New_York**, interprets the requested analysis and holdings, and generates the appropriate YCharts report. The result becomes available in the selected client's **Analysis** tab, using Opal presentation and the shared branded export system.

Andrew selected the **same BDAPI Kimi runner pattern**, with no OTP stage, and explicitly accepted Alyssa and the automation evicting one another's sessions. Session recovery is therefore part of normal operation. The quarter-hour schedule is for mailbox intake; vendor session acquisition is driven by generation work. Encrypted generation records belong in **opal-data-ycharts**. The [design annex](investor-reporting-ycharts-design-20260910.md) contains explicit retrieval instructions, field mappings, recovery behavior and the dependency sequence Andrew requested.

**Automation proposal for Andrew's review:** complete requests that pass input, identity, vendor-result and rendering checks should become available automatically. Human review is an **exception path**, not a staffing requirement on every analysis. The recordings describe an analyst queue; carrying that existing practice into every release would go beyond Andrew's stated hope for an entirely programmatic flow. His preference between automatic validated release and universal analyst approval has been asked explicitly; the former is this brief's proposed default, not a claimed ratified policy.

**Why exceptions remain:** the transcripts describe ambiguous securities and proposed ETF substitutions; the example manifest records wrong-object selection and concurrent-login eviction. No parser/inference accuracy study was performed, so these sources do not prove that all inference is unsafe unattended. Deterministic identity/type checks and resumable execution address the recorded object/session failures automatically. An unresolved security, ambiguous account grouping or unapproved economic substitution needs correction only when the resolver cannot establish a unique supported mapping. A validated mapping, reconciled inputs and certified output checks allow that class of request to proceed without an analyst. No generic confidence cutoff or mandatory human signoff is invented.

# PART I — THE OUTCOME TERRITORY

### O1 — An advisor submits holdings by email and can identify the resulting request

The advisor uses the forwarder address and includes holdings files plus the desired report and comparisons. A request received overnight is collected when the daily window resumes. Duplicate mailbox delivery does not silently create another report, while an intentional revision remains possible. Request status is visible in the portal without depending on a desktop session or Alyssa manually transferring files.

**Provable act:** carry an actual forwarded attachment through durable intake and the client-scoped request list; replay the delivery, interrupt a mailbox scan and cross the overnight boundary. Reconcile source message/attachment identities with resulting requests and revisions.

### O2 — An advisor or analyst can inspect and correct the holdings and choices the program inferred

Clear inputs proceed programmatically. An authorized viewer can see the requested variant, source file and holdings date, dollars versus weights, resolved securities, cash, advisory fee, comparison identities and cover information. Missing fields, ambiguous share classes and proposed ETF replacements remain visible in the exception path. Correcting an input creates a new revision and preserves the original evidence. Unsupported positions are not silently removed to obtain a successful report. Merely having an inspection/correction capability does not gate every request on a person.

**Provable act:** review fixtures containing cash, a share-class mismatch, an ambiguous name, an unsupported holding, multiple attachments and a missing comparison; trace every resolved or proposed field to its input or approved mapping. The recorded workflow's mistaken-symbol example must remain detectable in the review.

### O3 — An advisor obtains the requested Overview, Comparison or Multi-Comp analysis

The service uses **Comprehensive Overview (No Benchmark)** for the primary portfolio, **Comprehensive Comparison (No Benchmark)** for one comparison, and **Comprehensive Multi-Comp (No Benchmark)** for two to five comparisons. The analyst can distinguish a saved Opal model from a similarly named fund or separate account. The annual advisory fee is **0.30%**, as specified in the newer workflow. Other settings and vendor-returned dates remain explicit; modeled historical results are not represented as the client's realized performance.

**Provable act:** follow each variant from a fixed input revision through its exact vendor portfolio identity, report configuration, response and downloaded PDF. Exercise the supported comparison cardinalities and inspect the rendered results, including model and public-security comparisons. The supplied capture proves a three-security Multi-Comp example, not every allowed cardinality.

### O4 — An advisor obtains the same requested analysis after a recoverable session interruption

Alyssa may sign in while automation is working, and automation may acquire a new session when it needs one. The service records the completed stages, reacquires authentication when appropriate and resumes from known state. It never substitutes the newest item in the shared YCharts portfolio list for the requested portfolio. An uncertain report submission is visible as uncertain until reconciled; a retry does not imply that the vendor supports exactly-once generation.

**Provable act:** interrupt before and after portfolio creation, after report submission and during artifact persistence; inject a concurrent-login eviction. Verify that the same request stays attached to the correct portfolio and that uncertain side effects are reconciled before another submission.

### O5 — An authorized advisor reads and exports the validated analysis in Opal's presentation

The existing client selector routes the Analysis tab. It shows report variant, holdings date, generation date, fee/method assumptions, comparisons and validation/exception status. The advisor reads the supported YCharts sections in Opal components and exports the same released revision using the shared brand template, including optional advisor branding supplied by Andrew. Separate section data dates, missing data, footnotes and hypothetical disclosures survive shaping and export.

**Provable act:** compare a downloaded YCharts PDF, its extracted section contract, the tab and the Opal PDF for each variant. Verify exact values, labels, units, dates, series, comparison order and disclosures. An embedded vendor PDF can provide an intermediate preview; it does not satisfy this native presentation outcome.

### O6 — An advisor receives a validated revision and can recover its evidence later

The proposed default releases a revision automatically after its checks pass; unresolved exceptions enter an authorized correction/review queue. The advisor or analyst can inspect the original attachments, normalized inputs, generation configuration, vendor output and correction history. The portal displays only the revisions and clients the viewer is entitled to access. Release does not send an email automatically. Universal analyst approval is an alternative for Andrew to select, not an assumed dependency.

**Provable act:** complete a valid request without human intervention, correct an exception into a new revision, and reproduce each release's source chain and export identity. Try a different firm's request, report and download identifiers and revoke access while a cached result exists. Failed or superseded attempts remain identifiable without exposing them to another advisor.

# PART II — WHERE THE BOUNDARY SITS

| Boundary | WS3 owns | Named dependency or sibling |
|---|---|---|
| Intake and request interpretation | Mailbox delta processing, attachments, typed request/revision, holdings parsing and interpretation evidence | Microsoft 365/Sitez mailbox identity and the requests@ forwarder; actual application permissions must be established |
| Vendor execution | YCharts portfolio, comparison and template resolution; session recovery; report retrieval | **ADVI_BDAPIMIG.P1** runner primitives; **YALP_MDSRC** existing YCharts session/transport ownership |
| Records and serving | Encrypted request/generation history, vendor artifact, analysis section adapter, review lifecycle | **WS1** common report states, scope authorization, client directory, UI components and PDF/brand system |
| Holdings context | Submitted attachment snapshot and its mapping to the selected client/accounts | **WS4 / OPAL_ASSETS** supplies optional dated holdings context; it must not replace submitted holdings with newer silver holdings silently |
| Analytical meaning | YCharts modeled analysis, its settings and vendor disclosures | **WS2** owns custodian performance and its narrative page; WS3 does not recalculate those returns or add a separate scenario engine |

The shared YCharts login is vendor-wide; portal entitlement remains per firm/advisor/client. A mailbox sender, folder, PDF URL or YCharts object name cannot confer client access. WS1 supplies canonical scope checks; WS3 applies them to requests, jobs, reports, review actions and exports. The umbrella coordinator assigns write paths and resolves shared-contract changes. This brief issues no task orders or seat assignments.

# PART III — THE QUALITATIVE BAR

1. An ordinary, complete request reaches a generated draft without manual file transfer or browser operation.
2. An analyst can explain every included holding and comparison, including any proposed substitute.
3. A successful vendor response cannot conceal wrong-client, wrong-model or incomplete-input selection.
4. A session takeover delays work without losing the request's identity or silently duplicating vendor objects.
5. The Analysis tab and branded PDF preserve what YCharts actually calculated, with understandable assumptions and dates.
6. A historical report remains reproducible from its recorded evidence after templates, holdings or branding change.

No throughput, timeout SLA, numeric interpretation threshold or retention duration is ratified by this brief. Observed timings and configurable engineering budgets are identified separately in the annex.

# PART IV — THE SUBSTRATE

**F1 — The packet covers all three generation routes.** Six transcripts and a root request manifest were read. All 26 files in the ZIP's manifest matched their declared hashes and sizes. The three supplied slim HARs contain **220, 403 and 462 entries**, totaling **1,085**. All three variants are in the August HAR; the July HARs are additional blended walkthroughs. The [offline evidence inventory](sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json) records indices against these supplied files, not the different original indices quoted in the handoff prose.

**F2 — Report rendering returns a URL directly.** Six report POSTs returned HTTP 201 with a report URL; each URL matches a subsequent HTTP 200 PDF GET. The captured report POSTs took approximately 8.7–34.7 seconds. No PDF body is preserved in those GETs. Portfolio calculation uses status polling; report rendering in these captures is a synchronous POST. The handoff's background-job description is not supported by these responses.

**F3 — Older captures close two response-shape gaps.** July HAR 03 contains upload response fields and a creation response with **model_portfolio_id**, not a generic `id`. It also contains 1% fee settings that must not override the August capture and analyst's 0.30% workflow. The September root manifest records a concurrent-login eviction and a wrong-folder selection caused by falling back to the newest list row. These are recorded incidents, not failures reproduced in this research.

**F4 — The chosen authentication pattern exists in source.** The exact reference is `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js`, its shell wrapper and its Terraform module. It uses Node, Playwright and Kimi with bounded retries and DOM fallback, an SSM-managed transient EC2 runner and scoped secret persistence. Its OTP-dependent success checks require a YCharts-specific replacement. CTO messages 95295/95301 add a dated estate snapshot corroborating five declared resources; that is not a new live YCharts login test.

**F5 — Secret contracts need separation.** Live inspection found `ycharts/credentials` contains legacy **cookies**, despite older comments describing login credentials. The existing `ycharts/session/current` secret had no AWSCURRENT value. At Andrew's request, **ycharts/login/credentials was created in us-east-1 and read-back verified against the supplied login**. The legacy cookie secret was untouched. Values are omitted from repository artifacts. Source and metadata receipts are in the [source evidence](sources/INVESTOR_REPORTING_YCHARTS_SOURCE_EVIDENCE_20260910.json).

**F6 — The requested generation bucket is new infrastructure.** At **2026-09-10 15:41:51 UTC**, HeadBucket returned 404 and the location/encryption/public-access/versioning reads returned NoSuchBucket for `opal-data-ycharts` using the expected Opal account. The proposed bucket configuration is specified; no bucket was created in this research.

**F7 — Native rendering still needs output evidence.** The packet's PDF GETs omit bytes. Its separate non-YCharts report engine and sample outputs are not YCharts section-parity fixtures. The root manifest's referenced source spreadsheet and generated PDF were not found as written, relative to the supplied folder, by basename there or by exact basename within the extracted packet. The prior comparison field census is useful starting evidence, but all three actual output families need paired PDFs and extraction checks. Non-default transformations/downside scenarios remain uncaptured; null payload fields do not establish a scenario-creation API.

# PART V — DEPENDENCIES

The mailbox route and a narrowly scoped cloud mailbox identity precede verified unattended intake. Input/revision semantics precede safe portfolio creation. A YCharts session adapter and a certified template/configuration fixture precede dependable generation. Paired vendor outputs and section mappings precede native Opal rendering parity. WS1's client entitlement and export contracts precede advisor release and download. An analyst is a dependency for unresolved exceptions under the proposed default, not for every successful request. These dependencies can be developed under the existing workstreams; the annex describes their integration sequence without assigning task orders.

Remaining evidence to procure is concrete: one representative forwarded message with holdings attachment(s), the production mailbox application/folder binding, a current upload request/validation response, and matching YCharts output PDFs for the three report variants. The supplied recordings resolve the overall generation flow and the user's subsequent answers resolve daily polling, attachments, shared-session eviction and the Kimi runner choice.

# PART VI — CURRENT STATUS

**NOT-OUTCOME-BEARING.** This is a researched, reviewable brief and retrieval specification. The offline profiler is runnable; the login secret is stored and verified. These facts do not certify intake, login automation, generation, review, tab rendering or export in production. Endpoint ratification, project status and downstream issuance remain with their existing authorities.

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

No live YCharts login/report call, mailbox poll, forwarder setup, bucket deployment or production UI change was performed for this cut. The BDAPI reference does not prove that YCharts accepts the same native AWS execution environment. No OTP mechanism, fixed session-sharing schedule, proxy fallback, automatic client email distribution, replacement analytics engine or uncaptured scenario family is added. Original evidence gaps in the parent brief retain their historical meaning; this dated follow-up updates the WS3 research state.

## REFS TO CARRY

```text
BRIEF       docs/briefs/investor-reporting-ycharts-brief-20260910.md
DESIGN      docs/briefs/investor-reporting-ycharts-design-20260910.md
PARENT      docs/briefs/investor-reporting-lightweight-brief-20260910.md (WS3 / parent O4)
HAR FACTS   docs/briefs/sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json
SOURCES     docs/briefs/sources/INVESTOR_REPORTING_YCHARTS_SOURCE_EVIDENCE_20260910.json
PROFILER    docs/research/investor_reporting_ycharts_20260910/profile_handoff.py
DIRECTION   org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_YCHARTS_INTAKE_AND_SERVING.md
PROJECT     Existing Investor Reporting umbrella; no new registration by this brief
STATUS      NOT-OUTCOME-BEARING; no implementation or endpoint acceptance claimed
```
