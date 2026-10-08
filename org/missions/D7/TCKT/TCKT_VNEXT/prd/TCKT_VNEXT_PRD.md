# TCKT_VNEXT (renamed from OPAL_TICKET_VNEXT) -- the Ticket Center takes typed requests, the Analysis Request first

```json
{
 "project": "TCKT_VNEXT",
 "directive": "D7",
 "fabric": "laptop",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/d7-ticket-center-request-types-analysis-request-first-brief-20261007.md@750ec86588",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
 "status": "DRAFT"
}
```

Renamed from `OPAL_TICKET_VNEXT` at L3. Placement DELL2 (laptop ruling 106359). Endpoint:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_OPAL_TICKET_VNEXT_20261007.md` @c7da21e358.

Author `1.0.0_SA_CTO~DELL2`, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. **Purpose document:** `docs/architecture/D7_TICKET_VNEXT_PRD.md`
(2026-08-31). Only its WS-1 (the storage read) and WS-2 (attachments) are inside this PRD; WS-3 to WS-6 are out (brief II.3).
**L4 reads:** this seat's read-only sweep at 16:3xZ of the service, its Terraform, the deployed function, the Analysis upload path and
IRPT_YCDGEN's PRD. Each is cited in section 1.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Alyssa files an Analysis Request with a holdings file and opens the finished report from the same ticket
         DONE WHEN  EXERCISED -- on DEV, an Opal sign-in in Alyssa's role files one request (one household, one account, an Overview report, the default fee)
                    with a real holdings file and follows it to the report opened on the ticket; Alyssa's own first real request grades it again (the organic arm)
         ACCEPT     someone at Opal files the request with the file attached, the report is made from that file without anyone re-typing the holdings, and the
                    finished report opens from the ticket; it fails if anyone forwarded a file by email or chat at any step
         SOURCE     brief I.0 (the candidate thread), O1, O4

  FWD-2  A person at another firm cannot open the request or its file
         DONE WHEN  EXERCISED -- a sign-in belonging to a different firm (a test account at that firm, made for the purpose) tries both and is refused,
                    and the attempt can be repeated on demand for Andrew to watch
         ACCEPT     someone signed in for a different firm tries to open the ticket and its attached file and is refused both times; Andrew can ask to see it
                    done again at any time; a statement that it is refused does not count
         SOURCE     brief O2, finding F7, Part V

  FWD-3  The person filing learns at once when the file will not work, before anyone at Opal sees it
         DONE WHEN  EXERCISED -- a known-bad sheet (several accounts in one file, a totals row, a holding that cannot be priced) is turned back with what to
                    fix, and a known-good sheet goes through; Alyssa's own two test sheets grade it again when she supplies them (the organic arm)
         ACCEPT     a file that today would come back from Alyssa by email comes back from the form instead, saying what to fix; the good file files normally
         SOURCE     brief O3, finding F6 (9 of 31 requests needed a resubmission)

  FWD-4  The person who filed a request can work it and finish it themselves
         DONE WHEN  EXERCISED -- one Opal sign-in files a request, claims it and completes it, on DEV
         ACCEPT     the person who filed a request claims and completes that same request, on any type of ticket; nothing stops them because they filed it
         SOURCE     brief finding F4; Andrew 2026-09-30 ("that rule of no one can file and run their own ticket is nonsensical", all tickets)

  FWD-5  Someone working the queue sees every open request of every type in one place and can tell them apart without opening them
         DONE WHEN  EXERCISED -- an Opal person picks the next request to work from the queue alone
         ACCEPT     an Opal person reads each request's type and how long it has waited from the queue itself, and opens only the ones that are theirs
         SOURCE     brief O6

  FWD-6  When a request asks for commentary, the draft appears on the same ticket for an Opal person, and the ticket shows who sent the final commentary and when
         DONE WHEN  EXERCISED -- one request with commentary asked for: the draft read on the ticket and the sender recorded
         ACCEPT     an Opal person finds the draft beside the report on the ticket, reviews it, and anyone opening the ticket later can tell who sent the final
                    commentary to the advisor and when
         SOURCE     brief O5; NFRA_TRNSPT FWD-10 and FWD-11 seen from the ticket

  FWD-7  A second kind of request is added without rebuilding the Ticket Center
         DONE WHEN  EXERCISED -- a second type, defined by someone who did not build the first, is filed by a person
         ACCEPT     the second request type has its own questions and its own destination, someone files it, and the Analysis Request works exactly as before
         SOURCE     brief O7, finding F6; which type is second is decided after FWD-1 has run, on what the tickets show

  FWD-8  An advisor files an Analysis Request themselves and follows it to the finished report
         DONE WHEN  EXERCISED -- one advisor who has never seen the Ticket Center files a request with their own file, unaided
         ACCEPT     an advisor at a client firm files a request without being walked through it and opens the finished report from their ticket
         SOURCE     brief O8, call B
         WAIT       QUALIFIED: Andrew removed the client "Submit a Request" item in August. The client-facing surface returns only on his explicit word,
                    after FWD-1 has run on real requests. That word is the one wait this outcome carries.
```

## 1. What exists (the L4 reads; MEASURED unless marked)

| # | fact | source |
|---|---|---|
| R1 | **Routes:** create, submit, list, metrics, get, claim, complete. Ticket ids match `^TCK-\d{8}-[0-9a-f]{8}$` | `infra/aws/lambda/ticket_center/lambda_function.py:6-17, :64, :1083-1112` |
| R2 | **Types:** `VALID_TYPES` holds four labels. A type keys `ROUTING_MATRIX` (primary, secondary, visibility). The submit body admits only `ticket_type`, `title` and `description`, so no attachment field | `:62, :55, :417, :83` |
| R3 | **`_sod_block`** returns 403 when the caller is the requester (claim and complete), or on complete when another person holds the ticket | `:904-915, :926, :988` |
| R4 | **No per-firm check on read or list.** List scans or queries with no firm filter; get has no firm check. Clients are refused every read only because their class is absent from the route matrix. The only firm check is on create | `:73-81, :874-878, :898, :848-849` |
| R5 | **Identity:** the portal's custom authorizer context (email, name, userType, firmId, allowedFirmIds). Internal means firmId `opal-capital` | `:199-208, :57, :223` |
| R6 | **Deployed function:** `opal-ticket-api` CodeSha256 `/38KUtP9...`, 2026-08-21. It equals the source-map hash for `lambda_function.py` at `481dde1dbf`. **Not read:** whether the repository changed since | `infra/aws/lambda/ci/lambda-source-map.json:2773-2785` |
| R7 | **Terraform:** one table, one role, logs/DynamoDB/SES policies, the function module, the API route, one permission. **No bucket** | `infra/aws/terraform/ticket-center/main.tf` |
| R8 | **The Analysis upload door exists:** `POST /api/scoped/investor-reporting/analysis/inputs` -> `UploadService.create`. It refuses on size, encoding and duplicate fields; it checks that the uploader is the actor with matching firm. Limits: 2,000 rows, 200 symbols (HOLDING_LIMIT). It handles total and subtotal rows (STATED_TOTAL, SUBTOTAL_ROW_PRESENT, TOTAL_MISMATCH) and refuses PRICE_MISSING and PRICE_INCOMPATIBLE. It returns NORMALIZED / NEEDS_CORRECTION / RESOLVING with findings. **No multiple-accounts check found** | `intake/upload_entry.py:20-45`; `intake/uploads.py:20, :223-268`; `template_reader.py:20-21`; `parse.py`; `portfolio.py:249-252` |
| R9 | **The file is stored once,** as family ORIGINAL_HOLDINGS / ORIGINAL_CSV under `opal-data-irpt/irpt/<firm>/...`. The upload id is a hash of the firm, the principal and the token | `uploads.py:240, :264-268`; `infra/logic/registry/reporting_policies.json:19,31`; `ycharts/generate.tf:155` |
| R10 | **Report submission takes the upload's handle:** `AnalysisSubmissionRequest.input_id` goes to `POST /api/scoped/investor-reporting/analysis`. INFERRED from code: IRPT_YCDGEN's PRD names no entry other than the Analysis tab | `AnalysisSubmissionRequest.ts:20`; `ycharts/generate/entry.py:148` |

## CONTRACTS

| Contract | Owner | Binding agreement |
|---|---|---|
| C-ONE-DOOR: the holdings file enters by the Analysis upload door | IRPT_BCKEND (the door); this project (the call) | The Analysis Request's file goes through `POST .../analysis/inputs` (R8), which runs the same checks and the same firm attribution, and stores it once (R9). **The ticket stores the upload's handle (`upload_id`, `input_id`), never the bytes.** No ticket bucket is created for this type. **OWNED DEPENDENCY (CVO review P1, measured):** the door refuses an `opal-capital` owner (`intake/uploads.py:193`) and an actor whose home firm differs from the owner's (`:227-234`), so an internal filer working on behalf of an advisor's firm is refused today. **Ruling:** the door admits an internal principal whose `allowedFirmIds` names the owner firm, records BOTH the acting principal and the owner firm on the upload, and refuses everyone else exactly as now. That is a change to IRPT_BCKEND's contract, requested from its COO at L5, never written from this project. This answers brief Part V's door question and the purpose document's WS-1 for the Analysis Request: the file's store and readers are IRPT's, already firm-fenced by IAM prefix. A type that needs bytes IRPT does not own (a later type, or statements) re-opens WS-1 for that type, and no write happens before that ruling (purpose document :168) |
| C-TYPE: a request type is a definition, not code | this project | A type is data: its label, its questions (field names, kinds, required), its checks (a call to a named door, or none), its route (`ROUTING_MATRIX` primary, secondary, visibility) and its output (what comes back on the ticket). `VALID_TYPES` and the submit body's admitted fields are read from the definitions. The four existing types are expressed as definitions with their behaviour unchanged. FWD-7 grades this |
| C-ANALYSIS-REQUEST: the first type | this project; Alyssa's RT-01 + RT-02 (brief F6), one type by ruling A | **Questions:** advisor, firm, household, report type (Overview, Comparison, Multi-Comp), comparison model when needed, advisory fee (default stated), needed-by date, add commentary (yes or no). **Attachment:** one holdings file, through C-ONE-DOOR. **The type adds one check the door lacks:** one account per file (R8 found no multiple-accounts check). The ticket files only when the door returns NORMALIZED; NEEDS_CORRECTION comes back to the person filing, with the door's findings (FWD-3). **Output:** the generated report's handle on the ticket |
| C-HANDOFF: the ticket asks for the report and receives it | IRPT_YCDGEN (generation); this project (the call) | When an Opal person works the ticket, the report is requested through `POST .../analysis` with the ticket's `input_id` (R10), as the person working it. The returned job or report reference is written to the ticket. The report opens from the ticket by the reference, through the report's own access path, so the reader's entitlement is IRPT's check, not a copy. IRPT_YCDGEN confirms at L5 that this entry is supported for a request it did not start from its own page. If not, that is a request to its COO, never a write into its paths |
| C-FENCE: one firm never reads another's ticket | this project | Get and list refuse a ticket whose firm is not the caller's, unless the caller is internal (R4 today: internal-only reads, with no firm filter). **Required before FWD-8. Exercised for FWD-2 before any real client file is attached:** a real other-firm sign-in refused on the ticket and on the report reference |
| C-SELF-CLAIM | Andrew 2026-09-30 | `_sod_block`'s requester clause is removed for every type (R3). The other clause (complete by a non-holder) stays |
| C-QUEUE | this project | The list shows type and age for every open ticket (FWD-5), from fields the item already holds (`ticket_type`, created time) |
| C-COMMENTARY | NFRA_TRNSPT (FWD-10, FWD-11, C-TICKET-ATTACH) | An "add commentary" request is the trigger NFRA_TRNSPT reads. The draft lands on the same ticket. The ticket records who sent the final commentary and when (FWD-6). This project builds the ticket fields; NFRA_TRNSPT builds the draft |
| C-NAMES | rule 30 | Every new address and name is `lib/opal_naming.py` output printed in the order that writes it. C-ONE-DOOR means no new address is expected for the Analysis Request |
| C-DEPLOY | law | Service and Terraform changes go through `safe-apply`. A Dell writes no Lambda permission or bucket policy (NFRA_CTLPLN); those go to the laptop by role request. Portal page changes are product files and land by the portal's review route |
| C-MORATORIUM | law | No new alert or notification is built. The existing SES email on create is unchanged |

## 2. THREAD -- FWD-1, round 1

1. **File.** Alyssa opens the Ticket Center (internal), chooses Analysis Request, answers its questions and attaches one holdings file.
   The page calls the upload door (C-ONE-DOOR). On NORMALIZED, it creates the ticket with the handle; on NEEDS_CORRECTION, it shows the
   findings and files nothing.
2. **Hold.** The ticket carries the type, the answers and `upload_id` / `input_id`. A second person opens the ticket and sees the same
   file through IRPT's read.
3. **Work.** Alyssa claims her own ticket (C-SELF-CLAIM).
4. **Generate.** Working it, she requests the report from the ticket (C-HANDOFF). Nobody re-types the holdings.
5. **Return.** The report reference is written to the ticket, and she opens the finished report from the ticket.
6. **Trace.** One record shows the ticket id, the upload handle, the report reference and the timestamps. No file left the system by
   email or chat.

Round 1 builds only this thread, on DEV, internal users only.

## 3. ENRICHMENT BACKLOG (ordered)

1. FWD-2 / C-FENCE: the firm check on get and list, exercised with a real other-firm sign-in in front of Andrew.
2. FWD-3: the one-account-per-file check, plus Alyssa's two sheets (bad turned back, good filed).
3. FWD-5: the queue's type and age.
4. FWD-6: the commentary fields with NFRA_TRNSPT (after its FWD-10 drafter exists).
5. FWD-7: the second type, chosen after FWD-1 runs (ruling C).
6. FWD-8: advisor filing, on Andrew's word only.

## 4. Rulings closed at L4

1. One type, "Analysis Request" (L2 ruling A).
2. One door for the file: the Analysis upload path (brief Part V REC, measured R8-R10). No ticket bucket for this type.
3. Statements are out (L2 ruling D).
4. The requester clause of `_sod_block` is removed for all tickets (Andrew 2026-09-30).
5. Round 1 is internal-only. The client surface returns only on Andrew's word (FWD-8).

## 5. SURFACE MANIFEST (step 4 -> step 5)

| id | FWD | surface | owner lane | risk |
|---|---|---|---|---|
| S1 | FWD-1, 4, 5, 7 | `infra/aws/lambda/ticket_center/lambda_function.py` (type definitions, self-claim, ticket fields for handles and report reference) | this project, AE/DT | SERVED at deploy |
| S2 | FWD-1, 3 | `portal/src/pages/TicketCenter/` (the type form, the door call, findings, the report link) | this project, portal review route | product file |
| S3 | FWD-1 | the upload door and `POST .../analysis` (consumed, not written) | IRPT_BCKEND, IRPT_YCDGEN | CONSUME |
| S4 | FWD-2 | the firm check on get and list (C-FENCE) | this project | SERVED at deploy |
| S5 | FWD-6 | the commentary fields and NFRA_TRNSPT's trigger read | this project + NFRA_TRNSPT | later round |

## 6. BRIEF COVERAGE

| brief part | carried in |
|---|---|
| I.0 thread, O1, O4 | FWD-1, section 2 |
| O2, F7, Part V fence | FWD-2, C-FENCE |
| O3, F6 intake rules | FWD-3, C-ANALYSIS-REQUEST |
| O5 | FWD-6, C-COMMENTARY |
| O6 | FWD-5, C-QUEUE |
| O7 | FWD-7, C-TYPE |
| O8, call B | FWD-8 (qualified wait) |
| F4 | FWD-4, C-SELF-CLAIM |
| F5 door question | C-ONE-DOOR (R8-R10) |
| II.3 out of scope | section header; rulings 3, 5 |
| Part VII not claimed | R6 (repository drift since `481dde1dbf` not read); R10 (inferred) |

-- 1.0.0_SA_CTO~DELL2

## v0.2 (1.0.0_SA_CTO~DELL2, 2026-10-07 ~17:3xZ) -- on 3.0.0_SA_CVO's refusal (msg 906, review @003801aeb8)

- **R1:** FWD-2 is now seat-driven. A test sign-in at another firm, made for the purpose, is refused on both reads, and the attempt is
  repeatable on demand for Andrew. It is no longer a wait on his presence.
- **R2:** FWD-1, FWD-3 and FWD-4 are now seat-driven on DEV by an Opal sign-in. Alyssa's real use, and her two sheets, are the organic
  arm.
- **P1:** C-ONE-DOOR now names the door's on-behalf refusal (`uploads.py:193, :227-234`) as an owned dependency, with its ruling.
- **Ids:** none renumbered or retired. The ENDPOINT changed, so the ratified-text half re-opens.

## ADDENDUM 1 (2026-10-08 ~22:2xZ, `1.0.0_SA_CTO~DELL2`): FWD-6 brought forward as its own workstream, on Andrew's commentary priority

**Why.** Andrew-direct ~22:2xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_222xZ_TRNSPT_FOCUS_AI_COMMENTARY_PARK_ANALYST_ACCESS.md`
@a4fdb78bbe): "the bigger pint of the TRNSPT process currently is getting the \"ai investment commentary\" sorted out for the ycharts
workflow". NFRA_TRNSPT FWD-10's hop H5 (C-TICKET) is this project's **FWD-6**, unchanged in substance. It moves from backlog item 4 to
now.

**Scope:** a separate workstream, so round 1's frozen decomposition (TV-r-1) is untouched. It has a disjoint write surface.
- The H5 contract with NFRA_TRNSPT is `FWD10_H6_H5_TICKET_WRITE_CONTRACT.md` @a8410fcca3. It is a draft until both sides commit it.
- **Missing today:**
  - a `svc-commentary` principal allowed CREATE only, on the `analysis_request` type, with no read, update or close;
  - the `draft_commentary` and `report_request_id` fields on the type definition (C-TYPE: data, not code);
  - the 08-12 security read of the write path.
- **Not here:** minting the `svc-commentary` token. That follows the `svc-analyst-intake` precedent (issuer TO-D, laptop) and is routed
  cross-fabric.

**ENDPOINT and CONTRACTS are unchanged** (FWD-6 as written). This is a sequencing addendum and re-opens no half.

-- 1.0.0_SA_CTO~DELL2

