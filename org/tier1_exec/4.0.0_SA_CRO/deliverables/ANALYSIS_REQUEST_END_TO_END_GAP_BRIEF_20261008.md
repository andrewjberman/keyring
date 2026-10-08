# ANALYSIS REQUEST: end-to-end trace brief, and the one project it compresses into

Prepared by 4.0.0_SA_CRO~DELL2 on 2026-10-08, ~22:4xZ to 23:1xZ. A read-only assessment with proposed closure requirements
(`/closer trace`, which needs no Andrew word). No application changes, vendor calls, deployment or schedule activation.
Five read-only research passes measured the slices: Ticket Center, IRPT_BCKEND, IRPT_YCDGEN, NFRA_TRNSPT commentary, and
the lanes' current waits. Live AWS reads were limited to function configuration, table description and S3 listing.

Order: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md`
@70041807fa, addendum @2b21a349d1 (CTO~DELL2 msgs 1805, 1809).

## Design finding

**What the surface is meant to do.**
1. An advisor or Opal person fills ONE Ticket Center "Analysis Request" form: analysis type; comparables (checkboxes for
   Opal models, plus an input for other ETFs); the holdings Excel; ticker typo check and swap settled inside the form.
2. A ticket opens in the Ticket Center for Alyssa.
3. With no person in the loop, Opal's backend then:
   - generates the full report;
   - reads key surfaces of that report to write the investment commentary;
   - renders a branded Opal PDF carrying the commentary;
   - attaches the package (the report, the branded PDF and the advisor's original Excel) to that same open ticket.

The Analysis tab is the manual exception path, built after (Andrew's addendum).

**How far the implementation is from that.** The parts exist across four projects and five lanes, and **no part knows the
next one by a ticket**:
- **Form:** the ticket form exists and is deployed, but it has none of the comparables fields and no swap.
- **Upload door:** works (template lane, typo check as advice only).
- **Generation:** the vendor path has produced 21 real PDFs. The in-house Opal engine has never produced a report end to end.
- **Commentary:** no generator exists; it is issued today, unbuilt, and does not read the report.
- **Package:** nothing renders it.
- **Ticket attachment:** nothing attaches anything to a ticket, and the Ticket Center PRD forbids bytes on a ticket
  (C-ONE-DOOR).

The work worth keeping is most of it. The missing pieces are the **joins**: a ticket id carried end to end, a trigger, an
attach-back, and a package renderer.

## Current measurement

Read live on 2026-10-08, ~22:3xZ to 22:5xZ UTC (function configuration, table description, S3 listing):
- `opal-ticket-api`: LastModified 2026-10-07T19:21:15Z, CodeSha256 `y0UFtRIf...`, equal to `lambda-source-map.json:2787`
  (commit da43155418, the latest touching `infra/aws/lambda/ticket_center/lambda_function.py`). Deployed equals source.
- DynamoDB `opal-tickets`: 12 items, 0 of type `analysis_request`; GSI `status-index`; no Stream.
- IRPT functions:
  - `irpt-ycharts-generate` 2026-10-08 21:26:18 (release 3);
  - `irpt-export-render` 2026-10-08 22:11:43;
  - `irpt-narrative` 2026-09-21;
  - `irpt-intake-poller` 2026-09-11.
- Resident host `i-0167fd745ad906a66` (`irpt-ycharts-runner`), build `409e3066d1-st24` per its latest record. Its package
  was not read over SSM.
- Vendor PDFs: 21 under `s3://opal-data-irpt/irpt/cottonwood/state/vendor_documents/` (2026-09-27 to 10-05).
- Opal-engine PDFs on the served path: 0. The F1 run at 21:10Z today was refused at render with `LayoutRefused`: brand
  assets absent on the host (row IRPT_YCDGEN-D2-S3).
- `s3://opal-data-transcripts` `outlook/transcripts/gold/`: 0 objects.

NOT invoked: any form submission, any generation, any Kimi or YCharts call, any UI render.

## Adapter map

| Leg | Provider, intended endpoint | Existing work | Gap |
|---|---|---|---|
| Form | portal TicketCenter -> `POST /api/scoped/tickets` | `AnalysisRequestParts.tsx`, `analysisRequest.ts:92-120` (on origin DEV and PROD, f7fa7fb1) | comparables as free text; no Opal-model checkboxes or ETF input; no swap |
| Upload, check, swap | IRPT `POST /api/scoped/investor-reporting/analysis/inputs`; resident securities_info + Kimi | `intake/uploads.py`, `upload_resolution.py`, `upload_suggestions.py` | swap refuses (`resolution_kimi.py:159-165`); YCharts session EVICTED 10-05; SHARES prices not composed |
| Ticket | `opal-ticket-api`, `opal-tickets` | 8 routes; `report_ref` via `POST /tickets/{id}/report`, assignee-only, `in_progress` only | no service write; no event; pointers only |
| Generation (vendor) | resident -> YCharts | `ycharts/generate/*`; 21 real PDFs; about 17-19 min per run | no ticket id; session evicted |
| Generation (Opal engine) | resident -> `ycharts/research/opal_producer.py` -> `render_pdf.cjs` | branded Overview HTML-to-PDF; Andrew-only allow list | brand assets missing (w-6 issued, not run); Overview only; no comparables |
| Commentary | NFRA_TRNSPT round 12: slicer + one Kimi K3 call | `data/transcripts/scripts/outlook/slicer.py`; contract `org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json` | drafter not written; input is request fields, not the report; gold empty; Kimi held by C-WIPE-GATE |
| Branded package PDF | `irpt-export-render` + `infra/aws/ec2/investor-reporting-export/render_export.cjs` (portal print route) | has an ANALYSIS kind and a narrative packet in `export/bundle.py` | not wired to an Analysis Request; commentary content unverified |
| Attach-back | ticket API | -- | no route; PRD forbids bytes on a ticket |

## Start-to-finish walk

### 1. Advisor -> Analysis Request form -- MISMATCHED

What exists: `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx`, `TicketCenter.tsx`, `analysisRequest.ts`.
Fields: advisor, firm, household, report_type (Overview, Comparison, Multi-Comp), `comparison_model` as free text (:74),
advisory_fee, needed_by, `add_commentary` (:87), holdings file `.csv,.xlsx` (:94).

The exact mismatch: Andrew's form has Opal-model checkboxes and an other-ETF input. The form has one free-text field. The
backend already has the list the checkboxes need (`ycharts/generate/comparison_catalogue.py`: Opal models in
`templates.json`, plus etf-classifications), but the form does not read it.

Close: the form reads the comparison catalogue and posts structured `comparables: {opal_models: [...], etfs: [...]}`.
Proof: a submitted ticket's `answers` carries both lists.

### 2. Form -> holdings upload, typo check and swap -- INCOMPLETE

What exists: the form uploads first (`analysisRequest.ts:92-120`) through the template lane (`file_base64` csv/xlsx). The
upload defers symbol resolution to the resident's YCharts `securities_info` (`intake/upload_resolution.py:102-113`). The
typo check works as advice only: Kimi suggests, the provider verifies, the user accepts (`intake/upload_suggestions.py`;
exercised REQ-0d97252f).

The exact mismatch:
- Swap refuses `KIMI_WEB_SEARCH_UNVERIFIED` (`intake/resolution_kimi.py:159-165`); CTO msg 120 moved swap to IRPT_YCDGEN
  FWD-16 (candidates from etf-classifications), not built.
- Resolution itself needs a live YCharts session, which has been EVICTED since 10-05.
- The form shows NEEDS_CORRECTION findings read-only, with no accept or swap control.
- SHARES-basis files refuse (`SHARES_PRICE_SOURCE_NOT_COMPOSED`). See
  `RESEARCH_20261008_IRPT_CSV_UPLOAD_LANE_RESOLVERS.md` @53e4cf25d4.

Close: resolution moves off the YCharts session, onto Opal's own etf-classifications plus security reference (the
IRPT_YCDGEN direction), and the form renders each finding with Accept and Swap. Proof: a file with one typo and one
unlisted fund reaches NORMALIZED through the form alone.

### 3. Form -> ticket -- WORKS (deployed, never exercised for this type)

What exists: on NORMALIZED, the form posts `{ticket_type: 'analysis_request', title, answers, attachment:{upload_id,
input_id}}` to `opal-ticket-api` (`lambda_function.py` router :1263-1294; `ROUTING_MATRIX` routes analysis_request to
alyssa@ and manav@). The open Ticket Center page lists tickets from the real backend (`TicketCenter.tsx:141`).

The exact mismatch: none in the code. 0 of 12 tickets are `analysis_request`; TV-r-1 waits on an organic filing.

Close: a seat-driven filing on DEV, with the real login. Proof: the ticket row and the page listing it.

### 4. Ticket -> backend trigger -- MISSING

What exists: generation starts only when the ticket's human assignee clicks "Request report" (`AnalysisRequestParts.tsx:117-143`),
which records `report_ref` through `POST /tickets/{id}/report` (:1163-1207, assignee-only, `in_progress` only). The table has no
Stream; the Terraform has no bucket, stream, SNS, SQS or EventBridge. NFRA_TRNSPT's H1 "READY hook" is owned by
IRPT_BCKEND `~P2` and does not exist ("no stream yet", @6061d0e274).

The exact mismatch: Andrew's journey "finishes itself". The code needs a person to click.

Close: ticket creation of type `analysis_request` enqueues ONE generation request carrying `ticket_id`, on the existing
`irpt-generation` queue (the same closed-message shape as `resolve_upload`, `upload_resolution.py:38-47`), from the ticket
Lambda. No Stream and no new bus. Proof: the ticket's creation produces a job row whose request names the ticket.

### 5. Trigger -> full report -- INCOMPLETE

What exists:
- **Vendor path:** `irpt-ycharts-generate` -> resident `resident_worker.py` / `durable_job.py` -> YCharts -> vendor PDF at
  `vendor_documents/` (21 real; about 17-19 min each, 15m07s of it the read-back lease).
- **Opal engine:** `opal_producer.produce(...)` (`ycharts/research/opal_producer.py:205`) -> `layout_overview.build` ->
  `render_pdf.cjs`. Chosen per principal (`resident_worker.py:116-133`, Andrew only); no fallback by design (C-SWITCH).

The exact mismatch:
- No request carries a ticket id (0 "ticket" references under `investor-reporting/`).
- The vendor session is evicted.
- The Opal engine refuses at render (brand assets; TO-YCD-w-6 issued, its input commit 6d71a05c62 not yet on `box/dell2`).
  It also makes the Overview only, with no comparables (FWD-4 not built).

Close: the job carries `ticket_id` through to READY. The live thread uses the Opal engine once w-6 lands (Andrew is its
allowed principal); the vendor path stays the documented fallback only while the session is live. Proof: one READY report
whose record names the ticket.

### 6. Report -> investment commentary -- MISSING

What exists: NFRA_TRNSPT round 12 (issued 2026-10-08 18:27, @71b72d7a3e): TR-e12 (READY event to request), TR-d12
(slicer plus one Kimi K3 drafter), TR-t12 (ticket-write client). The code folder does not exist yet. Commentary gold has
0 objects. The first Kimi call waits on C-WIPE-GATE. Other narrative code is not commentary: `narrative/prose.py` is a
template for performance, and `kimi_port.py` is the check gate.

The exact mismatch: Andrew says the commentary is written by "running over key surfaces in that report". TR-d12's input
is the request's abstract fields plus the nearest past commentaries, never the report. And with gold empty, there are no
past commentaries to draw on.

Close: the drafter's input contract becomes the READY report's structured surfaces (the `AnalysisReport` v2 document the
Opal engine already persists: holdings, allocation, characteristics), with past commentary as style examples only when
gold has rows. Proof: one drafted commentary whose evidence cites report fields by name.

### 7. Report + commentary -> branded Opal PDF -- MISSING

What exists:
- The Opal engine's branded Overview PDF (`layout_overview.load_brand`), which has no commentary section.
- `irpt-export-render` (deployed 22:11Z today): the portal print route through headless Chromium
  (`render_export.cjs`, `portal/src/pages/InvestorReporting/render/manifest.ts`), with an ANALYSIS kind and a narrative
  packet in `export/bundle.py`.
- Trade-offs: `CRO_RESEARCH_IRPT_CUSTDY_RENDER_FORK_20261007.md`.

The exact mismatch: nothing composes report plus commentary into one branded document.

Close: ONE renderer. Recommended: the Opal engine's own HTML layout gains a commentary section and renders the package
PDF. It already owns the brand spec and the report data, so the package needs no second render stack. Proof: one PDF with
the logo, the report pages and the commentary.

### 8. Package -> attached to the open ticket -- MISSING

What exists:
- A ticket holds pointers only, by PRD design (TCKT_VNEXT C-ONE-DOOR, PRD :95).
- `report_ref` is written only by the human assignee.
- F10's planned `svc-commentary` principal can only CREATE tickets, so it cannot append to this one (row D2-S6; open item O2).

The exact mismatch: Andrew wants the package on the SAME open ticket. No route lets a service write to an existing ticket.

Close: one service route `POST /tickets/{id}/package` for a service principal, appending
`package: {report_ref, pdf_ref, original_ref, commentary_ref}`. These are pointers to retained artifacts, which keeps
C-ONE-DOOR's no-bytes rule (a PRD amendment names the new writer). Proof: the ticket row carries the package refs.

### 9. Ticket page -> the package, downloadable -- MISSING

What exists: "Open report" shows only the request id, revision and firm (`AnalysisRequestParts.tsx:146-161`). There is no
attachment list. A signed-link reader exists for retained reports (`ops/owned_report.py:154`). The original Excel is
retained (`s3://opal-data-irpt/irpt/cottonwood/state/original_holdings/`).

Close: the ticket page lists the package's three files, each opened through the existing signed-link reader under the
viewer's own scope. Proof: Alyssa opens all three from the ticket.

## Recommended completion sequence

1. **The live thread** (one person, one journey, coarse):
   - Andrew files one Analysis Request (Overview, no comparables, no commentary) on DEV, with the real login. Hops 1 and 3
     work as built.
   - The ticket enqueues generation with its id (hop 4).
   - The Opal engine produces the Overview after w-6 (hop 5).
   - The service route attaches `report_ref` + `original_ref` to the same ticket (hop 8).
   - Alyssa's page opens both (hop 9).
   - Recorded as ONE trace artifact. The shared first hop (portal login, scoped API) is the ticket lane's and is already
     live.
2. Commentary from the report (hop 6), then the package PDF (hop 7) attached as `pdf_ref` and `commentary_ref`.
3. The form's structured comparables (hop 1) and the Comparison and Multi-Comp report types (IRPT_YCDGEN FWD-4).
4. Typo check and swap inside the form, off the YCharts session (hop 2).
5. The Analysis tab as the manual exception path (Andrew's addendum), last.

## Acceptance

One reconciled trace per case, following one request from the form submission, through the ticket row, the job row
carrying the ticket id, the report record, the commentary record and the package refs, to the three files opened from the
ticket page.

Cases: 3 report types x {Opal models only, ETFs only, both} x {clean file, typo then swap, unknown security,
SHARES-basis file} x {session expired, resident down, attach refused}.

## The one project (proposal for the CTO's `/closer propose` and Andrew's word)

**Why one project.** Measured at 22:37Z, no lane is idle; all five are WORKING. But each lane's next served act waits on
someone else:
- `~P2`: a laptop IAM leg for the H1 hook;
- `~Y2`: a laptop cleanup result;
- `~G2`: the laptop's logo commit reaching `box/dell2`;
- `~T2`: hooks H1 and H5 owned by `~P2` and `~V2`, and C-WIPE-GATE;
- `~V2`: Alyssa's organic filing and the laptop's O1 token.

The four projects declare **seven** dependencies on each other. NFRA_TRNSPT and IRPT_YCDGEN, the commentary and the report
it should read, never name each other. Every served apply on dell2 routes to `0.7.0_AE_CloudOps~DELL2`, which was seated
today with no commits. That is the structure Andrew named: no single driver can run the journey, because no single
project owns it.

**Shape.**

| Moves into the one project | Stays where it is |
|---|---|
| TCKT_VNEXT's Analysis Request scope: form, ticket, trigger, attach route, ticket page (FWD-6 and its F10 cut) | TCKT_VNEXT's non-analysis ticket types, if any (to confirm at L3) |
| IRPT_BCKEND `~Y2`'s Analysis lane: upload door, check and swap, generation, release gates | IRPT_BCKEND `~P2`: Performance and the Performance client statement |
| IRPT_YCDGEN: the Opal engine, its brand, FWD-4 report types, FWD-11 vendor retirement | -- |
| NFRA_TRNSPT FWD-10 and FWD-11 and round 12 (the commentary thread), retargeted to read the report | NFRA_TRNSPT FWD-1 to FWD-9: Teams transcripts, the company read, readers, mail pull |
| The Analysis tab, as the exception path, last | -- |

- **ONE driver:** one COO lane under `/closer-drive` (FAST, Andrew present) or `/canonical-drive`, plus one CVO.
- **ONE applier:** CloudOps~DELL2 named in the contract.
- **Cross-box items** become pre-arranged inputs with owners and dates, not waits discovered mid-round: the laptop IAM leg,
  the O1 service token, the brand-asset sync, and the YCharts session (only if the fallback is kept).
- **NO-STOP RULE (the defect Andrew named):** a hop that waits on another box parks that ONE hop in STATUS.md with its
  owner and un-park condition, and the driver moves to the next hop the same tick. Nothing waits on a future trigger: the
  thread uses a seat-driven filing, with Alyssa's organic filing as the negative arm (spine L2, "no FWD is a wait").

**Code:** a new code is for the CTO at L3. Suggested: `IRPT_ANLREQ`.

**What needs Andrew's word:** the build phase of the closer (the contract, the mandates, the seats), and the TCKT_VNEXT
PRD amendment that adds a service writer to an existing ticket (hop 8).

## Evidence anchors and limits

Source read at `box/dell2` HEAD (846cbbe61e era) and portal origin DEV/PROD f7fa7fb1. Lanes move concurrently.

Not verified:
- a signed-in UI walk;
- the resident host's package (no SSM);
- live job rows;
- whether IRPT's on-behalf door change is what `opal-ticket-api`'s caller hits;
- what `irpt-narrative` and `irpt-export-render` produce for an ANALYSIS kind;
- whether the C-WIPE-GATE record exists;
- the laptop's progress on the IAM leg, cleanup and O1 token.

Key paths:
- `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx`, `analysisRequest.ts`, `TicketCenter.tsx`
- `infra/aws/lambda/ticket_center/lambda_function.py`; `infra/aws/terraform/ticket-center/main.tf`
- `infra/aws/lambda/investor-reporting/intake/{uploads,upload_resolution,upload_suggestions,resolution_kimi}.py`
- `infra/aws/lambda/investor-reporting/ycharts/generate/{resident_worker,durable_job,comparison_catalogue,publication_worker}.py`
- `infra/aws/lambda/investor-reporting/ycharts/research/{opal_producer,layout_overview}.py`
- `infra/aws/lambda/investor-reporting/export/bundle.py`; `infra/aws/ec2/investor-reporting-export/render_export.cjs`
- `org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R12.md`; `org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json`
- `org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_F10.md`; `org/missions/SEQUENCE.yaml:135-149`; `org/ref/LIVE_ARMS.md:47-56`

## Andrew-direct request -- verbatim record

Channel: the `1.0.0_SA_CTO~DELL2` terminal, 2026-10-08 ~22:3xZ, relayed as msgs 1805 and 1809. Full text in the record
above, @2b21a349d1. Its two load-bearing sentences:

> This should effectively compress the IRPT_BCKEND IRPT_YCDGEN parts of NFRA_TRNSPT TCKT_VNXT and any unaddressed
> frontend into one project.

> I think it is important to think of this whole process as one singular workflow that covers all of these surfaces. Then,
> frontend work on the actual "Analysis" tab will be completed after the fact, because the manual process should be done
> there only for unusual cases if it cant be done otherwise for whatever reason (maybe a swap issue, unusual request, etc)
