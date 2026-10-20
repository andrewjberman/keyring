# Ticket Center Analysis Request: the backend, step by step (state at 2026-10-20 9:12 AM ET)

Written by `4.0.0_SA_CRO~TCKT`, read-only. Sources are files at `origin/CLOUD` and the portal's `origin/PROD`, read 13:12Z.
The PRD is IRPT_ANLREQ v0.24.

**Times.** Times are US Eastern. Each technical line gives UTC (Z).

**Claim tags.**
- **[M]** measured: read from a receipt, live state or code.
- **[I]** inferred.

**State tags.**
- **LIVE-PROVEN**: a live run exercised it and left a receipt.
- **LIVE-UNEXERCISED**: deployed, but no live run has shown it.
- **BROKEN-ON-PROD**: the defect is live.
- **NOT-BUILT**: not built (or deliberately left unconfigured).

**How the "proof" runs work.** The proof runs so far (runs 5 and 6) called the APIs directly as a script. They did not
use the web page. No staff user has filed through the PROD page since the new form went live at 5:28 AM:
- IB2's read found 0 analysis tickets created after 09:28:44Z, with 35 of 35 items scanned at 11:56Z [M]
  (`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_pagefiled/A_PAGEFILED.txt`).

---

## S1. Open the Ticket Center and press New Ticket
- **What happens:**
  - The page is shown to Opal staff only (PRD v0.6).
  - Loading the board reads the open tickets and their counts from the ticket service.
  - No analysis work starts here.
- **Component:** Lambda `opal-ticket-api`, table `opal-tickets`, behind the portal API's JWT authorizer
  (`opal-portal-authorizer`).
- **State: LIVE-UNEXERCISED.**
  - The v0.24 page has been on PROD since 5:28 AM, portal `f48e09dd` [M].
  - It was proved offline against a build of the PROD code [M]
    (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~323/PAGE_NOTES.md` section 3).
  - No staff read on PROD yet [M].
- **Technical:**
  - `GET /api/scoped/tickets?status=open`
  - `GET /api/scoped/tickets/metrics`
  - shell reads `portal-content` and `advisor-intelligence/platinum/firm/*.json`
- **Gap:** New Ticket defaults to Service Request for staff, so the filer must choose Analysis Request [M] (PAGE_NOTES
  section 4 item 5).

## S2. The form opens
- **What happens:**
  - The form asks the firm-directory service which partner firms exist and shows them in "Choose the firm this request is
    filed under".
  - The five Opal models are a fixed list built into the page. They show immediately, with no network call.
  - The ETF catalogue is fetched only if the filer types in "Other ETFs".
  - There is no report-type dropdown, no advisor-email field and no commentary checkbox.
- **Component:** Investor Reporting directory route (`/investor-reporting/directory/resolve`), plus the static list
  `opalModels.ts` in the portal.
- **State: LIVE-UNEXERCISED.**
  - On PROD [M].
  - Proved offline: 12 labels, advisor optional, report_type absent, commentary absent, 3 firms, 5 models [M]
    (PAGE_NOTES section 5).
- **Technical:**
  - `POST /api/scoped/investor-reporting/directory/resolve` (Global context) is called when the form opens.
  - `GET .../analysis/comparisons` is called only when Other ETFs is typed (AR-y-419).
- **Gap:**
  - Firm labels on PROD were not read live [M] (PAGE_NOTES section 4 item 8).
  - The submit button stays held until the firm list loads. A retry was added in AR-y-429 [M] (FWD_STATE v4).

## S3. Upload the holdings file (the "upload door")
- **What happens:**
  - The browser sends the CSV/XLSX bytes to the upload door. The door checks every ticker in this order:
    1. Yahoo (yfinance);
    2. YCharts, only for a symbol Yahoo does not have.
  - A ticker that does not exist gets a "Did you mean <symbol>?" prompt with Yes, Replace and No.
  - A ticker that exists but cannot be priced is filed UNRESOLVED, with the words "Opal Staff will manage the
    replacement". C-SWAP replaces it later, in the backend.
  - An Opal staff filer is no longer refused for want of an advisor. With no advisor, or an unprovisioned one, the owner
    is the signed-in staff user. This is the O1 fix, live since 3:10 AM.
  - The upload is stored under the firm's state prefix as `original_holdings`, with its normalized form beside it.
- **Component:** Lambda `irpt-ycharts-generate` [M] (r37 receipt S1). The code is `intake/uploads.py` and
  `_authz/served.py` `_create_owner`. Objects are written under `irpt/<firm>/state/` (`original_holdings`,
  `normalized_portfolios`, `extraction_evidence`) [M] (run 6 note D).
- **State: LIVE-PROVEN through the API.**
  - Run 6, 4:02 AM: an unseeded staff user with no advisor and not on the allow-list. Upload NORMALIZED on the second
    post [M] (`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e6/A_E2E6.txt` lines U, A2).
  - The O1 owner fallback is live: r37 v2, CodeSha256 `PlCjNms/...`, applied 07:09:59Z to 07:11:01Z, census 0 [M]
    (`.../irpt_anlreq_r37/A_AFTER_R37.txt`).
- **Technical:**
  - `POST /api/scoped/investor-reporting/analysis/inputs?selected_tenant=<firm>`.
  - The answer is NORMALIZED or NEEDS_CORRECTION.
  - The page re-posts while the door answers RESOLVING (5 tries, 3 s apart).
  - `served.py:1078-1094`: a blank advisor, or an `AdvisorUnprovisioned`, returns `access.prospect_owner()` [M].
- **Gap:**
  - The Keep path (an unknown ticker kept, then replaced by C-SWAP) has never been exercised past the door [M]
    (FWD_STATE v6, "not yet exercised").
  - The page has no "Keep" control. Its hint buttons are Yes, Replace and No [M] (PAGE_NOTES section 4 item 3).

## S4. Create the ticket
- **What happens:**
  - The ticket service writes one ticket of type `analysis_request`.
  - The routing table fills its routing lists: `analysis_request` primary = manav@ and alyssa@opalinvest.com [M]
    (`infra/aws/terraform/ticket-center/main.tf`).
  - The ticket starts `open` and unclaimed.
- **Component:** `opal-ticket-api` (`create_ticket`, `lambda_function.py:1380`), table `opal-tickets`.
- **State: LIVE-PROVEN through the API** (run 6 line T, "ticket ok") [M].
- **Technical:** `POST /api/scoped/tickets` with source `ticketcenter:i1` [M] (PAGE_NOTES section 3).
- **Gap:** none measured.

## S5. Submit the analysis (BROKEN on the PROD page)
- **What happens:**
  - The page sends the analysis request.
  - The service validates it:
    - the report type is worked out from the number of comparisons (0 Overview, 1 Comparison, 2+ Multi-Comp;
      `variant: "auto"` accepted);
    - `commentary_requested` must be true or false.
  - It records the request and queues it for the report host.
  - The staff filing is stamped `ticket_confirmed` (the r37 fix in `ticket_confirmation.py`). That stamp is what routes
    it to Opal's own report producer.
- **Component:** `irpt-ycharts-generate` (`ycharts/generate/submission.py`), table `irpt-requests`, the generation
  queue to the resident host.
- **State on the backend: LIVE-PROVEN through the API** (run 6 S: `REQ-7206be963b5d2108980885ca` at 08:02:38Z) [M].
- **State on the page: BROKEN-ON-PROD** [M]. On PROD `f48e09dd`:
  - The page's own client check (`readSubmissionRequest`, `contracts/submission-request.ts`) refuses the body, because
    it now carries `commentary_requested`.
  - The page shows "Analysis: FAILED - Invalid analysis submission request".
  - No analysis POST is sent, so the ticket is left with no report.
  - Surprise row `IRPT_ANLREQ-D2-W323-S1`, 7:28 AM.
- **Fix:**
  - Commit `e9ca1106`; the CTO approved row 4bfc at 8:02 AM.
  - Promote order `TO-PROMOTE-GUARD` (AR-y-457) was cut to `0.4.0_DT_ClientPlatform~DELL2` at 8:01 AM.
  - Read at 9:12 AM: **not on PROD.** `origin/PROD` tip is still `f48e09dd` (5:20 AM), and `merge-base --is-ancestor
    e9ca1106 origin/PROD` is false [M].
- **Technical:**
  - `submission.py:16`: `PUBLIC_FIELDS` includes `commentary_requested` [M].
  - `:73`: the variant must be `auto` or the derived one [M].
  - `:82`: the value must be a bool [M].
  - The resident's pinned schema was fixed in r34m v2, 3:30 AM [M] (`.../irpt_anlreq_r34m/A_AFTER_R34M.txt`).

## S6. Record the report id on the ticket
- **What happens:** the page writes the new request id onto the ticket as `report_ref`. That is what makes "Open report"
  appear on the row.
- **Component:** `opal-ticket-api` `POST /api/scoped/tickets/{id}/report`.
- **State: LIVE-UNEXERCISED from the page.**
  - Blocked behind S5 on PROD [M].
  - Proved offline on the fix branch: the call list is upload, ticket-create, analysis-request, ticket-report [M]
    (PAGE_NOTES section 3).
  - Run 6's receipt does not show this step [M].
- **Gap:** on plain PROD the ticket never gets a `report_ref`, so there is no Open report button [M].

## S7. The report is generated on the resident host
- **What happens:**
  - The always-on EC2 host takes the request from the queue.
  - It routes a staff filing to Opal's own producer, not the YCharts report.
  - It prices every holding in this order:
    1. Opal's own stores;
    2. Yahoo, at T-1;
    3. YCharts, one symbol per call, price only;
    4. C-SWAP's class-matched replacement;
    5. otherwise the holding is dropped and the report says so.
  - It builds the report PDF and stores it as `ycharts_opal_reports`, and marks the job READY.
- **Component:** the resident host, running root `/opt/irpt-resident/0485393f3a-r34n` since 6:58 AM [M]. The code is
  `ycharts/generate/resident_worker.py` and `ycharts/research/opal_producer.py`.
- **State: LIVE-PROVEN.** Run 6 reached the Opal producer, and the job was READY within about 30 s [M] (A_E2E6 P1;
  FWD_STATE v5).
- **Technical:**
  - `producer_for` (`resident_worker.py:177`) picks Opal when either:
    - the principal is in `OPAL_PRODUCER_PRINCIPALS` (andrew@, `fwd1-staff-r41b@opal.invalid`; `:170`); or
    - the record is `ticket_confirmed` [M].
  - r34m v2: V2S PRICING OK, and "SPY KEPT and ZQXWVK NOT_KEPT" [M].
- **Gap:**
  - The content of a staff Multi-Comp report PDF has not been read since the fixes [I].
  - On 10-19 a Multi-Comp run.json showed `calls: []` [M, earlier gap file G8].

## S8. READY: the commentary is drafted and rendered as a PDF
- **What happens:**
  - At READY the host signals that the analysis is ready.
  - The commentary drafter (the Kimi model) writes the investment commentary from the report's key figures. It uses no
    client identity, and the draft is marked DRAFT.
  - The draft is stored as `analysis_commentaries`. It is then meant to be rendered as a standalone branded PDF.
  - The host's role lacked permission to read the draft. This was fixed live at 6:04 AM.
- **Component:**
  - Lambdas `irpt-commentary-composition-read-lambda` and `irpt-commentary-draft-store-lambda` [M, served graph].
  - The drafter is in `data/transcripts/scripts/commentary/`.
  - Storage: `opal-data-irpt/irpt/<firm>/state/analysis_commentaries/` [M].
- **State:**
  - Draft: **LIVE-PROVEN** (run 6: P2 commentary_ref yes, P3 draft yes, 08:04Z) [M].
  - Commentary PDF: **LIVE-UNEXERCISED.** In run 6 the PDF step did not run, because the packager stopped first (P5
    NOT-RUN) [M].
- **Technical:**
  - IAM statement `ReadTheAnalysisCommentaryDraft` (get only, put implicitDeny), applied 10:03:20Z to 10:04:12Z [M]
    (`.../irpt_anlreq_iamgrant/A_AFTER_IAMGRANT.txt`).
  - The commentary-ready queue held 1 message and its dead-letter queue 1 after run 6 [M].

## S9. The packager attaches the four files to the ticket
- **What happens:**
  - At READY, the packager posts pointers to three files onto the ticket: the original upload, the form as filed and
    the report PDF. This step no longer waits for commentary (AR-y-423).
  - When the commentary PDF exists, the packager adds it as the fourth.
  - It does this as the service account `svc-irpt-packager`, bound to the firms `49financial,cottonwood,inflection`.
- **Component:**
  - Host packager `ycharts/research/opal_packager.py`, calling `POST /api/scoped/tickets/{id}/package`
    (`package_ticket`, `lambda_function.py:1796`).
  - Since 6:58 AM it calls through the portal's CloudFront address (r34n).
- **State: LIVE-UNEXERCISED.**
  - Run 6, 4:02 AM, failed at this step [M]: the attach was refused 403 `ORIGIN_VERIFICATION_FAILED`, because the
    packager called the API's direct host [M] (`.../irpt_anlreq_packager_403/A_PACKAGER_403.txt`). The ticket had no
    `package` [M].
  - The fix is live:
    - r34n installed 10:58:00Z [M] (`.../irpt_anlreq_r34n/A_AFTER_R34N.txt`);
    - the CloudFront probe was ADMITTED by the authorizer and answered 404 for a bogus ticket, which shows the route
      works [M] (`.../irpt_anlreq_packager_cfprobe/A_PACKAGER_CFPROBE.txt`).
  - No real ticket has received a package yet [M].
- **Technical:** `PACKAGE_ALLOWED_FIRMS = "49financial,cottonwood,inflection"` (ticket-center `main.tf:361`) [M]. The
  package principal has no `opal-users-v2` profile row, by design [M] (A_PACKAGER_403 R3).
- **Gap:** this is the step FWD-1 depends on. Run 7, set for 10:15 AM, is the proof [M] (FWD_STATE v6).

## S10. The board shows the package; "Open report"
- **What happens:**
  - The ticket row shows "Report package" with four links: Original file, Form as filled (a table of the answers),
    Open Report and Open Commentary.
  - Each link is a short-lived signed link.
  - "Open report" now shows the report's own figures ("report mode"). The hundreds of internal "text / not available"
    cards are now under "Technical details".
- **Component:**
  - Portal `AnalysisRequestParts.tsx` (package block) and `RetainedSections` in report mode (FWD-8).
  - Data from `GET .../analysis/{requestId}/sections`.
- **State:**
  - Report face: **LIVE-PROVEN** on r34l. In run 5D, 3 sections (1 with a value) replaced about 425 cards [M]
    (FWD_STATE v4).
  - Package block on PROD: **LIVE-UNEXERCISED.** It was proved only offline with test data [M] (PAGE_NOTES; screenshots
    `shots_offline/`).
- **Gap:**
  - The form-as-filled table still prints a row "Add commentary: Yes", although the checkbox is gone [M] (offline
    screenshot b1).
  - The offline report face shows synthetic labels. Real section labels on a staff report have not been read [I].

## S11. When a step fails, the ticket says so
- **What happens:**
  - The three silent steps can each record one failure on the job: the ready signal, the commentary draft and the
    packager.
  - The ticket page reads the job's status and shows which step failed and what happens next, in fixed words. Nothing
    is written onto the ticket itself.
  - The failure display goes away once the package is attached.
- **Component:** `irpt-jobs` attribute `hop_failure`, status route `irpt-status` (`status.py` word table), portal
  `useHopFailureWords`.
- **State: LIVE-UNEXERCISED** [I].
  - Run 6 produced a packager retained-for-retry, `ClientError` [M].
  - No receipt shows what the ticket page displayed for it [M].
- **Gap:** FWD-4, which requires each failure driven on purpose, has not been run [I].

## S12. Emails to people
- **What happens today:** nothing is emailed for an analysis request.
  - Client notices ("Your request has been picked up") go only to an address in `CLIENT_NOTICE_CONTACT_MAP`, which is
    `{}` [M] (`main.tf:422`; live read 10-19).
  - Internal distribution emails go to `TICKET_DL_MAP`, which is `{}` [M] (`main.tf:391`).
- **Component:** `opal-ticket-api` SES sender `tickets@opalinvest.dev`.
- **State: NOT-BUILT (deliberately unconfigured)** [M].
- **Gap:** whether staff should be told when a package lands is not decided anywhere I read [I].

---

## What is not yet proven
1. A staff user filing through the PROD **page** end to end. It is blocked at S5 until `e9ca1106` reaches PROD [M].
2. The four attachments on a real open ticket (S9 to S10). Run 7 at 10:15 AM is the first chance [M].
3. The standalone **commentary PDF** being rendered and attached (S8): never reached [M].
4. The **Keep / C-SWAP** path for an unknown or unpriceable ticker, past the door (S3, S7) [M].
5. A **Multi-Comp** report's comparison figures, read in the PDF since the fixes (S7) [I].
6. The **failure display** on the ticket for a driven failure (S11, FWD-4) [I].
7. **Another firm's user** being refused the ticket and every package file (FWD-5): not part of today's runs [I].

## Open defects and their owners
| Defect | Where | Owner | State |
|---|---|---|---|
| Page refuses its own analysis submit (`commentary_requested`) | portal `contracts/submission-request.ts` | DT `0.4.0_DT_ClientPlatform~DELL2` (order TO-PROMOTE-GUARD); issuer `2.0.0_SA_COO~Y2` | fixed on DEV `e9ca1106`; NOT on PROD at 9:12 AM [M] |
| Package never yet attached to a real ticket | host packager / ticket `/package` | `2.0.0_SA_COO~Y2`, run by `0.7.0_AE_CloudOps~IB2` (run 7) | both measured causes fixed live; unproven [M] |
| Six synthetic run-6 objects could not be deleted (AccessDenied) | `irpt/49financial/state/` | `0.7.0_AE_CloudOps~IB2` / `2.0.0_SA_COO~Y2` | open [M] (A_E2E6 note D) |
| "Add commentary: Yes" row left in Form as filled | portal `AnalysisRequestParts.tsx` | `2.0.0_SA_COO~Y2` | open [M] |
| Run-6 commentary message in the dead-letter queue (1) | commentary-ready queue | `0.7.0_AE_CloudOps~IB2` | open [M] |
